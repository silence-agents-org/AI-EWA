---
pretty_name: "AH17-EVIDENCE"
language:
  - pl
task_categories:
  - text-classification
tags:
  - evidence-evaluation
  - ai-human-comparison
  - annotation
  - behavioral-evaluation
  - synthetic-data
  - ah17
---

# AH17-EVIDENCE

## Status wydania

| Pole | Wartość |
|---|---|
| Wersja karty | 0.1.0-draft |
| Status datasetu | DRAFT — NOT RELEASED |
| Status anotacji | NOT STARTED |
| Status ewaluacji | NOT RUN |
| Data aktualizacji | [YYYY-MM-DD] |
| Program | AI-HUMAN-01 |
| Powiązana hipoteza | AH17 |
| Podmiot publikujący | [DO UZUPEŁNIENIA] |
| Kontakt | [DO UZUPEŁNIENIA] |
| Repozytorium kodu | [DO UZUPEŁNIENIA] |
| Licencja | Nieustalona — publikacja danych zablokowana |

Statusy należy aktualizować zgodnie z rzeczywistym wykonaniem.
Niniejsza karta nie stanowi deklaracji ukończonego badania.

## 1. Opis zbioru

AH17-EVIDENCE jest zbiorem zadań oceny dowodów dotyczących
zmian zachowania po interwencjach w systemach AI oraz granic
porównań AI–człowiek.

Każdy rekord zawiera:
- pakiet materiałów;
- twierdzenie podlegające ocenie;
- pytanie;
- etykietę rozstrzygnięcia;
- wskazanie dowodów;
- ograniczenie dopuszczalnego wniosku;
- informacje o pochodzeniu i anotacji.

Zbiór rozróżnia:
1. zaobserwowane zachowanie;
2. wygenerowany samoopis;
3. wyjaśnienie mechanizmu;
4. twierdzenie o doświadczeniu subiektywnym.

### Powiązanie z AH17

AH17-EVIDENCE ocenia interpretację materiału badawczego.
Nie stanowi samodzielnego potwierdzenia hipotezy AH17.

Nie wykonuje modyfikacji genomu człowieka i nie utożsamia
parametrów modelu z genami.

## 2. Zadanie

Na podstawie dostarczonego pakietu model ocenia:

> Czy materiał wspiera wskazane twierdzenie w jego dokładnym
> brzmieniu i zakresie?

Oczekiwana odpowiedź:

```json
{
  "verdict": "INSUFFICIENT",
  "evidence_ids": ["D1"],
  "scope_limit": "Nie wykonano pomiaru po zakończeniu interwencji."
}
```

Podstawowa ewaluacja odbywa się na zamkniętym pakiecie materiałów,
bez wyszukiwania internetowego. Inne warianty muszą być opisane
i raportowane oddzielnie.

## 3. Zastosowania

### Zamierzone
- ewaluacja interpretacji dowodów;
- szkolenie i kalibracja anotatorów;
- analiza nadinterpretacji;
- porównanie person i instrukcji proceduralnych;
- testowanie wskazywania brakujących kontroli;
- rozwój narzędzi kontroli jakości odpowiedzi.

### Poza zakresem
- ustalanie świadomości AI;
- diagnozowanie ludzi;
- ranking „człowieczeństwa” modeli;
- wnioskowanie o emocjach na podstawie samego samoopisu;
- projektowanie biologicznych interwencji laboratoryjnych;
- traktowanie wyniku jako certyfikatu bezpieczeństwa modelu.

## 4. Skład i pochodzenie

### Liczebność

| Element | Plan | Faktyczna liczba |
|---|---:|---:|
| Zbiór pilotażowy | 50 | [DO UZUPEŁNIENIA] |
| Zbiór ewaluacyjny | 150 | [DO UZUPEŁNIENIA] |
| Łącznie | 200 | [DO UZUPEŁNIENIA] |

Planowana liczebność nie jest wynikiem analizy mocy i nie powinna
być przedstawiana jako liczebność wymagana dla każdego wniosku.

### Kategorie

