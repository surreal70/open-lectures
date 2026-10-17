---
author: Andreas Hümmer
title: Definition der Ableitung
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - differenzierbarkeit
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Definition der Ableitung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die formale Definition der Ableitung kennen und verstehen
> - Den Begriff der Differenzierbarkeit erklären können
> - Die Ableitungsfunktion von der Ableitung an einer Stelle unterscheiden können
> - Verschiedene Notationen für die Ableitung sicher anwenden können

---

## Überblick

Die Ableitung ist einer der fundamentalsten Begriffe der Analysis. Sie verallgemeinert das Konzept der Steigung einer Geraden auf beliebige Funktionen und ermöglicht die präzise Beschreibung, wie sich eine Funktion an jeder Stelle ihres Definitionsbereichs verhält. Nach den Vorarbeiten über [[Differenzenquotient|Differenzen-]] und [[Differentialquotient|Differentialquotient]] können wir nun die Ableitung formal definieren.

## Formale Definition

> [!note] **Definition: Ableitung an einer Stelle**
> Sei $f: D \to \mathbb{R}$ eine Funktion und $x_0 \in D$ ein innerer Punkt des Definitionsbereichs. Die Funktion $f$ heißt **differenzierbar an der Stelle $x_0$**, wenn der Grenzwert
> $$f'(x_0) := \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
> existiert und endlich ist. Dieser Grenzwert heißt dann die **Ableitung von $f$ an der Stelle $x_0$**.

### Alternative Formulierung

Mit $x = x_0 + h$ und damit $h = x - x_0$ sowie $h \to 0 \Leftrightarrow x \to x_0$:

$$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

## Differenzierbarkeit

> [!note] **Definition: Differenzierbarkeit**
> - Eine Funktion $f$ heißt **differenzierbar an der Stelle $x_0$**, wenn $f'(x_0)$ existiert.
> - Eine Funktion $f$ heißt **differenzierbar auf einem Intervall $I$**, wenn sie an jeder Stelle von $I$ differenzierbar ist.
> - Eine Funktion $f$ heißt **differenzierbar**, wenn sie auf ihrem gesamten Definitionsbereich differenzierbar ist.

### Zusammenhang mit Stetigkeit

> [!warning] **Wichtiger Satz**
> Ist $f$ differenzierbar an der Stelle $x_0$, so ist $f$ auch stetig an der Stelle $x_0$.
> 
> **Achtung:** Die Umkehrung gilt **nicht**! Eine stetige Funktion muss nicht differenzierbar sein.

**Beispiel:** Die Betragsfunktion $f(x) = |x|$ ist an der Stelle $x_0 = 0$ stetig, aber nicht differenzierbar (siehe [[Differentialquotient|Differentialquotient]]).

## Die Ableitungsfunktion

Wenn $f$ auf einem Intervall $I$ differenzierbar ist, können wir jedem $x \in I$ die Ableitung $f'(x)$ zuordnen. Dies definiert eine neue Funktion:

> [!note] **Definition: Ableitungsfunktion**
> Ist $f$ auf $I$ differenzierbar, so heißt die Funktion
> $$f': I \to \mathbb{R}, \quad x \mapsto f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$
> die **Ableitungsfunktion** oder kurz **Ableitung** von $f$.

### Beispiel: Ableitungsfunktion von $f(x) = x^2$

Für beliebiges $x$:
$$f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x$$

Die Ableitungsfunktion ist $f'(x) = 2x$.

| $x$ | $f(x) = x^2$ | $f'(x) = 2x$ |
|-----|-------------|--------------|
| −2 | 4 | −4 |
| −1 | 1 | −2 |
| 0 | 0 | 0 |
| 1 | 1 | 2 |
| 2 | 4 | 4 |

## Notationen für die Ableitung

Die Ableitung kann auf verschiedene Weisen notiert werden:

### Lagrange-Notation (Strich-Notation)
$$f'(x), \quad f'(x_0), \quad y'$$

**Vorteile:** Kompakt, übersichtlich
**Verwendung:** Allgemein verbreitet, besonders bei Funktionsschreibweise

### Leibniz-Notation
$$\frac{df}{dx}, \quad \frac{dy}{dx}, \quad \frac{d}{dx}f(x)$$

