# Unofficial Naval Skills [![Validate](https://github.com/thepraggyverse/naval/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/naval/actions/workflows/validate.yml)

`naval` is an unofficial plugin and skill pack for applying ideas from *The Almanack of Naval Ravikant*.

It gives agents 79 searchable `n-*` skills for wealth, judgment, happiness, health, values, reading, decisions, scorecards, daily reviews, weekly reviews, optional memory, source fidelity, and quote safety.

This repository does not include the full book text. It contains source-safe skill instructions, workflows, and reference maps.

It is not affiliated with Naval Ravikant, Eric Jorgenson, Navalmanack, or any publisher.

## What The Skills Do

Each skill gives the agent a specific job. The pack is split this way so the agent can load the right instructions for the user's situation instead of one giant prompt.

| Skill Type | What It Does | Examples |
|---|---|---|
| Router | Chooses the best Naval skill when the request is vague. | `n-router` |
| Wealth skills | Apply ideas about specific knowledge, accountability, ownership, leverage, long-term games, and risk. | `n-wealth-map`, `n-specific-knowledge`, `n-leverage-stack` |
| Judgment skills | Improve decisions with clear thinking, inversion, mental models, truth tests, and long-term consequences. | `n-decision-rules`, `n-clear-thinking`, `n-mental-models` |
| Happiness skills | Work through desire, envy, peace, presence, acceptance, and happiness habits. | `n-desire-audit`, `n-envy-antidote`, `n-presence-practice` |
| Health and agency skills | Build practical systems for health, exercise, diet, meditation, habits, and attention. | `n-health-first`, `n-meditation-system`, `n-habit-change` |
| Reading and philosophy skills | Build reading paths, values filters, meaning checks, and source trails. | `n-reading-curriculum`, `n-values-filter`, `n-next-sources` |
| Review and safety skills | Run daily/weekly reviews, score opportunities, check relationships, and keep quote use safe. | `n-weekly-compound-review`, `n-opportunity-scorecard`, `n-quote-safety` |
| Memory skills | Configure optional local output, save approved learnings, and refresh stale saved guidance. | `n-setup`, `n-save-learning`, `n-memory-refresh` |

## The Loop

```text
n-router
  -> picks the best skill for vague "use Naval on this" requests

n-wealth-map / n-decision-rules / n-desire-audit / n-health-first / ...
  -> applies one focused lens to the situation

n-principle-to-action / n-opportunity-scorecard / n-relationship-scorecard
  -> turns insight into an experiment, scorecard, boundary, or next action

n-daily-review / n-weekly-compound-review
  -> checks whether the actions are compounding

n-setup / n-save-learning / n-memory-refresh
  -> optionally saves approved learnings and keeps local memory clean

n-source-fidelity / n-quote-safety / n-coverage-auditor
  -> keeps the pack faithful, safe, and complete
```

Use whichever step fits the moment. If the user already knows the problem is about desire, start with `n-desire-audit`. If the situation is vague, start with `n-router`.

## Core Workflows

| Workflow | Start With | Then Use | Produces |
|---|---|---|---|
| Route a vague situation | `n-router` | The routed primary skill plus 1-3 secondary lenses. | Skill path, first question, output format. |
| Build a wealth path | `n-wealth-map` | `n-specific-knowledge`, `n-leverage-stack`, `n-equity-ownership`, `n-patience-compounding`. | Wealth strategy, leverage moves, ownership experiments. |
| Make a hard decision | `n-decision-rules` | `n-inversion-filter`, `n-risk-of-ruin`, `n-wisdom-long-term`. | Decision frame, avoid list, reversible next step. |
| Evaluate an opportunity | `n-opportunity-scorecard` | `n-long-term-games`, `n-accountability-risk`, `n-work-as-play`. | Scorecard, red flags, test plan. |
| Debug unhappiness | `n-desire-audit` | `n-envy-antidote`, `n-accept-change-leave`, `n-presence-practice`. | Desire map, cost, replacement practice. |
| Rebuild health and agency | `n-health-first` | `n-exercise-priority`, `n-diet-simplifier`, `n-meditation-system`, `n-habit-change`. | Health baseline, habit system, daily practice. |
| Learn and read better | `n-reading-curriculum` | `n-reading-system`, `n-foundational-learning`, `n-next-sources`. | Reading path, drop rules, weekly output. |
| Compound the week | `n-weekly-compound-review` | Any skills surfaced by the review. | Wins, leaks, deletion, commitment, review date. |
| Set up optional memory | `n-setup` | `n-save-learning`, `n-memory-refresh`. | Local config, output folders, schemas, approved saved learnings. |

