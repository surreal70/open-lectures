---
author: Dr. Müller
created: 2026-10-05
modified: 2026-10-09
tags:
  - uebung
  - komplexitaet
---

> [!info] **Lernziele**
> - Zeitkomplexität aus Code ableiten können
> - Komplexitätsklassen vergleichen können
> - Praktische Anwendung der Big-O-Notation

## Überblick

Übungsaufgaben zur Komplexitätsanalyse mit Lösungen.

## Aufgabe 1

Bestimmen Sie die Zeitkomplexität:

```python
def mystery(n):
    for i in range(n):
        for j in range(i):
            print(i, j)
```

> [!abstract] **Lösung**
> $O(n^2)$ – Die innere Schleife läuft im Durchschnitt $n/2$ mal.

## Aufgabe 2

Ordnen Sie nach Wachstum: $n!$, $2^n$, $n^2$, $n \log n$

> [!abstract] **Lösung**
> $n \log n < n^2 < 2^n < n!$

## Aufgabe 3

Analysieren Sie die folgende Funktion:

```python
def search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

> [!abstract] **Lösung**
> $O(\log n)$ – Binäre Suche halbiert den Suchbereich in jedem Schritt.

## Zusammenhänge

- → [[01-Grundlagen/01-Komplexitaetsanalyse]]

> [!warning] **Prüfungsrelevant**
> - Alle Aufgabentypen sind klausurrelevant

> [!question] **Typische Prüfungsfragen**
> - Siehe Aufgaben oben

## Quellen

- Übungsblatt 1, Algorithmen und Datenstrukturen, WS 2026/27

> [!tip] **Weiterführende Links**
> - [[01-Grundlagen/01-Komplexitaetsanalyse]]
