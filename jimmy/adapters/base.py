"""AgentAdapter protocol — workers implement this; Jimmy core does not import their internals."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from jimmy.models import TaskEvent, TaskRecord


@dataclass(frozen=True)
class AdapterStatus:
    agent_id: str
    label: str
    ready: bool
    detail: str
    workspace: str
    capabilities: tuple[str, ...]


@dataclass(frozen=True)
class AdapterResult:
    success: bool
    summary: str
    files_changed: tuple[str, ...]
    commands: tuple[dict, ...]
    errors: tuple[str, ...]


class AgentAdapter(Protocol):
    agent_id: str

    def get_capabilities(self) -> tuple[str, ...]: ...

    def get_status(self) -> AdapterStatus: ...

    def validate_task(self, task: TaskRecord) -> tuple[bool, str]: ...

    def execute_task(
        self,
        task: TaskRecord,
        emit: callable,
        cancel_event,
    ) -> AdapterResult: ...

    def cancel_task(self, task_id: str) -> None: ...
