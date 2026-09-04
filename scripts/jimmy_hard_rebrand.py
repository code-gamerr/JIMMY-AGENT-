#!/usr/bin/env python3
"""One-shot Jimmy hard rebrand rewriter (Jimmy/Nous → Jimmy).

Skips: .venv, node_modules, .git, openclaw, ECC, munder-difflin,
Facebook hermes-parser / hermes-estree package dirs.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIR_NAMES = {
    ".venv",
    "venv",
    "node_modules",
    ".git",
    "openclaw",
    "ECC",
    "munder-difflin",
    "hermes-parser",
    "hermes-estree",
    "__pycache__",
    ".pytest_cache",
    "dist",
    "build",
    "jimmy_agent.egg-info",
    "jimmy_agent.egg-info",
}

# Binary / non-text
SKIP_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".mp4",
    ".mp3",
    ".wav",
    ".zip",
    ".gz",
    ".bz2",
    ".xz",
    ".7z",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".pyc",
    ".pyo",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".pdf",
    ".xlsx",
    ".xls",
    ".parquet",
    ".whl",
    ".lock",
}

# Ordered replacements (longer / more specific first)
REPLACEMENTS: list[tuple[str, str]] = [
    ("Jimmy", "Jimmy"),
    ("jimmy-agent", "jimmy-agent"),
    ("Jimmy", "Jimmy"),
    ("JIMMY_HOME", "JIMMY_HOME"),
    ("JIMMY_CLI_NAME", "JIMMY_CLI_NAME"),
    ("JIMMY_DESKTOP", "JIMMY_DESKTOP"),
    ("JIMMY_TUI", "JIMMY_TUI"),
    ("JIMMY_ENABLE_PROJECT_PLUGINS", "JIMMY_ENABLE_PROJECT_PLUGINS"),
    ("JIMMY_KANBAN_BOARD", "JIMMY_KANBAN_BOARD"),
    ("JIMMY_BACKGROUND_NOTIFICATIONS", "JIMMY_BACKGROUND_NOTIFICATIONS"),
    ("JIMMY_SERVE_HEADLESS", "JIMMY_SERVE_HEADLESS"),
    ("JIMMY_TEST_FILE_RETRIES", "JIMMY_TEST_FILE_RETRIES"),
    ("JIMMY_", "JIMMY_"),
    ("jimmy_cli", "jimmy_cli"),
    ("jimmy_constants", "jimmy_constants"),
    ("jimmy_bootstrap", "jimmy_bootstrap"),
    ("jimmy_logging", "jimmy_logging"),
    ("jimmy_state_common", "jimmy_state_common"),
    ("jimmy_state_portability", "jimmy_state_portability"),
    ("jimmy_state_schema", "jimmy_state_schema"),
    ("jimmy_state_search", "jimmy_state_search"),
    ("jimmy_state", "jimmy_state"),
    ("jimmy_time", "jimmy_time"),
    ("jimmy-agent-skill-authoring", "jimmy-agent-skill-authoring"),
    ("inspecting-jimmy-desktop-dom", "inspecting-jimmy-desktop-dom"),
    ("jimmy-s6-container-supervision", "jimmy-s6-container-supervision"),
    ("jimmy-achievements", "jimmy-achievements"),
    ("jimmy-imports", "jimmy-imports"),
    ("jimmy-whatsapp-bridge", "jimmy-whatsapp-bridge"),
    ("jimmy-agent", "jimmy-agent"),
    ("@jimmy-agent/", "@jimmy-agent/"),
    ("@jimmy/", "@jimmy/"),
    ("jimmy-ink", "jimmy-ink"),
    ("jimmy-tui", "jimmy-tui"),
    ("jimmy-frames", "jimmy-frames"),
    ("jimmy-sprite", "jimmy-sprite"),
    ("jimmy-setup", "jimmy-setup"),
    ("jimmy-acp", "jimmy-acp"),
    ("main-jimmy", "main-jimmy"),
    ("setup-jimmy", "setup-jimmy"),
    ("Jimmy", "Jimmy"),
    ("JimmyCLI", "JimmyCLI"),
    ("AIAgent", "AIAgent"),  # keep
    ("get_jimmy_home", "get_jimmy_home"),
    ("display_jimmy_home", "display_jimmy_home"),
    ("~/.jimmy", "~/.jimmy"),
    (".jimmy/", ".jimmy/"),
    (".jimmy\\", ".jimmy\\"),
    (".jimmy-run", ".jimmy-run"),
    ("Jimmy", "Jimmy"),
    ("jimmy", "jimmy"),
]


def should_skip_dir(name: str) -> bool:
    return name in SKIP_DIR_NAMES or name.endswith(".egg-info")


def should_skip_file(path: Path) -> bool:
    if path.suffix.lower() in SKIP_SUFFIXES:
        return True
    # Keep Facebook parser package.json name intact if somehow reached
    if path.name in {"hermes-parser", "hermes-estree"}:
        return True
    return False


def rewrite_text(text: str) -> str:
    # Protect Facebook hermes-parser / hermes-estree tokens temporarily
    protected = {
        "hermes-parser": "hermes-parser",
        "hermes-estree": "hermes-estree",
        ""hermes-parser"": '"hermes-parser"',
        ""hermes-estree"": '"hermes-estree"',
    }
    text = text.replace("hermes-parser", "hermes-parser")
    text = text.replace("hermes-estree", "hermes-estree")
    for old, new in REPLACEMENTS:
        if old == "AIAgent":
            continue
        text = text.replace(old, new)
    for token, original in protected.items():
        text = text.replace(token, original)
    return text


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        for fn in filenames:
            p = Path(dirpath) / fn
            if should_skip_file(p):
                continue
            yield p


def rename_path_component(name: str) -> str:
    """Rename a single path component if it contains product jimmy."""
    if name in {"hermes-parser", "hermes-estree"}:
        return name
    mapping = [
        ("jimmy-agent-skill-authoring", "jimmy-agent-skill-authoring"),
        ("inspecting-jimmy-desktop-dom", "inspecting-jimmy-desktop-dom"),
        ("jimmy-s6-container-supervision", "jimmy-s6-container-supervision"),
        ("jimmy-achievements", "jimmy-achievements"),
        ("jimmy-imports", "jimmy-imports"),
        ("jimmy-agent", "jimmy-agent"),
        ("jimmy-ink", "jimmy-ink"),
        ("jimmy-frames", "jimmy-frames"),
        ("jimmy-sprite.png", "jimmy-sprite.png"),
        ("jimmy.png", "jimmy.png"),
        ("jimmy.ts", "jimmy.ts"),
        ("jimmy.test.ts", "jimmy.test.ts"),
        ("jimmy-capability-scope.test.ts", "jimmy-capability-scope.test.ts"),
        ("jimmy-cron-scope.test.ts", "jimmy-cron-scope.test.ts"),
        ("jimmy-parity.test.ts", "jimmy-parity.test.ts"),
        ("jimmy-profile-scope.test.ts", "jimmy-profile-scope.test.ts"),
        ("windows-jimmy-path.ts", "windows-jimmy-path.ts"),
        ("windows-jimmy-path.test.ts", "windows-jimmy-path.test.ts"),
        ("jimmy_tools_mcp_server.py", "jimmy_tools_mcp_server.py"),
        ("setup-jimmy.sh", "setup-jimmy.sh"),
        ("main-jimmy", "main-jimmy"),
        ("HERMES-OPENCLAW-MIGRATION.md", "JIMMY-OPENCLAW-MIGRATION.md"),
        ("HERMES-SETUP.md", "JIMMY-SETUP.md"),
    ]
    for old, new in mapping:
        if name == old:
            return new
        if old in name:
            name = name.replace(old, new)
    # Generic leftover file/dir jimmy → jimmy (careful)
    if re.search(r"(?i)jimmy", name) and "hermes-parser" not in name and "hermes-estree" not in name:
        name = re.sub(r"(?i)jimmy", "jimmy", name)
    return name


def rename_tree_bottom_up(root: Path) -> int:
    """Rename files/dirs whose names contain jimmy (product)."""
    renamed = 0
    # Collect all paths deepest first
    all_dirs: list[Path] = []
    all_files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # prune skips but still allow walking azure-build etc.
        pruned = []
        for d in list(dirnames):
            if should_skip_dir(d):
                continue
            pruned.append(d)
        dirnames[:] = pruned
        p = Path(dirpath)
        for fn in filenames:
            all_files.append(p / fn)
        for d in dirnames:
            all_dirs.append(p / d)

    for path in sorted(all_files, key=lambda x: len(x.parts), reverse=True):
        new_name = rename_path_component(path.name)
        if new_name != path.name:
            dest = path.with_name(new_name)
            if not dest.exists():
                path.rename(dest)
                renamed += 1
                print(f"rename file: {path.relative_to(root)} -> {new_name}")

    for path in sorted(all_dirs, key=lambda x: len(x.parts), reverse=True):
        if not path.exists():
            continue
        new_name = rename_path_component(path.name)
        if new_name != path.name:
            dest = path.with_name(new_name)
            if not dest.exists():
                path.rename(dest)
                renamed += 1
                print(f"rename dir: {path.relative_to(root)} -> {new_name}")
    return renamed


def rewrite_contents(root: Path) -> tuple[int, int]:
    changed = 0
    errors = 0
    for path in iter_files(root):
        try:
            raw = path.read_bytes()
        except OSError:
            errors += 1
            continue
        # skip obvious binary
        if b"\0" in raw[:8000]:
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = raw.decode("utf-8", errors="surrogateescape")
            except Exception:
                errors += 1
                continue
        new = rewrite_text(text)
        if new != text:
            path.write_bytes(new.encode("utf-8"))
            changed += 1
            if changed % 200 == 0:
                print(f"... rewritten {changed} files")
    return changed, errors


def main() -> int:
    print(f"ROOT={ROOT}")
    print("Phase A: rename path components")
    n = rename_tree_bottom_up(ROOT)
    print(f"Renamed {n} path components")
    print("Phase B: rewrite file contents")
    changed, errors = rewrite_contents(ROOT)
    print(f"Rewrote {changed} files; read_errors={errors}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
