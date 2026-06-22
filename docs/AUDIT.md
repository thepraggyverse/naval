# Reference Audit

This audit records what was checked before expanding `naval` beyond the original Codex-only plugin shape.

## Sources Audited

| Source | What Was Useful |
|---|---|
| [Every guide: Compound Engineering](https://every.to/guides/compound-engineering) | Clear philosophy, loop, what is in the plugin, installation by harness, where things live, core commands, update guidance. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Multi-harness manifests, `AGENTS.md`, `CLAUDE.md` shim, `GEMINI.md`, `PRIVACY.md`, `SECURITY.md`, OpenCode/Pi/Gemini packaging, update sections, local development instructions. |
| [EveryInc/compound-knowledge-plugin](https://github.com/EveryInc/compound-knowledge-plugin) | Small loop-driven plugin shape, components table, local-first knowledge wording, `AGENTS.md`, privacy/security docs. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Plain explanation of why skills exist, user-invoked vs model-invoked framing, `CONTEXT.md`, simple symlink scripts, skills grouped by audience. |
| [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | Shared agent instructions, `skills.sh.json`, terse skill routing descriptions, direct symlink strategy, portable validation. |

## What Naval Was Missing

| Gap | Adopted Change |
|---|---|
| Public repo instructions | Added `AGENTS.md`, `CLAUDE.md`, and `CONTEXT.md`. |
| Plain public explanation | Rewrote README header and intro around what the skills do. |
| Unofficial status | Added "Unofficial" to public title, manifest display name, and descriptions. |
| Multi-harness metadata | Added `.claude-plugin/`, `.cursor-plugin/`, `.agents/plugins/`, `gemini-extension.json`, `.opencode/`, `.pi/`, and `package.json`. |
| Harness install/update docs | Added `docs/HARNESS_SUPPORT.md` and expanded `docs/INSTALL.md`. |
| Skills.sh-style grouping | Added `skills.sh.json`. |
| Privacy/security docs | Added `PRIVACY.md` and `SECURITY.md`. |
| Release/history surface | Added `CHANGELOG.md`. |
| Broader direct skill targets | Expanded default symlink homes for Copilot, Cursor, Gemini, and OpenCode. |
| CI coverage for new files | Updated `scripts/validate_public.py` to check the new files and metadata. |
| No setup skill | Added `n-setup` plus `.naval/config.local.example.yaml` and `docs/NAVAL_MEMORY.md`. |
| No compound/save skill | Added `n-save-learning` for approved reusable learnings. |
| No memory refresh skill | Added `n-memory-refresh` for stale, duplicate, contradictory, or low-value saved guidance. |
| Direct-copy reference risk | Added `scripts/export_direct_install.py`, direct-copy install docs, and `scripts/validate_direct_install.py`. |

## Patterns Adopted

| Pattern | Naval Version |
|---|---|
| Loop first | `n-router -> focused skill -> scorecard/practice/action -> review -> fidelity/safety`. |
| What is in the box | README components table plus plugin reference. |
| Core commands | README core workflows plus `docs/PLUGIN_REFERENCE.md` command table. |
| Where things live | `docs/PLUGIN_REFERENCE.md` names source checkout, marketplace file, and skill homes. |
| Multi-harness support | Native manifests where possible, direct `SKILL.md` symlinks/copies everywhere else. |
| Source-safe public boundary | `docs/SOURCE_BOUNDARIES.md`, `n-source-fidelity`, and `n-quote-safety`. |
| Optional durable memory | `n-setup` keeps persistence off by default, then `n-save-learning` and review skills can save approved markdown artifacts. |
| Copied-skill portability | `npm run export:direct` builds a sibling `skills/` plus `references/` bundle; validation checks both simulated and real exported layouts. |

## Patterns Not Adopted

| Pattern | Reason |
|---|---|
| Standalone review/research agents | Naval skills are mostly advice/review workflows and do not need separate worker agents yet. |
| A TypeScript converter CLI | Too much machinery for this 79-skill pack. Direct manifests, generation scripts, and symlink support are enough for now. |
| Automatic project-local durable output folders | Naval should not create `docs/knowledge/`, `plans/`, or journals automatically. Durable output is opt-in through `n-setup`. |
| Long quote database | Copyright risk and unnecessary for skill operation. The pack stays paraphrase-first. |

## Follow-Up Ideas

| Idea | Why It Could Help |
|---|---|
| Add a generated `docs/skills/*.md` page per skill | Better browsing for users who do not want to open `SKILL.md` files. |
| Add a smoke-test script for live symlink installs | Direct-copy export and validation are covered; a live symlink smoke test could still confirm default homes and collision handling across machines. |
| Add release tags once the package stabilizes | Makes pinned installs easier for OpenCode, Gemini, Pi, and plugin managers. |
| Add screenshots or short demo transcripts | Makes the GitHub page easier to evaluate quickly. |

## 2026-06-22 OSS Readiness Re-Audit

After adding the memory layer, the public docs were checked again against the Every guide, `EveryInc/compound-engineering-plugin`, `EveryInc/compound-knowledge-plugin`, `mattpocock/skills`, and `steipete/agent-scripts`.

| Rechecked Area | Result |
|---|---|
| Root repo docs | Present: `README.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CONTEXT.md`, `CHANGELOG.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, license, and validation workflow. |
| Install docs | Present and expanded for Codex CLI enablement with `codex plugin add naval@personal --json`, plus direct skills and direct-copy bundle paths. |
| Update docs | Present in `docs/INSTALL.md`, `docs/HARNESS_SUPPORT.md`, and `docs/DEVELOPMENT.md`; local installs rerun marketplace/symlink installer and refresh plugin cache. |
| Durable memory docs | Present: `n-setup`, `docs/NAVAL_MEMORY.md`, `.naval/config.local.example.yaml`, gitignore guidance, schemas, and templates. |
| Direct-copy portability | Present: `npm run export:direct` creates a sibling `skills/` plus `references/` agent root, and `scripts/validate_direct_install.py --agent-root <agent-root>` validates copied installs. |
| Live Codex load path | Documented: register with `scripts/install_local.py --marketplace`, enable with `codex plugin add naval@personal --json`, then smoke with `codex exec` and `$n-setup`. |
| Remaining gap | No release tag yet. That is intentionally a publishing step after the first GitHub push. |
