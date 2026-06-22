#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skills_dir = root / "skills"
matrix = root / "references" / "coverage-matrix.yaml"
text = matrix.read_text(encoding="utf-8")
book_sections = text.split("\nall_skills:", 1)[0]

actual = {p.name for p in skills_dir.iterdir() if (p / "SKILL.md").exists()}
listed = set(re.findall(r"\b[n]-[a-z0-9-]+\b", text))
mapped = set(re.findall(r"\b[n]-[a-z0-9-]+\b", book_sections))

missing_dirs = sorted(listed - actual)
unmapped = sorted(actual - mapped)
bad_prefix = sorted(name for name in actual if not name.startswith("n-"))
missing_links = []
missing_metadata = []
todo_files = []

for skill_dir in sorted(skills_dir.iterdir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        continue
    if not (skill_dir / "agents" / "openai.yaml").exists():
        missing_metadata.append(skill_dir.name)
    skill_text = skill_md.read_text(encoding="utf-8")
    if "TODO" in skill_text:
        todo_files.append(str(skill_md.relative_to(root)))
    for ref in re.findall(r"`(\.\./\.\./references/[^`]+)`", skill_text):
        target = (skill_dir / ref).resolve()
        if not target.exists():
            missing_links.append(f"{skill_dir.name}: {ref}")

for ref_file in sorted((root / "references").rglob("*")):
    if ref_file.is_file() and "TODO" in ref_file.read_text(encoding="utf-8", errors="ignore"):
        todo_files.append(str(ref_file.relative_to(root)))

if missing_dirs or unmapped or bad_prefix or missing_links or missing_metadata or todo_files:
    print("Coverage check failed")
    if missing_dirs:
        print("Missing skill directories:", ", ".join(missing_dirs))
    if unmapped:
        print("Skill directories not in coverage matrix:", ", ".join(unmapped))
    if bad_prefix:
        print("Skills without n- prefix:", ", ".join(bad_prefix))
    if missing_metadata:
        print("Skills without agents/openai.yaml:", ", ".join(missing_metadata))
    if missing_links:
        print("Missing reference links:")
        for link in missing_links:
            print(" -", link)
    if todo_files:
        print("TODO markers found:")
        for file in todo_files:
            print(" -", file)
    sys.exit(1)

print(f"Coverage check passed: {len(actual)} n-prefixed skills mapped with valid references.")
