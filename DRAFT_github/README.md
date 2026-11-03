# DRAFT_github/ — staged `.github/` content (NOT active)

This folder holds the files that the AI-EWA pack (`docs/DRAFT_AI-EWA_pakiet_wdrozeniowy_2026-11-03.md`, section 4) proposes for `.github/`:
Discussion forms (`DISCUSSION_TEMPLATE/`), Issue forms (`ISSUE_TEMPLATE/`), `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`, `labels.yml` and workflows (`workflows/validate.yml`, `workflows/scorecard.yml`).

They are staged here on purpose, because of the freeze rule (until ~2026-11-08): no merge, no push to main, no tags, no workflows and no changes in `.github/` without Ewa's word. Files in this folder are inert: GitHub does not read templates, CODEOWNERS or workflows from here, so nothing runs.

## Conditions before moving to `.github/`
1. Explicit approval from Ewa (owner), recorded in `governance/decision-log.md`.
2. After the freeze ends (~2026-11-08).
3. Every `uses: ...@PIN` in `workflows/*.yml` is replaced with a full 40-character commit SHA (the pack's `scripts/bootstrap_repo.sh` does this; it has NOT been run). Until then `tools/validate_repo.py` fails on purpose.
4. Placeholders `OWNER_HANDLE` / `MAINTAINER_HANDLE` in `CODEOWNERS` are replaced with real GitHub handles.

Move with `git mv DRAFT_github/<path> .github/<path>` (same substructure), in a separate reviewed PR.
