"""Tests for prompt-based smart_model_routing."""

from agent.smart_model_routing import (
    apply_smart_model_routing,
    classify_prompt_tier,
    resolve_routed_model,
)


CFG = {
    "enabled": True,
    "cheap_model": "gpt-5-mini",
    "strong_model": "gpt-6-astra",
    "cheap_max_chars": 400,
}


def test_classify_greeting_is_cheap():
    assert classify_prompt_tier("hi") == "cheap"
    assert classify_prompt_tier("Thanks!") == "cheap"


def test_classify_code_fence_is_strong():
    assert classify_prompt_tier("fix this:\n```python\nx=1\n```") == "strong"


def test_classify_implement_keyword_is_strong():
    assert classify_prompt_tier("please implement a rate limiter") == "strong"


def test_classify_short_question_is_cheap():
    assert classify_prompt_tier("what time is it in Tokyo?") == "cheap"


def test_classify_long_prompt_is_strong():
    assert classify_prompt_tier("x" * 500) == "strong"


def test_resolve_inactive_when_disabled():
    model, tier = resolve_routed_model(
        "hi", current_model="gpt-6-astra", config={**CFG, "enabled": False}
    )
    assert model == "gpt-6-astra"
    assert tier is None


def test_resolve_picks_mini_for_simple():
    model, tier = resolve_routed_model("hello", current_model="gpt-6-astra", config=CFG)
    assert model == "gpt-5-mini"
    assert tier == "cheap"


def test_resolve_picks_astra_for_hard():
    model, tier = resolve_routed_model(
        "Refactor this module and add unit tests",
        current_model="gpt-5-mini",
        config=CFG,
    )
    assert model == "gpt-6-astra"
    assert tier == "strong"


def test_apply_updates_signature():
    route = {
        "model": "gpt-6-astra",
        "runtime": {
            "provider": "azure",
            "requested_provider": "azure",
            "base_url": "https://example.openai.azure.com",
            "api_mode": "chat_completions",
            "command": None,
            "args": [],
        },
        "signature": ("gpt-6-astra", "azure", "azure", "https://example.openai.azure.com", "chat_completions", None, ()),
    }
    out = apply_smart_model_routing("hi there", route, config=CFG)
    assert out["model"] == "gpt-5-mini"
    assert out["signature"][0] == "gpt-5-mini"
    assert out["_smart_route_tier"] == "cheap"
