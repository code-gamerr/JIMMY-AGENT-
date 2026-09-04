"""Task engine: plan → execute → observe → evaluate → store experience."""

from __future__ import annotations

import threading
import uuid
from collections.abc import Callable

from jimmy.adapters import build_adapters
from jimmy.events import EventBus
from jimmy.models import (
    EventType,
    Experience,
    TaskEvent,
    TaskRecord,
    TaskStatus,
    TERMINAL_STATUSES,
    new_task_id,
    utcnow,
)
from jimmy.planner import plan_request
from jimmy.security import agent_allowed, audit, load_permissions
from jimmy.store import OrchestratorStore

Emit = Callable[[TaskEvent], None]


class TaskEngine:
    def __init__(
        self,
        store: OrchestratorStore | None = None,
        bus: EventBus | None = None,
        adapters: dict | None = None,
    ) -> None:
        self.store = store or OrchestratorStore()
        self.bus = bus or EventBus()
        self.adapters = adapters or build_adapters()
        self._cancels: dict[str, threading.Event] = {}
        self._lock = threading.Lock()

    def emit(self, event: TaskEvent) -> None:
        self.store.append_event(event)
        self.bus.publish(event)
        task = self.store.get_task(event.task_id)
        if not task:
            return
        log_line = f"{event.ts} {event.type}"
        extra = event.payload.get("chunk") or event.payload.get("path") or event.payload.get("error")
        if extra:
            log_line = f"{log_line} {extra}"
        logs = task.logs + (log_line,)
        files = task.files_changed
        if event.type == EventType.FILE_CHANGED.value:
            path = str(event.payload.get("path") or "")
            if path and path not in files:
                files = files + (path,)
        errors = task.errors
        if event.type in {EventType.TASK_FAILED.value, EventType.TEST_FAILED.value}:
            err = str(event.payload.get("error") or event.payload.get("line") or "")
            if err:
                errors = errors + (err,)
        self.store.save_task(task.evolve(logs=logs[-500:], files_changed=files, errors=errors[-50:]))

    def submit(self, user_request: str, agent: str | None = None) -> TaskRecord:
        task = TaskRecord(
            task_id=new_task_id(),
            user_request=user_request.strip(),
            selected_agent=None if agent in (None, "auto") else agent,
            status=TaskStatus.QUEUED,
            current_step="queued",
        )
        self.store.save_task(task)
        self.emit(
            TaskEvent(
                type=EventType.TASK_CREATED.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={"user_request": task.user_request},
            )
        )
        audit("task.created", {"task_id": task.task_id, "agent": agent})
        thread = threading.Thread(target=self._run, args=(task.task_id,), daemon=True)
        thread.start()
        return self.store.get_task(task.task_id) or task

    def cancel(self, task_id: str) -> TaskRecord | None:
        ev = self._cancels.get(task_id)
        if ev:
            ev.set()
        adapter_id = (self.store.get_task(task_id) or TaskRecord(task_id="", user_request="")).selected_agent
        if adapter_id and adapter_id in self.adapters:
            self.adapters[adapter_id].cancel_task(task_id)
        task = self.store.get_task(task_id)
        if task and task.status not in TERMINAL_STATUSES:
            task = task.evolve(
                status=TaskStatus.CANCELLED,
                current_step="cancelled",
                completed_at=utcnow(),
            )
            self.store.save_task(task)
            self.emit(
                TaskEvent(
                    type=EventType.TASK_CANCELLED.value,
                    task_id=task_id,
                    ts=utcnow(),
                    payload={},
                )
            )
            audit("task.cancelled", {"task_id": task_id})
        return self.store.get_task(task_id)

    def _run(self, task_id: str) -> None:
        cancel = threading.Event()
        self._cancels[task_id] = cancel
        task = self.store.get_task(task_id)
        if not task:
            return
        try:
            self._run_inner(task, cancel)
        except Exception as exc:
            task = self.store.get_task(task_id) or task
            task = task.evolve(
                status=TaskStatus.FAILED,
                current_step="failed",
                completed_at=utcnow(),
                errors=task.errors + (str(exc),),
            )
            self.store.save_task(task)
            self.emit(
                TaskEvent(
                    type=EventType.TASK_FAILED.value,
                    task_id=task_id,
                    ts=utcnow(),
                    payload={"error": str(exc)},
                )
            )

    def _run_inner(self, task: TaskRecord, cancel: threading.Event) -> None:
        task = task.evolve(status=TaskStatus.PLANNING, current_step="planning")
        self.store.save_task(task)
        self.emit(
            TaskEvent(
                type=EventType.TASK_PLANNING.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={"user_request": task.user_request},
            )
        )
        prior = self.store.search_experiences(task.user_request, limit=5)
        plan = plan_request(
            task.user_request,
            explicit_agent=task.selected_agent,
            experiences=prior,
        )
        workers = tuple(plan.workers) or (plan.agent,)
        perms = load_permissions()
        for worker_id in workers:
            if worker_id not in self.adapters:
                raise RuntimeError(f"unknown worker {worker_id}")
            if not agent_allowed(worker_id, perms):
                raise PermissionError(f"agent {worker_id} is not permitted")
            ok, reason = self.adapters[worker_id].validate_task(
                task.evolve(selected_agent=worker_id)
            )
            if not ok:
                raise RuntimeError(f"{worker_id}: {reason}")

        primary = plan.agent
        adapter = self.adapters[primary]
        task = task.evolve(
            status=TaskStatus.ROUTING,
            selected_agent=primary,
            current_step="routing",
            plan_steps=plan.steps,
            experience_ids=plan.reused_experience_ids,
        )
        self.store.save_task(task)
        self.emit(
            TaskEvent(
                type=EventType.TASK_ROUTED.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={
                    "agent": primary,
                    "workers": list(workers),
                    "reason": plan.reason,
                    "approach": plan.approach,
                },
            )
        )

        if cancel.is_set():
            self.cancel(task.task_id)
            return

        task = task.evolve(
            status=TaskStatus.RUNNING,
            current_step="running",
            started_at=utcnow(),
        )
        self.store.save_task(task)
        self.emit(
            TaskEvent(
                type=EventType.TASK_STARTED.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={
                    "agent": primary,
                    "workers": list(workers),
                    "workspace": adapter.get_status().workspace,
                },
            )
        )

        all_commands: list[dict] = []
        all_files: list[str] = []
        all_errors: list[str] = []
        summaries: list[str] = []
        success = True
        for worker_id in workers:
            if cancel.is_set():
                self.cancel(task.task_id)
                return
            worker = self.adapters[worker_id]
            self.emit(
                TaskEvent(
                    type=EventType.COMMAND_OUTPUT.value,
                    task_id=task.task_id,
                    ts=utcnow(),
                    payload={
                        "stream": "stdout",
                        "chunk": f"assigning worker={worker_id}",
                        "command": ["assign", worker_id],
                        "cwd": worker.get_status().workspace,
                    },
                )
            )
            result = worker.execute_task(
                task.evolve(selected_agent=worker_id), self.emit, cancel
            )
            all_commands.extend(result.commands)
            all_files.extend(result.files_changed)
            all_errors.extend(result.errors)
            summaries.append(f"[{worker_id}] {result.summary}")
            if not result.success:
                success = False

        if cancel.is_set():
            self.cancel(task.task_id)
            return

        status = TaskStatus.COMPLETED if success else TaskStatus.FAILED
        task = self.store.get_task(task.task_id) or task
        summary = "\n\n".join(summaries)[-8000:]
        task = task.evolve(
            status=status,
            current_step="completed" if success else "failed",
            completed_at=utcnow(),
            files_changed=tuple(dict.fromkeys(task.files_changed + tuple(all_files))),
            errors=task.errors + tuple(all_errors),
            result={
                "summary": summary,
                "success": success,
                "workers": list(workers),
                "commands": all_commands,
            },
            execution_history=tuple(all_commands),
        )
        self.store.save_task(task)
        self.emit(
            TaskEvent(
                type=(EventType.TASK_COMPLETED.value if success else EventType.TASK_FAILED.value),
                task_id=task.task_id,
                ts=utcnow(),
                payload={"summary": summary, "success": success, "workers": list(workers)},
            )
        )

        exp = Experience(
            experience_id=uuid.uuid4().hex[:12],
            task_id=task.task_id,
            objective=task.user_request,
            approach=plan.approach,
            agent=primary,
            tools=tuple(
                " ".join(str(x) for x in (cmd.get("command") or []))
                for cmd in all_commands
            ),
            errors=tuple(all_errors),
            fixes=(),
            result_summary=summary[:1000],
            success=success,
            strategy=(
                f"Use workers {', '.join(workers)} for similar work. Approach: {plan.approach}."
            ),
        )
        self.store.save_experience(exp)
        self.emit(
            TaskEvent(
                type=EventType.EXPERIENCE_STORED.value,
                task_id=task.task_id,
                ts=utcnow(),
                payload={"experience_id": exp.experience_id, "success": success},
            )
        )
        audit(
            "task.finished",
            {"task_id": task.task_id, "success": success, "agent": primary, "workers": list(workers)},
        )

    def agent_statuses(self) -> list[dict]:
        out = []
        for adapter in self.adapters.values():
            st = adapter.get_status()
            out.append(
                {
                    "agent_id": st.agent_id,
                    "label": st.label,
                    "ready": st.ready,
                    "detail": st.detail,
                    "workspace": st.workspace,
                    "capabilities": list(st.capabilities),
                }
            )
        return out
