# Skill Quality

This repo treats each `n-*` folder as a callable skill, not a long note.
The goal is predictable behavior across Codex, Claude-compatible loaders, OpenCode, Pi, and direct `SKILL.md` installs.

## Authoring Rules

| Rule | Why It Matters | Checked By |
|---|---|---|
| Front-load `Naval` in every description. | The leading word makes invocation predictable. | `scripts/audit_skill_quality.py` |
| Keep descriptions under 220 characters. | Descriptions are always-loaded routing context in model-invoked harnesses. | `scripts/audit_skill_quality.py` |
| Use one sharp `Trigger` clause. | Broad trigger piles create routing noise. | `scripts/audit_skill_quality.py` |
| Keep detailed book knowledge in `references/`. | `SKILL.md` stays readable and portable. | `scripts/check_coverage.py` |
| Include a direct-copy fallback. | Copied skill folders need the sibling `references/` folder. | `scripts/audit_skill_quality.py` |
| End with a checkable artifact. | The skill should produce a decision, scorecard, experiment, practice, reading path, boundary, removal, or saved-file status. | `scripts/audit_skill_quality.py` |

## Description Pattern

Generated skills use this shape:

```text
Naval <leading word>: <specific purpose>. Trigger when the user asks "<example>" or names n-skill.
```

Memory skills use the same idea with a custom branch:

```text
Naval setup: configure optional memory paths, privacy defaults, and direct-install reference guidance. Trigger for setup, .naval/config.local.yaml, saved-review locations, or copied skills.
```

Avoid generic branches such as "wants this Naval lens".
They match too much and make routing less precise.

## Body Pattern

Every generated skill should keep this ladder:

1. `Purpose`
2. `Read First`
3. `Use When`
4. `Workflow`
5. `Output`
6. `Do Not`
7. `Example`
8. `Quality Bar`

The body should do the work that the agent always needs.
Long chapter summaries, workflows, copyright boundaries, memory schemas, and concept maps belong in `references/`.

## Regeneration

Edit generated skills in [scripts/build_naval_pack.py](../scripts/build_naval_pack.py), then run:

```bash
python3 scripts/build_naval_pack.py
python3 scripts/generate_skill_docs.py
npm run validate
```

Do not hand-edit generated `skills/n-*/SKILL.md` files unless you are intentionally testing the generator output.

## Audit

Run the quality audit directly:

```bash
npm run audit:skills
```

The audit is intentionally conservative.
If it fails, fix the generator or the skill body rather than weakening the check.
