# Examples

These examples show how to use `naval` as a plugin and how the `n-*` skills work together. They are prompt patterns, not scripts you must copy exactly.

## Example 1: Career Decision

Use this when the user has a high-stakes job, startup, city, company, or partner decision.

```text
Use Naval to decide whether I should leave my current job and work on my startup idea full time.

Context:
- I have 10 months of savings.
- The startup idea has early users but no revenue.
- My current job pays well but feels stagnant.
- I care about freedom, long-term upside, and health.
```

| Step | Skill | What It Should Produce |
|---|---|---|
| 1 | `n-router` | Primary route, secondary skills, first clarifying question. |
| 2 | `n-big-life-decisions` | Decision frame across job, company, money, health, and direction. |
| 3 | `n-opportunity-scorecard` | Score the startup on leverage, compounding, uniqueness, risk, and downside. |
| 4 | `n-risk-of-ruin` | Ruin risks, guardrails, runway limits, and reversible tests. |
| 5 | `n-principle-to-action` | A concrete experiment, deadline, and decision rule. |

Good output shape:

| Section | Content |
|---|---|
| Route | Why these skills were selected. |
| Clarifying Questions | Only the questions that change the decision. |
| Scorecard | Leverage, ownership, specific knowledge, compounding, reputation, health, downside. |
| Red Flags | Ruin risks and irreversible commitments. |
| Action | A small test, a kill criterion, and a date to revisit. |

## Example 2: Specific Knowledge Audit

Use this when the user wants to find their edge instead of copying someone else's path.

```text
Run n-specific-knowledge on me.

I like explaining complex technical ideas, building small tools, reading product strategy, and noticing where workflows break. I dislike heavy meetings and generic management tracks.
```

| Step | Skill | What It Should Produce |
|---|---|---|
| 1 | `n-specific-knowledge` | Authentic strengths, obsessions, taste, proof, and hard-to-copy patterns. |
| 2 | `n-authenticity-positioning` | Ways to position the user away from commodity competition. |
| 3 | `n-leverage-stack` | Code, media, distribution, automation, and brand leverage ideas. |
| 4 | `n-principle-to-action` | A 7-day or 30-day experiment. |

Good output shape:

```text
Specific knowledge candidates:
1. ...
2. ...

Evidence:
- ...

Leverage paths:
- Code:
- Media:
- Distribution:

Experiment:
- Build:
- Publish:
- Measure:
- Stop if:
```

## Example 3: Desire Audit

Use this when the user is restless, jealous, compulsively chasing, or unhappy despite external progress.

```text
n-desire-audit

I keep checking whether people in my field are ahead of me. It makes me anxious, but I also feel like the anxiety keeps me moving.
```

| Step | Skill | What It Should Produce |
|---|---|---|
| 1 | `n-desire-audit` | The desire, its cost, its hidden promise, and whether to drop, change, accept, or leave. |
| 2 | `n-envy-antidote` | The comparison trap and a cleaner personal scorecard. |
| 3 | `n-happiness-habits` | A practical daily habit to reduce the loop. |
| 4 | `n-presence-practice` | A short attention reset when the checking impulse appears. |

Good output shape:

| Section | Content |
|---|---|
| Desire | What the user appears to want and what they hope it will solve. |
| Cost | Attention, mood, health, relationships, or freedom cost. |
| Reality Check | What is true regardless of the desire. |
| Replacement | A calmer metric, habit, or boundary. |
| Practice | What to do the next time the loop appears. |

## Example 4: Opportunity Scorecard

Use this for jobs, startups, products, investments, writing projects, or major collaborations.

```text
n-opportunity-scorecard

Score this opportunity: building a paid course for senior developers who want to use AI agents safely inside existing codebases.
```

| Dimension | What To Look For |
|---|---|
| Specific knowledge | Does the user have a hard-to-train edge here? |
| Leverage | Can code, media, capital, people, or distribution multiply the work? |
| Ownership | Is there equity, IP, brand, audience, or durable asset creation? |
| Long-term game | Can this compound with long-term people in a long-term market? |
| Accountability | Would public ownership increase trust and upside? |
| Risk of ruin | What would make this legally, financially, reputationally, or health-wise dangerous? |
| Work as play | Is the work intrinsically energizing for the user? |

