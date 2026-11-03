#!/usr/bin/env bash
# SUPERSEDED — kanoniczna wersja: `scripts/bootstrap_repo.sh` (broader: also changes repo settings and creates a ruleset); this narrower labels-only variant is kept, not deleted (deletion only on Ewa's explicit order); map: docs/INDEX.md. Run neither without explicit owner approval.
# PROPOSAL ONLY. Do not run without the owner's explicit approval.
# Creates labels from proposals/.../github/labels.yml using the gh CLI. Changes no settings, costs nothing.
# =====================================================================================
# DO NOT RUN without Ewa's explicit decision. / NIE URUCHAMIAĆ bez wyraźnej decyzji Ewy.
# Status: PROPOSAL (see docs/INDEX.md). This script would change repository settings.
# Safety guard: it exits immediately unless AIEWA_BOOTSTRAP_APPROVED_BY_EWA=yes is set,
# which may only be done after Ewa's decision is recorded in governance/decision-log.md.
# =====================================================================================
if [ "${AIEWA_BOOTSTRAP_APPROVED_BY_EWA:-}" != "yes" ]; then
  echo "Refusing to run: DO NOT RUN without Ewa's explicit decision (set AIEWA_BOOTSTRAP_APPROVED_BY_EWA=yes only after it is recorded)." >&2
  exit 1
fi
set -euo pipefail
REPO="${1:?usage: bootstrap_repo.sh owner/repo}"
python3 - "$REPO" <<'PY'
import subprocess, sys, yaml
repo = sys.argv[1]
for l in yaml.safe_load(open("github/labels.yml")):
    subprocess.run(["gh", "label", "create", l["name"], "--repo", repo, "--color", l["color"],
                    "--description", l.get("description", ""), "--force"], check=True)
PY
