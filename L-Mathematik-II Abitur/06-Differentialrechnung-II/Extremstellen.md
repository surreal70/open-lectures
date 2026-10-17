---
author: Andreas Hümmer
title: Extremstellen
tags:
  - content
  - mathe
  - differentialrechnung
  - extremstellen
  - maximum
  - minimum
created: 2025-06-20
modified: 2025-06-20
---

# Extremstellen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Lokale und globale Extrema unterscheiden können
> - Notwendige und hinreichende Bedingungen für Extremstellen kennen
> - Verschiedene Kriterien zur Klassifikation von Extremstellen anwenden können
> - Extremwerte einer Funktion systematisch bestimmen können

---

## Überblick

**Extremstellen** sind Stellen, an denen eine Funktion lokale Maxima oder Minima annimmt – also Hoch- und Tiefpunkte des Graphen. Die Bestimmung von Extremstellen gehört zu den wichtigsten Anwendungen der Differentialrechnung und ist fundamentaler Bestandteil jeder Kurvendiskussion. Die erste und zweite Ableitung liefern effektive Werkzeuge zur systematischen Bestimmung und Klassifikation von Extrema.

## Definitionen

### Lokale Extrema

Eine Funktion $f$ hat an der Stelle $x_0$:
- ein **lokales Maximum**, wenn es eine Umgebung von $x_0$ gibt, sodass $f(x) \leq f(x_0)$ für alle $x$ in dieser Umgebung
- ein **lokales Minimum**, wenn es eine Umgebung von $x_0$ gibt, sodass $f(x) \geq f(x_0)$ für alle $x$ in dieser Umgebung

### Globale Extrema

Eine Funktion $f$ hat an der Stelle $x_0$:
- ein **globales Maximum**, wenn $f(x) \leq f(x_0)$ für alle $x \in D_f$
- ein **globales Minimum**, wenn $f(x) \geq f(x_0)$ für alle $x \in D_f$

### Extremwert vs. Extremstelle

- **Extremstelle**: Die $x$-Koordinate des Extremums ($x_0$)
- **Extremwert**: Der Funktionswert $f(x_0)$
- **Extrempunkt**: Der Punkt $(x_0, f(x_0))$

## Notwendige Bedingung

> [!note] **Satz: Notwendige Bedingung für Extrema**
> Hat die differenzierbare Funktion $f$ an der Stelle $x_0$ ein lokales Extremum, dann gilt:
> $$f'(x_0) = 0$$

**Achtung:** Die Umkehrung gilt nicht! Aus $f'(x_0) = 0$ folgt nicht zwingend ein Extremum. Beispiel: $f(x) = x^3$ hat bei $x_0 = 0$ eine waagerechte Tangente, aber kein Extremum.

Stellen mit $f'(x_0) = 0$ heißen **kritische Stellen** oder **stationäre Punkte**.

## Hinreichende Bedingungen

### Vorzeichenwechselkriterium (1. Ableitung)

Hat $f'$ an der Stelle $x_0$ einen Vorzeichenwechsel, so liegt dort ein Extremum vor:

- Wechsel von $+$ nach $-$ → **lokales Maximum**
- Wechsel von $-$ nach $+$ → **lokales Minimum**
- Kein Vorzeichenwechsel → **kein Extremum** (Sattelpunkt)

### Kriterium mit der 2. Ableitung

> [!note] **Satz: Hinreichende Bedingung mit f''**
> Sei $f$ zweimal differenzierbar mit $f'(x_0) = 0$. Dann gilt:
> - $f''(x_0) < 0$ $\Rightarrow$ lokales Maximum bei $x_0$
> - $f''(x_0) > 0$ $\Rightarrow$ lokales Minimum bei $x_0$
> - $f''(x_0) = 0$ $\Rightarrow$ keine Aussage möglich (Kriterium versagt)

