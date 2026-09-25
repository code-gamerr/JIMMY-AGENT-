"""``jimmy ecc`` — optional ECC harness sidecar (Everything Claude Code).

Wraps vendored ``ECC/scripts/ecc.js`` without replacing Jimmy's agent loop.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence


def resolve_ecc_root() -> Path:
    override = (os.environ.get("ECC_HOME") or "").strip()
    if override:
        return Path(override).expanduser().resolve()
    try:
        from jimmy.paths import worker_root

        return worker_root("ecc")
    except Exception:
        return (Path(__file__).resolve().parent.parent / "ECC").resolve()


def _node() -> str | None:
    return shutil.which("node")


def _ecc_js(root: Path) -> Path:
    return root / "scripts" / "ecc.js"


def _run(cmd: Sequence[str], *, cwd: Path) -> int:
    print(f"+ {' '.join(cmd)}  (cwd={cwd})")
    try:
        completed = subprocess.run(list(cmd), cwd=str(cwd), check=False)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 127
    return int(completed.returncode)


def cmd_ecc(args) -> int:
    """Entry for ``jimmy ecc {doctor,status,consult,memory,control-pane,help}``."""
    action = getattr(args, "ecc_action", None) or "help"
    passthrough = list(getattr(args, "ecc_args", None) or [])
    root = resolve_ecc_root()
    if not root.is_dir():
        print(
            f"ECC tree not found at {root}.\n"
            "Expected ./ECC or set ECC_HOME.",
            file=sys.stderr,
        )
        return 1

    node = _node()
    ecc_js = _ecc_js(root)
    if action == "doctor" and (not node or not ecc_js.is_file()):
        print(f"ECC root: {root}")
        print(f"ecc.js: {'yes' if ecc_js.is_file() else 'no'}")
        print(f"node: {'yes' if node else 'no'}")
        print(f"skills/: {(root / 'skills').is_dir()}")
        return 0 if ecc_js.is_file() else 1

    if not node:
        print("node is required on PATH for jimmy ecc", file=sys.stderr)
        return 127
    if not ecc_js.is_file():
        print(f"missing {ecc_js}", file=sys.stderr)
        return 1

    if action == "help":
        return _run([node, str(ecc_js), "help"], cwd=root)
    if action == "status":
        return _run([node, str(ecc_js), "status", *passthrough], cwd=root)
    if action == "doctor":
        return _run([node, str(ecc_js), "doctor", *passthrough], cwd=root)
    if action == "consult":
        query = " ".join(passthrough).strip() or "recommend a minimal Jimmy profile"
        consult = root / "scripts" / "consult.js"
        if consult.is_file():
            return _run([node, str(consult), query], cwd=root)
        return _run([node, str(ecc_js), "consult", query], cwd=root)
    if action == "memory":
        return _run([node, str(ecc_js), "memory", *passthrough], cwd=root)
    if action == "control-pane":
        return _run([node, str(ecc_js), "control-pane", *passthrough], cwd=root)
    if action == "setup":
        # Prefer minimal + no-hooks on Jimmy hosts (cache-safe).
        apply_js = root / "scripts" / "install-apply.js"
        if apply_js.is_file():
            return _run(
                [
                    node,
                    str(apply_js),
                    "--profile",
                    "minimal",
                    "--target",
                    "hermes",
                    "--no-hooks",
                    *passthrough,
                ],
                cwd=root,
            )
        return _run([node, str(ecc_js), "setup", *passthrough], cwd=root)

    print(f"Unknown ecc action: {action}", file=sys.stderr)
    return 2
