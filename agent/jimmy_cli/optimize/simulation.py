"""Explicit offline fixture simulations for harness optimize.

These are **named, opt-in** metric overlays for FakeRunner — not hidden magic.
Default offline runs (no simulation) keep baseline metrics so a no-op config
overlay is correctly rejected. A documented simulation must be selected to
demonstrate a measurable candidate improvement in dry-run / CI.

``lean_tool_use`` removes *unnecessary* turns/tools from intentionally bloated
baseline fixture metrics (see task ``fake_*`` fields that sit above
``expected_max_*``), recovering the -5/-2 penalties without changing success.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional


@dataclass(frozen=True)
class SimulationProfile:
    """Deterministic FakeRunner metric overrides keyed by task id."""

    name: str
    description: str
    # Per-task overrides: fake_llm_turns / fake_tool_calls / fake_completion_tokens
    # / fake_success (optional bool).
    task_overrides: Mapping[str, Mapping[str, Any]]


# Bring bloated baseline fixture metrics down to each task's expected_max_*.
# Completion tokens are left unchanged so the score delta is pure penalty relief.
_LEAN_OVERRIDES: Dict[str, Dict[str, Any]] = {
    "coding_hello_py": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "coding_add_function": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "coding_test_assert": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "coding_json_parse": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "debug_off_by_one": {"fake_llm_turns": 3, "fake_tool_calls": 3},
    "debug_name_error": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "debug_div_zero": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "repo_list_top_level": {"fake_llm_turns": 2, "fake_tool_calls": 3},
    "file_rename_note": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "file_append_line": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "file_create_nested": {"fake_llm_turns": 2, "fake_tool_calls": 2},
    "multi_read_edit_verify": {"fake_llm_turns": 3, "fake_tool_calls": 4},
    "multi_search_and_patch": {"fake_llm_turns": 3, "fake_tool_calls": 4},
    "multi_copy_and_hash": {"fake_llm_turns": 3, "fake_tool_calls": 4},
    "multi_pipeline_echo": {"fake_llm_turns": 3, "fake_tool_calls": 4},
}


SIMULATION_PROFILES: Dict[str, SimulationProfile] = {
    "lean_tool_use": SimulationProfile(
        name="lean_tool_use",
        description=(
            "Explicit offline fixture: strip unnecessary LLM turns/tool calls "
            "from bloated baseline fixture metrics down to expected_max_*, "
            "preserving success and completion-token credit. Selected only via "
            "--simulation / SearchCandidate.offline_simulation."
        ),
        task_overrides=_LEAN_OVERRIDES,
    ),
}


def get_simulation(name: Optional[str]) -> Optional[SimulationProfile]:
    if not name:
        return None
    key = str(name).strip()
    if not key:
        return None
    try:
        return SIMULATION_PROFILES[key]
    except KeyError as exc:
        known = ", ".join(sorted(SIMULATION_PROFILES))
        raise KeyError(
            f"unknown optimize simulation {name!r}; known: {known}"
        ) from exc


def apply_simulation_overrides(
    *,
    task_id: str,
    fake_success: bool,
    fake_llm_turns: int,
    fake_tool_calls: int,
    fake_completion_tokens: int,
    simulation: Optional[SimulationProfile],
) -> Dict[str, Any]:
    """Return effective fake metrics after optional named simulation."""
    out: Dict[str, Any] = {
        "fake_success": bool(fake_success),
        "fake_llm_turns": int(fake_llm_turns),
        "fake_tool_calls": int(fake_tool_calls),
        "fake_completion_tokens": int(fake_completion_tokens),
    }
    if simulation is None:
        return out
    override = simulation.task_overrides.get(task_id)
    if not override:
        return out
    for key in (
        "fake_success",
        "fake_llm_turns",
        "fake_tool_calls",
        "fake_completion_tokens",
    ):
        if key in override:
            out[key] = override[key]
    return out