**Merkhilfe:** 
- $f''(x_0) < 0$: Funktion ist rechtsgekrümmt (nach unten gebogen) → Berg → Maximum
- $f''(x_0) > 0$: Funktion ist linksgekrümmt (nach oben gebogen) → Tal → Minimum

## Vollständiges Beispiel

Gegeben: $f(x) = x^4 - 8x^2$

**Schritt 1:** Ableitungen berechnen
$$f'(x) = 4x^3 - 16x = 4x(x^2 - 4) = 4x(x-2)(x+2)$$
$$f''(x) = 12x^2 - 16$$

**Schritt 2:** Kritische Stellen ($f'(x) = 0$)
$$4x(x-2)(x+2) = 0 \implies x_1 = -2, \quad x_2 = 0, \quad x_3 = 2$$

**Schritt 3:** Klassifikation mit $f''$

| $x_0$ | $f''(x_0)$ | Vorzeichen | Art |
|-------|------------|------------|-----|
| $-2$ | $12 \cdot 4 - 16 = 32$ | $+$ | Minimum |
| $0$ | $-16$ | $-$ | Maximum |
| $2$ | $12 \cdot 4 - 16 = 32$ | $+$ | Minimum |

**Schritt 4:** Extremwerte berechnen
- Minimum bei $x = -2$: $f(-2) = 16 - 32 = -16$ → Tiefpunkt $(-2 \mid -16)$
- Maximum bei $x = 0$: $f(0) = 0$ → Hochpunkt $(0 \mid 0)$
- Minimum bei $x = 2$: $f(2) = 16 - 32 = -16$ → Tiefpunkt $(2 \mid -16)$

## Sonderfälle und Randextrema

### Fall $f''(x_0) = 0$

Wenn das Kriterium mit der 2. Ableitung versagt, nutze:

1. **Vorzeichenwechselkriterium** oder
2. **Höhere Ableitungen**: Ist $n$ die kleinste Zahl mit $f^{(n)}(x_0) \neq 0$:
   - $n$ gerade und $f^{(n)}(x_0) > 0$ → Minimum
   - $n$ gerade und $f^{(n)}(x_0) < 0$ → Maximum
   - $n$ ungerade → Sattelpunkt

### Randextrema

Bei Funktionen auf abgeschlossenen Intervallen $[a, b]$ können auch an den Randpunkten Extrema liegen. Diese müssen zusätzlich überprüft werden:

$$\text{Globales Maximum} = \max\{f(a), f(b), f(x_1), f(x_2), \ldots\}$$

wobei $x_1, x_2, \ldots$ die lokalen Extremstellen im Inneren sind.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Monotonieverhalten]] – Vorzeichenwechsel und Extrema
- → [[Hoehere-Ableitungen]] – Klassifikation bei versagendem Kriterium
- → [[Wendepunkte]] – Extrema der ersten Ableitung
- → [[Extremwertprobleme]] – Anwendung auf Optimierung
- → [[Vollstaendige-Kurvendiskussion]] – Einbettung in Funktionsanalyse

> [!warning] **Prüfungsrelevant**
> - Notwendige Bedingung: $f'(x_0) = 0$ (zwingend erforderlich)
> - Hinreichende Bedingung mit $f''$: Vorzeichen bestimmt Art
> - Bei $f''(x_0) = 0$ auf Vorzeichenwechsel von $f'$ zurückgreifen
> - Extremstelle vs. Extremwert unterscheiden!
> - Bei abgeschlossenen Intervallen Randpunkte prüfen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle lokalen Extremstellen und deren Art
> - Weisen Sie nach, dass an der Stelle $x_0$ ein lokales Maximum vorliegt
> - Ermitteln Sie das globale Maximum der Funktion auf dem Intervall $[a, b]$
> - An welcher Stelle hat $f$ den größten Funktionswert?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Extremwertprobleme]] – Anwendungen in der Praxis
> - [[Optimierungsaufgaben]] – Systematische Problemlösung
