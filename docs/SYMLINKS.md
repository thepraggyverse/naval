# Symlinks

This plugin can be used two ways:

1. As a Codex plugin through `.codex-plugin/plugin.json`.
2. As plain skill folders by symlinking `skills/n-*` into agent skill homes.

Symlinks are useful when a tool does not load Codex plugins directly but can discover `SKILL.md` folders.

## Default Skill Homes

`scripts/install_local.py --symlink-skills` targets:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.copilot/skills
~/.cursor/skills
~/.gemini/skills
~/.config/opencode/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

This matches a shared-home pattern where `.agents/skills` is often the durable common location, while Codex, Claude, Copilot, Cursor, Gemini, OpenCode, and OpenClaw homes can also see the same skill names.

## What Gets Linked

Every directory under:

```text
skills/n-*
```

is linked into each selected skill home.

Example:

```text
~/.codex/skills/n-specific-knowledge -> ~/plugins/naval/skills/n-specific-knowledge
```

## Collision Policy

The installer is conservative:

- If the destination does not exist, it creates the symlink.
- If the destination already points to the same source, it leaves it alone.
- If the destination exists and points somewhere else, it skips it.
- If you pass `--force`, it replaces existing files, folders, or symlinks at that skill name.

## Dry Run

See what would happen:

```bash
python3 scripts/install_local.py --symlink-skills --dry-run
```

## Single Home Example

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills
```

Project-local Kiro example:

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home /path/to/project/.kiro/skills
```

## Remove Symlinks

This repo does not include a destructive uninstall script. To remove symlinks manually:

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'n-*' -ls
```

Then remove only the symlinks you confirm point into this repo:

```bash
rm ~/.codex/skills/n-specific-knowledge
```

Repeat for the other homes as needed.
