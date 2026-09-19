"""langsmith — DeerFlow-parity observability plugin for Jimmy.

Enables LangSmith tracing when ``LANGSMITH_API_KEY`` (or ``LANGCHAIN_API_KEY``)
is set. Prefer Langfuse for first-class Jimmy hooks; this plugin covers teams
already on LangSmith (as DeerFlow documents).
"""

from __future__ import annotations

import logging
import os

logger = logging.getLogger(__name__)


def register(ctx=None) -> None:
    key = os.environ.get("LANGSMITH_API_KEY") or os.environ.get("LANGCHAIN_API_KEY")
    if not key:
        logger.debug("langsmith plugin loaded without API key — inert")
        return
    # Enable LangChain/LangSmith env tracing for any LangChain clients in-process.
    os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
    if os.environ.get("LANGSMITH_PROJECT") or os.environ.get("LANGCHAIN_PROJECT"):
        os.environ.setdefault(
            "LANGCHAIN_PROJECT",
            os.environ.get("LANGSMITH_PROJECT")
            or os.environ.get("LANGCHAIN_PROJECT")
            or "jimmy",
        )
    else:
        os.environ.setdefault("LANGCHAIN_PROJECT", "jimmy")
    logger.info(
        "LangSmith tracing enabled (project=%s)",
        os.environ.get("LANGCHAIN_PROJECT"),
    )


__all__ = ["register"]
