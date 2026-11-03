# DRAFT_github/ — staged `.github/` content — **NOT ACTIVE**

> **NOT ACTIVE · NOTHING PAID · REQUIRES EWA'S DECISION.**
> Nothing in this folder runs or takes effect. GitHub reads Actions workflows, Discussion/Issue forms, the PR template and `CODEOWNERS` only from `.github/` (CODEOWNERS also from the root or `docs/`), never from `DRAFT_github/`. There is **no `.github/` directory** in this repository and no workflow is active.
> Ewa's standing rules apply: no workflows, no `.github/**` changes and nothing paid on GitHub without her explicit word. This folder is an inert proposal kept for her decision (status: PROPOSAL, source: PR #2; see `docs/INDEX.md`).

This folder holds the files that the AI-EWA pack (`docs/DRAFT_AI-EWA_pakiet_wdrozeniowy_2026-11-03.md`, section 4) proposes for `.github/`:
Discussion forms (`DISCUSSION_TEMPLATE/`), Issue forms (`ISSUE_TEMPLATE/`), `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`, `labels.yml` and workflows (`workflows/validate.yml`, `workflows/scorecard.yml`).
A duplicate of the same proposal exists under `proposals/2026-11-03-lab-package/github/` (SUPERSEDED; canonical = this folder).

They are staged here on purpose, because of the freeze rule (until ~2026-11-08): no merge, no push to main, no tags, no workflows and no changes in `.github/` without Ewa's word. Files in this folder are inert: GitHub does not read templates, CODEOWNERS or workflows from here, so nothing runs.

## Conditions before anything moves to `.github/` (all required)
1. Explicit decision by Ewa (owner, `@ev-silence-owner`), recorded in `governance/decision-log.md`.
2. After the freeze ends (~2026-11-08).
3. Confirmation that it costs nothing (public repo, free plan; no paid features, no paid runners, no paid API calls).
4. Every `uses: ...@PIN` in `workflows/*.yml` is replaced with a full 40-character commit SHA. `tools/validate_repo.py` checks only `.github/`, so it passes today; once files are moved there it must pass too (it rejects privileged triggers and actions not pinned to a SHA). (`scripts/bootstrap_repo.sh` can do it — it has NOT been run — but it also changes repository settings — **DO NOT RUN** it without Ewa's explicit decision.)
5. Discussion categories with matching slugs are created by hand in the GitHub UI (only Ewa can decide this).

Placeholders `OWNER_HANDLE` / `MAINTAINER_HANDLE` in `CODEOWNERS` were replaced with the real handle `@ev-silence-owner` (2026-11-03).

Moving would be done with `git mv DRAFT_github/<path> .github/<path>` (same substructure), in a separate PR reviewed and merged by Ewa.