## Quick Example

Use `n-router` when you do not know the exact skill name:

```text
Use Naval to analyze whether I should leave my job for a startup idea.
```

The router should return a path like:

| Step | Skill | Why |
|---|---|---|
| 1 | `n-big-life-decisions` | Frames the job, city, company, and life-direction tradeoff. |
| 2 | `n-opportunity-scorecard` | Scores the startup idea on leverage, upside, compounding, and risk. |
| 3 | `n-risk-of-ruin` | Looks for health, financial, legal, relationship, and reputation blowups. |
| 4 | `n-principle-to-action` | Turns the decision into a reversible experiment or clear commitment. |

For more walkthroughs, see [docs/EXAMPLES.md](docs/EXAMPLES.md).

## Getting Started

Clone the repo:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/naval.git ~/plugins/naval
cd ~/plugins/naval
```

Validate it:

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
```

Register it with the default personal Codex marketplace:

```bash
python3 scripts/install_local.py --marketplace
```

That makes the plugin available to Codex. To install and enable it from the Codex CLI:

```bash
codex plugin add naval@personal --json
codex plugin list | grep 'naval@personal'
```

Optionally expose every skill to local agent homes:

```bash
python3 scripts/install_local.py --symlink-skills
```

For Codex-only use, the plugin install is enough. Use direct skill symlinks for tools that scan `SKILL.md` folders, and prefer `--skill-home` when you only need one harness.

