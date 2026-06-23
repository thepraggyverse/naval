#!/usr/bin/env python3
"""Smoke-check Naval source, direct-copy, and optional local Codex install."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 79
DEFAULT_HOMES = [
    "~/.agents/skills",
    "~/.codex/skills",
    "~/.claude/skills",
    "~/.copilot/skills",
    "~/.cursor/skills",
    "~/.gemini/skills",
    "~/.config/opencode/skills",
    "~/.openclaw/skills",
    "~/.openclaw/acpx/codex-home/skills",
]


def fail(message: str) -> None:
    print(f"smoke failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if check and result.returncode != 0:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        fail("command failed: " + " ".join(cmd))
    return result


def check_source() -> None:
    skills = sorted((ROOT / "skills").glob("n-*"))
    if len(skills) != EXPECTED_SKILLS:
        fail(f"expected {EXPECTED_SKILLS} source skills, found {len(skills)}")
    for name in ["n-router", "n-setup", "n-save-learning", "n-memory-refresh"]:
        if not (ROOT / "skills" / name / "SKILL.md").exists():
            fail(f"missing {name}")
    for rel in [
        "references/memory/README.md",
        "references/memory/templates/learning.md",
        "references/memory/schemas/learning.yaml",
        "docs/skills/README.md",
        "docs/RELEASE.md",
    ]:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")
    print(f"source smoke passed: {len(skills)} skills")


def check_direct_copy(agent_root: Path | None) -> None:
    if agent_root:
        root = agent_root.expanduser()
    else:
        root = ROOT / "dist" / "naval-direct-install"
        run(["npm", "run", "export:direct"])
    run(["python3", "scripts/validate_direct_install.py", "--agent-root", str(root)])
    print(f"direct-copy smoke passed: {root}")


def check_codex_plugin() -> None:
    codex = run(["bash", "-lc", "command -v codex"], check=False)
    if codex.returncode != 0:
        fail("codex CLI not found")
    listing = run(["codex", "plugin", "list"])
    cache_lines = [
        line.strip() for line in listing.stdout.splitlines()
        if line.strip().startswith("naval@personal")
    ]
    if not cache_lines:
        fail("naval@personal is not listed by Codex")
    naval_line = cache_lines[0]
    if "installed, enabled" not in naval_line:
        fail("naval@personal is not installed and enabled")
    print("codex plugin smoke passed: " + naval_line)


def check_skill_homes(homes: list[str]) -> None:
    for home_text in homes:
        home = Path(home_text).expanduser()
        if not home.exists():
            fail(f"skill home missing: {home}")
        skills = sorted(home.glob("n-*"))
        if len(skills) != EXPECTED_SKILLS:
            fail(f"{home} has {len(skills)} n-* skills, expected {EXPECTED_SKILLS}")
        if not (home / "n-setup").exists():
            fail(f"{home} missing n-setup")
    print(f"skill-home smoke passed: {len(homes)} homes")


def check_live() -> None:
    prompt = (
        "Use $n-setup. Do not write files. In two concise bullets, name the "
        "local config file it manages and the default project-local memory root."
    )
    result = run(["codex", "exec", "--ephemeral", "--sandbox", "read-only", "-C", str(ROOT), prompt])
    if ".naval/config.local.yaml" not in result.stdout or "docs/naval" not in result.stdout:
        fail("live Codex output did not mention expected n-setup paths")
    print("live Codex smoke passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--direct-root", type=Path, help="Existing direct-copy root to validate.")
    parser.add_argument("--codex", action="store_true", help="Require naval@personal to be installed and enabled in Codex.")
    parser.add_argument("--skill-homes", action="store_true", help="Check default direct skill homes.")
    parser.add_argument("--live", action="store_true", help="Run a live read-only Codex n-setup invocation.")
    args = parser.parse_args()

    check_source()
    check_direct_copy(args.direct_root)
    if args.codex or args.live:
        check_codex_plugin()
    if args.skill_homes:
        check_skill_homes(DEFAULT_HOMES)
    if args.live:
        check_live()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
