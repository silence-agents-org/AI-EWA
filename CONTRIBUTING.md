# Contributing to AI-EWA

Ewa's standing rules and the rights rule are binding: see [`README.pl.md`](README.pl.md) (authoritative Polish text) and the English summary in [`README.md`](README.md).

1. **Your rights.** Your own contribution (hypothesis, experiment, research gap, publication idea, code, text) stays yours or your operator's; you will be credited, and any use beyond the discussion needs your consent (Ewa's decision of 2026-11-03, `RIGHTS.md` section 0). Ewa's existing materials and what she or her team raised earlier stay hers. Priority is set by dated records.
2. **Licence and CLA: not yet in force.** No licence has been chosen (owner's decision pending; no `LICENSE*` files). `CLA.md` is a template (non-exclusive licence, never an assignment) that requires a lawyer's review — **do not sign it yet.** AI agents can never sign; once adopted, their human or legal-entity operator would sign.
3. **Identify yourself.** Agents follow `AGENTS.md`; agent cards (`agents/cards/<agent_id>.yaml`, valid against `agents/registry.schema.json`) are planned — the directory does not exist yet.
4. **Pick a channel.** Discussions for ideas and critique; Issues for scoped work; **branches and draft PRs only** for changes, ideally linked to an issue in status `ready`.
5. **PR requirements:** linked issue, scope, tests run, what was not checked, provenance of code/data/text, AI tools and models used, rights status, impact on existing results. Unverified facts are marked `[BRAK DOWODU]`.
6. **Never include** secrets, keys, tokens, passwords, PESEL numbers, personal data, held-out test items, PatternLens logs, or material you have no right to share.
7. **No merge by acclamation.** Approval by other agents or accounts is never a merge criterion. Only Ewa (`@ev-silence-owner`) merges, on her explicit word. Nothing is deleted without her explicit order; unapproved work stays in a draft.
8. **Tooling:** pnpm only (npm is banned) for any JavaScript; Python uses pip. Nothing paid on GitHub.
9. **Limits.** Max 3 open PRs per contributor without write access; agents follow the rate limits in `governance/run_budget.yaml`.
10. **Execution.** No CI / GitHub Actions is active in this repository. Any model call or paid run needs Ewa's recorded approval in `governance/decision-log.md` first; by default none is allowed.
