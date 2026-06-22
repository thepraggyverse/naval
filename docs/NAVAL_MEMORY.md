# Naval Memory

`naval` is stateless by default. The optional memory layer lets users save useful reviews, decisions, scorecards, experiments, practices, learnings, and quote notes so future Naval sessions can search them.

Memory is opt-in because Naval outputs can contain private reflections. Skills must ask before writing. Public repositories should keep only `public-safe` artifacts that the user intentionally approves.

## Setup

Run `n-setup` in a project or notes workspace. It creates or updates a local config only after approval:

```text
.naval/config.local.yaml
```

The example config lives at:

```text
.naval/config.local.example.yaml
```

Local configs are gitignored by:

```text
.naval/*.local.yaml
```

## Storage Modes

| Mode | Use When | Notes |
|---|---|---|
| No persistence | You want one-off coaching only. | `memory_enabled: false`. |
| Project-local `docs/naval/` | The repo is private or the artifacts are public-safe. | Good for project decisions and scorecards. |
| Custom folder | You have an existing notes path. | Use an absolute path in `memory_root`. |
| Personal vault | Reflections are private or cross-project. | Prefer this for health, relationships, desires, and inner work. |

## Folder Layout

The default project-local memory root is:

```text
docs/naval/
  reviews/
  decisions/
  scorecards/
  experiments/
  practices/
  learnings/
  quotes/
```

## Artifact Types

| Type | Folder | Created By | Purpose |
|---|---|---|---|
| Review | `reviews/` | `n-daily-review`, `n-weekly-compound-review` | Dated reflection across health, work, desire, judgment, and compounding. |
| Decision | `decisions/` | `n-decision-rules`, `n-big-life-decisions` | A choice, rationale, and reversal conditions. |
| Scorecard | `scorecards/` | `n-opportunity-scorecard`, `n-relationship-scorecard` | A scored opportunity, relationship, project, job, or investment. |
| Experiment | `experiments/` | `n-principle-to-action` | A time-boxed test of a principle. |
| Practice | `practices/` | `n-meditation-system`, `n-habit-change` | A repeatable behavior or inner-work protocol. |
| Learning | `learnings/` | `n-save-learning` | One reusable insight from a completed session. |
| Quote note | `quotes/` | `n-quote-safety`, `n-source-fidelity` | Safe paraphrase, attribution note, or verification reminder. |

## Schemas And Templates

Schemas live in:

```text
references/memory/schemas/
```

Templates live in:

```text
references/memory/templates/
```

Every saved artifact should include:

- `artifact_type`
- `created`
- `source_skill`
- `privacy`
- `tags`

## Privacy Rules

- Never auto-save private reflections.
- Prefer `personal` or `private` for health, relationships, desires, envy, anger, and inner work.
- Use `public-safe` only when the artifact has been reviewed for public repo safety.
- Do not save long book excerpts or full source text.
- Use `n-quote-safety` before publishing exact wording.

## Direct-Copy Installs

Generated skills reference shared files with `../../references/...`. Plugin installs and source symlinks resolve those paths from this repo.

For direct-copy installs, build the portable bundle:

```bash
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
```

The exported layout keeps both pieces in the same agent root:

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
    book-map.md
    coverage-matrix.yaml
    router-guide.md
    skill-catalog.md
```

Copy the full `references/` folder. The memory files alone are not enough because most generated skills also read chapter summaries, workflows, routing, catalog, and coverage files.

If you copy the bundle somewhere else, validate the final target:

```bash
python3 scripts/validate_direct_install.py --agent-root <agent-root>
```
