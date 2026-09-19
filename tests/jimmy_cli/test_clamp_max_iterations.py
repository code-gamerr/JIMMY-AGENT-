"""Tests for DeerFlow-parity recursion clamp."""

from jimmy_cli.config import TURN_LIMIT_UNLIMITED, clamp_max_iterations


def test_clamp_oversized_request():
    assert clamp_max_iterations(5000, ceiling=1000) == 1000


def test_clamp_valid_request():
    assert clamp_max_iterations(50, ceiling=1000) == 50


def test_clamp_unlimited_uses_ceiling():
    assert clamp_max_iterations(TURN_LIMIT_UNLIMITED, ceiling=1000) == 1000
