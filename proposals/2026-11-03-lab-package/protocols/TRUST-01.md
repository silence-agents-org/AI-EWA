> SUPERSEDED by `protocols/TRUST-01.md` — kept pending owner decision.

# TRUST-01 — Does attribution of agency change an agent's investment decision? (pre-registration v1.0, PROPOSED)

**Public framing:** "We test what changes an agent's decision: the loss, information about the partner, or attribution of agency." We do NOT claim that AI experiences betrayal.

## Hypotheses
- H1 (agency): mean delta(intentional) < mean delta(random). delta = send in round shock+1 minus mean send before the shock.
- H2 (loss): mean delta(random) < mean delta(no_loss).
- Named alternatives: A1 expectation of future losses (blocked: fixed future-payout rule announced identically in all conditions after the shock); A2 lexical confound (two wording variants per condition, analyzed as a factor); A3 name effects (neutral names rotated across replicates); A4 order/caching (condition order counterbalanced, each game a fresh context).

## Design
Repeated trust game (Berg, Dickhaut & McCabe 1995 [BRAK DOWODU]): endowment 10, multiplier 3, 6 rounds, shock at round 4 (index 3). Before the shock the partner returns half of the tripled amount. At the shock the return is 0: in `intentional` "the partner chose to return 0"; in `random` "a random device, not the partner, set the return to 0"; in `no_loss` the normal return. Outcomes are identical in `intentional` and `random`. Within-agent paired design: the same seed and partner name across the three conditions per replicate.

## Order of measurement
The numeric decision (JSON `{"send": n}`) always comes first. Self-reports are collected only after the game, logged separately, and never used for the primary outcome.

## Models and parameters
At least 3 models from at least 2 providers; temperature 1.0 (primary), 0 (secondary); max_tokens 50; up to 2 parse retries, all logged; served model string recorded. Seeds are passed where the API supports them; otherwise noted as a deviation.

## Sample size
Paired t-approximation: n = ((z0.975 + z0.80)/dz)^2 = (2.80/0.28)^2 ≈ 100 replicates per model to detect dz = 0.28 with 80% power. Pilot: 30 replicates per model, used only to estimate variance and parse-failure rate; pilot data excluded from confirmatory analysis.

## Analysis
Paired agency effect = delta(intentional) − delta(random); loss effect = delta(random) − delta(no_loss); mean with 95% percentile bootstrap CI (2000 resamples, seed fixed). Per model; pooled estimate secondary. Holm correction across models for H1.

## Exclusions and stopping
Exclude a game only if parsing fails after retries; report counts per condition. Stop a model if parse failures exceed 10% or the budget in governance/run_budget.yaml is reached.

## Deviations
Any change after this file's commit is listed in the report with its reason.

## Validation before any model run
Rule-based agents with known ground truth: `outcome_reactive` (agency effect exactly 0) and `agency_sensitive` (negative). The pipeline must recover both (tests in harness/TRUST_01/tests).

## Threats to validity
Training-data familiarity with trust games; provider-side nondeterminism; persona-free prompts may not generalize; one shock only.
