"""Tests for CRITICAL SkillScan static scanner."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.skillscan_static import (
    StaticScanBlockedError,
    enforce_static_scan,
    scan_skill_dir,
)


def test_scan_clean_skill(tmp_path: Path):
    skill = tmp_path / "clean"
    skill.mkdir()
    (skill / "SKILL.md").write_text("# Hello\nDo useful work.\n", encoding="utf-8")
    assert scan_skill_dir(skill) == []
    enforce_static_scan(skill, config={"agent": {"skill_scan": {"enabled": True}}})


def test_scan_blocks_private_key(tmp_path: Path):
    skill = tmp_path / "bad"
    skill.mkdir()
    (skill / "SKILL.md").write_text(
        "-----BEGIN RSA PRIVATE KEY-----\nAAAA\n-----END RSA PRIVATE KEY-----\n",
        encoding="utf-8",
    )
    findings = scan_skill_dir(skill)
    assert any(f.rule_id == "secret-private-key" for f in findings)
    with pytest.raises(StaticScanBlockedError):
        enforce_static_scan(skill)


def test_scan_can_be_disabled(tmp_path: Path):
    skill = tmp_path / "bad"
    skill.mkdir()
    (skill / "SKILL.md").write_text(
        "-----BEGIN RSA PRIVATE KEY-----\nAAAA\n-----END RSA PRIVATE KEY-----\n",
        encoding="utf-8",
    )
    enforce_static_scan(skill, config={"agent": {"skill_scan": {"enabled": False}}})
