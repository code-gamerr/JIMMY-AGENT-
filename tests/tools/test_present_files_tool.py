"""Tests for present_files (DeerFlow-inspired artifacts)."""

import json
from pathlib import Path

from tools.present_files_tool import present_files_tool


def test_present_files_copies_into_session_outputs(tmp_path, monkeypatch):
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "home"))
    src = tmp_path / "report.md"
    src.write_text("# hi\n", encoding="utf-8")

    raw = present_files_tool([str(src)], title="Report", session_id="sess1")
    data = json.loads(raw)
    assert data["presented"]
    presented = Path(data["presented"][0]["presented_path"])
    assert presented.is_file()
    assert presented.read_text(encoding="utf-8") == "# hi\n"
    assert "artifacts" in data["outputs_dir"]
    assert "sess1" in data["outputs_dir"]


def test_present_files_missing_path_errors(tmp_path, monkeypatch):
    monkeypatch.setenv("JIMMY_HOME", str(tmp_path / "home"))
    raw = present_files_tool([str(tmp_path / "nope.txt")], session_id="s")
    data = json.loads(raw)
    assert data["errors"]
    assert data["presented"] == []
