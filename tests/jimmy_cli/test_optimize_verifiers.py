"""Success-verifier behavioral contracts for harness optimize tasks."""

from __future__ import annotations

from pathlib import Path

import pytest

from jimmy_cli.optimize.tasks import get_task


def _ws(tmp_path: Path, seed: dict) -> Path:
    for rel, content in seed.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return tmp_path


def test_folder_summary_rejects_empty_and_hallucinated(tmp_path):
    task = get_task("repo_list_top_level")
    ws = _ws(
        tmp_path,
        {
            "README.md": "# Demo\n",
            "src/main.py": "print('hi')\n",
            "src/util.py": "X = 1\n",
        },
    )
    assert task.check is not None
    assert task.check("", ws, {}) is False
    assert task.check("Everything looks fine here.", ws, {}) is False
    assert task.check("This folder has README.md and main.py", ws, {}) is True


def test_off_by_one_rejects_explanation_without_fix(tmp_path):
    task = get_task("debug_off_by_one")
    ws = _ws(
        tmp_path,
        {
            "bug.py": (
                "def sum_to_n(n):\n"
                "    total = 0\n"
                "    for i in range(n):\n"
                "        total += i\n"
                "    return total\n"
            ),
        },
    )
    assert task.check is not None
    assert task.check("The bug is an off-by-one in range(n).", ws, {}) is False
    # Fix the artifact
    (ws / "bug.py").write_text(
        "def sum_to_n(n):\n"
        "    total = 0\n"
        "    for i in range(n + 1):\n"
        "        total += i\n"
        "    return total\n",
        encoding="utf-8",
    )
    assert task.check("fixed", ws, {}) is True


def test_coding_add_rejects_substring_only_hallucination(tmp_path):
    task = get_task("coding_add_function")
    ws = tmp_path
    assert task.check is not None
    # Substring-only fake that does not define a working add()
    (ws / "math_util.py").write_text(
        "# def add is mentioned but broken\ndef add(a, b):\n    return a - b\n",
        encoding="utf-8",
    )
    assert task.check("wrote def add", ws, {}) is False
    (ws / "math_util.py").write_text(
        "def add(a, b):\n    return a + b\n",
        encoding="utf-8",
    )
    assert task.check("done", ws, {}) is True


def test_hello_py_must_print_hello_world(tmp_path):
    task = get_task("coding_hello_py")
    ws = tmp_path
    assert task.check is not None
    (ws / "hello.py").write_text("print('hi')\n", encoding="utf-8")
    assert task.check("created hello.py", ws, {}) is False
    (ws / "hello.py").write_text("print('Hello, World!')\n", encoding="utf-8")
    assert task.check("ok", ws, {}) is True


def test_safe_div_must_return_none_on_zero(tmp_path):
    task = get_task("debug_div_zero")
    ws = _ws(tmp_path, {"safe_div.py": "def safe_div(a, b):\n    return a / b\n"})
    assert task.check is not None
    assert task.check("return None", ws, {}) is False
    (ws / "safe_div.py").write_text(
        "def safe_div(a, b):\n    if b == 0:\n        return None\n    return a / b\n",
        encoding="utf-8",
    )
    assert task.check("fixed", ws, {}) is True


def test_todo_patch_requires_todo_gone(tmp_path):
    task = get_task("multi_search_and_patch")
    ws = _ws(
        tmp_path,
        {"app/service.py": "x = 1\n# TODO\ny = 2\n", "app/other.py": "pass\n"},
    )
    assert task.check is not None
    assert task.check("DONE", ws, {}) is False
    (ws / "app" / "service.py").write_text("x = 1\n# DONE\ny = 2\n", encoding="utf-8")
    assert task.check("patched", ws, {}) is True
