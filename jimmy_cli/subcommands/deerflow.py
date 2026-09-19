"""``jimmy deerflow`` subcommand parser."""

from __future__ import annotations

from typing import Callable


def build_deerflow_parser(subparsers, *, cmd_deerflow: Callable) -> None:
    parser = subparsers.add_parser(
        "deerflow",
        help="Manage the optional DeerFlow research sidecar",
        description=(
            "Run the vendored deer-flow Compose stack as an optional sidecar. "
            "Does not replace Jimmy's agent loop."
        ),
    )
    parser.add_argument(
        "deerflow_action",
        choices=["setup", "up", "down", "doctor"],
        help="setup | up | down | doctor",
    )
    parser.set_defaults(func=cmd_deerflow)
