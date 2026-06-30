---
name: n-memory-refresh
description: "Naval memory refresh: audit saved reviews, learnings, scorecards, and decisions. Trigger for n-memory-refresh, docs/naval cleanup, stale memory, duplicates, or contradictions."
---

# Naval Memory Refresh

Keep the optional Naval memory layer useful, current, and small.

## Read First

- `../../references/memory/README.md`
- `../../references/memory/schemas/learning.yaml`
- `../../references/memory/schemas/review.yaml`
- `../../references/memory/schemas/decision.yaml`

If these files are unavailable, the install likely copied a skill without the sibling `references/` folder. Tell the user to copy or symlink `references/` beside the parent of the copied `skills/` folder before continuing.

## Workflow

1. Resolve the configured memory root from `.naval/config.local.yaml`, or ask for the folder to inspect.
2. Inventory markdown files under:
   - `reviews/`
   - `decisions/`
   - `scorecards/`
   - `experiments/`
   - `practices/`
   - `learnings/`
   - `quotes/`
3. Read frontmatter first. Group by tags, source skill, artifact type, and subject.
4. Classify each candidate:
   - Keep: still useful and accurate
   - Update: useful but references, tags, status, or wording drifted
   - Supersede: replaced by a newer, better entry
   - Consolidate: duplicates another entry
   - Recommend deletion: low-value, obsolete, or unsafe to retain
5. Be conservative. Ask before editing, deleting, or marking private material superseded.
6. Prefer marking `status: superseded` with `superseded_by` over deleting unless the user asks for deletion.
7. Produce a short refresh report. Save it only if the user approves.

## Output

Return:

- Memory root inspected
- Counts by artifact type
- Applied changes
- Recommended changes needing approval
- Contradictions found
- Next cleanup target
