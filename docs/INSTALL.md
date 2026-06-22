# Install

This document covers installing `naval` as a local Codex plugin and, optionally, exposing every `n-*` skill through local agent skill homes.

For Claude Code, Cursor, Copilot, Gemini CLI, OpenCode, Pi, Kiro, Qwen, Droid, and other harness-specific paths, see [HARNESS_SUPPORT.md](HARNESS_SUPPORT.md).

## Requirements

| Requirement | Why |
|---|---|
| macOS or Linux shell | The installer is a Python script that manages local files and symlinks. |
| Python 3.10 or newer | Required for `scripts/install_local.py` and validation scripts. |
| Git | Used to clone or update the repository. |
| Codex Desktop or a compatible local agent | Needed to use the plugin or discover `SKILL.md` folders. |
| Optional GitHub CLI | Helpful if you want to fork, publish, or inspect CI from the terminal. |

## Recommended Layout

The default installer assumes this layout:

```text
~/
  plugins/
    naval/
  .agents/
    plugins/
      marketplace.json
```

Clone into that location:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/naval.git ~/plugins/naval
cd ~/plugins/naval
```

## Install Options

| Option | Command | Result |
|---|---|---|
| Codex plugin only | `python3 scripts/install_local.py --marketplace` | Adds `naval` to `~/.agents/plugins/marketplace.json`. |
| Direct skills only | `python3 scripts/install_local.py --symlink-skills` | Symlinks every `skills/n-*` folder into default skill homes. |
| Plugin plus skills | `python3 scripts/install_local.py --marketplace --symlink-skills` | Gives Codex plugin visibility and direct skill-folder discovery. |
| Preview changes | `python3 scripts/install_local.py --marketplace --symlink-skills --dry-run` | Prints intended writes without changing files. |

The combo path is best for a multi-agent local setup: one repo remains the source of truth, while Codex and skill-scanning tools can both see the same `n-*` skills.

## Option 1: Install As A Codex Plugin

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

Restart or refresh Codex, then search for **Naval** or `n-`.

## Option 2: Symlink Skills Directly

Some tools do not load Codex plugins directly, but they can discover folders that contain `SKILL.md`.

Symlink every `n-*` skill into supported homes:

```bash
python3 scripts/install_local.py --symlink-skills
```

By default this targets:

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

Example result:

```text
~/.codex/skills/n-specific-knowledge -> ~/plugins/naval/skills/n-specific-knowledge
```

## Option 3: Marketplace Plus Symlinks

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
```

Use this when you want both:

| Need | Covered By |
|---|---|
| Codex plugin marketplace visibility | `--marketplace` |
| Direct `SKILL.md` discovery in local agent homes | `--symlink-skills` |
| One source repo for updates | both together |

## Custom Marketplace Path

Use this only when you intentionally manage a non-default local marketplace file:

```bash
python3 scripts/install_local.py \
  --marketplace \
  --marketplace-path /path/to/marketplace.json
```

For the default path, you do not need to run a separate marketplace-add command. The default personal marketplace file is:

```text
~/.agents/plugins/marketplace.json
```

## Custom Skill Homes

Install into one skill home:

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills
```

Install into multiple homes:

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills \
  --skill-home ~/.agents/skills
```

## Collision Policy

| Existing Destination | Default Behavior | With `--force` |
|---|---|---|
| Missing | Create symlink. | Create symlink. |
| Already points to this repo | Leave unchanged. | Leave unchanged. |
| Points somewhere else | Skip and print the path. | Replace it. |
| Plain file or directory | Skip and print the path. | Remove and replace it. |

Run a dry run first when replacing existing skill names:

```bash
python3 scripts/install_local.py --symlink-skills --force --dry-run
```

## Validate After Install

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

Expected output includes:

```text
Public validation passed: 76 n-prefixed skills
Coverage check passed: 76 n-prefixed skills mapped with valid references.
```

If you have Codex's local validation helpers installed:

```bash
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py ~/plugins/naval
for d in ~/plugins/naval/skills/n-*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
```

## Updating

```bash
cd ~/plugins/naval
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

If a local agent caches plugin versions, update the cachebuster in `.codex-plugin/plugin.json` with Codex's plugin helper during development, then reinstall or start a fresh thread so the agent reloads skills.

Harness-managed installs should use that host's own update flow. See [HARNESS_SUPPORT.md](HARNESS_SUPPORT.md#updating-local-installs) for details.

## Troubleshooting

| Symptom | Check |
|---|---|
| `naval` is not visible in Codex | Confirm `~/.agents/plugins/marketplace.json` contains a `naval` entry and restart Codex. |
| `n-*` skills are missing | Run `python3 scripts/install_local.py --symlink-skills --dry-run` to see target homes. |
| A symlink was skipped | A file, folder, or different symlink already exists at that skill name. Re-run with `--force` only if you intend to replace it. |
| Skill output feels too broad | Start with a specific skill such as `n-specific-knowledge`, `n-desire-audit`, or `n-opportunity-scorecard` instead of `n-router`. |
| You need exact quote wording | Use `n-quote-safety` and verify against an authorized source. |
