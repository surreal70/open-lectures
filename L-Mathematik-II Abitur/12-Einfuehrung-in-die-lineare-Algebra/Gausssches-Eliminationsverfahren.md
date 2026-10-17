---
author: Andreas Hümmer
title: Gaußsches Eliminationsverfahren
tags:
  - content
  - mathe
  - lineare-algebra
  - gauss
  - algorithmus
  - lgs
created: 2025-07-01
modified: 2025-07-01
---

# Gaußsches Eliminationsverfahren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Gauß-Verfahren als systematischen Algorithmus zur Lösung von LGS verstehen
> - Die erlaubten Zeilenumformungen kennen und korrekt anwenden können
> - Ein LGS auf Zeilenstufenform bringen können
> - Mittels Rückwärtseinsetzen die Lösung bestimmen können
> - Sonderfälle (keine Lösung, unendlich viele Lösungen) erkennen können

---

## Überblick

Das **Gaußsche Eliminationsverfahren** (auch **Gauß-Algorithmus**) ist ein systematisches Verfahren zur Lösung linearer Gleichungssysteme beliebiger Größe. Benannt nach Carl Friedrich Gauß (1777–1855), transformiert es das Gleichungssystem schrittweise in eine **Zeilenstufenform**, aus der die Lösung durch Rückwärtseinsetzen abgelesen werden kann.

## Erlaubte Zeilenumformungen

Die erweiterte Koeffizientenmatrix darf mit folgenden **elementaren Zeilenumformungen** verändert werden, ohne die Lösungsmenge zu ändern:

| Operation | Notation | Beispiel |
|-----------|----------|----------|
| Zeilen vertauschen | $Z_i \leftrightarrow Z_j$ | $Z_1 \leftrightarrow Z_2$ |
| Zeile mit Skalar multiplizieren ($\lambda \neq 0$) | $Z_i \leftarrow \lambda \cdot Z_i$ | $Z_2 \leftarrow 3 \cdot Z_2$ |
| Vielfaches einer Zeile zu anderer addieren | $Z_i \leftarrow Z_i + \lambda \cdot Z_j$ | $Z_2 \leftarrow Z_2 - 2 \cdot Z_1$ |

## Der Algorithmus

### Schritt 1: Vorwärtselimination

Bringe die Matrix auf **Zeilenstufenform** (obere Dreiecksform):

$$
\left(\begin{array}{ccc|c}
\boxed{a_{11}} & a_{12} & a_{13} & b_1 \\
0 & \boxed{a_{22}'} & a_{23}' & b_2' \\
0 & 0 & \boxed{a_{33}''} & b_3''
\end{array}\right)
$$

Die eingerahmten Elemente heißen **Pivotelemente**.

### Schritt 2: Rückwärtseinsetzen

Aus der letzten Zeile wird $x_3$ berechnet, dann $x_2$, dann $x_1$.

## Ausführliches Beispiel

Gegeben sei das LGS:
$$
\begin{align}
x + 2y + z &= 9 \\
2x + 4y - z &= 12 \\
3x - 2y + z &= 7
\end{align}
$$

### Aufstellen der erweiterten Matrix

$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
2 & 4 & -1 & 12 \\
3 & -2 & 1 & 7
\end{array}\right)
$$

### Vorwärtselimination

**Erste Spalte eliminieren:**

$Z_2 \leftarrow Z_2 - 2 \cdot Z_1$:
$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & 0 & -3 & -6 \\
3 & -2 & 1 & 7
\end{array}\right)
$$

$Z_3 \leftarrow Z_3 - 3 \cdot Z_1$:
$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & 0 & -3 & -6 \\
0 & -8 & -2 & -20
\end{array}\right)
$$

**Zeilen tauschen** ($Z_2 \leftrightarrow Z_3$, da $a_{22} = 0$):
$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 9 \\
0 & -8 & -2 & -20 \\
0 & 0 & -3 & -6
\end{array}\right)
$$

### Zeilenstufenform erreicht

Die Matrix ist nun in Zeilenstufenform.

### Rückwärtseinsetzen

Aus $Z_3$: $-3z = -6 \Rightarrow z = 2$

Aus $Z_2$: $-8y - 2z = -20 \Rightarrow -8y - 4 = -20 \Rightarrow y = 2$

Aus $Z_1$: $x + 2y + z = 9 \Rightarrow x + 4 + 2 = 9 \Rightarrow x = 3$

**Lösung:** $(x, y, z) = (3, 2, 2)$

## Sonderfälle erkennen

### Keine Lösung (widersprüchliches System)

Entsteht eine Zeile der Form $(0 \; 0 \; \ldots \; 0 \; | \; c)$ mit $c \neq 0$:

$$
\left(\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 0 & 3
\end{array}\right)
$$

Die zweite Zeile bedeutet $0 = 3$ — ein Widerspruch. Das System hat **keine Lösung**.

### Unendlich viele Lösungen

Entsteht eine Nullzeile $(0 \; 0 \; \ldots \; 0 \; | \; 0)$:

$$
\left(\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 0 & 0
\end{array}\right)
$$

Es gibt mehr Unbekannte als Gleichungen. Die Lösungsmenge enthält **freie Parameter**:

$x = 5 - 2t$, $y = t$ mit $t \in \mathbb{R}$

## Rang einer Matrix

Der **Rang** einer Matrix ist die Anzahl der Nicht-Nullzeilen in der Zeilenstufenform.

Für ein LGS $A \cdot \vec{x} = \vec{b}$ gilt:

| Rang(A) | Rang(A|b) | Lösung |
|---------|-----------|--------|
| $r = n$ | $r = n$ | Eindeutig |
| $r < n$ | $r < n$ | Unendlich viele ($n - r$ Parameter) |
| $r$ | $r + 1$ | Keine |

wobei $n$ die Anzahl der Unbekannten ist.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Lineare-Gleichungssysteme]] — Definition und Grundlagen
- → [[Matrizen]] — Matrixnotation
- → [[Determinanten]] — Alternative Lösbarkeitsanalyse
- → [[Inverse-Matrizen]] — Berechnung über Gauß-Jordan

> [!warning] **Prüfungsrelevant**
> - Korrekte Anwendung der Zeilenumformungen
> - Systematisches Erreichen der Zeilenstufenform
> - Rückwärtseinsetzen ohne Rechenfehler
> - Erkennen von Sonderfällen (Widerspruch, freie Parameter)
> - Bestimmung des Rangs

> [!question] **Typische Prüfungsfragen**
> - Lösen Sie das LGS mit dem Gauß-Verfahren.
> - Bestimmen Sie alle Lösungen des gegebenen Systems.
> - Für welchen Parameterwert $a$ hat das System keine/unendlich viele Lösungen?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Strang, G.: Lineare Algebra, Springer
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch

> [!tip] **Weiterführende Links**
> - [[Inverse-Matrizen]] — Gauß-Jordan zur Berechnung der Inversen
> - [[Determinanten]] — Lösbarkeit über Determinanten prüfen
