#!/usr/bin/env python3
"""Maintenance auto-reply for Jimmy Telegram bots + tiny HTTP status page.

Runs while the full Jimmy gateway is offline. Replies to every inbound
Telegram message (incl. "hi") with a maintenance notice. Tokens come from
env: JIMMY{N}_TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN.
"""
from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MAINTENANCE_TEXT = (
    "🛠️ Jimmy is under maintenance right now — we're upgrading the engine "
    "and wiring in some seriously cool new capabilities.\n\n"
    "We'll be back in about 42 hours with fresh skills, sharper tools, and "
    "smoother chats.\n\n"
    "Hang tight — the glow-up is worth it. ✨"
)

HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Jimmy — Maintenance</title>
<style>
  body{margin:0;min-height:100vh;display:grid;place-items:center;
  font-family:Georgia,serif;background:linear-gradient(145deg,#0f172a,#1e293b);
  color:#e2e8f0;padding:2rem}
  main{max-width:36rem;text-align:center}
  h1{font-size:2.4rem;margin:0 0 .75rem;letter-spacing:.02em}
  p{line-height:1.55;opacity:.9}
</style></head>
<body><main>
<h1>Jimmy is polishing up</h1>
<p>We're offline for a short maintenance window — about 42 hours — to ship
cooler tools and a sharper agent experience.</p>
<p>Telegram bots will auto-reply until we're back. See you soon. ✨</p>
</main></body></html>
"""


def _tokens() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for i in range(1, 9):
        t = (os.environ.get(f"JIMMY{i}_TELEGRAM_BOT_TOKEN") or "").strip()
        if t:
            found.append((f"jimmy{i}", t))
    t = (os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
    if t and not any(x[1] == t for x in found):
        found.append(("default", t))
    return found


def _api(token: str, method: str, **params):
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def _send(token: str, chat_id: int, text: str) -> None:
    try:
        _api(token, "sendMessage", chat_id=chat_id, text=text)
    except Exception as exc:  # noqa: BLE001
        print(f"send failed chat={chat_id}: {exc}", flush=True)


def _poll_bot(name: str, token: str) -> None:
    offset = 0
    print(f"[{name}] maintenance poller started", flush=True)
    while True:
        try:
            data = _api(
                token,
                "getUpdates",
                offset=offset,
                timeout=25,
                allowed_updates=json.dumps(["message", "edited_message"]),
            )
            for upd in data.get("result") or []:
                offset = max(offset, int(upd["update_id"]) + 1)
                msg = upd.get("message") or upd.get("edited_message") or {}
                chat = msg.get("chat") or {}
                chat_id = chat.get("id")
                if chat_id is None:
                    continue
                text = (msg.get("text") or "").strip()
                # Always reply — hi, /start, anything.
                print(f"[{name}] reply chat={chat_id} text={text[:40]!r}", flush=True)
                _send(token, chat_id, MAINTENANCE_TEXT)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode(errors="replace")[:200]
            print(f"[{name}] HTTP {exc.code}: {body}", flush=True)
            time.sleep(5)
        except Exception as exc:  # noqa: BLE001
            print(f"[{name}] poll error: {exc}", flush=True)
            time.sleep(3)


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        body = HTML.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):  # noqa: A003
        print(f"[http] {fmt % args}", flush=True)


def main() -> None:
    tokens = _tokens()
    if not tokens:
        print("No Telegram bot tokens in env — HTTP-only maintenance page", flush=True)
    for name, token in tokens:
        threading.Thread(target=_poll_bot, args=(name, token), daemon=True).start()

    port = int(os.environ.get("JIMMY_REMOTE_PORT") or os.environ.get("PORT") or "9119")
    server = ThreadingHTTPServer(("0.0.0.0", port), _Handler)
    print(f"Maintenance page on :{port}; bots={len(tokens)}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
