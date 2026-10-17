---
author: Andreas Hümmer
title: Betragsfunktionen
tags:
  - content
  - mathe
  - funktionen
  - betragsfunktion
  - abschnittsweise-definiert
created: 2025-06-19
modified: 2025-06-19
---

# Betragsfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Betragsfunktion als abschnittsweise definierte Funktion verstehen
> - Graphen von Funktionen mit Beträgen skizzieren können
> - Betragsgleichungen und Betragsungleichungen systematisch lösen können
> - Transformationen auf die Betragsfunktion anwenden können

---

## Überblick

Die Betragsfunktion ist ein fundamentaler Baustein für abschnittsweise definierte Funktionen. Sie ordnet jeder reellen Zahl ihren Abstand zum Ursprung zu und ist damit eng mit geometrischen Konzepten verbunden. Betragsfunktionen treten in vielen Anwendungen auf, etwa bei Fehlerbetrachtungen, Toleranzberechnungen und der Formulierung von Abstandsbedingungen.

## Definition des Betrags

### Algebraische Definition

Der **Betrag** einer reellen Zahl $x$ ist definiert als:

$$|x| = \begin{cases} x & \text{falls } x \geq 0 \\ -x & \text{falls } x < 0 \end{cases}$$

### Äquivalente Darstellungen

$$|x| = \sqrt{x^2}$$

$$|x| = \max\{x, -x\}$$

### Beispiele

- $|5| = 5$
- $|-3| = 3$
- $|0| = 0$
- $|-\pi| = \pi$

## Die Betragsfunktion

### Grundform $f(x) = |x|$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R}$ |
| Wertebereich | $W_f = [0, +\infty)$ |
| Nullstelle | $x = 0$ |
| Minimum | $(0|0)$ |
| Symmetrie | Achsensymmetrisch zur y-Achse |
| Stetigkeit | Stetig auf ganz $\mathbb{R}$ |
| Differenzierbarkeit | Nicht differenzierbar bei $x = 0$ |

### Graph

Der Graph von $f(x) = |x|$ besteht aus zwei Halbgeraden, die sich im Ursprung treffen:

```
     y
     │    ╲    ╱
     │     ╲  ╱
     │      ╲╱
     └───────┴──────── x
            0
```

### Abschnittsweise Darstellung

$$f(x) = |x| = \begin{cases} x & \text{für } x \geq 0 \\ -x & \text{für } x < 0 \end{cases}$$

## Eigenschaften des Betrags

### Rechenregeln

Für alle $x, y \in \mathbb{R}$:

| Regel | Formel |
|-------|--------|
| Nicht-Negativität | $|x| \geq 0$, mit $|x| = 0 \Leftrightarrow x = 0$ |
| Multiplikation | $|x \cdot y| = |x| \cdot |y|$ |
| Division | $\left|\frac{x}{y}\right| = \frac{|x|}{|y|}$ für $y \neq 0$ |
| Potenz | $|x^n| = |x|^n$ |
| Dreiecksungleichung | $|x + y| \leq |x| + |y|$ |
| Umgekehrte Dreiecksungleichung | $||x| - |y|| \leq |x - y|$ |

### Geometrische Interpretation

- $|x|$ ist der Abstand von $x$ zum Ursprung auf der Zahlengeraden
- $|x - a|$ ist der Abstand zwischen $x$ und $a$

## Funktionen mit Betragsstrichen

### Allgemeine Form $f(x) = |g(x)|$

Der Graph von $f(x) = |g(x)|$ entsteht aus dem Graphen von $g(x)$, indem alle Teile unterhalb der x-Achse an dieser gespiegelt werden.

**Beispiel:** $f(x) = |x^2 - 4|$

1. Graph von $g(x) = x^2 - 4$ zeichnen (Parabel mit Scheitel bei $(0|-4)$)
2. Nullstellen bestimmen: $x = \pm 2$
3. Bereich zwischen den Nullstellen ($-2 < x < 2$) nach oben spiegeln

### Transformierte Betragsfunktion

$$f(x) = a|x - b| + c$$

| Parameter | Wirkung |
|-----------|---------|
| $a > 0$ | Öffnung nach oben, Streckung bei $a > 1$ |
| $a < 0$ | Öffnung nach unten, Hochpunkt statt Tiefpunkt |
| $b$ | Verschiebung um $b$ nach rechts |
| $c$ | Verschiebung um $c$ nach oben |

