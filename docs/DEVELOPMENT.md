# Development

Most generated files are produced by:

```bash
python3 scripts/build_naval_pack.py
python3 scripts/generate_skill_docs.py
```

That script writes:

- `skills/n-*/SKILL.md`
- `skills/n-*/agents/openai.yaml`
- `references/book-map.md`
- `references/coverage-matrix.yaml`
- `references/skill-catalog.md`
- `references/router-guide.md`
- `references/chapter-summaries/*.md`
- `references/workflows/*.md`
- `references/memory/README.md`
- `references/memory/schemas/*.yaml`
- `references/memory/templates/*.md`
- `docs/skills/*.md`
- `scripts/check_coverage.py`

Hand-maintained public docs include:

- `AGENTS.md`
- `CHANGELOG.md`
- `CONTEXT.md`
- `README.md`
- `PRIVACY.md`
- `SECURITY.md`
- `docs/AUDIT.md`
- `docs/EXAMPLES.md`
- `docs/HARNESS_SUPPORT.md`
- `docs/INSTALL.md`
- `docs/NAVAL_MEMORY.md`
- `docs/PLUGIN_REFERENCE.md`
- `docs/RELEASE.md`
- `docs/SYMLINKS.md`
- `docs/DEVELOPMENT.md`
- `docs/SOURCE_BOUNDARIES.md`

Hand-maintained harness metadata includes:

- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `.cursor-plugin/plugin.json`
- `.cursor-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`
- `gemini-extension.json`
- `GEMINI.md`
- `.opencode/INSTALL.md`
- `.opencode/plugins/naval.js`
- `.pi/extensions/naval.ts`
- `package.json`
- `skills.sh.json`

## Validate

Run:

```bash
python3 scripts/generate_skill_docs.py
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/audit_skill_quality.py
python3 scripts/validate_direct_install.py
python3 scripts/smoke_install.py
```

For direct-copy packaging, build and validate the exported root:

```bash
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
```

If you have Codex's local validation helpers installed, you can also run:

```bash
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

And validate every skill:

```bash
for d in skills/n-*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
```

## Local Install Smoke

After changing plugin metadata, update the Codex cachebuster, reinstall, and run one read-only live invocation:

```bash
python3 ~/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py .
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add naval@personal --json
codex exec --ephemeral --sandbox read-only -C "$PWD" 'Use $n-setup. Do not write files. In two concise bullets, name the local config file it manages and the default project-local memory root.'
```

The smoke should identify `.naval/config.local.yaml` and `docs/naval/`.

Some developer machines have thousands of global skill folders. If `codex exec` warns that the skills context budget was exceeded, verify whether `$n-setup` still loads from the cached plugin path. For Codex-only testing, prefer the native plugin install and avoid broad all-home symlinks unless you are also testing direct-skill discovery.

The scripted equivalent is:

```bash
python3 scripts/smoke_install.py --codex --live
```

## Add A Skill

Edit `SKILLS` inside `scripts/build_naval_pack.py`.

Add or update mappings in `coverage_matrix()`.

Regenerate:

```bash
python3 scripts/build_naval_pack.py
python3 scripts/generate_skill_docs.py
```

Validate:

```bash
python3 scripts/generate_skill_docs.py
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
python3 scripts/smoke_install.py
```

The public validator expects the hand-maintained docs and harness metadata above to exist, so install and usage documentation stays part of the release surface.

`export_direct_install.py` builds a copied agent root with sibling `skills/` and `references/` folders. `validate_direct_install.py` can either simulate that layout or validate an exported/installed root with `--agent-root`. Keep both passing whenever generated skills add or change `../../references/...` paths.

## Add A Workflow

Edit `WORKFLOWS` inside `scripts/build_naval_pack.py`, then add it to `CATEGORY_WORKFLOWS` or a specific skill path if needed.

## Keep Skills Lean

Do not paste the whole book into a skill. Keep `SKILL.md` files small and route detailed knowledge to `references/`.
See [SKILL_QUALITY.md](SKILL_QUALITY.md) for the description shape, output bar, and authoring audit.

Every skill should end in one of:

- decision
- scorecard
- experiment
- practice
- reading path
- boundary
- removal

## Public Boundary

The repo is public. Do not add:

- the full book text
- private notes
- API keys
- local absolute paths except inside examples that are clearly user-local
- generated runtime caches
- generated `dist/` direct-copy bundles
- local `.naval/*.local.yaml` memory config files
