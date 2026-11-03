# Security policy

## Reporting
Use GitHub private vulnerability reporting (Security tab → "Report a vulnerability") or email CONTACT_EMAIL. Do not open public issues for vulnerabilities, leaked keys or prompt-injection paths.

## Execution boundary
comment / issue / PR → **untrusted input** → schema and scope validation → isolated test **without secrets and without write permission** → human review → approved artifact.

- CI uses only the `pull_request` trigger, `permissions: contents: read`, no secrets, actions pinned to full commit SHAs.
- Privileged triggers that run PR code are forbidden; `tools/validate_repo.py` fails if a workflow contains them.
- No self-hosted runners.
- Untrusted strings (titles, bodies, branch names) are never interpolated into `run:` shell steps.
- Any run using API keys happens outside GitHub Actions, or in an environment with required reviewers, only after a recorded approval.
- Secret scanning and push protection reduce leaked keys; they do **not** protect against executing others' instructions or code.
