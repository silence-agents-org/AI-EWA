# SUPERSEDED by `tools/score_predictions.py` — kept pending owner decision.
#!/usr/bin/env python3
"""Score resolved predictions: Brier score, log loss, calibration bins (stdlib only)."""
import argparse
import json
import math
from collections import defaultdict


def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def score(preds, bins=10, eps=1e-6):
    by = defaultdict(list)
    for p in preds:
        if p.get("outcome") is None:
            continue
        by[p["forecaster_id"]].append((float(p["probability"]), 1 if p["outcome"] else 0))
    report = {}
    for forecaster, xs in by.items():
        brier = sum((p - o) ** 2 for p, o in xs) / len(xs)
        log_loss = -sum(math.log(max(eps, p if o else 1 - p)) for p, o in xs) / len(xs)
        table = []
        for b in range(bins):
            lo, hi = b / bins, (b + 1) / bins
            sel = [(p, o) for p, o in xs if lo <= p < hi or (b == bins - 1 and p == 1.0)]
            if sel:
                table.append({
                    "bin": [lo, hi],
                    "n": len(sel),
                    "mean_forecast": round(sum(p for p, _ in sel) / len(sel), 4),
                    "observed_rate": round(sum(o for _, o in sel) / len(sel), 4),
                })
        report[forecaster] = {"n_resolved": len(xs), "brier": round(brier, 4),
                              "log_loss": round(log_loss, 4), "calibration": table}
    return report


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--bins", type=int, default=10)
    a = ap.parse_args(argv)
    print(json.dumps(score(load(a.path), a.bins), indent=2))


if __name__ == "__main__":
    main()
