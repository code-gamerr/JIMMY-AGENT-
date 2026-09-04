"""Process runner must capture real stdout/stderr/exit codes."""

from __future__ import annotations

import sys
import threading

from jimmy.models import EventType
from jimmy.process import python_executable, run_command


def test_run_command_captures_real_output(tmp_path):
    events = []
    result = run_command(
        task_id="t1",
        argv=[python_executable(), "-c", "print('jimmy-real')"],
        cwd=tmp_path,
        timeout_s=30,
        on_event=events.append,
    )
    assert result["exit_code"] == 0
    assert "jimmy-real" in result["stdout"]
    assert result["duration_ms"] is not None and result["duration_ms"] >= 0
    types = [e.type for e in events]
    assert EventType.COMMAND_STARTED.value in types
    assert EventType.COMMAND_FINISHED.value in types
    assert any(e.type == EventType.COMMAND_OUTPUT.value for e in events)


def test_blocked_binary_is_not_executed(tmp_path):
    result = run_command(
        task_id="t2",
        argv=["curl", "https://example.com"],
        cwd=tmp_path,
        timeout_s=5,
    )
    assert result["exit_code"] == 126
    assert result.get("blocked") is True


def test_windows_cmd_shim_is_allowlisted(tmp_path):
    from jimmy.security import command_allowed

    ok, reason = command_allowed([r"C:\Users\x\AppData\Roaming\npm\claude.CMD", "-p", "hi"])
    assert ok is True, reason
    ok2, _ = command_allowed([r"C:\npm\codex.cmd", "exec", "hi"])
    assert ok2 is True

