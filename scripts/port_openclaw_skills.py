"""Port curated OpenClaw skills into optional-skills/openclaw/ (sidecar-friendly).

Device-node / Apple-only packs stay in openclaw/ — use `jimmy openclaw` for those.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "openclaw" / "skills"
DST = ROOT / "optional-skills" / "openclaw"

CURATED = {
    "healthcheck",
    "clawhub",
    "coding-agent",
    "github",
    "gh-issues",
    "skill-creator",
    "weather",
    "tmux",
    "oracle",
}

CATEGORY = "openclaw"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_fm(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    data: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in data:
            data[key] = val
    return data, text[m.end() :]


def dump_fm(data: dict) -> str:
    lines = ["---"]
    lines.append(f"name: {data['name']}")
    desc = str(data.get("description") or "").replace("\r", "")
    lines.append("description: >-")
    for part in desc.split("\n"):
        lines.append(f"  {part}" if part else "  ")
    lines.append(f"version: {data.get('version', '0.1.0')}")
    lines.append(
        f"author: {data.get('author', 'OpenClaw Authors (adapted for Jimmy)')}"
    )
    lines.append(f"license: {data.get('license', 'MIT')}")
    lines.append("platforms: [linux, macos, windows]")
    lines.append("metadata:")
    lines.append("  jimmy:")
    lines.append("    tags: [openclaw]")
    lines.append(f"    category: {CATEGORY}")
    lines.append("    source: openclaw")
    lines.append("    upstream: https://github.com/openclaw/openclaw")
    lines.append("---\n")
    return "\n".join(lines)


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    missing: list[str] = []

    for name in sorted(CURATED):
        skill_dir = SRC / name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            missing.append(name)
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        data, body = parse_fm(text)
        data["name"] = name
        if not data.get("description"):
            data["description"] = f"OpenClaw skill: {name}"
        dest = DST / name
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)
        for item in skill_dir.iterdir():
            target = dest / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            elif item.name != "SKILL.md":
                shutil.copy2(item, target)
        (dest / "SKILL.md").write_text(dump_fm(data) + body.lstrip("\n"), encoding="utf-8")
        copied.append(name)

    print(f"ported {len(copied)} OpenClaw skills -> {DST}")
    if missing:
        print("missing:", ", ".join(missing))


if __name__ == "__main__":
    main()
