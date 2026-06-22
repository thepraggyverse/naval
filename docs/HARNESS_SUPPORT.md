# Harness Support

`naval` is distributed two ways:

1. Native plugin or extension metadata for harnesses that can install a package.
2. Direct `SKILL.md` symlinks or copies for harnesses that scan skill folders.

The skills themselves are plain `SKILL.md` folders under `skills/n-*`, so the fallback path works broadly even when native plugin support varies by host.

## Support Matrix

| Harness | Native Metadata | Recommended Install | Update |
|---|---|---|---|
| Codex App | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Local marketplace or custom marketplace source. | Pull repo, rerun installer, restart or start a new thread. |
| Codex CLI | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | `codex plugin marketplace add thepraggyverse/naval`, then install in `/plugins`. | Reopen `/plugins` after marketplace refresh, or rerun local installer. |
| Claude Code | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | `/plugin marketplace add thepraggyverse/naval`, then `/plugin install naval`. | `/plugin marketplace update naval`, then `/plugin update naval`. |
| Cursor | `.cursor-plugin/plugin.json`, `.cursor-plugin/marketplace.json` | Install from source if available, or use direct skills in `.cursor/skills` or `~/.cursor/skills`. | Pull or reinstall the source plugin; restart Cursor. |
| GitHub Copilot | Claude-compatible plugin metadata plus direct skills. | Install plugin from source in VS Code, or use Copilot CLI plugin commands. | Reinstall/update plugin source; restart the agent session. |
| Factory Droid | Claude-compatible plugin metadata. | `droid plugin marketplace add https://github.com/thepraggyverse/naval`, then `droid plugin install naval@naval`. | Use the host's plugin update flow or reinstall. |
| Qwen Code | Claude-compatible plugin metadata. | `qwen extensions install thepraggyverse/naval:naval`. | Use the host's extension update flow or reinstall. |
| Gemini CLI | `gemini-extension.json`, `GEMINI.md`, `skills/`. | `gemini extensions install https://github.com/thepraggyverse/naval`. | `gemini extensions update naval`, then restart Gemini. |
| OpenCode | `package.json`, `.opencode/plugins/naval.js`, `.opencode/INSTALL.md`. | Add `naval@git+https://github.com/thepraggyverse/naval.git` to `opencode.json`. | Pull/restart for local path, or update pinned git ref. |
| Pi | `package.json`, `.pi/extensions/naval.ts`. | `pi install git:github.com/thepraggyverse/naval`. | Use Pi's package update or reinstall flow. |
| Kiro | Direct `SKILL.md` folders. | Copy or symlink `skills/n-*` into `.kiro/skills/`. | Pull repo and refresh copied/symlinked skills. |
| OpenClaw | Direct `SKILL.md` folders. | `python3 scripts/install_local.py --symlink-skills`. | Pull repo and rerun symlink installer. |
| skills.sh-style browsers | `skills.sh.json`. | Use the skills.sh-compatible add flow for `thepraggyverse/naval`. | Re-run the installer or refresh the source. |

## Codex App

For the local checkout path:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/naval.git ~/plugins/naval
cd ~/plugins/naval
python3 scripts/install_local.py --marketplace
```

Restart Codex, open Plugins, and install **Unofficial Naval Skills**.

For a custom marketplace source in the Codex app:

| Field | Value |
|---|---|
| Source | `thepraggyverse/naval` |
| Git ref | `main` |
| Sparse paths | leave blank |

## Codex CLI

Register the marketplace:

```bash
codex plugin marketplace add thepraggyverse/naval
```

Launch `codex`, open `/plugins`, choose the Naval marketplace, install `naval`, then restart or start a new thread.

For a non-default profile, keep every step on the same `CODEX_HOME`:

```bash
CODEX_HOME="$HOME/.codex/profiles/work" codex plugin marketplace add thepraggyverse/naval
CODEX_HOME="$HOME/.codex/profiles/work" codex
```

## Claude Code

Inside Claude Code:

```text
/plugin marketplace add thepraggyverse/naval
/plugin install naval
```

Update later with:

```text
/plugin marketplace update naval
/plugin update naval
```

## Cursor

This repository includes Cursor plugin metadata. If your Cursor build supports installing a plugin from source, use:

```text
thepraggyverse/naval
```

If source plugin install is unavailable, use direct skills:

```bash
cd ~/plugins/naval
python3 scripts/install_local.py --symlink-skills --skill-home ~/.cursor/skills
```

Restart Cursor after installing or refreshing skills.

## GitHub Copilot

For VS Code Copilot Agent Plugins:

1. Run `Chat: Install Plugin from Source` from the VS Code command palette.
2. Use `thepraggyverse/naval`.
3. Select `naval` if prompted.

For Copilot CLI:

```text
/plugin marketplace add thepraggyverse/naval
/plugin install naval@naval
```

Or from a shell:

```bash
copilot plugin marketplace add thepraggyverse/naval
copilot plugin install naval@naval
```

Direct skills fallback:

```bash
python3 scripts/install_local.py --symlink-skills --skill-home ~/.copilot/skills
```

## Factory Droid

```bash
droid plugin marketplace add https://github.com/thepraggyverse/naval
droid plugin install naval@naval
```

## Qwen Code

```bash
qwen extensions install thepraggyverse/naval:naval
```

## Gemini CLI

Install from GitHub:

```bash
gemini extensions install https://github.com/thepraggyverse/naval
```

Update later:

```bash
gemini extensions update naval
```

Local development:

```bash
gemini extensions link /path/to/naval
```

Restart Gemini after install, update, or link changes.

## OpenCode

Add Naval to your global or project `opencode.json`:

```json
{
  "plugin": ["naval@git+https://github.com/thepraggyverse/naval.git"]
}
```

For a local checkout:

```json
{
  "plugin": ["/path/to/naval"]
}
```

Restart OpenCode after editing `opencode.json`.

## Pi

```bash
pi install git:github.com/thepraggyverse/naval
```

Local development:

```bash
pi -e /path/to/naval
```

## Direct Skill Fallback

Use this for Kiro, OpenClaw, project-local installs, or any host that loads `SKILL.md` folders.

```bash
cd ~/plugins/naval
python3 scripts/install_local.py --symlink-skills
```

Install into a specific project or harness home:

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home /path/to/project/.kiro/skills
```

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home /path/to/project/.agents/skills
```

## Updating Local Installs

For local checkout installs:

```bash
cd ~/plugins/naval
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

If a host caches plugin definitions, restart the app or start a fresh thread/session after updating.

## Collision Handling

The symlink installer is conservative:

| Destination State | Default | With `--force` |
|---|---|---|
| Missing | Create symlink. | Create symlink. |
| Already points to this repo | Leave unchanged. | Leave unchanged. |
| Existing different symlink | Skip. | Replace. |
| Existing file or directory | Skip. | Remove and replace. |

Preview changes first:

```bash
python3 scripts/install_local.py --symlink-skills --dry-run
```
