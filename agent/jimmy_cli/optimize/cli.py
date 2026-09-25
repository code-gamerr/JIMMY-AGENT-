"""CLI implementation for ``jimmy optimize``."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from jimmy_cli.optimize.candidate import run_candidate_workflow
from jimmy_cli.optimize.context_cost import diagnose_folder_summarize_cost
from jimmy_cli.optimize.report import write_offline_fixture_report
from jimmy_cli.optimize.runner import (
    AgentRunner,
    FakeRunner,
    RunResult,
    resolve_optimize_runtime,
    run_benchmark,
    seed_isolated_jimmy_home,
)
from jimmy_cli.optimize.search import run_search_workflow
from jimmy_cli.optimize.tasks import list_tasks


def _resolve_tasks(args: Any) -> List:
    categories = None
    if getattr(args, "category", None):
        categories = [c.strip() for c in str(args.category).split(",") if c.strip()]
    task_ids = None
    if getattr(args, "tasks", None):
        task_ids = [t.strip() for t in str(args.tasks).split(",") if t.strip()]
    return list_tasks(categories=categories, task_ids=task_ids)


def _load_overlay(args: Any) -> Dict[str, Any]:
    raw = getattr(args, "overlay", None) or "{}"
    path = getattr(args, "overlay_file", None)
    if path:
        text = Path(path).read_text(encoding="utf-8")
        if str(path).endswith((".yaml", ".yml")):
            import yaml

            data = yaml.safe_load(text) or {}
        else:
            data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError("overlay file must contain a mapping")
        return data
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("--overlay must be a JSON object")
    return data


def _is_dry_run(args: Any) -> bool:
    return bool(getattr(args, "dry_run", False) or getattr(args, "offline", False))


def _make_runner(args: Any, *, runtime: Optional[Dict[str, Any]] = None):
    if _is_dry_run(args):
        sim = getattr(args, "simulation", None) or None
        return FakeRunner(simulation=sim)
    if runtime is not None:
        return AgentRunner.from_resolved_runtime(
            runtime,
            platform=getattr(args, "platform", "cli") or "cli",
        )
    # Fallback: resolve now (caller should prefer pre-isolation resolve).
    resolved = resolve_optimize_runtime(
        model=getattr(args, "model", "") or "",
        api_key=getattr(args, "api_key", None),
        base_url=getattr(args, "base_url", None),
        provider=getattr(args, "provider", None),
        platform=getattr(args, "platform", "cli") or "cli",
    )
    return AgentRunner.from_resolved_runtime(
        resolved,
        platform=getattr(args, "platform", "cli") or "cli",
    )


def _paths(args: Any):
    root = Path(getattr(args, "out", None) or (Path.cwd() / "optimize-out"))
    root.mkdir(parents=True, exist_ok=True)
    workspace = Path(getattr(args, "workspace", None) or (root / "workspaces"))
    jimmy_home = Path(getattr(args, "jimmy_home", None) or (root / "jimmy_home"))
    artifacts = Path(getattr(args, "artifact_dir", None) or (root / "artifacts"))
    return root, workspace, jimmy_home, artifacts


def _benchmark_cannot_execute(result: RunResult) -> bool:
    """True when every task failed to run the agent (not merely check_failed)."""
    if not result.task_results:
        return True
    return all(
        (not r.success) and str(r.detail or "").startswith("agent_failed:")
        for r in result.task_results
    )


def cmd_optimize(args: Any) -> Optional[int]:
    """Entry point for ``jimmy optimize``.

    Returns a process exit code (``1`` when a live benchmark cannot execute).
    """
    command = getattr(args, "optimize_command", None) or "benchmark"

    if command == "list-tasks":
        tasks = _resolve_tasks(args)
        for t in tasks:
            print(f"{t.id:28}  {t.category:18}  {t.prompt[:60]}")
        print(f"\n{len(tasks)} tasks")
        return 0

    if command == "diagnose-context":
        diagnosis = diagnose_folder_summarize_cost(
            platform=getattr(args, "platform", "cli") or "cli"
        )
        if getattr(args, "json", False):
            payload = dict(diagnosis)
            print(json.dumps(payload, ensure_ascii=False, indent=2, default=str))
        else:
            print(diagnosis["report"])
        return 0

    if command == "report-offline":
        out = Path(
            getattr(args, "out", None)
            or (Path.cwd() / "docs" / "optimizer" / "OFFLINE_FIXTURE_REPORT.md")
        )
        path = write_offline_fixture_report(out_path=out)
        print(f"Wrote OFFLINE FIXTURE report: {path}")
        return 0

    tasks = _resolve_tasks(args)
    if not tasks:
        print("No tasks selected.")
        return 1

    dry_run = _is_dry_run(args)
    platform = getattr(args, "platform", "cli") or "cli"

    # Resolve live credentials against the *active* JIMMY_HOME before creating
    # / switching into the isolated optimize tree.
    runtime: Optional[Dict[str, Any]] = None
    if not dry_run:
        runtime = resolve_optimize_runtime(
            model=getattr(args, "model", "") or "",
            api_key=getattr(args, "api_key", None),
            base_url=getattr(args, "base_url", None),
            provider=getattr(args, "provider", None),
            platform=platform,
        )

    _, workspace, jimmy_home, artifacts = _paths(args)
    jimmy_home.mkdir(parents=True, exist_ok=True)
    seed_isolated_jimmy_home(jimmy_home, runtime=runtime)

    runner = _make_runner(args, runtime=runtime)

    if command == "benchmark":
        result = run_benchmark(
            tasks=tasks,
            runner=runner,
            workspace=workspace / "benchmark",
            jimmy_home=jimmy_home,
            artifact_dir=artifacts,
            run_id=getattr(args, "run_id", None) or "benchmark",
            platform=platform,
        )
        success_n = sum(1 for r in result.task_results if r.success)
        print(
            f"Benchmark complete: {success_n}/{len(result.task_results)} success, "
            f"total_score={result.total_score:.2f}"
        )
        print(f"Artifacts: {result.artifact_dir}")
        if not dry_run and _benchmark_cannot_execute(result):
            print(
                "Benchmark could not execute: every task failed at the agent/API "
                "layer (see task details). Exiting non-zero."
            )
            return 1
        return 0

    if command == "candidate":
        overlay = _load_overlay(args)
        report = run_candidate_workflow(
            tasks=tasks,
            runner=runner,
            workspace=workspace / "candidate_wf",
            jimmy_home=jimmy_home,
            artifact_dir=artifacts / "candidate_wf",
            candidate_overlay=overlay,
            dry_run=dry_run,
            platform=platform,
            candidate_simulation=getattr(args, "simulation", None) or None,
        )
        cmp_ = report["comparison"]
        verdict = "KEEP" if report["kept"] else "REJECT"
        print(
            f"Candidate {verdict}: baseline={cmp_['baseline_total']:.2f} "
            f"candidate={cmp_['candidate_total']:.2f} "
            f"delta={cmp_['delta_total']:+.2f} mode={report['mode']}"
        )
        print(f"Report: {artifacts / 'candidate_wf' / 'comparison.json'}")
        return 0

    if command == "search":
        report = run_search_workflow(
            tasks=tasks,
            runner=runner,
            workspace=workspace / "search_wf",
            jimmy_home=jimmy_home,
            artifact_dir=artifacts / "search_wf",
            dry_run=dry_run,
            platform=platform,
        )
        winner = report.get("winner")
        if winner and report.get("kept_winner"):
            print(
                f"Search KEEP winner={winner['id']} "
                f"delta={winner['delta_total']:+.2f} axis={winner['axis']}"
            )
        else:
            print("Search: no improving candidate kept.")
        print(f"Report: {artifacts / 'search_wf' / 'search_report.json'}")
        return 0

    print(f"Unknown optimize command: {command}")
    return 1
