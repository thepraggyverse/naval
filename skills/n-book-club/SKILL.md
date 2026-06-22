---
name: n-book-club
description: "Apply The Almanack of Naval Ravikant to discuss chapters, exercises, takeaways, and reading reflections. Use when the user asks for n-book-club, says \"Run a book club discussion for the wealth section.\", or wants this Naval lens."
---

# Naval Book Club

## Purpose

Discuss chapters, exercises, takeaways, and reading reflections.

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

- The user asks for `n-book-club` directly.
- The user asks: "Run a book club discussion for the wealth section."
- The user is dealing with: discuss chapters, exercises, takeaways, and reading reflections.
- The situation would benefit from a router result, review, scorecard, or generated study artifact.

## Workflow

1. Restate the user's situation in plain language.
2. Ask for missing context only when the decision would otherwise be unsafe or fake.
3. Apply the relevant Naval lens from the references.
4. Separate signal from status, desire, fear, identity, and generic self-help.
5. Convert the principle into a concrete decision, scorecard, experiment, practice, or next action.
6. Include a short caveat when the topic touches health, finance, legal risk, or exact citation.


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

User: "Run a book club discussion for the wealth section."
Assistant: Apply this skill, cite the relevant reference section, and end with one concrete action.

## Quality Bar

- Make the answer specific to the user's actual situation.
- Prefer one sharp recommendation over a buffet of advice.
- Name the tradeoff or hidden cost.
- End with something the user can do, test, stop, or observe today.
