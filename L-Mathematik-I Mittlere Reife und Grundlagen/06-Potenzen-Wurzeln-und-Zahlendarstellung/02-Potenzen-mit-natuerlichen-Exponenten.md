---
title: "Potenzen mit natürlichen Exponenten"
chapter: "06"
section: "02"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Potenzen mit natürlichen Exponenten berechnen"
  - "Vorzeichen bei Potenzen verstehen"
  - "Potenzen mit verschiedenen Basen vergleichen"
  - "Systematisch potenzieren"
tags:
  - mathematik
  - potenzen
  - natuerliche-zahlen
  - berechnung
created: 2026-10-13
modified: 2025-06-26
---

# Potenzen mit natürlichen Exponenten

> [!info] Lernziele
> - Potenzen mit natürlichen Exponenten berechnen
> - Vorzeichen bei Potenzen verstehen
> - Potenzen mit verschiedenen Basen vergleichen
> - Systematisch potenzieren

## Überblick

Bei natürlichen Exponenten (1, 2, 3, ...) wird die Basis entsprechend oft mit sich selbst multipliziert.

Das Konzept ist intuitiv: $3^4$ bedeutet „nimm die 3 viermal als Faktor". Diese wiederholte Multiplikation ist die ursprüngliche und anschaulichste Bedeutung von Potenzen. Erst später wurden Potenzen auf negative und gebrochene Exponenten erweitert – aber natürliche Exponenten bleiben das Fundament.

In der Praxis begegnen uns Potenzen mit natürlichen Exponenten bei **Flächenberechnungen** (Quadrat: $a^2$), **Volumenberechnungen** (Würfel: $a^3$) und bei **Wachstumsprozessen**. Wenn sich eine Bakterienkolonie alle 20 Minuten verdoppelt, ist die Anzahl nach $n$ Verdopplungen: $N = N_0 \cdot 2^n$.

## Berechnung

$$a^n = \underbrace{a \cdot a \cdot ... \cdot a}_{n \text{ Faktoren}}$$

### Beispiele

- $3^4 = 3 \cdot 3 \cdot 3 \cdot 3 = 81$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 64$
- $5^3 = 5 \cdot 5 \cdot 5 = 125$

## Vorzeichen bei Potenzen

### Positive Basis

Ergebnis ist immer **positiv**.

### Negative Basis

| Exponent | Ergebnis | Beispiel |
|----------|----------|----------|
| gerade | positiv | $(-2)^4 = 16$ |
| ungerade | negativ | $(-2)^3 = -8$ |

> [!tip] **Merkregel: Gerade macht's gerade**
> Bei einer **negativen Basis** entscheidet der Exponent über das Vorzeichen:
> - **Gerader Exponent** (2, 4, 6, ...): Das Ergebnis ist **positiv** – die negativen Vorzeichen „heben sich paarweise auf"
> - **Ungerader Exponent** (1, 3, 5, ...): Das Ergebnis ist **negativ** – ein Minuszeichen bleibt „übrig"
>
> Anschaulich: $(-2)^4 = (-2) \cdot (-2) \cdot (-2) \cdot (-2) = (+4) \cdot (+4) = 16$

> [!warning] **Häufiger Fehler: Klammern beachten!**
> $(-3)^2 = 9$ aber $-3^2 = -9$
> 
> Ohne Klammern bezieht sich das Minus nicht auf die Basis! Die Schreibweise $-3^2$ bedeutet $-(3^2) = -9$, nicht $(-3)^2 = 9$.
>
> **Eselsbrücke:** Steht das Minus „außerhalb" (ohne Klammer), wird es nicht potenziert.

## Wachstum von Potenzen

Potenzen wachsen sehr schnell (exponentielles Wachstum):

| n | 2ⁿ | 3ⁿ | 10ⁿ |
|---|----|----|-----|
| 1 | 2 | 3 | 10 |
| 2 | 4 | 9 | 100 |
| 3 | 8 | 27 | 1.000 |
| 4 | 16 | 81 | 10.000 |
| 5 | 32 | 243 | 100.000 |

> [!note] **Das explosive Wachstum verstehen**
> Exponentielles Wachstum ist für Menschen schwer intuitiv zu erfassen, weil es sich so schnell beschleunigt. Ein berühmtes Beispiel ist die **Legende vom Schachbrett**: Ein indischer König wollte den Erfinder des Schachspiels belohnen. Dieser bat bescheiden um Reiskörner: 1 Korn auf das erste Feld, 2 auf das zweite, 4 auf das dritte, und so weiter – immer verdoppeln.
>
> Das klingt harmlos, aber: Auf Feld 64 wären $2^{63} \approx 9,2 \cdot 10^{18}$ Körner nötig – mehr Reis, als jemals auf der Erde geerntet wurde! Die Gesamtsumme $2^{64} - 1$ entspräche etwa 460 Milliarden Tonnen Reis.

Diese explosive Eigenschaft macht Potenzen relevant für **Zinseszins** (Geldanlage), **Bevölkerungswachstum** und **Virusausbreitung** (Pandemien).

## Zusammenhänge

### Voraussetzungen

- [[01-Potenzschreibweise]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Besonders wichtig: Vorzeichen bei geraden/ungeraden Exponenten.

## Typische Prüfungsfragen

1. Berechne: $(-3)^3$, $(-2)^4$, $-2^4$
2. Welche Potenz ist größer: $3^4$ oder $4^3$?
3. Warum ist $(-5)^2$ positiv, aber $(-5)^3$ negativ?

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[03-Potenzgesetze]]
- [[04-Potenzen-mit-negativen-Exponenten]]
