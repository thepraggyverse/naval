# Changelog

## Unreleased

- Tightened generated `n-*` skill descriptions so model-invoked routing is shorter and more predictable.
- Added `scripts/audit_skill_quality.py` and `npm run audit:skills` to check description length, trigger shape, direct-copy fallbacks, reference pointers, and checkable output artifacts.
- Added the skill quality audit to `npm run validate` and GitHub Actions.
- Added `docs/SKILL_QUALITY.md` and linked it from README, development docs, and plugin reference docs.

## 0.1.0 - 2026-06-22

- Initial public release of the unofficial `naval` plugin and `n-*` skill pack.
- Added 79 skills for wealth, judgment, happiness, health, values, reading, decisions, scorecards, reviews, optional memory setup, source fidelity, and quote safety.
- Added `n-setup`, `n-save-learning`, `n-memory-refresh`, memory schemas/templates, direct-copy bundle export, and direct-copy install validation.
- Added Codex plugin metadata, local marketplace installer, direct skill symlink installer, coverage checks, public validation, and GitHub Actions validation.
- Added cross-harness metadata for Claude Code, Cursor, Gemini CLI, OpenCode, Pi, and skills.sh-style discovery.
- Added public install, examples, plugin reference, source boundary, privacy, security, and contributor docs.
- Documented Codex CLI enablement with `codex plugin add naval@personal --json` and a live `$n-setup` smoke test.
- Hardened direct-copy export with a generated-bundle marker so `--force` cannot delete arbitrary user directories.
- Added guidance to prefer the native Codex plugin for Codex-only use and target direct symlinks to the harness homes that need them.
- Added generated per-skill docs, an install smoke script, and a release checklist for tag/publish flow.