Good output shape:

```text
Score:
- Specific knowledge: 1-5
- Leverage: 1-5
- Ownership: 1-5
- Long-term compounding: 1-5
- Accountability fit: 1-5
- Risk of ruin: low / medium / high
- Work-as-play fit: 1-5

Verdict:
- Do:
- Do not:
- Test:
```

## Example 5: Weekly Compound Review

Use this at the end of a week to turn life and work into feedback.

```text
n-weekly-compound-review

This week:
- Shipped two product improvements.
- Slept badly three nights.
- Avoided one hard conversation.
- Read 80 pages.
- Spent too much time comparing myself online.
```

| Review Area | Helpful Skills |
|---|---|
| Wealth and work | `n-wealth-map`, `n-leverage-stack`, `n-time-value-focus` |
| Judgment | `n-clear-thinking`, `n-reality-ego-audit`, `n-inversion-filter` |
| Health | `n-health-first`, `n-exercise-priority`, `n-diet-simplifier` |
| Happiness | `n-desire-audit`, `n-envy-antidote`, `n-presence-practice` |
| Values | `n-values-filter`, `n-freedom-from-expectations` |

Good output shape:

| Section | Content |
|---|---|
| What Compounded | The actions that make next week easier. |
| What Leaked | The habits or decisions that made next week harder. |
| One Deletion | Something to stop or remove. |
| One Commitment | A visible action for the next week. |
| One Review Date | When to inspect the result. |

## Example 6: Reading Curriculum

Use this when the user wants to read in a way that compounds instead of collecting book titles.

```text
n-reading-curriculum

Build me a 12-week reading path for judgment, economics, science foundations, persuasion, and inner work. I prefer shorter books and essays.
```

| Step | Skill | What It Should Produce |
|---|---|---|
| 1 | `n-reading-curriculum` | Sequence, themes, and reading cadence. |
| 2 | `n-reading-system` | How to skim, reread, drop weak books, and follow curiosity. |
| 3 | `n-foundational-learning` | Foundations to prioritize before advanced material. |
| 4 | `n-next-sources` | Source trails for going deeper. |

Good output shape:

```text
12-week path:
- Weeks 1-2:
- Weeks 3-4:
- ...

Operating rules:
- Drop if:
- Reread if:
- Summarize by:

Output:
- One concept note per week
- One decision or behavior changed per week
```

## Example 7: Quote Safety

Use this when the user wants to quote or publish a Naval idea.

```text
n-quote-safety

I want to use a Naval quote about wealth, leverage, and judgment in a blog post. Help me make it safe and useful.
```

| Step | Skill | What It Should Produce |
|---|---|---|
| 1 | `n-quote-safety` | Short-quote discipline, attribution note, and paraphrase-first recommendation. |
| 2 | `n-source-fidelity` | Whether the interpretation matches the book's idea. |
| 3 | `n-next-sources` | Where to verify exact wording if exact wording matters. |

Good output shape:

```text
Recommendation:
- Prefer paraphrase / short quote:
- Attribution:
- Need exact verification: yes/no
- Safe paraphrase:
- Risk note:
```

## Example 8: Book Club Discussion

Use this for a guided reading group or self-review after a chapter.

```text
n-book-club

Run a book club discussion for the wealth section. I want questions that force action, not just agreement.
```

| Section | Prompt Type |
|---|---|
| Recall | What idea do you remember without looking? |
| Friction | Which idea do you resist and why? |
| Evidence | Where does your current life already prove or disprove it? |
| Application | What would change this week if you took it seriously? |
| Review | What will you inspect seven days from now? |

Good output shape:

```text
Discussion questions:
1. ...
2. ...

Action round:
- Stop:
- Start:
- Measure:

Follow-up:
- Review date:
- Evidence to bring:
```
