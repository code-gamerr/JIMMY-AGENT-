"""First-turn ``Summarize what is in this folder`` context-cost diagnosis.

Reuses ``jimmy_cli.prompt_size.compute_prompt_breakdown`` so numbers match
what a fresh CLI session would ship (tiers, skills index, tool schemas).
"""

from __future__ import annotations

from typing import Any, Dict

FOLDER_SUMMARIZE_PROMPT = "Summarize what is in this folder"


def diagnose_folder_summarize_cost(platform: str = "cli") -> Dict[str, Any]:
    """Return a structured diagnosis of fixed first-turn context cost."""
    from jimmy_cli.prompt_size import compute_prompt_breakdown, render_breakdown

    breakdown = compute_prompt_breakdown(platform=platform)
    system_bytes = int(breakdown["system_prompt"]["bytes"])
    tools_bytes = int(breakdown["tools"]["json_bytes"])
    prompt_bytes = len(FOLDER_SUMMARIZE_PROMPT.encode("utf-8"))
    fixed = system_bytes + tools_bytes

    sections = []
    for label, chars, byts in breakdown.get("sections") or []:
        sections.append({"label": label, "chars": chars, "bytes": byts})

    report_lines = [
        f"First-turn context cost for: {FOLDER_SUMMARIZE_PROMPT!r}",
        f"  User prompt bytes        : {prompt_bytes:,}",
        f"  Fixed system+tools bytes : {fixed:,}",
        f"  System prompt            : {system_bytes:,}",
        f"  Tool schemas             : {tools_bytes:,}",
        f"  Skills index             : {breakdown['skills_index']['bytes']:,}",
        "",
        render_breakdown(breakdown),
        "",
        "Note: the folder-summarize user turn is tiny; nearly all first-turn",
        "cost is the cached system prompt tiers + tool schemas shipped every call.",
    ]
    return {
        "prompt": FOLDER_SUMMARIZE_PROMPT,
        "platform": platform,
        "user_prompt_bytes": prompt_bytes,
        "first_turn_fixed_bytes": fixed,
        "prompt_breakdown": breakdown,
        "tiers": sections,
        "skills_index_bytes": breakdown["skills_index"]["bytes"],
        "tool_schema_bytes": tools_bytes,
        "report": "\n".join(report_lines),
    }
