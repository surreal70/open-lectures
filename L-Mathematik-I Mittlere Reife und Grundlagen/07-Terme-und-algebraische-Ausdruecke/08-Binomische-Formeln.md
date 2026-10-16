---
title: "Binomische Formeln"
chapter: "07"
section: "08"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Die drei binomischen Formeln kennen"
  - "Binomische Formeln vorwärts anwenden"
  - "Binomische Formeln rückwärts anwenden"
  - "Binomische Formeln erkennen"
tags:
  - mathematik
  - binomisch
  - formeln
  - quadrat
created: 2026-10-13
modified: 2025-07-23
---

# Binomische Formeln

> [!info] Lernziele
> - Die drei binomischen Formeln kennen
> - Binomische Formeln vorwärts anwenden
> - Binomische Formeln rückwärts anwenden
> - Binomische Formeln erkennen

## Überblick

Die **binomischen Formeln** sind wichtige Regeln zum schnellen Quadrieren von Summen und Differenzen.

Das Wort „binomisch" kommt von „Binom" (griechisch: „aus zwei Teilen bestehend"). Die drei binomischen Formeln gehören zu den wichtigsten Werkzeugen der Algebra. Sie ermöglichen es, bestimmte Berechnungen blitzschnell durchzuführen, die sonst mühsames Ausmultiplizieren erfordern würden.

> [!info] **Historischer Hintergrund**
> Die binomischen Formeln waren schon den Babyloniern vor über 3000 Jahren bekannt – allerdings nur als geometrische Zusammenhänge für Flächen. Die algebraische Formulierung, wie wir sie heute verwenden, entwickelte sich erst mit der Einführung der Symbolschreibweise im 16. und 17. Jahrhundert.

---

## Die drei Formeln

### 1. Binomische Formel

$$(a + b)^2 = a^2 + 2ab + b^2$$

**Merkspruch:** "Erstes Quadrat, plus 2 mal Produkt, plus zweites Quadrat"

### 2. Binomische Formel

$$(a - b)^2 = a^2 - 2ab + b^2$$

**Merkspruch:** "Erstes Quadrat, minus 2 mal Produkt, plus zweites Quadrat"

> [!tip] **Unterschied zwischen 1. und 2. Formel**
> Bei der 2. Formel ist nur das **mittlere** Vorzeichen negativ! Das letzte Glied $b^2$ ist immer positiv, denn ein Quadrat ist nie negativ (minus mal minus = plus).

### 3. Binomische Formel

$$(a + b)(a - b) = a^2 - b^2$$

**Merkspruch:** "Plus mal Minus ergibt Minus" (Differenz der Quadrate)

Diese Formel ist besonders nützlich, weil das mittlere Glied komplett wegfällt!

## Beispiele vorwärts

| Aufgabe | Lösung |
|---------|--------|
| $(x + 3)^2$ | $x^2 + 6x + 9$ |
| $(x - 5)^2$ | $x^2 - 10x + 25$ |
| $(x + 4)(x - 4)$ | $x^2 - 16$ |
| $(2x + 1)^2$ | $4x^2 + 4x + 1$ |

## Beispiele rückwärts (Faktorisieren)

| Ausdruck | Faktorisiert |
|----------|--------------|
| $x^2 + 8x + 16$ | $(x + 4)^2$ |
| $x^2 - 6x + 9$ | $(x - 3)^2$ |
| $x^2 - 25$ | $(x + 5)(x - 5)$ |

## Häufiger Fehler

> [!warning] **Häufiger Fehler: Das mittlere Glied vergessen**
> $(a + b)^2 \neq a^2 + b^2$
> 
> Das mittlere Glied $2ab$ fehlt! Dies ist einer der häufigsten Fehler in der Algebra.
> 
> **Beispiel:**
> - **Falsch:** $(x + 3)^2 = x^2 + 9$
> - **Richtig:** $(x + 3)^2 = x^2 + 6x + 9$
>
> **Gegenprobe mit Zahlen:** Setze $x = 2$:
> - Falsche Rechnung: $5^2 = 4 + 9 = 13$ ✗ (aber $5^2 = 25$)
> - Richtige Rechnung: $5^2 = 4 + 12 + 9 = 25$ ✓

> [!tip] **Merkregel: Der „Elternabend"**
> Die binomische Formel ist wie ein Elternabend: Die beiden Terme treffen sich ($2ab$) – man darf sie nicht einfach ignorieren!

## Visualisierung (1. Formel)

Die binomischen Formeln lassen sich geometrisch verstehen. Wenn wir ein Quadrat mit der Seitenlänge $(a+b)$ betrachten, hat es die Fläche $(a+b)^2$. Dieses Quadrat lässt sich in vier Teile zerlegen:

```
       a           b
   ┌─────────┬─────────┐
   │         │         │
 a │   a²    │   ab    │
   │         │         │
   ├─────────┼─────────┤
   │         │         │
 b │   ab    │   b²    │
   │         │         │
   └─────────┴─────────┘
   
   Gesamtfläche = a² + ab + ab + b² = a² + 2ab + b²
```

> [!info] **Geometrische Deutung**
> Das große Quadrat mit Seitenlänge $(a+b)$ besteht aus:
> - 1 Quadrat der Fläche $a^2$ (oben links)
> - 2 Rechtecke der Fläche $ab$ (oben rechts und unten links)
> - 1 Quadrat der Fläche $b^2$ (unten rechts)
>
> Diese anschauliche Vorstellung hilft, die Formel wirklich zu **verstehen** statt sie nur auswendig zu lernen.

## Zusammenhänge

### Voraussetzungen

- [[05-Ausmultiplizieren]]
- [[06-Ausklammern]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Die binomischen Formeln müssen sicher beherrscht werden!

## Typische Prüfungsfragen

1. Berechne mit binomischer Formel: $(x + 7)^2$
2. Faktorisiere: $x^2 - 12x + 36$
3. Berechne: $49 - x^2$ (faktorisiert)
4. Welche binomische Formel liegt vor bei $x^2 + 10x + 25$?

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[09-Faktorisierung]]
- [[05-Ausmultiplizieren]]
