"""Opt-in plan-mode premature-exit guard (DeerFlow TodoMiddleware parity).

When ``agent.plan_mode`` is enabled and the todo store still has incomplete
items, block a tool-less "final" answer and nudge the model to continue.
Bounded to avoid infinite loops.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

# Cap rematches so a stuck model cannot burn the iteration budget forever.
MAX_PLAN_MODE_NUDGES = 2

PLAN_MODE_NUDGE = (
    "<system_reminder>\n"
    "Plan mode is active and you still have incomplete todo items. "
    "Do not give a final answer yet. Continue working on the remaining tasks, "
    "call the `todo` tool to mark items completed as you finish them, and only "
    "respond with a final answer when every non-cancelled item is completed.\n\n"
    "Incomplete items:\n"
    "{incomplete}\n"
    "</system_reminder>"
)


def plan_mode_enabled(agent: Any) -> bool:
    return bool(getattr(agent, "plan_mode", False))


def incomplete_todos(agent: Any) -> List[Dict[str, str]]:
    store = getattr(agent, "_todo_store", None)
    if store is None:
        return []
    try:
        items = store.read()
    except Exception:
        return []
    return [
        item
        for item in items
        if item.get("status") in {"pending", "in_progress"}
    ]


def build_plan_mode_nudge(agent: Any) -> Optional[str]:
    """Return a nudge string when plan mode should block finalization, else None."""
    if not plan_mode_enabled(agent):
        return None
    attempts = int(getattr(agent, "_plan_mode_nudges", 0) or 0)
    if attempts >= MAX_PLAN_MODE_NUDGES:
        return None
    incomplete = incomplete_todos(agent)
    if not incomplete:
        return None
    lines = []
    for item in incomplete:
        status = item.get("status", "pending")
        content = item.get("content", "")
        item_id = item.get("id", "")
        lines.append(f"- [{status}] {item_id}. {content}".rstrip("."))
    return PLAN_MODE_NUDGE.format(incomplete="\n".join(lines))
