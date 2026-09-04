"""Reversible config-overlay candidate workflow for harness optimize."""

from __future__ import annotations

import copy
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator, Mapping, Optional, Sequence

from jimmy_cli.optimize.artifacts import write_json
from jimmy_cli.optimize.runner import FakeRunner, TaskRunner, run_benchmark
from jimmy_cli.optimize.scoring import aggregate_scores
from jimmy_cli.optimize.simulation import SimulationProfile
from jimmy_cli.optimize.tasks import OptimizeTask


class TaskSetMismatchError(ValueError):
    """Baseline and candidate scored different task-id sets."""


def _deep_merge(base: Dict[str, Any], overlay: Mapping[str, Any]) -> Dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in overlay.items():
        if key in out and isinstance(out[key], dict) and isinstance(value, Mapping):
            out[key] = _deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


class CandidateOverlay:
    """Apply a config.yaml overlay under JIMMY_HOME and restore on exit."""

    def __init__(self, jimmy_home: Path, changes: Mapping[str, Any]) -> None:
        self.jimmy_home = Path(jimmy_home)
        self.changes = dict(changes or {})
        self.config_path = self.jimmy_home / "config.yaml"
        self._backup: str | None = None
        self._existed = False

    @contextmanager
    def apply(self) -> Iterator["CandidateOverlay"]:
        import yaml

        self.jimmy_home.mkdir(parents=True, exist_ok=True)
        self._existed = self.config_path.exists()
        self._backup = (
            self.config_path.read_text(encoding="utf-8") if self._existed else None
        )
        try:
            base: Dict[str, Any] = {}
            if self._backup and self._backup.strip():
                loaded = yaml.safe_load(self._backup) or {}
                if isinstance(loaded, dict):
                    base = loaded
            merged = _deep_merge(base, self.changes)
            self.config_path.write_text(
                yaml.safe_dump(merged, sort_keys=False),
                encoding="utf-8",
            )
            yield self
        finally:
            if self._existed:
                self.config_path.write_text(self._backup or "", encoding="utf-8")
            elif self.config_path.exists():
                self.config_path.unlink()


def compare_runs(
    baseline: Mapping[str, Any],
    candidate: Mapping[str, Any],
) -> Dict[str, Any]:
    """Compare matched task scores; improved iff aggregate total increases.

    Requires identical task-id sets. Missing/extra candidate tasks fail closed
    with ``TaskSetMismatchError`` (they are not silently scored as zero).
    """
    base_scores = dict(baseline.get("task_scores") or {})
    cand_scores = dict(candidate.get("task_scores") or {})
    base_ids = set(base_scores)
    cand_ids = set(cand_scores)
    if base_ids != cand_ids:
        missing = sorted(base_ids - cand_ids)
        extra = sorted(cand_ids - base_ids)
        raise TaskSetMismatchError(
            "baseline and candidate task-id sets must match exactly; "
            f"missing_from_candidate={missing} extra_in_candidate={extra}"
        )
    base_total = float(baseline.get("total") or aggregate_scores(base_scores)["total"])
    cand_total = float(candidate.get("total") or aggregate_scores(cand_scores)["total"])
    deltas = {
        task_id: float(cand_scores[task_id]) - float(base_scores[task_id])
        for task_id in sorted(base_ids)
    }
    return {
        "baseline_total": base_total,
        "candidate_total": cand_total,
        "delta_total": cand_total - base_total,
        "improved": cand_total > base_total,
        "task_deltas": deltas,
        "matched_tasks": sorted(base_ids),
    }


def decide_keep_candidate(comparison: Mapping[str, Any]) -> bool:
    return bool(comparison.get("improved"))


def _resolve_runner(
    *,
    runner: TaskRunner,
    dry_run: bool,
    simulation: Optional[str | SimulationProfile],
) -> TaskRunner:
    if dry_run or simulation is not None:
        return FakeRunner(simulation=simulation)
    return runner


def run_candidate_workflow(
    *,
    tasks: Sequence[OptimizeTask],
    runner: TaskRunner,
    workspace: Path,
    jimmy_home: Path,
    artifact_dir: Path,
    candidate_overlay: Mapping[str, Any],
    dry_run: bool = False,
    platform: str = "cli",
    candidate_simulation: Optional[str | SimulationProfile] = None,
) -> Dict[str, Any]:
    """Run baseline then candidate; keep only if aggregate score improves.

    Candidate changes are config-overlay only (never edits core source).
    When ``dry_run`` is set, forces the fake offline runner.
    ``candidate_simulation`` is an *explicit* named FakeRunner profile applied
    only to the candidate leg (baseline stays unsimulated) so offline fixtures
    can demonstrate a measured improvement. Default / empty overlay with no
    simulation remains rejected.
    """
    import yaml

    artifact_dir = Path(artifact_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    if dry_run:
        baseline_runner: TaskRunner = FakeRunner(simulation=None)
    else:
        baseline_runner = runner

    candidate_runner = _resolve_runner(
        runner=runner,
        dry_run=dry_run,
        simulation=candidate_simulation,
    )
    # When not dry-run but a simulation was requested, still use FakeRunner for
    # the candidate only when simulation is set — that is offline-only.
    if candidate_simulation is not None and not dry_run:
        # Explicit: simulation is offline-only; force fake for that leg.
        candidate_runner = FakeRunner(simulation=candidate_simulation)

    baseline = run_benchmark(
        tasks=tasks,
        runner=baseline_runner,
        workspace=Path(workspace) / "baseline",
        jimmy_home=jimmy_home,
        artifact_dir=artifact_dir,
        run_id="baseline",
        platform=platform,
    )

    overlay = CandidateOverlay(jimmy_home=jimmy_home, changes=candidate_overlay)
    with overlay.apply():
        candidate = run_benchmark(
            tasks=tasks,
            runner=candidate_runner,
            workspace=Path(workspace) / "candidate",
            jimmy_home=jimmy_home,
            artifact_dir=artifact_dir,
            run_id="candidate",
            platform=platform,
        )

    comparison = compare_runs(
        {"task_scores": baseline.task_scores, "total": baseline.total_score},
        {"task_scores": candidate.task_scores, "total": candidate.total_score},
    )
    kept = decide_keep_candidate(comparison)

    overlay_text = yaml.safe_dump(dict(candidate_overlay), sort_keys=False)
    if kept:
        (artifact_dir / "kept_overlay.yaml").write_text(overlay_text, encoding="utf-8")
    else:
        (artifact_dir / "rejected_overlay.yaml").write_text(
            overlay_text, encoding="utf-8"
        )

    sim_name = None
    if isinstance(candidate_simulation, SimulationProfile):
        sim_name = candidate_simulation.name
    elif candidate_simulation:
        sim_name = str(candidate_simulation)

    report = {
        "mode": "dry_run" if dry_run else "live",
        "kept": kept,
        "comparison": comparison,
        "baseline_run": str(baseline.artifact_dir),
        "candidate_run": str(candidate.artifact_dir),
        "candidate_overlay": dict(candidate_overlay),
        "candidate_simulation": sim_name,
    }
    write_json(artifact_dir / "comparison.json", report)
    return report
