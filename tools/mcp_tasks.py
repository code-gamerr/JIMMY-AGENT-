"""Durable MCP long-running task store (DeerFlow mcp_tasks parity, Jimmy-native).

Persists submit/list/cancel state under ``~/.jimmy/mcp_tasks.sqlite3`` so tasks
survive process restarts. Execution is a thin wrapper around MCP tool calls
that may run longer than a single agent turn.
"""

from __future__ import annotations

import json
import logging
import sqlite3
import threading
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

from jimmy_constants import get_jimmy_home
from tools.registry import registry, tool_error

logger = logging.getLogger(__name__)

_LOCK = threading.Lock()
_VALID_STATUS = frozenset({"pending", "running", "completed", "failed", "cancelled"})

MCP_TASK_SCHEMA = {
    "name": "mcp_task",
    "description": (
        "Submit, list, status-check, or cancel a durable long-running MCP tool "
        "invocation. Use when an MCP server tool may take minutes and should "
        "survive across turns. Actions: submit | list | status | cancel."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["submit", "list", "status", "cancel"],
                "description": "Operation to perform.",
            },
            "server": {
                "type": "string",
                "description": "MCP server name (required for submit).",
            },
            "tool": {
                "type": "string",
                "description": "MCP tool name (required for submit).",
            },
            "arguments": {
                "type": "object",
                "description": "JSON arguments for the MCP tool (submit).",
            },
            "task_id": {
                "type": "string",
                "description": "Task id for status/cancel.",
            },
        },
        "required": ["action"],
    },
}


def _db_path() -> Path:
    return get_jimmy_home() / "mcp_tasks.sqlite3"


@contextmanager
def _conn() -> Iterator[sqlite3.Connection]:
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), timeout=30)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS mcp_tasks (
                id TEXT PRIMARY KEY,
                server TEXT NOT NULL,
                tool TEXT NOT NULL,
                arguments TEXT NOT NULL,
                status TEXT NOT NULL,
                result TEXT,
                error TEXT,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL
            )
            """
        )
        yield conn
        conn.commit()
    finally:
        conn.close()


def _row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    return {
        "task_id": row["id"],
        "server": row["server"],
        "tool": row["tool"],
        "arguments": json.loads(row["arguments"] or "{}"),
        "status": row["status"],
        "result": json.loads(row["result"]) if row["result"] else None,
        "error": row["error"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def submit_task(server: str, tool: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    task_id = uuid.uuid4().hex[:16]
    now = time.time()
    args = arguments if isinstance(arguments, dict) else {}
    with _LOCK, _conn() as conn:
        conn.execute(
            "INSERT INTO mcp_tasks (id, server, tool, arguments, status, result, error, created_at, updated_at) "
            "VALUES (?, ?, ?, ?, 'pending', NULL, NULL, ?, ?)",
            (task_id, server, tool, json.dumps(args), now, now),
        )
    # Best-effort inline kickoff on a daemon thread.
    threading.Thread(
        target=_run_task,
        args=(task_id,),
        name=f"mcp-task-{task_id}",
        daemon=True,
    ).start()
    return {"ok": True, "task_id": task_id, "status": "pending"}


def _run_task(task_id: str) -> None:
    with _LOCK, _conn() as conn:
        row = conn.execute("SELECT * FROM mcp_tasks WHERE id = ?", (task_id,)).fetchone()
        if not row or row["status"] == "cancelled":
            return
        conn.execute(
            "UPDATE mcp_tasks SET status = 'running', updated_at = ? WHERE id = ?",
            (time.time(), task_id),
        )
        server, tool = row["server"], row["tool"]
        arguments = json.loads(row["arguments"] or "{}")

    error: Optional[str] = None
    result: Any = None
    try:
        from tools.mcp_tool import mcp_prefixed_tool_name
        from tools.registry import registry

        tool_name = mcp_prefixed_tool_name(server, tool)
        result = registry.dispatch(tool_name, arguments or {})
        if isinstance(result, dict) and result.get("error"):
            error = str(result["error"])
            result = None
    except Exception as exc:
        error = str(exc)
        logger.warning("mcp_task %s failed: %s", task_id, exc)

    with _LOCK, _conn() as conn:
        current = conn.execute(
            "SELECT status FROM mcp_tasks WHERE id = ?", (task_id,)
        ).fetchone()
        if current and current["status"] == "cancelled":
            return
        if error:
            conn.execute(
                "UPDATE mcp_tasks SET status = 'failed', error = ?, updated_at = ? WHERE id = ?",
                (error, time.time(), task_id),
            )
        else:
            payload = result if isinstance(result, str) else json.dumps(result)
            conn.execute(
                "UPDATE mcp_tasks SET status = 'completed', result = ?, updated_at = ? WHERE id = ?",
                (payload, time.time(), task_id),
            )


def list_tasks(limit: int = 50) -> List[Dict[str, Any]]:
    with _LOCK, _conn() as conn:
        rows = conn.execute(
            "SELECT * FROM mcp_tasks ORDER BY created_at DESC LIMIT ?",
            (max(1, min(limit, 200)),),
        ).fetchall()
    return [_row_to_dict(r) for r in rows]


def get_task(task_id: str) -> Optional[Dict[str, Any]]:
    with _LOCK, _conn() as conn:
        row = conn.execute("SELECT * FROM mcp_tasks WHERE id = ?", (task_id,)).fetchone()
    return _row_to_dict(row) if row else None


def cancel_task(task_id: str) -> Dict[str, Any]:
    with _LOCK, _conn() as conn:
        row = conn.execute("SELECT status FROM mcp_tasks WHERE id = ?", (task_id,)).fetchone()
        if not row:
            return {"ok": False, "error": f"unknown task_id: {task_id}"}
        if row["status"] in {"completed", "failed", "cancelled"}:
            return {"ok": True, "task_id": task_id, "status": row["status"]}
        conn.execute(
            "UPDATE mcp_tasks SET status = 'cancelled', updated_at = ? WHERE id = ?",
            (time.time(), task_id),
        )
    return {"ok": True, "task_id": task_id, "status": "cancelled"}


def mcp_task_tool(
    action: str,
    server: Optional[str] = None,
    tool: Optional[str] = None,
    arguments: Optional[Dict[str, Any]] = None,
    task_id: Optional[str] = None,
) -> str:
    action = (action or "").strip().lower()
    if action == "submit":
        if not server or not tool:
            return tool_error("submit requires server and tool")
        return json.dumps(submit_task(server, tool, arguments))
    if action == "list":
        return json.dumps({"ok": True, "tasks": list_tasks()})
    if action == "status":
        if not task_id:
            return tool_error("status requires task_id")
        task = get_task(task_id)
        if not task:
            return tool_error(f"unknown task_id: {task_id}")
        return json.dumps({"ok": True, "task": task})
    if action == "cancel":
        if not task_id:
            return tool_error("cancel requires task_id")
        return json.dumps(cancel_task(task_id))
    return tool_error(f"unknown action: {action}")


registry.register(
    name="mcp_task",
    toolset="mcp",
    schema=MCP_TASK_SCHEMA,
    handler=lambda args: mcp_task_tool(
        action=args.get("action", ""),
        server=args.get("server"),
        tool=args.get("tool"),
        arguments=args.get("arguments"),
        task_id=args.get("task_id"),
    ),
    check_fn=None,
    emoji="⏳",
)
