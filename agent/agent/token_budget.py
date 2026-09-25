"""Per-run token budget (DeerFlow-inspired, Jimmy-native delivery).

Opt-in via ``agent.token_budget`` in config.yaml. Uses the same cache-safe
tool-result append channel as ``run_budget_seconds`` wrap-up notices.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

TOKEN_BUDGET_WRAPUP_NOTICE = (
    "[SYSTEM NOTICE — token budget nearly exhausted] "
    "Token budget nearly exhausted ({used:,} / {budget:,}, {percent:.0f}%). "
    "Stop new discovery work and produce the final deliverable from what you have."
)

TOKEN_BUDGET_HARD_STOP_NOTICE = (
    "[SYSTEM NOTICE — token budget exceeded] "
    "Token budget exceeded ({used:,} / {budget:,}). "
    "Do not call any more tools. Produce a final answer from results collected so far."
)


def _budget_cfg(agent: Any) -> Optional[Dict[str, Any]]:
    cfg = getattr(agent, "token_budget", None)
    if isinstance(cfg, dict) and cfg.get("enabled") and cfg.get("total"):
        try:
            total = int(cfg["total"])
        except (TypeError, ValueError):
            return None
        if total <= 0:
            return None
        return cfg
    return None


def _append_tool_notice(messages: List[Dict[str, Any]], notice: str) -> bool:
    for i in range(len(messages) - 1, -1, -1):
        msg = messages[i]
        if not (isinstance(msg, dict) and msg.get("role") == "tool"):
            continue
        existing = msg.get("content", "")
        if isinstance(existing, str):
            msg["content"] = existing + f"\n\n{notice}"
            return True
        try:
            blocks = list(existing) if existing else []
            blocks.append({"type": "text", "text": notice})
            msg["content"] = blocks
            return True
        except Exception:
            return False
    return False


def maybe_inject_token_budget_wrapup(agent: Any, messages: List[Dict[str, Any]]) -> bool:
    """Warn once when cumulative session tokens cross the warn fraction."""
    cfg = _budget_cfg(agent)
    if not cfg:
        return False
    if getattr(agent, "_token_budget_wrapup_injected", False):
        return False
    total = int(cfg["total"])
    warn_fraction = float(cfg.get("warn_fraction", 0.8) or 0.8)
    used = int(getattr(agent, "session_total_tokens", 0) or 0)
    if used < warn_fraction * total:
        return False
    notice = TOKEN_BUDGET_WRAPUP_NOTICE.format(
        used=used, budget=total, percent=100.0 * used / total
    )
    if _append_tool_notice(messages, notice):
        agent._token_budget_wrapup_injected = True
        logger.info(
            "Token budget wrap-up injected (used=%s budget=%s)", used, total
        )
        return True
    return False


def token_budget_hard_stop_reached(agent: Any) -> bool:
    """True when cumulative tokens crossed the hard-stop fraction."""
    cfg = _budget_cfg(agent)
    if not cfg:
        return False
    total = int(cfg["total"])
    hard = float(cfg.get("hard_stop_fraction", 1.0) or 1.0)
    used = int(getattr(agent, "session_total_tokens", 0) or 0)
    return used >= hard * total


def maybe_apply_token_budget_hard_stop(
    agent: Any,
    messages: List[Dict[str, Any]],
    assistant_message: Any,
) -> bool:
    """Strip tool_calls on the assistant message when hard-stop fires.

    Returns True when a hard-stop was applied. Also injects a tool notice when
    possible so the model sees why tools were cleared on the next iteration
    (usually the loop ends this turn).
    """
    if not token_budget_hard_stop_reached(agent):
        return False
    if getattr(agent, "_token_budget_hard_stopped", False):
        return True

    tool_calls = getattr(assistant_message, "tool_calls", None)
    if tool_calls:
        try:
            assistant_message.tool_calls = None
        except Exception:
            try:
                assistant_message.tool_calls = []
            except Exception:
                pass

    cfg = _budget_cfg(agent) or {}
    total = int(cfg.get("total") or 0)
    used = int(getattr(agent, "session_total_tokens", 0) or 0)
    notice = TOKEN_BUDGET_HARD_STOP_NOTICE.format(used=used, budget=total)
    _append_tool_notice(messages, notice)
    agent._token_budget_hard_stopped = True
    agent._token_budget_stop_reason = "token_capped"
    logger.warning(
        "Token budget hard-stop applied (used=%s budget=%s)", used, total
    )
    return True
