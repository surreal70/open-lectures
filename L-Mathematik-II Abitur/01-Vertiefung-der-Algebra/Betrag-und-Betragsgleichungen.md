---
author: Andreas Hümmer
title: Betrag und Betragsgleichungen
tags:
  - content
  - mathe
  - algebra
  - betrag
  - betragsgleichungen
  - fallunterscheidung
created: 2025-01-13
modified: 2025-01-13
---

# Betrag und Betragsgleichungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Betrag einer Zahl geometrisch und algebraisch interpretieren können
> - Betragsgleichungen durch Fallunterscheidung lösen können
> - Betragsungleichungen lösen und die Lösungsmenge angeben können
> - Betragsausdrücke vereinfachen können

---

## Überblick

Der Betrag einer Zahl gibt deren Abstand vom Nullpunkt an und ist daher stets nicht-negativ. Dieses scheinbar einfache Konzept führt zu interessanten Gleichungen und Ungleichungen, deren Lösung systematische Fallunterscheidungen erfordert. Die Betragsfunktion spielt auch in der Analysis eine wichtige Rolle, etwa bei der Definition von Grenzwerten und Stetigkeit.

## Definition des Betrags

Der **Betrag** (oder Absolutbetrag) einer reellen Zahl $x$ ist definiert als:

$$|x| = \begin{cases} x & \text{falls } x \geq 0 \\ -x & \text{falls } x < 0 \end{cases}$$

**Geometrische Interpretation:** $|x|$ ist der Abstand von $x$ zum Nullpunkt auf dem Zahlenstrahl.

**Beispiele:**
- $|5| = 5$
- $|-3| = 3$
- $|0| = 0$
- $|-\sqrt{2}| = \sqrt{2}$

## Eigenschaften des Betrags

### Grundlegende Eigenschaften

Für alle $x, y \in \mathbb{R}$ gilt:

1. **Nicht-Negativität:** $|x| \geq 0$ und $|x| = 0 \Leftrightarrow x = 0$

2. **Symmetrie:** $|-x| = |x|$

3. **Multiplikativität:** $|x \cdot y| = |x| \cdot |y|$

4. **Quotientenregel:** $\left|\frac{x}{y}\right| = \frac{|x|}{|y|}$ für $y \neq 0$

5. **Dreiecksungleichung:** $|x + y| \leq |x| + |y|$

6. **Umgekehrte Dreiecksungleichung:** $||x| - |y|| \leq |x - y|$

### Quadrat und Betrag

$$|x|^2 = x^2 \qquad \text{und} \qquad |x| = \sqrt{x^2}$$

> [!tip] **Merksatz**
> Der Betrag „macht positive Zahlen": $|x| = \sqrt{x^2}$ liefert immer das nicht-negative Ergebnis.

## Betragsgleichungen

### Typ 1: $|f(x)| = c$ mit $c > 0$

Diese Gleichung hat **zwei Lösungsfälle**:

$$|f(x)| = c \quad \Leftrightarrow \quad f(x) = c \quad \text{oder} \quad f(x) = -c$$

**Beispiel:** $|2x - 3| = 5$

Fall 1: $2x - 3 = 5 \Rightarrow x = 4$

Fall 2: $2x - 3 = -5 \Rightarrow x = -1$

Lösungsmenge: $\mathbb{L} = \{-1, 4\}$

### Typ 2: $|f(x)| = |g(x)|$

$$|f(x)| = |g(x)| \quad \Leftrightarrow \quad f(x) = g(x) \quad \text{oder} \quad f(x) = -g(x)$$

**Beispiel:** $|x + 2| = |3x - 4|$

Fall 1: $x + 2 = 3x - 4 \Rightarrow 6 = 2x \Rightarrow x = 3$

Fall 2: $x + 2 = -(3x - 4) = -3x + 4 \Rightarrow 4x = 2 \Rightarrow x = \frac{1}{2}$

