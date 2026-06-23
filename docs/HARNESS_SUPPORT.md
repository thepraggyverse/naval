# Harness Support

`naval` is distributed two ways:

1. Native plugin or extension metadata for harnesses that can install a package.
2. Direct `SKILL.md` symlinks or copies for harnesses that scan skill folders.

The skills themselves are plain `SKILL.md` folders under `skills/n-*`, so the fallback path works broadly even when native plugin support varies by host.

For Codex, prefer the native plugin path. Direct symlinks are mainly for hosts that scan `SKILL.md` folders; on machines with very large global skill libraries, broad symlinks can contribute to Codex skill-list budget warnings even though explicit `$n-*` skill invocation still works.

## Support Matrix

| Harness | Native Metadata | Recommended Install | Update |
|---|---|---|---|
| Codex App | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Local marketplace or custom marketplace source. | Pull repo, rerun installer, restart or start a new thread. |
| Codex CLI | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Local checkout: `python3 scripts/install_local.py --marketplace`, then `codex plugin add naval@personal --json`. Remote marketplace: register the repo, then install in `/plugins` if direct CLI install is unavailable. | Pull repo, rerun installer, reinstall or refresh plugin cache, restart or start a new thread. |
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

If you use the Codex CLI against the default personal marketplace, install and enable it directly:

```bash
codex plugin add naval@personal --json
codex plugin list | grep 'naval@personal'
```

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

For local development from `~/plugins/naval`, the default personal marketplace path is simpler:

```bash
cd ~/plugins/naval
python3 scripts/install_local.py --marketplace
codex plugin add naval@personal --json
codex plugin list | grep 'naval@personal'
```

Live smoke test:

```bash
python3 scripts/smoke_install.py --codex --live
```

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

For a large existing agent setup, target only the harness that needs direct skills:

```bash
python3 scripts/install_local.py --symlink-skills --skill-home ~/.cursor/skills
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

Symlinks are preferred because every generated skill can resolve shared files through this checkout. If a host needs copied files instead of symlinks, build the portable direct-copy bundle:

```bash
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
```

The exported bundle keeps `skills/` and `references/` as siblings:

```text
dist/naval-direct-install/
  skills/
    n-router/
    n-setup/
    n-save-learning/
    n-memory-refresh/
    ...
  references/
    chapter-summaries/
    memory/
    workflows/
    coverage-matrix.yaml
    router-guide.md
    skill-catalog.md
```

Copy or upload those two sibling folders together. If you validate an already-installed target, point the validator at that agent root:

```bash
python3 scripts/validate_direct_install.py --agent-root <agent-root>
```

## Updating Local Installs

For local checkout installs:

```bash
cd ~/plugins/naval
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add naval@personal --json
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
python3 scripts/smoke_install.py
```

If a host caches plugin definitions, restart the app or start a fresh thread/session after updating.

If you enabled optional memory with `n-setup`, keep `.naval/config.local.yaml` private and review saved files before committing any project-local `docs/naval/` output.

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
