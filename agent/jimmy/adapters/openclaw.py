"""OpenClaw worker: real `openclaw.mjs` process in the nested checkout."""

from __future__ import annotations

import shutil
import threading
from pathlib import Path

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.models import EventType, TaskEvent, TaskRecord, utcnow
from jimmy.paths import worker_root
from jimmy.process import run_command


class OpenClawAdapter:
    agent_id = "openclaw"

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or worker_root("openclaw")
        self._cancels: dict[str, threading.Event] = {}

    def get_capabilities(self) -> tuple[str, ...]:
        return (
            "messaging-gateway",
            "channels",
            "openclaw-cli",
            "device-nodes",
        )

    def get_status(self) -> AdapterStatus:
        launcher = self.root / "openclaw.mjs"
        node = shutil.which("node")
        ready = launcher.is_file() and bool(node)
        detail = "launcher present" if launcher.is_file() else "openclaw.mjs missing"
        if not node:
            detail = "node not on PATH"
        return AdapterStatus(
            agent_id=self.agent_id,
            label="OpenClaw",
            ready=ready,
            detail=detail,
            workspace=str(self.root),
            capabilities=self.get_capabilities(),
        )

    def validate_task(self, task: TaskRecord) -> tuple[bool, str]:
        status = self.get_status()
        if not status.ready:
            return False, status.detail
        if not task.user_request.strip():
            return False, "empty request"
        return True, "ok"

    def execute_task(self, task: TaskRecord, emit, cancel_event) -> AdapterResult:
        self._cancels[task.task_id] = cancel_event
        node = shutil.which("node") or "node"
        launcher = str(self.root / "openclaw.mjs")
        commands: list[dict] = []

        probe = run_command(
            task_id=task.task_id,
            argv=[node, launcher, "--help"],
            cwd=self.root,
            timeout_s=60,
            cancel_event=cancel_event,
            on_event=emit,
        )
        commands.append(probe)

        # Isolated state so we never touch the operator's live ~/.openclaw gateway.
        env = {
            "OPENCLAW_STATE_DIR": str(self.root / ".jimmy-task-state" / task.task_id),
        }
        Path(env["OPENCLAW_STATE_DIR"]).mkdir(parents=True, exist_ok=True)

        message = run_command(
            task_id=task.task_id,
            argv=[node, launcher, "agent", "--message", task.user_request],
            cwd=self.root,
            env=env,
            timeout_s=900,
            cancel_event=cancel_event,
            on_event=emit,
        )
        commands.append(message)

        success = message.get("exit_code") == 0
        errors = ()
        if not success:
            err = (message.get("stderr") or message.get("stdout") or "openclaw agent failed").strip()
            errors = (err[-2000:],)
            emit(
                TaskEvent(
                    type=EventType.TASK_FAILED.value,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload={"error": errors[0], "exit_code": message.get("exit_code")},
                )
            )
        summary = (message.get("stdout") or message.get("stderr") or "").strip()[-4000:]
        if probe.get("exit_code") not in (0, None) and not summary:
            summary = (probe.get("stderr") or "")[-4000:]
            success = False
            errors = (summary or "openclaw launcher failed",)
        return AdapterResult(
            success=success,
            summary=summary or ("OpenClaw agent exited 0" if success else "OpenClaw failed"),
            files_changed=(),
            commands=tuple(commands),
            errors=errors,
        )

    def cancel_task(self, task_id: str) -> None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
