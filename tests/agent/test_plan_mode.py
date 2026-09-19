"""Tests for agent.plan_mode premature-exit guard."""

from __future__ import annotations

from types import SimpleNamespace

from agent.plan_mode import (
    MAX_PLAN_MODE_NUDGES,
    build_plan_mode_nudge,
    incomplete_todos,
    plan_mode_enabled,
)
from tools.todo_tool import TodoStore


def test_plan_mode_disabled_returns_none():
    agent = SimpleNamespace(plan_mode=False, _todo_store=TodoStore(), _plan_mode_nudges=0)
    assert build_plan_mode_nudge(agent) is None


def test_plan_mode_blocks_when_incomplete():
    store = TodoStore()
    store.write([{"id": "1", "content": "Ship feature", "status": "pending"}])
    agent = SimpleNamespace(plan_mode=True, _todo_store=store, _plan_mode_nudges=0)
    assert plan_mode_enabled(agent) is True
    assert incomplete_todos(agent)
    nudge = build_plan_mode_nudge(agent)
    assert nudge is not None
    assert "Ship feature" in nudge


def test_plan_mode_allows_when_complete():
    store = TodoStore()
    store.write([{"id": "1", "content": "Done", "status": "completed"}])
    agent = SimpleNamespace(plan_mode=True, _todo_store=store, _plan_mode_nudges=0)
    assert build_plan_mode_nudge(agent) is None


def test_plan_mode_respects_nudge_cap():
    store = TodoStore()
    store.write([{"id": "1", "content": "Left", "status": "in_progress"}])
    agent = SimpleNamespace(
        plan_mode=True,
        _todo_store=store,
        _plan_mode_nudges=MAX_PLAN_MODE_NUDGES,
    )
    assert build_plan_mode_nudge(agent) is None
