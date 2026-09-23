#!/usr/bin/env python3
"""Hotpatch installed azure_foundry_model_api_mode so gpt-6* uses Responses API."""
from __future__ import annotations

import importlib
from pathlib import Path

NEEDLE_MARKERS = (
    "_AZURE_FOUNDRY_RESPONSES_PREFIXES",
    "azure_foundry_model_api_mode",
)


def candidate_files() -> list[Path]:
    found: list[Path] = []

    # Prefer the module actually imported at runtime.
    for mod_name in ("jimmy_cli.models", "hermes_cli.models", "nous_cli.models"):
        try:
            mod = importlib.import_module(mod_name)
        except Exception as exc:
            print(f"import {mod_name}: {exc}")
            continue
        path = Path(getattr(mod, "__file__", "") or "")
        if path.is_file():
            print(f"runtime module {mod_name} -> {path}")
            found.append(path)

    roots = [Path("/opt/jimmy"), Path("/opt/hermes"), Path("/app")]
    for root in roots:
        if not root.exists():
            continue
        for pkg in ("jimmy_cli", "hermes_cli", "nous_cli"):
            direct = root / pkg / "models.py"
            if direct.is_file():
                found.append(direct)
            venv = root / ".venv" / "lib"
            if venv.is_dir():
                for p in venv.glob(f"python*/site-packages/{pkg}/models.py"):
                    found.append(p)

    uniq: list[Path] = []
    seen = set()
    for p in found:
        key = str(p.resolve()) if p.exists() else str(p)
        if key not in seen:
            seen.add(key)
            uniq.append(p)
    return uniq


def patch_text(text: str) -> tuple[str, bool]:
    if '"gpt-6"' in text and "_AZURE_FOUNDRY_RESPONSES_PREFIXES" in text:
        return text, False
    if "'gpt-6'" in text and "_AZURE_FOUNDRY_RESPONSES_PREFIXES" in text:
        return text, False
    patterns = [
        (
            '"gpt-5",       # gpt-5, gpt-5.x, gpt-5-codex, gpt-5.x-codex\n    "o1",',
            '"gpt-5",       # gpt-5, gpt-5.x, gpt-5-codex, gpt-5.x-codex\n    "gpt-6",       # gpt-6-astra and later Azure Responses-only deployments\n    "o1",',
        ),
        (
            '"gpt-5",\n    "o1",',
            '"gpt-5",\n    "gpt-6",\n    "o1",',
        ),
        (
            '("codex", "gpt-5", "o1", "o3", "o4")',
            '("codex", "gpt-5", "gpt-6", "o1", "o3", "o4")',
        ),
        (
            "('codex', 'gpt-5', 'o1', 'o3', 'o4')",
            "('codex', 'gpt-5', 'gpt-6', 'o1', 'o3', 'o4')",
        ),
    ]
    for old, new in patterns:
        if old in text:
            return text.replace(old, new, 1), True
    return text, False


def main() -> None:
    targets = candidate_files()
    print("candidates:", ", ".join(str(p) for p in targets) or "(none)")
    patched = 0
    for path in targets:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"skip {path}: {exc}")
            continue
        if not any(m in text for m in NEEDLE_MARKERS):
            print(f"skip {path}: not azure foundry helper")
            continue
        new_text, changed = patch_text(text)
        if not changed:
            print(f"already patched: {path}")
            # still verify
            try:
                import importlib.util

                spec = importlib.util.spec_from_file_location("_m", path)
                mod = importlib.util.module_from_spec(spec)
                assert spec and spec.loader
                spec.loader.exec_module(mod)
                mode = mod.azure_foundry_model_api_mode("gpt-6-astra")
                print(f"verify {path}: gpt-6-astra -> {mode}")
            except Exception as exc:
                print(f"verify failed {path}: {exc}")
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"patched: {path}")
        patched += 1
        try:
            import importlib.util

            spec = importlib.util.spec_from_file_location("_m", path)
            mod = importlib.util.module_from_spec(spec)
            assert spec and spec.loader
            spec.loader.exec_module(mod)
            mode = mod.azure_foundry_model_api_mode("gpt-6-astra")
            print(f"verify {path}: gpt-6-astra -> {mode}")
        except Exception as exc:
            print(f"verify failed {path}: {exc}")
    print(f"done patched={patched}")


if __name__ == "__main__":
    main()
