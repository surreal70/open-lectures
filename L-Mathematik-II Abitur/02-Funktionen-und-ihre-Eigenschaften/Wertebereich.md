---
author: Andreas Hümmer
title: Wertebereich
tags:
  - content
  - mathe
  - funktionen
  - wertebereich
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Wertebereich

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Wertebereich einer Funktion bestimmen können
> - Verschiedene Methoden zur Wertebereichsbestimmung anwenden können
> - Den Unterschied zwischen Wertemenge und Bildmenge verstehen
> - Extremwerte zur Eingrenzung des Wertebereichs nutzen können

---

## Überblick

Der **Wertebereich** einer Funktion beschreibt die Menge aller Werte, die die Funktion tatsächlich annimmt. Seine Bestimmung ist oft anspruchsvoller als die des Definitionsbereichs und erfordert ein tieferes Verständnis des Funktionsverhaltens.

## Definition und Notation

### Formale Definition

Der **Wertebereich** (auch: Bildmenge) $W_f$ einer Funktion $f: D_f \to \mathbb{R}$ ist die Menge aller Funktionswerte:

$$W_f = \{y \in \mathbb{R} \mid \exists x \in D_f: f(x) = y\} = f(D_f)$$

**Notation:**
- $W_f$, $W(f)$ oder $\text{Bild}(f)$
- Im Englischen: range oder image, geschrieben als $\text{ran}(f)$ oder $\text{im}(f)$

### Unterschied: Zielmenge vs. Bildmenge

- **Zielmenge (Wertemenge):** Die Menge, in die $f$ abbildet (bei $f: D \to W$ ist $W$ die Zielmenge)
- **Bildmenge (Wertebereich):** Die Menge der tatsächlich angenommenen Werte

Die Bildmenge ist immer eine Teilmenge der Zielmenge: $W_f \subseteq W$

## Methoden zur Bestimmung des Wertebereichs

### Methode 1: Graphische Analyse

Aus dem Graphen einer Funktion lässt sich der Wertebereich als Projektion auf die $y$-Achse ablesen.

**Beispiel:** Für $f(x) = x^2$ mit $D_f = \mathbb{R}$:
- Minimum bei $x = 0$ mit $f(0) = 0$
- Kein Maximum (Graph steigt unbeschränkt)
- $W_f = [0, \infty)$

### Methode 2: Algebraische Umkehrung

Löse die Gleichung $y = f(x)$ nach $x$ auf und bestimme, für welche $y$-Werte eine Lösung existiert.

**Beispiel:** $f(x) = 2x + 3$

Auflösen nach $x$:
$$y = 2x + 3 \quad \Leftrightarrow \quad x = \frac{y-3}{2}$$

Da diese Gleichung für alle $y \in \mathbb{R}$ lösbar ist:
$$W_f = \mathbb{R}$$

**Beispiel:** $f(x) = x^2 - 4x + 5$

Auflösen nach $x$ mittels quadratischer Gleichung:
$$y = x^2 - 4x + 5$$
$$x^2 - 4x + (5-y) = 0$$
$$x = \frac{4 \pm \sqrt{16 - 4(5-y)}}{2} = 2 \pm \sqrt{y-1}$$

Eine reelle Lösung existiert genau dann, wenn:
$$y - 1 \geq 0 \quad \Leftrightarrow \quad y \geq 1$$

Also: $W_f = [1, \infty)$

### Methode 3: Extremwertanalyse

Bestimme Minimum und Maximum der Funktion (falls vorhanden).

**Für stetige Funktionen auf kompakten Intervallen** garantiert der Satz von Weierstraß die Existenz von Minimum und Maximum.

**Beispiel:** $f(x) = \sin(x)$ mit $D_f = \mathbb{R}$

- Globales Maximum: $\max f(x) = 1$
- Globales Minimum: $\min f(x) = -1$
- $W_f = [-1, 1]$

### Methode 4: Grenzwertbetrachtung

Untersuche das Verhalten der Funktion an den Rändern des Definitionsbereichs.

**Beispiel:** $f(x) = e^x$ mit $D_f = \mathbb{R}$

- $\lim_{x \to -\infty} e^x = 0$ (Wert wird nicht angenommen)
- $\lim_{x \to \infty} e^x = \infty$
- $W_f = (0, \infty)$

## Ausführliche Beispiele

### Beispiel 1: Rationale Funktion

