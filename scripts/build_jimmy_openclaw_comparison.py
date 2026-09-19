"""Build Jimmy vs OpenClaw deep comparison workbook (Sheet1 only)."""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Jimmy_vs_OpenClaw_Deep_Comparison.xlsx"

ROWS = [
    ("Architecture", "Primary gateway", "Jimmy gateway + platforms", "OpenClaw Gateway control plane", "Jimmy primary", "Never swap", "WONTFIX replace"),
    ("Architecture", "Agent loop", "conversation_loop", "OpenClaw agents + tools", "Jimmy primary", "Different product cores", "Keep Jimmy"),
    ("Messaging", "Major IM channels", "Broader plugins/platforms set", "Many channels via extensions", "Jimmy stronger / equal", "Overlap large", "Migrate tokens via jimmy claw"),
    ("Messaging", "Exotic channels", "Partial / missing niches", "Nostr, Twitch, Synology, Tlon, …", "SIDECAR", "Long tail", "jimmy openclaw gateway"),
    ("Migration", "Import ~/.openclaw", "jimmy claw migrate + skill", "Source of truth for legacy installs", "EXISTS", "SOUL/MEMORY/skills/MCP/…", "Prefer deepen migrate"),
    ("Skills", "Skill packs", "optional + hub", "51 skills + ClawHub", "PARTIAL", "Curated port + imports", "optional-skills/openclaw"),
    ("Devices", "Companion nodes", "Desktop Electron (different)", "iOS/Android/macOS/Linux node-host", "SIDECAR", "Unique OC value", "Don’t fork into core"),
    ("UI", "Control UI", "Jimmy desktop/web/TUI", "Lit Control UI", "SIDECAR", "Separate product chrome", "jimmy openclaw dashboard"),
    ("CLI", "Sidecar wrapper", "jimmy openclaw …", "openclaw.mjs", "PORTED", "Isolated OPENCLAW_STATE_DIR", "jimmy_cli/openclaw_cmd.py"),
    ("CLI", "Migration CLI", "jimmy claw …", "N/A", "EXISTS", "Already primary path", "Keep claw for migrate"),
    ("Adapter", "Command-center worker", "jimmy/adapters/openclaw.py", "Nested openclaw.mjs agent", "EXISTS", "Isolated state", "Keep"),
    ("Cron", "Scheduled jobs", "Jimmy cron/", "OpenClaw cron", "Jimmy EXISTS", "Migrate archives", "Recreate in Jimmy"),
    ("Sandbox", "Computer use / canvas", "Browser + terminal envs", "node-host computer-use/canvas/camera", "SIDECAR / PARTIAL", "Selective later", "Sidecar first"),
    ("Legal", "License", "Jimmy licenses", "MIT OpenClaw", "OK", "Preserve notices", "THIRD_PARTY_NOTICES_OPENCLAW.md"),
]


def main() -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    headers = [
        "Category",
        "Capability",
        "Jimmy",
        "OpenClaw",
        "Verdict",
        "Notes",
        "Action",
    ]
    ws.append(headers)
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for row in ROWS:
        ws.append(list(row))
    wb.save(OUT)
    print(f"Wrote {OUT} with {len(ROWS)} data rows on Sheet1")


if __name__ == "__main__":
    main()
