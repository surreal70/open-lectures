---
author: Prof. Dr. Schmidt
created: 2026-10-01
modified: 2026-10-09
tags:
  - content
  - algorithmen
  - sortierung
---

> [!info] **Lernziele**
> - Die wichtigsten Sortieralgorithmen kennen und unterscheiden können
> - Zeitkomplexität von Sortieralgorithmen analysieren können
> - Geeigneten Sortieralgorithmus für verschiedene Anwendungsfälle auswählen können

## Überblick

Sortieralgorithmen ordnen Elemente einer Liste nach einem bestimmten Kriterium. Sie gehören zu den grundlegendsten Algorithmen der Informatik und dienen als Basis für viele komplexere Verfahren.

## Bubble Sort

Bubble Sort ist ein einfacher Sortieralgorithmus, der benachbarte Elemente vergleicht und bei falscher Reihenfolge vertauscht.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

> [!note] **Hinweis**
> Bubble Sort ist für große Datenmengen ineffizient, eignet sich aber gut für Lehrzwecke.

**Zeitkomplexität:** $O(n^2)$

## Quick Sort

Quick Sort ist ein effizienter Divide-and-Conquer-Algorithmus.

```
┌─────────────────────────────────────┐
│  [8, 3, 7, 1, 5, 9, 2]              │
│           ↓ Pivot: 5                │
│  [3, 1, 2] | 5 | [8, 7, 9]          │
│       ↓           ↓                 │
│  [1, 2, 3]    [7, 8, 9]             │
│           ↓                         │
│  [1, 2, 3, 5, 7, 8, 9]              │
└─────────────────────────────────────┘
```

*<span class="fig-id">01-sortieralgorithmen-1</span>: Visualisierung des Quick Sort Algorithmus mit Pivot-Element.*

> [!tip] **Merkhilfe**
> "Quick Sort teilt und herrscht" – Das Pivot-Element teilt die Liste, dann wird rekursiv sortiert.

**Zeitkomplexität:** 
- Best/Average Case: $O(n \log n)$
- Worst Case: $O(n^2)$

## Merge Sort

Merge Sort teilt die Liste rekursiv in Hälften und fügt sie sortiert zusammen.

> [!example] **Beispiel**
> Liste `[38, 27, 43, 3]` wird zu `[38, 27]` und `[43, 3]` geteilt, dann weiter zu Einzelelementen, und schließlich sortiert zusammengeführt.

**Zeitkomplexität:** $O(n \log n)$ (garantiert)

## Zusammenhänge

Querverweise zu anderen relevanten Dokumenten im Vault:

- → [[01-Grundlagen/01-Komplexitaetsanalyse]]
- → [[02-Datenstrukturen/01-Arrays-und-Listen]]
- → [[03-Algorithmen/02-Rekursion]]

> [!warning] **Prüfungsrelevant**
> - Zeitkomplexitäten aller drei Algorithmen (Best, Average, Worst Case)
> - Unterschied zwischen stabilen und instabilen Sortierverfahren
> - Wann welcher Algorithmus geeignet ist

> [!question] **Typische Prüfungsfragen**
> - Erklären Sie den Unterschied zwischen Bubble Sort und Quick Sort bezüglich der Zeitkomplexität.
> - Warum ist Merge Sort für große Datenmengen besser geeignet als Bubble Sort?
> - Führen Sie Quick Sort auf der Liste [5, 2, 8, 1, 9] mit Pivot = erstes Element durch.

## Quellen

- Cormen, T. H. et al.: Introduction to Algorithms, 4th Edition, MIT Press, 2022
- Sedgewick, R.: Algorithms, 4th Edition, Addison-Wesley, 2011

> [!tip] **Weiterführende Links**
> - [Visualgo - Sorting Algorithms](https://visualgo.net/en/sorting)
> - [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
> - [[Anhang/01-Sortieralgorithmen-Vergleich]]
