---
name: n-save-learning
description: "Save one to three approved reusable learnings from a completed Naval session with YAML frontmatter, privacy checks, duplicate search, and optional docs/naval storage. Use when the user says save what we learned, compound this Naval session, remember this, or capture a review insight."
---

# Naval Save Learning

Save only the reusable insight, not a transcript or generic activity log.

## Read First

- `../../references/memory/README.md`
- `../../references/memory/templates/learning.md`
- `../../references/memory/schemas/learning.yaml`

If these files are unavailable, the install likely copied a skill without the sibling `references/` folder. Tell the user to copy or symlink `references/` beside the parent of the copied `skills/` folder before continuing.

## Workflow

1. Resolve memory config:
   - Prefer `.naval/config.local.yaml` in the current repo.
   - If config exists with `memory_enabled: false`, treat persistence as disabled. Do not search or write under `memory_root` unless the user explicitly asks for a one-off save path or chooses to run `n-setup` to enable memory.
   - If no config exists, ask whether to continue with no write, write once to a user-provided path, or run `n-setup`.
2. Extract at most 1-3 learnings from the completed session. Look for:
   - a corrected assumption
   - a reusable decision rule
   - an experiment that should be repeated
   - a practice that worked
   - a scorecard signal that should guide future choices
3. Discard material that was merely discussed. Do not save private details unless they are necessary and the user approves the privacy level.
4. Draft each learning with:
   - title
   - type: insight, correction, playbook, pattern, or practice
   - tags for future retrieval
   - confidence: high, medium, or low
   - privacy: public-safe, personal, or private
   - why it matters later
5. If persistence remains disabled, return the drafted learnings as unsaved output and stop before duplicate search or writes.
6. Search the approved memory root before writing. Check `learnings/`, `reviews/`, `decisions/`, `scorecards/`, `experiments/`, and `practices/` for duplicate or superseded entries.
7. Present the draft and duplicate findings. Ask for approval before creating or updating any file.
8. Write approved learnings to `<memory_root>/learnings/YYYY-MM-DD-short-title.md` using `references/memory/templates/learning.md`.

## Do Not

- Do not auto-save.
- Do not save the full conversation.
- Do not store private reflections in a public repo unless the user explicitly chooses that.
- Do not create five or more learnings from one session; filter harder.

## Output

Return:

- Saved files or skipped reason
- Duplicate or supersession handling
- Privacy level used
- Tags that will help future retrieval
