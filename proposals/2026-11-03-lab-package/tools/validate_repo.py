# SUPERSEDED — kanoniczna wersja: `tools/validate_repo.py`; kept, not deleted (deletion only on Ewa's explicit order); map: docs/INDEX.md.
#!/usr/bin/env python3
"""Validate AI-EWA structured files and workflow policy. No network, no secrets."""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")
FORBIDDEN = ("pull_request_target", "workflow_run", "self-hosted")
errors = []


def check(instance, schema_rel, label):
    schema = json.loads((ROOT / schema_rel).read_text(encoding="utf-8"))
    for e in Draft202012Validator(schema).iter_errors(instance):
        errors.append(f"{label}: {e.message} at {list(e.path)}")


def main():
    for d in ("agents/cards", "agents/examples"):
        for p in sorted((ROOT / d).glob("*.yaml")):
            check(yaml.safe_load(p.read_text(encoding="utf-8")), "agents/registry.schema.json", str(p.relative_to(ROOT)))
    check(yaml.safe_load((ROOT / "research/claims.yaml").read_text(encoding="utf-8")),
          "research/claims.schema.json", "research/claims.yaml")
    for i, line in enumerate((ROOT / "research/predictions.jsonl").read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            check(json.loads(line), "research/predictions.schema.json", f"predictions.jsonl:{i}")
    for p in list((ROOT / ".github").glob("**/*.yml")) + [ROOT / "governance/run_budget.yaml"]:
        try:
            yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"{p.relative_to(ROOT)}: invalid YAML: {e}")
    for p in (ROOT / ".github/workflows").glob("*.yml"):
        text = p.read_text(encoding="utf-8")
        for word in FORBIDDEN:
            if word in text:
                errors.append(f"{p.name}: forbidden by SECURITY.md: {word}")
        for line in text.splitlines():
            s = line.strip().removeprefix("- ")
            if s.startswith("uses:"):
                ref = s.split("@", 1)[1].split()[0] if "@" in s else ""
                if not SHA.match(ref):
                    errors.append(f"{p.name}: action not pinned to a full commit SHA: {s}")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
