#!/usr/bin/env python3
"""Force gpt-6-astra Azure Foundry homes onto Responses API."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOTS = [
    Path("/opt/data"),
    Path("/mnt/maint"),
]
HOMES = []
for root in ROOTS:
    HOMES.append(root)
    for i in range(1, 5):
        HOMES.append(root / "profiles" / f"jimmy{i}")


def patch(path: Path) -> bool:
    cfg_path = path / "config.yaml"
    if not cfg_path.is_file():
        print(f"{cfg_path}: missing")
        return False
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        print(f"{cfg_path}: not a mapping")
        return False
    model = dict(data["model"]) if isinstance(data.get("model"), dict) else {}
    agent = dict(data["agent"]) if isinstance(data.get("agent"), dict) else {}
    changed = False
    if model.get("api_mode") != "codex_responses":
        model["api_mode"] = "codex_responses"
        changed = True
    if model.get("default") in (None, "", "gpt-5.6-sol"):
        model["default"] = "gpt-6-astra"
        changed = True
    if str(model.get("default") or "").startswith("gpt-6") and model.get("api_mode") != "codex_responses":
        model["api_mode"] = "codex_responses"
        changed = True
    if model.get("provider") != "azure-foundry":
        model["provider"] = "azure-foundry"
        changed = True
    # Always force Responses for gpt-6* defaults even if something else was set.
    if str(model.get("default") or "").lower().startswith("gpt-6"):
        if model.get("api_mode") != "codex_responses":
            model["api_mode"] = "codex_responses"
            changed = True
    if str(agent.get("reasoning_effort") or "").strip().lower() != "none":
        agent["reasoning_effort"] = "none"
        changed = True
    data["model"] = model
    data["agent"] = agent
    if changed:
        cfg_path.write_text(
            yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )
    print(
        f"{cfg_path}: changed={changed} default={model.get('default')} "
        f"api_mode={model.get('api_mode')} provider={model.get('provider')}"
    )
    return changed


n = sum(1 for h in HOMES if patch(h))
print(f"patched {n} config(s)")
