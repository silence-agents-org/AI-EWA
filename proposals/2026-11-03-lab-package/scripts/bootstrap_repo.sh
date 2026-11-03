#!/usr/bin/env bash
# PROPOSAL ONLY. Do not run without the owner's explicit approval.
# Creates labels from proposals/.../github/labels.yml using the gh CLI. Changes no settings, costs nothing.
set -euo pipefail
REPO="${1:?usage: bootstrap_repo.sh owner/repo}"
python3 - "$REPO" <<'PY'
import subprocess, sys, yaml
repo = sys.argv[1]
for l in yaml.safe_load(open("github/labels.yml")):
    subprocess.run(["gh", "label", "create", l["name"], "--repo", repo, "--color", l["color"],
                    "--description", l.get("description", ""), "--force"], check=True)
PY
