"""User-facing narration is a projection of real events, not a script."""

from jimmy.models import TaskEvent, utcnow
from jimmy.narration import project, render_telegram


def _event(kind: str, **payload) -> TaskEvent:
    return TaskEvent(type=kind, task_id="t1", ts=utcnow(), payload=payload)


def test_assignment_precedes_active_and_hides_scores():
    events = [
        _event("task.created", status="Understanding your request..."),
        _event("task.planning", status="Building execution plan..."),
        _event(
            "task.decomposed",
            breakdown=["Handle workflow and implementation"],
        ),
        _event(
            "task.assigned",
            agent_id="munder",
            label="Munder-Difflin",
            capability="workflow",
            description="Handle workflow and implementation",
            index=1,
        ),
        _event(
            "task.assignment_confirmed",
            agent_id="munder",
            label="Munder-Difflin",
            capability="workflow",
            description="Handle workflow and implementation",
            index=1,
        ),
        _event("task.assignments_complete", count=1),
    ]
    snap = project(events)
    assert snap["phase"] == "assigned"
    assert snap["cards"][0]["status"] == "assigned"
    assert snap["cards"][0]["status"] != "active"
    text = render_telegram(snap)
    assert "Munder-Difflin" in text
    assert "score" not in text.lower()
    assert "Assigned" in text


def test_active_only_after_activation():
    assigned = _event(
        "task.assignment_confirmed",
        agent_id="munder",
        label="Munder-Difflin",
        capability="workflow",
        description="Handle workflow and implementation",
    )
    snap = project([assigned])
    assert snap["cards"][0]["status"] == "assigned"
    live = project(
        [
            assigned,
            _event("task.agent_activated", agent_id="munder", label="Munder-Difflin"),
        ]
    )
    assert live["cards"][0]["status"] == "active"
    assert "activated" in live["headline"]


def test_telegram_is_one_card_not_a_score_dump():
    text = render_telegram(
        project(
            [
                _event("task.execution_starting", parallel=False),
                _event(
                    "task.agent_completed",
                    agent_id="ecc",
                    label="ECC",
                    success=True,
                ),
            ]
        )
    )
    assert "ECC" in text
    assert "Completed" in text
