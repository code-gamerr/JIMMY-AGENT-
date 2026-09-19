"""Tests for cron fire-claim TTL config."""

from cron.lease_config import fire_claim_kwargs, fire_claim_ttl_seconds


def test_fire_claim_kwargs_empty_at_default():
    assert fire_claim_kwargs({}) == {}


def test_fire_claim_kwargs_when_overridden():
    cfg = {"cron": {"multi_instance": {"fire_claim_ttl_seconds": 600}}}
    assert fire_claim_kwargs(cfg) == {"claim_ttl_seconds": 600}


def test_fire_claim_ttl_default():
    assert fire_claim_ttl_seconds({}) == 300


def test_fire_claim_ttl_from_config():
    assert (
        fire_claim_ttl_seconds(
            {"cron": {"multi_instance": {"fire_claim_ttl_seconds": 600}}}
        )
        == 600
    )


def test_fire_claim_ttl_clamped():
    assert fire_claim_ttl_seconds(
        {"cron": {"multi_instance": {"fire_claim_ttl_seconds": 1}}}
    ) == 30
