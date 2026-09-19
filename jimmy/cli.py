"""``jimmy command-center`` / ``jimmy task`` CLI."""

from __future__ import annotations

import json
import time

from jimmy.engine import TaskEngine
from jimmy.server import serve


def cmd_command_center(args) -> None:
    verb = getattr(args, "cc_command", None) or "serve"
    if verb == "serve":
        serve(
            host=getattr(args, "host", "127.0.0.1"),
            port=int(getattr(args, "port", 8765)),
            open_browser=not getattr(args, "no_browser", False),
        )
        return
    if verb == "submit":
        engine = TaskEngine()
        task = engine.submit(
            args.message,
            agent=getattr(args, "agent", "auto"),
            telegram_chat_id=getattr(args, "telegram_chat", None),
        )
        print(json.dumps(task.to_dict(), indent=2))
        if getattr(args, "wait", False):
            deadline = time.time() + int(getattr(args, "timeout", 1800))
            while time.time() < deadline:
                current = engine.store.get_task(task.task_id)
                if current and current.status.value in {"FAILED", "COMPLETED", "CANCELLED"}:
                    print(json.dumps(current.to_dict(), indent=2))
                    return
                time.sleep(0.4)
            raise SystemExit("timeout waiting for task")
        return
    if verb == "list":
        engine = TaskEngine()
        print(json.dumps([t.to_dict() for t in engine.store.list_tasks()], indent=2))
        return
    if verb == "show":
        engine = TaskEngine()
        task = engine.store.get_task(args.task_id)
        if not task:
            raise SystemExit("task not found")
        events = [e.to_dict() for e in engine.store.list_events(args.task_id)]
        print(json.dumps({"task": task.to_dict(), "events": events}, indent=2))
        return
    if verb == "cancel":
        engine = TaskEngine()
        task = engine.cancel(args.task_id)
        if not task:
            raise SystemExit("task not found")
        print(json.dumps(task.to_dict(), indent=2))
        return
    raise SystemExit(f"unknown command-center verb {verb}")
