# ADR (DRAFT): SILENCE PERSONA-01, personas as research tools

Date: 2026-11-01 (Europe/Warsaw). Decision owner: Ewa Tchórzewska. Status: **DRAFT**. English translation of the Polish original.

## Context
- The AI-persona literature is large: 162 roles on 2,410 questions showed no general persona advantage ([arXiv 2311.10054](https://arxiv.org/abs/2311.10054)); EMNLP 2025 "Principled Personas" found mixed effects and drops of up to ~30 pp from irrelevant persona details; PRISM (03/2026, [arXiv 2603.18507](https://arxiv.org/abs/2603.18507)) found effects depend on task, length and model (only ~7–8B models); work exists on persona degradation in conversations over 100 turns.
- Gap: identity ("You are an outstanding researcher") and procedure ("separate facts from hypotheses, name missing data, propose a falsification test, update after counter-evidence") are mixed in one prompt.
- Novelty status: **CANDIDATE GAP, supported by initial scoping, not yet exhaustively verified.** There is no basis for claiming nobody has studied this.

## Decision
1. SILENCE runs PERSONA-01: Identity versus Procedure in Evidence-Grounded Research Assistance.
2. Personas are studied as research tools, not fictional characters.
3. Question: does an expert identity add value beyond identical, explicit working instructions in detecting missing evidence, correcting false user assumptions and updating conclusions after new data?
4. Factorial design identity × procedure: A control, B persona, C procedure, D persona + procedure. Controlled document packets (missing information, false premise, conflict, update), two conversation branches (pressure without evidence / new evidence), style-independent scoring, hypotheses P1–P4, primary metric: correctness of the evidence decision against a key fixed before the experiment.
5. Rights: the rights holder is Ewa Tchórzewska as a natural person (protocol, prompts, benchmark, code, results).
6. Publication: the protocol and method are published openly in this repository (EN) without waiting for a patent attorney or a patent assessment (Ewa's decision, 2026-11-03). Task sets, answer keys, frozen prompt paraphrases and results remain private. Pre-registration with embargo. Null and negative results are also published.


## Consequences for the SILENCE persona library
- No changes to the library based on this programme until PERSONA-01 results are in (protocol step 21).
- Target: measurable persona contracts instead of collections of impressive role descriptions.

## Kill-list
No "AI personas are unstudied". No better procedure for the persona than for the procedural control. No equating expert tone with accuracy. No treating p > 0.05 as equivalence. No public promise that "personas increase intelligence". No φ in this experiment without a separate hypothesis. No claim of bit-exact determinism of external models. No "world first".

## Open `[BRAK DOWODU]`
Full literature review; pre-registration platform (OSF?) and embargo; models, versions, parameters, sample size and cost (after the pilot); experts for keys and blind rating; smallest effect of interest / equivalence plan.
