"""present_files — DeerFlow-inspired artifact presentation for Jimmy.

Copies (or links) deliverable files into a session-scoped outputs directory
under Jimmy home so clients (desktop/web/CLI) can surface them to the user.
"""

from __future__ import annotations

import json
import logging
import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

from jimmy_constants import get_jimmy_home
from tools.registry import registry, tool_error

logger = logging.getLogger(__name__)

PRESENT_FILES_SCHEMA = {
    "name": "present_files",
    "description": (
        "Make finished deliverable files visible to the user for viewing or "
        "download. Call after writing reports, slides, images, zips, or other "
        "outputs the user should see. Prefer final artifacts — not temp files."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "filepaths": {
                "type": "array",
                "items": {"type": "string"},
                "description": (
                    "Absolute or workspace-relative paths of files to present. "
                    "Each must exist and be a regular file."
                ),
            },
            "title": {
                "type": "string",
                "description": "Optional short label for this presentation bundle.",
            },
        },
        "required": ["filepaths"],
    },
}


def _session_outputs_dir(session_id: Optional[str]) -> Path:
    sid = (session_id or "default").strip() or "default"
    # Keep path segment safe
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in sid)[:120]
    out = get_jimmy_home() / "artifacts" / safe / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    return out


def present_files_tool(
    filepaths: Optional[List[str]] = None,
    title: Optional[str] = None,
    *,
    session_id: Optional[str] = None,
) -> str:
    if not filepaths:
        return tool_error("filepaths is required and must be a non-empty list")

    outputs = _session_outputs_dir(session_id)
    presented: List[Dict[str, Any]] = []
    errors: List[str] = []

    for raw in filepaths:
        if not isinstance(raw, str) or not raw.strip():
            errors.append(f"invalid path: {raw!r}")
            continue
        src = Path(raw).expanduser()
        if not src.is_absolute():
            src = (Path.cwd() / src).resolve()
        else:
            src = src.resolve()
        if not src.is_file():
            errors.append(f"not a file or missing: {src}")
            continue
        # Refuse escaping into sensitive dirs via symlink games for the copy target name
        dest = outputs / src.name
        # Avoid clobber: uniquify
        if dest.exists() and dest.resolve() != src:
            stem, suf = dest.stem, dest.suffix
            n = 2
            while dest.exists():
                dest = outputs / f"{stem}_{n}{suf}"
                n += 1
        try:
            if dest.resolve() != src:
                shutil.copy2(src, dest)
            presented.append(
                {
                    "name": dest.name,
                    "source": str(src),
                    "presented_path": str(dest),
                    "size_bytes": dest.stat().st_size,
                }
            )
        except OSError as exc:
            errors.append(f"{src}: {exc}")

    result = {
        "ok": bool(presented) and not errors,
        "title": title or "",
        "outputs_dir": str(outputs),
        "presented": presented,
        "errors": errors,
        "hint": (
            "Files are available under the session artifacts outputs directory. "
            "Desktop/web clients should surface presented_path to the user."
        ),
    }
    # Also stamp env for gateway/desktop consumers in this process
    if presented:
        os.environ["JIMMY_LAST_PRESENTED_ARTIFACTS"] = json.dumps(presented)
    return json.dumps(result, indent=2)


def check_present_files_requirements() -> bool:
    return True


registry.register(
    name="present_files",
    toolset="artifacts",
    schema=PRESENT_FILES_SCHEMA,
    handler=lambda args, **kw: present_files_tool(
        filepaths=args.get("filepaths"),
        title=args.get("title"),
        session_id=kw.get("session_id"),
    ),
    check_fn=check_present_files_requirements,
    emoji="📎",
)
