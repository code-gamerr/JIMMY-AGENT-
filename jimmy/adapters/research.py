"""Research worker — ECC consult + optional local notes."""

from __future__ import annotations

import shutil
import threading
from pathlib import Path

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.models import TaskRecord
from jimmy.paths import worker_root
from jimmy.process import run_command


class ResearchAdapter:
    agent_id = "research"

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or worker_root("ecc")
        self._cancels: dict[str, threading.Event] = {}

    def get_capabilities(self) -> tuple[str, ...]:
        return ("research", "consult", "skills-discovery")

    def get_status(self) -> AdapterStatus:
        node = shutil.which("node")
        consult = self.root / "scripts" / "consult.js"
        ready = bool(node) and consult.is_file()
        return AdapterStatus(
            agent_id=self.agent_id,
            label="Research",
            ready=ready,
            detail="consult.js ready" if ready else "ECC consult unavailable",
            workspace=str(self.root),
            capabilities=self.get_capabilities(),
        )

    def validate_task(self, task: TaskRecord) -> tuple[bool, str]:
        st = self.get_status()
        return (True, "ok") if st.ready and task.user_request.strip() else (False, st.detail)

    def execute_task(self, task: TaskRecord, emit, cancel_event) -> AdapterResult:
        self._cancels[task.task_id] = cancel_event
        node = shutil.which("node") or "node"
        consult = str(self.root / "scripts" / "consult.js")
        result = run_command(
            task_id=task.task_id,
            argv=[node, consult, task.user_request, "--json", "--limit", "8"],
            cwd=self.root,
            timeout_s=120,
            cancel_event=cancel_event,
            on_event=emit,
        )
        success = result.get("exit_code") == 0
        return AdapterResult(
            success=success,
            summary=(result.get("stdout") or result.get("stderr") or "")[-4000:],
            files_changed=(),
            commands=(result,),
            errors=() if success else ((result.get("stderr") or "research failed")[-2000:],),
        )

    def cancel_task(self, task_id: str) -> None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
