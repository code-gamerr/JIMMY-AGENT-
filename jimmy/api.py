"""Loopback FastAPI for the Jimmy Command Center. Bind 127.0.0.1 only."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from jimmy.engine import TaskEngine
from jimmy.security import load_or_create_token, read_audit, token_matches

UI_FILE = Path(__file__).resolve().parent / "ui" / "command-center.html"

_engine: TaskEngine | None = None
_token: str = ""


def get_engine() -> TaskEngine:
    global _engine
    if _engine is None:
        _engine = TaskEngine()
    return _engine


def set_engine(engine: TaskEngine) -> None:
    global _engine
    _engine = engine


def get_token() -> str:
    global _token
    if not _token:
        _token = load_or_create_token()
    return _token


class SubmitBody(BaseModel):
    user_request: str = Field(min_length=1, max_length=20000)
    agent: str | None = Field(default="auto")
    telegram_chat_id: str | None = Field(default=None, max_length=64)


def _extract_token(request: Request, authorization: str | None, x_jimmy_token: str | None) -> str | None:
    q = request.query_params.get("token")
    if q:
        return q
    if x_jimmy_token:
        return x_jimmy_token
    if authorization and authorization.lower().startswith("bearer "):
        return authorization[7:].strip()
    return None


def create_app(engine: TaskEngine | None = None) -> FastAPI:
    if engine is not None:
        set_engine(engine)
    get_token()
    app = FastAPI(title="Jimmy Command Center", docs_url=None, redoc_url=None)

    @app.middleware("http")
    async def cors_gate(request: Request, call_next):
        if request.method == "OPTIONS":
            return JSONResponse(
                {},
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "authorization, x-jimmy-token, content-type",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                },
            )
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "authorization, x-jimmy-token, content-type"
        return response

    @app.middleware("http")
    async def auth_gate(request: Request, call_next):
        path = request.url.path
        if path in {"/", "/healthz"}:
            return await call_next(request)
        if path.startswith("/api/"):
            provided = _extract_token(
                request,
                request.headers.get("authorization"),
                request.headers.get("x-jimmy-token"),
            )
            if not token_matches(provided, get_token()):
                return JSONResponse({"success": False, "data": None, "error": "unauthorized"}, status_code=401)
        return await call_next(request)

    @app.get("/healthz")
    def healthz():
        return {"ok": True, "bind": "127.0.0.1"}

    @app.get("/")
    def index():
        return FileResponse(UI_FILE)

    @app.get("/api/jimmy/agents")
    def agents():
        return {"success": True, "data": get_engine().agent_statuses(), "error": None}

    @app.get("/api/jimmy/tasks")
    def list_tasks():
        tasks = [t.to_dict() for t in get_engine().store.list_tasks()]
        return {"success": True, "data": tasks, "error": None}

    @app.post("/api/jimmy/tasks")
    def submit(body: SubmitBody):
        task = get_engine().submit(
            body.user_request,
            agent=body.agent,
            telegram_chat_id=body.telegram_chat_id,
        )
        return {"success": True, "data": task.to_dict(), "error": None}

    @app.get("/api/jimmy/tasks/{task_id}")
    def show_task(task_id: str):
        task = get_engine().store.get_task(task_id)
        if not task:
            raise HTTPException(404, "task not found")
        events = [e.to_dict() for e in get_engine().store.list_events(task_id)]
        return {
            "success": True,
            "data": {
                "task": task.to_dict(),
                "events": events,
                "narration": get_engine().narration(task_id),
            },
            "error": None,
        }

    @app.post("/api/jimmy/tasks/{task_id}/cancel")
    def cancel(task_id: str):
        task = get_engine().cancel(task_id)
        if not task:
            raise HTTPException(404, "task not found")
        return {"success": True, "data": task.to_dict(), "error": None}

    @app.get("/api/jimmy/experiences")
    def experiences(q: str = ""):
        items = [e.to_dict() for e in get_engine().store.search_experiences(q)]
        return {"success": True, "data": items, "error": None}

    @app.get("/api/jimmy/audit")
    def audit():
        return {"success": True, "data": read_audit(), "error": None}

    @app.get("/api/jimmy/events")
    async def events(task_id: str | None = Query(default=None)):
        queue: asyncio.Queue = asyncio.Queue()
        loop = asyncio.get_event_loop()

        def listener(event):
            if task_id and event.task_id != task_id:
                return
            loop.call_soon_threadsafe(queue.put_nowait, event.to_dict())

        get_engine().bus.subscribe(listener, task_id)

        async def gen():
            try:
                # Replay persisted events first.
                for event in get_engine().store.list_events(task_id):
                    yield f"data: {json.dumps(event.to_dict())}\n\n"
                while True:
                    item = await queue.get()
                    yield f"data: {json.dumps(item)}\n\n"
            finally:
                get_engine().bus.unsubscribe(listener, task_id)

        return StreamingResponse(gen(), media_type="text/event-stream")

    return app
