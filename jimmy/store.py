"""SQLite task + experience store (profile-scoped via jimmy_home)."""

from __future__ import annotations

import json
import sqlite3
import threading
from pathlib import Path

from jimmy.models import Experience, TaskEvent, TaskRecord, TaskStatus, utcnow
from jimmy.paths import db_path


class OrchestratorStore:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or db_path()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._init()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.path), check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init(self) -> None:
        with self._lock, self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id TEXT PRIMARY KEY,
                    payload TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS events (
                    event_id TEXT PRIMARY KEY,
                    task_id TEXT NOT NULL,
                    ts TEXT NOT NULL,
                    type TEXT NOT NULL,
                    payload TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS experiences (
                    experience_id TEXT PRIMARY KEY,
                    task_id TEXT NOT NULL,
                    objective TEXT NOT NULL,
                    agent TEXT NOT NULL,
                    success INTEGER NOT NULL,
                    payload TEXT NOT NULL
                );
                CREATE VIRTUAL TABLE IF NOT EXISTS experiences_fts USING fts5(
                    experience_id UNINDEXED,
                    objective,
                    strategy,
                    approach
                );
                """
            )

    def save_task(self, task: TaskRecord) -> None:
        blob = json.dumps(task.to_dict())
        with self._lock, self._connect() as conn:
            conn.execute(
                "INSERT INTO tasks(task_id, payload) VALUES(?, ?) "
                "ON CONFLICT(task_id) DO UPDATE SET payload=excluded.payload",
                (task.task_id, blob),
            )

    def get_task(self, task_id: str) -> TaskRecord | None:
        with self._lock, self._connect() as conn:
            row = conn.execute(
                "SELECT payload FROM tasks WHERE task_id=?", (task_id,)
            ).fetchone()
        if not row:
            return None
        return _task_from_dict(json.loads(row["payload"]))

    def list_tasks(self, limit: int = 100) -> list[TaskRecord]:
        with self._lock, self._connect() as conn:
            rows = conn.execute(
                "SELECT payload FROM tasks ORDER BY rowid DESC LIMIT ?", (limit,)
            ).fetchall()
        return [_task_from_dict(json.loads(r["payload"])) for r in rows]

    def append_event(self, event: TaskEvent) -> None:
        with self._lock, self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO events(event_id, task_id, ts, type, payload) "
                "VALUES(?,?,?,?,?)",
                (
                    event.event_id,
                    event.task_id,
                    event.ts,
                    event.type,
                    json.dumps(event.to_dict()),
                ),
            )

    def list_events(self, task_id: str | None = None, after_ts: str | None = None) -> list[TaskEvent]:
        sql = "SELECT payload FROM events WHERE 1=1"
        params: list[object] = []
        if task_id:
            sql += " AND task_id=?"
            params.append(task_id)
        if after_ts:
            sql += " AND ts>?"
            params.append(after_ts)
        sql += " ORDER BY ts ASC, rowid ASC"
        with self._lock, self._connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        out: list[TaskEvent] = []
        for row in rows:
            data = json.loads(row["payload"])
            out.append(
                TaskEvent(
                    event_id=data["event_id"],
                    type=data["type"],
                    task_id=data["task_id"],
                    ts=data["ts"],
                    payload=data.get("payload") or {},
                )
            )
        return out

    def save_experience(self, exp: Experience) -> None:
        blob = json.dumps(exp.to_dict())
        with self._lock, self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO experiences"
                "(experience_id, task_id, objective, agent, success, payload) "
                "VALUES(?,?,?,?,?,?)",
                (
                    exp.experience_id,
                    exp.task_id,
                    exp.objective,
                    exp.agent,
                    int(exp.success),
                    blob,
                ),
            )
            conn.execute(
                "INSERT INTO experiences_fts(experience_id, objective, strategy, approach) "
                "VALUES(?,?,?,?)",
                (exp.experience_id, exp.objective, exp.strategy, exp.approach),
            )

    def search_experiences(self, query: str, limit: int = 8) -> list[Experience]:
        q = (query or "").strip()
        with self._lock, self._connect() as conn:
            if not q:
                rows = conn.execute(
                    "SELECT payload FROM experiences ORDER BY rowid DESC LIMIT ?",
                    (limit,),
                ).fetchall()
            else:
                try:
                    rows = conn.execute(
                        "SELECT e.payload FROM experiences e "
                        "JOIN experiences_fts f ON f.experience_id=e.experience_id "
                        "WHERE experiences_fts MATCH ? LIMIT ?",
                        (q, limit),
                    ).fetchall()
                except sqlite3.OperationalError:
                    like = f"%{q}%"
                    rows = conn.execute(
                        "SELECT payload FROM experiences WHERE objective LIKE ? "
                        "OR payload LIKE ? LIMIT ?",
                        (like, like, limit),
                    ).fetchall()
        return [_experience_from_dict(json.loads(r["payload"])) for r in rows]


def _task_from_dict(data: dict) -> TaskRecord:
    return TaskRecord(
        task_id=data["task_id"],
        user_request=data["user_request"],
        selected_agent=data.get("selected_agent"),
        status=TaskStatus(data["status"]),
        created_at=data.get("created_at") or utcnow(),
        started_at=data.get("started_at"),
        completed_at=data.get("completed_at"),
        current_step=data.get("current_step") or "",
        logs=tuple(data.get("logs") or ()),
        files_changed=tuple(data.get("files_changed") or ()),
        errors=tuple(data.get("errors") or ()),
        result=data.get("result"),
        execution_history=tuple(data.get("execution_history") or ()),
        plan_steps=tuple(data.get("plan_steps") or ()),
        experience_ids=tuple(data.get("experience_ids") or ()),
        retry_count=int(data.get("retry_count") or 0),
    )


def _experience_from_dict(data: dict) -> Experience:
    return Experience(
        experience_id=data["experience_id"],
        task_id=data["task_id"],
        objective=data["objective"],
        approach=data.get("approach") or "",
        agent=data["agent"],
        tools=tuple(data.get("tools") or ()),
        errors=tuple(data.get("errors") or ()),
        fixes=tuple(data.get("fixes") or ()),
        result_summary=data.get("result_summary") or "",
        success=bool(data.get("success")),
        strategy=data.get("strategy") or "",
        created_at=data.get("created_at") or utcnow(),
    )
