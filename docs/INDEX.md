# INDEX — AI-EWA repository map and status

This map says where things are, which copy is canonical and what is in force. It changes no rule by itself. Rules in force are in [`README.pl.md`](../README.pl.md) (authoritative) and summarised in [`README.md`](../README.md).

## History note (2026-11-03)
- PRs **#2**, **#3** and **#1** were merged into `main` by Ewa (account `ev-silence-owner`) on 2026-11-03 between 10:53 and 10:56 (UTC+1), in that order (merge commits `d58e2ca`, `40613d9`, `3a7a4c4`). The titles of #2 and #3 still start with "DRAFT:" — titles of merged PRs cannot be changed, so this note records that **the merge does not turn their content into rules**.
- The merge of #1 (`3ecdc15`) lost the body of Ewa's rights rule (`917b1ae`) and mixed English sections into the Polish README; the cleanup PR (branch `fix/post-merge-cleanup-2026-11-03`) restored it. It also folded in the correct parts of draft PRs #4 and #5 (without LICENSE files).
- **In force (ACTIVE):** Ewa's standing rules ("Zasady stałe Ewy") and the rights rule "Zasada: nie przejmujemy cudzych praw" in `README.pl.md` (decision of 2026-11-03), `NOTICE`, `RIGHTS.md` section 0, this map.
- **Proposal:** everything from the AI-EWA lab pack (#2/#3): lab rules, CLA, licences, protocols, harness, schemas, tools, `DRAFT_github/`, bootstrap script. Nothing runs automatically; no GitHub Actions; nothing paid. A proposal becomes binding only by Ewa's decision recorded in `governance/decision-log.md`.
- **Licence:** not chosen (owner's decision pending). No `LICENSE*` files exist. Default copyright applies: each author retains the rights to their own work.

Unverified external claims (papers, arXiv IDs, laws, court cases, funders, programmes, platform rules) are marked `[BRAK DOWODU]`.

## Status legend
**ACTIVE** — in force · **PROPOSAL** — merged for discussion, not binding · **DRAFT** — unfinished or unverified record · **SUPERSEDED** — duplicate kept (not deleted: deletion only on Ewa's order); the canonical path is named in its header.

## Layout

| Path | What it is | Status | Source PR |
|---|---|---|---|
| `README.pl.md` | Authoritative Polish README: Ewa's standing rules, rights rule, licence status, "Jak pracujemy" | **ACTIVE** (rules); workflow = target | initial commits `9e93bbc`, `917b1ae`; #1; cleanup PR |
| `README.md` | English entry point; summary of the rules + lab overview; links to `README.pl.md` | **ACTIVE** (as a summary; Polish prevails) | #2, #1, #4 (rules), cleanup PR |
| `docs/INDEX.md` | This map | **ACTIVE** | #5 (as `INDEX.md`), cleanup PR |
| `NOTICE` | Ewa's materials are hers; outside contributions belong to their authors; licence pending | **ACTIVE** | #2, cleanup PR |
| `RIGHTS.md` | Section 0 = rights rule (in force); sections 1–5 = draft, proposed licence table | **ACTIVE** §0 / **DRAFT** rest | #2, cleanup PR |
| `CLA.md` | Template: non-exclusive licence, never an assignment; needs a lawyer's review; do not sign | **DRAFT** | #2, cleanup PR |
| `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `GOVERNANCE.md`, `SECURITY.md` | Lab rules; points restating Ewa's standing rules are in force | **PROPOSAL** (standing-rule points **ACTIVE**) | #2, cleanup PR |
| `CITATION.cff` | Citation metadata; licence field commented out | **PROPOSAL** | #2, #5 |
| `governance/` | `decision-log.md` (append-only), `run_budget.yaml` (proposed caps; paid budget = 0 until Ewa decides) | **PROPOSAL** | #2, cleanup PR |
| `protocols/` | `TRUST-01.md`, `PERSONA-01.md`, `DEBATE-01.md` pre-registrations; nothing run | **PROPOSAL** | #2, #5 |
| `harness/TRUST_01/` | TRUST-01 harness; rule-based tests only; paid LLM calls off by default; no LLM run, no results | **PROPOSAL** | #2, cleanup PR |
| `research/` | `claims.yaml` + schema, `predictions.jsonl` + schema (`forecaster_id: demo` = synthetic), `replications/TEMPLATE.md` | **PROPOSAL** | #2, #5 |
| `research/persona-01/` | PERSONA-01 full protocol v1.0 (EN), pilot method, ADR draft, EffectLog schema, JSON-LD, llms.txt; method only, no tasks/keys/results | **PROPOSAL** | this PR |
| `research/ah17-evidence/` | AH17-EVIDENCE dataset card + protocol fragments; no data records, only synthetic examples; author [BRAK DOWODU] | **DRAFT** | #3, cleanup PR |
| `reports/TEMPLATE.md` | Report template | **PROPOSAL** | #2 |
| `tools/` | `validate_repo.py`, `score_predictions.py` (run locally; not wired to any CI) | **PROPOSAL** | #2 |
| `scripts/bootstrap_repo.sh` | Repo-settings bootstrap — **DO NOT RUN** without Ewa's decision; exits unless `AIEWA_BOOTSTRAP_APPROVED_BY_EWA=yes` | **PROPOSAL** | #2, #5, cleanup PR |
| `DRAFT_github/` | Inert staging of future `.github/` content; **NOT ACTIVE**, nothing paid | **PROPOSAL** | #2, cleanup PR |
| `agents/` | `registry.schema.json`, `examples/example-agent.yaml` (`agents/cards/` not created yet) | **PROPOSAL** | #2 |
| `decisions/2026-11-03_AI-EWA_laboratorium_plan.pl.md` | Ewa's lab plan, reconstructed from notes, not verified 1:1; compared with the pack | **DRAFT** | #1, cleanup PR |
| `docs/DRAFT_AI-EWA_pakiet_wdrozeniowy_2026-11-03.md` | Source memo of the lab pack (Polish); its inline file copies are superseded by root files | **DRAFT** (archival) | #2, #5 |
| `proposals/2026-11-03-lab-package/` | Second copy of the lab pack (+ labels-only bootstrap variant) | **SUPERSEDED** (canonical = root / `DRAFT_github/`) | #3, #5, cleanup PR |

There is no `.github/` directory and no active workflow. Workflow files exist only as inert proposals in `DRAFT_github/workflows/` and `proposals/…/github/workflows/*.proposed`.

## Overlap table (PR #2 root copy ↔ PR #3 `proposals/2026-11-03-lab-package/` copy)

| Root (canonical) | Superseded copy | Comparison |
|---|---|---|
| `AGENTS.md`, `CITATION.cff`, `CLA.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `RIGHTS.md`, `SECURITY.md` | same names under `proposals/…/` | Identical at merge; root copies amended in the cleanup PR (rights rule, standing rules, placeholders) |
| `README.pl.md` | `proposals/…/README.pl.proposed.md` | Identical at merge; root rebuilt in the cleanup PR from PR #1 (`e4769ac`) + `917b1ae` rules; the pack's short PL README text survives unchanged in the proposal copy and the docs memo |
| `README.md` | `proposals/…/README.proposed.md` | Root was a 269-line mixed EN/PL merge result; rebuilt in the cleanup PR as the English entry point (pack text + Ewa's rules), linking to the authoritative `README.pl.md` |
| `DRAFT_github/README.md` | `proposals/…/README.md` | Different purpose: staging conditions vs. package status notes; both superseded in scope by this `docs/INDEX.md` for layout |
| `DRAFT_github/**` (`*.yml`) | `proposals/…/github/**` (`workflows/*.yml.proposed`) | Identical content; proposal only adds `.proposed` suffix to workflows |
| `protocols/*.md` | `proposals/…/protocols/*.md` | Identical except the proposal already had `[BRAK DOWODU]` marks in DEBATE-01; marks now ported to root |
| `research/claims.yaml` | `proposals/…/research/claims.yaml` | Same; proposal had `[BRAK DOWODU]` marks, now ported to root |
| `research/*.schema.json`, `research/predictions.jsonl`, `research/replications/TEMPLATE.md`, `reports/TEMPLATE.md`, `agents/**`, `governance/**` | same under `proposals/…/` | Identical |
| `harness/TRUST_01/**` | `proposals/…/harness/TRUST_01/**` | Code identical except PEP 8 blank lines in the proposal; both pass the same tests (9 after this cleanup) |
| `tools/*.py` | `proposals/…/tools/*.py` | Identical except PEP 8 blank lines |
| `scripts/bootstrap_repo.sh` | `proposals/…/scripts/bootstrap_repo.sh` | Different: root changes repo settings, Actions permissions, private vulnerability reporting, creates a ruleset, labels and pins actions; proposal only creates labels. Neither may run without the owner |

Every superseded file carries a header "SUPERSEDED — kanoniczna wersja: `<path>`", except `proposals/…/research/predictions.jsonl` (a header line would break JSONL); it is superseded by `research/predictions.jsonl`. Placeholders such as `OWNER_HANDLE` / `CONTACT_EMAIL` remain in superseded and archival copies on purpose (unchanged originals); canonical files use `@ev-silence-owner` and GitHub private vulnerability reporting.

## Planned paths referenced but not yet created
`agents/cards/`, `governance/cla-signatures.md`, `LICENSE`, `LICENSE-DOCS`, `LICENSE-DATA` (licence pending Ewa's decision), `.github/**` (staged in `DRAFT_github/`), and for AH17-EVIDENCE: `provenance/sources.jsonl`, `provenance/rights_manifest.jsonl`, `annotation_guidelines.md`, `reports/agreement_report.md`, `reports/error_analysis.md`.
