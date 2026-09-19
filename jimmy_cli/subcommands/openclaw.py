"""``jimmy openclaw`` subcommand parser (sidecar; migration is ``jimmy claw``)."""

from __future__ import annotations

from typing import Callable


def build_openclaw_parser(subparsers, *, cmd_openclaw: Callable) -> None:
    parser = subparsers.add_parser(
        "openclaw",
        help="Run the optional OpenClaw sidecar (not Jimmy's primary gateway)",
        description=(
            "Thin wrapper over vendored openclaw/openclaw.mjs. "
            "For migrating ~/.openclaw into Jimmy, use `jimmy claw migrate`."
        ),
    )
    parser.add_argument(
        "openclaw_action",
        nargs="?",
        default="doctor",
        choices=["doctor", "status", "help", "dashboard", "gateway", "agent"],
        help="OpenClaw sidecar action",
    )
    parser.add_argument(
        "openclaw_args",
        nargs="*",
        help="Extra args forwarded to openclaw.mjs",
    )
    parser.set_defaults(func=cmd_openclaw)
