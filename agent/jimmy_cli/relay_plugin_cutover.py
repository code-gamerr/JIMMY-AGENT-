"""Shared migration guards for Jimmy' native NeMo Relay ownership."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


RELAY_PLUGINS_CONFIG_ENV = "JIMMY_NEMO_RELAY_PLUGINS_TOML"

LEGACY_RELAY_PLUGIN_KEYS = frozenset(
    {
        "nemo_relay",
        "observability/nemo_relay",
    }
)

LEGACY_RELAY_EXPORT_ENV_VARS = frozenset(
    {
        "JIMMY_NEMO_RELAY_ATOF_ENABLED",
        "JIMMY_NEMO_RELAY_ATOF_OUTPUT_DIRECTORY",
        "JIMMY_NEMO_RELAY_ATOF_FILENAME",
        "JIMMY_NEMO_RELAY_ATOF_MODE",
        "JIMMY_NEMO_RELAY_ATIF_ENABLED",
        "JIMMY_NEMO_RELAY_ATIF_OUTPUT_DIRECTORY",
        "JIMMY_NEMO_RELAY_ATIF_FILENAME_TEMPLATE",
        "JIMMY_NEMO_RELAY_ATIF_AGENT_NAME",
        "JIMMY_NEMO_RELAY_ATIF_AGENT_VERSION",
        "JIMMY_NEMO_RELAY_ATIF_EXPORT_TIMEOUT_S",
        "JIMMY_NEMO_RELAY_ATIF_MODEL_NAME",
        "JIMMY_NEMO_RELAY_ATIF_SUBAGENT_EXPORT_MODE",
    }
)


def legacy_relay_plugin_keys(values: Any) -> tuple[str, ...]:
    """Return removed Relay plugin identities present in a config value."""
    if not isinstance(values, (list, tuple, set, frozenset)):
        return ()
    return tuple(
        sorted(
            {
                value
                for value in values
                if isinstance(value, str) and value in LEGACY_RELAY_PLUGIN_KEYS
            }
        )
    )


def configured_legacy_relay_env_vars(
    env: Mapping[str, Any] | None,
) -> tuple[str, ...]:
    """Return non-empty legacy Relay exporter variables in *env*."""
    if env is None:
        return ()
    return tuple(
        sorted(
            name
            for name in LEGACY_RELAY_EXPORT_ENV_VARS
            if env.get(name) is not None and str(env[name]).strip()
        )
    )
