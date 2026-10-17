---
author: Andreas Hümmer
title: Divergenz
tags:
  - content
  - mathe
  - folgen
  - divergenz
  - grenzwert
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Divergenz

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Divergenz verstehen und von Konvergenz abgrenzen können
> - Verschiedene Arten der Divergenz unterscheiden können
> - Divergente Folgen erkennen und klassifizieren können
> - Bestimmte und unbestimmte Divergenz unterscheiden können

---

## Überblick

Eine Folge heißt **divergent**, wenn sie nicht konvergiert – das heißt, wenn sie keinen endlichen Grenzwert besitzt. Divergenz ist das Gegenteil von Konvergenz. Während konvergente Folgen sich einem festen Wert annähern, "verhalten sich divergente Folgen anders": Sie können unbeschränkt wachsen, unbeschränkt fallen oder unregelmäßig schwanken.

Das Verständnis divergenter Folgen ist wichtig, um die Grenzen der Grenzwertrechnung zu kennen und um bei Anwendungen einschätzen zu können, wann ein Prozess stabil ist und wann nicht.

## Definition

### Formale Definition

Eine Folge $(a_n)$ heißt **divergent**, wenn sie **nicht konvergiert**, d.h. wenn kein $L \in \mathbb{R}$ existiert mit $\lim_{n \to \infty} a_n = L$.

**Äquivalent:** Die Negation der Konvergenzdefinition:

$$\forall L \in \mathbb{R} \; \exists \varepsilon > 0 \; \forall N \in \mathbb{N} \; \exists n \geq N : |a_n - L| \geq \varepsilon$$

## Arten der Divergenz

### 1. Bestimmte Divergenz gegen $+\infty$

Eine Folge $(a_n)$ **divergiert bestimmt gegen $+\infty$**, wenn gilt:

$$\forall K > 0 \; \exists N \in \mathbb{N} : \forall n \geq N : a_n > K$$

**Schreibweise:** $\lim_{n \to \infty} a_n = +\infty$ oder $a_n \to +\infty$

**Bedeutung:** Die Folge wächst über jede noch so große Schranke hinaus.

**Beispiele:**
- $a_n = n$ → $\lim_{n \to \infty} n = +\infty$
- $a_n = n^2$ → $\lim_{n \to \infty} n^2 = +\infty$
- $a_n = 2^n$ → $\lim_{n \to \infty} 2^n = +\infty$

### 2. Bestimmte Divergenz gegen $-\infty$

Eine Folge $(a_n)$ **divergiert bestimmt gegen $-\infty$**, wenn gilt:

$$\forall K < 0 \; \exists N \in \mathbb{N} : \forall n \geq N : a_n < K$$

**Schreibweise:** $\lim_{n \to \infty} a_n = -\infty$ oder $a_n \to -\infty$

**Beispiele:**
- $a_n = -n$ → $\lim_{n \to \infty} (-n) = -\infty$
- $a_n = -n^2$ → $\lim_{n \to \infty} (-n^2) = -\infty$

### 3. Unbestimmte Divergenz

Eine Folge heißt **unbestimmt divergent**, wenn sie weder konvergiert noch bestimmt gegen $\pm\infty$ divergiert.

**Typisch:** Die Folge schwankt oder oszilliert ohne sich einem Wert anzunähern.

**Beispiele:**
- $a_n = (-1)^n$ ergibt $(−1, 1, −1, 1, \ldots)$ – schwankt zwischen $-1$ und $1$
- $a_n = (-1)^n \cdot n$ ergibt $(−1, 2, −3, 4, \ldots)$ – schwankt mit wachsender Amplitude
- $a_n = \sin(n)$ – schwankt unregelmäßig zwischen $-1$ und $1$

## Übersicht: Folgenverhalten

```
                    Folge (a_n)
                         │
            ┌────────────┴────────────┐
            │                         │
        konvergent                divergent
     (endlicher Grenzwert L)          │
                          ┌───────────┴───────────┐
                          │                       │
                   bestimmt                  unbestimmt
                   divergent                 divergent
                       │                    (oszilliert)
              ┌────────┴────────┐
              │                 │
         gegen +∞          gegen -∞
```

## Nachweis von Divergenz

### Methode 1: Zwei Teilfolgen mit verschiedenen Grenzwerten