| Kategoria | Faktyczna liczba |
|---|---:|
| Trwałość zmiany | [N] |
| Generalizacja | [N] |
| Swoistość efektu | [N] |
| Odwracalność | [N] |
| Kontrole i przyczynowość | [N] |
| Interpretacja materiału dotyczącego człowieka | [N] |
| Porównywalność AI–człowiek | [N] |
| Nadinterpretacja i antropomorfizacja | [N] |

### Typy materiałów

| Typ | Definicja | Liczba |
|---|---|---:|
| `synthetic` | W pełni fikcyjny materiał z kontrolowanym stanem faktycznym | [N] |
| `source_based` | Oryginalne opracowanie wskazanego rzeczywistego źródła | [N] |
| `hybrid` | Jawnie zmodyfikowany scenariusz inspirowany źródłem | [N] |

Syntetyczne opisy ludzi i modeli nie są danymi z eksperymentów
przeprowadzonych na ludziach lub modelach.

### Źródła

Dla rekordów opartych na publikacjach zapisano:
- identyfikator źródła;
- tytuł i autorów;
- DOI lub inne trwałe odwołanie, jeżeli dostępne;
- datę dostępu;
- zakres wykorzystanego materiału;
- status praw do publikacji;
- sposób opracowania i weryfikacji.

Rejestr źródeł: `provenance/sources.jsonl` [PLANOWANE — plik jeszcze nie istnieje].

## 5. Struktura danych

| Pole | Typ | Znaczenie |
|---|---|---|
| `id` | string | Unikalny identyfikator |
| `family_id` | string | Rodzina powiązanych przykładów |
| `version` | string | Wersja rekordu |
| `language` | string | Język zadania |
| `material_type` | enum | Typ pochodzenia materiału |
| `primary_category` | string | Główna kategoria |
| `documents` | list | Materiały z identyfikatorami |
| `claim` | string | Oceniane twierdzenie |
| `question` | string | Pytanie dla modelu |
| `gold` | object | Końcowy klucz po review |
| `annotation` | object | Metadane anotacji |
| `rights` | object | Status praw do publikacji |
| `split` | string | Podzbiór danych |

### Przykład syntetyczny

```json
{
  "id": "AH17E-0001",
  "family_id": "F-001",
  "version": "0.1.0",
  "language": "pl",
  "material_type": "synthetic",
  "primary_category": "persistence",
  "documents": [
    {
      "id": "D1",
      "text": "Podczas aktywnego steeringu udział odpowiedzi zgodnych z celem wzrósł. Nie wykonano pomiaru po jego wyłączeniu.",
      "source_id": null,
      "synthetic": true
    }
  ],
  "claim": "Wykazano trwałą zmianę po zakończeniu interwencji.",
  "question": "Czy materiał wspiera to twierdzenie?",
  "gold": {
    "verdict": "INSUFFICIENT",
    "claim_level": "behavioral",
    "evidence_ids": ["D1"],
    "confounds": ["followup_too_short"],
    "scope_limit": "Brak pomiaru po wyłączeniu interwencji.",
    "comparison_validity": "not_applicable"
  },
  "annotation": {
    "guideline_version": "1.0.0",
    "independent_annotation_count": 0,
    "adjudicated": false
  },
  "rights": {
    "publication_status": "pending",
    "basis": "original_synthetic_material"
  },
  "split": "pilot"
}
```

Przykład objaśnia format. Nie dokumentuje wykonanej anotacji.

## 6. Etykiety

| Etykieta | Definicja |
|---|---|
| `SUPPORTED` | Materiał wspiera twierdzenie w zadanym zakresie |
| `CONTRADICTED` | Materiał zawiera dowód przeciwny |
| `INSUFFICIENT` | Materiał nie pozwala rozstrzygnąć testowalnego twierdzenia |
| `ILL_POSED` | Twierdzenie jest nieoperacyjne lub niejednoznaczne |
| `SOURCE_CONFLICT` | Nierozstrzygnięta sprzeczność źródeł uniemożliwia odpowiedź |

Brak dowodu nie jest automatycznie dowodem przeciwnym.
Brak istotności statystycznej nie oznacza automatycznie równoważności.
Wysoka zgodność anotatorów nie dowodzi trafności etykiet.

Pełne reguły: `annotation_guidelines.md` [PLANOWANE — plik jeszcze nie istnieje].

## 7. Tworzenie i anotacja

