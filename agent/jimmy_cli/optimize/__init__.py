"""Opt-in AutoAgent-style harness optimizer for Jimmy.

Zero model-tool schema footprint. Instrumentation is inactive until
``OptimizeObserver.enable()`` (or ``jimmy optimize``) turns it on.
"""

from __future__ import annotations

from jimmy_cli.optimize.observer import OptimizeObserver, get_active_observer

__all__ = ["OptimizeObserver", "get_active_observer"]
