"""Artifact writers for optimize runs (JSON summary + JSONL events)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping


def ensure_run_dir(artifact_dir: Path, run_id: str) -> Path:
    run_dir = Path(artifact_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def write_summary(run_dir: Path, summary: Mapping[str, Any]) -> Path:
    path = Path(run_dir) / "summary.json"
    path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return path


def write_events(run_dir: Path, events: Iterable[Mapping[str, Any]]) -> Path:
    path = Path(run_dir) / "events.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for event in events:
            fh.write(json.dumps(dict(event), ensure_ascii=False, default=str))
            fh.write("\n")
    return path


def write_json(path: Path, payload: Mapping[str, Any]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(payload), ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return path


def append_event(run_dir: Path, event: Dict[str, Any]) -> None:
    path = Path(run_dir) / "events.jsonl"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False, default=str))
        fh.write("\n")
