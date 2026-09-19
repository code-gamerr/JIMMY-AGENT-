"""Tests for jimmy ecc sidecar CLI helpers."""

from __future__ import annotations

from types import SimpleNamespace
from pathlib import Path

from jimmy_cli.ecc_cmd import cmd_ecc, resolve_ecc_root


def test_resolve_ecc_root_override(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("ECC_HOME", str(tmp_path))
    assert resolve_ecc_root() == tmp_path.resolve()


def test_doctor_missing_tree(monkeypatch, tmp_path: Path, capsys):
    missing = tmp_path / "nope"
    monkeypatch.setenv("ECC_HOME", str(missing))
    code = cmd_ecc(SimpleNamespace(ecc_action="doctor", ecc_args=[]))
    assert code == 1
    assert "not found" in capsys.readouterr().err.lower()


def test_doctor_static_without_node(monkeypatch, tmp_path: Path):
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "ecc.js").write_text("console.log('ecc')\n", encoding="utf-8")
    monkeypatch.setenv("ECC_HOME", str(tmp_path))
    monkeypatch.setattr("jimmy_cli.ecc_cmd._node", lambda: None)
    code = cmd_ecc(SimpleNamespace(ecc_action="doctor", ecc_args=[]))
    assert code == 0  # static doctor path when ecc.js present
