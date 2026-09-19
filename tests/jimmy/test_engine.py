"""Engine with a real process adapter (python -c), not mocked progress."""

from __future__ import annotations

import time

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.engine import TaskEngine
from jimmy.models import TaskRecord
from jimmy.process import python_executable, run_command
from jimmy.store import OrchestratorStore


class _PyAdapter:
    agent_id = "munder"

    def __init__(self, cwd):
        self.cwd = cwd

    def get_capabilities(self):
        return ("python",)

    def get_status(self):
        return AdapterStatus(
            agent_id="munder",
            label="Munder-Difflin",
            ready=True,
            detail="test adapter",
            workspace=str(self.cwd),
            capabilities=("python",),
        )

    def validate_task(self, task: TaskRecord):
        return True, "ok"

    def execute_task(self, task, emit, cancel_event):
        result = run_command(
            task_id=task.task_id,
            argv=[python_executable(), "-c", "print('engine-real-exec')"],
            cwd=self.cwd,
            timeout_s=30,
            cancel_event=cancel_event,
            on_event=emit,
        )
        return AdapterResult(
            success=result["exit_code"] == 0,
            summary=result["stdout"].strip(),
            files_changed=(),
            commands=(result,),
            errors=(),
        )

    def cancel_task(self, task_id: str) -> None:
        return None


def test_engine_runs_real_process_and_stores_experience(tmp_path, monkeypatch):
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "home"))
    store = OrchestratorStore(tmp_path / "home" / "jimmy" / "o.sqlite")
    engine = TaskEngine(store=store, adapters={"munder": _PyAdapter(tmp_path)})
    task = engine.submit("Build authentication for my project.", agent="munder")
    deadline = time.time() + 20
    final = None
    while time.time() < deadline:
        final = engine.store.get_task(task.task_id)
        events = engine.store.list_events(task.task_id)
        if (
            final
            and final.status.value in {"COMPLETED", "FAILED"}
            and any(e.type == "experience.stored" for e in events)
        ):
            break
        time.sleep(0.05)
    assert final is not None
    assert final.status.value == "COMPLETED"
    assert final.result and "engine-real-exec" in final.result["summary"]
    events = engine.store.list_events(task.task_id)
    assert any(e.type == "command.started" for e in events)
    assigned_at = next(i for i, e in enumerate(events) if e.type == "task.assignment_confirmed")
    started_at = next(i for i, e in enumerate(events) if e.type == "command.started")
    assert assigned_at < started_at
    assert any(e.type == "task.assignments_complete" for e in events)
    assert events[assigned_at].payload.get("status") == "assigned"
    assert any(e.type == "task.assignments_complete" for e in events)
    assert any(e.type == "experience.stored" for e in events)
    confirmed = [e for e in events if e.type == "task.assignment_confirmed"]
    assert confirmed
    assert confirmed[0].payload.get("status") == "assigned"
    started = next(i for i, e in enumerate(events) if e.type == "command.started")
    assigned = next(i for i, e in enumerate(events) if e.type == "task.assignment_confirmed")
    assert assigned < started
    exps = engine.store.search_experiences("authentication")
    assert exps
