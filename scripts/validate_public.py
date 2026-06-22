#!/usr/bin/env python3
"""Validate the public Naval plugin repository without private Codex helpers."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{path} is not UTF-8 text")


def validate_plugin_json() -> None:
    path = ROOT / ".codex-plugin" / "plugin.json"
    if not path.exists():
        fail("missing .codex-plugin/plugin.json")
    data = json.loads(read_text(path))
    if data.get("name") != "naval":
        fail("plugin name must be naval")
    if data.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")
    interface = data.get("interface")
    if not isinstance(interface, dict):
        fail("plugin interface must be an object")
    for key in ["displayName", "shortDescription", "longDescription"]:
        if not interface.get(key):
            fail(f"plugin interface missing {key}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("skill frontmatter missing")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        frontmatter[key.strip()] = value
    return frontmatter


def validate_skills() -> int:
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        fail("missing skills directory")
    count = 0
    for skill_dir in sorted(skills_dir.glob("n-*")):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            fail(f"{skill_dir.name} missing SKILL.md")
        text = read_text(skill_md)
        fm = parse_frontmatter(text)
        if fm.get("name") != skill_dir.name:
            fail(f"{skill_dir.name} frontmatter name mismatch")
        if not fm.get("description"):
            fail(f"{skill_dir.name} missing description")
        if "TODO" in text:
            fail(f"{skill_dir.name} contains TODO")
        if not (skill_dir / "agents" / "openai.yaml").exists():
            fail(f"{skill_dir.name} missing agents/openai.yaml")
        for ref in re.findall(r"`(\.\./\.\./references/[^`]+)`", text):
            target = (skill_dir / ref).resolve()
            if not target.exists():
                fail(f"{skill_dir.name} references missing file {ref}")
        count += 1
    if count != 76:
        fail(f"expected 76 n-* skills, found {count}")
    return count


def validate_references() -> None:
    required = [
        "book-map.md",
        "coverage-matrix.yaml",
        "skill-catalog.md",
        "router-guide.md",
        "concept-graph.json",
    ]
    for rel in required:
        path = ROOT / "references" / rel
        if not path.exists():
            fail(f"missing references/{rel}")
    json.loads(read_text(ROOT / "references" / "concept-graph.json"))


def validate_docs() -> None:
    required = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "docs/EXAMPLES.md",
        "docs/INSTALL.md",
        "docs/PLUGIN_REFERENCE.md",
        "docs/SYMLINKS.md",
        "docs/DEVELOPMENT.md",
        "docs/SOURCE_BOUNDARIES.md",
        ".github/workflows/validate.yml",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")


def main() -> int:
    validate_plugin_json()
    skill_count = validate_skills()
    validate_references()
    validate_docs()
    print(f"Public validation passed: {skill_count} n-prefixed skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
