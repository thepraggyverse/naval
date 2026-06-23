# Release

Use this checklist before tagging or publishing a public Naval release.

## Preflight

```bash
git status --short
python3 scripts/generate_skill_docs.py
npm run validate
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
python3 scripts/smoke_install.py
python3 -m py_compile scripts/*.py
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Optional local install smoke:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add naval@personal --json
python3 scripts/smoke_install.py --codex --skill-homes
python3 scripts/smoke_install.py --codex --live
```

Structured review:

```bash
autoreview --mode local
```

## Commit And Tag

```bash
git add -A
git commit -m "Prepare Naval v0.1.0 release"
git push origin main
git tag -a v0.1.0 -m "Naval v0.1.0"
git push origin v0.1.0
```

## Verify GitHub

```bash
gh run list --repo thepraggyverse/naval --limit 5
gh release view v0.1.0 --repo thepraggyverse/naval
```

Create the release if it does not exist:

```bash
gh release create v0.1.0 \
  --repo thepraggyverse/naval \
  --title "Naval v0.1.0" \
  --notes "Initial public release of the unofficial Naval skill pack with 79 n-prefixed skills, optional memory, direct-copy export, and multi-harness install docs."
```
