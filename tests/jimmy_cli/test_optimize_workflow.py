"""Task catalog, fake runner, candidate workflow, and context-cost diagnosis."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from jimmy_cli.optimize.candidate import (
    CandidateOverlay,
    TaskSetMismatchError,
    compare_runs,
    decide_keep_candidate,
    run_candidate_workflow,
)
from jimmy_cli.optimize.context_cost import diagnose_folder_summarize_cost
from jimmy_cli.optimize.runner import AgentRunner, FakeRunner, run_benchmark
from jimmy_cli.optimize.search import built_in_search_catalog, run_search_workflow
from jimmy_cli.optimize.tasks import (
    TASK_CATEGORIES,
    get_task,
    list_tasks,
)


REQUIRED_CATEGORIES = {
    "qa",
    "coding",
    "debugging",
    "repo_exploration",
    "file_manipulation",
    "multi_step_tools",
}


def test_at_least_twenty_tasks_cover_required_categories():
    tasks = list_tasks()
    assert len(tasks) >= 20
    cats = {t.category for t in tasks}
    assert REQUIRED_CATEGORIES <= cats
    assert set(TASK_CATEGORIES) >= REQUIRED_CATEGORIES
    for t in tasks:
        assert t.id
        assert t.prompt
        assert t.expected_max_llm_turns >= 1
        assert t.max_useful_completion_tokens > 0


def test_fake_runner_is_deterministic_and_offline(tmp_path, monkeypatch):
    jimmy_home = tmp_path / "home"
    workspace = tmp_path / "ws"
    jimmy_home.mkdir()
    workspace.mkdir()
    monkeypatch.setenv("JIMMY_HOME", str(jimmy_home))

    runner = FakeRunner()
    tasks = list_tasks()[:5]
    result = run_benchmark(
        tasks=tasks,
        runner=runner,
        workspace=workspace,
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "artifacts",
        run_id="baseline",
    )
    assert result.run_id == "baseline"
    assert len(result.task_results) == 5
    result2 = run_benchmark(
        tasks=tasks,
        runner=runner,
        workspace=workspace,
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "artifacts2",
        run_id="baseline2",
    )
    scores1 = {r.task_id: r.score for r in result.task_results}
    scores2 = {r.task_id: r.score for r in result2.task_results}
    assert scores1 == scores2
    summary = tmp_path / "artifacts" / "baseline" / "summary.json"
    assert summary.is_file()
    data = json.loads(summary.read_text(encoding="utf-8"))
    assert data["run_id"] == "baseline"
    assert "prompt_breakdown" in data
    events = tmp_path / "artifacts" / "baseline" / "events.jsonl"
    assert events.is_file()
    # Trajectories include messages + request_metrics
    task_json = tmp_path / "artifacts" / "baseline" / "tasks" / f"{tasks[0].id}.json"
    payload = json.loads(task_json.read_text(encoding="utf-8"))
    assert "messages" in payload and payload["messages"]
    assert "request_metrics" in payload


def test_candidate_kept_only_when_aggregate_improves(tmp_path):
    baseline = {
        "task_scores": {"a": 90.0, "b": 80.0},
        "total": 170.0,
    }
    worse = {
        "task_scores": {"a": 88.0, "b": 80.0},
        "total": 168.0,
    }
    better = {
        "task_scores": {"a": 95.0, "b": 80.0},
        "total": 175.0,
    }
    cmp_worse = compare_runs(baseline, worse)
    assert cmp_worse["improved"] is False
    assert decide_keep_candidate(cmp_worse) is False

    cmp_better = compare_runs(baseline, better)
    assert cmp_better["improved"] is True
    assert decide_keep_candidate(cmp_better) is True


def test_compare_runs_fail_closed_on_task_set_mismatch():
    baseline = {"task_scores": {"a": 10.0, "b": 20.0}, "total": 30.0}
    missing = {"task_scores": {"a": 10.0}, "total": 10.0}
    with pytest.raises(TaskSetMismatchError, match="missing_from_candidate"):
        compare_runs(baseline, missing)
    extra = {"task_scores": {"a": 10.0, "b": 20.0, "c": 0.0}, "total": 30.0}
    with pytest.raises(TaskSetMismatchError, match="extra_in_candidate"):
        compare_runs(baseline, extra)


def test_noop_overlay_rejected_but_simulation_improves(tmp_path, monkeypatch):
    jimmy_home = tmp_path / "home"
    workspace = tmp_path / "ws"
    jimmy_home.mkdir()
    workspace.mkdir()
    (jimmy_home / "config.yaml").write_text("model:\n  default: fake\n", encoding="utf-8")
    monkeypatch.setenv("JIMMY_HOME", str(jimmy_home))
    tasks = list_tasks()

    noop = run_candidate_workflow(
        tasks=tasks,
        runner=FakeRunner(),
        workspace=workspace / "noop",
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "noop_out",
        candidate_overlay={"display": {"tool_progress": "off"}},
        dry_run=True,
        candidate_simulation=None,
    )
    assert noop["kept"] is False
    assert noop["comparison"]["delta_total"] == 0.0

    improved = run_candidate_workflow(
        tasks=tasks,
        runner=FakeRunner(),
        workspace=workspace / "sim",
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "sim_out",
        candidate_overlay={"agent": {"max_turns": 60}},
        dry_run=True,
        candidate_simulation="lean_tool_use",
    )
    assert improved["kept"] is True
    assert improved["comparison"]["delta_total"] > 0
    assert improved["candidate_simulation"] == "lean_tool_use"


def test_overlay_is_reversible_and_never_edits_core(tmp_path):
    home = tmp_path / ".jimmy"
    home.mkdir()
    config = home / "config.yaml"
    config.write_text("model:\n  default: base-model\n", encoding="utf-8")
    overlay = CandidateOverlay(
        jimmy_home=home,
        changes={"agent": {"max_iterations": 8}},
    )
    with overlay.apply() as applied:
        assert applied.config_path == config
        text = config.read_text(encoding="utf-8")
        assert "max_iterations" in text
        assert not (tmp_path / "run_agent.py").exists()
    restored = config.read_text(encoding="utf-8")
    assert "max_iterations" not in restored
    assert "base-model" in restored


def test_dry_run_offline_fixture_workflow(tmp_path, monkeypatch):
    jimmy_home = tmp_path / "home"
    workspace = tmp_path / "ws"
    jimmy_home.mkdir()
    workspace.mkdir()
    (jimmy_home / "config.yaml").write_text("model:\n  default: fake\n", encoding="utf-8")
    monkeypatch.setenv("JIMMY_HOME", str(jimmy_home))

    report = run_candidate_workflow(
        tasks=list_tasks()[:3],
        runner=FakeRunner(),
        workspace=workspace,
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "out",
        candidate_overlay={"display": {"tool_progress": "off"}},
        dry_run=True,
    )
    assert report["mode"] == "dry_run"
    assert report["kept"] is False
    assert "comparison" in report
    assert (tmp_path / "out" / "comparison.json").is_file()


def test_search_dry_run_has_one_win_and_rejections(tmp_path, monkeypatch):
    jimmy_home = tmp_path / "home"
    workspace = tmp_path / "ws"
    jimmy_home.mkdir()
    workspace.mkdir()
    (jimmy_home / "config.yaml").write_text("model:\n  default: fake\n", encoding="utf-8")
    monkeypatch.setenv("JIMMY_HOME", str(jimmy_home))
    monkeypatch.chdir(tmp_path)

    # Small catalog: one noop reject + one simulated win (keeps the test fast).
    from jimmy_cli.optimize.search import SearchCandidate

    catalog = [
        SearchCandidate(
            id="noop_empty_overlay",
            axis="guidance",
            description="Empty overlay control",
            overlay={},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="turn_policy_lean_fixture_win",
            axis="turn_policy",
            description="Lean simulation win",
            overlay={"agent": {"max_turns": 60}},
            offline_simulation="lean_tool_use",
        ),
    ]
    tasks = list_tasks(categories=["coding", "multi_step_tools"])
    report = run_search_workflow(
        tasks=tasks,
        runner=FakeRunner(),
        workspace=workspace,
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "search",
        dry_run=True,
        catalog=catalog,
    )
    assert report["mode"] == "dry_run"
    assert any(c["improved"] for c in report["candidates"])
    assert any(not c["improved"] for c in report["candidates"])
    assert report["kept_winner"] is True
    assert report["winner"]["id"] == "turn_policy_lean_fixture_win"
    assert (tmp_path / "search" / "search_report.json").is_file()
    axes = {c.axis for c in built_in_search_catalog()}
    assert "context" in axes and "turn_policy" in axes and "tool_schemas" in axes


def test_folder_summarize_context_cost_includes_tiers(tmp_path, monkeypatch):
    jimmy_home = tmp_path / ".jimmy"
    jimmy_home.mkdir()
    monkeypatch.setenv("JIMMY_HOME", str(jimmy_home))
    monkeypatch.chdir(tmp_path)
    (tmp_path / "AGENTS.md").write_text("# Agents\nnotes\n", encoding="utf-8")

    diagnosis = diagnose_folder_summarize_cost(platform="cli")
    assert diagnosis["prompt"] == "Summarize what is in this folder"
    assert "prompt_breakdown" in diagnosis
    pb = diagnosis["prompt_breakdown"]
    assert "sections" in pb
    assert "skills_index" in pb
    assert "tools" in pb
    assert diagnosis["first_turn_fixed_bytes"] == (
        pb["system_prompt"]["bytes"] + pb["tools"]["json_bytes"]
    )
    assert "report" in diagnosis


def test_agent_runner_uses_runtime_resolution_not_missing_sentinel(monkeypatch):
    """Without OPENROUTER_API_KEY, AgentRunner must not pass api_key='missing'."""
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    captured = {}

    def fake_resolve(**kwargs):
        captured["resolve_kwargs"] = kwargs
        return {
            "api_key": "resolved-from-runtime",
            "base_url": "https://example.test/v1",
            "provider": "custom",
            "requested_provider": "custom",
            "api_mode": "chat_completions",
        }

    monkeypatch.setattr(
        "jimmy_cli.runtime_provider.resolve_runtime_provider",
        fake_resolve,
    )
    runner = AgentRunner(platform="cli")
    kwargs = runner.build_agent_kwargs()
    assert kwargs.get("api_key") == "resolved-from-runtime"
    assert kwargs.get("api_key") != "missing"
    assert "missing" not in str(kwargs.get("api_key"))
    assert kwargs.get("base_url") == "https://example.test/v1"
    assert "resolve_kwargs" in captured


def test_agent_runner_passes_explicit_credentials_only_when_supplied(monkeypatch):
    def boom(**_kwargs):
        raise AssertionError("resolve_runtime_provider should not run when explicit")

    monkeypatch.setattr(
        "jimmy_cli.runtime_provider.resolve_runtime_provider",
        boom,
    )
    runner = AgentRunner(
        model="my-model",
        api_key="explicit-key",
        base_url="https://explicit.test/v1",
        provider="custom",
    )
    kwargs = runner.build_agent_kwargs()
    assert kwargs["api_key"] == "explicit-key"
    assert kwargs["base_url"] == "https://explicit.test/v1"
    assert kwargs["model"] == "my-model"
    assert kwargs["provider"] == "custom"


def test_azure_like_runtime_resolved_before_isolated_jimmy_home(tmp_path, monkeypatch):
    """Live optimize must resolve provider/model under the active home, not isolated.

    Repro class: isolated JIMMY_HOME seeded with model.default=optimize-harness
    caused AgentRunner to resolve after the switch and send azure-foundry with an
    empty/wrong deployment (HTTP 400 Missed model deployment).
    """
    import os

    from jimmy_cli.optimize.runner import (
        AgentRunner,
        resolve_optimize_runtime,
        seed_isolated_jimmy_home,
    )

    active = tmp_path / "active_home"
    isolated = tmp_path / "isolated_home"
    active.mkdir()
    isolated.mkdir()
    (active / "config.yaml").write_text(
        "model:\n"
        "  provider: azure-foundry\n"
        "  default: gpt-5.6-sol\n"
        "  base_url: https://example.openai.azure.com/openai/v1\n"
        "  api_mode: chat_completions\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("JIMMY_HOME", str(active))

    resolve_homes: list[str] = []

    def fake_resolve(**kwargs):
        resolve_homes.append(os.environ.get("JIMMY_HOME") or "")
        assert kwargs.get("target_model") in (None, "", "gpt-5.6-sol")
        return {
            "api_key": "azure-test-key",
            "base_url": "https://example.openai.azure.com/openai/v1",
            "provider": "azure-foundry",
            "requested_provider": "azure-foundry",
            "api_mode": "chat_completions",
            "model": "gpt-5.6-sol",
        }

    monkeypatch.setattr(
        "jimmy_cli.runtime_provider.resolve_runtime_provider",
        fake_resolve,
    )

    runtime = resolve_optimize_runtime(platform="cli")
    assert resolve_homes == [str(active)]
    assert runtime["model"] == "gpt-5.6-sol"
    assert runtime["provider"] == "azure-foundry"
    assert runtime["api_key"] == "azure-test-key"
    assert "azure-test-key" not in str(runtime.get("safe_model_config") or {})

    seed_isolated_jimmy_home(isolated, runtime=runtime)
    seeded = (isolated / "config.yaml").read_text(encoding="utf-8")
    assert "gpt-5.6-sol" in seeded
    assert "azure-foundry" in seeded
    assert "azure-test-key" not in seeded
    assert "api_key" not in seeded.lower()

    # Simulate run_benchmark switching JIMMY_HOME to the isolated tree.
    monkeypatch.setenv("JIMMY_HOME", str(isolated))
    # Poison isolated resolution: if AgentRunner re-resolves here, model is lost.
    def boom_resolve(**_kwargs):
        raise AssertionError(
            "AgentRunner must not re-resolve after isolated JIMMY_HOME switch"
        )

    monkeypatch.setattr(
        "jimmy_cli.runtime_provider.resolve_runtime_provider",
        boom_resolve,
    )
    runner = AgentRunner.from_resolved_runtime(runtime, platform="cli")
    kwargs = runner.build_agent_kwargs()
    assert kwargs.get("model") == "gpt-5.6-sol"
    assert kwargs.get("provider") == "azure-foundry"
    assert kwargs.get("api_key") == "azure-test-key"
    assert kwargs.get("base_url") == "https://example.openai.azure.com/openai/v1"
    assert kwargs.get("api_mode") == "chat_completions"


def test_agent_runner_marks_failed_aiagent_http_error(tmp_path, monkeypatch):
    """AIAgent failed/HTTP errors must be clearly failed tasks, not soft check misses."""
    from jimmy_cli.optimize.observer import OptimizeObserver
    from jimmy_cli.optimize.tasks import get_task

    class FakeAgent:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def run_conversation(self, _prompt):
            return {
                "final_response": "Error: HTTP 400: Missed model deployment",
                "messages": [{"role": "user", "content": "x"}],
                "completed": False,
                "failed": True,
                "error": "HTTP 400: Missed model deployment",
            }

    monkeypatch.setattr("run_agent.AIAgent", FakeAgent)
    task = get_task("qa_capital_france")
    workspace = tmp_path / "ws"
    workspace.mkdir()
    observer = OptimizeObserver()
    observer.enable(run_id="fail-check", attribution="parent")
    runner = AgentRunner(
        model="gpt-5.6-sol",
        api_key="k",
        base_url="https://example.openai.azure.com/openai/v1",
        provider="azure-foundry",
        api_mode="chat_completions",
        skip_runtime_resolve=True,
    )
    result = runner.run_task(task, workspace, observer=observer)
    assert result.success is False
    assert result.detail.startswith("agent_failed:")
    assert "400" in result.detail or "Missed model deployment" in result.detail


def test_cmd_optimize_exits_nonzero_when_benchmark_cannot_execute(tmp_path, monkeypatch):
    """Live benchmark that cannot execute any task must not exit 0 looking healthy."""
    from types import SimpleNamespace

    from jimmy_cli.optimize.cli import cmd_optimize
    from jimmy_cli.optimize.runner import RunResult, TaskRunResult

    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "active"))
    (tmp_path / "active").mkdir()
    (tmp_path / "active" / "config.yaml").write_text(
        "model:\n  provider: azure-foundry\n  default: gpt-5.6-sol\n",
        encoding="utf-8",
    )

    def fake_resolve(**_kwargs):
        return {
            "api_key": "k",
            "base_url": "https://example.openai.azure.com/openai/v1",
            "provider": "azure-foundry",
            "requested_provider": "azure-foundry",
            "api_mode": "chat_completions",
            "model": "gpt-5.6-sol",
        }

    monkeypatch.setattr(
        "jimmy_cli.runtime_provider.resolve_runtime_provider",
        fake_resolve,
    )

    def fake_benchmark(**_kwargs):
        return RunResult(
            run_id="benchmark",
            task_results=[
                TaskRunResult(
                    task_id="qa_capital_france",
                    success=False,
                    score=0.0,
                    llm_turns=0,
                    tool_calls=0,
                    completion_tokens=0,
                    detail="agent_failed: HTTP 400: Missed model deployment",
                )
            ],
        )

    monkeypatch.setattr("jimmy_cli.optimize.cli.run_benchmark", fake_benchmark)
    args = SimpleNamespace(
        optimize_command="benchmark",
        dry_run=False,
        offline=False,
        category=None,
        tasks="qa_capital_france",
        out=str(tmp_path / "out"),
        workspace=None,
        jimmy_home=None,
        artifact_dir=None,
        run_id="benchmark",
        platform="cli",
        model="",
        api_key=None,
        base_url=None,
        provider=None,
        simulation=None,
        overlay=None,
        overlay_file=None,
        json=False,
    )
    rc = cmd_optimize(args)
    assert rc == 1
    seeded = Path(tmp_path / "out" / "jimmy_home" / "config.yaml")
    assert seeded.is_file()
    text = seeded.read_text(encoding="utf-8")
    assert "gpt-5.6-sol" in text
    assert "azure-foundry" in text
    assert "api_key" not in text.lower()
    assert "azure-test-key" not in text
    assert "\nk\n" not in text and ": k\n" not in text and ": k" not in text


def test_run_benchmark_restores_jimmy_home_and_cwd(tmp_path, monkeypatch):
    import os

    jimmy_home = tmp_path / "home"
    workspace = tmp_path / "ws"
    jimmy_home.mkdir()
    workspace.mkdir()
    orig_home = os.environ.get("JIMMY_HOME")
    orig_cwd = os.getcwd()
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "outer"))
    run_benchmark(
        tasks=list_tasks()[:1],
        runner=FakeRunner(),
        workspace=workspace,
        jimmy_home=jimmy_home,
        artifact_dir=tmp_path / "art",
        run_id="restore-check",
    )
    assert os.getcwd() == orig_cwd
    assert os.environ.get("JIMMY_HOME") == str(tmp_path / "outer")
    if orig_home is None:
        pass  # restored to outer set by monkeypatch


def test_get_task_lookup():
    t = get_task(list_tasks()[0].id)
    assert t.id == list_tasks()[0].id
