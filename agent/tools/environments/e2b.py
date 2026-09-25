"""E2B cloud execution environment (DeerFlow-inspired, Jimmy-native).

Uses the ``e2b-code-interpreter`` SDK to run commands in cloud sandboxes.
Selected via ``TERMINAL_ENV=e2b`` / ``terminal.backend: e2b``.
"""

from __future__ import annotations

import logging
import os
import shlex
import threading
from typing import Any, Optional

from tools.environments.base import BaseEnvironment, _ThreadedProcessHandle

logger = logging.getLogger(__name__)

DEFAULT_E2B_CWD = "/home/user"


class E2BEnvironment(BaseEnvironment):
    """E2B cloud sandbox execution backend (spawn-per-call)."""

    _stdin_mode = "heredoc"

    def __init__(
        self,
        image: str = "",
        cwd: str = DEFAULT_E2B_CWD,
        timeout: int = 60,
        *,
        api_key: Optional[str] = None,
        template: Optional[str] = None,
    ):
        super().__init__(cwd=cwd or DEFAULT_E2B_CWD, timeout=timeout)
        self._lock = threading.Lock()
        self._sandbox = None
        key = (api_key or os.getenv("E2B_API_KEY") or "").strip()
        if not key:
            raise ImportError(
                "E2B backend requires E2B_API_KEY. "
                "Get a key at https://e2b.dev and set it in ~/.jimmy/.env"
            )
        try:
            from e2b_code_interpreter import Sandbox
        except ImportError as exc:
            raise ImportError(
                "e2b-code-interpreter is required for TERMINAL_ENV=e2b. "
                "Install with: pip install e2b-code-interpreter"
            ) from exc

        create_kwargs: dict[str, Any] = {"api_key": key, "timeout": max(60, int(timeout))}
        tpl = (template or os.getenv("E2B_TEMPLATE") or image or "").strip()
        if tpl:
            create_kwargs["template"] = tpl
        self._sandbox = Sandbox.create(**create_kwargs)
        logger.info("E2B: created sandbox %s", getattr(self._sandbox, "sandbox_id", "?"))
        self.init_session()

    def _run_bash(
        self,
        cmd_string: str,
        *,
        login: bool = False,
        timeout: int = 120,
        stdin_data: str | None = None,
    ):
        sandbox = self._sandbox
        if sandbox is None:
            raise RuntimeError("E2B sandbox is not connected")
        lock = self._lock
        workdir = self.cwd or DEFAULT_E2B_CWD
        if login:
            shell = f"bash -l -c {shlex.quote(cmd_string)}"
        else:
            shell = f"bash -c {shlex.quote(cmd_string)}"
        wrapped = f"cd {shlex.quote(workdir)} && {shell}"

        def cancel():
            pass

        def exec_fn() -> tuple[str, int]:
            with lock:
                result = sandbox.commands.run(
                    wrapped,
                    timeout=float(timeout),
                )
            stdout = getattr(result, "stdout", "") or ""
            stderr = getattr(result, "stderr", "") or ""
            code = int(getattr(result, "exit_code", 0) or 0)
            combined = stdout if not stderr else f"{stdout}{stderr}"
            return combined, code

        return _ThreadedProcessHandle(exec_fn, cancel_fn=cancel)

    def cleanup(self) -> None:
        sandbox = self._sandbox
        self._sandbox = None
        if sandbox is None:
            return
        try:
            kill = getattr(sandbox, "kill", None)
            if callable(kill):
                kill()
            else:
                closer = getattr(sandbox, "close", None)
                if callable(closer):
                    closer()
        except Exception as exc:
            logger.warning("E2B cleanup failed: %s", exc)
