"""Port DeerFlow public skills into Jimmy optional-skills/deerflow/."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "deer-flow" / "skills" / "public"
DST = ROOT / "optional-skills" / "deerflow"

SKIP = {
    "claude-to-deerflow",
    "bootstrap",
    "skill-reviewer",
}

CATEGORY = "deerflow"
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
    lines.append(f"author: {data.get('author', 'DeerFlow / ByteDance (adapted for Jimmy)')}")
    lines.append(f"license: {data.get('license', 'MIT')}")
    platforms = data.get("platforms") or ["linux", "macos", "windows"]
    if isinstance(platforms, str):
        platforms = [p.strip() for p in platforms.strip("[]").split(",") if p.strip()]
    lines.append(f"platforms: [{', '.join(platforms)}]")
    tags = data.get("_tags") or ["deerflow"]
    lines.append("metadata:")
    lines.append("  jimmy:")
    lines.append(f"    tags: [{', '.join(tags)}]")
    lines.append(f"    category: {CATEGORY}")
    lines.append("    source: deerflow")
    lines.append("    upstream: https://github.com/bytedance/deer-flow")
    lines.append("---\n")
    return "\n".join(lines)


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    skipped: list[str] = []

    for skill_dir in sorted(SRC.iterdir()):
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
        if name in SKIP:
            skipped.append(name)
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            skipped.append(f"{name} (no SKILL.md)")
            continue

        dest = DST / name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(
            skill_dir,
            dest,
            ignore=shutil.ignore_patterns("__pycache__", ".git", "*.pyc"),
        )

        text = (dest / "SKILL.md").read_text(encoding="utf-8")
        fm, body = parse_fm(text)
        fm["name"] = fm.get("name") or name
        fm["version"] = fm.get("version") or "0.1.0"
        fm["author"] = "DeerFlow / ByteDance (adapted for Jimmy)"
        fm["license"] = "MIT"
        fm["platforms"] = ["linux", "macos", "windows"]
        desc = fm.get("description") or f"DeerFlow skill: {name}"
        if "instead of WebSearch" in desc:
            desc = desc.replace(
                "Use this skill instead of WebSearch for ANY question requiring web research.",
                "Use this skill for thorough multi-angle web research when a single search is not enough.",
            )
        fm["description"] = desc

        tags = [name.replace("-", " "), "deerflow"]
        if "research" in name or name in {
            "academic-paper-review",
            "systematic-literature-review",
            "consulting-analysis",
            "data-analysis",
        }:
            tags.append("research")
        if any(
            x in name
            for x in (
                "ppt",
                "podcast",
                "video",
                "music",
                "image",
                "newsletter",
                "chart",
                "frontend",
                "web-design",
                "surprise",
            )
        ):
            tags.append("creative")
        fm["_tags"] = tags

        attribution = (
            "\n> **Source:** Adapted from [DeerFlow](https://github.com/bytedance/deer-flow) "
            f"`skills/public/{name}` (MIT License, ByteDance / DeerFlow Authors). "
            "Installed into Jimmy as an optional skill — use via "
            f"`jimmy skills install official/deerflow/{name}`.\n\n"
        )
        if "Adapted from [DeerFlow]" not in body:
            body = attribution + body.lstrip("\n")

        (dest / "SKILL.md").write_text(dump_fm(fm) + body, encoding="utf-8")
        copied.append(name)

    print(f"COPIED {len(copied)}")
    for n in copied:
        print(f"  {n}")
    print(f"SKIPPED {skipped}")


if __name__ == "__main__":
    main()
