"""GitHub webhook platform plugin (DeerFlow-inspired).

Jimmy already ships a generic webhook adapter that can validate HMAC,
render prompts from GitHub events, run the agent, and deliver replies as
``github_comment``. This plugin documents and installs a recommended
route recipe so GitHub Issues/PR comments behave like DeerFlow's first-class
GitHub channel without a second HTTP stack.
"""

from __future__ import annotations

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

# Recommended platforms.webhook.extra.routes entry for GitHub.
GITHUB_ROUTE_RECIPE: Dict[str, Any] = {
    "name": "github",
    "events": [
        "issues",
        "issue_comment",
        "pull_request",
        "pull_request_review_comment",
    ],
    "secret_env": "GITHUB_WEBHOOK_SECRET",
    "prompt": (
        "You are Jimmy responding on GitHub.\n"
        "Event: {event}\n"
        "Repository: {repository[full_name]}\n"
        "Sender: {sender[login]}\n"
        "Payload summary:\n{payload_json}\n\n"
        "Write a helpful, concise reply suitable for a GitHub comment. "
        "If no reply is needed, respond with [SILENT]."
    ),
    "deliver": "github_comment",
}


def register(ctx: Any = None) -> None:
    """Plugin entry — recipe is applied via gateway webhook config docs."""
    logger.debug(
        "github-platform loaded; enable via gateway webhook routes "
        "(see plugins/platforms/github/README.md)"
    )


__all__ = ["GITHUB_ROUTE_RECIPE", "register"]
