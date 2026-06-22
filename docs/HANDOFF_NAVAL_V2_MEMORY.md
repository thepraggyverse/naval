# Naval v2 Memory Handoff

Date: 2026-06-22

## Summary

This pass upgrades `naval` from a 76-skill public pack to a 79-skill pack with an opt-in memory/setup layer and copied-install portability checks.

Major additions:

- `n-setup` configures optional output location, privacy default, and copied-install guidance.
- `n-save-learning` saves 1-3 approved reusable learnings with YAML frontmatter, duplicate checks, and explicit `memory_enabled: false` handling.
- `n-memory-refresh` audits saved Naval memory for stale, duplicated, contradictory, superseded, or low-value entries.
- `n-daily-review` and `n-weekly-compound-review` can optionally save dated review logs after approval.
- `references/memory/` now contains schemas and templates for reviews, decisions, scorecards, experiments, practices, learnings, and quote notes.
- `.naval/config.local.example.yaml` documents local memory config while `.naval/*.local.yaml` stays ignored.
- `scripts/export_direct_install.py` builds a portable copied `skills/` plus sibling `references/` bundle.
- `scripts/validate_direct_install.py` simulates copied installs and validates real exported agent roots.
- Codex CLI install docs now distinguish marketplace registration from plugin enablement with `codex plugin add naval@personal --json`.

## Files Touched

Generated or regenerated:

- `skills/n-*`
- `skills/n-*/agents/openai.yaml`
- `references/coverage-matrix.yaml`
- `references/skill-catalog.md`
- `references/memory/`

Generator and validators:

- `scripts/build_naval_pack.py`
- `scripts/export_direct_install.py`
- `scripts/validate_public.py`
- `scripts/validate_direct_install.py`

Docs and metadata:

- `README.md`
- `AGENTS.md`
- `CONTEXT.md`
- `CHANGELOG.md`
- `docs/AUDIT.md`
- `docs/DEVELOPMENT.md`
- `docs/HARNESS_SUPPORT.md`
- `docs/INSTALL.md`
- `docs/NAVAL_MEMORY.md`
- `docs/PLUGIN_REFERENCE.md`
- `docs/SYMLINKS.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/*`
- `.cursor-plugin/*`
- `.github/workflows/validate.yml`
- `.opencode/INSTALL.md`
- `gemini-extension.json`
- `package.json`
- `skills.sh.json`

## Validation Run

All checks passed after the final fixes:

```bash
python3 scripts/validate_public.py
# Public validation passed: 79 n-prefixed skills

python3 scripts/check_coverage.py
# Coverage check passed: 79 n-prefixed skills mapped with valid references.

python3 scripts/validate_direct_install.py
# Direct install validation passed: 79 skills with sibling references.

python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
# Plugin validation passed

python3 -m py_compile scripts/build_naval_pack.py scripts/export_direct_install.py scripts/validate_public.py scripts/validate_direct_install.py scripts/install_local.py
# passed with no output

npm run export:direct
# Exported direct install bundle: dist/naval-direct-install

python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
# Direct install validation passed: 79 skills with sibling references in dist/naval-direct-install.

for d in skills/n-*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
# all 79 skills reported "Skill is valid!"
```

The generator was also rerun:

```bash
python3 scripts/build_naval_pack.py
# Generated 79 n-prefixed Naval skills
```

Local install/load smoke:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
# Marketplace entry already up to date: ~/.agents/plugins/marketplace.json
# Symlinked skills: 711

python3 ~/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py .
# Updated plugin version cachebuster in .codex-plugin/plugin.json

codex plugin add naval@personal --json
# naval@personal installed, enabled

codex exec --ephemeral --sandbox read-only -C "$PWD" 'Use $n-setup. Do not write files. In two concise bullets, name the local config file it manages and the default project-local memory root.'
# Local config file: .naval/config.local.yaml
# Default project-local memory root: docs/naval/
```

The live run loaded `n-setup` from the cached plugin path and read its memory references. Warnings seen during the run were from unrelated installed plugins/MCP auth and this machine's very large global skill library; the Naval plugin itself loaded and answered correctly.

After final docs cleanup, the latest installed Codex cache was `0.1.0+codex.20260622184649`. Source plugin validation, cached plugin validation, `codex plugin list`, direct-install validation, and a live `$n-setup` invocation all passed for that version.

## Autoreview

Command:

```bash
autoreview --mode local
```

Findings fixed:

- `docs/NAVAL_MEMORY.md` direct-copy example originally showed only memory references. It now says to copy the full sibling `references/` folder.
- `n-save-learning` originally did not explicitly honor `memory_enabled: false`. The generator now makes disabled memory stop before duplicate search or writes unless the user explicitly provides a one-off save path or enables memory through `n-setup`.
- `scripts/export_direct_install.py --force` originally could remove an arbitrary target directory. It now only replaces directories that contain the generated direct-install marker.
- Public docs originally included local absolute paths in generic command examples. They now use portable `~/plugins/naval` or `$PWD` examples.

Final autoreview result:

```text
autoreview clean: no accepted/actionable findings reported
overall: patch is correct (0.78)
```

## Install And Update

Local plugin:

```bash
python3 scripts/install_local.py --marketplace
```

Direct skill symlinks:

```bash
python3 scripts/install_local.py --symlink-skills
```

Both:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
```

Update local checkout:

```bash
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
```

Copied-skill installs must copy both:

```text
agent-root/
  skills/
    n-*/
  references/
```

Preferred direct-copy export:

```bash
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
```

## Memory Use

Memory is off by default. Start with:

```text
Use n-setup to configure optional Naval memory.
```

Then use:

- `n-save-learning` after a session produces reusable guidance.
- `n-memory-refresh` to clean stale or duplicated saved learnings.
- `n-daily-review` or `n-weekly-compound-review` when the user wants a dated review log.

Local config belongs in `.naval/config.local.yaml` and should not be committed.

## Remaining Risks

- Direct-copy installs are now deterministic when users use `npm run export:direct`. Hosts that transform uploaded folders may still need their own import-specific verification, so validate the final agent root with `python3 scripts/validate_direct_install.py --agent-root <agent-root>`.
- The optional memory schemas are lightweight contracts, not strict runtime parsers.
- Saved `docs/naval/` artifacts can still contain private content if a user chooses a public project-local folder, so the docs and skills keep approval and privacy checks explicit.
- Broad all-home symlink installs can contribute to Codex skill-list budget warnings on machines that already have thousands of skills. Codex users should prefer the native plugin and use targeted `--skill-home` symlinks for non-Codex harnesses.

## Next Improvements

- Add a live symlink smoke test that verifies default agent homes on a real machine.
- Add browsable generated docs pages per skill if GitHub readers want a non-`SKILL.md` view.
- Add release tags once the package stabilizes for pinned OpenCode, Gemini, Pi, and plugin-manager installs.
