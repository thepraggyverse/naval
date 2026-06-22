# Naval

`naval` is a Codex plugin that turns *The Almanack of Naval Ravikant* into a searchable set of `n-` prefixed skills.

It is not a quote dump and it does not include the full book text. It is an operating system for applying the book's major ideas to decisions, audits, experiments, reviews, and daily practice.

## What You Get

- 76 `n-*` skills for wealth, judgment, happiness, health, values, reading, and life-review workflows.
- A router skill, `n-router`, for vague "use Naval on this" requests.
- A browsable catalog at `references/skill-catalog.md`.
- A coverage matrix at `references/coverage-matrix.yaml` that maps book sections to skills.
- Practical workflows for wealth scorecards, decision scorecards, desire audits, meditation, reading paths, daily reviews, and weekly compound reviews.
- Validation scripts that check coverage, broken references, skill metadata, and public repo structure.

## Quick Start

Clone the repo:

```bash
git clone https://github.com/thepraggyverse/naval.git ~/plugins/naval
cd ~/plugins/naval
```

Validate it:

```bash
python3 scripts/validate_public.py
```

Register it with the default personal Codex marketplace:

```bash
python3 scripts/install_local.py --marketplace
```

Optionally symlink the skills into local agent homes:

```bash
python3 scripts/install_local.py --symlink-skills
```

For all supported local homes:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
```

## How To Use

Search for `n-` in your agent or Codex skill picker.

Useful starting points:

| Prompt | Skill |
|---|---|
| "Use Naval to analyze this career decision." | `n-router` |
| "Build me a Naval-style wealth plan." | `n-wealth-map` |
| "Help me identify my specific knowledge." | `n-specific-knowledge` |
| "Apply Naval's decision rules to this choice." | `n-decision-rules` |
| "What desire is making me unhappy?" | `n-desire-audit` |
| "Run my weekly compound review." | `n-weekly-compound-review` |
| "Build me a Naval reading curriculum." | `n-reading-curriculum` |

For the full list, see [`references/skill-catalog.md`](references/skill-catalog.md).

## Installation Details

See:

- [`docs/INSTALL.md`](docs/INSTALL.md) for plugin installation.
- [`docs/SYMLINKS.md`](docs/SYMLINKS.md) for multi-agent skill-home symlinks.
- [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) for regeneration and validation.
- [`docs/SOURCE_BOUNDARIES.md`](docs/SOURCE_BOUNDARIES.md) for copyright and source-use boundaries.

## Repository Layout

```text
naval/
  .codex-plugin/plugin.json
  skills/
    n-router/
    n-wealth-map/
    n-specific-knowledge/
    ...
  references/
    book-map.md
    skill-catalog.md
    router-guide.md
    coverage-matrix.yaml
    chapter-summaries/
    workflows/
  scripts/
    build_naval_pack.py
    check_coverage.py
    install_local.py
    validate_public.py
```

## Design Principles

This pack follows a few patterns from the shared skill/plugin ecosystem:

- Small, composable skills rather than one giant mega-skill.
- A router for ambiguous requests.
- References and workflows loaded only when needed.
- Validation scripts that make drift visible.
- Public install docs that explain both plugin registration and direct skill symlinks.

Inspirations:

- [mattpocock/skills](https://github.com/mattpocock/skills)
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [EveryInc/compound-knowledge-plugin](https://github.com/EveryInc/compound-knowledge-plugin)
- [steipete/agent-scripts](https://github.com/steipete/agent-scripts)

## Source Boundaries

This repository contains paraphrased operating knowledge, skill workflows, and coverage maps. It does not include the full text of *The Almanack of Naval Ravikant*.

The original book is by Eric Jorgenson and is available from Navalmanack.com. This project is not affiliated with Naval Ravikant, Eric Jorgenson, Navalmanack, or any publisher.

## License

MIT for the code, generated skill scaffolding, and original documentation in this repository. See [`LICENSE`](LICENSE).