$$f(x) = \frac{2x+1}{x-1}, \quad D_f = \mathbb{R} \setminus \{1\}$$

**Lösung durch Umkehrung:**
$$y = \frac{2x+1}{x-1}$$
$$y(x-1) = 2x+1$$
$$xy - y = 2x + 1$$
$$xy - 2x = y + 1$$
$$x(y-2) = y + 1$$
$$x = \frac{y+1}{y-2}$$

Diese Gleichung ist für alle $y \neq 2$ lösbar.

**Überprüfung:** Kann $y = 2$ angenommen werden?
$$2 = \frac{2x+1}{x-1} \Leftrightarrow 2(x-1) = 2x+1 \Leftrightarrow -2 = 1$$

Widerspruch! Also: $W_f = \mathbb{R} \setminus \{2\}$

### Beispiel 2: Wurzelfunktion mit Bruch

$$f(x) = \frac{1}{\sqrt{x}+1}, \quad D_f = [0, \infty)$$

Für $x \geq 0$ gilt:
- $\sqrt{x} \geq 0$, also $\sqrt{x} + 1 \geq 1$
- Daher $\frac{1}{\sqrt{x}+1} \leq 1$

Grenzwerte:
- $f(0) = \frac{1}{0+1} = 1$ (Maximum)
- $\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{1}{\sqrt{x}+1} = 0$ (wird nicht angenommen)

Also: $W_f = (0, 1]$

### Beispiel 3: Quadratische Funktion mit beschränktem Definitionsbereich

$$f(x) = x^2 - 2x, \quad D_f = [0, 3]$$

Scheitelpunktform: $f(x) = (x-1)^2 - 1$

Der Scheitelpunkt liegt bei $(1, -1)$ im Definitionsbereich.

Randwerte:
- $f(0) = 0$
- $f(3) = 9 - 6 = 3$

Minimum: $f(1) = -1$
Maximum: $f(3) = 3$

Also: $W_f = [-1, 3]$

## Wertebereich wichtiger Grundfunktionen

| Funktion | Definitionsbereich | Wertebereich |
|----------|-------------------|--------------|
| $f(x) = x^n$ ($n$ gerade) | $\mathbb{R}$ | $[0, \infty)$ |
| $f(x) = x^n$ ($n$ ungerade) | $\mathbb{R}$ | $\mathbb{R}$ |
| $f(x) = \sqrt{x}$ | $[0, \infty)$ | $[0, \infty)$ |
| $f(x) = e^x$ | $\mathbb{R}$ | $(0, \infty)$ |
| $f(x) = \ln(x)$ | $(0, \infty)$ | $\mathbb{R}$ |
| $f(x) = \sin(x)$ | $\mathbb{R}$ | $[-1, 1]$ |
| $f(x) = \cos(x)$ | $\mathbb{R}$ | $[-1, 1]$ |
| $f(x) = \tan(x)$ | $\mathbb{R} \setminus \{\frac{\pi}{2}+k\pi\}$ | $\mathbb{R}$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Definitionsbereich]] – Bestimmung der zulässigen Eingabewerte
- → [[Umkehrfunktionen]] – Der Wertebereich von $f$ wird zum Definitionsbereich von $f^{-1}$
- → [[Monotonie]] – Streng monotone Funktionen sind bijektiv auf ihren Wertebereich
- → [[Transformationen]] – Wie verschieben und strecken den Wertebereich beeinflusst

> [!warning] **Prüfungsrelevant**
> - Bestimmung des Wertebereichs durch algebraische Umkehrung
> - Nutzung von Extremwerten und Grenzwerten
> - Wertebereich bei beschränktem Definitionsbereich
> - Wertebereich rationaler Funktionen (welche $y$-Werte werden nicht angenommen?)

> [!question] **Typische Prüfungsfragen**
> - Bestimme den Wertebereich von $f(x) = \frac{x}{x^2+1}$.
> - Zeige, dass die Funktion $f(x) = e^x + e^{-x}$ den Wertebereich $[2, \infty)$ hat.
> - Für welche $y$-Werte ist die Gleichung $y = \frac{3x-1}{x+2}$ nach $x$ auflösbar?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Quadratische-Funktionen]] – Scheitelpunktform und Extremwerte
> - [[Exponentialfunktionen]] – Eigenschaften der Exponentialfunktion
> - [[Trigonometrische-Funktionen]] – Wertebereich trigonometrischer Funktionen
