---
title: "Näherungsverfahren"
chapter: "06"
section: "11"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Wurzeln durch Intervallschachtelung approximieren"
  - "Das Heron-Verfahren anwenden können"
  - "Näherungswerte abschätzen"
  - "Die Genauigkeit von Näherungen beurteilen"
tags:
  - mathematik
  - naeherung
  - approximation
  - heron
created: 2026-10-13
modified: 2026-10-13
---

# Näherungsverfahren

> [!info] Lernziele
> - Wurzeln durch Intervallschachtelung approximieren
> - Das Heron-Verfahren anwenden können
> - Näherungswerte abschätzen
> - Die Genauigkeit von Näherungen beurteilen

## Überblick

**Näherungsverfahren** erlauben die Berechnung von Wurzeln ohne Taschenrechner.

## Intervallschachtelung

**Beispiel:** $\sqrt{20}$ bestimmen

| Schritt | Intervall | Mitte | Mitte² |
|---------|-----------|-------|--------|
| 1 | [4; 5] | 4,5 | 20,25 (zu groß) |
| 2 | [4; 4,5] | 4,25 | 18,06 (zu klein) |
| 3 | [4,25; 4,5] | 4,375 | 19,14 (zu klein) |
| 4 | [4,375; 4,5] | 4,4375 | 19,69 |

**Ergebnis:** $\sqrt{20} \approx 4,47$

## Heron-Verfahren

**Formel:**
$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

**Beispiel:** $\sqrt{10}$, Startwert $x_0 = 3$

| n | $x_n$ | $10/x_n$ | $x_{n+1}$ |
|---|-------|----------|-----------|
| 0 | 3 | 3,333 | 3,1667 |
| 1 | 3,1667 | 3,158 | 3,1623 |
| 2 | 3,1623 | 3,1623 | 3,1623 |

**Ergebnis:** $\sqrt{10} \approx 3,162$

## Zusammenhänge

### Voraussetzungen

- [[06-Quadratwurzeln]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Niedrig-Mittel
> Mathematisches Verständnis, selten in Prüfungen.

## Typische Prüfungsfragen

1. Bestimme $\sqrt{30}$ durch Intervallschachtelung (2 Schritte).
2. Führe einen Schritt des Heron-Verfahrens für $\sqrt{5}$ durch.

## Quellen

- Lambacher Schweizer Mathematik 9

## Weiterführende Links

- [[06-Quadratwurzeln]]
