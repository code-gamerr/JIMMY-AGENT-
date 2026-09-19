"""``jimmy deerflow`` subcommand — optional DeerFlow research sidecar.

Wraps the vendored ``deer-flow/`` Compose/Make stack without merging LangGraph
into Jimmy's core loop.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional, Sequence


def resolve_deerflow_root() -> Path:
    override = (os.environ.get("DEER_FLOW_HOME") or "").strip()
    if override:
        return Path(override).expanduser().resolve()
    # Repo-vendored tree: jimmy_cli/ -> repo root -> deer-flow/
    here = Path(__file__).resolve().parent
    candidate = here.parent / "deer-flow"
    return candidate.resolve()


def _run(cmd: Sequence[str], *, cwd: Path) -> int:
    print(f"+ {' '.join(cmd)}  (cwd={cwd})")
    try:
        completed = subprocess.run(list(cmd), cwd=str(cwd), check=False)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 127
    return int(completed.returncode)


def _has_make(root: Path) -> bool:
    return shutil.which("make") is not None and (root / "Makefile").is_file()


def cmd_deerflow(args) -> int:
    """Entry point for ``jimmy deerflow {setup,up,down,doctor}``."""
    action = getattr(args, "deerflow_action", None) or getattr(args, "action", None)
    root = resolve_deerflow_root()
    if not root.is_dir():
        print(
            f"DeerFlow tree not found at {root}.\n"
            "Clone/vendoring expected at ./deer-flow or set DEER_FLOW_HOME.",
            file=sys.stderr,
        )
        return 1

    use_make = _has_make(root)
    if action == "setup":
        if use_make:
            code = _run(["make", "config"], cwd=root)
            if code != 0:
                return code
            return _run(["make", "docker-init"], cwd=root)
        print("Run DeerFlow Install.md steps manually (make not available).")
        print(f"See: {root / 'Install.md'}")
        return 0

    if action == "up":
        if use_make:
            return _run(["make", "docker-start"], cwd=root)
        compose = root / "docker" / "docker-compose.yaml"
        if compose.is_file():
            return _run(["docker", "compose", "-f", str(compose), "up", "-d"], cwd=root)
        print("No Makefile or docker-compose.yaml found.", file=sys.stderr)
        return 1

    if action == "down":
        if use_make:
            return _run(["make", "docker-stop"], cwd=root)
        compose = root / "docker" / "docker-compose.yaml"
        if compose.is_file():
            return _run(["docker", "compose", "-f", str(compose), "down"], cwd=root)
        print("No Makefile or docker-compose.yaml found.", file=sys.stderr)
        return 1

    if action == "doctor":
        print(f"DeerFlow root: {root}")
        print(f"Makefile: {'yes' if (root / 'Makefile').is_file() else 'no'}")
        compose = root / "docker" / "docker-compose.yaml"
        print(f"Compose: {'yes' if compose.is_file() else 'no'}")
        helm = root / "deploy" / "helm" / "deer-flow"
        print(f"Helm chart: {'yes' if helm.is_dir() else 'no'}")
        if use_make:
            return _run(["make", "doctor"], cwd=root)
        print("Doctor: static path checks only (make not available).")
        return 0

    print(f"Unknown deerflow action: {action}", file=sys.stderr)
    return 2