Lösungsmenge: $\mathbb{L} = \left\{\frac{1}{2}, 3\right\}$

### Typ 3: Mehrere Betragsausdrücke

Bei mehreren Betragsausdrücken muss eine **vollständige Fallunterscheidung** durchgeführt werden.

**Beispiel:** $|x - 1| + |x + 2| = 5$

**Nullstellen der Betragsausdrücke:** $x = 1$ und $x = -2$

**Fall 1:** $x < -2$ (beide Ausdrücke negativ)

$$-(x-1) + (-(x+2)) = 5 \Rightarrow -x + 1 - x - 2 = 5 \Rightarrow -2x = 6 \Rightarrow x = -3$$

Probe: $-3 < -2$ ✓ und $|-4| + |-1| = 4 + 1 = 5$ ✓

**Fall 2:** $-2 \leq x < 1$ (erster negativ, zweiter positiv)

$$-(x-1) + (x+2) = 5 \Rightarrow -x + 1 + x + 2 = 5 \Rightarrow 3 = 5$$

Keine Lösung in diesem Bereich.

**Fall 3:** $x \geq 1$ (beide positiv)

$$(x-1) + (x+2) = 5 \Rightarrow 2x + 1 = 5 \Rightarrow x = 2$$

Probe: $2 \geq 1$ ✓ und $|1| + |4| = 1 + 4 = 5$ ✓

Lösungsmenge: $\mathbb{L} = \{-3, 2\}$

## Betragsungleichungen

### Typ 1: $|f(x)| < c$ mit $c > 0$

$$|f(x)| < c \quad \Leftrightarrow \quad -c < f(x) < c$$

**Beispiel:** $|2x - 1| < 3$

$$-3 < 2x - 1 < 3$$
$$-2 < 2x < 4$$
$$-1 < x < 2$$

Lösungsmenge: $\mathbb{L} = (-1, 2)$

### Typ 2: $|f(x)| > c$ mit $c > 0$

$$|f(x)| > c \quad \Leftrightarrow \quad f(x) < -c \quad \text{oder} \quad f(x) > c$$

**Beispiel:** $|x + 3| \geq 2$

$$x + 3 \leq -2 \quad \text{oder} \quad x + 3 \geq 2$$
$$x \leq -5 \quad \text{oder} \quad x \geq -1$$

Lösungsmenge: $\mathbb{L} = (-\infty, -5] \cup [-1, \infty)$

> [!warning] **Merkhilfe**
> - „kleiner als" → **ein** Intervall (Zahlen nahe bei Null)
> - „größer als" → **zwei** Intervalle (Zahlen weit weg von Null)

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Reelle-Zahlen-und-Intervalle]] – Intervallschreibweise für Lösungsmengen
- → [[Ungleichungen]] – Allgemeine Ungleichungslösung
- → [[Betragsfunktionen]] – Die Betragsfunktion als Funktionstyp
- → [[Grenzwerte-von-Funktionen]] – Betrag in der $\varepsilon$-$\delta$-Definition

> [!warning] **Prüfungsrelevant**
> - Systematische Fallunterscheidung bei Betragsgleichungen
> - Lösungsmenge bei Betragsungleichungen in Intervallschreibweise
> - Probe durchführen – passt die Lösung zum jeweiligen Fall?
> - Geometrische Interpretation: $|x - a| < r$ bedeutet „Abstand von $a$ kleiner als $r$"

> [!question] **Typische Prüfungsfragen**
> - Löse die Gleichung $|3x + 2| = |x - 4|$.
> - Für welche $x$ gilt $|x - 2| + |x + 1| < 5$?
> - Beschreibe die Menge $\{x \in \mathbb{R} \mid |x - 3| \leq 2\}$ geometrisch und in Intervallschreibweise.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Betrag|Glossar: Betrag]]
> - [[Glossar#Fallunterscheidung|Glossar: Fallunterscheidung]]