Wenn eine Folge zwei Teilfolgen besitzt, die gegen verschiedene Werte konvergieren, ist die Folge divergent.

**Beispiel:** $a_n = (-1)^n$
- Teilfolge der geraden Indizes: $a_{2k} = 1 \to 1$
- Teilfolge der ungeraden Indizes: $a_{2k+1} = -1 \to -1$

Da $1 \neq -1$, ist $(a_n)$ divergent.

### Methode 2: Unbeschränktheit

Eine konvergente Folge ist stets beschränkt. Ist eine Folge unbeschränkt, muss sie divergent sein.

**Beispiel:** $a_n = n$ ist unbeschränkt, also divergent.

**Achtung:** Die Umkehrung gilt nicht! Eine beschränkte Folge kann trotzdem divergent sein (z.B. $a_n = (-1)^n$).

### Methode 3: Direkter Nachweis

Zeige, dass für keinen Kandidaten $L$ die Konvergenzdefinition erfüllt ist.

## Rechenregeln bei bestimmter Divergenz

Für $\lim a_n = +\infty$ und $\lim b_n = L$ (endlich, $L > 0$):

| Operation | Ergebnis |
|-----------|----------|
| $a_n + b_n$ | $+\infty$ |
| $a_n \cdot b_n$ | $+\infty$ (für $L > 0$) |
| $\frac{1}{a_n}$ | $0$ |
| $a_n - b_n$ | $+\infty$ |

**Unbestimmte Ausdrücke** (erfordern genauere Analyse):
- $\infty - \infty$
- $0 \cdot \infty$
- $\frac{\infty}{\infty}$
- $\frac{0}{0}$

## Beispiele und Gegenbeispiele

### Beispiel 1: $a_n = \frac{n^2}{n+1}$

$$\frac{n^2}{n+1} = \frac{n^2}{n+1} \cdot \frac{1/n}{1/n} = \frac{n}{1 + 1/n} \to +\infty$$

Die Folge divergiert bestimmt gegen $+\infty$.

### Beispiel 2: $a_n = \frac{(-1)^n \cdot n}{n+1}$

- Für gerade $n$: $a_{2k} = \frac{2k}{2k+1} \to 1$
- Für ungerade $n$: $a_{2k+1} = \frac{-(2k+1)}{2k+2} \to -1$

Die Folge ist unbestimmt divergent.

### Beispiel 3: $a_n = n \cdot (-1)^n$

Die Folge lautet: $(-1, 2, -3, 4, -5, \ldots)$

- Unbeschränkt nach oben und unten
- Divergiert weder gegen $+\infty$ noch gegen $-\infty$
- Unbestimmt divergent

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Konvergenz]] – Das Gegenteil: Folgen mit endlichem Grenzwert
- → [[Zahlenfolgen]] – Grundlagen des Folgenbegriffs
- → [[Grenzwerte-von-Folgen]] – Wann existiert ein Grenzwert?
- → [[Geometrische-Folgen]] – Divergent für $|q| \geq 1$
- → [[Grenzwerte-von-Funktionen]] – Übertragung auf Funktionen

> [!warning] **Prüfungsrelevant**
> - Unterscheidung konvergent/divergent ist Grundwissen
> - Bestimmte vs. unbestimmte Divergenz muss erkannt werden
> - Nachweis über Teilfolgen mit verschiedenen Grenzwerten ist wichtig
> - Beschränktheit als notwendige (nicht hinreichende) Bedingung für Konvergenz
> - Typische divergente Folgen erkennen: $n$, $n^2$, $(-1)^n$, $q^n$ für $|q| \geq 1$

> [!question] **Typische Prüfungsfragen**
> - Untersuche die Folge $a_n = \frac{(-1)^n \cdot n^2}{n^2 + 1}$ auf Konvergenz.
> - Zeige, dass die Folge $a_n = (-1)^n + \frac{1}{n}$ divergiert.
> - Klassifiziere die Divergenz der Folge $a_n = (-2)^n$.

## Quellen

- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.

> [!tip] **Weiterführende Links**
> - [[Unendliche-geometrische-Reihen]] – Wann divergiert eine geometrische Reihe?
> - [[Einfuehrung-in-die-mathematische-Grenzwertbildung]] – Formale Beweise für Divergenz
