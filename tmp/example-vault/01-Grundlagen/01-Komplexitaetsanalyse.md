---
author: Prof. Dr. Schmidt
created: 2026-10-02
modified: 2026-10-09
tags:
  - content
  - grundlagen
  - komplexitaet
---

> [!info] **Lernziele**
> - Die Big-O-Notation verstehen und anwenden können
> - Zeitkomplexität von Algorithmen bestimmen können
> - Verschiedene Komplexitätsklassen unterscheiden können

## Überblick

Die Komplexitätsanalyse ermöglicht es, die Effizienz von Algorithmen unabhängig von der Hardware zu bewerten.

## Big-O-Notation

Die Big-O-Notation beschreibt das asymptotische Verhalten eines Algorithmus.

$$O(f(n)) = \{ g(n) : \exists c > 0, n_0 > 0 \text{ sodass } g(n) \leq c \cdot f(n) \text{ für alle } n \geq n_0 \}$$

> [!note] **Hinweis**
> Big-O beschreibt die obere Schranke – den "schlimmsten Fall" des Wachstums.

## Komplexitätsklassen

| Klasse | Beispiel |
|--------|----------|
| $O(1)$ | Array-Zugriff |
| $O(\log n)$ | Binäre Suche |
| $O(n)$ | Lineare Suche |
| $O(n \log n)$ | Merge Sort |
| $O(n^2)$ | Bubble Sort |

![[.assets/komplexitaet-graph.png]]
*<span class="fig-id">01-komplexitaetsanalyse-1</span>: Vergleich der Wachstumsraten verschiedener Komplexitätsklassen.*

## Analyse-Methoden

> [!example] **Beispiel**
> ```python
> for i in range(n):      # n Iterationen
>     for j in range(n):  # n Iterationen
>         print(i, j)     # O(1)
> # Gesamt: O(n²)
> ```

## Zusammenhänge

- → [[01-Grundlagen/02-Einfuehrung]]
- → [[03-Algorithmen/01-Sortieralgorithmen]]
- → [[Glossar#Komplexität]]

> [!warning] **Prüfungsrelevant**
> - Definition der Big-O-Notation
> - Bestimmung der Komplexität aus Code
> - Vergleich von Komplexitätsklassen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Zeitkomplexität des folgenden Codes.
> - Ordnen Sie die Funktionen $n^2$, $n \log n$, $2^n$ nach Wachstum.
> - Erklären Sie den Unterschied zwischen O(n) und Θ(n).

## Quellen

- Cormen, T. H. et al.: Introduction to Algorithms, Kapitel 3, MIT Press, 2022

> [!tip] **Weiterführende Links**
> - [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
> - [[Uebungsaufgaben/01-Komplexitaet-Uebung]]
