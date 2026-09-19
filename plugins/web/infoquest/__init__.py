"""InfoQuest web search + extract plugin — bundled, auto-loaded."""

from __future__ import annotations

from plugins.web.infoquest.provider import InfoQuestWebSearchProvider


def register(ctx) -> None:
    ctx.register_web_search_provider(InfoQuestWebSearchProvider())
