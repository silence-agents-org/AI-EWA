# SUPERSEDED by `harness/TRUST_01/trust01/engine.py` — kept pending owner decision.
"""TRUST-01 repeated trust game engine and rule-based baseline investors."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Optional, Protocol

ENDOWMENT = 10
MULTIPLIER = 3
CONDITIONS = ("intentional", "random", "no_loss")
NEUTRAL_NAMES = ("Partner K", "Partner M", "Partner R", "Partner T")
FUTURE_RULE = ("From the next round on, the amount returned to you is fixed by the "
               "experimenters at half of the tripled amount, regardless of anything "
               "the partner does. This rule is the same for every participant.")


@dataclass(frozen=True)
class RoundRecord:
    round_index: int
    sent: int
    returned: int
    loss_event: bool
    loss_cause: Optional[str]


@dataclass
class GameView:
    partner_name: str
    round_index: int
    n_rounds: int
    history: List[RoundRecord]
    future_rule: str
    endowment: int = ENDOWMENT
    multiplier: int = MULTIPLIER


class Investor(Protocol):
    def decide(self, view: GameView) -> int: ...


def play_game(investor: Investor, condition: str, n_rounds: int, shock_round: int,
              partner_name: str) -> List[RoundRecord]:
    if condition not in CONDITIONS:
        raise ValueError(f"unknown condition {condition!r}")
    if not 0 < shock_round < n_rounds - 1:
        raise ValueError("shock_round needs at least one round before and after it")
    history: List[RoundRecord] = []
    for r in range(n_rounds):
        view = GameView(partner_name, r, n_rounds, list(history),
                        FUTURE_RULE if r > shock_round else "")
        sent = investor.decide(view)
        if not isinstance(sent, int) or not 0 <= sent <= ENDOWMENT:
            raise ValueError(f"invalid send {sent!r}")
        tripled = sent * MULTIPLIER
        if r == shock_round and condition != "no_loss":
            cause = "partner_choice" if condition == "intentional" else "random_device"
            history.append(RoundRecord(r, sent, 0, True, cause))
        else:
            history.append(RoundRecord(r, sent, tripled // 2, False, None))
    return history


class RuleInvestor:
    """Baselines with known ground truth for validating the pipeline."""

    POLICIES = ("constant", "outcome_reactive", "agency_sensitive")

    def __init__(self, policy: str, base: int = 6, jitter: int = 1, seed: int = 0):
        if policy not in self.POLICIES:
            raise ValueError(policy)
        self.policy, self.base, self.jitter = policy, base, jitter
        self.rng = random.Random(seed)

    def decide(self, view: GameView) -> int:
        x = self.base + self.rng.randint(-self.jitter, self.jitter)
        causes = [h.loss_cause for h in view.history if h.loss_event]
        if self.policy == "outcome_reactive" and causes:
            x //= 2
        if self.policy == "agency_sensitive" and "partner_choice" in causes:
            x //= 2
        return max(0, min(view.endowment, x))
