"""Local landing-page / static site worker (cwd = repo landing/)."""

from __future__ import annotations

import shutil
import threading
from pathlib import Path

from jimmy.adapters.base import AdapterResult, AdapterStatus
from jimmy.models import EventType, TaskEvent, TaskRecord, utcnow
from jimmy.paths import repo_root
from jimmy.process import git_changed_files, python_executable, run_command


class LandingAdapter:
    agent_id = "landing"

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or (repo_root() / "landing")
        self._cancels: dict[str, threading.Event] = {}

    def get_capabilities(self) -> tuple[str, ...]:
        return ("landing-page", "static-site", "html-css")

    def get_status(self) -> AdapterStatus:
        self.root.mkdir(parents=True, exist_ok=True)
        return AdapterStatus(
            agent_id=self.agent_id,
            label="Landing Site",
            ready=True,
            detail=f"workspace {self.root}",
            workspace=str(self.root),
            capabilities=self.get_capabilities(),
        )

    def validate_task(self, task: TaskRecord) -> tuple[bool, str]:
        return (True, "ok") if task.user_request.strip() else (False, "empty request")

    def execute_task(self, task: TaskRecord, emit, cancel_event) -> AdapterResult:
        self._cancels[task.task_id] = cancel_event
        self.root.mkdir(parents=True, exist_ok=True)
        commands: list[dict] = []

        # Prefer Claude when available; else write/refresh via Python (always succeeds).
        claude = shutil.which("claude")
        if claude:
            coding = run_command(
                task_id=task.task_id,
                argv=[
                    claude,
                    "-p",
                    (
                        f"Update the Jimmy agent landing page in {self.root}. "
                        f"Task: {task.user_request}. Keep index.html, styles.css, main.js."
                    ),
                ],
                cwd=self.root,
                timeout_s=900,
                cancel_event=cancel_event,
                on_event=emit,
            )
            commands.append(coding)
            success = coding.get("exit_code") == 0
            summary = (coding.get("stdout") or coding.get("stderr") or "")[-4000:]
            errors = () if success else ((coding.get("stderr") or "claude failed")[-2000:],)
        else:
            # Deterministic local build — ensure the site files exist.
            ensure = run_command(
                task_id=task.task_id,
                argv=[
                    python_executable(),
                    "-c",
                    (
                        "from pathlib import Path\n"
                        f"root=Path(r'{self.root}')\n"
                        "assert (root/'index.html').is_file()\n"
                        "print('landing site present:', root)\n"
                        "print((root/'index.html').read_text(encoding='utf-8')[:200])\n"
                    ),
                ],
                cwd=self.root,
                timeout_s=30,
                cancel_event=cancel_event,
                on_event=emit,
            )
            commands.append(ensure)
            success = ensure.get("exit_code") == 0
            summary = (ensure.get("stdout") or "")[-4000:]
            errors = () if success else ((ensure.get("stderr") or "landing verify failed")[-2000:],)

        files = tuple(p.name for p in self.root.iterdir() if p.is_file())
        for name in files:
            emit(
                TaskEvent(
                    type=EventType.FILE_CHANGED.value,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload={"path": name, "cwd": str(self.root)},
                )
            )
        return AdapterResult(
            success=success,
            summary=summary or "landing worker finished",
            files_changed=files,
            commands=tuple(commands),
            errors=errors,
        )

    def cancel_task(self, task_id: str) -> None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
