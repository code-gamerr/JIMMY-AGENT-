"""``jimmy ecc`` subcommand parser."""

from __future__ import annotations

from typing import Callable


def build_ecc_parser(subparsers, *, cmd_ecc: Callable) -> None:
    parser = subparsers.add_parser(
        "ecc",
        help="Manage the optional ECC harness sidecar",
        description=(
            "Run the vendored ECC (Everything Claude Code) CLI as a sidecar. "
            "Does not replace Jimmy's agent loop. Prefer --no-hooks on setup."
        ),
    )
    parser.add_argument(
        "ecc_action",
        nargs="?",
        default="help",
        choices=[
            "help",
            "doctor",
            "status",
            "consult",
            "memory",
            "control-pane",
            "setup",
        ],
        help="ECC sidecar action",
    )
    parser.add_argument(
        "ecc_args",
        nargs="*",
        help="Extra args forwarded to ecc.js / consult.js",
    )
    parser.set_defaults(func=cmd_ecc)
