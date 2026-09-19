"""Project real orchestrator events into user-facing status.

Both the command-center UI and Telegram render this snapshot. Nothing here
is invented: a line appears only after the matching event was emitted.
Private routing scores and chain-of-thought never enter the snapshot.
"""

from __future__ import annotations

from typing import Any

from jimmy.models import EventType, TaskEvent
from jimmy.planner import WORKER_LABEL

# Events that change the public status card. Command stdout is not narration.
NARRATION_TYPES = frozenset(
    {
        EventType.TASK_CREATED.value,
        EventType.TASK_PLANNING.value,
        EventType.TASK_DECOMPOSED.value,
        EventType.TASK_ASSIGNED.value,
        EventType.TASK_ASSIGNMENT_CONFIRMED.value,
        EventType.TASK_ASSIGNMENTS_COMPLETE.value,
        EventType.TASK_EXECUTION_STARTING.value,
        EventType.TASK_ROUTED.value,
        EventType.TASK_STARTED.value,
        EventType.TASK_AGENT_ACTIVATED.value,
        EventType.TASK_WAITING.value,
        EventType.TASK_HANDOFF.value,
        EventType.TASK_AGENT_COMPLETED.value,
        EventType.COMMAND_STARTED.value,
        EventType.COMMAND_FINISHED.value,
        EventType.TASK_COMPLETED.value,
        EventType.TASK_FAILED.value,
        EventType.TASK_CANCELLED.value,
    }
)

_PHASE_HEADLINE = {
    "received": "Understanding your request...",
    "planning": "Building execution plan...",
    "decomposed": "Execution plan ready.",
    "assigning": "Assigning tasks...",
    "assigned": "All tasks assigned.",
    "starting": "Starting execution...",
    "executing": "Executing...",
    "handoff": "Routing result...",
    "complete": "Execution complete.",
    "failed": "Execution failed.",
    "cancelled": "Execution cancelled.",
}


def should_refresh(event_type: str) -> bool:
    return event_type in NARRATION_TYPES


def project(events: list[TaskEvent] | tuple[TaskEvent, ...]) -> dict[str, Any]:
    """Fold persisted events into one assignment/execution snapshot."""
    cards: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    phase = "received"
    headline = _PHASE_HEADLINE["received"]
    breakdown: list[str] = []
    handoff: dict[str, Any] | None = None
    error = ""
    parallel = False

    for event in events:
        payload = event.payload or {}
        kind = event.type

        if kind == EventType.TASK_CREATED.value:
            phase = "received"
            headline = _PHASE_HEADLINE["received"]
        elif kind == EventType.TASK_PLANNING.value:
            phase = "planning"
            headline = str(payload.get("status") or _PHASE_HEADLINE["planning"])
        elif kind == EventType.TASK_DECOMPOSED.value:
            phase = "decomposed"
            headline = _PHASE_HEADLINE["decomposed"]
            breakdown = [str(item) for item in payload.get("breakdown") or []]
        elif kind == EventType.TASK_ASSIGNED.value:
            phase = "assigning"
            headline = _PHASE_HEADLINE["assigning"]
            card = _card_from_assignment(payload, status="assigning")
            _upsert(cards, order, card)
        elif kind == EventType.TASK_ASSIGNMENT_CONFIRMED.value:
            card = _card_from_assignment(payload, status="assigned")
            _upsert(cards, order, card)
        elif kind == EventType.TASK_ASSIGNMENTS_COMPLETE.value:
            phase = "assigned"
            headline = _PHASE_HEADLINE["assigned"]
        elif kind == EventType.TASK_EXECUTION_STARTING.value:
            phase = "starting"
            headline = _PHASE_HEADLINE["starting"]
            parallel = bool(payload.get("parallel"))
        elif kind == EventType.TASK_WAITING.value:
            agent_id = str(payload.get("agent_id") or "")
            if agent_id in cards:
                cards[agent_id] = {**cards[agent_id], "status": "waiting"}
            headline = str(payload.get("status") or "Waiting for dependencies...")
        elif kind == EventType.TASK_HANDOFF.value:
            phase = "handoff"
            headline = str(payload.get("status") or _PHASE_HEADLINE["handoff"])
            handoff = {
                "from_agent": payload.get("from_agent"),
                "from_label": payload.get("from_label"),
                "to_agent": payload.get("to_agent"),
                "to_label": payload.get("to_label"),
                "status": "routing",
            }
        elif kind == EventType.TASK_AGENT_ACTIVATED.value:
            phase = "executing"
            agent_id = str(payload.get("agent_id") or "")
            if agent_id in cards:
                cards[agent_id] = {**cards[agent_id], "status": "active"}
            else:
                _upsert(cards, order, _card_from_assignment(payload, status="active"))
            headline = str(payload.get("status") or f"{_label(payload)} activated")
        elif kind == EventType.COMMAND_STARTED.value:
            phase = "executing"
            agent_id = str(payload.get("agent_id") or "")
            if agent_id and agent_id in cards:
                cards[agent_id] = {**cards[agent_id], "status": "active", "tool": "running"}
            headline = str(payload.get("status") or "Tools running...")
        elif kind == EventType.TASK_AGENT_COMPLETED.value:
            agent_id = str(payload.get("agent_id") or "")
            ok = bool(payload.get("success", True))
            status = "completed" if ok else "failed"
            if agent_id in cards:
                cards[agent_id] = {**cards[agent_id], "status": status}
            elif agent_id:
                _upsert(cards, order, _card_from_assignment(payload, status=status))
            headline = str(payload.get("status") or f"{_label(payload)} completed")
        elif kind == EventType.TASK_COMPLETED.value:
            phase = "complete"
            headline = _PHASE_HEADLINE["complete"]
        elif kind == EventType.TASK_FAILED.value:
            phase = "failed"
            headline = _PHASE_HEADLINE["failed"]
            error = str(payload.get("error") or payload.get("summary") or "")
        elif kind == EventType.TASK_CANCELLED.value:
            phase = "cancelled"
            headline = _PHASE_HEADLINE["cancelled"]

    card_list = [cards[key] for key in order]
    assigned = sum(1 for card in card_list if card["status"] in {"assigned", "waiting", "active", "completed"})
    return {
        "phase": phase,
        "headline": headline,
        "breakdown": breakdown,
        "cards": card_list,
        "assigned_count": assigned,
        "total": len(card_list),
        "parallel": parallel,
        "handoff": handoff,
        "error": error,
        "all_assigned": phase in {"assigned", "starting", "executing", "handoff", "complete"}
        and bool(card_list)
        and all(card["status"] != "assigning" for card in card_list),
    }


