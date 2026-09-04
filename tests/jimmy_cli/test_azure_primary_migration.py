"""Regression: Azure is primary; Nous provider is removed."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest


def test_azure_openai_env_aliases_resolve(monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "test-key")
    monkeypatch.setenv(
        "AZURE_OPENAI_ENDPOINT",
        "https://example.openai.azure.com/openai/deployments/gpt-4o",
    )
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2024-10-21")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    monkeypatch.delenv("AZURE_FOUNDRY_API_KEY", raising=False)
    monkeypatch.delenv("AZURE_FOUNDRY_BASE_URL", raising=False)

    from hermes_cli.runtime_provider import _resolve_azure_foundry_runtime

    runtime = _resolve_azure_foundry_runtime(
        requested_provider="azure-foundry",
        model_cfg={"provider": "azure-foundry"},
    )
    assert runtime["provider"] == "azure-foundry"
    assert runtime["api_key"] == "test-key"
    assert "example.openai.azure.com" in runtime["base_url"]
    assert "api-version=2024-10-21" in runtime["base_url"]
    assert runtime.get("model") == "gpt-4o"


def test_auto_prefers_azure_before_openrouter(monkeypatch):
    monkeypatch.setenv("AZURE_FOUNDRY_API_KEY", "azure-key")
    monkeypatch.setenv("AZURE_FOUNDRY_BASE_URL", "https://example.openai.azure.com")
    monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")

    from hermes_cli.auth import resolve_provider

    assert resolve_provider("auto") == "azure-foundry"


def test_nous_provider_rejected():
    from hermes_cli.auth import AuthError, resolve_provider

    with pytest.raises(AuthError, match="removed"):
        resolve_provider("nous")


def test_managed_tool_gateway_module_absent():
    import importlib.util
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    assert not (root / "tools" / "managed_tool_gateway.py").exists()
    assert not (root / "hermes_cli" / "nous_subscription.py").exists()
    assert not (root / "plugins" / "model-providers" / "nous").exists()
    assert importlib.util.find_spec("tools.managed_tool_gateway") is None
    assert importlib.util.find_spec("hermes_cli.nous_subscription") is None


def test_dual_home_prefers_graphy_when_fresh(tmp_path, monkeypatch):
    monkeypatch.delenv("HERMES_HOME", raising=False)
    monkeypatch.delenv("GRAPHY_HOME", raising=False)
    monkeypatch.setattr("sys.platform", "win32")
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))

    import importlib
    import hermes_constants

    importlib.reload(hermes_constants)
    home = hermes_constants._get_platform_default_hermes_home()
    assert home.name == "graphy"
