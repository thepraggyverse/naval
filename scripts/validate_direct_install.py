#!/usr/bin/env python3
"""Validate the documented direct-copy skill install layout.

Direct-copy installs must copy `skills/n-*` under an agent root's `skills/`
folder and copy or symlink this repo's `references/` folder beside that
`skills/` folder. This preserves generated `../../references/...` links.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REF_PATTERN = re.compile(r"`(\.\./\.\./references/[^`]+)`")


def fail(message: str) -> None:
    print(f"direct install validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def refs_for(skill_md: Path) -> list[str]:
    return REF_PATTERN.findall(skill_md.read_text(encoding="utf-8"))


def copy_skill_tree(source: Path, dest: Path) -> None:
    shutil.copytree(
        source,
        dest,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )


def source_skills() -> list[Path]:
    return sorted((ROOT / "skills").glob("n-*"))


def validate_layout(agent_root: Path, required_skill_names: set[str]) -> None:
    skills_root = agent_root / "skills"
    refs_root = agent_root / "references"
    if not skills_root.exists():
        fail(f"{agent_root} missing skills/ folder")
    if not refs_root.exists():
        fail(f"{agent_root} missing references/ folder")

    copied_skill_names = {path.name for path in skills_root.glob("n-*")}
    missing = required_skill_names - copied_skill_names
    if missing:
        fail(f"{agent_root} missing copied skills: {', '.join(sorted(missing))}")

    for skill_dir in sorted(skills_root.glob("n-*")):
        if skill_dir.name not in required_skill_names:
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            fail(f"{skill_dir.name} missing SKILL.md in copied layout")
        for ref in refs_for(skill_md):
            target = (skill_dir / ref).resolve()
            if not target.exists():
                fail(f"{skill_dir.name} reference does not resolve in copied layout: {ref}")


def validate_agent_root(agent_root: Path) -> int:
    required = source_skills()
    if not required:
        fail("no source skills found")
    validate_layout(agent_root.expanduser().resolve(), {path.name for path in required})
    return len(required)


def validate_simulated_layout() -> int:
    source = source_skills()
    if not source:
        fail("no source skills found")
    if not (ROOT / "references").exists():
        fail("source references folder missing")

    with tempfile.TemporaryDirectory(prefix="naval-direct-install-") as temp:
        agent_root = Path(temp) / "agent-root"
        copied_skills = agent_root / "skills"
        copied_refs = agent_root / "references"
        copied_skills.mkdir(parents=True)
        shutil.copytree(ROOT / "references", copied_refs)
        for skill in source:
            copy_skill_tree(skill, copied_skills / skill.name)
        validate_layout(agent_root, {path.name for path in source})
    return len(source)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--agent-root",
        type=Path,
        help="Existing direct-copy root containing sibling skills/ and references/ folders.",
    )
    args = parser.parse_args()

    if args.agent_root:
        count = validate_agent_root(args.agent_root)
        print(f"Direct install validation passed: {count} skills with sibling references in {args.agent_root}.")
    else:
        count = validate_simulated_layout()
        print(f"Direct install validation passed: {count} skills with sibling references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
