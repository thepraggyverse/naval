# Development

Most generated files are produced by:

```bash
python3 scripts/build_naval_pack.py
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
- `scripts/check_coverage.py`

Hand-maintained public docs include:

- `README.md`
- `docs/EXAMPLES.md`
- `docs/INSTALL.md`
- `docs/PLUGIN_REFERENCE.md`
- `docs/SYMLINKS.md`
- `docs/DEVELOPMENT.md`
- `docs/SOURCE_BOUNDARIES.md`

## Validate

Run:

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
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

## Add A Skill

Edit `SKILLS` inside `scripts/build_naval_pack.py`.

Add or update mappings in `coverage_matrix()`.

Regenerate:

```bash
python3 scripts/build_naval_pack.py
```

Validate:

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

The public validator expects the hand-maintained docs above to exist, so install and usage
documentation stays part of the release surface.

## Add A Workflow

Edit `WORKFLOWS` inside `scripts/build_naval_pack.py`, then add it to `CATEGORY_WORKFLOWS` or a specific skill path if needed.

## Keep Skills Lean

Do not paste the whole book into a skill. Keep `SKILL.md` files small and route detailed knowledge to `references/`.

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
