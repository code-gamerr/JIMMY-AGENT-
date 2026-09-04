"""CLI registration for ``jimmy optimize``."""

from __future__ import annotations

import argparse

from jimmy_cli.subcommands.optimize import build_optimize_parser


def test_optimize_parser_wires_func_and_subcommands():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    called = {}

    def cmd_optimize(args):
        called["args"] = args

    build_optimize_parser(sub, cmd_optimize=cmd_optimize)
    assert "optimize" in sub.choices

    args = parser.parse_args(["optimize", "benchmark", "--dry-run"])
    assert args.func is cmd_optimize
    assert args.optimize_command == "benchmark"
    assert args.dry_run is True

    args2 = parser.parse_args(
        ["optimize", "candidate", "--overlay", "{}", "--dry-run"]
    )
    assert args2.optimize_command == "candidate"

    args3 = parser.parse_args(["optimize", "diagnose-context"])
    assert args3.optimize_command == "diagnose-context"

    args4 = parser.parse_args(["optimize", "search", "--dry-run"])
    assert args4.optimize_command == "search"
    assert args4.dry_run is True

    args5 = parser.parse_args(["optimize", "report-offline"])
    assert args5.optimize_command == "report-offline"
