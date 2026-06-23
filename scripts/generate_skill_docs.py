#!/usr/bin/env python3
"""Generate browsable markdown pages for every Naval skill."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references" / "skill-catalog.md"
SKILLS = ROOT / "skills"
OUT = ROOT / "docs" / "skills"


@dataclass(frozen=True)
class Skill:
    name: str
    area: str
    use_when: str
    example: str
    description: str


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise SystemExit("skill frontmatter missing")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        fields[key.strip()] = value
    return fields


def catalog_rows() -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `n-"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4:
            raise SystemExit(f"unexpected catalog row: {line}")
        name = cells[0].strip("`")
        rows.append((name, cells[1], cells[2], cells[3]))
    return rows


def load_skills() -> list[Skill]:
    skills: list[Skill] = []
    for name, area, use_when, example in catalog_rows():
        skill_md = SKILLS / name / "SKILL.md"
        if not skill_md.exists():
            raise SystemExit(f"missing skill file for {name}")
        frontmatter = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        description = frontmatter.get("description", "")
        if frontmatter.get("name") != name:
            raise SystemExit(f"name mismatch for {name}")
        skills.append(Skill(name, area, use_when, example, description))
    if len(skills) != 79:
        raise SystemExit(f"expected 79 skills, found {len(skills)}")
    return skills


def write_index(skills: list[Skill]) -> None:
    by_area: dict[str, list[Skill]] = {}
    for skill in skills:
        by_area.setdefault(skill.area, []).append(skill)

    lines = [
        "# Naval Skill Pages",
        "",
        "Generated browsable pages for every `n-*` skill.",
        "",
        "Regenerate with:",
        "",
        "```bash",
        "python3 scripts/generate_skill_docs.py",
        "```",
        "",
        "## By Area",
        "",
    ]
    for area in sorted(by_area):
        lines.append(f"### {area}")
        lines.append("")
        lines.append("| Skill | Use When |")
        lines.append("|---|---|")
        for skill in by_area[area]:
            lines.append(f"| [`{skill.name}`]({skill.name}.md) | {skill.use_when} |")
        lines.append("")
    (OUT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_skill_page(skill: Skill) -> None:
    source = f"../../skills/{skill.name}/SKILL.md"
    lines = [
        f"# `{skill.name}`",
        "",
        f"**Area:** {skill.area}",
        "",
        f"**Use when:** {skill.use_when}",
        "",
        f"**Example prompt:**",
        "",
        "```text",
        skill.example,
        "```",
        "",
        "## What It Does",
        "",
        skill.description,
        "",
        "## How To Use",
        "",
        f"Ask the agent to use `${skill.name}` or say `{skill.name}` in the prompt. If you are unsure which skill fits, start with `n-router`.",
        "",
        "## Source Files",
        "",
        f"- Skill instructions: [{source}]({source})",
        "- Full catalog: [../../references/skill-catalog.md](../../references/skill-catalog.md)",
        "- Coverage matrix: [../../references/coverage-matrix.yaml](../../references/coverage-matrix.yaml)",
        "",
    ]
    (OUT / f"{skill.name}.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for stale in OUT.glob("n-*.md"):
        stale.unlink()
    skills = load_skills()
    write_index(skills)
    for skill in skills:
        write_skill_page(skill)
    print(f"Generated {len(skills)} skill docs in {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
