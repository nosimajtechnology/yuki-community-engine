#!/usr/bin/env python3
"""Validate the portable Yuki Community Engine repository."""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "assets/canon/yuki-turnaround.png",
    "canon/character/yuki-canon.md",
    "canon/world/y2kverse.md",
    "canon/references/source-register.md",
    "engine/core/brief-contract.md",
    "engine/modes/modes.md",
    "engine/continuity/continuity-ledger.md",
    "engine/storyboard/storyboard-system.md",
    "engine/research/historical-grounding.md",
    "adapters/adapter-contract.md",
    "adapters/image/image-generation.md",
    "adapters/video/video-generation.md",
    "community/quickstart/quickstart.md",
    "community/remix-templates/starter-templates.md",
    "community/guidelines/remix-boundaries.md",
    "docs/architecture.md",
    "docs/canon-policy.md",
    "docs/contribution-guide.md",
    "docs/research-findings.md",
    "docs/portability-notes.md",
    "docs/validation-report.md",
    "examples/dry-runs.md",
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) != 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md has invalid YAML frontmatter fences", failures)
    else:
        keys = re.findall(r"^([a-z_]+):", frontmatter.group(1), re.MULTILINE)
        if keys != ["name", "description"]:
            fail(f"SKILL.md frontmatter keys must be name, description; got {keys}", failures)
        if "name: yuki-community-engine" not in frontmatter.group(0):
            fail("SKILL.md name is incorrect", failures)

    modes = (ROOT / "engine/modes/modes.md").read_text(encoding="utf-8")
    for mode in [
        "CHARACTER",
        "STILL",
        "SCENE",
        "CLASSIC CINEMATIC",
        "MEME",
        "COMMERCIAL",
        "EPISODE",
    ]:
        if f"## {mode}" not in modes:
            fail(f"missing engine mode: {mode}", failures)

    for beat in [
        "Hook + Setup",
        "Escalation / Development",
        "Major Development / Turn",
        "Payoff / Resolution",
    ]:
        if beat not in modes:
            fail(f"missing episode beat: {beat}", failures)
    if "only for" not in modes or "structural justification" not in modes:
        fail("optional fifth-board guardrail is missing", failures)

    canon = (ROOT / "canon/character/yuki-canon.md").read_text(encoding="utf-8")
    for anchor in ["cyan", "three-feather", "blue-gray eyes", "oversized", "Tier 1"]:
        if anchor.casefold() not in canon.casefold():
            fail(f"canon anchor absent: {anchor}", failures)

    source_register = (ROOT / "canon/references/source-register.md").read_text(
        encoding="utf-8"
    )
    for tier in range(1, 6):
        if f"Tier {tier}" not in source_register and tier > 3:
            policy = (ROOT / "docs/canon-policy.md").read_text(encoding="utf-8")
            if f"Tier {tier}" not in policy:
                fail(f"reference hierarchy missing Tier {tier}", failures)

    dry_runs = (ROOT / "examples/dry-runs.md").read_text(encoding="utf-8")
    test_count = len(re.findall(r"^## \d+\.", dry_runs, re.MULTILINE))
    if test_count < 8:
        fail(f"expected at least 8 dry-runs, found {test_count}", failures)

    try:
        width, height = png_dimensions(ROOT / "assets/canon/yuki-turnaround.png")
        if (width, height) != (1491, 1055):
            fail(f"unexpected canonical image dimensions: {width}x{height}", failures)
    except ValueError as exc:
        fail(f"canonical asset invalid: {exc}", failures)

    license_files = [
        path.name
        for path in ROOT.iterdir()
        if path.is_file() and path.name.casefold().startswith("license")
    ]
    if license_files:
        fail(f"public license file present without approval: {license_files}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    print(f"PASS: {len(REQUIRED)} required files present")
    print("PASS: SKILL.md frontmatter and engine modes valid")
    print("PASS: four-board episode structure and fifth-board guardrail present")
    print(f"PASS: {test_count} textual dry-runs present")
    print(f"PASS: canonical PNG is {width}x{height}")
    print("PASS: no public license included")
    return 0


if __name__ == "__main__":
    sys.exit(main())

