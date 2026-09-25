"""Start the Command Center on 127.0.0.1 only."""

from __future__ import annotations

import webbrowser

from jimmy.api import create_app, get_token
from jimmy.security import audit


def serve(host: str = "127.0.0.1", port: int = 8765, open_browser: bool = True) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise ValueError("Jimmy Command Center binds loopback only")
    token = get_token()
    app = create_app()
    audit("command_center.start", {"host": host, "port": port})
    url = f"http://{host}:{port}/?token={token}"
    print(f"Jimmy Command Center: {url}")
    print("This token is stored in JIMMY_HOME/jimmy/auth.json and is required for API calls.")
    if open_browser:
        webbrowser.open(url)
    import uvicorn

    uvicorn.run(app, host=host, port=port, log_level="info")
