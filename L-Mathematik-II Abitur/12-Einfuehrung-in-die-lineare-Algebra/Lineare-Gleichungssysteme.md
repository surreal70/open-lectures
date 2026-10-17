---
author: Andreas Hümmer
title: Lineare Gleichungssysteme
tags:
  - content
  - mathe
  - lineare-algebra
  - gleichungssysteme
  - lgs
created: 2025-07-01
modified: 2025-07-01
---

# Lineare Gleichungssysteme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition eines linearen Gleichungssystems kennen und anwenden können
> - Verschiedene Darstellungsformen (ausgeschrieben, Matrix, erweiterte Koeffizientenmatrix) beherrschen
> - Die drei Lösungstypen (eindeutig, unendlich viele, keine Lösung) unterscheiden können
> - Den geometrischen Zusammenhang zwischen LGS und Geraden/Ebenen verstehen

---

## Überblick

Ein **lineares Gleichungssystem (LGS)** besteht aus mehreren linearen Gleichungen mit gemeinsamen Unbekannten. Die Lösung eines LGS ist die Menge aller Werte für die Unbekannten, die alle Gleichungen gleichzeitig erfüllen. Lineare Gleichungssysteme sind fundamentale mathematische Werkzeuge mit zahlreichen Anwendungen in Naturwissenschaften, Technik und Wirtschaft.

## Definition und Notation

### Allgemeine Form

Ein lineares Gleichungssystem mit $m$ Gleichungen und $n$ Unbekannten $x_1, x_2, \ldots, x_n$ hat die Form:

$$
\begin{align}
a_{11} x_1 + a_{12} x_2 + \ldots + a_{1n} x_n &= b_1 \\
a_{21} x_1 + a_{22} x_2 + \ldots + a_{2n} x_n &= b_2 \\
\vdots \\
a_{m1} x_1 + a_{m2} x_2 + \ldots + a_{mn} x_n &= b_m
\end{align}
$$

wobei $a_{ij}$ die **Koeffizienten** und $b_i$ die **Absolutglieder** (rechte Seite) sind.

### Beispiel: LGS mit zwei Gleichungen

$$
\begin{align}
2x + 3y &= 8 \\
x - y &= 1
\end{align}
$$

Die Lösung ist $x = \frac{11}{5}$ und $y = \frac{6}{5}$.

## Matrixschreibweise

### Koeffizientenmatrix und Vektorform

Das obige System lässt sich kompakt als Matrixgleichung schreiben:

$$
\underbrace{\begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}}_{A} \cdot \underbrace{\begin{pmatrix} x \\ y \end{pmatrix}}_{\vec{x}} = \underbrace{\begin{pmatrix} 8 \\ 1 \end{pmatrix}}_{\vec{b}}
$$

oder kurz: $A \cdot \vec{x} = \vec{b}$

### Erweiterte Koeffizientenmatrix

Für das Gauß-Verfahren verwendet man die **erweiterte Koeffizientenmatrix** $(A|\vec{b})$:

$$
(A|\vec{b}) = \left(\begin{array}{cc|c} 2 & 3 & 8 \\ 1 & -1 & 1 \end{array}\right)
$$

## Lösungstypen

Ein lineares Gleichungssystem kann drei verschiedene Lösungsmengen haben:

### 1. Eindeutige Lösung

Das System hat genau einen Lösungspunkt.

**Geometrisch (2D):** Zwei Geraden schneiden sich in genau einem Punkt.

**Beispiel:**
$$
\begin{align}
x + y &= 5 \\
x - y &= 1
\end{align}
$$
Lösung: $(3, 2)$

### 2. Unendlich viele Lösungen

Das System hat eine Lösungsmenge mit einem oder mehreren freien Parametern.

**Geometrisch (2D):** Zwei Geraden sind identisch (liegen aufeinander).

**Beispiel:**
$$
\begin{align}
2x + 4y &= 6 \\
x + 2y &= 3
\end{align}
$$
Lösung: $\{(x, y) \mid x + 2y = 3\} = \{(3 - 2t, t) \mid t \in \mathbb{R}\}$

### 3. Keine Lösung

Das System ist widersprüchlich und hat keine Lösung.

**Geometrisch (2D):** Zwei Geraden sind parallel, aber nicht identisch.

**Beispiel:**
$$
\begin{align}
x + y &= 5 \\
x + y &= 7
\end{align}
$$
Keine Lösung, da $5 \neq 7$.

## Homogene und inhomogene Systeme

### Homogenes LGS

Ein LGS heißt **homogen**, wenn alle Absolutglieder null sind: $A \cdot \vec{x} = \vec{0}$

Homogene Systeme haben immer mindestens die **triviale Lösung** $\vec{x} = \vec{0}$.

### Inhomogenes LGS

Ein LGS heißt **inhomogen**, wenn mindestens ein Absolutglied ungleich null ist.

## Lösungsverfahren im Überblick

| Verfahren | Anwendung | Vorteile |
|-----------|-----------|----------|
| Einsetzungsverfahren | Kleine Systeme (2×2) | Intuitiv |
| Gleichsetzungsverfahren | Kleine Systeme (2×2) | Schnell bei einfachen Koeffizienten |
| Additionsverfahren | Kleine bis mittlere Systeme | Eliminiert gezielt Variablen |
| Gauß-Algorithmus | Beliebig große Systeme | Systematisch, programmierbar |
| Cramersche Regel | Theoretisch wichtig | Direktformel bei eindeutiger Lösung |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Gausssches-Eliminationsverfahren]] — Systematisches Lösungsverfahren für LGS
- → [[Matrizen]] — Matrixnotation für LGS
- → [[Determinanten]] — Lösbarkeit über die Determinante
- → [[Gleichungssysteme]] — Grundlagen aus der Algebra

> [!warning] **Prüfungsrelevant**
> - Definition und Notation eines LGS in ausgeschriebener und Matrixform
> - Aufstellen der erweiterten Koeffizientenmatrix
> - Unterscheidung der drei Lösungstypen
> - Geometrische Interpretation (Schnitt von Geraden/Ebenen)
> - Unterscheidung homogen/inhomogen

> [!question] **Typische Prüfungsfragen**
> - Schreiben Sie das LGS in Matrixform und als erweiterte Koeffizientenmatrix.
> - Welche Lösungsmenge hat das gegebene LGS (eindeutig, unendlich viele, keine)?
> - Interpretieren Sie das LGS geometrisch im $\mathbb{R}^2$ oder $\mathbb{R}^3$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Gausssches-Eliminationsverfahren]] — Fortsetzung mit dem Gauß-Algorithmus
> - [[Inverse-Matrizen]] — Alternative Lösungsmethode über $A^{-1}$
