---
title: "Ausmultiplizieren"
chapter: "07"
section: "05"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Das Distributivgesetz anwenden"
  - "Klammern mit einem Faktor ausmultiplizieren"
  - "Zwei Klammern ausmultiplizieren"
  - "Vorzeichen beim Ausmultiplizieren beachten"
tags:
  - mathematik
  - terme
  - ausmultiplizieren
  - distributiv
created: 2026-10-13
modified: 2025-07-23
---

# Ausmultiplizieren

> [!info] Lernziele
> - Das Distributivgesetz anwenden
> - Klammern mit einem Faktor ausmultiplizieren
> - Zwei Klammern ausmultiplizieren
> - Vorzeichen beim Ausmultiplizieren beachten

## Überblick

**Ausmultiplizieren** bedeutet, Klammern durch Anwendung des Distributivgesetzes aufzulösen.

Das Wort „Distributiv" kommt vom lateinischen *distribuere* (verteilen). Und genau das passiert: Der Faktor vor der Klammer wird auf jeden Summanden in der Klammer „verteilt". Diese Technik ist fundamental für die gesamte Algebra – ohne sie könnte man weder Gleichungen lösen noch mit komplexeren Formeln arbeiten.

> [!info] **Historischer Hintergrund**
> Das Distributivgesetz wurde bereits von den griechischen Mathematikern verwendet, allerdings geometrisch formuliert. Die algebraische Schreibweise, wie wir sie heute kennen, entwickelte sich erst im 16. und 17. Jahrhundert mit der Einführung der Symbolsprache.

## Distributivgesetz

$$a \cdot (b + c) = a \cdot b + a \cdot c$$
$$a \cdot (b - c) = a \cdot b - a \cdot c$$

## Einfache Klammer

### Beispiele

$$3(x + 2) = 3x + 6$$
$$-2(a - 5) = -2a + 10$$
$$5(2x + 3y) = 10x + 15y$$

### Mit Minus vor der Klammer

Ein Minuszeichen vor der Klammer ist gleichbedeutend mit dem Faktor $-1$:

$$-(x + 3) = -1 \cdot (x + 3) = -x - 3$$
$$-(2a - b) = -2a + b$$

> [!warning] **Häufiger Fehler: Vorzeichen vergessen**
> Das Minus vor der Klammer wirkt auf **alle** Terme in der Klammer!
> 
> **Falsch:** $-(3x - 2) = -3x - 2$
> **Richtig:** $-(3x - 2) = -3x + 2$
> 
> Tipp: Denke an das Minus als „$-1$, der verteilt wird". Dann wird aus $-2$ automatisch $-1 \cdot (-2) = +2$.

## Zwei Klammern (FOIL-Methode)

$$(a + b)(c + d) = ac + ad + bc + bd$$

**FOIL:** First, Outer, Inner, Last

Die FOIL-Methode ist eine Eselsbrücke aus dem englischsprachigen Raum, die hilft, beim Ausmultiplizieren zweier Klammern keinen Term zu vergessen:

- **F**irst: Erste Terme beider Klammern multiplizieren ($a \cdot c$)
- **O**uter: Äußere Terme multiplizieren ($a \cdot d$)
- **I**nner: Innere Terme multiplizieren ($b \cdot c$)
- **L**ast: Letzte Terme beider Klammern multiplizieren ($b \cdot d$)

> [!tip] **Alternative Merkregel: „Jeder mit jedem"**
> Jeder Term der ersten Klammer wird mit jedem Term der zweiten Klammer multipliziert. Bei zwei Binomen (je 2 Terme) erhält man also $2 \times 2 = 4$ Produkte.

### Beispiel

$$(x + 3)(x + 2)$$
$$= x \cdot x + x \cdot 2 + 3 \cdot x + 3 \cdot 2$$
$$= x^2 + 2x + 3x + 6$$
$$= x^2 + 5x + 6$$

## Übersicht

| Aufgabe | Lösung |
|---------|--------|
| $2(x + 4)$ | $2x + 8$ |
| $-3(a - 2)$ | $-3a + 6$ |
| $(x + 1)(x + 2)$ | $x^2 + 3x + 2$ |
| $(x - 3)(x + 3)$ | $x^2 - 9$ |

## Zusammenhänge

### Voraussetzungen

- [[04-Zusammenfassen-gleichartiger-Terme]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Grundtechnik für alle algebraischen Umformungen.

## Typische Prüfungsfragen

1. Multipliziere aus: 4(2x − 3)
2. Multipliziere aus: (x + 5)(x − 2)
3. Vereinfache: 3(x + 2) − 2(x − 1)

## Quellen

- Lambacher Schweizer Mathematik 7

## Weiterführende Links

- [[06-Ausklammern]]
- [[08-Binomische-Formeln]]
