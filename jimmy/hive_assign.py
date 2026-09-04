"""Assign real work into the live Munder-Difflin hive (tasks.json + god inbox)."""

from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from jimmy.paths import repo_root

DEFAULT_HARNESS = Path.home() / "Documents" / "hAR"
MUNDER_CONFIG = Path(os.environ.get("APPDATA", "")) / "munder-difflin" / "config.json"


def munder_config_path() -> Path:
    return MUNDER_CONFIG


def read_harness_home() -> Path:
    cfg = munder_config_path()
    if cfg.is_file():
        try:
            data = json.loads(cfg.read_text(encoding="utf-8"))
            home = data.get("harnessHome")
            if home:
                return Path(str(home))
        except (OSError, json.JSONDecodeError):
            pass
    return DEFAULT_HARNESS


def hive_root() -> Path:
    return read_harness_home() / "hive"


def is_munder_running() -> bool:
    if os.name == "nt":
        try:
            out = subprocess.check_output(
                ["tasklist", "/FI", "IMAGENAME eq electron.exe"],
                text=True,
                errors="replace",
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            return "electron.exe" in out.lower()
        except (OSError, subprocess.CalledProcessError):
            return False
    try:
        out = subprocess.check_output(["pgrep", "-fl", "electron"], text=True, errors="replace")
        return "munder" in out.lower() or "electron" in out.lower()
    except (OSError, subprocess.CalledProcessError):
        return False


def ensure_munder_open() -> dict:
    """Launch Munder Electron if needed. Returns status dict with real process info."""
    if is_munder_running():
        return {"opened": True, "already_running": True, "pid": None}
    munder = repo_root() / "munder-difflin"
    if not (munder / "package.json").is_file():
        return {"opened": False, "already_running": False, "error": "munder-difflin missing"}
    creation = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0) | getattr(
        subprocess, "CREATE_NO_WINDOW", 0
    )
    proc = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=str(munder),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=(os.name == "nt"),
        creationflags=creation if os.name == "nt" else 0,
    )
    # Give Electron a moment to spawn.
    for _ in range(40):
        if is_munder_running():
            return {"opened": True, "already_running": False, "pid": proc.pid}
        time.sleep(0.5)
    return {
        "opened": is_munder_running(),
        "already_running": False,
        "pid": proc.pid,
        "note": "spawned npm run dev; electron window may still be booting",
    }


def _atomic_write(path: Path, data: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def assign_hive_task(
    *,
    task_id: str,
    title: str,
    description: str,
    assignee: str = "god",
    status: str = "todo",
    priority: int = 1,
) -> dict:
    """Write a HiveTask into the live hive ledger and notify god via inbox."""
    root = hive_root()
    root.mkdir(parents=True, exist_ok=True)
    tasks_path = root / "tasks.json"
    if tasks_path.is_file():
        try:
            ledger = json.loads(tasks_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            ledger = {"tasks": []}
    else:
        ledger = {"tasks": []}
    tasks = list(ledger.get("tasks") or [])
    created = datetime.now(timezone.utc).isoformat()
    card = {
        "id": f"jimmy-{task_id}",
        "title": title[:200],
        "description": description[:4000],
        "assignee": assignee,
        "status": status,
        "dependsOn": [],
        "priority": priority,
        "createdAt": created,
        "origin": "jimmy-orchestrator",
    }
    # Replace same id if re-assigned.
    tasks = [t for t in tasks if t.get("id") != card["id"]]
    tasks.append(card)
    _atomic_write(tasks_path, {"tasks": tasks})

    # Activity log for the floor UI.
    log_path = root / "log.jsonl"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(
            json.dumps(
                {
                    "ts": created,
                    "kind": "jimmy.assign",
                    "task_id": card["id"],
                    "assignee": assignee,
                    "title": title,
                }
            )
            + "\n"
        )

    # Deliver to god inbox so Michael/KING sees the work.
    inbox = root / "agents" / "god" / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    msg_id = f"{created.replace(':', '-')}-{task_id}"
    msg = {
        "id": msg_id,
        "conversation": f"jimmy-{task_id}",
        "in_reply_to": None,
        "from": "jimmy",
        "to": "god",
        "act": "request",
        "subject": title[:120],
        "body": (
            f"Jimmy orchestrator assigned work.\n\n"
            f"**Task:** {title}\n\n{description}\n\n"
            f"Card id: `{card['id']}` — also on tasks.json (status={status}, assignee={assignee})."
        ),
        "hops": 0,
        "requires_reply": True,
        "needs_human": False,
        "created_at": created,
    }
    (inbox / f"{msg_id}.json").write_text(json.dumps(msg, indent=2) + "\n", encoding="utf-8")

    # Board note (append-only hint; god is scribe for full board).
    board = root / "board.md"
    note = f"\n\n## Jimmy assignment {created}\n- [{status}] {title} → `{assignee}` (`{card['id']}`)\n"
    if board.is_file():
        board.write_text(board.read_text(encoding="utf-8") + note, encoding="utf-8")
    else:
        board.write_text("# Board\n" + note, encoding="utf-8")

    return {
        "hive": str(root),
        "task": card,
        "inbox_message": str(inbox / f"{msg_id}.json"),
        "tasks_path": str(tasks_path),
    }


def list_hive_agents() -> list[dict]:
    reg = hive_root() / "registry.json"
    if not reg.is_file():
        return []
    try:
        data = json.loads(reg.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    agents = data.get("agents") or {}
    return [dict(v) for v in agents.values() if isinstance(v, dict)]
