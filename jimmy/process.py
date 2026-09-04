"""Run a real subprocess and emit measured command events. Never invent I/O."""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
from collections.abc import Callable, Iterator
from pathlib import Path

from jimmy.models import EventType, TaskEvent, utcnow
from jimmy.security import command_allowed

OnEvent = Callable[[TaskEvent], None]


def _creationflags() -> int:
    if os.name != "nt":
        return 0
    return int(getattr(subprocess, "CREATE_NO_WINDOW", 0))


def python_executable() -> str:
    return sys.executable


def run_command(
    *,
    task_id: str,
    argv: list[str],
    cwd: Path,
    env: dict[str, str] | None = None,
    timeout_s: float | None = 600,
    cancel_event: threading.Event | None = None,
    on_event: OnEvent | None = None,
) -> dict:
    """Spawn argv in cwd. Returns measured stdout/stderr/exit/duration."""
    allowed, reason = command_allowed(argv)
    if not allowed:
        event = TaskEvent(
            type=EventType.COMMAND_FINISHED.value,
            task_id=task_id,
            ts=utcnow(),
            payload={
                "command": argv,
                "cwd": str(cwd),
                "exit_code": 126,
                "stderr": reason,
                "blocked": True,
            },
        )
        if on_event:
            on_event(event)
        return {
            "command": argv,
            "cwd": str(cwd),
            "stdout": "",
            "stderr": reason,
            "exit_code": 126,
            "duration_ms": 0,
            "blocked": True,
        }

    cwd = cwd.resolve()
    started = utcnow()
    t0 = time.monotonic()
    if on_event:
        on_event(
            TaskEvent(
                type=EventType.COMMAND_STARTED.value,
                task_id=task_id,
                ts=started,
                payload={"command": argv, "cwd": str(cwd)},
            )
        )

    merged = os.environ.copy()
    if env:
        merged.update(env)

    proc = subprocess.Popen(
        argv,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=merged,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=_creationflags(),
    )
    stdout_chunks: list[str] = []
    stderr_chunks: list[str] = []

    def _pump(stream, bucket: list[str], stream_name: str) -> None:
        if stream is None:
            return
        for line in iter(stream.readline, ""):
            bucket.append(line)
            if on_event:
                on_event(
                    TaskEvent(
                        type=EventType.COMMAND_OUTPUT.value,
                        task_id=task_id,
                        ts=utcnow(),
                        payload={
                            "stream": stream_name,
                            "chunk": line.rstrip("\n"),
                            "command": argv,
                            "cwd": str(cwd),
                        },
                    )
                )

    t_out = threading.Thread(target=_pump, args=(proc.stdout, stdout_chunks, "stdout"), daemon=True)
    t_err = threading.Thread(target=_pump, args=(proc.stderr, stderr_chunks, "stderr"), daemon=True)
    t_out.start()
    t_err.start()

    deadline = None if timeout_s is None else (t0 + timeout_s)
    exit_code: int | None = None
    while True:
        if cancel_event is not None and cancel_event.is_set():
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
            exit_code = proc.poll()
            break
        if deadline is not None and time.monotonic() > deadline:
            proc.kill()
            exit_code = proc.wait()
            stderr_chunks.append("\n[jimmy] process killed after timeout\n")
            break
        code = proc.poll()
        if code is not None:
            exit_code = code
            break
        time.sleep(0.05)

    t_out.join(timeout=2)
    t_err.join(timeout=2)
    duration_ms = int((time.monotonic() - t0) * 1000)
    finished = utcnow()
    result = {
        "command": argv,
        "cwd": str(cwd),
        "stdout": "".join(stdout_chunks),
        "stderr": "".join(stderr_chunks),
        "exit_code": exit_code,
        "duration_ms": duration_ms,
        "started_at": started,
        "finished_at": finished,
        "blocked": False,
    }
    if on_event:
        on_event(
            TaskEvent(
                type=EventType.COMMAND_FINISHED.value,
                task_id=task_id,
                ts=finished,
                payload={
                    "command": argv,
                    "cwd": str(cwd),
                    "exit_code": exit_code,
                    "duration_ms": duration_ms,
                    "stdout_tail": result["stdout"][-4000:],
                    "stderr_tail": result["stderr"][-4000:],
                },
            )
        )
    return result


def git_changed_files(cwd: Path) -> list[str]:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=_creationflags(),
    )
    if proc.returncode != 0:
        return []
    files: list[str] = []
    for line in proc.stdout.splitlines():
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if path:
            files.append(path)
    return files


def iter_test_hints(stdout: str, stderr: str) -> Iterator[tuple[str, str]]:
    """Best-effort parse of real test runner lines (pytest / vitest / jest)."""
    text = stdout + "\n" + stderr
    for line in text.splitlines():
        lower = line.lower()
        if "fail" in lower and (".test." in lower or "failed" in lower):
            yield EventType.TEST_FAILED.value, line.strip()
        elif "passed" in lower and ("test" in lower or "pytest" in lower):
            yield EventType.TEST_PASSED.value, line.strip()
