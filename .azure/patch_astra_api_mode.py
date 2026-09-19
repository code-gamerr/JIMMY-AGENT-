#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import yaml
HOMES = [Path("/opt/data")] + [Path(f"/opt/data/profiles/jimmy{i}") for i in range(1, 5)]

def patch(path: Path) -> bool:
    cfg_path = path / "config.yaml"
    if not cfg_path.is_file():
        return False
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
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
    if model.get("provider") != "azure-foundry":
        model["provider"] = "azure-foundry"
        changed = True
    if str(agent.get("reasoning_effort") or "").strip().lower() != "none":
        agent["reasoning_effort"] = "none"
        changed = True
    data["model"] = model
    data["agent"] = agent
    if changed:
        cfg_path.write_text(yaml.safe_dump(data, default_flow_style=False, sort_keys=False), encoding="utf-8")
    print(f"{cfg_path}: changed={changed} api_mode={model.get('api_mode')} effort={agent.get('reasoning_effort')}")
    return changed

n = sum(1 for h in HOMES if patch(h))
print(f"patched {n} config(s)")