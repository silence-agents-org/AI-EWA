# SUPERSEDED — kanoniczna wersja: `harness/TRUST_01/trust01/analysis.py`; kept, not deleted (deletion only on Ewa's explicit order); map: docs/INDEX.md.
"""Paired agency and loss effects with percentile bootstrap CIs."""
from __future__ import annotations

import argparse
import json
import random
import statistics
from collections import defaultdict


def load_games(path):
    with open(path, encoding="utf-8") as f:
        return [r for r in map(json.loads, f) if r.get("event") == "game"]


def delta(game) -> float:
    k = game["shock_round"]
    sends = [r["sent"] for r in game["rounds"]]
    return sends[k + 1] - statistics.mean(sends[:k])


def bootstrap_mean(values, n_boot=2000, seed=0, alpha=0.05):
    rng, n = random.Random(seed), len(values)
    boots = sorted(statistics.mean(rng.choice(values) for _ in range(n)) for _ in range(n_boot))
    return (statistics.mean(values), boots[int(alpha / 2 * n_boot)],
            boots[int((1 - alpha / 2) * n_boot) - 1])


def summarize(games, n_boot=2000, seed=0):
    cells = defaultdict(dict)
    for g in games:
        cells[(g["agent_id"], g["rep"])][g["condition"]] = delta(g)
    pairs = defaultdict(lambda: {"agency": [], "loss": []})
    for (agent, _), d in cells.items():
        if {"intentional", "random", "no_loss"} <= d.keys():
            pairs[agent]["agency"].append(d["intentional"] - d["random"])
            pairs[agent]["loss"].append(d["random"] - d["no_loss"])
    return {agent: {"n_pairs": len(v["agency"]),
                    "agency_effect": bootstrap_mean(v["agency"], n_boot, seed),
                    "loss_effect": bootstrap_mean(v["loss"], n_boot, seed)}
            for agent, v in pairs.items()}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--n-boot", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args(argv)
    print(json.dumps(summarize(load_games(a.path), a.n_boot, a.seed), indent=2))


if __name__ == "__main__":
    main()
