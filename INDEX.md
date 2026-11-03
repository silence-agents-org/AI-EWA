# INDEX — AI-EWA repository map

Status: DRAFT map written during the repo tidy of 2026-11-03 (after PRs #1, #2 and #3 were merged into `main` at `3a7a4c4`). Nothing in this file changes any rule; it only says where things are and which copy is canonical.

Copyright holder: **Ewa Tchórzewska** (natural person). See `NOTICE` ("All rights reserved"). No licence has been adopted yet: `RIGHTS.md`, `CLA.md`, `CITATION.cff` licence notes and the `license` hints in packaging are drafts, not legal advice, not adopted. `LICENSE`, `LICENSE-DOCS` and `LICENSE-DATA` referenced in `RIGHTS.md` do not exist.

Unverified external claims (papers, arXiv IDs, laws, court cases, funders, programmes, platform rules) are marked `[BRAK DOWODU]` ("no evidence yet").

## Why there are duplicates
PR #2 (`draft/ai-ewa-lab-pack-2026-11-03`) added the lab pack at the repository root and `DRAFT_github/`. PR #3 (`agent/2026-11-03-lab-package-ah17-evidence`) added the same pack again under `proposals/2026-11-03-lab-package/` plus `research/ah17-evidence/`. Most pairs are byte-identical. **Canonical = the root copy** (paths that `tools/validate_repo.py`, `CITATION.cff` and the docs expect). The `proposals/2026-11-03-lab-package/` copies are **superseded** and carry a header "SUPERSEDED by <path> — kept pending owner decision" where the file format allows it. Nothing was deleted or moved.

## Layout

| Path | What it is | Status |
|---|---|---|
| `README.md` | Main README (English + Polish owner sections) | Canonical. Mixed-language after merge; consolidation proposed |
| `README.pl.md` | Polish README | Canonical (Polish by design) |
| `INDEX.md` | This map | Canonical |
| `NOTICE` | Copyright notice: Ewa Tchórzewska, all rights reserved | Canonical |
| `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `GOVERNANCE.md`, `SECURITY.md` | Lab rules (drafts) | Canonical |
| `RIGHTS.md`, `CLA.md` | Rights/CLA drafts — not legal advice, not adopted | Canonical draft (agents may not edit, `AGENTS.md` rule 7) |
| `CITATION.cff` | Citation metadata | Canonical; licence field commented out until adopted |
| `governance/` | `decision-log.md` (append-only), `run_budget.yaml` | Canonical (agents may not edit) |
| `protocols/` | `TRUST-01.md`, `PERSONA-01.md`, `DEBATE-01.md` pre-registrations (PROPOSED) | Canonical |
| `harness/TRUST_01/` | TRUST-01 harness, rule-based tests only; no LLM run executed, no results | Canonical |
| `research/` | `claims.yaml` + schema, `predictions.jsonl` + schema (`forecaster_id: demo` = synthetic), `replications/TEMPLATE.md` | Canonical |
| `research/ah17-evidence/` | AH17-EVIDENCE dataset card (DRAFT, not released, no licence, nothing on Hugging Face) and protocol fragments | Canonical (only copy; Polish) |
| `reports/TEMPLATE.md` | Report template | Canonical |
| `tools/` | `validate_repo.py`, `score_predictions.py` | Canonical |
| `scripts/bootstrap_repo.sh` | Repo-settings bootstrap — **PROPOSAL ONLY, do not run** | Canonical proposal, owner decision required |
| `DRAFT_github/` | Inactive staging of future `.github/` content (`@PIN` placeholders) | Canonical staging; nothing active |
| `agents/` | `registry.schema.json`, `examples/example-agent.yaml` (`agents/cards/` not created yet) | Canonical |
| `decisions/2026-11-03_AI-EWA_laboratorium_plan.pl.md` | Owner's lab plan (Polish, reconstructed from notes, not verified word-for-word) | Canonical record |
| `docs/DRAFT_AI-EWA_pakiet_wdrozeniowy_2026-11-03.md` | Source document of the lab pack (Polish); its inline file copies are superseded by the root files | Archival source |
| `proposals/2026-11-03-lab-package/` | Second copy of the lab pack (PR #3) | **Superseded** — see table below |

## Overlap table (PR #2 root copy ↔ PR #3 `proposals/2026-11-03-lab-package/` copy)

| Root (canonical) | Superseded copy | Comparison |
|---|---|---|
| `AGENTS.md`, `CITATION.cff`, `CLA.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `RIGHTS.md`, `SECURITY.md` | same names under `proposals/…/` | Identical at merge |
| `README.pl.md` | `proposals/…/README.pl.proposed.md` | Identical |
| `README.md` | `proposals/…/README.proposed.md` | Proposal is a clean English README (35 lines); root is a 269-line mixed EN/PL merge result. Root kept canonical; use the proposal as a base for consolidation |
| `DRAFT_github/README.md` | `proposals/…/README.md` | Different purpose: staging conditions vs. package status notes; both superseded in scope by this `INDEX.md` for layout |
| `DRAFT_github/**` (`*.yml`) | `proposals/…/github/**` (`workflows/*.yml.proposed`) | Identical content; proposal only adds `.proposed` suffix to workflows |
| `protocols/*.md` | `proposals/…/protocols/*.md` | Identical except the proposal already had `[BRAK DOWODU]` marks in DEBATE-01; marks now ported to root |
| `research/claims.yaml` | `proposals/…/research/claims.yaml` | Same; proposal had `[BRAK DOWODU]` marks, now ported to root |
| `research/*.schema.json`, `research/predictions.jsonl`, `research/replications/TEMPLATE.md`, `reports/TEMPLATE.md`, `agents/**`, `governance/**` | same under `proposals/…/` | Identical |
| `harness/TRUST_01/**` | `proposals/…/harness/TRUST_01/**` | Code identical except PEP 8 blank lines in the proposal; both pass the same 8 tests |
| `tools/*.py` | `proposals/…/tools/*.py` | Identical except PEP 8 blank lines |
| `scripts/bootstrap_repo.sh` | `proposals/…/scripts/bootstrap_repo.sh` | Different: root changes repo settings, Actions permissions, private vulnerability reporting, creates a ruleset, labels and pins actions; proposal only creates labels. Neither may run without the owner |

Superseded files without an inline header (format or rules do not allow one): `proposals/…/research/predictions.jsonl` (a header line would break JSONL), `proposals/…/RIGHTS.md`, `proposals/…/CLA.md`, `proposals/…/governance/**`, `proposals/…/github/**` (legal/governance/`.github` content that agents do not edit). They are superseded by the root/`DRAFT_github/` paths listed above.

## Planned paths referenced but not yet created
`agents/cards/`, `governance/cla-signatures.md`, `LICENSE`, `LICENSE-DOCS`, `LICENSE-DATA`, `.github/**` (staged in `DRAFT_github/`), and for AH17-EVIDENCE: `provenance/sources.jsonl`, `provenance/rights_manifest.jsonl`, `annotation_guidelines.md`, `reports/agreement_report.md`, `reports/error_analysis.md`.
