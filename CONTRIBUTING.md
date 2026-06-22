# Contributing

Contributions are welcome if they keep the pack practical, source-safe, and easy to install.

## Good Contributions

- Better routing rules.
- Better scorecards and workflows.
- More precise coverage mapping.
- Clearer install docs.
- Validation improvements.
- New `n-*` skills that map to a real book concept or useful operating workflow.

## Avoid

- Long book excerpts.
- Generic motivation with no action.
- Skills that do not produce a decision, scorecard, practice, experiment, boundary, reading path, or removal.
- Unvalidated generated changes.

## Development Flow

```bash
python3 scripts/build_naval_pack.py
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
```

Then inspect the generated files you changed.

Read [AGENTS.md](AGENTS.md) before larger changes. It describes generated files, harness metadata, validation, and the public source boundary.

If a change affects install paths, plugin metadata, skill counts, or public descriptions, update the relevant docs and manifests in the same change.

## Naming

All user-facing skills must use the `n-` prefix:

```text
n-specific-knowledge
n-desire-audit
n-decision-rules
```

Keep names short and action-oriented.
