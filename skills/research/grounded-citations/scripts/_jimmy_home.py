"""Resolve JIMMY_HOME for standalone skill scripts.

Skill scripts may run outside the Jimmy process (system Python, nix env,
CI) where ``jimmy_constants`` is not importable.  This module provides the
same ``get_jimmy_home()`` contract without requiring it on ``sys.path``.

When ``jimmy_constants`` IS available it is used directly so profile
resolution and any future enhancements are picked up automatically.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from jimmy_constants import get_jimmy_home as get_jimmy_home
except (ModuleNotFoundError, ImportError):

    def get_jimmy_home() -> Path:
        """Return the Jimmy home directory (default: ``~/.jimmy``)."""
        val = os.environ.get("JIMMY_HOME", "").strip()
        return Path(val) if val else Path.home() / ".jimmy"
