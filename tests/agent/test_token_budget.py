"""Tests for DeerFlow-inspired token budget helpers."""

from types import SimpleNamespace

from agent.token_budget import (
    maybe_apply_token_budget_hard_stop,
    maybe_inject_token_budget_wrapup,
    token_budget_hard_stop_reached,
)


def _agent(**kw):
    base = {
        "token_budget": {
            "enabled": True,
            "total": 1000,
            "warn_fraction": 0.8,
            "hard_stop_fraction": 1.0,
        },
        "session_total_tokens": 0,
        "_token_budget_wrapup_injected": False,
        "_token_budget_hard_stopped": False,
    }
    base.update(kw)
    return SimpleNamespace(**base)


def test_hard_stop_not_reached_below_budget():
    agent = _agent(session_total_tokens=999)
    assert token_budget_hard_stop_reached(agent) is False


def test_hard_stop_reached_at_budget():
    agent = _agent(session_total_tokens=1000)
    assert token_budget_hard_stop_reached(agent) is True


def test_wrapup_injects_into_tool_result():
    agent = _agent(session_total_tokens=850)
    messages = [{"role": "tool", "content": "ok"}]
    assert maybe_inject_token_budget_wrapup(agent, messages) is True
    assert "token budget nearly exhausted" in messages[0]["content"]
    assert agent._token_budget_wrapup_injected is True
    # latched — second call no-ops
    assert maybe_inject_token_budget_wrapup(agent, messages) is False


def test_hard_stop_strips_tool_calls():
    agent = _agent(session_total_tokens=1200)
    assistant = SimpleNamespace(tool_calls=[{"id": "1"}])
    messages = [{"role": "tool", "content": "ok"}]
    assert maybe_apply_token_budget_hard_stop(agent, messages, assistant) is True
    assert not assistant.tool_calls
    assert agent._token_budget_stop_reason == "token_capped"
