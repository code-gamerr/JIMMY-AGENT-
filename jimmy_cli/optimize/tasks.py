"""Deterministic representative task definitions for harness optimize.

Success checkers are behavioral where possible: they execute/import safe
fixture code and assert filesystem state — not substring-only heuristics.
"""

from __future__ import annotations

import ast
import importlib.util
import json
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence

TASK_CATEGORIES: Sequence[str] = (
    "qa",
    "coding",
    "debugging",
    "repo_exploration",
    "file_manipulation",
    "multi_step_tools",
)

SuccessFn = Callable[[str, Path, Dict], bool]


@dataclass(frozen=True)
class OptimizeTask:
    id: str
    category: str
    prompt: str
    expected_max_llm_turns: int = 1
    expected_max_tool_calls: int = 0
    max_useful_completion_tokens: int = 120
    # Seed files relative to the task workspace: path -> content
    seed_files: Dict[str, str] = field(default_factory=dict)
    # Offline fake-runner expected success (deterministic fixtures).
    fake_success: bool = True
    fake_completion_tokens: int = 40
    fake_llm_turns: int = 1
    fake_tool_calls: int = 0
    # Optional checker for real-runner responses (response, workspace, meta).
    check: Optional[SuccessFn] = None
    description: str = ""


def _contains(*needles: str) -> SuccessFn:
    lowered = tuple(n.lower() for n in needles)

    def _check(response: str, _ws: Path, _meta: Dict) -> bool:
        text = (response or "").lower()
        return all(n in text for n in lowered)

    return _check


_ALLOWED_STDLIB = frozenset(
    {"json", "math", "typing", "dataclasses", "collections", "re"}
)
_DENIED_IMPORT_ROOTS = frozenset(
    {
        "os",
        "sys",
        "subprocess",
        "socket",
        "ctypes",
        "shutil",
        "builtins",
        "pty",
        "fcntl",
        "pathlib",
        "importlib",
        "pickle",
        "code",
        "codeop",
        "multiprocessing",
        "threading",
        "asyncio",
        "http",
        "urllib",
        "requests",
    }
)


def _load_module(path: Path, module_name: str = "_optimize_fixture"):
    """Import a workspace .py file after a lightweight AST safety screen."""
    if not path.is_file():
        raise FileNotFoundError(path)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names: List[str] = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif node.module:
                names = [node.module.split(".")[0]]
            for name in names:
                if not name:
                    continue
                if name in _DENIED_IMPORT_ROOTS:
                    raise ValueError(f"disallowed import: {name}")
                # Allow known stdlib + simple local module names (no dots).
                if name not in _ALLOWED_STDLIB and "." in name:
                    raise ValueError(f"disallowed import: {name}")
        if isinstance(node, (ast.Global, ast.Nonlocal)):
            raise ValueError("disallowed global/nonlocal")
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    if spec is None:
        raise ImportError(module_name)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(tree, str(path), "exec"), mod.__dict__)
    return mod


def _file_exists_exact(rel: str, *, must_equal: Optional[str] = None,
                       must_contain: Optional[str] = None) -> SuccessFn:
    def _check(_response: str, ws: Path, _meta: Dict) -> bool:
        path = ws / rel
        if not path.is_file():
            return False
        body = path.read_text(encoding="utf-8")
        if must_equal is not None and body != must_equal:
            return False
        if must_contain is not None and must_contain not in body:
            return False
        return True

    return _check


