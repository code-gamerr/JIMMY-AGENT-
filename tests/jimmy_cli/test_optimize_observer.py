"""Behavior tests for the opt-in harness optimize observer."""

from __future__ import annotations

import threading

import pytest

from jimmy_cli.optimize.observer import OptimizeObserver, get_active_observer


@pytest.fixture
def observer():
    obs = OptimizeObserver()
    yield obs
    obs.disable()


def test_disabled_observer_handles_no_hooks(observer):
    assert observer.enabled is False
    assert observer.handles_hook("post_api_request") is False
    assert observer.handles_hook("post_tool_call") is False
    observer.observe_lifecycle(
        "post_api_request",
        session_id="s1",
        usage={"prompt_tokens": 10, "completion_tokens": 5},
        finish_reason="stop",
    )
    assert observer.llm_calls == []
    assert observer.tool_calls == []


def test_enabled_observer_records_llm_and_tool_metrics(observer):
    observer.enable(run_id="run-a", attribution="parent")
    assert observer.enabled is True
    assert observer.handles_hook("post_api_request") is True
    assert observer.handles_hook("post_tool_call") is True

    observer.observe_lifecycle(
        "post_api_request",
        session_id="sess-1",
        turn_id="t1",
        api_call_count=1,
        finish_reason="tool_calls",
        usage={
            "prompt_tokens": 1200,
            "completion_tokens": 80,
            "cache_read_tokens": 900,
            "cache_write_tokens": 50,
            "input_tokens": 1200,
            "output_tokens": 80,
        },
        assistant_tool_call_count=2,
        api_duration=0.42,
    )
    observer.observe_lifecycle(
        "post_tool_call",
        tool_name="terminal",
        duration_ms=15,
        task_id="sess-1",
        success=True,
    )

    assert len(observer.llm_calls) == 1
    call = observer.llm_calls[0]
    assert call["input_tokens"] == 1200
    assert call["output_tokens"] == 80
    assert call["cache_read_tokens"] == 900
    assert call["cache_write_tokens"] == 50
    assert call["finish_reason"] == "tool_calls"
    assert call["tool_call_count"] == 2
    assert call["turn_number"] == 1
    assert call["attribution"] == "parent"
    assert call["session_id"] == "sess-1"

    assert len(observer.tool_calls) == 1
    tool = observer.tool_calls[0]
    assert tool["tool_name"] == "terminal"
    assert tool["latency_ms"] == 15
    assert tool["attribution"] == "parent"


def test_subagent_hooks_set_attribution(observer):
    observer.enable(run_id="run-b", attribution="parent")
    observer.observe_lifecycle(
        "subagent_start",
        parent_session_id="parent-sess",
        child_session_id="child-sess",
        child_subagent_id="sub-1",
        child_goal="explore repo",
    )
    observer.observe_lifecycle(
        "post_api_request",
        session_id="child-sess",
        api_call_count=1,
        finish_reason="stop",
        usage={"prompt_tokens": 10, "completion_tokens": 3},
        assistant_tool_call_count=0,
    )
    observer.observe_lifecycle(
        "subagent_stop",
        child_session_id="child-sess",
        child_subagent_id="sub-1",
    )

    assert observer.llm_calls[0]["attribution"] == "subagent:sub-1"
    assert observer.llm_calls[0]["parent_session_id"] == "parent-sess"
    assert "sub-1" in observer.subagent_ids


def test_post_tool_call_attribution_uses_task_id_from_real_payload(observer):
    """delegate_tool uses task_id=child_subagent_id; post_tool_call must match."""
    observer.enable(run_id="run-task-id", attribution="parent")
    # Real subagent_start payload shape from tools/delegate_tool.py
    observer.observe_lifecycle(
        "subagent_start",
        parent_session_id="parent-sess",
        parent_turn_id="turn-9",
        parent_subagent_id=None,
        child_session_id="child-sess-abc",
        child_subagent_id="subagent-worker-42",
        child_role="leaf",
        child_goal="fix bug",
    )
    # Real post_tool_call payload shape from model_tools._emit_post_tool_call_hook
    observer.observe_lifecycle(
        "post_tool_call",
        tool_name="terminal",
        args={"command": "ls"},
        result='{"ok": true}',
        task_id="subagent-worker-42",
        session_id="child-sess-abc",
        tool_call_id="call_1",
        turn_id="turn-9",
        duration_ms=12,
        status="ok",
    )
    tool = observer.tool_calls[0]
    assert tool["attribution"] == "subagent:subagent-worker-42"
    assert tool["task_id"] == "subagent-worker-42"
    assert tool["parent_session_id"] == "parent-sess"


def test_concurrent_observe_is_thread_safe(observer):
    observer.enable(run_id="run-concurrent")

    def worker(n: int) -> None:
        for i in range(50):
            observer.observe_lifecycle(
                "post_api_request",
                session_id=f"s-{n}",
                api_call_count=i,
                finish_reason="stop",
                usage={"prompt_tokens": 1, "completion_tokens": 1},
            )
            observer.observe_lifecycle(
                "post_tool_call",
                tool_name="terminal",
                duration_ms=1,
                task_id=f"s-{n}",
                status="ok",
            )

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    snap = observer.snapshot()
    assert snap["llm_call_count"] == 200
    assert snap["tool_call_count"] == 200


def test_snapshot_includes_task_success_fields(observer):
    observer.enable(run_id="run-c")
    observer.observe_lifecycle(
        "post_api_request",
        session_id="s",
        api_call_count=1,
        finish_reason="stop",
        usage={"prompt_tokens": 1, "completion_tokens": 1},
    )
    observer.mark_task_result(task_id="qa_1", success=True, detail="ok")
    snap = observer.snapshot()
    assert snap["run_id"] == "run-c"
    assert snap["task_results"]["qa_1"]["success"] is True
    assert snap["llm_call_count"] == 1
    assert get_active_observer() is observer
