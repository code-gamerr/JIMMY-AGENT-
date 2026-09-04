"""Unit tests for Jimmy planner routing."""

from __future__ import annotations

from jimmy.models import Experience
from jimmy.planner import plan_request


def test_build_auth_routes_to_munder():
    plan = plan_request("Build authentication for my project.")
    assert plan.agent == "munder"
    assert plan.steps
    assert "munder" in plan.workers


def test_landing_page_assigns_landing_and_munder():
    plan = plan_request("Build a landing page website for the Jimmy agent")
    assert "landing" in plan.workers or plan.agent in {"landing", "munder"}
    assert plan.workers


def test_company_goal_gets_multiple_workers():
    plan = plan_request("Coordinate a startup launch across the company of agents")
    assert len(plan.workers) >= 2



def test_telegram_routes_to_openclaw():
    plan = plan_request("Connect Telegram channel on the OpenClaw gateway")
    assert plan.agent == "openclaw"


def test_ecc_consult_routes_to_ecc():
    plan = plan_request("Use ECC to consult which skills help with TDD hooks")
    assert plan.agent == "ecc"


def test_explicit_agent_wins():
    plan = plan_request("Build authentication", explicit_agent="ecc")
    assert plan.agent == "ecc"


def test_successful_experience_boosts_agent():
    exp = Experience(
        experience_id="e1",
        task_id="t1",
        objective="Connect Slack",
        approach="openclaw",
        agent="openclaw",
        tools=(),
        errors=(),
        fixes=(),
        result_summary="ok",
        success=True,
        strategy="Use openclaw for messaging",
    )
    plan = plan_request("Connect Slack workspace", experiences=[exp])
    assert plan.agent == "openclaw"
    assert "e1" in plan.reused_experience_ids
