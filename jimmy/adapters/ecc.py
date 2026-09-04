"""ECC worker: real `scripts/ecc.js` (and related Node CLIs) in the ECC tree."""

from __future__ import annotations

import shutil
import threading
from pathlib import Path

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.models import TaskRecord
from jimmy.paths import worker_root
from jimmy.process import git_changed_files, run_command


class EccAdapter:
    agent_id = "ecc"

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or worker_root("ecc")
        self._cancels: dict[str, threading.Event] = {}

    def get_capabilities(self) -> tuple[str, ...]:
        return (
            "ecc-cli",
            "skills-hooks",
            "consult",
            "doctor",
            "memory-vault",
            "control-pane",
        )

    def get_status(self) -> AdapterStatus:
        from jimmy.adapters.base import AdapterStatus as Status

        ecc_js = self.root / "scripts" / "ecc.js"
        node = shutil.which("node")
        ready = ecc_js.is_file() and bool(node)
        detail = "ecc.js present" if ecc_js.is_file() else "ECC scripts/ecc.js missing"
        if not node:
            detail = "node not on PATH"
        return Status(
            agent_id=self.agent_id,
            label="ECC",
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

    def _argv_for(self, request: str) -> list[list[str]]:
        node = shutil.which("node") or "node"
        ecc = str(self.root / "scripts" / "ecc.js")
        consult = str(self.root / "scripts" / "consult.js")
        low = request.lower()
        if "doctor" in low:
            return [[node, ecc, "doctor"]]
        if "status" in low and "loop" not in low:
            return [[node, ecc, "status"]]
        if "memory" in low:
            return [[node, ecc, "memory", "--help"]]
        if "control pane" in low or "control-pane" in low:
            return [[node, ecc, "help", "control-pane"]]
        # Default: live consult against the real ECC catalog (no install).
        return [
            [node, ecc, "status"],
            [node, consult, request, "--json", "--limit", "8"],
        ]

    def execute_task(self, task: TaskRecord, emit, cancel_event) -> AdapterResult:
        self._cancels[task.task_id] = cancel_event
        commands: list[dict] = []
        last = {"exit_code": 1, "stdout": "", "stderr": ""}
        for argv in self._argv_for(task.user_request):
            last = run_command(
                task_id=task.task_id,
                argv=argv,
                cwd=self.root,
                timeout_s=120,
                cancel_event=cancel_event,
                on_event=emit,
            )
            commands.append(last)
            if last.get("exit_code") not in (0,):
                break
        files = tuple(git_changed_files(self.root))
        success = last.get("exit_code") == 0
        errors = () if success else ((last.get("stderr") or last.get("stdout") or "ecc failed")[-2000:],)
        summary = (last.get("stdout") or last.get("stderr") or "").strip()[-4000:]
        return AdapterResult(
            success=bool(success),
            summary=summary or ("ECC command ok" if success else "ECC command failed"),
            files_changed=files,
            commands=tuple(commands),
            errors=errors,
        )

    def cancel_task(self, task_id: str) -> None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
