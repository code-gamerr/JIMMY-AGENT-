"""Telegram narration edits one message from real events."""

from jimmy.models import TaskEvent, utcnow
from jimmy.telegram_status import TelegramStatusNarrator


def test_telegram_sends_once_then_edits():
    calls = []

    def post(url, payload):
        calls.append((url, payload))
        if url.endswith("/sendMessage"):
            return {"ok": True, "result": {"message_id": 42}}
        return {"ok": True, "result": {"message_id": 42}}

    narrator = TelegramStatusNarrator("99", token="test-token", task_id="t1", post=post)
    narrator.on_event(
        TaskEvent(type="task.planning", task_id="t1", ts=utcnow(), payload={"status": "Building execution plan..."})
    )
    narrator.on_event(
        TaskEvent(
            type="task.assigned",
            task_id="t1",
            ts=utcnow(),
            payload={
                "agent_id": "munder",
                "label": "Munder-Difflin",
                "description": "Handle workflow and implementation",
            },
        )
    )
    assert calls[0][0].endswith("/sendMessage")
    assert calls[1][0].endswith("/editMessageText")
    assert calls[1][1]["message_id"] == "42"
    assert "Munder-Difflin" in calls[1][1]["text"]
    assert narrator.message_id == "42"


def test_stdout_chunks_do_not_spam():
    calls = []

    def post(url, payload):
        calls.append(url)
        return {"ok": True, "result": {"message_id": 1}}

    narrator = TelegramStatusNarrator("99", token="test-token", task_id="t1", post=post)
    narrator.on_event(
        TaskEvent(type="command.output", task_id="t1", ts=utcnow(), payload={"chunk": "noise"})
    )
    assert calls == []
