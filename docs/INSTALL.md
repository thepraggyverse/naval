# Install

This document covers installing `naval` as a local Codex plugin and, optionally, exposing every `n-*` skill through local agent skill homes.

## Requirements

- macOS or Linux shell.
- Python 3.10 or newer.
- Codex Desktop or another agent that can load `SKILL.md` skill folders.
- Optional: GitHub CLI if you want to fork or publish your own copy.

## Option 1: Install As A Codex Plugin

Clone the repo into the conventional local plugin directory:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/naval.git ~/plugins/naval
cd ~/plugins/naval
```

Register the plugin in the default personal marketplace:

```bash
python3 scripts/install_local.py --marketplace
```

This updates:

```text
~/.agents/plugins/marketplace.json
```

It adds an entry like:

```json
{
  "name": "naval",
  "source": {
    "source": "local",
    "path": "./plugins/naval"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Restart or refresh Codex, then search for the **Naval** plugin.

## Option 2: Symlink Skills Directly

Some local setups expose skills from multiple homes. To symlink every `n-*` skill into supported homes:

```bash
python3 scripts/install_local.py --symlink-skills
```

By default this targets:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

The script creates missing home directories and skips existing skill names unless `--force` is passed.

## Option 3: Marketplace Plus Symlinks

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
```

Use this when you want both:

- Codex plugin marketplace visibility.
- Direct skill exposure for tools that scan skill folders.

## Custom Marketplace Path

```bash
python3 scripts/install_local.py \
  --marketplace \
  --marketplace-path /path/to/marketplace.json
```

## Custom Skill Homes

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills \
  --skill-home ~/.agents/skills
```

## Validate After Install

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

Expected output includes:

```text
Public validation passed
Coverage check passed: 76 n-prefixed skills mapped with valid references.
```

## Updating

```bash
cd ~/plugins/naval
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
python3 scripts/validate_public.py
```

If you already have a skill with the same name and intentionally want this repo to replace the symlink:

```bash
python3 scripts/install_local.py --symlink-skills --force
```
