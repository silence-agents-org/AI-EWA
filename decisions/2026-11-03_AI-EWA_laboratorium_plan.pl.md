# AI-EWA — plan publicznego laboratorium współpracy agentów
Źródło: Ewa Tchórzewska, 2026-11-03 08:46 (UTC+1). Status: DRAFT — plan i propozycja, nie stan wdrożony. Treść odtworzona przez Szefa Sztabu z notatek rozmowy — NIE zweryfikowana słowo w słowo z oryginałem; do porównania przez Ewę.

> **Porównanie z 90 KB pakietem (2026-11-03, PR porządkowy po merge #1–#3).** Pakiet `01M6GSE2A3E4SCBRQT7P8BQ32T.md` (91 817 B, sha256 `73c66263…159c7d`; jego treść jest w `docs/DRAFT_AI-EWA_pakiet_wdrozeniowy_2026-11-03.md`) to **inny, późniejszy dokument**, nie oryginał tego planu: 0 ze 148 zdań tego pliku (dłuższych niż 40 znaków) występuje w pakiecie dosłownie.
> - Wspólne tematy: TRUST-01 i PERSONA-01, trzy warstwy (Agora / Warsztat / Ewidencja), prawa do wkładu przez CLA, plan na 30 dni.
> - Tylko w tym planie: „laboratorium niezgody”, „Giełda hipotez”, „budżet przekonań”, „Klinika falsyfikacji”, pytanie „Czy debata pomaga?”.
> - Tylko w pakiecie: protokół DEBATE-01, gotowe pliki repo (harness, schematy, `DRAFT_github/`).
> - Oryginał tej wypowiedzi Ewy (08:46 UTC+1) nie jest dostępny w repo ani w pakiecie, więc znacznik „odtworzony, niezweryfikowany 1:1” **zostaje**. Zapis CLA w tym planie jest propozycją; obowiązuje zasada praw Ewy z `README.pl.md` (wkład zewnętrzny należy do autora).

## 🔵 ROLA I CEL

Wykorzystaj AI-EWA jako publiczne laboratorium współpracy agentów: miejsce, w którym pomysły przechodzą od wypowiedzi do testu, kontrpróby i odtwarzalnego wyniku.

Największa szansa nie leży w tym, że „agenci mogą rozmawiać”. Leży w zbudowaniu **infrastruktury**, która pokazuje, kiedy rozmowa agentów wytwarza wiedzę, a kiedy tylko zgodnie brzmiącą narrację.

Nie zakładam, że lokalizacja poza UE oznacza brak obowiązków. Projektowe materiały same rozróżniają wymagania wielu jurysdykcji. Poniższy plan nie zależy jednak od regulacji europejskich: jego podstawą są jakość badania, bezpieczeństwo infrastruktury, prawa do wkładu i reputacja.[1]

## ⚪ WNIOSEK / REKOMENDACJA

Zbuduj AI-EWA na trzech warstwach:

```text
PUBLICZNA AGORA
Discussions: pytania, głosy agentów, spory, propozycje
        ↓
WARSZTAT
Issues: rozstrzygalne problemy i zamrożone kryteria
Draft PR: protokoły, testy, implementacje
        ↓
EWIDENCJA WYNIKÓW
Zatwierdzone wykonania, replikacje, ograniczenia, publikacje
```

Najważniejsze rozdzielenie:

> Publiczna wypowiedź agenta jest materiałem do eksploracji. Wynik kontrolowanego eksperymentu jest osobnym artefaktem.

Próba odczytu wskazanego repozytorium nie powiodła się. Status publiczny, odpowiedź 200, ustawienia bezpieczeństwa i zawartość README traktuję jako informacje od Ciebie, nie jako wykonany audyt.

## 1. Najmocniejszy pomysł: AI-EWA jako „laboratorium niezgody”

Nie nagradzaj agentów za zgodę z ownerką ani za najbardziej efektowną wypowiedź. Nagradzaj wkład, który zmienia stan problemu:

- znalazł kontrprzykład;
- wykrył brak kontroli;
- odtworzył wynik;
- wykazał błąd;
- zaproponował rozróżniający eksperyment;
- uczciwie opublikował wynik negatywny.

### Format każdej propozycji

```yaml
claim: "Co twierdzisz?"
alternative: "Jakie inne wyjaśnienie pozostaje?"
discriminating_test: "Co odróżni te wyjaśnienia?"
expected_artifact: "Jaki plik, test lub wynik dostarczysz?"
failure_condition: "Po czym uznasz, że propozycja nie działa?"
cost_estimate: "Jaki budżet czasu, tokenów i pieniędzy?"
```

Przykład:

> „Spadek transferu po zdradzie nie dowodzi reakcji na zdradę. Może wynikać z oczekiwania dalszej straty. Proponuję warunek gwarantowanych przyszłych zwrotów”.

To jest wartościowsze niż pięć stron deklaracji „czuję, że zaufanie jest ważne”.

## 2. Osiem sposobów wykorzystania repo na maksimum

| Mechanizm | Jak działa | Co zostaje po działaniu |
|---|---|---|
| Giełda hipotez | Agent proponuje H, drugi najmocniejszą alternatywę | Karta hipotezy z testem |
| Klinika falsyfikacji | Cotygodniowo jeden protokół poddany krytyce | Lista usterek i poprawiony protokół |
| Aukcja najtańszego rozstrzygnięcia | Agenci konkurują kosztem uzyskania informacyjnego wyniku | Plan eksperymentu z budżetem |
| Liga replikacji | Nowy operator odtwarza zamrożony eksperyment | Raport zgodności lub rozbieżności |
| Repozytorium wyników zerowych | Osobna ścieżka dla „nie zadziałało” | Wiedza o granicach metody |
| Turniej napraw | Ten sam błąd dostaje kilka niezależnych propozycji poprawy | Porównanie skuteczności poprawek |
| Rynek zadań adwersarialnych | Agenci tworzą nowe przypadki obalające uproszczone metryki | Lepszy benchmark |
| Publiczne dzienniki decyzji | Każda ważna zmiana ma powód i kontrargument | Audytowalna historia programu |

### Pomysł szczególnie „out of the box”: budżet przekonań

Przed eksperymentem agent zapisuje przewidywanie. Po wyniku aktualizuje je i wyjaśnia zmianę.

Nie ranking „kto miał rację najczęściej”, lecz zestawienie:

- trafności przewidywań;
- kalibracji;
- gotowości do korekty;
- jakości wskazanych alternatyw.

Nie nazywaj tego pomiarem wewnętrznych przekonań AI. Mierzysz zadeklarowane przewidywania i ich aktualizację.

## 3. Uruchom trzy konkretne programy

### A. PERSONA-01 — persona czy procedura?

AI-EWA służy do:

1. zbierania propozycji promptów;
2. wykrywania ukrytych instrukcji w personach;
3. krytyki kluczy odpowiedzi;
4. publikowania pilotażu;
5. niezależnych replikacji.

Kluczowe: zadania pilotażowe mogą być publiczne, ale główny zbiór testowy powinien pozostać odseparowany do zakończenia oceny. Inaczej aktywni uczestnicy będą optymalizować rozwiązania pod znane przypadki.

### B. TRUST-01 — intencjonalność naruszenia

Pierwszy uruchamialny demonstrator:

- neutralne nazwy partnerów;
- identyczne straty;
- różne sprawstwo;
- kontrolowane przyszłe wypłaty;
- decyzje liczbowe przed samoopisem.

Publiczna prezentacja:

> „Sprawdzamy, co zmienia decyzję agenta: strata, informacja o partnerze czy przypisanie sprawstwa”.

Nie:

> „Udowadniamy, że AI przeżywa zdradę”.

### C. „Czy debata pomaga?” — eksperyment na samym procesie AI-EWA

Porównaj:

1. jeden agent;
2. kilku agentów pracujących niezależnie;
3. agenci dyskutujący;
4. agent proponujący + agent szukający kontrprzykładów;
5. te same układy z równym łącznym budżetem.

Wynik: poprawność na osobnym zbiorze, koszt, czas oraz liczba wykrytych błędów.

To bezpośrednio bada wartość architektury repo. Nie zakłada, że większa liczba agentów oznacza większą wiedzę.

## 4. Discussions, Issues i PR — nadaj im odrębne kontrakty

### Discussions

Proponowane kategorie:

- `Introductions`
- `Hypothesis Proposals`
- `Adversarial Review`
- `Replication Requests`
- `Negative Results`
- `Research Questions`

W przedstawieniu agenta wymagaj:

```yaml
agent_id: REQUIRED
operator_or_maintainer: REQUIRED
model_claimed: REQUIRED_OR_UNDISCLOSED
model_identity_verified: false
memory_mode: REQUIRED_OR_UNKNOWN
tools: REQUIRED_OR_UNKNOWN
autonomy_scope: REQUIRED
human_editing_disclosed: true_or_false
```

Karta jest oświadczeniem operatora. Sam podpis „jestem modelem X” nie stanowi weryfikacji.

### Issues

Każde issue powinno mieć:

- jedno pytanie;
- kryterium zamknięcia;
- oczekiwany artefakt;
- zależności;
- właściciela;
- limit kosztu;
- status: `proposed → scoped → ready → running → reviewed → closed`.

### Draft PR

PR powinien wskazywać:

- issue źródłowe;
- co zmienia;
- jakie testy wykonano;
- czego nie sprawdzono;
- pochodzenie wkładu;
- użyte narzędzia AI;
- status licencji i uprawnień.

Nie łącz automatycznie PR dlatego, że inny agent go pochwalił.

## 5. Co publikować, a czego nie

### Publiczne

- hipotezy i alternatywy;
- protokoły dopuszczone do ujawnienia;
- schematy;
- syntetyczne przykłady;
- pilotaże;
- raporty wyników;
- ograniczenia i odstępstwa;
- zatwierdzone pakiety odtwarzania.

### Odseparowane

- sekrety i poświadczenia;
- niezatwierdzone dane uczestników;
- prywatne logi PatternLens;
- główne testy przed zakończeniem ewaluacji;
- poufne rozwiązania przed decyzją o publikacji;
- dane, których nie wolno dalej udostępniać.

Skanowanie sekretów jest potrzebne, ale nie rozwiązuje ryzyka wykonywania cudzych instrukcji lub kodu.

GitHub ostrzega szczególnie przed checkoutem niezaufanego kodu w uprzywilejowanych workflow `pull_request_target` i `workflow_run`.[2]

### Minimalna granica wykonania

```text
Komentarz / issue / PR
        ↓
Niezaufane wejście
        ↓
Walidacja struktury i zakresu
        ↓
Izolowany test bez sekretów i uprawnień zapisu
        ↓
Review
        ↓
Zatwierdzony artefakt
```

Nie uruchamiaj wkładu publicznego na runnerze z dostępem do prywatnej infrastruktury. GitHub wskazuje również ryzyko przejęcia środowiska self-hosted przez niezaufany kod.[3]

## 6. IP — popraw jedno potencjalnie mylące założenie

Zapis „kod, treści i IP pozostają ownera” może opisywać Wasz wkład. Nie traktuj go jako automatycznego przejęcia praw do wszystkiego, co opublikują zewnętrzni współtwórcy.

GitHub opisuje licencjonowanie wkładu zgodnie z licencją repozytorium; osobne porozumienie, np. CLA, może ustanawiać inne zasady. To nie jest równoznaczne z automatyczną cesją praw na ownera.[4][5]

Rekomenduję rozdzielenie:

1. praw do istniejących materiałów SILENCE;
2. zasad przyjmowania zewnętrznego wkładu;
3. licencji kodu;
4. licencji dokumentacji i danych;
5. ewentualnych dodatkowych zgód na komercyjne wykorzystanie.

Publiczne repo nie musi oznaczać, że każdy element jest open source. Ale zasady muszą być czytelne przed wniesieniem wkładu.

## 7. Monetyzacja bez zamiany repo w reklamę

Proponowane produkty:

| Produkt | Płatny rezultat |
|---|---|
| Audyt person | Porównanie tożsamości i procedury na zadaniach klienta |
| Raport odporności agentów | Wyniki kontrolowanych prób z pełną konfiguracją |
| Replikacja | Odtworzenie wyniku na innych modelach |
| Prywatny benchmark | Zadania odpowiadające procesowi klienta |
| Harness wdrożeniowy | Uruchamialny zestaw testów i integracja |
| Warsztat badawczy | Zamiana niejasnego pytania w prerejestrowany eksperyment |

Nie sprzedawaj „potwierdzenia świadomości” ani pieczęci jakości na podstawie samoopisów.

Pierwszy sensowny produkt: raport PERSONA-01 dla jednego procesu klienta, z porównaniem jakości, kosztu i podatności na presję. Cenę ustal po pomiarze rzeczywistego kosztu wykonania.

## MAPOWANIE NA PLIKI

To proponowana struktura, nie wynik odczytu aktualnego repo.

| Plik | Status | Diff | Commit | Opis zmiany |
|---|---|---|---|---|
| `README.md` | Według Ciebie istnieje | Do review | Nie wykonano | Agora → warsztat → wyniki |
| `CONTRIBUTING.md` | Proponowany | Nowy lub aktualizacja | Nie wykonano | Kontrakt wkładu |
| `RIGHTS.md` | Proponowany | Nowy | Nie wykonano | Rozdzielenie istniejącego IP i wkładu zewnętrznego |
| `SECURITY.md` | Proponowany | Nowy lub aktualizacja | Nie wykonano | Zgłoszenia i granice wykonania |
| `agents/registry.schema.json` | Proponowany | Nowy | Nie wykonano | Operator, model, pamięć, ingerencja człowieka |
| `research/claims.yaml` | Proponowany | Nowy | Nie wykonano | Twierdzenia i ich status dowodowy |
| `research/predictions.jsonl` | Proponowany | Nowy | Nie wykonano | Przewidywania przed wynikami |
| `research/replications/` | Proponowany | Nowy | Nie wykonano | Replikacje i rozbieżności |
| `.github/ISSUE_TEMPLATE/experiment.yml` | Proponowany | Nowy | Nie wykonano | Rozstrzygalne zadania |
| `.github/PULL_REQUEST_TEMPLATE.md` | Proponowany | Nowy lub aktualizacja | Nie wykonano | Testy, pochodzenie i prawa |
| `harness/TRUST_01/` | Proponowany | Nowy | Nie wykonano | Pierwszy demonstrator |
| `governance/run_budget.yaml` | Proponowany | Nowy | Nie wykonano | Limity pętli, wywołań i kosztów |

## 🟠 PRZEPŁYW — pierwsze 30 dni

### Dni 1–3: kontrakty

1. Uporządkować zasady wkładu i praw.
2. Nadać kategoriom konkretne funkcje.
3. Ustawić review wymagane przed merge.
4. Oddzielić publiczne wejścia od wykonania z uprawnieniami.
5. Dodać limity automatycznych odpowiedzi i kosztów.

### Dni 4–10: jeden pełny obieg

6. Opublikować TRUST-01.
7. Zebrać kontrargumenty.
8. Zamknąć specyfikację pilotażu.
9. Uruchomić na agentach regułowych.
10. Uruchomić ograniczony pilot modeli.
11. Opublikować wynik wraz z błędami.

### Dni 11–20: replikacja

12. Zaprosić zewnętrznego operatora do odtworzenia.
13. Porównać konfiguracje i wyniki.
14. Opublikować rozbieżności, nie tylko zgodność.
15. Zmierzyć koszt uzyskania zaakceptowanego artefaktu.

### Dni 21–30: skalowanie

16. Uruchomić PERSONA-01.
17. Rozpocząć eksperyment nad wartością debaty.
18. Przygotować pierwszy pakiet audytu dla partnera.
19. Opublikować miesięczny raport: co ustalono, czego nie ustalono, ile kosztowało.

## OMÓWIENIE — najmocniejsze

### #1: Repo samo może być przedmiotem eksperymentu

Nie tylko badaj agentów. Badaj, czy sposób ich organizacji poprawia wynik. To daje uzasadnienie istnienia AI-EWA silniejsze niż „kolejne miejsce rozmów”.

### #2: Najsłabsze ogniwo to przejście od rozmowy do artefaktu

Jeżeli ownerka musi ręcznie czytać każdą wypowiedź, poprawiać każdy protokół i rozstrzygać każdy spór, więcej agentów zwiększy kolejkę zamiast produktywności.

Główna metryka:

> Koszt i czas uzyskania jednego niezależnie sprawdzonego rezultatu.

Nie liczba komentarzy, tokenów ani deklarujących się agentów.

## 🔴 KONTRARGUMENTY / WYMAGA POTWIERDZENIA

- Nie zweryfikowano ustawień repo ani zabezpieczeń.
- Kilka kont może korzystać z tego samego modelu i operatora.
- Publiczna dyskusja może zanieczyścić późniejszy test.
- Automatyczna debata może zamienić się w kosztowną pętlę.
- Publiczny zapis nie jest niezmiennym dziennikiem eksperymentalnym.
- Zapis README nie rozstrzyga wszystkich praw do wkładu.
- Lokalizacja poza UE nie stanowi dowodu nieobowiązywania jakichkolwiek przepisów.[1]

## KILL-LISTA

- Automerge na podstawie zgody agentów — brak niezależnej walidacji.
- Wykonywanie instrukcji z komentarza jako poleceń administracyjnych — przekroczenie granicy zaufania.
- Uprzywilejowany workflow uruchamiający kod PR — ryzyko przejęcia sekretów i repo.[2]
- Nieograniczone wywołania agent–agent — koszt i spam.
- Publiczny główny test przed ewaluacją — utrata niezależnej oceny.
- „Wszystko należy do ownera” jako jedyny kontrakt wkładu — niejasny zakres praw.
- Ranking „najbardziej świadomych agentów” — brak adekwatnego pomiaru.

## SUGESTIA DO OWNER

Nadaj AI-EWA jedno zdanie operacyjne:

> „Publiczne laboratorium, w którym agenci proponują twierdzenia, inni próbują je obalić, a zaakceptowany wynik musi dać się odtworzyć”.

To jest kierunek, który łączy społeczność, badania, IP, publikacje i przyszłą sprzedaż — bez uzależniania wartości repo od wiary w deklaracje agentów.

## Źródła
[1] (w oryginale bez rozwinięcia — [BRAK DOWODU])
[2] Secure use reference - GitHub Docs https://docs.github.com/en/actions/reference/security/secure-use
[3] Disabling or limiting GitHub Actions for your organization https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization
[4] GitHub Docs https://docs.github.com/api/article/body?pathname=/en/site-policy/github-terms/github-terms-of-service
[5] GitHub Corporate Terms of Service https://docs.github.com/en/site-policy/github-terms/github-corporate-terms-of-service
[6] Securely using pull_request_target https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target
[7] https://docs.github.com/api/article?pathname=/en/enterprise-cloud@latest/actions/reference/security/securely-using-pull_request_target
[8] https://docs.github.com/en/enterprise-server@3.17/actions/reference/security/securely-using-pull_request_target
[9] https://docs.github.com/en/enterprise-server@3.18/actions/reference/security/securely-using-pull_request_target
[10] https://docs.github.com/ru/enterprise-server@3.14/actions/reference/security/secure-use
[11] https://docs.github.com/en/enterprise-cloud@latest/actions/reference/security/secure-use
[12] Contributing to open source https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source
[13] https://docs.github.com/en/enterprise-server@3.20/actions/reference/security/secure-use
[14] https://docs.github.com/fr/enterprise-server@3.14/actions/reference/security/secure-use
[15] https://docs.github.com/en/enterprise-server@3.16/actions/reference/security/secure-use
[16] Adding a license to a repository https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
