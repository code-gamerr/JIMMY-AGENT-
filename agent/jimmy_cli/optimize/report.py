"""Offline before/after report generation (labeled OFFLINE FIXTURE)."""

from __future__ import annotations

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from jimmy_cli.optimize.candidate import run_candidate_workflow
from jimmy_cli.optimize.runner import FakeRunner
from jimmy_cli.optimize.tasks import list_tasks


REPORT_BANNER = (
    "OFFLINE FIXTURE — deterministic FakeRunner results. "
    "This is NOT evidence of real model improvement."
)


def build_offline_fixture_report(*, work_root: Optional[Path] = None) -> Dict[str, Any]:
    """Run full 24-task baseline + lean_tool_use candidate; return report dict."""
    root = Path(work_root) if work_root else Path(tempfile.mkdtemp(prefix="jimmy-opt-report-"))
    jimmy_home = root / "jimmy_home"
    jimmy_home.mkdir(parents=True, exist_ok=True)
    (jimmy_home / "config.yaml").write_text(
        "model:\n  default: offline-fixture\n",
        encoding="utf-8",
    )
    tasks = list_tasks()
    report = run_candidate_workflow(
        tasks=tasks,
        runner=FakeRunner(),
        workspace=root / "workspaces",
        jimmy_home=jimmy_home,
        artifact_dir=root / "artifacts",
        candidate_overlay={"agent": {"max_turns": 60}},
        dry_run=True,
        platform="cli",
        candidate_simulation="lean_tool_use",
    )
    cmp_ = report["comparison"]
    return {
        "label": "OFFLINE FIXTURE",
        "banner": REPORT_BANNER,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "task_count": len(tasks),
        "baseline_name": "named-baseline-offline",
        "candidate_name": "simulated-lean_tool_use",
        "baseline_total": cmp_["baseline_total"],
        "candidate_total": cmp_["candidate_total"],
        "delta_total": cmp_["delta_total"],
        "improved": cmp_["improved"],
        "kept": report["kept"],
        "task_deltas": cmp_["task_deltas"],
        "artifact_root": str(root / "artifacts"),
        "comparison": report,
    }


def render_offline_fixture_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Offline Fixture Before/After Report",
        "",
        f"> **{REPORT_BANNER}**",
        "",
        f"- Generated (UTC): `{payload.get('generated_at')}`",
        f"- Label: **{payload.get('label')}**",
        f"- Tasks: `{payload.get('task_count')}`",
        f"- Baseline: `{payload.get('baseline_name')}`",
        f"- Candidate: `{payload.get('candidate_name')}` "
        f"(explicit simulation `lean_tool_use`)",
        "",
        "## Aggregate",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Baseline total | {payload.get('baseline_total'):.2f} |",
        f"| Candidate total | {payload.get('candidate_total'):.2f} |",
        f"| Delta | {payload.get('delta_total'):+.2f} |",
        f"| Improved / kept | {payload.get('improved')} / {payload.get('kept')} |",
        "",
        "## Per-task deltas (offline fixture)",
        "",
        "| Task | Delta |",
        "|---|---|",
    ]
    for task_id, delta in sorted((payload.get("task_deltas") or {}).items()):
        lines.append(f"| `{task_id}` | {delta:+.2f} |")
    lines.extend(
        [
            "",
            "## JSON summary",
            "",
            "```json",
            json.dumps(
                {
                    "label": payload.get("label"),
                    "banner": payload.get("banner"),
                    "baseline_total": payload.get("baseline_total"),
                    "candidate_total": payload.get("candidate_total"),
                    "delta_total": payload.get("delta_total"),
                    "kept": payload.get("kept"),
                },
                indent=2,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_offline_fixture_report(*, out_path: Path) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = build_offline_fixture_report()
    text = render_offline_fixture_markdown(payload)
    out_path.write_text(text, encoding="utf-8")
    # Also drop JSON sibling for machine consumers.
    json_path = out_path.with_suffix(".json")
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return out_path
