"""Hive assignment writes into the live Munder hive paths (or temp harness)."""

from __future__ import annotations

import json
from pathlib import Path

from jimmy import hive_assign


def test_assign_hive_task_writes_ledger(tmp_path, monkeypatch):
    monkeypatch.setattr(hive_assign, "read_harness_home", lambda: tmp_path)
    (tmp_path / "hive" / "agents" / "god" / "inbox").mkdir(parents=True)

    result = hive_assign.assign_hive_task(
        task_id="abc123",
        title="Build landing page",
        description="Create a Jimmy agent landing page",
        assignee="god",
        status="todo",
    )
    tasks_path = Path(result["tasks_path"])
    assert tasks_path.is_file()
    ledger = json.loads(tasks_path.read_text(encoding="utf-8"))
    assert any(t.get("id") == "jimmy-abc123" for t in ledger["tasks"])
    assert Path(result["inbox_message"]).is_file()
