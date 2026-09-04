"""Task, event, and experience records. Immutable dataclasses."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class TaskStatus(str, Enum):
    QUEUED = "QUEUED"
    PLANNING = "PLANNING"
    ROUTING = "ROUTING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


TERMINAL_STATUSES = frozenset(
    {TaskStatus.FAILED, TaskStatus.COMPLETED, TaskStatus.CANCELLED}
)


class EventType(str, Enum):
    TASK_CREATED = "task.created"
    TASK_PLANNING = "task.planning"
    TASK_ROUTED = "task.routed"
    TASK_STARTED = "task.started"
    COMMAND_STARTED = "command.started"
    COMMAND_OUTPUT = "command.output"
    COMMAND_FINISHED = "command.finished"
    FILE_CHANGED = "file.changed"
    TEST_STARTED = "test.started"
    TEST_FAILED = "test.failed"
    TEST_PASSED = "test.passed"
    TASK_RETRYING = "task.retrying"
    TASK_COMPLETED = "task.completed"
    TASK_FAILED = "task.failed"
    TASK_CANCELLED = "task.cancelled"
    EXPERIENCE_STORED = "experience.stored"


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_task_id() -> str:
    return uuid.uuid4().hex[:12]


@dataclass(frozen=True)
class CommandRecord:
    command: list[str]
    cwd: str
    stdout: str = ""
    stderr: str = ""
    exit_code: int | None = None
    duration_ms: int | None = None
    started_at: str = ""
    finished_at: str = ""


@dataclass(frozen=True)
class TaskEvent:
    type: str
    task_id: str
    ts: str
    payload: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: uuid.uuid4().hex[:16])

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "type": self.type,
            "task_id": self.task_id,
            "ts": self.ts,
            "payload": dict(self.payload),
        }


@dataclass(frozen=True)
class TaskRecord:
    task_id: str
    user_request: str
    selected_agent: str | None = None
    status: TaskStatus = TaskStatus.QUEUED
    created_at: str = field(default_factory=utcnow)
    started_at: str | None = None
    completed_at: str | None = None
    current_step: str = "queued"
    logs: tuple[str, ...] = ()
    files_changed: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    result: dict[str, Any] | None = None
    execution_history: tuple[dict[str, Any], ...] = ()
    plan_steps: tuple[dict[str, Any], ...] = ()
    experience_ids: tuple[str, ...] = ()
    retry_count: int = 0

    def evolve(self, **changes: Any) -> TaskRecord:
        return replace(self, **changes)

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "user_request": self.user_request,
            "selected_agent": self.selected_agent,
            "status": self.status.value,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "current_step": self.current_step,
            "logs": list(self.logs),
            "files_changed": list(self.files_changed),
            "errors": list(self.errors),
            "result": self.result,
            "execution_history": list(self.execution_history),
            "plan_steps": list(self.plan_steps),
            "experience_ids": list(self.experience_ids),
            "retry_count": self.retry_count,
        }


@dataclass(frozen=True)
class Experience:
    experience_id: str
    task_id: str
    objective: str
    approach: str
    agent: str
    tools: tuple[str, ...]
    errors: tuple[str, ...]
    fixes: tuple[str, ...]
    result_summary: str
    success: bool
    strategy: str
    created_at: str = field(default_factory=utcnow)

    def to_dict(self) -> dict[str, Any]:
        return {
            "experience_id": self.experience_id,
            "task_id": self.task_id,
            "objective": self.objective,
            "approach": self.approach,
            "agent": self.agent,
            "tools": list(self.tools),
            "errors": list(self.errors),
            "fixes": list(self.fixes),
            "result_summary": self.result_summary,
            "success": self.success,
            "strategy": self.strategy,
            "created_at": self.created_at,
        }