**Beispiel:** $f(x) = 2|x - 3| - 1$
- Tiefpunkt bei $(3|-1)$
- Steigung der Äste: $\pm 2$

## Betragsgleichungen

### Typ $|f(x)| = c$

Für $c > 0$ gilt: $|f(x)| = c \Leftrightarrow f(x) = c$ oder $f(x) = -c$

**Beispiel:** $|2x - 5| = 3$

Fall 1: $2x - 5 = 3 \Rightarrow x = 4$
Fall 2: $2x - 5 = -3 \Rightarrow x = 1$

Lösungsmenge: $\mathbb{L} = \{1, 4\}$

### Typ $|f(x)| = |g(x)|$

$$|f(x)| = |g(x)| \Leftrightarrow f(x) = g(x) \text{ oder } f(x) = -g(x)$$

**Beispiel:** $|x + 2| = |3x - 4|$

Fall 1: $x + 2 = 3x - 4 \Rightarrow 6 = 2x \Rightarrow x = 3$
Fall 2: $x + 2 = -(3x - 4) \Rightarrow x + 2 = -3x + 4 \Rightarrow 4x = 2 \Rightarrow x = \frac{1}{2}$

Lösungsmenge: $\mathbb{L} = \left\{\frac{1}{2}, 3\right\}$

### Systematische Methode: Fallunterscheidung

1. Bestimme alle Stellen, an denen ein Betragsausdruck sein Vorzeichen wechselt (Nullstellen der Betragsargumente)
2. Teile die Zahlengerade in Intervalle
3. Entferne die Betragsstriche in jedem Intervall mit dem korrekten Vorzeichen
4. Löse die entstehende Gleichung in jedem Intervall
5. Prüfe, ob die Lösung im betrachteten Intervall liegt

## Betragsungleichungen

### Grundtypen

| Ungleichung | Lösung (für $c > 0$) |
|-------------|---------------------|
| $|x| < c$ | $-c < x < c$ |
| $|x| \leq c$ | $-c \leq x \leq c$ |
| $|x| > c$ | $x < -c$ oder $x > c$ |
| $|x| \geq c$ | $x \leq -c$ oder $x \geq c$ |

### Beispiel

$|2x - 1| < 5$

$$-5 < 2x - 1 < 5$$
$$-4 < 2x < 6$$
$$-2 < x < 3$$

Lösungsmenge: $\mathbb{L} = (-2, 3)$

### Geometrische Interpretation

$|x - a| < r$ beschreibt alle Punkte, deren Abstand zu $a$ kleiner als $r$ ist:
$$|x - a| < r \Leftrightarrow a - r < x < a + r$$

Dies ist ein offenes Intervall mit Mittelpunkt $a$ und Radius $r$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Betrag-und-Betragsgleichungen]] — Algebraische Behandlung
- → [[Ungleichungen]] — Allgemeine Ungleichungslehre
- → [[Symmetrie]] — Achsensymmetrie bei $f(x) = |g(x)|$
- → [[Wurzelfunktionen]] — Zusammenhang $\sqrt{x^2} = |x|$
- → [[Stetigkeit]] — Stetigkeit der Betragsfunktion
- → [[05-Differentialrechnung-I|Differentialrechnung]] — Knickstellen und Differenzierbarkeit

> [!warning] **Prüfungsrelevant**
> - Fallunterscheidung bei Betragsgleichungen und -ungleichungen
> - Graphen von $|f(x)|$ durch Spiegelung konstruieren
> - Dreiecksungleichung $|a + b| \leq |a| + |b|$
> - Geometrische Interpretation: $|x - a|$ als Abstand
> - Transformierte Betragsfunktionen $a|x - b| + c$ analysieren

> [!question] **Typische Prüfungsfragen**
> - Lösen Sie die Gleichung $|3x + 2| = |x - 4|$.
> - Für welche $x$ gilt $|x^2 - 4| < 3$?
> - Skizzieren Sie den Graphen von $f(x) = |x^2 - 2x - 3|$ und bestimmen Sie alle lokalen Extrema.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, 2023

> [!tip] **Weiterführende Links**
> - [[Reelle-Zahlen-und-Intervalle]] — Intervallschreibweise bei Ungleichungen
> - [[11-Analytische-Geometrie|Analytische Geometrie]] — Abstandsbegriff im Raum

