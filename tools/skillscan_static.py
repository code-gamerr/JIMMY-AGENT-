"""Lean CRITICAL static SkillScan (DeerFlow-inspired) for Jimmy skill installs.

Blocks installs that match high-confidence malicious patterns. Complements
``tools.skills_guard`` (heuristic verdicts) — this module only raises on
CRITICAL content findings.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

logger = logging.getLogger(__name__)

# Kill switch: agent.skill_scan.enabled / env JIMMY_SKILL_SCAN=0
_DEFAULT_ENABLED = True

_TEXT_SUFFIXES = frozenset(
    {
        ".md",
        ".txt",
        ".py",
        ".sh",
        ".bash",
        ".zsh",
        ".js",
        ".ts",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".env",
        ".ps1",
    }
)

_CRITICAL_PATTERNS: Sequence[tuple[str, re.Pattern[str], str]] = (
    (
        "secret-private-key",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "Private key material is embedded in skill content.",
    ),
    (
        "secret-cloud-token",
        re.compile(
            r"(?:sk-[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[a-zA-Z0-9]{36}|xox[baprs]-[a-zA-Z0-9-]{10,})"
        ),
        "High-confidence cloud or API token is embedded in skill content.",
    ),
    (
        "python-dynamic-exec",
        re.compile(r"\b(?:eval|exec)\s*\("),
        "Python dynamic code execution primitive is used in a skill file.",
    ),
    (
        "shell-reverse-shell",
        re.compile(r"(?:bash\s+-i\s+>&\s*/dev/tcp/|nc\s+-[elp].*\d{2,5}|/dev/tcp/[0-9.]+/)"),
        "Shell script contains a reverse-shell idiom.",
    ),
    (
        "network-cloud-metadata",
        re.compile(r"169\.254\.169\.254|metadata\.google\.internal"),
        "Skill content references a cloud metadata service.",
    ),
    (
        "resource-fork-bomb",
        re.compile(r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;?\s*:"),
        "Skill content contains a fork-bomb pattern.",
    ),
)


@dataclass(frozen=True)
class StaticFinding:
    rule_id: str
    path: str
    message: str


class StaticScanBlockedError(Exception):
    """Raised when CRITICAL findings must block skill install."""

    def __init__(self, findings: List[StaticFinding]):
        self.findings = findings
        summary = "; ".join(f"{f.rule_id} ({f.path})" for f in findings[:5])
        super().__init__(f"SkillScan blocked install: {summary}")


def skill_scan_enabled(config: dict | None = None) -> bool:
    import os

    env = os.getenv("JIMMY_SKILL_SCAN", "").strip().lower()
    if env in {"0", "false", "no", "off"}:
        return False
    if env in {"1", "true", "yes", "on"}:
        return True
    if isinstance(config, dict):
        section = config.get("skill_scan") if "skill_scan" in config else None
        if section is None and isinstance(config.get("agent"), dict):
            section = config["agent"].get("skill_scan")
        if isinstance(section, dict) and "enabled" in section:
            return bool(section.get("enabled"))
        if isinstance(section, bool):
            return section
    return _DEFAULT_ENABLED


def _iter_skill_files(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in _TEXT_SUFFIXES or path.name.upper() == "SKILL.MD":
            yield path


def scan_skill_dir(skill_path: Path) -> List[StaticFinding]:
    """Return CRITICAL findings for a quarantined skill directory."""
    findings: List[StaticFinding] = []
    root = Path(skill_path)
    for path in _iter_skill_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = str(path.relative_to(root)).replace("\\", "/")
        for rule_id, pattern, message in _CRITICAL_PATTERNS:
            if pattern.search(text):
                findings.append(StaticFinding(rule_id=rule_id, path=rel, message=message))
    return findings


def enforce_static_scan(skill_path: Path, *, config: dict | None = None) -> None:
    """Raise StaticScanBlockedError when CRITICAL findings are present."""
    if not skill_scan_enabled(config):
        return
    findings = scan_skill_dir(Path(skill_path))
    if findings:
        logger.warning(
            "SkillScan blocked %s (%d CRITICAL findings)", skill_path, len(findings)
        )
        raise StaticScanBlockedError(findings)


def format_static_findings(findings: Sequence[StaticFinding]) -> str:
    lines = ["SkillScan CRITICAL findings:"]
    for finding in findings:
        lines.append(f"- [{finding.rule_id}] {finding.path}: {finding.message}")
    return "\n".join(lines)