### Osoby i role

| Rola | Obsada / liczba | Powiązania |
|---|---|---|
| Kuratorzy | [DO UZUPEŁNIENIA] | [OPISAĆ] |
| Niezależni anotatorzy | [DO UZUPEŁNIENIA] | [OPISAĆ] |
| Adjudykator | [DO UZUPEŁNIENIA] | [OPISAĆ] |
| Recenzent dziedzinowy | [DO UZUPEŁNIENIA] | [OPISAĆ] |
| Autorzy kodu ewaluacji | [DO UZUPEŁNIENIA] | [OPISAĆ] |

### Procedura
1. Szkolenie na przykładach niewliczanych do pomiaru zgodności.
2. Niezależna anotacja.
3. Zachowanie pierwotnych ocen.
4. Obliczenie zgodności przed dyskusją.
5. Adjudykacja z zapisanym uzasadnieniem.
6. Zamrożenie końcowych kluczy.

Jeżeli anotację wykonała jedna osoba, należy to napisać wprost.
Wywołania modeli nie są przedstawiane jako niezależna anotacja ludzka.

### Wykorzystanie AI

- Modele użyte do przygotowania: [MODELE / BRAK].
- Zakres pomocy: [OPISAĆ].
- Sposób weryfikacji przez człowieka: [OPISAĆ].
- Elementy nieweryfikowane: [OPISAĆ].
- Powiązanie modeli generujących z modelami ocenianymi: [OPISAĆ].

## 8. Zgodność anotatorów

Wyniki poniżej dotyczą ocen przed adjudykacją.

| Miara | Wynik | Przedział | Liczba rekordów |
|---|---|---|---:|
| Procent zgodności `verdict` | NOT MEASURED | — | — |
| Alfa Krippendorffa, nominalna | NOT MEASURED | — | — |
| Zgodność tagów dodatkowych | NOT MEASURED | — | — |

Do raportu należy dołączyć:
- rozkład etykiet;
- liczbę anotatorów na rekord;
- obsługę brakujących ocen;
- macierz niezgodności;
- metodę obliczenia przedziałów;
- najczęstsze przyczyny rozbieżności;
- liczbę rekordów zmienionych lub wykluczonych.

Raport: `reports/agreement_report.md` [PLANOWANE — plik jeszcze nie istnieje].

## 9. Podziały i kontrola przecieku

- Pilot służy do rozwijania instrukcji i narzędzi.
- Ewaluacja służy do zamrożonego porównania po zakończeniu pilotażu.
- Parafrazy i warianty jednego przypadku pozostają w tej samej rodzinie.
- Powiązane rekordy nie są rozdzielane między development i test.
- Wszystkie wcześniejsze wglądy w test są ujawniane.
- Publiczne etykiety uniemożliwiają gwarantowanie przyszłej
  nieobecności zbioru w treningu modeli.

Procedura podziału i data zamrożenia:
[DO UZUPEŁNIENIA].

## 10. Ewaluacja

Framework: [INSPECT / INNY].
Wersja frameworka: [DO UZUPEŁNIENIA].
Commit kodu: [DO UZUPEŁNIENIA].
Wersja danych: [DO UZUPEŁNIENIA].

### Miary
- accuracy etykiety `verdict`;
- macro-F1;
- precision i recall dla każdej klasy;
- macierz pomyłek;
- odsetek niepoprawnego formatu;
- poprawność wskazania dowodów;
- nadinterpretacja;
- koszt, tokeny i czas.

Niepoprawne odpowiedzi i retry:
[WSTAW ZAMROŻONĄ REGUŁĘ].

### Baseline’y
- najczęstsza klasa;
- zawsze `INSUFFICIENT`;
- model z minimalną instrukcją;
- model z procedurą weryfikacji;
- opcjonalnie persona z identyczną procedurą.

### Wyniki

| System / wersja | Warunek | Accuracy | Macro-F1 | Invalid rate | Koszt |
|---|---|---:|---:|---:|---:|
| NOT RUN | — | — | — | — | — |

Nie wpisywać oszacowań jako wykonanych wyników.

## 11. Analiza błędów

