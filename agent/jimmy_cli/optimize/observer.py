"""Opt-in lifecycle observer for harness optimize metrics.

Captures per-LLM-call tokens (input/output/cache-read/cache-write),
finish_reason, tool calls, tool latency, turn number, task success, and
subagent attribution. No-ops when disabled — hooks are only claimed while
an observer is active.

All mutable collections are guarded by an instance RLock so concurrent
subagent / tool threads cannot corrupt writes or snapshots.
"""

from __future__ import annotations

import threading
from typing import Any, Dict, List, Optional, Set

# Hooks this observer consumes when enabled.
_HANDLED_HOOKS = frozenset(
    {
        "post_api_request",
        "post_tool_call",
        "subagent_start",
        "subagent_stop",
    }
)

_lock = threading.RLock()
_active: Optional["OptimizeObserver"] = None


def get_active_observer() -> Optional["OptimizeObserver"]:
    with _lock:
        return _active


class OptimizeObserver:
    """Process-local metrics sink. Enable only for optimize runs."""

    def __init__(self) -> None:
        self._data_lock = threading.RLock()
        self._enabled = False
        self.run_id: str = ""
        self.default_attribution: str = "parent"
        self.llm_calls: List[Dict[str, Any]] = []
        self.tool_calls: List[Dict[str, Any]] = []
        self.task_results: Dict[str, Dict[str, Any]] = {}
        self.subagent_ids: Set[str] = set()
        # Keys may be child_session_id OR child_subagent_id / child task_id —
        # post_tool_call uses task_id (subagent id), post_api uses session_id.
        self._session_attribution: Dict[str, str] = {}
        self._session_parent: Dict[str, str] = {}

    @property
    def enabled(self) -> bool:
        return self._enabled

    def enable(self, run_id: str = "", attribution: str = "parent") -> None:
        global _active
        with _lock:
            self.run_id = run_id or self.run_id or "optimize"
            self.default_attribution = attribution or "parent"
            self._enabled = True
            _active = self

    def disable(self) -> None:
        global _active
        with _lock:
            self._enabled = False
            if _active is self:
                _active = None

    def handles_hook(self, hook_name: str) -> bool:
        return self._enabled and hook_name in _HANDLED_HOOKS

    def observe_lifecycle(self, hook_name: str, **kwargs: Any) -> None:
        if not self._enabled:
            return
        with self._data_lock:
            if hook_name == "subagent_start":
                self._on_subagent_start(**kwargs)
            elif hook_name == "subagent_stop":
                self._on_subagent_stop(**kwargs)
            elif hook_name == "post_api_request":
                self._on_post_api(**kwargs)
            elif hook_name == "post_tool_call":
                self._on_post_tool(**kwargs)

    def mark_task_result(
        self, task_id: str, success: bool, detail: str = ""
    ) -> None:
        with self._data_lock:
            self.task_results[task_id] = {
                "success": bool(success),
                "detail": detail or "",
            }

    def reset_metrics(self) -> None:
        with self._data_lock:
            self.llm_calls.clear()
            self.tool_calls.clear()
            self.task_results.clear()
            self.subagent_ids.clear()
            self._session_attribution.clear()
            self._session_parent.clear()

    def snapshot(self) -> Dict[str, Any]:
        with self._data_lock:
            return {
                "run_id": self.run_id,
                "llm_calls": list(self.llm_calls),
                "tool_calls": list(self.tool_calls),
                "task_results": dict(self.task_results),
                "subagent_ids": sorted(self.subagent_ids),
                "llm_call_count": len(self.llm_calls),
                "tool_call_count": len(self.tool_calls),
            }

    def slice_llm_calls(self, start: int) -> List[Dict[str, Any]]:
        with self._data_lock:
            return list(self.llm_calls[start:])

    def slice_tool_calls(self, start: int) -> List[Dict[str, Any]]:
        with self._data_lock:
            return list(self.tool_calls[start:])

    def llm_call_count(self) -> int:
        with self._data_lock:
            return len(self.llm_calls)

    def tool_call_count(self) -> int:
        with self._data_lock:
            return len(self.tool_calls)

    def _attribution_for_key(self, key: str) -> str:
        if not key:
            return self.default_attribution
        return self._session_attribution.get(key, self.default_attribution)

    def _bind_attribution(
        self, key: str, label: str, parent_session: str = ""
    ) -> None:
        if not key:
            return
        self._session_attribution[key] = label
        if parent_session:
            self._session_parent[key] = parent_session

    def _on_subagent_start(self, **kwargs: Any) -> None:
        child_session = str(kwargs.get("child_session_id") or "")
        child_id = str(
            kwargs.get("child_subagent_id")
            or kwargs.get("child_task_id")
            or kwargs.get("subagent_id")
            or ""
        )
        parent_session = str(kwargs.get("parent_session_id") or "")
        if child_id:
            self.subagent_ids.add(child_id)
        label = f"subagent:{child_id}" if child_id else "subagent"
        # Map session id (post_api_request) and task/subagent id (post_tool_call).
        self._bind_attribution(child_session, label, parent_session)
        self._bind_attribution(child_id, label, parent_session)

    def _on_subagent_stop(self, **kwargs: Any) -> None:
        child_id = str(
            kwargs.get("child_subagent_id")
            or kwargs.get("child_task_id")
            or kwargs.get("subagent_id")
            or ""
        )
        if child_id:
            self.subagent_ids.add(child_id)

    def _on_post_api(self, **kwargs: Any) -> None:
        usage = kwargs.get("usage") or {}
        if not isinstance(usage, dict):
            usage = {}
        session_id = str(kwargs.get("session_id") or "")
        turn_number = int(kwargs.get("api_call_count") or 0)
        input_tokens = int(
            usage.get("input_tokens")
            or usage.get("prompt_tokens")
            or 0
        )
        output_tokens = int(
            usage.get("output_tokens")
            or usage.get("completion_tokens")
            or 0
        )
        record = {
            "session_id": session_id,
            "turn_id": str(kwargs.get("turn_id") or ""),
            "turn_number": turn_number,
            "finish_reason": kwargs.get("finish_reason"),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "prompt_tokens": int(usage.get("prompt_tokens") or input_tokens),
            "completion_tokens": int(usage.get("completion_tokens") or output_tokens),
            "cache_read_tokens": int(usage.get("cache_read_tokens") or 0),
            "cache_write_tokens": int(usage.get("cache_write_tokens") or 0),
            "tool_call_count": int(kwargs.get("assistant_tool_call_count") or 0),
            "api_duration_s": float(kwargs.get("api_duration") or 0.0),
            "attribution": self._attribution_for_key(session_id),
            "parent_session_id": self._session_parent.get(session_id),
            "model": kwargs.get("model"),
            "provider": kwargs.get("provider"),
        }
        self.llm_calls.append(record)

    def _on_post_tool(self, **kwargs: Any) -> None:
        # Real payload shape (model_tools._emit_post_tool_call_hook):
        #   task_id=..., session_id=..., tool_name=..., duration_ms=..., status=...
        # For subagents, task_id == child_subagent_id (delegate_tool child_task_id).
        task_id = str(kwargs.get("task_id") or "")
        session_id = str(kwargs.get("session_id") or "")
        attr_key = task_id or session_id
        duration_ms = kwargs.get("duration_ms")
        if duration_ms is None:
            duration_ms = kwargs.get("latency_ms")
        success = kwargs.get("success")
        if success is None:
            status = str(kwargs.get("status") or "").lower()
            if status:
                success = status in {"ok", "success", "completed"}
        record = {
            "tool_name": str(kwargs.get("tool_name") or kwargs.get("name") or ""),
            "latency_ms": int(duration_ms or 0),
            "success": success,
            "task_id": task_id,
            "session_id": session_id,
            "attribution": self._attribution_for_key(attr_key),
            "parent_session_id": self._session_parent.get(attr_key)
            or self._session_parent.get(session_id),
        }
        self.tool_calls.append(record)


def handles_hook(hook_name: str) -> bool:
    obs = get_active_observer()
    return bool(obs and obs.handles_hook(hook_name))


def observe_lifecycle(hook_name: str, **kwargs: Any) -> None:
    obs = get_active_observer()
    if obs is not None:
        obs.observe_lifecycle(hook_name, **kwargs)
