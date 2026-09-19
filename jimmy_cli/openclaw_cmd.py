"""``jimmy openclaw`` — optional OpenClaw gateway sidecar.

Wraps vendored ``openclaw/openclaw.mjs`` for doctor/status/dashboard/agent.
Migration stays on ``jimmy claw migrate`` — this command never replaces
Jimmy's gateway as the primary runtime.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Sequence


def resolve_openclaw_root() -> Path:
    override = (os.environ.get("OPENCLAW_HOME") or "").strip()
    if override:
        return Path(override).expanduser().resolve()
    try:
        from jimmy.paths import worker_root

        return worker_root("openclaw")
    except Exception:
        return (Path(__file__).resolve().parent.parent / "openclaw").resolve()


def _node() -> str | None:
    return shutil.which("node")


def _launcher(root: Path) -> Path:
    return root / "openclaw.mjs"


def _run(cmd: Sequence[str], *, cwd: Path, env: dict | None = None) -> int:
    print(f"+ {' '.join(cmd)}  (cwd={cwd})")
    try:
        completed = subprocess.run(
            list(cmd), cwd=str(cwd), check=False, env=env
        )
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 127
    return int(completed.returncode)


def _isolated_env() -> dict:
    """Never touch the operator's live ~/.openclaw by default."""
    env = os.environ.copy()
    state = env.get("OPENCLAW_STATE_DIR", "").strip()
    if not state:
        state_dir = Path(tempfile.gettempdir()) / "jimmy-openclaw-sidecar"
        state_dir.mkdir(parents=True, exist_ok=True)
        env["OPENCLAW_STATE_DIR"] = str(state_dir)
    return env


def cmd_openclaw(args) -> int:
    action = getattr(args, "openclaw_action", None) or "doctor"
    passthrough = list(getattr(args, "openclaw_args", None) or [])
    root = resolve_openclaw_root()
    if not root.is_dir():
        print(
            f"OpenClaw tree not found at {root}.\n"
            "Expected ./openclaw or set OPENCLAW_HOME.",
            file=sys.stderr,
        )
        return 1

    launcher = _launcher(root)
    node = _node()

    if action == "doctor" and (not node or not launcher.is_file()):
        print(f"OpenClaw root: {root}")
        print(f"openclaw.mjs: {'yes' if launcher.is_file() else 'no'}")
        print(f"node: {'yes' if node else 'no'}")
        print(f"skills/: {(root / 'skills').is_dir()}")
        print(f"ui/: {(root / 'ui').is_dir()}")
        print("Hint: use `jimmy claw migrate` to import an existing ~/.openclaw into Jimmy.")
        return 0 if launcher.is_file() else 1

    if not node:
        print("node is required on PATH for jimmy openclaw", file=sys.stderr)
        return 127
    if not launcher.is_file():
        print(f"missing {launcher}", file=sys.stderr)
        return 1

    env = _isolated_env()
    base = [node, str(launcher)]

    if action == "help":
        return _run([*base, "--help"], cwd=root, env=env)
    if action == "status":
        return _run([*base, "status", *passthrough], cwd=root, env=env)
    if action == "doctor":
        # Prefer built-in health if present; fall back to --help smoke.
        code = _run([*base, "doctor", *passthrough], cwd=root, env=env)
        if code == 0:
            return 0
        return _run([*base, "--help"], cwd=root, env=env)
    if action == "dashboard":
        return _run([*base, "dashboard", *passthrough], cwd=root, env=env)
    if action == "gateway":
        print(
            "Warning: OpenClaw gateway is a SIDECAR only — Jimmy gateway stays primary.",
            file=sys.stderr,
        )
        return _run([*base, "gateway", *passthrough], cwd=root, env=env)
    if action == "agent":
        return _run([*base, "agent", *passthrough], cwd=root, env=env)

    print(f"Unknown openclaw action: {action}", file=sys.stderr)
    return 2
