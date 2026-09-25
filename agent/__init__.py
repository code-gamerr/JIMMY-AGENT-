"""Load the real ``agent`` package when the workspace root is on ``sys.path``.

The distribution directory is also named ``agent``. When that directory is
the ``sys.path`` entry, Python imports ``agent/agent`` and never executes
this file. When the workspace root is the entry, this file is the package,
so submodule lookup has to point at the inner package.
"""
from __future__ import annotations

import os

__path__ = [os.path.join(os.path.dirname(__file__), "agent")]

from . import jiter_preload as _jiter_preload  # noqa: F401
