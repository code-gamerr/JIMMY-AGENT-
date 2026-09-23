#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import yaml

HOMES = [Path("/opt/data")] + [Path(f"/opt/data/profiles/jimmy{i}") for i in range(1, 5)]


def main() -> None:
    for home in HOMES:
        cfg = home / "config.yaml"
        print(f"=== {cfg} exists={cfg.is_file()} ===")
        if not cfg.is_file():
            continue
        data = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
        model = data.get("model") if isinstance(data, dict) else None
        agent = data.get("agent") if isinstance(data, dict) else None
        print("model:", model)
        if isinstance(agent, dict):
            print(
                "agent.reasoning_effort:",
                agent.get("reasoning_effort"),
                "max_iterations:",
                agent.get("max_iterations"),
            )
        env = home / ".env"
        if env.is_file():
            keys = []
            for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k = line.split("=", 1)[0].strip()
                if k:
                    keys.append(k)
            print("env keys:", ", ".join(keys))
    # recent log snippets (no secrets)
    for pattern in ("*.log", "gateway*.log", "jimmy*.log"):
        for path in Path("/opt/data").rglob(pattern):
            try:
                if path.stat().st_mtime < __import__("time").time() - 3 * 86400:
                    continue
            except OSError:
                continue
            print(f"--- log {path} ---")
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError as exc:
                print("read fail:", exc)
                continue
            for line in lines[-200:]:
                low = line.lower()
                if any(
                    token in low
                    for token in (
                        "error",
                        "fail",
                        "401",
                        "403",
                        "404",
                        "429",
                        "api call",
                        "provider",
                        "astra",
                        "openai",
                        "deployment",
                        "retries",
                        "codex",
                        "api_mode",
                    )
                ):
                    # crude secret scrub
                    scrubbed = line
                    for marker in ("api-key", "api_key", "Bearer ", "token="):
                        if marker.lower() in scrubbed.lower():
                            scrubbed = scrubbed[:120] + " ...[redacted]"
                            break
                    print(scrubbed)


if __name__ == "__main__":
    main()
