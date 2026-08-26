#!/usr/bin/env python3
"""Validate and build dist/yuki-community-engine.zip."""

import hashlib
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skill" / "yuki-community-engine"
DIST = ROOT / "dist"
ZIP_NAME = "yuki-community-engine.zip"
MAX_FILES = 500
MAX_UNCOMPRESSED_BYTES = 25 * 1024 * 1024
MAX_ZIP_BYTES = 50 * 1024 * 1024
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


def validate() -> list[Path]:
    if not SKILL_DIR.is_dir():
        fail(f"missing {SKILL_DIR.relative_to(ROOT)}")

    files = sorted(path for path in SKILL_DIR.rglob("*") if path.is_file())
    if not files:
        fail("skill folder is empty")
    if len(files) > MAX_FILES:
        fail(f"{len(files)} files; maximum is {MAX_FILES}")

    manifests = [path for path in files if path.name.lower() == "skill.md"]
    if len(manifests) != 1 or manifests[0].parent != SKILL_DIR:
        fail("expected exactly one top-level SKILL.md")

    text = manifests[0].read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not front:
        fail("SKILL.md has no YAML frontmatter")

    fields = {
        line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
        for line in front.group(1).splitlines()
        if ":" in line
    }
    if set(fields) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description")
    if fields["name"] != "yuki-community-engine":
        fail("SKILL.md name must be yuki-community-engine")

    total = sum(path.stat().st_size for path in files)
    if total > MAX_UNCOMPRESSED_BYTES:
        fail(f"{total} uncompressed bytes; maximum is {MAX_UNCOMPRESSED_BYTES}")

    for path in files:
        if path.suffix.lower() != ".md":
            continue
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target):
                continue
            if not (path.parent / target).exists():
                fail(f"{path.relative_to(ROOT)} links to missing '{target}'")

    print(f"OK   {len(files)} files, {total} bytes")
    return files


def build(files: list[Path]) -> None:
    DIST.mkdir(exist_ok=True)
    output = DIST / ZIP_NAME

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            arcname = f"{SKILL_DIR.name}/{path.relative_to(SKILL_DIR).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())

    with zipfile.ZipFile(output) as archive:
        top_levels = {name.split("/", 1)[0] for name in archive.namelist()}
        if top_levels != {SKILL_DIR.name}:
            fail(f"unexpected ZIP roots: {sorted(top_levels)}")
        if archive.testzip() is not None:
            fail("ZIP integrity check failed")

    if output.stat().st_size > MAX_ZIP_BYTES:
        fail(f"ZIP is larger than {MAX_ZIP_BYTES} bytes")

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    (DIST / "SHA256SUMS").write_text(
        f"{digest}  {ZIP_NAME}\n", encoding="utf-8"
    )
    print(f"OK   {output.relative_to(ROOT)} ({output.stat().st_size} bytes)")
    print(f"OK   sha256 {digest}")


if __name__ == "__main__":
    validated = validate()
    if "--check" not in sys.argv:
        build(validated)
