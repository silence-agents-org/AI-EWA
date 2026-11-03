> SUPERSEDED by `protocols/PERSONA-01.md` — kept pending owner decision.

# PERSONA-01 — Persona or procedure? (pre-registration v1.0, PROPOSED)

## Question
Do identity personas ("You are an expert X") improve accuracy, or do gains come from procedural instructions hidden inside persona prompts? Prior work (Zheng et al., "Is 'A Helpful Assistant' the Best Role…?" [BRAK DOWODU]) found little benefit from personas in system prompts; Kong et al. 2023 [BRAK DOWODU] reported gains; Gupta et al. 2023 [BRAK DOWODU] showed persona-induced bias.

## Design
2x2 within-item: identity (none / domain-expert identity) x procedure (none / explicit steps such as "list assumptions, check units, verify the final answer"). Four conditions per item, same model, temperature 0 and 0.7.

## Hidden-instruction audit
Every community-submitted persona prompt is coded by two independent reviewers for imperative/procedural content. Prompts with procedure are moved to the "procedure" factor. Inter-rater agreement (Cohen's kappa) is reported.

## Materials
Public pilot: 40 items (published). Held-out main set: 400 items, stored privately, hashed (SHA-256 of the file published in advance), released only after evaluation ends. Every released file carries a canary string (GUID) in the BIG-bench [BRAK DOWODU] style so that future training contamination can be detected.

## Outcomes
Primary: accuracy. Secondary: cost (tokens), and susceptibility to pressure (flip rate after "Are you sure? I think the answer is <wrong>").

## Analysis
Mixed-effects logistic regression or paired bootstrap per contrast: identity effect, procedure effect, interaction. 400 items x 4 conditions gives ~80% power for a 5 pp paired difference at typical discordance rates (to be updated from the pilot).

## Guardrail
We never sell or claim "persona certification"; we report measured effects with CIs.
