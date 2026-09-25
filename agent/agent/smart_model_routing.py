"""Prompt-based cheap/strong model routing for a single user turn.

When ``smart_model_routing.enabled`` is true, Jimmy picks ``cheap_model`` or
``strong_model`` from a lightweight heuristic over the user prompt — no extra
LLM call (keeps latency/cost low and avoids tool-schema churn).

Per-turn model changes rebuild the agent for that turn (cache prefix is
per-model), which is intentional for this opt-in feature.
"""

from __future__ import annotations

import re
from typing import Any, Mapping, Optional

# Signals that usually need the frontier/strong model.
_STRONG_PATTERNS = (
    re.compile(r"```"),  # code fence
    re.compile(
        r"\b("
        r"implement|refactor|architect|debug|traceback|stack\s*trace|"
        r"optimize|benchmark|migrate|redesign|multi[- ]?step|"
        r"write\s+(a\s+)?(full|complete|production)|"
        r"deep\s+dive|root\s+cause|security\s+audit|"
        r"design\s+(a\s+)?system|compare\s+and\s+contrast|"
        r"pull\s+request|code\s+review|unit\s+tests?|"
        r"end[- ]?to[- ]?end|e2e|dockerfile|kubernetes|terraform|"
        r"prove|derive|formal\s+proof"
        r")\b",
        re.I,
    ),
)

# Short chit-chat / trivia that can stay on the cheap model.
_CHEAP_PATTERNS = (
    re.compile(
        r"^\s*("
        r"hi|hello|hey|thanks|thank\s+you|ok|okay|yes|no|yep|nope|"
        r"good\s+(morning|afternoon|evening)|how\s+are\s+you|"
        r"what('?s|\s+is)\s+up"
        r")[\s!.?]*$",
        re.I,
    ),
    re.compile(
        r"^\s*("
        r"what\s+time\s+is\s+it|what('?s|\s+is)\s+the\s+date|"
        r"who\s+are\s+you|what\s+can\s+you\s+do|"
        r"ping|test|hello\s+world"
        r")[\s!.?]*$",
        re.I,
    ),
)


def _cfg(mapping: Optional[Mapping[str, Any]] = None) -> dict[str, Any]:
    if mapping is not None:
        return dict(mapping)
    try:
        from jimmy_cli.config import load_config

        raw = load_config().get("smart_model_routing") or {}
        return dict(raw) if isinstance(raw, dict) else {}
    except Exception:
        return {}


def classify_prompt_tier(
    user_message: str,
    *,
    cheap_max_chars: int = 400,
) -> str:
    """Return ``\"cheap\"`` or ``\"strong\"`` for *user_message*."""
    text = (user_message or "").strip()
    if not text:
        return "cheap"

    for pat in _STRONG_PATTERNS:
        if pat.search(text):
            return "strong"

    if len(text) > max(50, int(cheap_max_chars)):
        return "strong"

    # Multi-paragraph or many lines → treat as strong.
    if text.count("\n") >= 6:
        return "strong"

    for pat in _CHEAP_PATTERNS:
        if pat.match(text):
            return "cheap"

    # Short single-sentence questions default to cheap.
    if len(text) <= cheap_max_chars and text.count("?") <= 2 and text.count("\n") <= 2:
        return "cheap"

    return "strong"


def resolve_routed_model(
    user_message: str,
    *,
    current_model: str,
    config: Optional[Mapping[str, Any]] = None,
) -> tuple[str, Optional[str]]:
    """Pick the model id for this turn.

    Returns ``(model_id, tier)`` where *tier* is ``\"cheap\"``, ``\"strong\"``,
    or ``None`` when routing is inactive (caller keeps *current_model*).
    """
    cfg = _cfg(config)
    if not cfg.get("enabled"):
        return current_model, None

    cheap = str(cfg.get("cheap_model") or "").strip()
    strong = str(cfg.get("strong_model") or "").strip()
    if not cheap or not strong:
        return current_model, None
    if "embedding" in cheap.lower() or "embedding" in strong.lower():
        return current_model, None

    max_chars = cfg.get("cheap_max_chars", 400)
    try:
        max_chars = int(max_chars)
    except (TypeError, ValueError):
        max_chars = 400

    tier = classify_prompt_tier(user_message, cheap_max_chars=max_chars)
    chosen = cheap if tier == "cheap" else strong
    return chosen, tier


def apply_smart_model_routing(
    user_message: str,
    route: dict[str, Any],
    *,
    config: Optional[Mapping[str, Any]] = None,
) -> dict[str, Any]:
    """Mutate a turn *route* dict in place (and return it) with routed model.

    Expects ``route`` shaped like ``_resolve_turn_agent_config`` output:
    ``{\"model\", \"runtime\", \"signature\", ...}``.
    """
    current = str(route.get("model") or "")
    chosen, tier = resolve_routed_model(
        user_message, current_model=current, config=config
    )
    if tier is None or chosen == current:
        route.setdefault("_smart_route_tier", tier)
        return route

    runtime = dict(route.get("runtime") or {})
    route["model"] = chosen
    route["runtime"] = runtime
    route["signature"] = (
        chosen,
        runtime.get("provider"),
        runtime.get("requested_provider"),
        runtime.get("base_url"),
        runtime.get("api_mode"),
        runtime.get("command"),
        tuple(runtime.get("args") or ()),
    )
    route["_smart_route_tier"] = tier
    return route
