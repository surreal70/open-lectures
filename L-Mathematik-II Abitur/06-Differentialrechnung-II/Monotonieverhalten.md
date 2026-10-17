---
author: Andreas Hümmer
title: Monotonieverhalten
tags:
  - content
  - mathe
  - differentialrechnung
  - monotonie
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Monotonieverhalten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Monotonieverhalten einer Funktion mithilfe der ersten Ableitung bestimmen können
> - Monotone Intervalle korrekt angeben können
> - Den Zusammenhang zwischen Nullstellen der Ableitung und Monotonieänderungen verstehen
> - Monotonieeigenschaften für Kurvendiskussionen nutzen können

---

## Überblick

Das **Monotonieverhalten** beschreibt, ob eine Funktion in einem Bereich steigt oder fällt. Diese Information ist fundamental für das Verständnis des Funktionsverlaufs und bildet die Grundlage für die Bestimmung von Extremstellen. Die erste Ableitung liefert ein mächtiges Werkzeug zur systematischen Analyse der Monotonie.

## Definition der Monotonie

Eine Funktion $f$ heißt auf einem Intervall $I$:

- **streng monoton steigend**, wenn für alle $x_1, x_2 \in I$ mit $x_1 < x_2$ gilt: $f(x_1) < f(x_2)$
- **streng monoton fallend**, wenn für alle $x_1, x_2 \in I$ mit $x_1 < x_2$ gilt: $f(x_1) > f(x_2)$
- **monoton steigend** (nicht streng), wenn $f(x_1) \leq f(x_2)$
- **monoton fallend** (nicht streng), wenn $f(x_1) \geq f(x_2)$

## Monotoniekriterium

> [!note] **Satz: Monotoniekriterium**
> Sei $f$ differenzierbar auf dem Intervall $I$. Dann gilt:
> - $f'(x) > 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist streng monoton steigend auf $I$
> - $f'(x) < 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist streng monoton fallend auf $I$
> - $f'(x) \geq 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist monoton steigend auf $I$
> - $f'(x) \leq 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist monoton fallend auf $I$

**Geometrische Interpretation:** Die Ableitung gibt die Steigung der Tangente an. Positive Tangentensteigung bedeutet steigende Funktion.

## Vorgehensweise zur Monotonleuntersuchung

**Schritt 1:** Erste Ableitung $f'(x)$ berechnen

**Schritt 2:** Nullstellen von $f'(x)$ bestimmen

**Schritt 3:** Definitionslücken berücksichtigen

**Schritt 4:** Vorzeichen von $f'(x)$ in den entstehenden Intervallen prüfen

**Schritt 5:** Monotonieverhalten angeben

### Beispiel 1: Ganzrationale Funktion

Gegeben: $f(x) = x^3 - 3x^2 - 9x + 5$

**Schritt 1:** $f'(x) = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)$

**Schritt 2:** Nullstellen: $x_1 = -1$, $x_2 = 3$

**Schritt 4:** Vorzeichentabelle:

| Intervall | $(-\infty, -1)$ | $(-1, 3)$ | $(3, \infty)$ |
|-----------|-----------------|-----------|----------------|
| $f'(x)$ | $+$ | $-$ | $+$ |
| Monotonie | steigend | fallend | steigend |

**Schritt 5:** Die Funktion ist streng monoton steigend auf $(-\infty, -1]$ und $[3, \infty)$, streng monoton fallend auf $[-1, 3]$.

### Beispiel 2: Gebrochenrationale Funktion

Gegeben: $f(x) = \frac{x^2}{x-1}$ mit $D_f = \mathbb{R} \setminus \{1\}$

**Schritt 1:** Mit Quotientenregel:
$$f'(x) = \frac{2x(x-1) - x^2 \cdot 1}{(x-1)^2} = \frac{x^2 - 2x}{(x-1)^2} = \frac{x(x-2)}{(x-1)^2}$$

**Schritt 2:** Nullstellen von $f'$: $x_1 = 0$, $x_2 = 2$

**Schritt 3:** Definitionslücke bei $x = 1$

**Schritt 4:** Vorzeichentabelle:

| Intervall | $(-\infty, 0)$ | $(0, 1)$ | $(1, 2)$ | $(2, \infty)$ |
|-----------|----------------|----------|----------|----------------|
| $x$ | $-$ | $+$ | $+$ | $+$ |
| $x-2$ | $-$ | $-$ | $-$ | $+$ |
| $(x-1)^2$ | $+$ | $+$ | $+$ | $+$ |
| $f'(x)$ | $+$ | $-$ | $-$ | $+$ |

**Schritt 5:** Streng monoton steigend auf $(-\infty, 0]$ und $[2, \infty)$, streng monoton fallend auf $[0, 1)$ und $(1, 2]$.

## Sonderfälle

### Konstante Funktion

Für $f(x) = c$ (konstant) ist $f'(x) = 0$ überall. Die Funktion ist (nicht streng) monoton steigend und fallend zugleich.

### Streng monotone Funktionen ohne positive/negative Ableitung überall

Die Funktion $f(x) = x^3$ ist streng monoton steigend auf ganz $\mathbb{R}$, obwohl $f'(0) = 0$. Es genügt, wenn $f'(x) \geq 0$ ist und $f'(x) = 0$ nur an isolierten Stellen gilt.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Extremstellen]] – Monotoniewechsel führen zu Extrema
- → [[Nullstellen]] – Nullstellen von $f'$ als kritische Stellen
- → [[Monotonie]] – Grundlegende Definition aus Modul 2
- → [[Vollstaendige-Kurvendiskussion]] – Monotonie als Bestandteil
- → [[Ableitungsregeln]] – Berechnung der Ableitung

> [!warning] **Prüfungsrelevant**
> - Die erste Ableitung bestimmt das Monotonieverhalten
> - Nullstellen von $f'$ sind potenzielle Stellen für Monotonieänderungen
> - Bei gebrochenrationalen Funktionen: Definitionslücken beachten!
> - Monotone Intervalle immer mit Randpunkten angeben (z.B. $[-1, 3]$)

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Intervalle, in denen $f$ streng monoton steigt bzw. fällt
> - Zeigen Sie, dass $f$ auf dem Intervall $I$ streng monoton steigend ist
> - Begründen Sie mithilfe des Monotoniekriteriums, warum die Gleichung genau eine Lösung hat

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Extremstellen]] – Zusammenhang mit Extremwertbestimmung
> - [[Wendepunkte]] – Monotonie von $f'$ und Wendepunkte
