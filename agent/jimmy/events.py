"""In-process event bus. Subscribers get copies; nothing is fabricated."""

from __future__ import annotations

import threading
from collections import defaultdict
from typing import Callable

from jimmy.models import TaskEvent

Listener = Callable[[TaskEvent], None]


class EventBus:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._listeners: dict[str, list[Listener]] = defaultdict(list)
        self._global: list[Listener] = []

    def subscribe(self, listener: Listener, task_id: str | None = None) -> None:
        with self._lock:
            if task_id is None:
                self._global.append(listener)
            else:
                self._listeners[task_id].append(listener)

    def unsubscribe(self, listener: Listener, task_id: str | None = None) -> None:
        with self._lock:
            bucket = self._global if task_id is None else self._listeners.get(task_id, [])
            if listener in bucket:
                bucket.remove(listener)

    def publish(self, event: TaskEvent) -> None:
        with self._lock:
            listeners = list(self._global) + list(self._listeners.get(event.task_id, []))
        for listener in listeners:
            listener(event)
