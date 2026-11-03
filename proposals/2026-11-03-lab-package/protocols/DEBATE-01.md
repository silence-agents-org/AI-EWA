> SUPERSEDED by `protocols/DEBATE-01.md` — kept pending owner decision.

# DEBATE-01 — Does debate help at equal compute? (pre-registration v1.0, PROPOSED)

## Conditions (all on the same held-out items)
1. Single agent, chain-of-thought.
2. Self-consistency: k samples, majority vote.
3. k independent agents (different seeds/models), majority vote.
4. Debate: n agents x r rounds (Du et al. 2023 [BRAK DOWODU] style), final vote.
5. Proposer + counterexample-seeker (critic), proposer decides.
Budgets: each of 2–5 run at matched total output-token budgets B in {4x, 8x, 16x} the CoT budget; k, n, r chosen to hit B within ±10%.

## Outcomes
Primary: accuracy on held-out items. Secondary: tokens, USD, wall time, number of errors detected (an initially wrong answer corrected), number of correct answers abandoned (conformity), failure categories coded with the MAST taxonomy (Cemri et al. 2025 [BRAK DOWODU]).

## Hypothesis
H0 (pre-registered expectation): debate does not exceed self-consistency by >= 2 pp at matched budget (Huang et al. 2023 [BRAK DOWODU]; arXiv 2605.00914 [BRAK DOWODU]). Alternative: heterogeneous-model debate helps on hard items (arXiv 2605.01566 [BRAK DOWODU] reportedly reports +1.3 pp for debate and +2.7 pp for mixture-of-agents over self-consistency at equal budget).

## Analysis
Paired item-level bootstrap and McNemar per budget; Pareto frontier of accuracy vs tokens; strata by difficulty (pilot-based) and model homogeneity.

## Process experiment
The same comparison is applied to AI-EWA's own reviews: single reviewer vs independent reviewers vs discussing agents, measured by errors found in seeded-defect protocols.
