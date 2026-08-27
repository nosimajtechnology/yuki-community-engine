#!/usr/bin/env python3
"""Instruction-level regression checks for v1.1 reference grounding."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skill" / "yuki-community-engine"


def require(path: Path, *phrases: str) -> None:
    text = " ".join(path.read_text(encoding="utf-8").lower().split())
    missing = [
        phrase
        for phrase in phrases
        if " ".join(phrase.lower().split()) not in text
    ]
    if missing:
        raise AssertionError(f"{path.relative_to(ROOT)} missing: {missing}")


def main() -> None:
    grounding = SKILL / "references" / "rendering-grounding.md"
    require(
        SKILL / "SKILL.md",
        "rendering-grounding.md",
        "research and visually inspect",
        "internal fidelity gate",
    )
    require(
        grounding,
        "Do not trigger it merely because",
        "explicit modern rendering",
        "original-platform gameplay",
        "YUKI CANONICAL TURNAROUND",
        "GAMEPLAY REFERENCE A",
        "modern PBR",
        "Two or more failures",
        "one automatic narrow repair",
        "Do not bundle, redistribute, trace, or reproduce",
    )
    require(
        SKILL / "references" / "workflows.md",
        "STILL, SCENE, CLASSIC CINEMATIC, COMMERCIAL, and EPISODE",
        "Do not expand a frame that fails",
        "Re-run the gate on each board",
    )
    require(
        SKILL / "references" / "continuity.md",
        "selected rendering-reference set",
        "later panels do not gain polygons",
        "rendering-era drift",
    )
    require(
        SKILL / "references" / "model-adapters.md",
        "gameplay-reference assignments",
        "screenshot-derived rendering contract",
        "volumetric atmosphere",
    )
    require(
        ROOT / "examples" / "reference-grounding-regressions.md",
        "Ruined-city PS2 failure case",
        "Named-game fidelity",
        "Y2K but not PS2",
        "Modern rendering override",
        "Storyboard continuity",
    )
    print("OK   reference-grounding instruction regressions A-E")


if __name__ == "__main__":
    main()
