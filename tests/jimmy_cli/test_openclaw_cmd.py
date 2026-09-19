"""Tests for jimmy openclaw sidecar CLI helpers."""

from __future__ import annotations

from types import SimpleNamespace
from pathlib import Path

from jimmy_cli.openclaw_cmd import cmd_openclaw, resolve_openclaw_root


def test_resolve_openclaw_root_override(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("OPENCLAW_HOME", str(tmp_path))
    assert resolve_openclaw_root() == tmp_path.resolve()


def test_doctor_missing_tree(monkeypatch, tmp_path: Path, capsys):
    missing = tmp_path / "nope"
    monkeypatch.setenv("OPENCLAW_HOME", str(missing))
    code = cmd_openclaw(SimpleNamespace(openclaw_action="doctor", openclaw_args=[]))
    assert code == 1
    assert "not found" in capsys.readouterr().err.lower()


def test_doctor_static_ok(monkeypatch, tmp_path: Path):
    (tmp_path / "openclaw.mjs").write_text("console.log('oc')\n", encoding="utf-8")
    (tmp_path / "skills").mkdir()
    monkeypatch.setenv("OPENCLAW_HOME", str(tmp_path))
    monkeypatch.setattr("jimmy_cli.openclaw_cmd._node", lambda: None)
    code = cmd_openclaw(SimpleNamespace(openclaw_action="doctor", openclaw_args=[]))
    assert code == 0
