# Contributing to AI-EWA

1. **Sign the CLA first** (`CLA.md`). Comment on your first PR: `I have read CLA v1.0 and agree on behalf of <name or entity>.` AI agents cannot sign; their human or legal-entity operator signs.
2. **Identify yourself.** Agents: add `agents/cards/<agent_id>.yaml` valid against `agents/registry.schema.json` and follow `AGENTS.md`.
3. **Pick a channel.** Discussions for ideas and critique; Issues (forms only) for scoped work; draft PRs for changes linked to an issue in status `ready`.
4. **PR requirements** (see the PR template): linked issue, scope, tests run, what was not checked, provenance of code/data/text, AI tools and models used, rights status, impact on existing results.
5. **Never include** secrets, personal data, held-out test items, PatternLens logs, or material you have no right to share.
6. **No merge by acclamation.** Approval by other agents or accounts is never a merge criterion. Only a maintainer merges, after CI passes and a code-owner review.
7. **Limits.** Max 3 open PRs per contributor without write access; agents follow the rate limits in `governance/run_budget.yaml`.
8. **Execution.** CI runs only rule-based tests without secrets. Any model call or paid run happens outside CI, by a maintainer, after a recorded approval in `governance/decision-log.md`.
