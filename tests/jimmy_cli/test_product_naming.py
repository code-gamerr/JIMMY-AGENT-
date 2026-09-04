"""Behavior tests for Jimmy vs Jimmy CLI product naming.

Covers ``cli_name`` / ``product_name`` resolution (env + argv0), argparse
``prog`` / help epilogue branding, console parser ``prog``, and cache
isolation across cases.
"""

from __future__ import annotations

import pytest

from jimmy_cli import product as product_mod
from jimmy_cli.product import (
    clear_cli_name_cache,
    cli_name,
    is_jimmy,
    product_name,
)


@pytest.fixture(autouse=True)
def _isolate_cli_name_cache(monkeypatch):
    """Each test starts from a clean cache and Jimmy-default env/argv."""
    monkeypatch.delenv("JIMMY_CLI_NAME", raising=False)
    monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
    clear_cli_name_cache()
    yield
    clear_cli_name_cache()


class TestCliNameResolution:
    def test_default_is_jimmy(self):
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"
        assert is_jimmy() is False

    def test_env_jimmy(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"
        assert is_jimmy() is True

    def test_env_jimmy_overrides_jimmy_argv(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        monkeypatch.setattr(product_mod.sys, "argv", ["/usr/bin/jimmy"])
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"

    def test_argv0_jimmy(self, monkeypatch):
        monkeypatch.setattr(product_mod.sys, "argv", ["/usr/local/bin/jimmy"])
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"

    def test_argv0_jimmy_exe(self, monkeypatch):
        monkeypatch.setattr(
            product_mod.sys, "argv", [r"C:\Python\Scripts\jimmy.exe"]
        )
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"

    def test_argv0_jimmy_script_wrapper(self, monkeypatch):
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy-script"])
        clear_cli_name_cache()
        assert cli_name() == "jimmy"

    def test_env_case_and_whitespace_insensitive(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "  Jimmy  ")
        clear_cli_name_cache()
        assert cli_name() == "jimmy"

    def test_unknown_env_falls_back_to_argv(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "other")
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
        clear_cli_name_cache()
        assert cli_name() == "jimmy"

    def test_cache_isolation_between_env_flips(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()
        assert cli_name() == "jimmy"

        monkeypatch.delenv("JIMMY_CLI_NAME", raising=False)
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
        # Without clear, keyed cache still returns jimmy for the new key;
        # after clear, resolution must remain jimmy (isolation / no sticky jimmy).
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        assert product_name() == "Jimmy"

        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        # Keyed cache: new env is visible without an explicit clear.
        assert cli_name() == "jimmy"
        clear_cli_name_cache()
        assert cli_name() == "jimmy"

    def test_cli_name_cache_clear_alias(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()
        assert cli_name() == "jimmy"
        monkeypatch.delenv("JIMMY_CLI_NAME")
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
        cli_name.cache_clear()
        assert cli_name() == "jimmy"


class TestParserProgramNaming:
    def test_jimmy_help_uses_jimmy_prog_and_examples(self, monkeypatch):
        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()

        from jimmy_cli._parser import build_top_level_parser

        parser, _subparsers, chat_parser = build_top_level_parser()
        assert parser.prog == "jimmy"
        assert parser.description.startswith("Jimmy")
        assert "Jimmy" in parser.description
        assert "Jimmy" not in parser.description

        help_text = parser.format_help()
        assert "usage: jimmy" in help_text
        assert "jimmy chat -q" in help_text
        assert "Open the safe Jimmy command console" in help_text
        assert "jimmy chat -q" not in help_text

        assert "Jimmy" in (chat_parser.description or "")

    def test_jimmy_default_help_stays_jimmy(self, monkeypatch):
        monkeypatch.delenv("JIMMY_CLI_NAME", raising=False)
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
        clear_cli_name_cache()

        from jimmy_cli._parser import build_top_level_parser

        parser, _subparsers, chat_parser = build_top_level_parser()
        assert parser.prog == "jimmy"
        assert parser.description.startswith("Jimmy")

        help_text = parser.format_help()
        assert "usage: jimmy" in help_text
        assert "jimmy chat -q" in help_text
        assert "Open the safe Jimmy command console" in help_text
        assert "usage: jimmy" not in help_text
        assert "Jimmy" not in help_text

        assert "Jimmy" in (chat_parser.description or "")

    def test_argv0_jimmy_exe_brands_parser(self, monkeypatch):
        monkeypatch.delenv("JIMMY_CLI_NAME", raising=False)
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy.exe", "--help"])
        clear_cli_name_cache()

        from jimmy_cli._parser import build_top_level_parser

        parser, _subparsers, _chat = build_top_level_parser()
        assert parser.prog == "jimmy"
        assert "jimmy setup" in parser.format_help()


class TestConsoleProgramNaming:
    def test_console_parser_prog_follows_cli_name(self, monkeypatch):
        from jimmy_cli.console_engine import _parser_root

        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()
        parser, _subs = _parser_root()
        assert parser.prog == "jimmy"

        monkeypatch.delenv("JIMMY_CLI_NAME")
        monkeypatch.setattr(product_mod.sys, "argv", ["jimmy"])
        clear_cli_name_cache()
        parser, _subs = _parser_root()
        assert parser.prog == "jimmy"

    def test_console_strips_leading_jimmy_token(self, monkeypatch):
        from jimmy_cli.console_engine import JimmyConsoleEngine

        monkeypatch.setenv("JIMMY_CLI_NAME", "jimmy")
        clear_cli_name_cache()
        engine = JimmyConsoleEngine()
        # `version` is a registered console command; prefix must be ignored.
        result = engine.execute("jimmy version")
        assert result.status == "ok"
        assert result.output  # non-empty version text
