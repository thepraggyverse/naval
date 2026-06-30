#!/usr/bin/env python3
"""Audit Naval skills for predictable invocation and maintainable bodies."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MAX_DESCRIPTION_CHARS = 220
EXPECTED_SKILLS = 79
REQUIRED_HEADINGS = ["## Read First", "## Output"]
OUTPUT_ACTIONS = {
    "decision",
    "scorecard",
    "experiment",
    "practice",
    "reading path",
    "boundary",
    "removal",
    "saved files",
    "skipped reason",
    "recommended action",
    "next skills",
    "applied changes",
    "recommended changes",
    "refresh report",
    "next cleanup target",
}


def fail(message: str) -> None:
    print(f"skill quality audit failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str, skill_name: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{skill_name} missing frontmatter")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"{skill_name} invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        frontmatter[key.strip()] = value
    return frontmatter


def audit_description(skill_name: str, description: str) -> list[str]:
    issues: list[str] = []
    if len(description) > MAX_DESCRIPTION_CHARS:
        issues.append(f"description too long: {len(description)} chars")
    if not description.startswith("Naval "):
        issues.append("description should front-load the Naval leading word")
    if "Trigger" not in description:
        issues.append("description should include a concrete Trigger clause")
    if "Use when" in description:
        issues.append("description should use one sharp Trigger clause, not broad Use when prose")
    if "wants this Naval lens" in description:
        issues.append("description repeats the generic Naval lens branch")
    if re.search(r"\b(and|or|with|for|to|of|from|using|while|before)\.", description):
        issues.append("description appears truncated into an incomplete clause")
    if re.search(r",\s*(and|or)\.", description):
        issues.append("description appears truncated after a list conjunction")
    if skill_name not in description and skill_name not in {"n-setup", "n-save-learning", "n-memory-refresh"}:
        issues.append("description should include the explicit n-* name for user invocation")
    return issues


def audit_body(skill_dir: Path, text: str) -> list[str]:
    issues: list[str] = []
    name = skill_dir.name
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            issues.append(f"missing {heading}")
    if "## Workflow" not in text:
        issues.append("missing ## Workflow")
    if "If these reference paths are unavailable" not in text and "If these files are unavailable" not in text:
        issues.append("missing direct-copy reference fallback")
    if "TODO" in text:
        issues.append("contains TODO")
    output = text.split("## Output", 1)[1] if "## Output" in text else ""
    lowered_output = output.lower()
    if not any(action in lowered_output for action in OUTPUT_ACTIONS):
        issues.append("output section lacks a checkable action artifact")
    for ref in re.findall(r"`(\.\./\.\./references/[^`]+)`", text):
        target = (skill_dir / ref).resolve()
        if not target.exists():
            issues.append(f"broken reference pointer: {ref}")
    if name != "n-router" and "n-router" in text.split("## Read First", 1)[0]:
        issues.append("mentions n-router before routing context")
    return issues


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS.glob("n-*") if (path / "SKILL.md").exists())
    if len(skill_dirs) != EXPECTED_SKILLS:
        fail(f"expected {EXPECTED_SKILLS} skills, found {len(skill_dirs)}")

    all_issues: dict[str, list[str]] = {}
    descriptions: dict[str, str] = {}
    for skill_dir in skill_dirs:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text, skill_dir.name)
        description = frontmatter.get("description", "")
        if not description:
            all_issues.setdefault(skill_dir.name, []).append("missing description")
        else:
            all_issues.setdefault(skill_dir.name, []).extend(audit_description(skill_dir.name, description))
            descriptions[skill_dir.name] = description
        all_issues.setdefault(skill_dir.name, []).extend(audit_body(skill_dir, text))

    duplicate_descriptions = {
        description
        for description in descriptions.values()
        if list(descriptions.values()).count(description) > 1
    }
    if duplicate_descriptions:
        for name, description in descriptions.items():
            if description in duplicate_descriptions:
                all_issues.setdefault(name, []).append("description duplicates another skill")

    all_issues = {name: issues for name, issues in all_issues.items() if issues}
    if all_issues:
        print("Skill quality issues:")
        for name, issues in all_issues.items():
            print(f"- {name}")
            for issue in issues:
                print(f"  - {issue}")
        return 1

    print(f"Skill quality audit passed: {len(skill_dirs)} skills with lean descriptions and checkable outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
