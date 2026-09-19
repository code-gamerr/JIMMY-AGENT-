"""Edit one Telegram status message from orchestrator narration events."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Callable

from jimmy.narration import project, render_telegram, should_refresh

HttpPost = Callable[[str, dict], dict]


def _default_post(url: str, payload: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


class TelegramStatusNarrator:
    """Keeps a single chat message in sync with real task events."""

    def __init__(
        self,
        chat_id: str,
        *,
        token: str | None = None,
        task_id: str | None = None,
        post: HttpPost | None = None,
    ) -> None:
        self.chat_id = str(chat_id)
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN") or ""
        self.task_id = task_id
        self._post = post or _default_post
        self.message_id: str | None = None
        self._last_text = ""
        self._events: list = []

    def on_event(self, event) -> None:
        if self.task_id and event.task_id != self.task_id:
            return
        if not should_refresh(event.type):
            return
        if not self.token or not self.chat_id:
            return
        self._events.append(event)
        text = render_telegram(project(self._events))
        if not text or text == self._last_text:
            return
        self._last_text = text
        try:
            if self.message_id is None:
                data = self._post(
                    f"https://api.telegram.org/bot{self.token}/sendMessage",
                    {"chat_id": self.chat_id, "text": text},
                )
                result = data.get("result") or {}
                if result.get("message_id") is not None:
                    self.message_id = str(result["message_id"])
            else:
                self._post(
                    f"https://api.telegram.org/bot{self.token}/editMessageText",
                    {
                        "chat_id": self.chat_id,
                        "message_id": self.message_id,
                        "text": text,
                    },
                )
        except (urllib.error.URLError, TimeoutError, OSError, ValueError):
            return
