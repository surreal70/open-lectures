---
author: Andreas Hümmer
title: Gleichungssysteme
tags:
  - content
  - mathe
  - algebra
  - gleichungssysteme
  - lineare-algebra
  - gauss
created: 2025-01-13
modified: 2025-01-13
---

# Gleichungssysteme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Lineare Gleichungssysteme mit verschiedenen Methoden lösen können
> - Das Gauß-Verfahren systematisch anwenden können
> - Die Lösbarkeit von Gleichungssystemen beurteilen können
> - Nichtlineare Gleichungssysteme mit Substitution lösen können

---

## Überblick

Gleichungssysteme treten in vielen mathematischen und praktischen Anwendungen auf, etwa bei der Bestimmung von Schnittpunkten oder der Lösung von Optimierungsproblemen. Die systematischen Lösungsverfahren bilden die Grundlage für die lineare Algebra und sind auch in der analytischen Geometrie unverzichtbar.

## Lineare Gleichungssysteme (LGS)

### Allgemeine Form

Ein **lineares Gleichungssystem** mit $m$ Gleichungen und $n$ Unbekannten:

$$\begin{align}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n &= b_m
\end{align}$$

### Lösbarkeit

Ein LGS kann haben:
- **Genau eine Lösung** (eindeutig lösbar)
- **Unendlich viele Lösungen** (unterbestimmt)
- **Keine Lösung** (überbestimmt/widersprüchlich)

## Lösungsverfahren für 2×2-Systeme

### Einsetzungsverfahren (Substitution)

**Beispiel:**
$$\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}$$

**Schritt 1:** Eine Gleichung nach einer Variablen auflösen

Aus Gleichung 2: $x = y + 1$

**Schritt 2:** In die andere Gleichung einsetzen

$2(y + 1) + y = 5 \Rightarrow 3y + 2 = 5 \Rightarrow y = 1$

**Schritt 3:** Rückeinsetzen

$x = 1 + 1 = 2$

**Lösung:** $(x, y) = (2, 1)$

### Gleichsetzungsverfahren

Beide Gleichungen nach derselben Variablen auflösen und gleichsetzen.

### Additionsverfahren (Eliminationsverfahren)

**Beispiel:**
$$\begin{cases} 3x + 2y = 7 \\ x - 2y = 1 \end{cases}$$

Addition der Gleichungen eliminiert $y$:

$4x = 8 \Rightarrow x = 2$

Einsetzen: $2 - 2y = 1 \Rightarrow y = \frac{1}{2}$

## Das Gauß-Verfahren

Das **Gauß-Eliminationsverfahren** ist die systematische Methode für größere Systeme.

### Erlaubte Umformungen

1. Vertauschen zweier Zeilen
2. Multiplikation einer Zeile mit einer Zahl $\neq 0$
3. Addition eines Vielfachen einer Zeile zu einer anderen

### Beispiel: 3×3-System

$$\begin{cases}
x + 2y + z = 6 \\
2x + y - z = 1 \\
x - y + 2z = 1
\end{cases}$$

**Erweiterte Koeffizientenmatrix:**

$$\left(\begin{array}{ccc|c}
1 & 2 & 1 & 6 \\
2 & 1 & -1 & 1 \\
1 & -1 & 2 & 1
\end{array}\right)$$

**Schritt 1:** Eliminiere $x$ in Zeile 2 und 3

$Z_2 \leftarrow Z_2 - 2Z_1$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 1 & 6 \\
0 & -3 & -3 & -11 \\
1 & -1 & 2 & 1
\end{array}\right)$$

$Z_3 \leftarrow Z_3 - Z_1$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 1 & 6 \\
0 & -3 & -3 & -11 \\
0 & -3 & 1 & -5
\end{array}\right)$$

**Schritt 2:** Eliminiere $y$ in Zeile 3

$Z_3 \leftarrow Z_3 - Z_2$:
$$\left(\begin{array}{ccc|c}
1 & 2 & 1 & 6 \\
0 & -3 & -3 & -11 \\
0 & 0 & 4 & 6
\end{array}\right)$$

**Schritt 3:** Rückwärtseinsetzen

Aus Zeile 3: $4z = 6 \Rightarrow z = \frac{3}{2}$

Aus Zeile 2: $-3y - 3 \cdot \frac{3}{2} = -11 \Rightarrow y = \frac{13}{6}$

Aus Zeile 1: $x + 2 \cdot \frac{13}{6} + \frac{3}{2} = 6 \Rightarrow x = \frac{5}{6}$

### Sonderfälle

**Keine Lösung:** Eine Zeile der Form $(0 \; 0 \; \ldots \; 0 \mid c)$ mit $c \neq 0$ zeigt einen Widerspruch an.

**Unendlich viele Lösungen:** Eine Nullzeile $(0 \; 0 \; \ldots \; 0 \mid 0)$ zeigt unterbestimmtes System an. Eine Variable kann frei gewählt werden (Parameter).

## Nichtlineare Gleichungssysteme

### Substitutionsmethode

**Beispiel:** Schnittpunkte von Gerade und Parabel

$$\begin{cases} y = x^2 - 1 \\ y = 2x + 2 \end{cases}$$

Gleichsetzen: $x^2 - 1 = 2x + 2$

$x^2 - 2x - 3 = 0$

$(x-3)(x+1) = 0 \Rightarrow x_1 = 3, x_2 = -1$

$y_1 = 2 \cdot 3 + 2 = 8, \quad y_2 = 2 \cdot (-1) + 2 = 0$

**Schnittpunkte:** $(3, 8)$ und $(-1, 0)$

### Kreisgleichungen

**Beispiel:** Schnittpunkte zweier Kreise

$$\begin{cases} x^2 + y^2 = 25 \\ (x-3)^2 + y^2 = 16 \end{cases}$$

Subtrahiere Gleichung 2 von Gleichung 1:

$x^2 - (x-3)^2 = 25 - 16 = 9$

$x^2 - x^2 + 6x - 9 = 9$

$6x = 18 \Rightarrow x = 3$

Einsetzen: $9 + y^2 = 25 \Rightarrow y = \pm 4$

**Schnittpunkte:** $(3, 4)$ und $(3, -4)$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-algebraischer-Grundlagen]] – Termumformungen
- → [[Lineare-Funktionen]] – Geometrische Interpretation
- → [[Quadratische-Funktionen]] – Parabel-Gerade-Schnitt
- → [[12-Einfuehrung-in-die-lineare-Algebra-Index]] – Matrizendarstellung

> [!warning] **Prüfungsrelevant**
> - Alle drei Verfahren für 2×2-Systeme beherrschen
> - Gauß-Verfahren für 3×3-Systeme durchführen
> - Sonderfälle erkennen (keine/unendlich viele Lösungen)
> - Geometrische Interpretation der Lösungsfälle

> [!question] **Typische Prüfungsfragen**
> - Löse das System $\begin{cases} 2x - 3y = 7 \\ 4x + y = 5 \end{cases}$ mit dem Additionsverfahren.
> - Bestimme die Schnittpunkte von $y = x^2$ und $y = 4x - 3$.
> - Für welchen Wert von $a$ hat das System $\begin{cases} x + 2y = 3 \\ 2x + 4y = a \end{cases}$ unendlich viele Lösungen?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Lineares Gleichungssystem|Glossar: Lineares Gleichungssystem]]
> - [[Glossar#Gauß-Verfahren|Glossar: Gauß-Verfahren]]
