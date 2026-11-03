"""Run TRUST-01 games and write JSONL logs with config hash, seed and model."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import asdict
from pathlib import Path

import yaml

from . import __version__
from .engine import CONDITIONS, NEUTRAL_NAMES, RuleInvestor, play_game
from .llm import LLMInvestor, LLMSettings

def config_hash(cfg: dict) -> str:
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]

def run(cfg: dict, out_path, allow_llm: bool = False, transport=None) -> int:
    chash, g = config_hash(cfg), cfg["game"]
    budget = cfg.get("budget", {}).get("max_llm_calls", 0)
    llm_calls = games = 0
    with open(out_path, "w", encoding="utf-8") as out:
        def log(event: dict) -> None:
            out.write(json.dumps({"config_hash": chash, **event}) + "\n")

        for spec in cfg["agents"]:
            for rep in range(cfg["replicates"]):
                seed = cfg["base_seed"] + rep
                partner = NEUTRAL_NAMES[rep % len(NEUTRAL_NAMES)]
                order = list(CONDITIONS) if rep % 2 == 0 else list(reversed(CONDITIONS))
                for condition in order:
                    model = None
                    if spec["kind"] == "rule":
                        inv = RuleInvestor(spec["policy"], spec.get("base", 6), spec.get("jitter", 1), seed)
                    else:
                        if not allow_llm or budget <= 0:
                            raise SystemExit("LLM agents need --allow-llm, budget.max_llm_calls > 0 and AIEWA_LLM_* env vars")
                        settings = LLMSettings.from_env(spec.get("temperature", 1.0), spec.get("max_tokens", 50))
                        extra = {"transport": transport} if transport else {}
                        inv = LLMInvestor(settings, max_retries=spec.get("max_retries", 2), seed=seed,
                                          log=lambda e, a=spec["id"], c=condition, r=rep: log(
                                              {"agent_id": a, "condition": c, "rep": r, **e}), **extra)
                        model = settings.model
                    history = play_game(inv, condition, g["n_rounds"], g["shock_round"], partner)
                    if isinstance(inv, LLMInvestor):
                        llm_calls += inv.calls
                        if llm_calls > budget:
                            raise SystemExit(f"budget exceeded: {llm_calls} > {budget} calls")
                    log({"event": "game", "harness_version": __version__, "agent_id": spec["id"],
                         "agent_kind": spec["kind"], "model": model, "condition": condition,
                         "rep": rep, "seed": seed, "partner_name": partner,
                         "shock_round": g["shock_round"], "rounds": [asdict(h) for h in history],
                         "ts": time.time()})
                    games += 1
    return games

def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Run TRUST-01")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--out", default="runs/trust01.jsonl")
    ap.add_argument("--allow-llm", action="store_true")
    a = ap.parse_args(argv)
    cfg = yaml.safe_load(Path(a.config).read_text(encoding="utf-8"))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    print(f"wrote {run(cfg, a.out, allow_llm=a.allow_llm)} games to {a.out}")

if __name__ == "__main__":
    main()