For both:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
```

Then search for `n-` in your agent or Codex skill picker.

Quick live smoke after installing:

```bash
codex exec --ephemeral --sandbox read-only -C "$PWD" 'Use $n-setup. Do not write files. In two concise bullets, name the local config file it manages and the default project-local memory root.'
```

## Optional Memory Layer

`naval` is stateless by default. It does not save private reflections, reviews, or decisions unless the user explicitly opts in.

Use `n-setup` when you want durable outputs. It can configure no persistence, project-local `docs/naval/`, a personal notes or Obsidian folder, or a custom path. Saved artifacts use small schemas and templates under [references/memory/](references/memory/), and every write should be confirmed before it happens.

Useful follow-up skills:

| Skill | Use When | Saves To |
|---|---|---|
| `n-save-learning` | A session produced 1-3 reusable insights worth keeping. | `learnings/` |
| `n-memory-refresh` | Saved guidance may be stale, duplicated, contradictory, or low-value. | Updates existing memory files after approval. |
| `n-daily-review` | You want a dated review log after a daily review. | `reviews/` |
| `n-weekly-compound-review` | You want a dated weekly compounding review. | `reviews/` |

See [docs/NAVAL_MEMORY.md](docs/NAVAL_MEMORY.md) for the privacy contract, folder layout, direct-copy install requirements, and memory templates.

## Harness Support

| Harness | Best Path | Details |
|---|---|---|
| Codex App / CLI | Native Codex plugin or local marketplace | [docs/INSTALL.md](docs/INSTALL.md) |
| Claude Code | Claude plugin marketplace metadata | [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) |
| Cursor | Cursor plugin metadata or direct skills | [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) |
| GitHub Copilot | Source plugin or direct skills | [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) |
| Gemini CLI | Native Gemini extension | [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) |
| OpenCode | OpenCode plugin entrypoint | [.opencode/INSTALL.md](.opencode/INSTALL.md) |
| Pi | Pi extension metadata | [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) |
| Kiro, OpenClaw, other SKILL.md loaders | Direct `SKILL.md` symlinks or copies | [docs/SYMLINKS.md](docs/SYMLINKS.md) |

## Components

| Type | Count | What It Does | Where |
|---|---:|---|---|
| Harness metadata | multiple | Makes the pack visible to plugin-capable harnesses. | `.codex-plugin/`, `.claude-plugin/`, `.cursor-plugin/`, `.agents/plugins/`, `gemini-extension.json`, `.opencode/`, `.pi/`, `package.json` |
| Skills | 79 | Small callable `n-*` behaviors for applying book concepts. | [skills/](skills/) |
| Router | 1 | Routes vague requests to the right primary and secondary skills. | [skills/n-router/SKILL.md](skills/n-router/SKILL.md) |
| Catalog | 1 | Lists every skill with area, use case, and example prompt. | [references/skill-catalog.md](references/skill-catalog.md) |
| Coverage matrix | 1 | Maps book sections to skills so gaps are visible. | [references/coverage-matrix.yaml](references/coverage-matrix.yaml) |
| Workflows | 10 | Reusable scorecards and review protocols. | [references/workflows/](references/workflows/) |
| Memory schemas/templates | 14 | Optional saved-output contracts for reviews, decisions, scorecards, experiments, practices, learnings, and quote notes. | [references/memory/](references/memory/) |
| Chapter summaries | 7 | Paraphrased coverage anchors by book area. | [references/chapter-summaries/](references/chapter-summaries/) |
| Discovery metadata | 1 | Groups the skills for skills.sh-style browsers. | [skills.sh.json](skills.sh.json) |
| Installer | 1 | Updates the local marketplace and/or symlinks skills. | [scripts/install_local.py](scripts/install_local.py) |
| Direct-copy exporter | 1 | Builds a portable `skills/` plus `references/` bundle for SKILL.md-only hosts. | [scripts/export_direct_install.py](scripts/export_direct_install.py) |
| Validators | 3 | Check public structure, skill count, references, coverage, and copied-skill portability. | [scripts/validate_public.py](scripts/validate_public.py), [scripts/check_coverage.py](scripts/check_coverage.py), [scripts/validate_direct_install.py](scripts/validate_direct_install.py) |

## Skill Areas

| Area | Skills | Use For |
|---|---:|---|
| Wealth | 20 | Specific knowledge, accountability, ownership, leverage, work as play, patience, reputation, risk, and freedom. |
| Judgment | 10 | Clear thinking, reality checks, decision rules, mental models, inversion, falsifiability, and learning foundations. |
| Happiness | 9 | Desire, peace, presence, envy, success games, acceptance, habits, and death awareness. |
| Saving Yourself | 15 | Health, exercise, diet, meditation, habit change, systems, anger, expectations, and modern addiction defense. |
| Philosophy | 5 | Meaning, values, rational inner work, long-term wisdom, and present action. |
| Reading | 4 | Reading systems, curricula, formulas, rules, and source trails. |
| Meta | 14 | Routing, setup, memory, coverage, quote safety, daily/weekly reviews, scorecards, coaching, flashcards, and book clubs. |
| Front Matter | 2 | Source fidelity and biographical context. |

## Full Skill Inventory

Every callable skill uses the `n-` prefix so search can find it quickly.

| Skill | Area | Use When |
|---|---|---|
| `n-router` | meta | You want Naval applied but do not know which skill to start with. |
| `n-setup` | meta | You want to configure optional output folders, privacy defaults, and direct-install reference guidance. |
| `n-source-fidelity` | front-matter | You need faithful interpretation, attribution, or a citation-safety check. |
| `n-biographical-context` | front-matter | You want life context for why a principle appears in the book. |
| `n-wealth-map` | wealth | You want an end-to-end wealth strategy. |
| `n-wealth-vs-money-status` | wealth | You need to separate wealth creation from money, approval, prestige, or hierarchy. |
| `n-specific-knowledge` | wealth | You want to identify hard-to-train strengths and authentic edges. |
| `n-authenticity-positioning` | wealth | You want positioning that is natural, rare, and hard to copy. |
| `n-long-term-games` | wealth | You need to evaluate compounding relationships, markets, or work. |
| `n-integrity-partner-filter` | wealth | You need to assess a collaborator or partner. |
| `n-accountability-risk` | wealth | You are deciding whether to put your name or reputation behind something. |
| `n-equity-ownership` | wealth | You want to move from wages toward ownership, IP, assets, or upside. |
| `n-leverage-stack` | wealth | You want to add code, media, capital, labor, brand, distribution, or automation leverage. |
| `n-build-or-sell` | wealth | You are choosing whether to learn building, selling, or both. |
| `n-judgment-compensation` | wealth | You want to become paid for judgment under leverage, not just time. |
| `n-time-value-focus` | wealth | You need to clear the calendar and apply personal hourly-rate thinking. |
| `n-status-game-detector` | wealth | You suspect zero-sum approval, politics, prestige, or comparison is driving behavior. |
| `n-big-life-decisions` | wealth | You are making a job, city, company, partner, or life-direction decision. |
| `n-work-as-play` | wealth | You want work that feels like play to you and work to others. |
| `n-retirement-freedom-design` | wealth | You want a path to freedom through income, low burn, or loved work. |
| `n-luck-engineering` | wealth | You want to increase luck through motion, skill, reputation, and character. |
| `n-reputation-networking` | wealth | You want relationships built through craft and generosity instead of shallow networking. |
| `n-patience-compounding` | wealth | You need to balance urgent action with long-term compounding. |
| `n-risk-of-ruin` | wealth | You need to find legal, health, financial, relationship, or reputation ruin risks. |
| `n-judgment-builder` | judgment | You want better decision quality in leveraged work or life choices. |
| `n-clear-thinking` | judgment | You want confused thinking simplified to basics and plain language. |
| `n-reality-ego-audit` | judgment | You need to see where desire, ego, or fear blocks reality. |
| `n-identity-shedding` | judgment | You want to drop inherited labels, tribes, packages, or stale self-images. |
| `n-decision-rules` | judgment | You want compact decision heuristics applied to a choice. |
| `n-mental-models` | judgment | You want lenses like compounding, incentives, game theory, inversion, or probability. |
| `n-inversion-filter` | judgment | You need to find what fails, what to avoid, and which mistakes matter. |
| `n-falsifiability-truth` | judgment | You need to test whether a claim has predictive power. |
| `n-foundational-learning` | judgment | You want foundations in math, science, economics, persuasion, or learning. |
| `n-reading-system` | judgment | You want curiosity-led reading habits, rereading, skimming, and dropping weak books. |
| `n-happiness-baseline` | happiness | You want to train happiness as a baseline. |
| `n-desire-audit` | happiness | You need to identify a desire creating suffering. |
| `n-presence-practice` | happiness | You need to reduce rumination and return attention to present reality. |
| `n-peace-over-joy` | happiness | You want stable peace instead of stimulation or mood chasing. |
| `n-success-game-exit` | happiness | You may have outgrown a game with large rewards. |
| `n-envy-antidote` | happiness | You want to dissolve jealousy, comparison, or external scorecards. |
| `n-happiness-habits` | happiness | You want daily habits that support mood stability and happiness. |
| `n-accept-change-leave` | happiness | You need to choose acceptance, change, or exit. |
| `n-death-awareness` | happiness | You want mortality to clarify priorities and reduce ego battles. |
| `n-self-responsibility` | saving-yourself | You are outsourcing responsibility to gurus, mentors, doctors, teachers, or tools. |
| `n-be-yourself` | saving-yourself | You want original contribution instead of copying others. |
| `n-health-first` | saving-yourself | You need to reorder life around physical, mental, and spiritual health. |
| `n-diet-simplifier` | saving-yourself | You want to subtract processed food and appetite traps. |
| `n-exercise-priority` | saving-yourself | You need daily exercise to become non-negotiable. |
| `n-meditation-system` | saving-yourself | You want a practical awareness, sitting, walking, or journaling protocol. |
| `n-mental-debugging` | saving-yourself | You want to observe thoughts, reactions, fear, desire, and ego as processes. |
| `n-habit-change` | saving-yourself | You want triggers, substitutes, tracking, and commitment for habit change. |
| `n-systems-not-goals` | saving-yourself | You want to turn a goal into an environment or system. |
| `n-grow-yourself` | saving-yourself | You want self-change through self-image, learning, and readiness. |
| `n-freedom-from-expectations` | saving-yourself | You need boundaries around obligations and others' imagined claims. |
| `n-anger-release` | saving-yourself | You want a cleaner response to anger. |
| `n-employment-freedom` | saving-yourself | You want to reduce dependence on employment. |
| `n-uncontrolled-thinking` | saving-yourself | You want the mind to become a tool instead of the master. |
| `n-modern-addiction-defense` | saving-yourself | You need to audit screens, news, processed food, games, porn, stimulants, or dopamine traps. |
| `n-meaning-maker` | philosophy | You want to explore personal meaning without borrowing a universal answer. |
| `n-values-filter` | philosophy | You need to check honesty, long-term thinking, peer relationships, anger, or freedom. |
| `n-rational-buddhism` | philosophy | You want testable inner work without unverifiable claims as operating truth. |
| `n-wisdom-long-term` | philosophy | You want to evaluate long-term consequences. |
| `n-present-moment` | philosophy | You need to return to the present and act on perishable inspiration. |
| `n-reading-curriculum` | reading | You want book paths across science, mental models, philosophy, economics, and fiction. |
| `n-life-formulas` | reading | You want formula-style framing for health, wealth, happiness, income, or learning. |
| `n-rules` | reading | You want compact rules as reminders, not substitutes for reasoning. |
| `n-next-sources` | reading | You want deeper Naval resources and source trails. |
| `n-coverage-auditor` | meta | You want to check whether the plugin missed a major book section. |
| `n-principle-to-action` | meta | You want to turn a principle into an experiment, behavior, or operating rule. |
| `n-save-learning` | meta | You want to save 1-3 approved reusable insights from a completed Naval session. |
| `n-memory-refresh` | meta | You want to review saved Naval memory for stale, duplicate, contradictory, or low-value entries. |
| `n-daily-review` | meta | You want a daily health, work, desire, focus, and freedom review. |
| `n-weekly-compound-review` | meta | You want a weekly review across wealth, judgment, health, happiness, relationships, and values. |
| `n-opportunity-scorecard` | meta | You want to score a job, startup, product, project, content idea, or investment. |
| `n-relationship-scorecard` | meta | You want to score collaborators, friends, partners, or teams for long-term fit. |
| `n-quote-safety` | meta | You want quotations kept short, attributed, and compliant. |
| `n-socratic-coach` | meta | You want questions before advice. |
| `n-flashcards` | meta | You want recall prompts, reflection cards, or spaced repetition items. |
| `n-book-club` | meta | You want a chapter discussion, exercise, or reading reflection. |

## Common Prompts

| Prompt | Start With | Good Output Shape |
|---|---|---|
| "Use Naval to analyze this career decision." | `n-router` | Route, first question, decision scorecard, next action. |
| "Build me a Naval-style wealth plan." | `n-wealth-map` | Wealth map, leverage stack, ownership moves, patient experiments. |
| "Help me identify my specific knowledge." | `n-specific-knowledge` | Strength inventory, obsession map, marketable edge, practice loop. |
| "Apply Naval's decision rules to this choice." | `n-decision-rules` | One-way/two-way door check, inversion, long-term consequences. |
| "What desire is making me unhappy?" | `n-desire-audit` | Desire, cost, root, accept/change/leave path, replacement practice. |
| "Run my weekly compound review." | `n-weekly-compound-review` | Review table, compounding wins, leaks, next week constraints. |
| "Set up Naval memory for this repo." | `n-setup` | Storage mode, privacy default, config draft, folder plan. |
| "Save what we learned from this Naval session." | `n-save-learning` | 1-3 approved learnings with YAML frontmatter. |
| "Refresh my saved Naval learnings." | `n-memory-refresh` | Keep/update/merge/delete recommendations. |
| "Build me a Naval reading curriculum." | `n-reading-curriculum` | Reading path, sequence, reread list, drop criteria. |

## Install Paths

| Path | Use When | Command |
|---|---|---|
| Codex plugin | You want the plugin visible as `naval` in Codex. | `python3 scripts/install_local.py --marketplace` |
| Direct skill symlinks | Your agent scans `SKILL.md` folders directly. | `python3 scripts/install_local.py --symlink-skills` |
| Both | You use multiple local agents and want one source of truth. | `python3 scripts/install_local.py --marketplace --symlink-skills` |
| Dry run | You want to inspect changes before writing. | `python3 scripts/install_local.py --marketplace --symlink-skills --dry-run` |

See [docs/INSTALL.md](docs/INSTALL.md) and [docs/SYMLINKS.md](docs/SYMLINKS.md) for full install details.

## How It Fits Together

| Question | Answer |
|---|---|
| Is this a plugin or skills? | Both. The plugin is the installable package; the `n-*` skills are the callable units. |
| Why not one giant skill? | Smaller skills route better, load less context, and make each workflow easier to inspect. |
| Why `n-`? | It makes every skill searchable by a short namespace. |
| Where is the full list? | [references/skill-catalog.md](references/skill-catalog.md) is the canonical catalog. |
| How do I check coverage? | Run `python3 scripts/check_coverage.py` or call `n-coverage-auditor`. |
| Where do saved outputs go? | Run `n-setup`; by default memory is off, and project-local memory uses `docs/naval/`. |
| Do copied skills need references? | Yes. Use `npm run export:direct` or copy `skills/n-*` and the sibling `references/` folder together; validate with `python3 scripts/validate_direct_install.py --agent-root <agent-root>`. |
| Can I use exact quotes? | Use `n-quote-safety`; prefer paraphrase and short attributed excerpts. |

## Documentation

| Document | What It Covers |
|---|---|
| [docs/AUDIT.md](docs/AUDIT.md) | Reference-project audit and adopted patterns. |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Detailed example prompts, skill routes, and output shapes. |
| [docs/HARNESS_SUPPORT.md](docs/HARNESS_SUPPORT.md) | Claude, Codex, Cursor, Copilot, Gemini, OpenCode, Pi, Kiro, and direct skill install paths. |
| [docs/INSTALL.md](docs/INSTALL.md) | Plugin install, local marketplace, updates, validation, and custom paths. |
| [docs/NAVAL_MEMORY.md](docs/NAVAL_MEMORY.md) | Optional memory setup, privacy contract, folders, schemas, and direct-copy reference layout. |
| [docs/SYMLINKS.md](docs/SYMLINKS.md) | How direct `n-*` skill symlinks work across agent homes. |
| [docs/PLUGIN_REFERENCE.md](docs/PLUGIN_REFERENCE.md) | Architecture, component map, and plugin-vs-skill tradeoffs. |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Regeneration, validation, adding skills, and public repo boundaries. |
| [docs/SOURCE_BOUNDARIES.md](docs/SOURCE_BOUNDARIES.md) | Copyright, attribution, and source-use boundaries. |

## Local Development

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
```

