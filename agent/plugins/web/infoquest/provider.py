"""InfoQuest web search + fetch — DeerFlow community port as Jimmy plugin."""

from __future__ import annotations

import logging
from typing import Any, Dict, List

import httpx

from agent.web_search_provider import WebSearchProvider, get_provider_env

logger = logging.getLogger(__name__)

_SEARCH_URL = "https://search.infoquest.bytepluses.com"
_FETCH_URL = "https://reader.infoquest.bytepluses.com"


def _headers() -> Dict[str, str]:
    headers = {"Content-Type": "application/json", "X-Client-Name": "jimmy-agent"}
    key = get_provider_env("INFOQUEST_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    return headers


class InfoQuestWebSearchProvider(WebSearchProvider):
    """BytePlus InfoQuest search + page fetch."""

    @property
    def name(self) -> str:
        return "infoquest"

    @property
    def display_name(self) -> str:
        return "InfoQuest"

    def supports_search(self) -> bool:
        return True

    def supports_extract(self) -> bool:
        return True

    def is_available(self) -> bool:
        return bool(get_provider_env("INFOQUEST_API_KEY"))

    def search(self, query: str, *, max_results: int = 5, **kwargs: Any) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "query": query,
            "count": max(1, min(int(max_results or 5), 20)),
        }
        response = httpx.post(_SEARCH_URL, json=payload, headers=_headers(), timeout=60)
        if response.status_code >= 400:
            raise ValueError(response.text or f"HTTP {response.status_code}")
        data = response.json()
        results = data.get("results") or data.get("web") or data.get("data") or []
        web: List[Dict[str, Any]] = []
        for i, item in enumerate(results if isinstance(results, list) else []):
            if not isinstance(item, dict):
                continue
            web.append(
                {
                    "title": item.get("title") or item.get("name") or "",
                    "url": item.get("url") or item.get("link") or "",
                    "description": item.get("description")
                    or item.get("snippet")
                    or item.get("content")
                    or "",
                    "position": i + 1,
                }
            )
        return {"success": True, "data": {"web": web}}

    def extract(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        payload = {"url": url, "return_format": kwargs.get("return_format", "markdown")}
        response = httpx.post(_FETCH_URL, json=payload, headers=_headers(), timeout=90)
        if response.status_code >= 400:
            raise ValueError(response.text or f"HTTP {response.status_code}")
        text = response.text or ""
        content = text
        try:
            body = response.json()
            content = body.get("reader_result") or body.get("content") or text
        except Exception:
            pass
        return {
            "success": True,
            "documents": [
                {
                    "url": url,
                    "title": "",
                    "content": content,
                    "raw_content": content,
                    "metadata": {"sourceURL": url},
                }
            ],
        }
