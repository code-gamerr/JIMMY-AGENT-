"""Store + experience memory."""

from __future__ import annotations

from jimmy.models import Experience, TaskEvent, TaskRecord, TaskStatus, utcnow
from jimmy.store import OrchestratorStore


def test_task_and_experience_roundtrip(tmp_path):
    store = OrchestratorStore(tmp_path / "o.sqlite")
    task = TaskRecord(task_id="abc", user_request="Build auth", status=TaskStatus.QUEUED)
    store.save_task(task)
    loaded = store.get_task("abc")
    assert loaded is not None
    assert loaded.user_request == "Build auth"

    store.append_event(
        TaskEvent(type="task.created", task_id="abc", ts=utcnow(), payload={})
    )
    assert store.list_events("abc")

    exp = Experience(
        experience_id="x1",
        task_id="abc",
        objective="Build authentication module",
        approach="munder",
        agent="munder",
        tools=("git status",),
        errors=(),
        fixes=(),
        result_summary="done",
        success=True,
        strategy="Use munder for auth builds",
    )
    store.save_experience(exp)
    hits = store.search_experiences("authentication")
    assert any(h.experience_id == "x1" for h in hits)
