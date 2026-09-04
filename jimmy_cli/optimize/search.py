"""Built-in ``optimize search`` catalog of reversible config overlays.

Only axes that are genuinely configurable via ``config.yaml`` are tested.
This does **not** claim to evaluate prompt/tool source edits.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

from jimmy_cli.optimize.artifacts import write_json
from jimmy_cli.optimize.candidate import (
    decide_keep_candidate,
    run_candidate_workflow,
)
from jimmy_cli.optimize.runner import FakeRunner, TaskRunner, run_benchmark
from jimmy_cli.optimize.tasks import OptimizeTask


# Documented configurable axes only (config.yaml). Not source/prompt edits.
CONFIGURABLE_AXES = (
    "context",       # compression / context-window related settings
    "skills",        # skills index / skill loading preferences
    "tool_schemas",  # tools.<platform>.enabled|disabled
    "guidance",      # display / progress / non-prompt guidance knobs
    "turn_policy",   # agent.max_turns / run_budget / delegation iteration caps
)


@dataclass(frozen=True)
class SearchCandidate:
    id: str
    axis: str
    description: str
    overlay: Mapping[str, Any]
    # Explicit offline FakeRunner simulation name (see simulation.py).
    # None → metrics identical to baseline in dry-run → rejected.
    offline_simulation: Optional[str] = None


def built_in_search_catalog() -> List[SearchCandidate]:
    """Small documented catalog of reversible overlays across configurable axes."""
    return [
        SearchCandidate(
            id="noop_empty_overlay",
            axis="guidance",
            description="Empty overlay control — must not improve offline scores.",
            overlay={},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="guidance_tool_progress_off",
            axis="guidance",
            description="display.tool_progress=off (UI verbosity; no schema change).",
            overlay={"display": {"tool_progress": "off"}},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="context_compression_threshold",
            axis="context",
            description="Tighten compression threshold_tokens (config-only).",
            overlay={"compression": {"threshold_tokens": 24000}},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="skills_quiet_index",
            axis="skills",
            description="skills config tweak (enabled list unchanged — reversible).",
            overlay={"skills": {"disabled": []}},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="tool_schemas_cli_disable_tts",
            axis="tool_schemas",
            description="Disable tts toolset on cli platform (schema footprint).",
            overlay={"tools": {"cli": {"disabled": ["tts"]}}},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="turn_policy_max_turns",
            axis="turn_policy",
            description="Cap agent.max_turns (turn policy).",
            overlay={"agent": {"max_turns": 80}},
            offline_simulation=None,
        ),
        SearchCandidate(
            id="turn_policy_lean_fixture_win",
            axis="turn_policy",
            description=(
                "Same turn-policy overlay PLUS explicit offline simulation "
                "'lean_tool_use' so dry-run can demonstrate a measured win. "
                "Not evidence of live model improvement."
            ),
            overlay={"agent": {"max_turns": 60}},
            offline_simulation="lean_tool_use",
        ),
    ]


def run_search_workflow(
    *,
    tasks: Sequence[OptimizeTask],
    runner: TaskRunner,
    workspace: Path,
    jimmy_home: Path,
    artifact_dir: Path,
    dry_run: bool = False,
    platform: str = "cli",
    catalog: Optional[Sequence[SearchCandidate]] = None,
) -> Dict[str, Any]:
    """Evaluate catalog candidates, rank by score, keep winner only if improved."""
    artifact_dir = Path(artifact_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    candidates = list(catalog or built_in_search_catalog())

    baseline_runner: TaskRunner = FakeRunner() if dry_run else runner
    baseline = run_benchmark(
        tasks=tasks,
        runner=baseline_runner,
        workspace=Path(workspace) / "search_baseline",
        jimmy_home=jimmy_home,
        artifact_dir=artifact_dir,
        run_id="search_baseline",
        platform=platform,
    )

    ranked: List[Dict[str, Any]] = []
    for spec in candidates:
        # Skip re-running empty noop as a full candidate workflow when dry-run:
        # still evaluate via overlay path for consistent artifacts.
        report = run_candidate_workflow(
            tasks=tasks,
            runner=runner,
            workspace=Path(workspace) / f"search_{spec.id}",
            jimmy_home=jimmy_home,
            artifact_dir=artifact_dir / "candidates" / spec.id,
            candidate_overlay=dict(spec.overlay),
            dry_run=dry_run,
            platform=platform,
            candidate_simulation=spec.offline_simulation if dry_run else None,
        )
        cmp_ = report["comparison"]
        ranked.append(
            {
                "id": spec.id,
                "axis": spec.axis,
                "description": spec.description,
                "overlay": dict(spec.overlay),
                "offline_simulation": spec.offline_simulation,
                "kept": report["kept"],
                "baseline_total": cmp_["baseline_total"],
                "candidate_total": cmp_["candidate_total"],
                "delta_total": cmp_["delta_total"],
                "improved": cmp_["improved"],
            }
        )

    ranked.sort(key=lambda r: (r["candidate_total"], r["delta_total"]), reverse=True)
    winner = next((r for r in ranked if r["improved"]), None)
    keep_winner = bool(winner and decide_keep_candidate({
        "improved": winner["improved"],
    }))

    summary = {
        "mode": "dry_run" if dry_run else "live",
        "axes": list(CONFIGURABLE_AXES),
        "note": (
            "Only reversible config.yaml overlays are evaluated. "
            "Non-configurable prompt/tool source changes are not tested."
        ),
        "baseline_total": baseline.total_score,
        "baseline_run": str(baseline.artifact_dir),
        "candidates": ranked,
        "winner": winner,
        "kept_winner": keep_winner,
    }
    write_json(artifact_dir / "search_report.json", summary)
    if keep_winner and winner is not None:
        import yaml

        (artifact_dir / "kept_winner_overlay.yaml").write_text(
            yaml.safe_dump(winner["overlay"], sort_keys=False),
            encoding="utf-8",
        )
    return summary
