"""Resolve JIMMY_HOME for standalone skill scripts.

Skill scripts may run outside the Jimmy process (e.g. system Python,
nix env, CI) where ``jimmy_constants`` is not importable.  This module
provides the same ``get_jimmy_home()`` and ``display_jimmy_home()``
contracts as ``jimmy_constants`` without requiring it on ``sys.path``.

When ``jimmy_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``jimmy_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``JIMMY_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from jimmy_constants import display_jimmy_home as display_jimmy_home
    from jimmy_constants import get_jimmy_home as get_jimmy_home
except (ModuleNotFoundError, ImportError):

    def get_jimmy_home() -> Path:
        """Return the Jimmy home directory (default: ~/.jimmy).

        Mirrors ``jimmy_constants.get_jimmy_home()``."""
        val = os.environ.get("JIMMY_HOME", "").strip()
        return Path(val) if val else Path.home() / ".jimmy"

    def display_jimmy_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``jimmy_constants.display_jimmy_home()``."""
        home = get_jimmy_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
