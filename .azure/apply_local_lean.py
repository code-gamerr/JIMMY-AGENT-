"""Apply Jimmy lean first-turn limits to local JIMMY_HOME configs."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from jimmy_cli.jimmy_seed_profiles import (  # noqa: E402
    _apply_jimmy_agent_limits,
    _dump_yaml,
    _load_yaml,
)

# Extra local CLI toolsets not in the Azure lean baseline.
_LOCAL_EXTRA_DISABLE = ("computer_use", "browser-use", "bfl")


def main() -> None:
    home = Path(r"C:\Users\Arnav Singh\AppData\Local\jimmy")
    paths = [home / "config.yaml"]
    profiles = home / "profiles"
    if profiles.is_dir():
        paths.extend(sorted(profiles.glob("*/config.yaml")))

    for path in paths:
        if not path.exists():
            print(f"skip missing {path}")
            continue
        cfg = _load_yaml(path)
        before = (cfg.get("platform_toolsets") or {}).get("cli")
        _apply_jimmy_agent_limits(cfg, home=path.parent)

        agent = dict(cfg["agent"]) if isinstance(cfg.get("agent"), dict) else {}
        disabled = {
            str(x)
            for x in (agent.get("disabled_toolsets") or [])
            if isinstance(x, str) and x.strip()
        }
        disabled.update(_LOCAL_EXTRA_DISABLE)
        agent["disabled_toolsets"] = sorted(disabled)
        cfg["agent"] = agent

        platform_toolsets = (
            dict(cfg["platform_toolsets"])
            if isinstance(cfg.get("platform_toolsets"), dict)
            else {}
        )
        for platform, entries in list(platform_toolsets.items()):
            if not isinstance(entries, list):
                continue
            platform_toolsets[platform] = [
                e
                for e in entries
                if isinstance(e, str) and e not in _LOCAL_EXTRA_DISABLE
            ]
        cfg["platform_toolsets"] = platform_toolsets

        _dump_yaml(path, cfg)
        print(f"patched {path}")
        print(f"  coding_context={agent.get('coding_context')}")
        print(f"  disabled={agent.get('disabled_toolsets')}")
        print(f"  before_cli={before}")
        print(f"  after_cli={(cfg.get('platform_toolsets') or {}).get('cli')}")
        print(f"  after_tg={(cfg.get('platform_toolsets') or {}).get('telegram')}")
        print(f"  tool_search={(cfg.get('tools') or {}).get('tool_search')}")


if __name__ == "__main__":
    main()
