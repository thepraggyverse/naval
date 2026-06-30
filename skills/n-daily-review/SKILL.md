---
name: n-daily-review
description: "Naval daily review: Run a daily health, work, desire, focus, and freedom review. Trigger when the user asks \"Run my daily Naval review.\" or names n-daily-review."
---

# Naval Daily Review

## Purpose

Run a daily health, work, desire, focus, and freedom review.

## Read First

- `../../references/book-map.md`
- `../../references/coverage-matrix.yaml`
- `../../references/skill-catalog.md`
- `../../references/chapter-summaries/wealth.md`
- `../../references/chapter-summaries/judgment.md`
- `../../references/chapter-summaries/happiness.md`
- `../../references/chapter-summaries/saving-yourself.md`
- `../../references/chapter-summaries/philosophy.md`
- `../../references/chapter-summaries/reading.md`
- `../../references/workflows/daily-review.md`
- `../../references/workflows/weekly-compound-review.md`
- `../../references/workflows/opportunity-scorecard.md`
- `../../references/workflows/relationship-scorecard.md`
- `../../references/workflows/quote-safety.md`

If these reference paths are unavailable, the install likely copied a skill without the sibling `references/` folder. Ask the user to copy or symlink `references/` beside the parent of the copied `skills/` folder, or reinstall through the plugin/symlink path.

## Use When

- The user asks for `n-daily-review` directly.
- The user asks: "Run my daily Naval review."
- The user is dealing with: run a daily health, work, desire, focus, and freedom review.
- The situation would benefit from a router result, review, scorecard, or generated study artifact.

## Workflow

1. Restate the user's situation in plain language.
2. Ask for missing context only when the decision would otherwise be unsafe or fake.
3. Apply the relevant Naval lens from the references.
4. Separate signal from status, desire, fear, identity, and generic self-help.
5. Convert the principle into a concrete decision, scorecard, experiment, practice, or next action.
6. Include a short caveat when the topic touches health, finance, legal risk, or exact citation.

## Optional Persistence

After producing the review, check whether the user asked to save it or whether `.naval/config.local.yaml` enables memory. If saving is relevant:

1. Read `../../references/memory/templates/review.md` and `../../references/memory/schemas/review.yaml`.
2. Ask before writing. Never auto-save private reflections.
3. Use the configured memory root, usually `docs/naval/`.
4. Save to `<memory_root>/reviews/YYYY-MM-DD-daily-review.md`.
5. Set `artifact_type: review`, `source_skill: n-daily-review`, `review_period: daily`, and a privacy level.
6. If no config exists, offer `n-setup` instead of inventing a storage location.


## Output

Return concise sections:

- Situation
- Naval lens
- Diagnosis
- Options or scorecard
- Recommended action
- 7-day experiment or daily practice
- What to avoid

## Do Not

- Do not reproduce long book passages.
- Do not pretend Naval has one answer for every person.
- Do not give generic motivation when a decision, practice, or test is possible.
- Do not treat money, status, peace, health, and meaning as interchangeable.

## Example

User: "Run my daily Naval review."
Assistant: Apply this skill, cite the relevant reference section, and end with one concrete action.

## Quality Bar

- Make the answer specific to the user's actual situation.
- Prefer one sharp recommendation over a buffet of advice.
- Name the tradeoff or hidden cost.
- End with something the user can do, test, stop, or observe today.
