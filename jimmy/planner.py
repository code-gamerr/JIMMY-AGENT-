"""Route a natural-language request to one or more workers."""

from __future__ import annotations

from dataclasses import dataclass

from jimmy.models import Experience

OPENCLAW_HINTS = (
    "openclaw",
    "telegram",
    "discord",
    "slack",
    "whatsapp",
    "channel",
    "gateway",
    "molty",
    "pairing",
    "control ui",
    "imessage",
    "signal",
)
ECC_HINTS = (
    "ecc",
    "skill",
    "hook",
    "harness",
    "tdd",
    "agent-sort",
    "control pane",
    "memory vault",
    "consult",
    "doctor",
    "ecc-universal",
    "plugin install",
)
MUNDER_HINTS = (
    "munder",
    "difflin",
    "authentication",
    "auth",
    "code",
    "implement",
    "build",
    "test",
    "refactor",
    "file",
    "repo",
    "typescript",
    "electron",
    "frontend",
    "backend",
    "module",
    "dependency",
    "website",
    "landing",
)
LANDING_HINTS = (
    "landing page",
    "landing",
    "marketing site",
    "homepage",
    "hero",
)
RESEARCH_HINTS = (
    "research",
    "investigate",
    "compare",
    "survey",
    "recommend skills",
    "what should i use",
)


@dataclass(frozen=True)
class Plan:
    agent: str
    reason: str
    steps: tuple[dict, ...]
    reused_experience_ids: tuple[str, ...]
    approach: str
    workers: tuple[str, ...] = ()


def _score(text: str, hints: tuple[str, ...]) -> int:
    low = text.lower()
    return sum(2 if hint in low else 0 for hint in hints)


# User-facing assignment copy. Never include route scores or registry internals.
WORKER_ASSIGNMENT = {
    "openclaw": ("messaging", "Handle channel and gateway work"),
    "munder": ("workflow", "Handle workflow and implementation"),
    "research": ("research", "Research and compare options"),
    "ecc": ("validation", "Validate the result"),
    "landing": ("site", "Handle the public site"),
}

WORKER_LABEL = {
    "openclaw": "OpenClaw",
    "munder": "Munder-Difflin",
    "research": "Research",
    "ecc": "ECC",
    "landing": "Landing",
}


def assignment_briefs(workers: tuple[str, ...]) -> tuple[dict, ...]:
    """Public assignment cards for the selected workers, in execution order."""
    briefs = []
    total = len(workers)
    for index, agent_id in enumerate(workers, start=1):
        capability, description = WORKER_ASSIGNMENT.get(
            agent_id, ("work", "Handle the assigned work")
        )
        briefs.append(
            {
                "index": index,
                "total": total,
                "agent_id": agent_id,
                "label": WORKER_LABEL.get(agent_id, agent_id),
                "capability": capability,
                "description": description,
            }
        )
    return tuple(briefs)


def plan_request(
    user_request: str,
    *,
    explicit_agent: str | None = None,
    experiences: list[Experience] | None = None,
) -> Plan:
    experiences = experiences or []
    low = user_request.lower()

    if explicit_agent and explicit_agent != "auto":
        agent = explicit_agent
        reason = f"User pinned agent {agent}"
        reused: tuple[str, ...] = ()
        approach = "explicit-agent"
        workers = (agent,)
    else:
        scores = {
            "openclaw": _score(user_request, OPENCLAW_HINTS),
            "ecc": _score(user_request, ECC_HINTS),
            "munder": _score(user_request, MUNDER_HINTS) + 1,
            "landing": _score(user_request, LANDING_HINTS),
            "research": _score(user_request, RESEARCH_HINTS),
        }
        reused_ids: list[str] = []
        for exp in experiences:
            if not exp.success:
                continue
            scores[exp.agent] = scores.get(exp.agent, 0) + 3
            reused_ids.append(exp.experience_id)
        agent = max(scores, key=scores.get)
        reason = f"Selected {WORKER_LABEL.get(agent, agent)} for this request"
        reused = tuple(reused_ids[:5])
        approach = "keyword+experience"

        # Multi-worker: if the goal spans site + coding + research, assign extras.
        workers_list = [agent]
        if scores["landing"] >= 2 and "landing" not in workers_list:
            workers_list.append("landing")
        if scores["research"] >= 2 and "research" not in workers_list:
            workers_list.append("research")
        if scores["munder"] >= 2 and "munder" not in workers_list and agent != "munder":
            workers_list.append("munder")
        if scores["ecc"] >= 2 and "ecc" not in workers_list and agent != "ecc":
            workers_list.append("ecc")
        # Company-style goals get coding floor + research by default.
        if any(w in low for w in ("company", "startup", "launch", "coordinate", "multi")):
            for extra in ("munder", "research", "landing"):
                if extra not in workers_list:
                    workers_list.append(extra)
        workers = tuple(workers_list)

    steps = (
        {"id": "analyze", "label": "Requirement analyzed", "done": True},
        {
            "id": "select",
            "label": f"Workers selected: {', '.join(workers)}",
            "done": True,
        },
        {"id": "inspect", "label": "Repository / worker inspected", "done": False},
        {"id": "execute", "label": "Worker command running", "done": False},
        {"id": "validate", "label": "Collect result and git/file evidence", "done": False},
    )
    strategy = ""
    if experiences:
        winners = [e for e in experiences if e.success]
        if winners:
            strategy = winners[0].strategy
    return Plan(
        agent=agent,
        reason=reason,
        steps=steps,
        reused_experience_ids=reused,
        approach=strategy or approach,
        workers=workers,
    )
