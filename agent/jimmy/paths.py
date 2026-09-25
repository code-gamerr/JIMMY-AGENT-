"""Locate the Jimmy repo and the three worker trees without hardcoding HOME."""

from __future__ import annotations

from pathlib import Path

from jimmy_constants import get_jimmy_home, get_workspace_root

_REPO_ROOT = get_workspace_root()

WORKER_DIRS = {
    "openclaw": "openclaw",
    "munder": "munder-difflin",
    "ecc": "ECC",
}


def repo_root() -> Path:
    return _REPO_ROOT


def worker_root(agent_id: str) -> Path:
    rel = WORKER_DIRS.get(agent_id)
    if not rel:
        raise KeyError(f"unknown worker {agent_id!r}")
    return repo_root() / rel


def jimmy_home() -> Path:
    path = get_jimmy_home() / "jimmy"
    path.mkdir(parents=True, exist_ok=True)
    return path


def db_path() -> Path:
    return jimmy_home() / "orchestrator.sqlite"


def auth_path() -> Path:
    return jimmy_home() / "auth.json"


def audit_path() -> Path:
    return jimmy_home() / "audit.jsonl"
