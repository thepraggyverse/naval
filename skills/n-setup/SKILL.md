---
name: n-setup
description: "Configure optional Naval memory output paths, privacy defaults, and direct-install reference guidance. Use when the user asks to set up Naval memory, choose where reviews/learnings should be saved, configure .naval/config.local.yaml, or prepare copied/direct skill installs."
---

# Naval Setup

Configure the optional Naval memory layer for the current repo or workspace.

## Read First

- `../../references/memory/README.md`
- `../../references/memory/templates/review.md`
- `../../references/memory/schemas/review.yaml`

If these files are unavailable, the install likely copied a skill without the sibling `references/` folder. Tell the user to copy or symlink `references/` beside the parent of the copied `skills/` folder before continuing.

## Workflow

1. Inspect the current repo root and check for `.naval/config.local.yaml`, `.naval/config.local.example.yaml`, `.gitignore`, and an existing `docs/naval/` folder.
2. Explain that persistence is optional and private by default. Naval reviews can contain personal reflections; never save them without explicit approval.
3. Ask where outputs should live, one question at a time:
   - no persistence
   - project-local `docs/naval/`
   - custom folder
   - personal notes or vault
4. Ask for the default privacy level: `public-safe`, `personal`, or `private`.
5. Draft `.naval/config.local.yaml` and show it before writing.
6. Write only after approval. If writing a local config, ensure `.naval/*.local.yaml` is covered by `.gitignore`; ask before editing `.gitignore`.
7. Offer to create the selected memory root and these folders only after approval: `reviews/`, `decisions/`, `scorecards/`, `experiments/`, `practices/`, `learnings/`, `quotes/`.

## Config Shape

```yaml
memory_enabled: true
memory_root: docs/naval
privacy_default: personal
require_save_confirmation: true
direct_install_requires_references: true
```

Use `memory_enabled: false` for no persistence.

## Output

Return:

- Config path
- Memory root
- Privacy default
- Folders created or skipped
- Whether `.naval/*.local.yaml` is gitignored
- Next skills to use, usually `n-daily-review`, `n-weekly-compound-review`, or `n-save-learning`
