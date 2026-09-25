"""The checkout root stays the workspace root after the monorepo split."""

from pathlib import Path

from jimmy_cli.config import get_project_root
from jimmy_constants import get_workspace_root


def test_project_root_is_the_checkout():
    root = get_project_root()
    assert root == get_workspace_root()
    assert (root / "pyproject.toml").is_file()
    assert "[tool.uv.workspace]" in (root / "pyproject.toml").read_text(encoding="utf-8")
    assert (root / "agent" / "run_agent.py").is_file()
    assert (root / "app" / "ui-tui" / "package.json").is_file()
    assert (root / "training" / "runners" / "batch_runner.py").is_file()
    assert root == Path(__file__).resolve().parents[1]


def test_agent_and_training_imports():
    import batch_runner
    import jimmy_cli
    import trajectory_compressor

    assert jimmy_cli.__file__
    assert batch_runner.BatchRunner
    assert trajectory_compressor.TrajectoryCompressor
