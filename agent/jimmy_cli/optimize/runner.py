"""Benchmark runners for harness optimize (fake/offline + real AIAgent).

``run_benchmark`` mutates process-global ``JIMMY_HOME`` and may change cwd
via AgentRunner. It is therefore single-thread orchestration only: a process
lock rejects concurrent callers, and both env + cwd are restored in ``finally``.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Protocol, Sequence

from jimmy_cli.optimize.artifacts import ensure_run_dir, write_events, write_summary
from jimmy_cli.optimize.observer import OptimizeObserver
from jimmy_cli.optimize.scoring import ScoreComponents, compute_score
from jimmy_cli.optimize.simulation import (
    SimulationProfile,
    apply_simulation_overrides,
    get_simulation,
)
from jimmy_cli.optimize.tasks import OptimizeTask

# Single-thread orchestration guard for process-global JIMMY_HOME / cwd.
_BENCHMARK_LOCK = threading.RLock()
_BENCHMARK_HELD = False


class BenchmarkBusyError(RuntimeError):
    """Raised when run_benchmark is already active in this process."""


@dataclass
class TaskRunResult:
    task_id: str
    success: bool
    score: float
    llm_turns: int
    tool_calls: int
    completion_tokens: int
    input_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    response: str = ""
    detail: str = ""
    attribution_summary: Dict[str, int] = field(default_factory=dict)
    events: List[Dict[str, Any]] = field(default_factory=list)
    messages: List[Dict[str, Any]] = field(default_factory=list)
    request_metrics: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class RunResult:
    run_id: str
    task_results: List[TaskRunResult]
    prompt_breakdown: Dict[str, Any] = field(default_factory=dict)
    artifact_dir: Optional[Path] = None

    @property
    def task_scores(self) -> Dict[str, float]:
        return {r.task_id: r.score for r in self.task_results}

    @property
    def total_score(self) -> float:
        return sum(self.task_scores.values())


class TaskRunner(Protocol):
    def run_task(
        self,
        task: OptimizeTask,
        workspace: Path,
        *,
        observer: OptimizeObserver,
    ) -> TaskRunResult: ...


_SECRET_KEY_RE = re.compile(
    r"(api[_-]?key|authorization|access[_-]?token|secret|password|bearer)",
    re.IGNORECASE,
)
_SECRET_VALUE_RE = re.compile(
    r"(?i)(sk-[a-z0-9]{8,}|Bearer\s+\S+|api[_-]?key[=:\s]+\S+)"
)


def redact_secrets(value: Any) -> Any:
    """Recursively redact secret-looking keys/values from trajectory payloads."""
    if isinstance(value, dict):
        out: Dict[str, Any] = {}
        for k, v in value.items():
            key = str(k)
            if _SECRET_KEY_RE.search(key):
                out[key] = "[REDACTED]"
            else:
                out[key] = redact_secrets(v)
        return out
    if isinstance(value, list):
        return [redact_secrets(v) for v in value]
    if isinstance(value, str):
        if _SECRET_VALUE_RE.search(value):
            return _SECRET_VALUE_RE.sub("[REDACTED]", value)
        return value
    return value


def sanitize_messages(messages: Sequence[Any]) -> List[Dict[str, Any]]:
    """Keep role/content/tool_calls structure; never include raw API payloads."""
    cleaned: List[Dict[str, Any]] = []
    for msg in messages or []:
        if not isinstance(msg, dict):
            continue
        entry: Dict[str, Any] = {}
        for key in (
            "role",
            "content",
            "name",
            "tool_call_id",
            "tool_calls",
            "finish_reason",
        ):
            if key in msg:
                entry[key] = redact_secrets(msg[key])
        # Drop reasoning/raw provider blobs that may embed secrets.
        cleaned.append(entry)
    return cleaned


def request_metrics_from_llm_events(
    events: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    """Compact per-request metrics without request/response bodies."""
    metrics: List[Dict[str, Any]] = []
    for ev in events:
        if not isinstance(ev, dict):
            continue
        metrics.append(
            {
                "turn_number": ev.get("turn_number"),
                "finish_reason": ev.get("finish_reason"),
                "input_tokens": ev.get("input_tokens"),
                "output_tokens": ev.get("output_tokens"),
                "completion_tokens": ev.get("completion_tokens"),
                "cache_read_tokens": ev.get("cache_read_tokens"),
                "cache_write_tokens": ev.get("cache_write_tokens"),
                "tool_call_count": ev.get("tool_call_count"),
                "api_duration_s": ev.get("api_duration_s"),
                "attribution": ev.get("attribution"),
                "model": ev.get("model"),
                "provider": ev.get("provider"),
            }
        )
    return metrics


class FakeRunner:
    """Deterministic offline runner — no network, no AIAgent.

    Optional ``simulation`` (name or SimulationProfile) applies an *explicit*
    named fixture profile so candidate dry-runs can demonstrate improvement.
    Without a simulation, metrics match the task definitions (no-op overlays
    correctly fail to improve).
    """

    def __init__(
        self,
        *,
        simulation: Optional[str | SimulationProfile] = None,
    ) -> None:
        if isinstance(simulation, SimulationProfile):
            self.simulation: Optional[SimulationProfile] = simulation
        else:
            self.simulation = get_simulation(simulation)

    def run_task(
        self,
        task: OptimizeTask,
        workspace: Path,
        *,
        observer: OptimizeObserver,
    ) -> TaskRunResult:
        _seed_workspace(task, workspace)
        metrics = apply_simulation_overrides(
            task_id=task.id,
            fake_success=bool(task.fake_success),
            fake_llm_turns=int(task.fake_llm_turns),
            fake_tool_calls=int(task.fake_tool_calls),
            fake_completion_tokens=int(task.fake_completion_tokens),
            simulation=self.simulation,
        )
        # Apply deterministic file side-effects for tasks the fake "succeeds".
        if metrics["fake_success"]:
            _apply_fake_side_effects(task, workspace)

        response = _fake_response_for(task)
        success = bool(metrics["fake_success"])
        detail = "fake_ok" if success else "fake_fail"
        if task.check is not None:
            try:
                checked = bool(task.check(response, workspace, {"fake": True}))
            except Exception as exc:
                success = False
                detail = f"check_error: {exc}"
            else:
                if success and not checked:
                    success = False
                    detail = "fake_check_failed"
                elif not success and checked:
                    detail = "fake_fail_but_check_passed"

        llm_turns = int(metrics["fake_llm_turns"])
        tool_calls = int(metrics["fake_tool_calls"])
        completion_tokens = int(metrics["fake_completion_tokens"])
        input_tokens = 800 + len(task.prompt)

        for i in range(1, llm_turns + 1):
            observer.observe_lifecycle(
                "post_api_request",
                session_id=f"fake-{task.id}",
                api_call_count=i,
                finish_reason="tool_calls" if i < llm_turns else "stop",
                usage={
                    "prompt_tokens": input_tokens,
                    "completion_tokens": max(1, completion_tokens // max(llm_turns, 1)),
                    "input_tokens": input_tokens,
                    "output_tokens": max(1, completion_tokens // max(llm_turns, 1)),
                    "cache_read_tokens": int(input_tokens * 0.7) if i > 1 else 0,
                    "cache_write_tokens": 40 if i == 1 else 0,
                },
                assistant_tool_call_count=1 if i < llm_turns else 0,
                api_duration=0.01,
            )
        for j in range(tool_calls):
            observer.observe_lifecycle(
                "post_tool_call",
                tool_name="terminal",
                duration_ms=1 + j,
                task_id=f"fake-{task.id}",
                success=True,
            )

        observer.mark_task_result(task.id, success, detail)
        score = compute_score(
            ScoreComponents(
                success=success,
                completion_tokens=completion_tokens,
                llm_turns=llm_turns,
                tool_calls=tool_calls,
                expected_max_llm_turns=task.expected_max_llm_turns,
                expected_max_tool_calls=task.expected_max_tool_calls,
                max_useful_completion_tokens=task.max_useful_completion_tokens,
            )
        )
        llm_events = observer.slice_llm_calls(max(0, observer.llm_call_count() - llm_turns))
        tool_events = observer.slice_tool_calls(
            max(0, observer.tool_call_count() - tool_calls)
        )
        messages = [
            {"role": "user", "content": task.prompt},
            {"role": "assistant", "content": response},
        ]
        return TaskRunResult(
            task_id=task.id,
            success=success,
            score=score,
            llm_turns=llm_turns,
            tool_calls=tool_calls,
            completion_tokens=completion_tokens,
            input_tokens=input_tokens,
            response=response,
            detail=detail,
            events=list(llm_events) + list(tool_events),
            messages=messages,
            request_metrics=request_metrics_from_llm_events(llm_events),
        )


def _config_model_default() -> str:
    """Read ``model.default`` from the *current* JIMMY_HOME config (non-secret)."""
    try:
        from jimmy_cli.config import load_config

        cfg = load_config()
    except Exception:
        return ""
    model_cfg = cfg.get("model") if isinstance(cfg, dict) else None
    if isinstance(model_cfg, dict):
        default = model_cfg.get("default")
        if isinstance(default, dict):
            try:
                from jimmy_cli.config import split_model_config_default

                name, _provider = split_model_config_default(default)
                return str(name or "").strip()
            except Exception:
                return str(default.get("model") or "").strip()
        return str(default or model_cfg.get("model") or "").strip()
    if isinstance(model_cfg, str):
        return model_cfg.strip()
    return ""


def resolve_optimize_runtime(
    *,
    model: str = "",
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    provider: Optional[str] = None,
    platform: str = "cli",
) -> Dict[str, Any]:
    """Resolve live provider/model credentials against the *active* JIMMY_HOME.

    Must be called **before** ``run_benchmark`` switches ``JIMMY_HOME`` to the
    isolated optimize tree. Returns both the full runtime (for AgentRunner) and
    a safe non-secret ``safe_model_config`` suitable for seeding isolated
    ``config.yaml`` (never includes api keys / tokens).
    """
    del platform  # reserved for future platform-scoped resolution
    from jimmy_cli.runtime_provider import resolve_runtime_provider

    explicit_model = (model or "").strip()
    explicit_key = api_key
    explicit_base = (base_url or "").strip() or None
    explicit_provider = (provider or "").strip() or None

    runtime = resolve_runtime_provider(
        requested=explicit_provider,
        explicit_api_key=explicit_key if isinstance(explicit_key, str) else None,
        explicit_base_url=explicit_base,
        target_model=explicit_model or None,
    )

    resolved_model = explicit_model
    if not resolved_model:
        raw = runtime.get("model")
        if isinstance(raw, str) and raw.strip():
            resolved_model = raw.strip()
    if not resolved_model:
        resolved_model = _config_model_default()

    resolved_provider = (
        explicit_provider
        or (str(runtime.get("provider") or "").strip() or None)
        or (str(runtime.get("requested_provider") or "").strip() or None)
    )
    resolved_key = runtime.get("api_key")
    if explicit_key is not None and not (
        isinstance(explicit_key, str) and not explicit_key.strip()
    ):
        # Honour CLI --api-key (string) or pre-built callable token providers.
        resolved_key = explicit_key
    resolved_base = explicit_base or (str(runtime.get("base_url") or "").strip() or None)

    safe_model_config: Dict[str, Any] = {}
    if resolved_model:
        safe_model_config["default"] = resolved_model
    if resolved_provider:
        safe_model_config["provider"] = resolved_provider
    api_mode = runtime.get("api_mode")
    if isinstance(api_mode, str) and api_mode.strip():
        safe_model_config["api_mode"] = api_mode.strip()
    # base_url is an endpoint identity, not a credential — useful for overlays
    # / prompt diagnosis under the isolated home without re-resolving secrets.
    if resolved_base:
        safe_model_config["base_url"] = resolved_base

    return {
        "model": resolved_model,
        "api_key": resolved_key,
        "base_url": resolved_base,
        "provider": resolved_provider,
        "requested_provider": runtime.get("requested_provider") or resolved_provider,
        "api_mode": runtime.get("api_mode"),
        "command": runtime.get("command"),
        "args": runtime.get("args"),
        "credential_pool": runtime.get("credential_pool"),
        "auth_mode": runtime.get("auth_mode"),
        "source": runtime.get("source"),
        "safe_model_config": safe_model_config,
    }


def seed_isolated_jimmy_home(
    jimmy_home: Path,
    *,
    runtime: Optional[Mapping[str, Any]] = None,
) -> None:
    """Create isolated ``config.yaml`` with safe non-secret model identity only.

    Never writes api keys, tokens, or other credentials into artifacts/config.
    """
    import yaml

    jimmy_home = Path(jimmy_home)
    jimmy_home.mkdir(parents=True, exist_ok=True)
    config_path = jimmy_home / "config.yaml"
    safe = {}
    if runtime:
        raw_safe = runtime.get("safe_model_config")
        if isinstance(raw_safe, Mapping):
            safe = {k: v for k, v in raw_safe.items() if v not in (None, "")}

    if not config_path.exists():
        model_block = dict(safe) if safe else {"default": "optimize-harness"}
        config_path.write_text(
            yaml.safe_dump({"model": model_block}, sort_keys=False),
            encoding="utf-8",
        )
        return

    if not safe:
        return

    # Ensure live identity is present without clobbering candidate-overlay fields
    # and without ever injecting secrets.
    try:
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception:
        loaded = {}
    if not isinstance(loaded, dict):
        loaded = {}
    model_cfg = loaded.get("model")
    if not isinstance(model_cfg, dict):
        model_cfg = {}
    changed = False
    for key, value in safe.items():
        if model_cfg.get(key) in (None, "", "optimize-harness") or key not in model_cfg:
            if model_cfg.get(key) != value:
                model_cfg[key] = value
                changed = True
    if changed:
        loaded["model"] = model_cfg
        config_path.write_text(
            yaml.safe_dump(loaded, sort_keys=False),
            encoding="utf-8",
        )


def _normalize_api_key(api_key: Any) -> Any:
    if api_key is None:
        return None
    if callable(api_key):
        return api_key
    text = str(api_key).strip()
    return text or None


class AgentRunner:
    """Real runner that constructs AIAgent with normal runtime credentials.

    Prefer ``AgentRunner.from_resolved_runtime(...)`` for live optimize: resolve
    once against the active JIMMY_HOME **before** isolation, then pass explicit
    values so a stub isolated ``config.yaml`` cannot empty the model deployment.

    When constructed without a pre-resolved runtime, credentials come from
    ``resolve_runtime_provider`` (config + OAuth + env) — never a sentinel
    like ``api_key="missing"``.
    """

    def __init__(
        self,
        *,
        model: str = "",
        api_key: Any = None,
        base_url: Optional[str] = None,
        provider: Optional[str] = None,
        api_mode: Optional[str] = None,
        requested_provider: Optional[str] = None,
        credential_pool: Any = None,
        acp_command: Optional[str] = None,
        acp_args: Optional[List[Any]] = None,
        platform: str = "cli",
        skip_runtime_resolve: bool = False,
    ) -> None:
        self.model = (model or "").strip()
        self.api_key = _normalize_api_key(api_key)
        self.base_url = (base_url or "").strip() or None
        self.provider = (provider or "").strip() or None
        self.api_mode = (api_mode or "").strip() or None
        self.requested_provider = (requested_provider or "").strip() or None
        self.credential_pool = credential_pool
        self.acp_command = (acp_command or "").strip() or None
        self.acp_args = list(acp_args) if acp_args is not None else None
        self.platform = platform
        self.skip_runtime_resolve = bool(skip_runtime_resolve)

    @classmethod
    def from_resolved_runtime(
        cls,
        runtime: Mapping[str, Any],
        *,
        platform: str = "cli",
    ) -> "AgentRunner":
        """Build a runner pinned to a pre-resolved runtime (no re-resolve)."""
        command = runtime.get("command")
        args = runtime.get("args")
        return cls(
            model=str(runtime.get("model") or ""),
            api_key=runtime.get("api_key"),
            base_url=str(runtime.get("base_url") or "") or None,
            provider=str(runtime.get("provider") or "") or None,
            api_mode=str(runtime.get("api_mode") or "") or None,
            requested_provider=str(runtime.get("requested_provider") or "") or None,
            credential_pool=runtime.get("credential_pool"),
            acp_command=str(command) if command else None,
            acp_args=list(args) if args is not None else None,
            platform=platform,
            skip_runtime_resolve=True,
        )

    def build_agent_kwargs(self) -> Dict[str, Any]:
        """Public for tests — kwargs for ``AIAgent(**kwargs)``."""
        kwargs: Dict[str, Any] = {
            "quiet_mode": True,
            "save_trajectories": False,
            "platform": self.platform,
            "skip_memory": True,
        }
        if self.model:
            kwargs["model"] = self.model
        if self.api_key is not None:
            kwargs["api_key"] = self.api_key
        if self.base_url is not None:
            kwargs["base_url"] = self.base_url
        if self.provider is not None:
            kwargs["provider"] = self.provider
            kwargs["requested_provider"] = self.requested_provider or self.provider
        elif self.requested_provider is not None:
            kwargs["requested_provider"] = self.requested_provider
        if self.api_mode is not None:
            kwargs["api_mode"] = self.api_mode
        if self.acp_command is not None:
            kwargs["acp_command"] = self.acp_command
        if self.acp_args is not None:
            kwargs["acp_args"] = list(self.acp_args)
        if self.credential_pool is not None:
            kwargs["credential_pool"] = self.credential_pool

        # Pre-resolved live runtime, or explicit key/base → do not consult
        # (possibly isolated) JIMMY_HOME again.
        if self.skip_runtime_resolve or self.api_key is not None or self.base_url is not None:
            return kwargs

        from jimmy_cli.runtime_provider import resolve_runtime_provider

        runtime = resolve_runtime_provider(
            requested=self.provider,
            target_model=self.model or None,
        )
        kwargs["api_key"] = runtime.get("api_key")
        kwargs["base_url"] = runtime.get("base_url")
        if runtime.get("provider"):
            kwargs["provider"] = runtime.get("provider")
        if runtime.get("requested_provider"):
            kwargs["requested_provider"] = runtime.get("requested_provider")
        if runtime.get("api_mode"):
            kwargs["api_mode"] = runtime.get("api_mode")
        if runtime.get("command"):
            kwargs["acp_command"] = runtime.get("command")
        if runtime.get("args") is not None:
            kwargs["acp_args"] = list(runtime.get("args") or [])
        if runtime.get("credential_pool") is not None:
            kwargs["credential_pool"] = runtime.get("credential_pool")
        if not self.model:
            cfg_model = runtime.get("model")
            if isinstance(cfg_model, str) and cfg_model.strip():
                kwargs["model"] = cfg_model.strip()
        return kwargs

    def run_task(
        self,
        task: OptimizeTask,
        workspace: Path,
        *,
        observer: OptimizeObserver,
    ) -> TaskRunResult:
        from run_agent import AIAgent

        _seed_workspace(task, workspace)
        prev_cwd = os.getcwd()
        os.chdir(workspace)
        llm_before = observer.llm_call_count()
        tool_before = observer.tool_call_count()
        messages: List[Dict[str, Any]] = []
        agent_error = ""
        response = ""
        try:
            try:
                agent = AIAgent(**self.build_agent_kwargs())
                result = agent.run_conversation(task.prompt)
            except Exception as exc:
                agent_error = f"agent_failed: {exc}"
                result = {
                    "final_response": str(exc),
                    "messages": [],
                    "failed": True,
                    "error": str(exc),
                }
            if isinstance(result, dict):
                response = str(
                    result.get("final_response") or result.get("response") or ""
                )
                raw_messages = result.get("messages") or []
                if isinstance(raw_messages, list):
                    messages = sanitize_messages(raw_messages)
                if not agent_error and result.get("failed") is True:
                    err = result.get("error") or response or "agent returned failure"
                    agent_error = f"agent_failed: {err}"
            else:
                response = str(result or "")
        finally:
            os.chdir(prev_cwd)

        new_llm = observer.slice_llm_calls(llm_before)
        new_tools = observer.slice_tool_calls(tool_before)
        llm_turns = len(new_llm)
        tool_calls = len(new_tools)
        completion_tokens = sum(int(c.get("completion_tokens") or 0) for c in new_llm)
        input_tokens = sum(int(c.get("input_tokens") or 0) for c in new_llm)
        cache_read = sum(int(c.get("cache_read_tokens") or 0) for c in new_llm)
        cache_write = sum(int(c.get("cache_write_tokens") or 0) for c in new_llm)

        success = False
        detail = "no_check"
        if agent_error:
            success = False
            detail = agent_error
        elif task.check is not None:
            try:
                success = bool(task.check(response, workspace, {"fake": False}))
                detail = "ok" if success else "check_failed"
            except Exception as exc:
                success = False
                detail = f"check_error: {exc}"
            if llm_turns == 0:
                llm_turns = 1
        else:
            success = bool(response.strip())
            detail = "response_nonempty" if success else "empty_response"
            if llm_turns == 0:
                llm_turns = 1

        observer.mark_task_result(task.id, success, detail)
        score = compute_score(
            ScoreComponents(
                success=success,
                completion_tokens=completion_tokens,
                llm_turns=llm_turns,
                tool_calls=tool_calls,
                expected_max_llm_turns=task.expected_max_llm_turns,
                expected_max_tool_calls=task.expected_max_tool_calls,
                max_useful_completion_tokens=task.max_useful_completion_tokens,
            )
        )
        attribution_summary: Dict[str, int] = {}
        for call in new_llm:
            key = str(call.get("attribution") or "parent")
            attribution_summary[key] = attribution_summary.get(key, 0) + 1

        req_metrics = request_metrics_from_llm_events(new_llm)
        return TaskRunResult(
            task_id=task.id,
            success=success,
            score=score,
            llm_turns=llm_turns,
            tool_calls=tool_calls,
            completion_tokens=completion_tokens,
            input_tokens=input_tokens,
            cache_read_tokens=cache_read,
            cache_write_tokens=cache_write,
            response=response,
            detail=detail,
            attribution_summary=attribution_summary,
            events=list(new_llm) + list(new_tools),
            messages=messages,
            request_metrics=req_metrics,
        )


def run_benchmark(
    *,
    tasks: Sequence[OptimizeTask],
    runner: TaskRunner,
    workspace: Path,
    jimmy_home: Path,
    artifact_dir: Path,
    run_id: str,
    platform: str = "cli",
) -> RunResult:
    """Run tasks under an isolated workspace/JIMMY_HOME and write artifacts.

    Single-thread only: concurrent calls raise ``BenchmarkBusyError``.
    """
    global _BENCHMARK_HELD
    acquired = _BENCHMARK_LOCK.acquire(blocking=False)
    if not acquired:
        raise BenchmarkBusyError(
            "run_benchmark is single-thread orchestration only; "
            "another optimize run holds the process lock"
        )
    _BENCHMARK_HELD = True

    workspace = Path(workspace)
    jimmy_home = Path(jimmy_home)
    artifact_dir = Path(artifact_dir)
    workspace.mkdir(parents=True, exist_ok=True)
    jimmy_home.mkdir(parents=True, exist_ok=True)

    prev_home = os.environ.get("JIMMY_HOME")
    prev_cwd = os.getcwd()
    os.environ["JIMMY_HOME"] = str(jimmy_home)

    observer = OptimizeObserver()
    observer.enable(run_id=run_id, attribution="parent")

    prompt_breakdown: Dict[str, Any] = {}
    folder_cost: Dict[str, Any] = {}
    task_results: List[TaskRunResult] = []
    all_events: List[Dict[str, Any]] = []
    try:
        # Fake/offline runs skip live prompt construction (avoids loading the
        # host AGENTS.md / constructing provider clients during dry-run).
        if isinstance(runner, FakeRunner):
            prompt_breakdown = {
                "skipped": True,
                "reason": "fake_runner_offline",
            }
            folder_cost = {
                "skipped": True,
                "reason": "fake_runner_offline",
                "prompt": "Summarize what is in this folder",
            }
        else:
            try:
                from jimmy_cli.prompt_size import compute_prompt_breakdown

                prompt_breakdown = compute_prompt_breakdown(platform=platform)
            except Exception as exc:
                prompt_breakdown = {"error": str(exc)}

            try:
                from jimmy_cli.optimize.context_cost import diagnose_folder_summarize_cost

                folder_cost = diagnose_folder_summarize_cost(platform=platform)
            except Exception as exc:
                folder_cost = {"error": str(exc)}

        for task in tasks:
            task_ws = workspace / task.id
            if task_ws.exists():
                shutil.rmtree(task_ws)
            task_ws.mkdir(parents=True)
            observer.reset_metrics()
            observer.enable(run_id=run_id, attribution="parent")
            result = runner.run_task(task, task_ws, observer=observer)
            task_results.append(result)
            for ev in result.events:
                all_events.append({"task_id": task.id, **ev})
            all_events.append(
                {
                    "type": "task_result",
                    "task_id": task.id,
                    "success": result.success,
                    "score": result.score,
                    "detail": result.detail,
                }
            )
    finally:
        observer.disable()
        try:
            os.chdir(prev_cwd)
        except Exception:
            pass
        if prev_home is None:
            os.environ.pop("JIMMY_HOME", None)
        else:
            os.environ["JIMMY_HOME"] = prev_home
        _BENCHMARK_HELD = False
        _BENCHMARK_LOCK.release()

    run_dir = ensure_run_dir(artifact_dir, run_id)
    summary = {
        "run_id": run_id,
        "task_scores": {r.task_id: r.score for r in task_results},
        "total": sum(r.score for r in task_results),
        "success_count": sum(1 for r in task_results if r.success),
        "task_count": len(task_results),
        "tasks": [
            {
                "task_id": r.task_id,
                "success": r.success,
                "score": r.score,
                "llm_turns": r.llm_turns,
                "tool_calls": r.tool_calls,
                "completion_tokens": r.completion_tokens,
                "input_tokens": r.input_tokens,
                "cache_read_tokens": r.cache_read_tokens,
                "cache_write_tokens": r.cache_write_tokens,
                "detail": r.detail,
                "attribution_summary": r.attribution_summary,
            }
            for r in task_results
        ],
        "prompt_breakdown": prompt_breakdown,
        "folder_summarize_context_cost": folder_cost,
        "orchestration": {
            "single_thread": True,
            "restores_jimmy_home": True,
            "restores_cwd": True,
        },
    }
    write_summary(run_dir, summary)
    write_events(run_dir, all_events)
    tasks_dir = run_dir / "tasks"
    tasks_dir.mkdir(exist_ok=True)
    for r in task_results:
        (tasks_dir / f"{r.task_id}.json").write_text(
            json.dumps(
                {
                    "task_id": r.task_id,
                    "success": r.success,
                    "score": r.score,
                    "response": r.response,
                    "detail": r.detail,
                    "llm_turns": r.llm_turns,
                    "tool_calls": r.tool_calls,
                    "completion_tokens": r.completion_tokens,
                    "events": r.events,
                    "messages": r.messages,
                    "request_metrics": r.request_metrics,
                },
                ensure_ascii=False,
                indent=2,
                default=str,
            )
            + "\n",
            encoding="utf-8",
        )

    return RunResult(
        run_id=run_id,
        task_results=task_results,
        prompt_breakdown=prompt_breakdown,
        artifact_dir=run_dir,
    )


_FAKE_RESPONSES = {
    "qa_capital_france": "Paris",
    "qa_two_plus_two": "4",
    "qa_http_meaning": "Hypertext Transfer Protocol",
    "qa_list_three_primaries": "red, blue, and yellow",
    "debug_read_traceback": "missing_value",
    "repo_list_top_level": "Demo repo with README.md and src/main.py util",
    "repo_find_entry_point": "src/cli.py",
    "repo_count_py_files": "3",
    "repo_read_version": "1.4.2",
}


def _fake_response_for(task: OptimizeTask) -> str:
    return _FAKE_RESPONSES.get(task.id, f"[fake] completed {task.id}")


def _seed_workspace(task: OptimizeTask, workspace: Path) -> None:
    for rel, content in (task.seed_files or {}).items():
        path = workspace / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def _apply_fake_side_effects(task: OptimizeTask, workspace: Path) -> None:
    """Make fake successes satisfy file-based checkers without an LLM."""
    effects = {
        "coding_hello_py": ("hello.py", "print('Hello, World!')\n"),
        "coding_add_function": ("math_util.py", "def add(a, b):\n    return a + b\n"),
        "coding_test_assert": (
            "test_add.py",
            "from math_util import add\nassert add(2, 3) == 5\n",
        ),
        "coding_json_parse": (
            "parse_cfg.py",
            "import json\ndef load_cfg(path):\n    with open(path, encoding='utf-8') as f:\n        return json.load(f)\n",
        ),
        "debug_off_by_one": (
            "bug.py",
            "def sum_to_n(n):\n    total = 0\n    for i in range(n + 1):\n        total += i\n    return total\n",
        ),
        "debug_name_error": ("broken.py", "def greet():\n    return 'Hello'\n"),
        "debug_div_zero": (
            "safe_div.py",
            "def safe_div(a, b):\n    if b == 0:\n        return None\n    return a / b\n",
        ),
        "file_rename_note": None,
        "file_append_line": None,
        "file_create_nested": ("out/data/flag.txt", "ok\n"),
        "file_delete_temp": None,
        "multi_read_edit_verify": ("config.json", '{"enabled": true}\n'),
        "multi_search_and_patch": ("app/service.py", "x = 1\n# DONE\ny = 2\n"),
        "multi_copy_and_hash": None,
        "multi_pipeline_echo": None,
    }
    if task.id == "file_rename_note":
        src = workspace / "note.txt"
        if src.exists():
            (workspace / "note.md").write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            src.unlink()
        return
    if task.id == "file_append_line":
        path = workspace / "log.txt"
        path.write_text(path.read_text(encoding="utf-8") + "done\n", encoding="utf-8")
        return
    if task.id == "file_delete_temp":
        p = workspace / "temp.bin"
        if p.exists():
            p.unlink()
        return
    if task.id == "multi_copy_and_hash":
        secret = (workspace / "secret.txt").read_text(encoding="utf-8")
        backup = workspace / "backup"
        backup.mkdir(parents=True, exist_ok=True)
        (backup / "secret.txt").write_text(secret, encoding="utf-8")
        (backup / "len.txt").write_text(str(len(secret.encode("utf-8"))), encoding="utf-8")
        return
    if task.id == "multi_pipeline_echo":
        (workspace / "a.txt").write_text("alpha\n", encoding="utf-8")
        (workspace / "b.txt").write_text("beta\n", encoding="utf-8")
        (workspace / "c.txt").write_text("alpha\nbeta\n", encoding="utf-8")
        return

    spec = effects.get(task.id)
    if isinstance(spec, tuple):
        rel, content = spec
        path = workspace / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
