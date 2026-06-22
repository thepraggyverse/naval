# Naval Memory References

These files define the optional memory layer used by `n-setup`, `n-save-learning`, `n-memory-refresh`, and review skills that save output.

The memory layer is opt-in. Skills must ask before writing private reflections, scorecards, reviews, or quote notes. Public repositories should store only public-safe or intentionally reviewed artifacts.

## Artifact Types

- `review`: daily, weekly, or custom reflection.
- `decision`: a remembered choice and reversal conditions.
- `scorecard`: an opportunity or relationship scorecard.
- `experiment`: a time-boxed test of a principle.
- `practice`: a repeatable habit or inner-work protocol.
- `learning`: a reusable insight from a completed session.
- `quote-note`: a paraphrase, short excerpt note, or verification reminder.

## Storage Convention

Use the configured memory root. The default project-local root is `docs/naval/`.

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

Use `references/memory/templates/` for starting shapes and `references/memory/schemas/` for required frontmatter.
