"""Scoring and useful-token bound behavior for harness optimize."""

from __future__ import annotations

import pytest

from jimmy_cli.optimize.scoring import (
    USEFUL_COMPLETION_CAP,
    ScoreComponents,
    aggregate_scores,
    compute_score,
    useful_completion_tokens,
)


def test_score_formula_weights():
    """100*success + 0.1*useful - 5*extra_turns - 2*extra_tools."""
    components = ScoreComponents(
        success=True,
        completion_tokens=200,
        llm_turns=3,
        tool_calls=4,
        expected_max_llm_turns=1,
        expected_max_tool_calls=1,
        max_useful_completion_tokens=100,
    )
    # useful = min(200, 100) = 100
    # unnecessary turns = 2, tools = 3
    # score = 100 + 0.1*100 - 5*2 - 2*3 = 100 + 10 - 10 - 6 = 94
    assert compute_score(components) == pytest.approx(94.0)


def test_verbosity_cannot_game_useful_tokens():
    assert useful_completion_tokens(10_000, max_useful=50) == 50
    assert useful_completion_tokens(10, max_useful=50) == 10
    assert useful_completion_tokens(-5, max_useful=50) == 0
    assert useful_completion_tokens(USEFUL_COMPLETION_CAP + 500, max_useful=None) == USEFUL_COMPLETION_CAP


def test_failure_scores_below_success_even_with_token_credit():
    fail = compute_score(
        ScoreComponents(
            success=False,
            completion_tokens=USEFUL_COMPLETION_CAP,
            llm_turns=1,
            tool_calls=0,
            expected_max_llm_turns=1,
            expected_max_tool_calls=0,
            max_useful_completion_tokens=USEFUL_COMPLETION_CAP,
        )
    )
    succeed = compute_score(
        ScoreComponents(
            success=True,
            completion_tokens=0,
            llm_turns=1,
            tool_calls=0,
            expected_max_llm_turns=1,
            expected_max_tool_calls=0,
            max_useful_completion_tokens=10,
        )
    )
    assert succeed > fail


def test_aggregate_prefers_higher_total():
    a = {"t1": 90.0, "t2": 80.0}
    b = {"t1": 95.0, "t2": 70.0}
    assert aggregate_scores(a)["total"] == 170.0
    assert aggregate_scores(b)["total"] == 165.0
    assert aggregate_scores(a)["mean"] == 85.0
