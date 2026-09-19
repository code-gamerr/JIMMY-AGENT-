"""Tests for durable mcp_task store."""

from __future__ import annotations

import json

from tools import mcp_tasks


def test_mcp_task_submit_list_status_cancel(monkeypatch, tmp_path):
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path))

    # Avoid real MCP dispatch in the background thread.
    monkeypatch.setattr(
        mcp_tasks,
        "_run_task",
        lambda task_id: None,
    )

    submitted = json.loads(
        mcp_tasks.mcp_task_tool(
            action="submit",
            server="demo",
            tool="echo",
            arguments={"text": "hi"},
        )
    )
    assert submitted["ok"] is True
    task_id = submitted["task_id"]

    listed = json.loads(mcp_tasks.mcp_task_tool(action="list"))
    assert listed["ok"] is True
    assert any(t["task_id"] == task_id for t in listed["tasks"])

    status = json.loads(mcp_tasks.mcp_task_tool(action="status", task_id=task_id))
    assert status["ok"] is True
    assert status["task"]["task_id"] == task_id

    cancelled = json.loads(mcp_tasks.mcp_task_tool(action="cancel", task_id=task_id))
    assert cancelled["ok"] is True
    assert cancelled["status"] == "cancelled"
