#!/usr/bin/env python3
"""Seed four isolated Jimmy profiles sharing Azure OpenAI credentials.

Run inside the container (or with JIMMY_HOME set) on first boot:

    python -m jimmy_cli.jimmy_seed_profiles

Creates profiles jimmy1..jimmy4 under the profiles root, writes matching
model config, enables gateway.multiplex_profiles on the default home, and
never copies Telegram tokens between profiles.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

JIMMY_PROFILES = ("jimmy1", "jimmy2", "jimmy3", "jimmy4")


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return raw if isinstance(raw, dict) else {}


def _dump_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )


def _azure_model_block() -> dict[str, Any]:
    endpoint = (
        os.environ.get("AZURE_FOUNDRY_BASE_URL")
        or os.environ.get("AZURE_OPENAI_ENDPOINT")
        or ""
    ).rstrip("/")
    model = (
        os.environ.get("AZURE_OPENAI_DEPLOYMENT")
        or os.environ.get("JIMMY_MODEL")
        or "gpt-6-astra"
    )
    # gpt-6-astra rejects tools+reasoning on /chat/completions (HTTP 400);
    # Responses API is required. Keep chat_completions only for classic chat
    # models (gpt-4o, etc.) if someone overrides AZURE_OPENAI_DEPLOYMENT.
    api_mode = "chat_completions"
    slug = str(model).strip().lower()
    if slug.startswith(("gpt-6", "gpt-5", "o1", "o3", "o4", "codex")):
        api_mode = "codex_responses"
    block: dict[str, Any] = {
        "default": model,
        "provider": "azure-foundry",
        "api_mode": api_mode,
    }
    if endpoint:
        if not endpoint.endswith("/openai/v1"):
            if "openai.azure.com" in endpoint and "/openai" not in endpoint:
                endpoint = endpoint + "/openai/v1"
        block["base_url"] = endpoint
    return block


def _scrub_wal_sidecars(home: Path) -> None:
    """Drop stale ``*-wal`` / ``*-shm`` files left by a prior WAL attempt.

    Safe only before other processes open the DB (container CMD runs seed
    before ``jimmy dashboard``). On Azure Files these sidecars are a common
    source of indefinite locks once WAL was attempted.
    """
    for pattern in ("*.db-wal", "*.db-shm", "state.db-wal", "state.db-shm"):
        for path in home.glob(pattern):
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass


def _force_delete_journal(home: Path) -> None:
    """Convert ``state.db`` off WAL before the dashboard opens it.

    ``apply_wal_with_fallback`` refuses to live-downgrade an on-disk WAL DB.
    On Azure Files that leaves sessions permanently hung. At boot (seed-only
    process) we can safely flip the header to DELETE or recreate an empty store.
    """
    import sqlite3

    db = home / "state.db"
    _scrub_wal_sidecars(home)
    if not db.is_file():
        return
    try:
        conn = sqlite3.connect(f"file:{db}?mode=rw", uri=True, timeout=8.0)
        try:
            row = conn.execute("PRAGMA journal_mode=DELETE").fetchone()
            mode = (row[0] if row else "").lower()
            if mode != "delete":
                raise RuntimeError(f"journal_mode stayed {mode!r}")
            conn.commit()
        finally:
            conn.close()
    except Exception as exc:
        print(f"seed: recreating {db} after journal convert failed: {exc}")
        for path in (db, Path(str(db) + "-wal"), Path(str(db) + "-shm")):
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass


def _upsert_env_key(env_path: Path, key: str, value: str) -> None:
    """Set ``key=value`` in a dotenv file, replacing any existing line."""
    lines: list[str] = []
    if env_path.is_file():
        lines = env_path.read_text(encoding="utf-8").splitlines()
    prefix = f"{key}="
    out: list[str] = []
    found = False
    for line in lines:
        if line.startswith(prefix) or line.startswith(f"export {prefix}"):
            if not found:
                out.append(f"{key}={value}")
                found = True
            continue
        out.append(line)
    if not found:
        if out and out[-1].strip():
            out.append("")
        out.append(f"{key}={value}")
    env_path.parent.mkdir(parents=True, exist_ok=True)
    env_path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


# Shared Azure OpenAI / Foundry credentials. Under gateway.multiplex_profiles,
# profile turns install a fail-closed secret scope from that profile's .env and
# do NOT fall through to process os.environ for credential names — so these
# must be copied into every profile .env (and the default home .env).
_SHARED_PROVIDER_ENV_KEYS = (
    "AZURE_OPENAI_API_KEY",
    "AZURE_FOUNDRY_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_FOUNDRY_BASE_URL",
    "AZURE_OPENAI_DEPLOYMENT",
    "AZURE_OPENAI_API_VERSION",
)


def _sync_shared_provider_env(env_path: Path) -> int:
    """Copy shared Azure provider env vars into a profile/default .env.

    Returns the number of keys written.
    """
    written = 0
    for key in _SHARED_PROVIDER_ENV_KEYS:
        val = os.environ.get(key, "").strip()
        if not val:
            continue
        _upsert_env_key(env_path, key, val)
        written += 1
    return written


def _enable_telegram_platform(cfg: dict[str, Any]) -> None:
    platforms = cfg.get("platforms") if isinstance(cfg.get("platforms"), dict) else {}
    platforms = dict(platforms)
    telegram = (
        dict(platforms["telegram"])
        if isinstance(platforms.get("telegram"), dict)
        else {}
    )
    telegram["enabled"] = True
    platforms["telegram"] = telegram
    cfg["platforms"] = platforms


# Heavy / non-messaging toolsets Jimmy keeps off. Includes names that
# ``_get_platform_tools`` can reintroduce via recently-shipped or recovery
# paths (bfl, kanban, computer_use, browser-use) so disabled_toolsets is the
# hard belt after platform_toolsets is narrowed.
_JIMMY_DISABLED_TOOLSETS = frozenset(
    {
        "browser",
        "browser-use",
        "bfl",
        "computer_use",
        "image_gen",
        "tts",
        "video",
        "video_gen",
        "homeassistant",
        "spotify",
        "moa",
        "vision",
        "delegation",
        "code_execution",
        "session_search",
        "cronjob",
        "kanban",
        "rl",
        # Do NOT disable "search" or "debugging": both resolve to tools that
        # overlap the lean surface (web_search / read_file / terminal), and
        # disabled_toolsets subtracts by tool name after enable — wiping them
        # would gut file/terminal/web even when those toolsets stay enabled.
        "x_search",
        "discord",
        "discord_admin",
        "feishu_doc",
        "feishu_drive",
        "yuanbao",
    }
)

_JIMMY_LEAN_TOOLSETS = (
    "file",
    "terminal",
    "web",
    "skills",
    "memory",
    "clarify",
    "todo",
)


def _jimmy_known_toolset_names() -> set[str]:
    """Built-in + plugin toolset names that must never be treated as MCP."""
    names: set[str] = set(_JIMMY_DISABLED_TOOLSETS)
    names.update(_JIMMY_LEAN_TOOLSETS)
    try:
        from toolsets import TOOLSETS

        names.update(str(k) for k in TOOLSETS.keys())
    except Exception:
        pass
    try:
        from jimmy_cli.tools_config import CONFIGURABLE_TOOLSETS, _get_plugin_toolset_keys

        names.update(str(k) for k, _, _ in CONFIGURABLE_TOOLSETS)
        names.update(str(k) for k in _get_plugin_toolset_keys())
    except Exception:
        pass
    return names


def _apply_jimmy_agent_limits(
    cfg: dict[str, Any], *, home: Path | None = None
) -> None:
    """Cap turns, shrink compression tail, and cut first-turn token waist.

    First-turn cost is mostly tool schemas + skills/MCP in the prefix —
    conversation compression never helps turn 1. Keep chat/coding useful
    (files, terminal, web, memory, skills, clarify, todo) and drop heavy
    non-messaging toolsets; defer MCP schemas via tool_search.

    ``api_max_retries`` is applied to default *and* profile configs: under
    multiplex each profile turn loads that profile's ``config.yaml``, so RPM
    survival must live on every home, not only the parent.

    ``home`` (when provided) becomes ``terminal.cwd`` if unset, so messaging
    / dashboard sessions do not inherit a developer checkout's huge AGENTS.md.
    """
    agent = dict(cfg["agent"]) if isinstance(cfg.get("agent"), dict) else {}
    agent["max_turns"] = 75
    agent["coding_context"] = "focus"
    # Survive Azure OpenAI RPM bursts (4 users + tool loops).
    agent["api_max_retries"] = max(int(agent.get("api_max_retries") or 0), 8)
    # gpt-6-astra rejects tools + non-none reasoning on /chat/completions.
    # Seed prefers Responses API for gpt-5+/gpt-6; this is a safe fallback.
    if not str(agent.get("reasoning_effort") or "").strip():
        agent["reasoning_effort"] = "none"
    disabled = {
        str(x)
        for x in (agent.get("disabled_toolsets") or [])
        if isinstance(x, str) and x.strip()
    }
    disabled.update(_JIMMY_DISABLED_TOOLSETS)
    agent["disabled_toolsets"] = sorted(disabled)
    cfg["agent"] = agent

    compression = (
        dict(cfg["compression"]) if isinstance(cfg.get("compression"), dict) else {}
    )
    compression["protect_last_n"] = 10
    cfg["compression"] = compression

    tools = dict(cfg["tools"]) if isinstance(cfg.get("tools"), dict) else {}
    tool_search = (
        dict(tools["tool_search"]) if isinstance(tools.get("tool_search"), dict) else {}
    )
    tool_search["enabled"] = "on"
    tool_search["listing"] = "auto"
    tool_search["listing_max_tokens"] = 2000
    tools["tool_search"] = tool_search
    cfg["tools"] = tools

    skills = dict(cfg["skills"]) if isinstance(cfg.get("skills"), dict) else {}
    skills["project_discovery"] = False
    skills["external_dirs"] = []
    cfg["skills"] = skills

    # Explicit short lists — avoid inheriting full _JIMMY_CORE_TOOLS.
    lean = list(_JIMMY_LEAN_TOOLSETS)
    lean_set = set(lean)
    known_builtin = _jimmy_known_toolset_names()
    platform_toolsets = (
        dict(cfg["platform_toolsets"])
        if isinstance(cfg.get("platform_toolsets"), dict)
        else {}
    )
    for platform in ("cli", "telegram"):
        existing = platform_toolsets.get(platform)
        # Preserve MCP / custom server names only — never re-keep built-in
        # toolsets (computer_use, browser-use, …) that used to sneak through
        # an incomplete deny-list and inflate first-turn schemas.
        preserved: list[str] = []
        if isinstance(existing, list):
            for entry in existing:
                if not isinstance(entry, str):
                    continue
                name = entry.strip()
                if not name or name in lean_set or name.startswith("jimmy-"):
                    continue
                if name == "no_mcp":
                    continue
                if name in known_builtin:
                    continue
                preserved.append(name)
        # no_mcp: opt out of default MCP schema inclusion on this platform.
        platform_toolsets[platform] = list(dict.fromkeys([*lean, "no_mcp", *preserved]))
    cfg["platform_toolsets"] = platform_toolsets

    # Mark every checklist / plugin toolset as already "seen" so
    # ``_enable_recently_shipped_toolsets`` and plugin default-on do not
    # re-inflate the lean list on the next resolve.
    try:
        from jimmy_cli.tools_config import CONFIGURABLE_TOOLSETS, _get_plugin_toolset_keys

        catalog = sorted({str(k) for k, _, _ in CONFIGURABLE_TOOLSETS})
        plugin_catalog = sorted({str(k) for k in _get_plugin_toolset_keys()})
    except Exception:
        catalog = sorted(_JIMMY_DISABLED_TOOLSETS | set(_JIMMY_LEAN_TOOLSETS))
        plugin_catalog = []
    known_builtin_map = (
        dict(cfg["known_builtin_toolsets"])
        if isinstance(cfg.get("known_builtin_toolsets"), dict)
        else {}
    )
    known_plugin_map = (
        dict(cfg["known_plugin_toolsets"])
        if isinstance(cfg.get("known_plugin_toolsets"), dict)
        else {}
    )
    for platform in ("cli", "telegram"):
        known_builtin_map[platform] = catalog
        if plugin_catalog:
            known_plugin_map[platform] = plugin_catalog
    cfg["known_builtin_toolsets"] = known_builtin_map
    if plugin_catalog or known_plugin_map:
        cfg["known_plugin_toolsets"] = known_plugin_map

    # Messaging / dashboard cwd: keep context-file discovery off the Jimmy
    # install tree and any developer checkout that happens to contain a huge
    # AGENTS.md (dominant first-turn cost when cwd is this repo).
    terminal = dict(cfg["terminal"]) if isinstance(cfg.get("terminal"), dict) else {}
    if home is not None and not str(terminal.get("cwd") or "").strip():
        terminal["cwd"] = str(home)
        cfg["terminal"] = terminal

    # Disable every configured MCP server unless Jimmy explicitly needs it.
    # Schemas still defer via tool_search; enabled:false drops them entirely.
    mcp_servers = cfg.get("mcp_servers")
    if isinstance(mcp_servers, dict):
        for name, entry in list(mcp_servers.items()):
            if not isinstance(entry, dict):
                continue
            patched = dict(entry)
            patched["enabled"] = False
            mcp_servers[name] = patched
        cfg["mcp_servers"] = mcp_servers


def _ensure_profile(profiles_root: Path, name: str, model: dict[str, Any]) -> Path:
    home = profiles_root / name
    home.mkdir(parents=True, exist_ok=True)
    (home / "memories").mkdir(exist_ok=True)
    (home / "skills").mkdir(exist_ok=True)
    (home / "sessions").mkdir(exist_ok=True)
    cfg_path = home / "config.yaml"
    cfg = _load_yaml(cfg_path)
    cfg["model"] = {**(cfg.get("model") or {}), **model}
    gateway = cfg.get("gateway") if isinstance(cfg.get("gateway"), dict) else {}
    gateway = dict(gateway)
    # Per-profile gateways are driven by the default multiplex parent.
    cfg["gateway"] = gateway
    database = dict(cfg["database"]) if isinstance(cfg.get("database"), dict) else {}
    database["journal_mode"] = "delete"
    cfg["database"] = database
    _apply_jimmy_agent_limits(cfg, home=home)

    # Optional per-Jimmy Telegram bot (Azure secrets JIMMY1_TELEGRAM_BOT_TOKEN…)
    idx = JIMMY_PROFILES.index(name) + 1 if name in JIMMY_PROFILES else 0
    tg_token = (
        os.environ.get(f"JIMMY{idx}_TELEGRAM_BOT_TOKEN", "").strip() if idx else ""
    )
    if tg_token:
        _enable_telegram_platform(cfg)
    _dump_yaml(cfg_path, cfg)
    _force_delete_journal(home)
    env_path = home / ".env"
    if not env_path.exists():
        env_path.write_text(
            "# Profile secrets. Azure OpenAI keys are mirrored here so "
            "multiplexed gateway turns can resolve them (fail-closed scope).\n",
            encoding="utf-8",
        )
    # Must run every seed: process env alone is invisible under multiplex scope.
    n = _sync_shared_provider_env(env_path)
    if n:
        print(f"seed: mirrored {n} Azure provider env key(s) into {name}")
    if tg_token:
        _upsert_env_key(env_path, "TELEGRAM_BOT_TOKEN", tg_token)
        # Allow anyone who DMs the bot (pairing still available for groups).
        allow = os.environ.get(f"JIMMY{idx}_TELEGRAM_ALLOWED_USERS", "").strip()
        if allow:
            _upsert_env_key(env_path, "TELEGRAM_ALLOWED_USERS", allow)
        else:
            # Platform allow-all: TELEGRAM_ALLOW_ALL_USERS (see gateway platforms).
            _upsert_env_key(env_path, "TELEGRAM_ALLOW_ALL_USERS", "true")
        print(f"seed: telegram token set for profile {name}")
    soul = home / "SOUL.md"
    if not soul.exists():
        soul.write_text(
            "You are Jimmy, an intelligent AI assistant. "
            "You are helpful, knowledgeable, and direct.\n",
            encoding="utf-8",
        )
    return home


def seed_jimmy_profiles(*, jimmy_home: Path | None = None) -> list[Path]:
    from jimmy_constants import get_jimmy_home
    from jimmy_cli.profiles import _get_profiles_root

    home = Path(jimmy_home or get_jimmy_home())
    home.mkdir(parents=True, exist_ok=True)
    profiles_root = _get_profiles_root()
    profiles_root.mkdir(parents=True, exist_ok=True)

    model = _azure_model_block()

    # Default home: multiplex all four profile gateways; shared model.
    default_cfg_path = home / "config.yaml"
    default_cfg = _load_yaml(default_cfg_path)
    default_cfg["model"] = {**(default_cfg.get("model") or {}), **model}
    gateway = (
        dict(default_cfg["gateway"])
        if isinstance(default_cfg.get("gateway"), dict)
        else {}
    )
    gateway["multiplex_profiles"] = True
    default_cfg["gateway"] = gateway

    # Azure Files (SMB) cannot host SQLite WAL safely — PRAGMA WAL can hang
    # indefinitely instead of raising, which surfaces as /api/sessions timeouts
    # and "Internal server error" in the dashboard. Force DELETE journal mode.
    database = (
        dict(default_cfg["database"])
        if isinstance(default_cfg.get("database"), dict)
        else {}
    )
    database["journal_mode"] = "delete"
    default_cfg["database"] = database
    _apply_jimmy_agent_limits(default_cfg, home=home)
    _force_delete_journal(home)

    # Wire multi-user basic auth when JIMMY*_PASSWORD present and users empty.
    dash = (
        dict(default_cfg["dashboard"])
        if isinstance(default_cfg.get("dashboard"), dict)
        else {}
    )
    basic = (
        dict(dash["basic_auth"])
        if isinstance(dash.get("basic_auth"), dict)
        else {}
    )
    if not basic.get("users"):
        users = []
        for i, name in enumerate(JIMMY_PROFILES, start=1):
            pw = os.environ.get(f"JIMMY{i}_PASSWORD", "").strip()
            if not pw:
                continue
            users.append(
                {
                    "username": os.environ.get(f"JIMMY{i}_USERNAME", name).strip()
                    or name,
                    "password": pw,
                    "profile": name,
                }
            )
        if users:
            basic["users"] = users
            if os.environ.get("JIMMY_DASHBOARD_BASIC_AUTH_SECRET"):
                basic["secret"] = os.environ["JIMMY_DASHBOARD_BASIC_AUTH_SECRET"]
            dash["basic_auth"] = basic
            default_cfg["dashboard"] = dash

    _dump_yaml(default_cfg_path, default_cfg)

    # Default-home .env also needs Azure keys (unscoped / default-profile paths).
    default_env = home / ".env"
    if not default_env.exists():
        default_env.write_text(
            "# Shared Jimmy secrets mirrored from the container env.\n",
            encoding="utf-8",
        )
    n = _sync_shared_provider_env(default_env)
    if n:
        print(f"seed: mirrored {n} Azure provider env key(s) into default home")

    created = [_ensure_profile(profiles_root, name, model) for name in JIMMY_PROFILES]
    return created


def main() -> None:
    paths = seed_jimmy_profiles()
    for p in paths:
        print(f"seeded {p}")


if __name__ == "__main__":
    main()
