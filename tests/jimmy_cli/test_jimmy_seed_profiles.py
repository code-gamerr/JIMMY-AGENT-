"""Tests for jimmy_seed_profiles (four isolated profile homes)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml

from jimmy_cli.jimmy_seed_profiles import (
    JIMMY_PROFILES,
    _SHARED_PROVIDER_ENV_KEYS,
    _upsert_env_key,
    seed_jimmy_profiles,
)

_LEAN_TOOLSETS = [
    "file",
    "terminal",
    "web",
    "skills",
    "memory",
    "clarify",
    "todo",
    "no_mcp",
]


@pytest.fixture
def jimmy_seed_env(tmp_path, monkeypatch):
    """Isolated JIMMY_HOME + profiles root; fake provider env only."""
    home = tmp_path / "data"
    home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.setenv("JIMMY_HOME", str(home))
    monkeypatch.setattr(
        "jimmy_cli.profiles._get_default_jimmy_home",
        lambda: home,
    )
    monkeypatch.setattr(
        "jimmy_constants.get_jimmy_home",
        lambda: home,
    )
    # Fake Azure provider values — never real secrets.
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "fake-azure-openai-key")
    monkeypatch.setenv("AZURE_FOUNDRY_API_KEY", "fake-foundry-key")
    monkeypatch.setenv(
        "AZURE_OPENAI_ENDPOINT",
        "https://example.openai.azure.com/openai/v1",
    )
    monkeypatch.setenv("AZURE_FOUNDRY_BASE_URL", "https://example.openai.azure.com")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.6-sol")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")
    return home


def _env_map(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#") or "=" not in raw:
            continue
        if raw.startswith("export "):
            raw = raw[len("export ") :]
        key, _, val = raw.partition("=")
        out[key] = val
    return out


def test_seed_creates_four_isolated_homes(jimmy_seed_env, monkeypatch):
    home = jimmy_seed_env
    monkeypatch.setenv("JIMMY1_PASSWORD", "a")
    monkeypatch.setenv("JIMMY2_PASSWORD", "b")
    monkeypatch.setenv("JIMMY3_PASSWORD", "c")
    monkeypatch.setenv("JIMMY4_PASSWORD", "d")

    paths = seed_jimmy_profiles(jimmy_home=home)
    assert len(paths) == 4
    for name, path in zip(JIMMY_PROFILES, paths):
        assert path == home / "profiles" / name
        assert (path / "config.yaml").is_file()
        cfg = yaml.safe_load((path / "config.yaml").read_text(encoding="utf-8"))
        assert cfg["model"]["provider"] == "azure-foundry"
        assert cfg["model"]["default"] == "gpt-5.6-sol"
        assert cfg["agent"]["max_turns"] == 75
        assert cfg["agent"]["coding_context"] == "focus"
        assert cfg["agent"]["api_max_retries"] >= 8
        assert "browser" in cfg["agent"]["disabled_toolsets"]
        assert "computer_use" in cfg["agent"]["disabled_toolsets"]
        assert "bfl" in cfg["agent"]["disabled_toolsets"]
        assert "kanban" in cfg["agent"]["disabled_toolsets"]
        assert cfg["compression"]["protect_last_n"] == 10
        assert cfg["tools"]["tool_search"]["enabled"] == "on"
        assert cfg["skills"]["project_discovery"] is False
        assert cfg["platform_toolsets"]["telegram"] == _LEAN_TOOLSETS
        assert cfg["platform_toolsets"]["cli"] == cfg["platform_toolsets"]["telegram"]
        assert "computer_use" not in cfg["platform_toolsets"]["cli"]
        assert "browser-use" not in cfg["platform_toolsets"]["cli"]
        assert cfg["terminal"]["cwd"] == str(path)
        assert "file" in cfg["known_builtin_toolsets"]["telegram"]
        assert path.is_dir()

    default_cfg = yaml.safe_load((home / "config.yaml").read_text(encoding="utf-8"))
    assert default_cfg["gateway"]["multiplex_profiles"] is True
    assert default_cfg["tools"]["tool_search"]["enabled"] == "on"
    assert default_cfg["terminal"]["cwd"] == str(home)
    assert default_cfg["agent"]["coding_context"] == "focus"
    assert default_cfg["agent"]["api_max_retries"] >= 8
    users = default_cfg["dashboard"]["basic_auth"]["users"]
    assert len(users) == 4
    assert {u["profile"] for u in users} == set(JIMMY_PROFILES)


def test_upsert_env_key_replaces_and_appends(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("FOO=old\nexport BAR=keep\n", encoding="utf-8")
    _upsert_env_key(env_path, "FOO", "new")
    _upsert_env_key(env_path, "BAZ", "added")
    text = env_path.read_text(encoding="utf-8")
    assert "FOO=new" in text
    assert "FOO=old" not in text
    assert "export BAR=keep" in text
    assert "BAZ=added" in text
    # Second upsert is idempotent for the same value.
    _upsert_env_key(env_path, "FOO", "new")
    assert env_path.read_text(encoding="utf-8").count("FOO=") == 1


def test_mirrors_shared_provider_env_into_default_and_profiles(jimmy_seed_env):
    home = jimmy_seed_env
    expected = {
        key: os.environ[key]
        for key in _SHARED_PROVIDER_ENV_KEYS
        if os.environ.get(key, "").strip()
    }
    assert expected, "fixture must set shared provider env keys"

    seed_jimmy_profiles(jimmy_home=home)

    default_env = _env_map(home / ".env")
    for key, val in expected.items():
        assert default_env.get(key) == val, f"default .env mismatch for {key}"

    for name in JIMMY_PROFILES:
        profile_env = _env_map(home / "profiles" / name / ".env")
        for key, val in expected.items():
            assert profile_env.get(key) == val, f"{name} .env mismatch for {key}"
        # Telegram credentials must not leak across profiles when unset.
        assert "TELEGRAM_BOT_TOKEN" not in profile_env


def test_telegram_token_sets_allow_all_when_no_allowlist(jimmy_seed_env, monkeypatch):
    home = jimmy_seed_env
    monkeypatch.setenv("JIMMY1_TELEGRAM_BOT_TOKEN", "111111:FAKE-TOKEN-jimmy1")
    monkeypatch.setenv("JIMMY3_TELEGRAM_BOT_TOKEN", "333333:FAKE-TOKEN-jimmy3")

    seed_jimmy_profiles(jimmy_home=home)

    j1 = yaml.safe_load(
        (home / "profiles" / "jimmy1" / "config.yaml").read_text(encoding="utf-8")
    )
    assert j1["platforms"]["telegram"]["enabled"] is True
    j1_env = _env_map(home / "profiles" / "jimmy1" / ".env")
    assert j1_env["TELEGRAM_BOT_TOKEN"] == "111111:FAKE-TOKEN-jimmy1"
    assert j1_env["TELEGRAM_ALLOW_ALL_USERS"] == "true"
    assert "TELEGRAM_ALLOWED_USERS" not in j1_env

    j2_env = _env_map(home / "profiles" / "jimmy2" / ".env")
    assert "TELEGRAM_BOT_TOKEN" not in j2_env
    j2 = yaml.safe_load(
        (home / "profiles" / "jimmy2" / "config.yaml").read_text(encoding="utf-8")
    )
    platforms = j2.get("platforms") or {}
    telegram = platforms.get("telegram") if isinstance(platforms, dict) else None
    assert not (isinstance(telegram, dict) and telegram.get("enabled") is True)

    j3_env = _env_map(home / "profiles" / "jimmy3" / ".env")
    assert j3_env["TELEGRAM_BOT_TOKEN"] == "333333:FAKE-TOKEN-jimmy3"
    assert j3_env["TELEGRAM_ALLOW_ALL_USERS"] == "true"


def test_telegram_allowlist_branch_skips_allow_all(jimmy_seed_env, monkeypatch):
    home = jimmy_seed_env
    monkeypatch.setenv("JIMMY2_TELEGRAM_BOT_TOKEN", "222222:FAKE-TOKEN-jimmy2")
    monkeypatch.setenv("JIMMY2_TELEGRAM_ALLOWED_USERS", "42,99")

    seed_jimmy_profiles(jimmy_home=home)

    j2_env = _env_map(home / "profiles" / "jimmy2" / ".env")
    assert j2_env["TELEGRAM_BOT_TOKEN"] == "222222:FAKE-TOKEN-jimmy2"
    assert j2_env["TELEGRAM_ALLOWED_USERS"] == "42,99"
    assert "TELEGRAM_ALLOW_ALL_USERS" not in j2_env

    # Sibling profiles must not receive jimmy2's token (fail-closed isolation).
    for other in ("jimmy1", "jimmy3", "jimmy4"):
        other_env = _env_map(home / "profiles" / other / ".env")
        assert "TELEGRAM_BOT_TOKEN" not in other_env
        assert other_env.get("TELEGRAM_ALLOWED_USERS") != "42,99"


def test_mcp_servers_disabled_on_default_and_profiles(jimmy_seed_env):
    home = jimmy_seed_env
    (home / "config.yaml").write_text(
        yaml.safe_dump(
            {
                "mcp_servers": {
                    "demo": {"command": "npx", "args": ["-y", "demo"], "enabled": True},
                    "other": {"url": "http://127.0.0.1:9", "enabled": True},
                }
            }
        ),
        encoding="utf-8",
    )
    profiles_root = home / "profiles" / "jimmy1"
    profiles_root.mkdir(parents=True)
    (profiles_root / "config.yaml").write_text(
        yaml.safe_dump(
            {
                "mcp_servers": {
                    "demo": {"command": "npx", "enabled": True},
                }
            }
        ),
        encoding="utf-8",
    )

    seed_jimmy_profiles(jimmy_home=home)

    default_cfg = yaml.safe_load((home / "config.yaml").read_text(encoding="utf-8"))
    assert default_cfg["mcp_servers"]["demo"]["enabled"] is False
    assert default_cfg["mcp_servers"]["other"]["enabled"] is False

    for name in JIMMY_PROFILES:
        cfg = yaml.safe_load(
            (home / "profiles" / name / "config.yaml").read_text(encoding="utf-8")
        )
        if name == "jimmy1":
            assert cfg["mcp_servers"]["demo"]["enabled"] is False
        assert cfg["platform_toolsets"]["cli"] == _LEAN_TOOLSETS
        assert cfg["platform_toolsets"]["telegram"] == _LEAN_TOOLSETS


def test_seed_is_idempotent(jimmy_seed_env, monkeypatch):
    home = jimmy_seed_env
    monkeypatch.setenv("JIMMY1_TELEGRAM_BOT_TOKEN", "111111:FAKE-TOKEN-jimmy1")
    monkeypatch.setenv("JIMMY1_TELEGRAM_ALLOWED_USERS", "7")
    monkeypatch.setenv("JIMMY1_PASSWORD", "pw1")

    seed_jimmy_profiles(jimmy_home=home)
    first_default = (home / "config.yaml").read_text(encoding="utf-8")
    first_j1_cfg = (home / "profiles" / "jimmy1" / "config.yaml").read_text(
        encoding="utf-8"
    )
    first_j1_env = (home / "profiles" / "jimmy1" / ".env").read_text(encoding="utf-8")
    first_default_env = (home / ".env").read_text(encoding="utf-8")

    seed_jimmy_profiles(jimmy_home=home)
    assert (home / "config.yaml").read_text(encoding="utf-8") == first_default
    assert (
        home / "profiles" / "jimmy1" / "config.yaml"
    ).read_text(encoding="utf-8") == first_j1_cfg
    assert (
        home / "profiles" / "jimmy1" / ".env"
    ).read_text(encoding="utf-8") == first_j1_env
    assert (home / ".env").read_text(encoding="utf-8") == first_default_env

    # Provider keys appear once each after re-seed.
    default_env = _env_map(home / ".env")
    for key in _SHARED_PROVIDER_ENV_KEYS:
        assert first_default_env.count(f"{key}=") == 1
        assert default_env[key]


def test_api_max_retries_parity_default_and_profiles(jimmy_seed_env):
    home = jimmy_seed_env
    seed_jimmy_profiles(jimmy_home=home)

    default_cfg = yaml.safe_load((home / "config.yaml").read_text(encoding="utf-8"))
    assert default_cfg["agent"]["api_max_retries"] >= 8

    for name in JIMMY_PROFILES:
        cfg = yaml.safe_load(
            (home / "profiles" / name / "config.yaml").read_text(encoding="utf-8")
        )
        assert cfg["agent"]["api_max_retries"] == default_cfg["agent"]["api_max_retries"]


def test_api_max_retries_preserves_higher_existing_value(jimmy_seed_env):
    home = jimmy_seed_env
    (home / "config.yaml").write_text(
        yaml.safe_dump({"agent": {"api_max_retries": 12}}),
        encoding="utf-8",
    )
    seed_jimmy_profiles(jimmy_home=home)
    default_cfg = yaml.safe_load((home / "config.yaml").read_text(encoding="utf-8"))
    assert default_cfg["agent"]["api_max_retries"] == 12


def test_lean_seed_strips_heavy_toolsets_preserves_mcp_name(jimmy_seed_env):
    """computer_use/browser-use must not survive as faux-MCP; real MCP names may."""
    home = jimmy_seed_env
    (home / "config.yaml").write_text(
        yaml.safe_dump(
            {
                "platform_toolsets": {
                    "cli": [
                        "file",
                        "terminal",
                        "computer_use",
                        "browser-use",
                        "bfl",
                        "my-custom-mcp",
                    ],
                    "telegram": [
                        "file",
                        "delegation",
                        "session_search",
                        "my-custom-mcp",
                    ],
                }
            }
        ),
        encoding="utf-8",
    )
    seed_jimmy_profiles(jimmy_home=home)
    cfg = yaml.safe_load((home / "config.yaml").read_text(encoding="utf-8"))
    for platform in ("cli", "telegram"):
        entries = cfg["platform_toolsets"][platform]
        assert entries[:7] == _LEAN_TOOLSETS[:7]
        assert "no_mcp" in entries
        assert "computer_use" not in entries
        assert "browser-use" not in entries
        assert "bfl" not in entries
        assert "delegation" not in entries
        assert "session_search" not in entries
        assert "my-custom-mcp" in entries
    for name in ("computer_use", "browser-use", "bfl", "kanban"):
        assert name in cfg["agent"]["disabled_toolsets"]


def test_jimmy_telegram_first_turn_under_half_of_31k(jimmy_seed_env, monkeypatch, tmp_path):
    """Hermetic first-turn estimate must be <= 15.5k (half of ~31k baseline).

    Measures system prompt + tool schemas the way ``jimmy prompt-size`` /
    ``estimate_request_tokens_rough`` do, from a cwd without a huge AGENTS.md.
    """
    home = jimmy_seed_env
    # Fat pre-lean baseline (matches the previous Azure / local first-turn waist).
    (home / "config.yaml").write_text(
        yaml.safe_dump(
            {
                "model": {"provider": "azure-foundry", "default": "gpt-5.6-sol"},
                "platform_toolsets": {
                    "telegram": [
                        "file",
                        "terminal",
                        "web",
                        "skills",
                        "memory",
                        "clarify",
                        "todo",
                        "browser",
                        "vision",
                        "tts",
                        "delegation",
                        "code_execution",
                        "session_search",
                        "image_gen",
                        "computer_use",
                        "browser-use",
                    ],
                    "cli": [
                        "file",
                        "terminal",
                        "web",
                        "skills",
                        "memory",
                        "clarify",
                        "todo",
                        "browser",
                        "vision",
                        "tts",
                        "delegation",
                        "code_execution",
                        "session_search",
                        "image_gen",
                        "computer_use",
                        "browser-use",
                    ],
                },
            }
        ),
        encoding="utf-8",
    )

    clean_cwd = tmp_path / "clean_cwd"
    clean_cwd.mkdir()
    monkeypatch.chdir(clean_cwd)
    monkeypatch.setenv("TERMINAL_CWD", str(home))

    from agent.model_metadata import estimate_request_tokens_rough
    from agent.system_prompt import build_system_prompt
    from jimmy_cli.prompt_size import _build_inspection_agent

    def _estimate(platform: str) -> int:
        agent = _build_inspection_agent(platform)
        full = build_system_prompt(agent)
        tools = getattr(agent, "tools", None) or []
        return estimate_request_tokens_rough(
            messages=[{"role": "user", "content": "hi"}],
            system_prompt=full,
            tools=tools,
        )

    before = _estimate("telegram")
    seed_jimmy_profiles(jimmy_home=home)
    # Force config reload paths that cache on first load_config().
    try:
        from jimmy_cli import config as cfgmod

        for attr in ("_cached_config", "_config_cache", "CONFIG_CACHE"):
            if hasattr(cfgmod, attr):
                setattr(cfgmod, attr, None)
    except Exception:
        pass

    after = _estimate("telegram")
    assert before >= 15_500, f"baseline too lean to prove a cut: {before}"
    assert after <= 15_500, f"after lean still too fat: {after} (before={before})"
    assert after < before

    from jimmy_cli.config import load_config
    from jimmy_cli.tools_config import _get_platform_tools

    cfg = load_config()
    enabled = _get_platform_tools(cfg, "telegram")
    for required_ts in ("file", "terminal", "web", "skills", "memory", "clarify", "todo"):
        assert required_ts in enabled, f"missing toolset {required_ts}: {sorted(enabled)}"
    for banned_ts in (
        "computer_use",
        "browser-use",
        "bfl",
        "kanban",
        "delegation",
        "session_search",
        "code_execution",
        "tts",
        "vision",
    ):
        assert banned_ts not in enabled, f"banned toolset still enabled: {banned_ts}"

    agent = _build_inspection_agent("telegram")
    names = {
        (t.get("function") or {}).get("name") or t.get("name")
        for t in (getattr(agent, "tools", None) or [])
        if isinstance(t, dict)
    }
    # Schemas that always register without external API keys.
    for required in (
        "read_file",
        "write_file",
        "terminal",
        "skills_list",
        "memory",
        "clarify",
        "todo",
    ):
        assert required in names, f"missing required tool {required}: {sorted(names)}"
    # Web toolset may expose only web_extract when no search provider key is set.
    assert names & {"web_search", "web_extract"}, f"no web tools: {sorted(names)}"
    for banned in (
        "computer_use",
        "delegate_task",
        "session_search",
        "execute_code",
        "text_to_speech",
        "vision_analyze",
    ):
        assert banned not in names, f"banned tool still present: {banned}"
