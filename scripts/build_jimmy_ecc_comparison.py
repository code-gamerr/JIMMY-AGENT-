"""Build Jimmy vs ECC deep comparison workbook (Sheet1 only)."""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Jimmy_vs_ECC_Deep_Comparison.xlsx"

ROWS = [
    ("Architecture", "Agent loop", "Jimmy conversation_loop / run_agent", "Harness OS (skills/hooks/commands), not a chat loop", "Jimmy primary", "ECC is complementary", "Keep Jimmy loop; ECC sidecar"),
    ("Architecture", "Install targets", "JIMMY_HOME / profiles", "Multi-harness (claude/cursor/codex/hermes/…)", "Both", "hermes target maps to Jimmy lineage", "Document hermes→jimmy; optional jimmy alias later"),
    ("Skills", "Skill catalog size", "Bundled + optional-skills + hub", "286 skill dirs in ECC/skills", "ECC denser catalog", "Jimmy ports curated subset", "optional-skills/ecc via port_ecc_skills.py"),
    ("Skills", "Curated port", "optional-skills/ecc/*", "Source packs in ECC/skills", "PORTED", "delivery-gate, context-budget, tdd, …", "Rebuild with scripts/port_ecc_skills.py"),
    ("Commands", "Slash / orch commands", "jimmy_cli COMMAND_REGISTRY", "94 markdown commands", "PARTIAL", "Overlap with Cursor ECC install", "Sidecar or selective command packs"),
    ("Agents", "Personas / subagents", "plugins + delegate_task", "68 agent markdowns", "PARTIAL", "Different orchestration model", "SIDECAR personas; don’t dual-orchestrate"),
    ("Hooks", "PreToolUse/PostToolUse", "Jimmy hooks (opt-in)", "ECC/Cursor hooks packs", "PARTIAL", "Hooks can break prompt cache", "WONTFIX default-on; --no-hooks setup"),
    ("Memory", "Memory Vault", "Jimmy memory tool + plugins", "ECC .ecc/memory + ecc memory CLI", "SIDECAR", "Cross-harness vault is ECC’s niche", "jimmy ecc memory"),
    ("Ops", "Doctor / repair", "jimmy doctor", "ecc doctor/repair/auto-update", "Both", "Different scopes", "jimmy ecc doctor for harness drift"),
    ("Ops", "Consult / catalog", "N/A in core", "ecc consult + install profiles", "SIDECAR", "Useful for profile advice", "jimmy ecc consult"),
    ("UI", "Control pane", "Desktop / Command Center", "ecc control-pane / ECC2", "SIDECAR", "Don’t replace Jimmy UI", "jimmy ecc control-pane"),
    ("CLI", "Sidecar wrapper", "jimmy ecc …", "node scripts/ecc.js", "PORTED", "Thin wrapper", "jimmy_cli/ecc_cmd.py"),
    ("Adapter", "Command-center worker", "jimmy/adapters/ecc.py", "Same tree", "EXISTS", "Already wired", "Keep"),
    ("Legal", "License", "Apache/MIT mix in Jimmy", "MIT Affaan Mustafa", "OK", "Preserve notices", "THIRD_PARTY_NOTICES_ECC.md"),
]


def main() -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    headers = [
        "Category",
        "Capability",
        "Jimmy",
        "ECC",
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
