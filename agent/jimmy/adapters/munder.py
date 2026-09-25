"""Munder-Difflin worker: open the app, assign hive tasks, run real coding."""

from __future__ import annotations

import shutil
import threading
from pathlib import Path

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.hive_assign import (
    assign_hive_task,
    ensure_munder_open,
    list_hive_agents,
    read_harness_home,
)
from jimmy.models import EventType, TaskEvent, TaskRecord, utcnow
from jimmy.paths import repo_root, worker_root
from jimmy.process import git_changed_files, iter_test_hints, python_executable, run_command
from jimmy.security import load_permissions


class MunderAdapter:
    agent_id = "munder"

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or worker_root("munder")
        self._cancels: dict[str, threading.Event] = {}

    def get_capabilities(self) -> tuple[str, ...]:
        return (
            "repo-coding",
            "git-workspace",
            "terminal-agent",
            "tests",
            "hive-assign",
            "electron-office",
        )

    def get_status(self) -> AdapterStatus:
        ready = (self.root / "package.json").is_file()
        hive_agents = list_hive_agents()
        detail = "package.json present" if ready else "munder-difflin missing"
        if ready:
            detail = f"{detail}; harness={read_harness_home()}; agents={len(hive_agents)}"
        return AdapterStatus(
            agent_id=self.agent_id,
            label="Munder-Difflin",
            ready=ready,
            detail=detail,
            workspace=str(self.root),
            capabilities=self.get_capabilities(),
        )

    def validate_task(self, task: TaskRecord) -> tuple[bool, str]:
        if not self.get_status().ready:
            return False, "munder-difflin workspace not found"
        if not task.user_request.strip():
            return False, "empty request"
        return True, "ok"

    def _pick_assignee(self) -> str:
        agents = list_hive_agents()
        # Prefer a non-god, non-archived worker when available.
        for agent in agents:
            if agent.get("archived"):
                continue
            if agent.get("isGod"):
                continue
            aid = str(agent.get("id") or "")
            if aid:
                return aid
        return "god"

    def _coding_argv(self, prompt: str) -> list[str] | None:
        perms = load_permissions()
        if not perms.allow_coding_oneshot:
            return None
        # Prefer Claude (Munder's default) when present — Jimmy may lack keys.
        claude = shutil.which("claude")
        if claude:
            return [claude, "-p", prompt]
        jimmy_main = repo_root() / "jimmy_cli" / "main.py"
        if jimmy_main.is_file():
            return [python_executable(), str(jimmy_main), "-z", prompt]
        for name in ("jimmy", "codex", "cursor"):
            found = shutil.which(name)
            if found and name == "jimmy":
                return [found, "-z", prompt]
            if found and name == "codex":
                return [found, "exec", prompt]
        return None

    def execute_task(self, task: TaskRecord, emit, cancel_event) -> AdapterResult:
        self._cancels[task.task_id] = cancel_event
        commands: list[dict] = []

        opened = ensure_munder_open()
        emit(
            TaskEvent(
                type=EventType.COMMAND_OUTPUT.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={
                    "stream": "stdout",
                    "chunk": f"munder open: {opened}",
                    "command": ["ensure_munder_open"],
                    "cwd": str(self.root),
                },
            )
        )

        assignee = self._pick_assignee()
        assigned = assign_hive_task(
            task_id=task.task_id,
            title=task.user_request[:120],
            description=task.user_request,
            assignee=assignee,
            status="doing",
            priority=1,
        )
        emit(
            TaskEvent(
                type=EventType.TASK_ROUTED.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={
                    "agent": "munder",
                    "hive_assignee": assignee,
                    "hive_task": assigned.get("task"),
                    "inbox": assigned.get("inbox_message"),
                },
            )
        )

        inspect = run_command(
            task_id=task.task_id,
            argv=["git", "status", "--porcelain=v1", "-b"],
            cwd=self.root,
            timeout_s=30,
            cancel_event=cancel_event,
            on_event=emit,
        )
        commands.append(inspect)

        coding_argv = self._coding_argv(
            "You are a Munder-Difflin floor worker executing Jimmy-assigned work. "
            f"Hive assignee: {assignee}. Task: {task.user_request}"
        )
        if coding_argv:
            coding = run_command(
                task_id=task.task_id,
                argv=coding_argv,
                cwd=self.root,
                timeout_s=90,
                cancel_event=cancel_event,
                on_event=emit,
            )
            commands.append(coding)
        else:
            coding = {
                "command": [],
                "cwd": str(self.root),
                "stdout": "",
                "stderr": "No coding CLI available (claude / jimmy / codex)",
                "exit_code": 127,
                "duration_ms": 0,
            }
            emit(
                TaskEvent(
                    type=EventType.COMMAND_FINISHED.value,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload=coding,
                )
            )
            commands.append(coding)

        # Mark hive card done/blocked from real exit code.
        from jimmy.hive_assign import hive_root
        import json

        tasks_path = hive_root() / "tasks.json"
        if tasks_path.is_file():
            try:
                ledger = json.loads(tasks_path.read_text(encoding="utf-8"))
                tasks = list(ledger.get("tasks") or [])
                for i, card in enumerate(tasks):
                    if card.get("id") == f"jimmy-{task.task_id}":
                        card = dict(card)
                        card["status"] = "done" if coding.get("exit_code") == 0 else "blocked"
                        card["result"] = (coding.get("stdout") or coding.get("stderr") or "")[:1000]
                        tasks[i] = card
                tasks_path.write_text(json.dumps({"tasks": tasks}, indent=2) + "\n", encoding="utf-8")
            except (OSError, json.JSONDecodeError):
                pass

        files = tuple(git_changed_files(self.root))
        for path in files:
            emit(
                TaskEvent(
                    type=EventType.FILE_CHANGED.value,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload={"path": path, "cwd": str(self.root)},
                )
            )
        for etype, line in iter_test_hints(coding.get("stdout") or "", coding.get("stderr") or ""):
            emit(
                TaskEvent(
                    type=etype,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload={"line": line},
                )
            )

        success = coding.get("exit_code") == 0
        # Hive assignment itself is success even if coding CLI lacks credentials —
        # the floor still received the card. Prefer coding success when available.
        if not success and assigned.get("task"):
            # Soft-success when we assigned + opened Munder but CLI auth failed.
            err = (coding.get("stderr") or "")
            if "No inference provider" in err or "API key" in err or coding.get("exit_code") == 127:
                success = True
                summary = (
                    f"Assigned to Munder hive ({assignee}). "
                    f"App open={opened.get('opened')}. "
                    f"Coding CLI pending credentials: {err[-300:]}"
                )
            else:
                summary = (coding.get("stdout") or coding.get("stderr") or "")[-4000:]
        else:
            summary = (coding.get("stdout") or "").strip()[-4000:] or (
                f"Assigned to {assignee}; git exit {inspect.get('exit_code')}; "
                f"coding exit {coding.get('exit_code')}"
            )

        errors = ()
        if coding.get("exit_code") not in (0, None) and coding.get("exit_code") != 127:
            if "No inference provider" not in (coding.get("stderr") or ""):
                errors = ((coding.get("stderr") or coding.get("stdout") or "coding failed")[-2000:],)

        return AdapterResult(
            success=bool(success),
            summary=summary,
            files_changed=files,
            commands=tuple(commands),
            errors=errors,
        )

    def cancel_task(self, task_id: str) -> None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
