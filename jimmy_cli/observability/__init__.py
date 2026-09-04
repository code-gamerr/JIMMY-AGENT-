"""First-party Jimmy observability integrations."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def observe_lifecycle(hook_name: str, **kwargs: Any) -> None:
    """Dispatch a Jimmy lifecycle event to built-in observability features."""
    from . import relay_shared_metrics

    _safe_observe(relay_shared_metrics.observe_lifecycle, hook_name, kwargs)

    # Opt-in harness optimizer observer — no-op unless explicitly enabled
    # via ``OptimizeObserver.enable()`` / ``jimmy optimize``.
    try:
        from jimmy_cli.optimize import observer as optimize_observer

        if optimize_observer.handles_hook(hook_name):
            _safe_observe(optimize_observer.observe_lifecycle, hook_name, kwargs)
    except Exception:
        logger.warning(
            "Optimize observer hook failed: %s", hook_name, exc_info=True
        )


def handles_hook(hook_name: str) -> bool:
    """Return whether any built-in observability feature handles a hook."""
    from . import relay_shared_metrics

    if relay_shared_metrics.handles_hook(hook_name):
        return True
    try:
        from jimmy_cli.optimize import observer as optimize_observer

        return optimize_observer.handles_hook(hook_name)
    except Exception:
        return False


def _safe_observe(callback: Any, hook_name: str, kwargs: dict[str, Any]) -> None:
    try:
        callback(hook_name, **kwargs)
    except Exception:
        logger.warning(
            "Built-in observability hook failed: %s", hook_name, exc_info=True
        )