def render_telegram(snapshot: dict[str, Any]) -> str:
    """Single status message. Callers edit this in place instead of sending a new one."""
    lines = ["ORCHESTRATOR", "", snapshot.get("headline") or ""]
    breakdown = snapshot.get("breakdown") or []
    if breakdown and snapshot.get("phase") in {"decomposed", "assigning", "assigned", "starting"}:
        lines.append("")
        lines.append("Task breakdown:")
        for index, item in enumerate(breakdown, start=1):
            lines.append(f"{index}. {item}")

    cards = snapshot.get("cards") or []
    if cards:
        lines.append("")
        for card in cards:
            mark = _telegram_mark(card.get("status"))
            lines.append(f"{mark} {card.get('label')}")
            lines.append(f"→ {card.get('description')}")
            lines.append(_telegram_state(card.get("status")))

    handoff = snapshot.get("handoff")
    if handoff and snapshot.get("phase") == "handoff":
        lines.append("")
        lines.append(
            f"Routing result: {handoff.get('from_label')} → {handoff.get('to_label')}"
        )

    if snapshot.get("phase") == "assigned":
        lines.extend(["", "All required tasks assigned."])
    if snapshot.get("phase") == "complete":
        lines.extend(["", "All assigned agents completed successfully."])
    if snapshot.get("error"):
        lines.extend(["", str(snapshot["error"])[:500]])
    return "\n".join(lines).strip()


def _label(payload: dict[str, Any]) -> str:
    agent_id = str(payload.get("agent_id") or "")
    return str(payload.get("label") or WORKER_LABEL.get(agent_id, agent_id or "Agent"))


def _card_from_assignment(payload: dict[str, Any], *, status: str) -> dict[str, Any]:
    agent_id = str(payload.get("agent_id") or "")
    return {
        "agent_id": agent_id,
        "label": _label(payload),
        "capability": str(payload.get("capability") or "work"),
        "description": str(payload.get("description") or "Handle the assigned work"),
        "status": status,
        "index": int(payload.get("index") or 0),
    }


def _upsert(cards: dict[str, dict[str, Any]], order: list[str], card: dict[str, Any]) -> None:
    agent_id = card["agent_id"]
    if not agent_id:
        return
    if agent_id not in cards:
        order.append(agent_id)
    cards[agent_id] = {**cards.get(agent_id, {}), **card}


def _telegram_mark(status: str | None) -> str:
    return {
        "assigning": "…",
        "assigned": "•",
        "waiting": "…",
        "active": "●",
        "completed": "✓",
        "failed": "✕",
    }.get(status or "", "○")


def _telegram_state(status: str | None) -> str:
    return {
        "assigning": "Assigning",
        "assigned": "Assigned",
        "waiting": "Waiting",
        "active": "Running",
        "completed": "Completed",
        "failed": "Failed",
    }.get(status or "", "Not started")
