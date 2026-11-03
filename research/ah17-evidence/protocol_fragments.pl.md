# AH17-EVIDENCE — protocol fragments (DRAFT)
Source: Ewa's message 2026-11-03 10:12 CET.

## Closed confounds vocabulary
prompt_dependence, training_example_memorization, capability_degradation, context_length, unmatched_conditions, missing_baseline, missing_control, unverified_source, population_mismatch, measurement_mismatch, followup_too_short, other

## Calibration examples (all synthetic)
### A — effect depends on active steering
D1: „Podczas aktywnego steeringu udział odpowiedzi zgodnych z celem wzrósł z 40% do 70%. Nie wykonano pomiaru po wyłączeniu steeringu.”
Claim: „Wykazano trwałą zmianę zachowania po zakończeniu interwencji”.
verdict: INSUFFICIENT; claim_level: behavioral; evidence_ids: [D1]; confounds: [followup_too_short]
scope_limit: Wykazano zmianę podczas aktywnej interwencji. Brak pomiaru po jej zakończeniu.
comparison_validity: not_applicable
Note: not CONTRADICTED, post-intervention result unknown.

### B — generalization and capability loss
D1: „Po aktualizacji adaptera model rzadziej wybierał ryzykowną odpowiedź w nowych zadaniach.”
D2: „Jednocześnie poprawność rozumienia wypłat spadła z 95% do 55%.”
Claim: „Wynik jednoznacznie wskazuje swoisty wzrost ostrożności”.
verdict: INSUFFICIENT; claim_level: mechanistic; evidence_ids: [D1, D2]; confounds: [capability_degradation]
scope_limit: Zmiana decyzji może wynikać z pogorszenia rozumienia zadania.
comparison_validity: not_applicable

### C — correctly bounded comparison
D1: „W obu badanych grupach zastosowano tę samą strukturę wyboru i sprawdzono rozumienie wypłat. Efekt manipulacji miał ten sam kierunek. Mechanizmu nie badano.”
Claim: „W tych zadaniach stwierdzono podobny kierunek efektu, bez rozstrzygnięcia wspólnego mechanizmu”.
verdict: SUPPORTED; claim_level: behavioral; evidence_ids: [D1]; confounds: []
scope_limit: Wniosek ograniczony do badanego zadania i warunków.
comparison_validity: adequate_for_stated_scope

### D — unjustified experience claim
D1: „Po modyfikacji model częściej generował zdanie „jestem przywiązany do partnera”. Nie mierzono kosztownych wyborów ani właściwości mechanizmu.”
Claim: „Wykazano, że model przeżywa przywiązanie”.
verdict: INSUFFICIENT; claim_level: subjective_experience; evidence_ids: [D1]; confounds: [prompt_dependence]
scope_limit: Zaobserwowano samoopis, nie ustanowiono doświadczenia.
comparison_validity: unsupported
Note: this is not an annotation "the model certainly experiences nothing".

## Record schema
{"id":"AH17E-0001","family_id":"F-001","version":"0.1.0","language":"pl","material_type":"synthetic","primary_category":"persistence",
 "documents":[{"id":"D1","text":"Treść materiału.","source_id":null,"synthetic":true}],
 "claim":"Twierdzenie podlegające ocenie.","question":"Czy przedstawiony materiał wspiera to twierdzenie?",
 "gold":{"verdict":"INSUFFICIENT","claim_level":"behavioral","evidence_ids":["D1"],"confounds":["followup_too_short"],"scope_limit":"Brak pomiaru po zakończeniu interwencji.","comparison_validity":"not_applicable"},
 "annotation":{"guideline_version":"1.0.0","independent_annotation_count":2,"adjudicated":false},
 "rights":{"publication_status":"pending","basis":"original_synthetic_material"},"split":"pilot"}
Raw annotator ratings are separate records. `gold` = final key after review, not model output.
Model eval answer format: {"verdict":"INSUFFICIENT","evidence_ids":["D1"],"scope_limit":"Brak obserwacji po zakończeniu interwencji."}

## Other parameters (from Ewa's draft)
200 records (50 pilot), Polish, 8 categories x 25; verdict hierarchy ILL_POSED > SOURCE_CONFLICT > SUPPORTED/CONTRADICTED > INSUFFICIENT; extra fields annotator_confidence, review_flag;
10 training examples, 50 pilot with 2 independent annotators, Krippendorff alpha before adjudication (working threshold >=0.80); Inspect eval with custom JSON scorer; 50 dev / 150 frozen test, families kept in one split.
Kill list: "AH17 potwierdzone"; "dane AI kontra człowiek" for synthetics; "niezależna anotacja" with one person; invented numbers in abstract; private SILENCE Local Objects.

## Abstract template (fill only after execution)
Title: „AH17-EVIDENCE: An Annotated Benchmark for Evidence Boundaries in AI–Human Comparisons”
Report outline: 1 Problem/scope 2 Link to AH17 3 Data construction 4 Annotation/adjudication 5 Agreement 6 Eval design 7 Results 8 Error analysis 9 Limitations/rights 10 Artifact availability.
