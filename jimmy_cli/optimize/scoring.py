"""Harness optimize scoring.

Primary signal is task success; useful completion tokens are a bounded
secondary credit. Unnecessary LLM turns and tool calls are penalized.

Formula:
    100 * success
  + 0.1 * useful_completion_tokens
  - 5 * unnecessary_llm_turns
  - 2 * unnecessary_tool_calls
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Mapping, Optional

# Hard ceiling so verbosity cannot dominate the score even if a task
# forgets to set max_useful_completion_tokens.
USEFUL_COMPLETION_CAP = 500


@dataclass(frozen=True)
class ScoreComponents:
    success: bool
    completion_tokens: int
    llm_turns: int
    tool_calls: int
    expected_max_llm_turns: int
    expected_max_tool_calls: int
    max_useful_completion_tokens: Optional[int] = None


def useful_completion_tokens(
    completion_tokens: int,
    max_useful: Optional[int] = None,
) -> int:
    """Bound completion tokens credited as 'useful' (anti-verbosity)."""
    tokens = max(0, int(completion_tokens or 0))
    cap = USEFUL_COMPLETION_CAP if max_useful is None else int(max_useful)
    cap = max(0, min(cap, USEFUL_COMPLETION_CAP))
    return min(tokens, cap)


def compute_score(components: ScoreComponents) -> float:
    useful = useful_completion_tokens(
        components.completion_tokens,
        max_useful=components.max_useful_completion_tokens,
    )
    unnecessary_turns = max(
        0, int(components.llm_turns) - int(components.expected_max_llm_turns)
    )
    unnecessary_tools = max(
        0, int(components.tool_calls) - int(components.expected_max_tool_calls)
    )
    success_pts = 100.0 if components.success else 0.0
    return (
        success_pts
        + 0.1 * useful
        - 5.0 * unnecessary_turns
        - 2.0 * unnecessary_tools
    )


def aggregate_scores(task_scores: Mapping[str, float]) -> Dict[str, float]:
    values = [float(v) for v in task_scores.values()]
    total = sum(values)
    n = len(values)
    return {
        "total": total,
        "mean": (total / n) if n else 0.0,
        "count": float(n),
    }
