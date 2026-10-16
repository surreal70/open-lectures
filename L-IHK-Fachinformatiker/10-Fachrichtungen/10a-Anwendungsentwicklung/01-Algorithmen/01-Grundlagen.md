---
title: "Algorithmen-Grundlagen"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11a
  - algorithmen
  - komplexitaet
  - o-notation
  - laufzeit
source: proTirone (CC-BY-4.0)
---

# Algorithmen-Grundlagen

> [!info] Lernziele
> - O-Notation verstehen und anwenden
> - Komplexitätsklassen unterscheiden
> - Algorithmen nach Kriterien bewerten

## Zusammenhang Suchen und Sortieren

**Suchen** und **Sortieren** sind eng miteinander verknüpft:

- Manche Suchverfahren setzen sortierte Daten voraus (z.B. binäre Suche)
- Manche Sortierverfahren nutzen intern Suchoperationen

```
┌─────────────────────────────────────────────────────────┐
│                    ALGORITHMEN                          │
├──────────────────────┬──────────────────────────────────┤
│       SUCHEN         │          SORTIEREN               │
├──────────────────────┼──────────────────────────────────┤
│ • Lineare Suche      │ • Insertion Sort                 │
│ • Binäre Suche       │ • Selection Sort                 │
│ • Baumsuche          │ • Bubble Sort                    │
│ • Wegesuche          │ • Quick Sort                     │
│                      │ • Merge Sort                     │
└──────────────────────┴──────────────────────────────────┘
```

## Bewertungskriterien

Algorithmen werden nach drei Hauptkriterien verglichen:

### 1. Geschwindigkeit (Laufzeitverhalten)

Angegeben in **O-Notation**, bezogen auf die Anzahl der Elemente `n`:

| Notation | Name | Beispiel |
|----------|------|----------|
| O(1) | Konstant | Array-Zugriff per Index |
| O(log n) | Logarithmisch | Binäre Suche |
| O(n) | Linear | Lineare Suche |
| O(n log n) | Linearithmisch | Merge Sort, Quick Sort (avg) |
| O(n²) | Quadratisch | Bubble Sort, Insertion Sort |
| O(2ⁿ) | Exponentiell | Rekursives Fibonacci |

### 2. Speicherbedarf (Platzkomplexität)

Wie viel zusätzlicher Speicher wird benötigt?

| Notation | Bedeutung |
|----------|-----------|
| O(1) | In-place, konstanter Zusatzspeicher |
| O(log n) | Logarithmischer Zusatzspeicher (z.B. Rekursionsstack) |
| O(n) | Linearer Zusatzspeicher (Kopie der Daten) |

### 3. Stabilität

> [!note] Definition
> Ein Sortieralgorithmus ist **stabil**, wenn er die relative Reihenfolge von Elementen mit gleichem Sortierschlüssel beibehält.

**Beispiel:** Sortierung nach Nachname

```
Eingabe:  [{Anton, First}, {Dorothea, Last}, {Bertram, First}]

Stabil:   [{Anton, First}, {Bertram, First}, {Dorothea, Last}]
          (Anton bleibt vor Bertram, da beide "First" heißen)

Instabil: [{Bertram, First}, {Anton, First}, {Dorothea, Last}]
          (Reihenfolge von Anton/Bertram nicht garantiert)
```

## O-Notation (Landau-Symbole)

Die **O-Notation** beschreibt das asymptotische Verhalten eines Algorithmus:

- Abstrahiert von konkreter Hardware
- Abstrahiert von Implementierungsdetails
- Beschreibt Wachstum bei steigender Eingabegröße

### Komplexitätsklassen

```
Wachstum
    │
    │                                    ╱ O(2ⁿ) exponentiell
    │                                 ╱
    │                              ╱
    │                           ╱
    │                        ╱        ╱ O(n²) quadratisch
    │                     ╱       ╱
    │                  ╱      ╱
    │               ╱     ╱
    │            ╱    ╱          ╱ O(n log n)
    │         ╱   ╱          ╱
    │      ╱  ╱          ╱        ╱ O(n) linear
    │    ╱╱          ╱        ╱
    │ ╱╱         ╱        ╱          ╱ O(log n)
    │─────────────────────────────── O(1) konstant
    └─────────────────────────────────▶ n (Eingabegröße)
```

### Rangfolge (von schnell nach langsam)

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n)$$

## Vergleich der Sortieralgorithmen

| Algorithmus | Best | Average | Worst | Platz | Stabil |
|-------------|------|---------|-------|-------|--------|
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Ja |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ Nein |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Ja |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ Nein |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Ja |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ Nein |

## Best/Average/Worst Case

| Fall | Bedeutung | Beispiel (Bubble Sort) |
|------|-----------|------------------------|
| **Best Case** | Günstigster Fall | Bereits sortierte Liste |
| **Average Case** | Durchschnitt | Zufällig angeordnete Liste |
| **Worst Case** | Ungünstigster Fall | Rückwärts sortierte Liste |

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Was bedeutet O(n²)?
> - Ordnen Sie die Komplexitätsklassen nach Wachstum
> - Welcher Algorithmus ist für kleine/große Datenmengen geeignet?
> - Was bedeutet "stabiler Sortieralgorithmus"?

## Querverweise

- → [[../02-Suchalgorithmen/01-Lineare-Suche|Lineare Suche]]
- → [[../02-Suchalgorithmen/02-Binaere-Suche|Binäre Suche]]
- → [[../03-Sortieralgorithmen/01-Einfache-Verfahren|Einfache Sortierverfahren]]

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
