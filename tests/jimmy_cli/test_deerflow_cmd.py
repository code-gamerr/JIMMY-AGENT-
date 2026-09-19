"""Tests for jimmy deerflow sidecar CLI helpers."""

from __future__ import annotations

from types import SimpleNamespace
from pathlib import Path

from jimmy_cli.deerflow_cmd import cmd_deerflow, resolve_deerflow_root


def test_resolve_deerflow_root_override(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("DEER_FLOW_HOME", str(tmp_path))
    assert resolve_deerflow_root() == tmp_path.resolve()


def test_doctor_missing_tree(monkeypatch, tmp_path: Path, capsys):
    missing = tmp_path / "nope"
    monkeypatch.setenv("DEER_FLOW_HOME", str(missing))
    code = cmd_deerflow(SimpleNamespace(deerflow_action="doctor"))
    assert code == 1
    assert "not found" in capsys.readouterr().err.lower()


def test_doctor_static_ok(monkeypatch, tmp_path: Path):
    (tmp_path / "docker").mkdir()
    (tmp_path / "docker" / "docker-compose.yaml").write_text("services: {}\n", encoding="utf-8")
    monkeypatch.setenv("DEER_FLOW_HOME", str(tmp_path))
    # No Makefile → static doctor path
    code = cmd_deerflow(SimpleNamespace(deerflow_action="doctor"))
    assert code == 0
