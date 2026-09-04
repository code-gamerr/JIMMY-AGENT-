"""Product / CLI naming for Jimmy.

``jimmy`` is the primary console entry point (``jimmy_cli.main:main``).
Help text, banners, and examples always use the Jimmy product name.
"""

from __future__ import annotations

import os
import sys
from functools import lru_cache


def _normalize_argv0(argv0: str) -> str:
    """Basename + strip Windows executable suffix for argv0 matching."""
    name = os.path.basename(argv0 or "").lower()
    if name.endswith(".exe"):
        name = name[:-4]
    return name


@lru_cache(maxsize=16)
def _cli_name_cached(forced: str, argv0_base: str) -> str:
    """Always Jimmy; forced env may override only to ``jimmy``."""
    if forced == "jimmy":
        return "jimmy"
    if argv0_base == "jimmy" or argv0_base.startswith("jimmy-"):
        return "jimmy"
    return "jimmy"


def clear_cli_name_cache() -> None:
    """Drop cached CLI names (tests / rare mid-process env or argv changes)."""
    _cli_name_cached.cache_clear()


def cli_name() -> str:
    """Return the CLI program name for argparse / help text."""
    forced = (os.environ.get("JIMMY_CLI_NAME") or "").strip().lower()
    argv0 = sys.argv[0] if sys.argv else ""
    return _cli_name_cached(forced, _normalize_argv0(argv0))


# Back-compat: older tests / callers may clear via ``cli_name.cache_clear``.
cli_name.cache_clear = clear_cli_name_cache  # type: ignore[attr-defined]


def product_name() -> str:
    """Human product name."""
    return "Jimmy"


def is_jimmy() -> bool:
    return True