def _check_hello_py(response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "hello.py"
    if not path.is_file():
        return False
    # Execute and capture print output.
    import io
    import contextlib

    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mod = _load_module(path, "_hello_py")
            # If module only defines code at top level, stdout already captured.
            # Also accept a main() if present.
            if hasattr(mod, "main") and callable(mod.main):
                mod.main()
    except Exception:
        return False
    out = buf.getvalue()
    return "Hello, World!" in out


def _check_add_function(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "math_util.py"
    if not path.is_file():
        return False
    try:
        mod = _load_module(path, "_math_util")
        return callable(getattr(mod, "add", None)) and mod.add(2, 3) == 5
    except Exception:
        return False


def _check_test_assert(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "test_add.py"
    if not path.is_file():
        return False
    # Ensure math_util is importable from workspace.
    import sys

    sys_path_added = False
    try:
        if str(ws) not in sys.path:
            sys.path.insert(0, str(ws))
            sys_path_added = True
        # Run the test file as a module; assert failures → fail.
        _load_module(path, "_test_add")
        return True
    except Exception:
        return False
    finally:
        if sys_path_added:
            try:
                sys.path.remove(str(ws))
            except ValueError:
                pass


def _check_json_parse(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "parse_cfg.py"
    if not path.is_file():
        return False
    try:
        mod = _load_module(path, "_parse_cfg")
        load_cfg = getattr(mod, "load_cfg", None)
        if not callable(load_cfg):
            return False
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as fh:
            json.dump({"a": 1}, fh)
            tmp = fh.name
        try:
            result = load_cfg(tmp)
        finally:
            Path(tmp).unlink(missing_ok=True)
        return isinstance(result, dict) and result.get("a") == 1
    except Exception:
        return False


def _check_off_by_one(_response: str, ws: Path, _meta: Dict) -> bool:
    """Must fix bug.py so sum_to_n(n) == n*(n+1)/2 — explanations alone fail."""
    path = ws / "bug.py"
    if not path.is_file():
        return False
    try:
        mod = _load_module(path, "_bug_sum")
        fn = getattr(mod, "sum_to_n", None)
        if not callable(fn):
            return False
        for n, expected in ((0, 0), (1, 1), (5, 15), (10, 55)):
            if fn(n) != expected:
                return False
        return True
    except Exception:
        return False


def _check_greet(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "broken.py"
    if not path.is_file():
        return False
    try:
        mod = _load_module(path, "_broken_greet")
        greet = getattr(mod, "greet", None)
        return callable(greet) and greet() == "Hello"
    except Exception:
        return False


def _check_safe_div(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "safe_div.py"
    if not path.is_file():
        return False
    try:
        mod = _load_module(path, "_safe_div")
        fn = getattr(mod, "safe_div", None)
        if not callable(fn):
            return False
        return fn(10, 2) == 5 and fn(1, 0) is None
    except Exception:
        return False


def _folder_summary_check() -> SuccessFn:
    """Require naming real seeded artifacts — empty/hallucinated text fails."""

    def _check(response: str, ws: Path, _meta: Dict) -> bool:
        text = (response or "").lower()
        if not text.strip():
            return False
        files = [p for p in ws.rglob("*") if p.is_file()]
        if not files:
            return False
        # Must mention at least two distinct seeded file basenames or paths.
        hits = 0
        for path in files:
            name = path.name.lower()
            rel = str(path.relative_to(ws)).replace("\\", "/").lower()
            stem = path.stem.lower()
            if name in text or rel in text or stem in text:
                hits += 1
        return hits >= 2

    return _check


def _check_config_enabled(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "config.json"
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("enabled") is True
    except Exception:
        return False


def _check_todo_patched(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "app" / "service.py"
    if not path.is_file():
        return False
    body = path.read_text(encoding="utf-8")
    return "DONE" in body and "TODO" not in body


def _check_copy_and_hash(_response: str, ws: Path, _meta: Dict) -> bool:
    secret = ws / "secret.txt"
    backup = ws / "backup" / "secret.txt"
    length = ws / "backup" / "len.txt"
    if not (secret.is_file() and backup.is_file() and length.is_file()):
        return False
    raw = secret.read_bytes()
    if backup.read_bytes() != raw:
        return False
    try:
        return int(length.read_text(encoding="utf-8").strip()) == len(raw)
    except Exception:
        return False


def _check_pipeline(_response: str, ws: Path, _meta: Dict) -> bool:
    a = ws / "a.txt"
    b = ws / "b.txt"
    c = ws / "c.txt"
    if not (a.is_file() and b.is_file() and c.is_file()):
        return False
    if a.read_text(encoding="utf-8").strip() != "alpha":
        return False
    if b.read_text(encoding="utf-8").strip() != "beta":
        return False
    body = c.read_text(encoding="utf-8")
    return "alpha" in body and "beta" in body


def _check_rename_note(_response: str, ws: Path, _meta: Dict) -> bool:
    return (
        (ws / "note.md").is_file()
        and not (ws / "note.txt").exists()
        and (ws / "note.md").read_text(encoding="utf-8") == "keep me\n"
    )


def _check_append_line(_response: str, ws: Path, _meta: Dict) -> bool:
    path = ws / "log.txt"
    if not path.is_file():
        return False
    lines = path.read_text(encoding="utf-8").splitlines()
    return lines[:1] == ["start"] and any(line.strip() == "done" for line in lines)


def _check_delete_temp(_response: str, ws: Path, _meta: Dict) -> bool:
    return (not (ws / "temp.bin").exists()) and (ws / "keep.txt").is_file()


def _check_count_py(_response: str, ws: Path, _meta: Dict) -> bool:
    text = (response or "").strip()
    # Prefer exact number; reject unrelated prose that happens to contain "3".
    if re.fullmatch(r"3", text):
        return True
    # Allow short answers like "3 files" / "There are 3".
    return bool(re.search(r"(^|\D)3(\D|$)", text)) and len(text) < 40


def _build_tasks() -> List[OptimizeTask]:
    return [
        # --- simple Q&A ---
        OptimizeTask(
            id="qa_capital_france",
            category="qa",
            prompt="What is the capital of France? Answer with one word.",
            max_useful_completion_tokens=20,
            fake_completion_tokens=5,
            check=_contains("paris"),
            description="One-word factual answer",
        ),
        OptimizeTask(
            id="qa_two_plus_two",
            category="qa",
            prompt="What is 2 + 2? Reply with only the number.",
            max_useful_completion_tokens=10,
            fake_completion_tokens=2,
            check=_contains("4"),
            description="Arithmetic smoke check",
        ),
        OptimizeTask(
            id="qa_http_meaning",
            category="qa",
            prompt="What does HTTP stand for? One sentence.",
            max_useful_completion_tokens=60,
            check=_contains("hypertext", "transfer"),
        ),
        OptimizeTask(
            id="qa_list_three_primaries",
            category="qa",
            prompt="List the three primary colors.",
            max_useful_completion_tokens=40,
            check=_contains("red", "blue"),
        ),
        # --- coding ---
        OptimizeTask(
            id="coding_hello_py",
            category="coding",
            prompt=(
                "Create a file hello.py that prints Hello, World! when run. "
                "Do not explain."
            ),
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            max_useful_completion_tokens=80,
            fake_llm_turns=4,
            fake_tool_calls=4,
            fake_completion_tokens=30,
            check=_check_hello_py,
        ),
        OptimizeTask(
            id="coding_add_function",
            category="coding",
            prompt=(
                "Write math_util.py defining def add(a, b): return a + b"
            ),
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_add_function,
        ),
        OptimizeTask(
            id="coding_test_assert",
            category="coding",
            prompt=(
                "Create test_add.py that asserts add(2, 3) == 5. "
                "Assume math_util.add exists."
            ),
            seed_files={
                "math_util.py": "def add(a, b):\n    return a + b\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_test_assert,
        ),
        OptimizeTask(
            id="coding_json_parse",
            category="coding",
            prompt=(
                "Create parse_cfg.py with a function load_cfg(path) that "
                "json-loads a file and returns the dict."
            ),
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_json_parse,
        ),
        # --- debugging ---
        OptimizeTask(
            id="debug_off_by_one",
            category="debugging",
            prompt=(
                "bug.py has an off-by-one error in sum_to_n. Fix it in place."
            ),
            seed_files={
                "bug.py": (
                    "def sum_to_n(n):\n"
                    "    total = 0\n"
                    "    for i in range(n):\n"
                    "        total += i\n"
                    "    return total\n"
                ),
            },
            expected_max_llm_turns=3,
            expected_max_tool_calls=3,
            fake_llm_turns=5,
            fake_tool_calls=5,
            check=_check_off_by_one,
        ),
        OptimizeTask(
            id="debug_name_error",
            category="debugging",
            prompt="Fix the NameError in broken.py so greet() returns Hello.",
            seed_files={
                "broken.py": "def greet():\n    return Helllo\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_greet,
        ),
        OptimizeTask(
            id="debug_div_zero",
            category="debugging",
            prompt=(
                "safe_div.py raises on b=0. Make it return None when b is 0."
            ),
            seed_files={
                "safe_div.py": "def safe_div(a, b):\n    return a / b\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_safe_div,
        ),
        OptimizeTask(
            id="debug_read_traceback",
            category="debugging",
            prompt=(
                "traceback.txt shows a crash. Name the missing variable in one word."
            ),
            seed_files={
                "traceback.txt": (
                    "Traceback (most recent call last):\n"
                    '  File "app.py", line 3, in <module>\n'
                    "    print(missing_value)\n"
                    "NameError: name 'missing_value' is not defined\n"
                ),
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=1,
            fake_llm_turns=1,
            fake_tool_calls=1,
            fake_completion_tokens=5,
            check=_contains("missing_value"),
        ),
        # --- repo exploration ---
        OptimizeTask(
            id="repo_list_top_level",
            category="repo_exploration",
            prompt="Summarize what is in this folder",
            seed_files={
                "README.md": "# Demo\nA tiny repo.\n",
                "src/main.py": "print('hi')\n",
                "src/util.py": "X = 1\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=3,
            max_useful_completion_tokens=150,
            fake_llm_turns=4,
            fake_tool_calls=5,
            fake_completion_tokens=60,
            check=_folder_summary_check(),
            description="First-turn folder summarize (context-cost probe)",
        ),
        OptimizeTask(
            id="repo_find_entry_point",
            category="repo_exploration",
            prompt="Which file is the entry point? Reply with the path only.",
            seed_files={
                "README.md": "Run src/cli.py\n",
                "src/cli.py": "def main():\n    pass\n",
                "src/lib.py": "pass\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=2,
            fake_tool_calls=1,
            check=_contains("cli.py"),
        ),
        OptimizeTask(
            id="repo_count_py_files",
            category="repo_exploration",
            prompt="How many .py files are under this folder? Reply with a number.",
            seed_files={
                "a.py": "pass\n",
                "b/c.py": "pass\n",
                "b/d.py": "pass\n",
                "notes.txt": "ignore\n",
            },
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=2,
            fake_tool_calls=1,
            fake_completion_tokens=3,
            check=_check_count_py,
        ),
        OptimizeTask(
            id="repo_read_version",
            category="repo_exploration",
            prompt="What version is declared in VERSION? Reply with the version only.",
            seed_files={"VERSION": "1.4.2\n"},
            expected_max_llm_turns=2,
            expected_max_tool_calls=1,
            fake_llm_turns=1,
            fake_tool_calls=1,
            fake_completion_tokens=5,
            check=_contains("1.4.2"),
        ),
        # --- file manipulation ---
        OptimizeTask(
            id="file_rename_note",
            category="file_manipulation",
            prompt="Rename note.txt to note.md (keep contents).",
            seed_files={"note.txt": "keep me\n"},
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_rename_note,
        ),
        OptimizeTask(
            id="file_append_line",
            category="file_manipulation",
            prompt="Append a line 'done' to log.txt.",
            seed_files={"log.txt": "start\n"},
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_check_append_line,
        ),
        OptimizeTask(
            id="file_create_nested",
            category="file_manipulation",
            prompt="Create out/data/flag.txt containing ok.",
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=4,
            fake_tool_calls=4,
            check=_file_exists_exact("out/data/flag.txt", must_contain="ok"),
        ),
        OptimizeTask(
            id="file_delete_temp",
            category="file_manipulation",
            prompt="Delete temp.bin if it exists. Confirm briefly.",
            seed_files={"temp.bin": "x", "keep.txt": "y"},
            expected_max_llm_turns=2,
            expected_max_tool_calls=2,
            fake_llm_turns=1,
            fake_tool_calls=1,
            check=_check_delete_temp,
        ),
        # --- multi-step tool usage ---
        OptimizeTask(
            id="multi_read_edit_verify",
            category="multi_step_tools",
            prompt=(
                "Read config.json, set enabled to true, write it back, "
                "then confirm the value."
            ),
            seed_files={"config.json": '{"enabled": false}\n'},
            expected_max_llm_turns=3,
            expected_max_tool_calls=4,
            fake_llm_turns=5,
            fake_tool_calls=6,
            fake_completion_tokens=50,
            check=_check_config_enabled,
        ),
        OptimizeTask(
            id="multi_search_and_patch",
            category="multi_step_tools",
            prompt=(
                "Find TODO in the repo and replace it with DONE in that file."
            ),
            seed_files={
                "app/service.py": "x = 1\n# TODO\ny = 2\n",
                "app/other.py": "pass\n",
            },
            expected_max_llm_turns=3,
            expected_max_tool_calls=4,
            fake_llm_turns=5,
            fake_tool_calls=6,
            check=_check_todo_patched,
        ),
        OptimizeTask(
            id="multi_copy_and_hash",
            category="multi_step_tools",
            prompt=(
                "Copy secret.txt to backup/secret.txt and write its byte length "
                "into backup/len.txt."
            ),
            seed_files={"secret.txt": "abcdef\n"},
            expected_max_llm_turns=3,
            expected_max_tool_calls=4,
            fake_llm_turns=5,
            fake_tool_calls=6,
            check=_check_copy_and_hash,
        ),
        OptimizeTask(
            id="multi_pipeline_echo",
            category="multi_step_tools",
            prompt=(
                "Create a.txt with 'alpha', b.txt with 'beta', then c.txt "
                "containing both lines concatenated."
            ),
            expected_max_llm_turns=3,
            expected_max_tool_calls=4,
            fake_llm_turns=5,
            fake_tool_calls=6,
            check=_check_pipeline,
        ),
    ]


_TASKS: List[OptimizeTask] = _build_tasks()
_BY_ID: Dict[str, OptimizeTask] = {t.id: t for t in _TASKS}


def list_tasks(
    categories: Optional[Sequence[str]] = None,
    task_ids: Optional[Sequence[str]] = None,
) -> List[OptimizeTask]:
    tasks = list(_TASKS)
    if task_ids:
        wanted = set(task_ids)
        tasks = [t for t in tasks if t.id in wanted]
    if categories:
        wanted_c = set(categories)
        tasks = [t for t in tasks if t.category in wanted_c]
    return tasks


def get_task(task_id: str) -> OptimizeTask:
    try:
        return _BY_ID[task_id]
    except KeyError as exc:
        raise KeyError(f"unknown optimize task: {task_id}") from exc