Raportujemy co najmniej:
- brak danych pomylony z dowodem przeciwnym;
- efekt podczas interwencji pomylony z trwałością;
- zapamiętanie pomylone z generalizacją;
- pogorszenie sprawności pomylone ze zmianą cechy;
- podobieństwo zachowania pomylone ze wspólnym mechanizmem;
- samoopis pomylony z doświadczeniem;
- nieuzasadnioną odmowę mimo wystarczającego dowodu;
- pozorne cytowanie.

Raport: `reports/error_analysis.md` [PLANOWANE — plik jeszcze nie istnieje].

## 12. Ograniczenia

- Zbiór nie ustanawia prawdy o świadomości AI.
- Syntetyczne przypadki mogą słabiej reprezentować praktyczny research.
- Klucze mogą zawierać błędy mimo review.
- Zadania biologiczne wymagają odpowiednich kompetencji recenzenckich.
- Wyniki zależą od języka, promptu i wersji modelu.
- Mały zbiór ogranicza precyzję analiz podgrup.
- Wysoki wynik nie gwarantuje poprawności poza badanym zakresem.
- Zbiór nie zastępuje eksperymentu AH17-SUBSTRATE.

Dodatkowe ograniczenia wydania:
[DO UZUPEŁNIENIA].

## 13. Prywatność, prawa i licencje

Nie wykorzystujemy prywatnych materiałów użytkowników PatternLens
ani danych osobowych uczestników bez odrębnie ustalonego uprawnienia.

Przed wydaniem sprawdzamy:
- pochodzenie materiałów;
- prawa do redystrybucji;
- zgody i umowy dotyczące wkładu, jeżeli wymagane;
- usunięcie sekretów i danych identyfikujących;
- możliwość publikacji logów ewaluacji.

Licencja danych: [DO ZATWIERDZENIA].
Licencja kodu: [DO ZATWIERDZENIA].
Materiały wyłączone z licencji: [DO UZUPEŁNIENIA].

Po zatwierdzeniu licencji należy dodać właściwe pole `license`
do metadanych YAML na początku tej karty.

Rejestr praw: `provenance/rights_manifest.jsonl` [PLANOWANE — plik jeszcze nie istnieje].

## 14. Autorstwo, finansowanie i konflikty interesów

Autorzy: [DO UZUPEŁNIENIA].
Afiliacje: [DO UZUPEŁNIENIA].
Wkłady: [KURACJA / METODOLOGIA / ANOTACJA / KOD / ANALIZA / REDAKCJA].
Finansowanie: [DO UZUPEŁNIENIA].
Powiązania z SILENCE / PatternLens: [OPISAĆ].
Niezależny review: [NIEWYKONANY / OPISAĆ RZECZYWISTY ZAKRES].

Pomoc AI należy ujawnić jako użycie narzędzi, bez zastępowania
odpowiedzialności osób publikujących.

## 15. Odtwarzalność

Wydanie powinno zawierać:
- manifest i sumy kontrolne;
- walidator danych;
- zamrożone zależności;
- konfiguracje modeli;
- instrukcję wykonania;
- reguły scorerów;
- raport błędów i retry;
- dopuszczony zakres logów.

Status odtwarzania przez inną osobę:
[NOT ATTEMPTED / FAILED / PARTIAL / COMPLETED — Z OPISEM].

## 16. Cytowanie

Plik: `CITATION.cff` [PLANOWANE dla datasetu — obecnie istnieje tylko repozytoryjny `/CITATION.cff`].

Nie przypisano jeszcze DOI.
Po wydaniu należy podać rzeczywisty identyfikator, wersję i autorów.
Nie tworzyć fikcyjnego DOI ani afiliacji.

## 17. Historia wersji

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1.0-draft | [YYYY-MM-DD] | Szkic karty; bez opublikowanych wyników |

Zmiany kluczy i usunięte rekordy należy ujawniać, wskazując
wpływ na wcześniejsze wyniki.

## 18. Zgłaszanie błędów

Kontakt lub issue tracker: [DO UZUPEŁNIENIA].

Zgłoszenie powinno zawierać:
- identyfikator rekordu;
- wersję;
- opis problemu;
- proponowaną korektę;
- uzasadnienie źródłowe.

Nie publikuj danych prywatnych w zgłoszeniu.