**Vorteile:** Zeigt die Variablen explizit, suggestiv für Kettenregel
**Verwendung:** Bei Differentialgleichungen, implizitem Differenzieren

### Newton-Notation (Punkt-Notation)
$$\dot{x}, \quad \dot{y}$$

**Vorteile:** Sehr kompakt
**Verwendung:** Physik, bei Zeitabhängigkeit ($\dot{x} = \frac{dx}{dt}$)

### Operator-Notation
$$D_x f, \quad Df(x_0)$$

**Vorteile:** Betont die Ableitung als Operation
**Verwendung:** Höhere Mathematik, Funktionalanalysis

## Höhere Ableitungen

Wenn die Ableitungsfunktion $f'$ selbst wieder differenzierbar ist, können wir erneut ableiten:

> [!note] **Definition: Höhere Ableitungen**
> - Die **zweite Ableitung** ist die Ableitung der ersten Ableitung: $f'' = (f')'$
> - Die **dritte Ableitung**: $f''' = (f'')'$
> - Allgemein: Die **$n$-te Ableitung**: $f^{(n)} = (f^{(n-1)})'$

### Notationen für höhere Ableitungen

| Ordnung | Lagrange | Leibniz |
|---------|----------|---------|
| 1 | $f'(x)$ | $\frac{df}{dx}$ |
| 2 | $f''(x)$ | $\frac{d^2f}{dx^2}$ |
| 3 | $f'''(x)$ | $\frac{d^3f}{dx^3}$ |
| $n$ | $f^{(n)}(x)$ | $\frac{d^nf}{dx^n}$ |

### Beispiel: Höhere Ableitungen

Für $f(x) = x^4$:
- $f'(x) = 4x^3$
- $f''(x) = 12x^2$
- $f'''(x) = 24x$
- $f^{(4)}(x) = 24$
- $f^{(5)}(x) = 0$

## Bedeutung der Ableitung

Die Ableitung hat verschiedene Interpretationen:

### Geometrisch
$f'(x_0)$ ist die **Steigung der Tangente** an den Graphen von $f$ im Punkt $(x_0 | f(x_0))$.

### Physikalisch
$f'(t)$ ist die **momentane Änderungsrate** von $f$ zum Zeitpunkt $t$.

**Beispiele:**
- Ort $s(t)$ → Geschwindigkeit $v(t) = s'(t)$
- Geschwindigkeit $v(t)$ → Beschleunigung $a(t) = v'(t) = s''(t)$

### Analytisch
$f'(x_0)$ beschreibt das **lokale lineare Verhalten** von $f$ bei $x_0$:
$$f(x) \approx f(x_0) + f'(x_0) \cdot (x - x_0) \quad \text{für } x \text{ nahe } x_0$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Differenzenquotient|Differenzenquotient]] – Der Ausgangspunkt
- → [[Differentialquotient|Differentialquotient]] – Der Grenzwert
- → [[Geometrische-Bedeutung-der-Ableitung|Geometrische Bedeutung]] – Visualisierung
- → [[Ableitungsregeln|Ableitungsregeln]] – Effizientes Berechnen
- → [[Stetigkeit|Stetigkeit]] – Zusammenhang mit Differenzierbarkeit

> [!warning] **Prüfungsrelevant**
> - Die formale Definition der Ableitung muss bekannt sein
> - Differenzierbarkeit impliziert Stetigkeit, aber nicht umgekehrt!
> - Verschiedene Notationen müssen erkannt und verwendet werden können
> - Höhere Ableitungen und ihre physikalische Bedeutung (Ort → Geschwindigkeit → Beschleunigung)

> [!question] **Typische Prüfungsfragen**
> - "Geben Sie die Definition der Ableitung an."
> - "An welchen Stellen ist die Funktion $f$ differenzierbar?"
> - "Berechnen Sie $f'$, $f''$ und $f'''$ für die gegebene Funktion."
> - "Was bedeutet die zweite Ableitung physikalisch?"

## Quellen

- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.
- Forster, O. (2016): *Analysis 1*. Springer Spektrum.

> [!tip] **Weiterführende Links**
> - [[Ableitungsregeln|Ableitungsregeln]] – Praktische Berechnung von Ableitungen
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Ableitung
