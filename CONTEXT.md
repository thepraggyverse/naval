# Naval Skills Context

Shared vocabulary for this repository. This is contributor context, not a source text from the book.

## Terms

**Plugin**

The installable package named `naval`. It contains manifests, skills, references, docs, and scripts.

**Skill**

A folder under `skills/n-*` with a `SKILL.md` file. Each skill gives an agent a focused way to apply one Naval-related idea or workflow.

**n-prefix**

The `n-` namespace used by every callable skill. It makes search easier and avoids generic names like `wealth` or `reading`.

**Router**

`n-router`, the skill that chooses a primary skill and optional secondary skills when the user says "use Naval" or describes a vague situation.

**Reference**

A source-safe file under `references/` that supports skills without pasting long book excerpts into skill bodies.

**Memory layer**

Optional saved Naval output configured by `n-setup`. It is off by default and can write approved reviews, decisions, scorecards, experiments, practices, learnings, or quote notes to a project-local or personal notes folder.

**Local memory config**

`.naval/config.local.yaml`, usually created from `.naval/config.local.example.yaml`. This file is private, ignored by git, and controls whether memory is enabled.

**Direct-copy install**

A harness setup that copies `skills/n-*` folders instead of symlinking them. These installs must also copy the sibling `references/` folder so `../../references/...` paths keep resolving.

**Workflow**

A reusable practical format such as an opportunity scorecard, desire audit, meditation protocol, daily review, or weekly review.

**Coverage matrix**

`references/coverage-matrix.yaml`, the map that connects major book areas to skills and references so omissions are visible.

**Source boundary**

The rule that this repository uses paraphrase, operating knowledge, and short attribution guidance rather than reproducing the book text.

## Avoided Phrases

- Avoid calling the plugin an "operating system" in public docs.
- Avoid presenting it as official, authorized, or affiliated.
- Avoid vague descriptions like "helps with Naval things." Say what the skills do.
