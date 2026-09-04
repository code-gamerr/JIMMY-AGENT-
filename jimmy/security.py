"""Local-only auth, per-agent permissions, command allowlist, audit log."""

from __future__ import annotations

import json
import os
import secrets
import threading
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from pathlib import Path

from jimmy.paths import audit_path, auth_path, jimmy_home

ALLOWED_BINARIES = frozenset(
    {
        "node",
        "npm",
        "npx",
        "pnpm",
        "git",
        "python",
        "python3",
        "py",
        "jimmy",
        "jimmy",
        "claude",
        "codex",
        "cursor",
        "ecc",
        "ecc-universal",
        "openclaw",
    }
)

# Denied even if the basename would otherwise match.
DENIED_SUBSTRINGS = (
    "rm -rf /",
    "format c:",
    "shutdown",
    "mkfs",
)


@dataclass(frozen=True)
class Permissions:
    agents: dict[str, bool] = field(
        default_factory=lambda: {
            "openclaw": True,
            "munder": True,
            "ecc": True,
            "landing": True,
            "research": True,
        }
    )
    allow_coding_oneshot: bool = True
    max_concurrent_tasks: int = 3


def load_or_create_token() -> str:
    path = auth_path()
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        token = str(data.get("token") or "")
        if token:
            return token
    token = secrets.token_urlsafe(32)
    path.write_text(
        json.dumps({"token": token, "created_at": datetime.now(timezone.utc).isoformat()}),
        encoding="utf-8",
    )
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return token


def token_matches(provided: str | None, expected: str) -> bool:
    if not provided:
        return False
    return secrets.compare_digest(provided.strip(), expected)


def load_permissions() -> Permissions:
    cfg = jimmy_home() / "permissions.json"
    if not cfg.is_file():
        perms = Permissions()
        cfg.write_text(
            json.dumps(
                {
                    "agents": dict(perms.agents),
                    "allow_coding_oneshot": perms.allow_coding_oneshot,
                    "max_concurrent_tasks": perms.max_concurrent_tasks,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        return perms
    data = json.loads(cfg.read_text(encoding="utf-8"))
    agents = dict(Permissions().agents)
    agents.update({str(k): bool(v) for k, v in (data.get("agents") or {}).items()})
    return Permissions(
        agents=agents,
        allow_coding_oneshot=bool(data.get("allow_coding_oneshot", True)),
        max_concurrent_tasks=int(data.get("max_concurrent_tasks") or 3),
    )


def agent_allowed(agent_id: str, perms: Permissions | None = None) -> bool:
    perms = perms or load_permissions()
    return bool(perms.agents.get(agent_id, False))


def command_allowed(argv: list[str]) -> tuple[bool, str]:
    if not argv:
        return False, "empty command"
    joined = " ".join(argv).lower()
    for bad in DENIED_SUBSTRINGS:
        if bad in joined:
            return False, f"blocked pattern: {bad}"
    binary = Path(argv[0]).name.lower()
    for suffix in (".exe", ".cmd", ".bat", ".ps1"):
        if binary.endswith(suffix):
            binary = binary[: -len(suffix)]
            break
    if binary.startswith("python") or binary in {"py", "node"}:
        return True, "ok"
    if binary not in ALLOWED_BINARIES:
        return False, f"binary not allowlisted: {binary}"
    return True, "ok"


_audit_lock = threading.Lock()


def audit(action: str, detail: dict) -> None:
    line = json.dumps(
        {
            "ts": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "detail": detail,
        }
    )
    path = audit_path()
    with _audit_lock:
        with path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def read_audit(limit: int = 200) -> list[dict]:
    path = audit_path()
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines[-limit:]:
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def replace_permissions(perms: Permissions) -> Permissions:
    return replace(perms)
