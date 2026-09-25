"""Resolve cron multi-instance fire-claim TTL from config."""

from __future__ import annotations

from typing import Any, Dict


DEFAULT_FIRE_CLAIM_TTL_SECONDS = 300


def fire_claim_kwargs(config: Dict[str, Any] | None = None) -> Dict[str, int]:
    """Extra kwargs for ``claim_job_for_fire`` — empty unless the TTL is overridden.

    Keeps the unconfigured call path identical to the built-in default.
    """
    ttl = fire_claim_ttl_seconds(config)
    if ttl == DEFAULT_FIRE_CLAIM_TTL_SECONDS:
        return {}
    return {"claim_ttl_seconds": ttl}


def fire_claim_ttl_seconds(config: Dict[str, Any] | None = None) -> int:
    """Return fire_claim TTL seconds (default 300).

    Reads ``cron.multi_instance.fire_claim_ttl_seconds`` when present.
    """
    default = DEFAULT_FIRE_CLAIM_TTL_SECONDS
    if not isinstance(config, dict):
        try:
            from jimmy_cli.config import load_config_readonly

            config = load_config_readonly()
        except Exception:
            return default
    cron = config.get("cron") if isinstance(config, dict) else None
    if not isinstance(cron, dict):
        return default
    multi = cron.get("multi_instance")
    if not isinstance(multi, dict):
        return default
    try:
        ttl = int(multi.get("fire_claim_ttl_seconds", default))
    except (TypeError, ValueError):
        return default
    return max(30, min(ttl, 86400))
