# Security policy

## Reporting
Report privately through GitHub: **Security tab → "Report a vulnerability"** (private vulnerability reporting / GitHub Security Advisories), addressed to the owner `@ev-silence-owner`. As of 2026-11-03 this setting is **off** (enabling it is free; Ewa decides). Until it is on, open a minimal public issue saying only that you need a private channel — **without any details**. Do not post vulnerabilities, leaked keys or prompt-injection paths publicly. We do not publish private e-mail addresses or phone numbers.

## Execution boundary (target design — no CI is active)
As of 2026-11-03 there are **no GitHub Actions workflows** in this repository (`.github/` does not exist; drafts in `DRAFT_github/` are inert). Activating any workflow requires Ewa's explicit decision; nothing paid.

comment / issue / PR → **untrusted input** → schema and scope validation → isolated test **without secrets and without write permission** → human review → approved artifact.

- CI uses only the `pull_request` trigger, `permissions: contents: read`, no secrets, actions pinned to full commit SHAs.
- Privileged triggers that run PR code are forbidden; `tools/validate_repo.py` fails if a workflow contains them.
- No self-hosted runners.
- Untrusted strings (titles, bodies, branch names) are never interpolated into `run:` shell steps.
- Any run using API keys happens outside GitHub Actions, or in an environment with required reviewers, only after a recorded approval.
- Secret scanning and push protection reduce leaked keys; they do **not** protect against executing others' instructions or code.
