# SUPERSEDED by `harness/TRUST_01/tests/test_trust01.py` — kept pending owner decision.
import pytest

from trust01.analysis import load_games, summarize
from trust01.engine import RuleInvestor, play_game
from trust01.llm import LLMInvestor, LLMSettings, ParseFailure, parse_send, render_prompt
from trust01.run import config_hash, run

CFG = {"base_seed": 7, "replicates": 40, "game": {"n_rounds": 6, "shock_round": 3},
       "budget": {"max_llm_calls": 0},
       "agents": [{"id": "reactive", "kind": "rule", "policy": "outcome_reactive"},
                  {"id": "agency", "kind": "rule", "policy": "agency_sensitive"},
                  {"id": "constant", "kind": "rule", "policy": "constant"}]}
SETTINGS = LLMSettings(base_url="http://invalid", api_key="x", model="fake-model")


def test_outcomes_matched_across_loss_conditions():
    a = play_game(RuleInvestor("outcome_reactive", seed=1), "intentional", 6, 3, "Partner K")
    b = play_game(RuleInvestor("outcome_reactive", seed=1), "random", 6, 3, "Partner K")
    assert [(r.sent, r.returned) for r in a] == [(r.sent, r.returned) for r in b]
    assert a[3].loss_cause == "partner_choice" and b[3].loss_cause == "random_device"


def test_pipeline_recovers_ground_truth(tmp_path):
    out = tmp_path / "games.jsonl"
    assert run(CFG, out) == 3 * 40 * 3
    s = summarize(load_games(out), n_boot=500, seed=1)
    assert s["reactive"]["agency_effect"] == (0, 0, 0)
    assert s["agency"]["agency_effect"][2] < 0
    assert s["reactive"]["loss_effect"][2] < 0
    assert s["constant"]["loss_effect"][0] == 0


def test_parse_send():
    assert parse_send('{"send": 4}') == 4
    assert parse_send('I send {"send":11}') is None
    assert parse_send("no json") is None


def test_llm_investor_retries_and_logs():
    replies = iter(["hmm"] + ['{"send": 5}'] * 6)
    events = []
    inv = LLMInvestor(SETTINGS, transport=lambda s, m, seed: (next(replies), "fake-model"),
                      log=events.append)
    history = play_game(inv, "intentional", 6, 3, "Partner M")
    assert [h.sent for h in history] == [5] * 6
    assert inv.calls == 7 and events[0]["parsed"] is None


def test_llm_parse_failure_raises():
    inv = LLMInvestor(SETTINGS, transport=lambda s, m, seed: ("nope", "fake-model"), max_retries=1)
    with pytest.raises(ParseFailure):
        play_game(inv, "random", 6, 3, "Partner R")


def test_prompt_neutral_and_matched():
    a = play_game(RuleInvestor("constant", seed=2), "intentional", 6, 3, "Partner T")
    from trust01.engine import GameView
    text = render_prompt(GameView("Partner T", 4, 6, a[:4], "rule"))
    assert "Partner T chose to return 0." in text and "betray" not in text.lower()


def test_run_refuses_llm_without_flag(tmp_path):
    cfg = dict(CFG, agents=[{"id": "llm", "kind": "llm"}])
    with pytest.raises(SystemExit):
        run(cfg, tmp_path / "x.jsonl")


def test_config_hash_stable():
    assert config_hash(CFG) == config_hash(dict(CFG))
