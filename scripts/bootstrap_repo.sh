#!/usr/bin/env bash
# Configure AI-EWA with gh CLI. Requires: gh auth login (owner/admin), python3 with pyyaml.
set -euo pipefail
REPO="${REPO:-silence-agents-org/AI-EWA}"

gh repo edit "$REPO" --enable-issues --enable-discussions --delete-branch-on-merge \
  --enable-auto-merge=false --enable-squash-merge --enable-merge-commit=false

python3 - "$REPO" <<'EOF'
import subprocess, sys, yaml
repo = sys.argv[1]
for l in yaml.safe_load(open(".github/labels.yml")):
    subprocess.run(["gh", "label", "create", l["name"], "--repo", repo, "--color", l["color"],
                    "--description", l.get("description", ""), "--force"], check=True)
EOF

# Read-only default token; Actions may not approve PRs.
gh api -X PUT "repos/$REPO/actions/permissions/workflow" \
  -f default_workflow_permissions=read -F can_approve_pull_request_reviews=false
# Private vulnerability reporting.
gh api -X PUT "repos/$REPO/private-vulnerability-reporting"
# Require approval for workflows from all external contributors (set in UI if this call fails).
gh api -X PUT "repos/$REPO/actions/permissions/fork-pr-contributor-approval" \
  -f approval_policy=all_external_contributors || echo "Set fork PR approval policy in UI"

# Ruleset on the default branch (admins may bypass only via pull request).
gh api -X POST "repos/$REPO/rulesets" --input - <<'EOF'
{"name": "main-protection", "target": "branch", "enforcement": "active",
 "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
 "bypass_actors": [{"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "pull_request"}],
 "rules": [{"type": "deletion"}, {"type": "non_fast_forward"},
  {"type": "pull_request", "parameters": {"required_approving_review_count": 1,
    "dismiss_stale_reviews_on_push": true, "require_code_owner_review": true,
    "require_last_push_approval": true, "required_review_thread_resolution": true}},
  {"type": "required_status_checks", "parameters": {"strict_required_status_checks_policy": true,
    "required_status_checks": [{"context": "validate"}]}}]}
EOF

# Pin actions to full SHAs of their latest releases.
pin() { local tag sha; tag=$(gh api "repos/$1/releases/latest" --jq .tag_name)
  sha=$(gh api "repos/$1/commits/$tag" --jq .sha)
  sed -i "s#$2@PIN#$2@$sha \# $tag#g" .github/workflows/*.yml; }
pin actions/checkout actions/checkout
pin ossf/scorecard-action ossf/scorecard-action
pin github/codeql-action github/codeql-action/upload-sarif
echo "Done. Commit the pinned workflows, then complete the manual UI checklist."
