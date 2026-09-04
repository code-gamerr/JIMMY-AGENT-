"""API auth + task submit against real engine thread."""

from __future__ import annotations

import time

from fastapi.testclient import TestClient

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.api import create_app, set_engine
from jimmy.engine import TaskEngine
from jimmy.models import TaskRecord
from jimmy.process import python_executable, run_command
from jimmy.security import load_or_create_token
from jimmy.store import OrchestratorStore


class _OkAdapter:
    agent_id = "ecc"

    def __init__(self, cwd):
        self.cwd = cwd

    def get_capabilities(self):
        return ("ecc",)

    def get_status(self):
        return AdapterStatus("ecc", "ECC", True, "ok", str(self.cwd), ("ecc",))

    def validate_task(self, task: TaskRecord):
        return True, "ok"

    def execute_task(self, task, emit, cancel_event):
        result = run_command(
            task_id=task.task_id,
            argv=[python_executable(), "-c", "print('api-real')"],
            cwd=self.cwd,
            on_event=emit,
        )
        return AdapterResult(True, result["stdout"].strip(), (), (result,), ())

    def cancel_task(self, task_id: str) -> None:
        return None


def test_api_requires_token_and_runs_task(tmp_path, monkeypatch):
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "home"))
    token = load_or_create_token()
    store = OrchestratorStore(tmp_path / "home" / "jimmy" / "o.sqlite")
    engine = TaskEngine(store=store, adapters={"ecc": _OkAdapter(tmp_path), "munder": _OkAdapter(tmp_path), "openclaw": _OkAdapter(tmp_path)})
    # Force routing to ecc by agent pin
    app = create_app(engine)
    set_engine(engine)
    client = TestClient(app)

    denied = client.get("/api/jimmy/agents")
    assert denied.status_code == 401

    ok = client.get("/api/jimmy/agents", headers={"X-Jimmy-Token": token})
    assert ok.status_code == 200
    assert ok.json()["success"] is True

    created = client.post(
        "/api/jimmy/tasks",
        headers={"X-Jimmy-Token": token},
        json={"user_request": "ECC consult for TDD skills", "agent": "ecc"},
    )
    assert created.status_code == 200
    task_id = created.json()["data"]["task_id"]

    deadline = time.time() + 20
    while time.time() < deadline:
        shown = client.get(f"/api/jimmy/tasks/{task_id}", headers={"X-Jimmy-Token": token})
        status = shown.json()["data"]["task"]["status"]
        if status in {"COMPLETED", "FAILED"}:
            assert status == "COMPLETED"
            assert "api-real" in (shown.json()["data"]["task"]["result"]["summary"] or "")
            return
        time.sleep(0.05)
    raise AssertionError("task did not finish")