Build a direct-copy bundle for SKILL.md-only hosts:

```bash
npm run export:direct
python3 scripts/validate_direct_install.py --agent-root dist/naval-direct-install
```

If you have Codex's local validation helpers:

```bash
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
for d in skills/n-*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
```

Regenerate generated skill and reference files:

```bash
python3 scripts/build_naval_pack.py
```

## Limitations

- This is an unofficial skill pack, not an official edition of the book.
- It does not include the full book text.
- It keeps saved memory opt-in; local `.naval/*.local.yaml` config files should not be committed.
- It should not be used as legal, medical, financial, or mental-health advice.
- Exact quotation work should use `n-quote-safety` and, when needed, verification against an authorized source.

## Inspirations

This repository borrows structural ideas from public skill and plugin projects while keeping the Naval content original and paraphrased:

- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [EveryInc/compound-knowledge-plugin](https://github.com/EveryInc/compound-knowledge-plugin)
- [mattpocock/skills](https://github.com/mattpocock/skills)
- [steipete/agent-scripts](https://github.com/steipete/agent-scripts)

## Source Boundaries

This repository contains paraphrased operating knowledge, skill workflows, and coverage maps. It does not include the full text of *The Almanack of Naval Ravikant*.

The original book is by Eric Jorgenson and is available from Navalmanack.com. This project is not affiliated with Naval Ravikant, Eric Jorgenson, Navalmanack, or any publisher.

## License

MIT for the code, generated skill scaffolding, and original documentation in this repository. See [LICENSE](LICENSE).
