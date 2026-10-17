---
author: Andreas Hümmer
title: Transponierte Matrizen
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - transposition
created: 2025-07-01
modified: 2025-07-01
---

# Transponierte Matrizen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Transposition einer Matrix durchführen können (Vertauschen von Zeilen und Spalten)
> - Die Rechenregeln für transponierte Matrizen kennen
> - Symmetrische Matrizen als spezielle Klasse erkennen ($A = A^T$)
> - Den Zusammenhang zwischen Transposition und Skalarprodukt verstehen

---

## Überblick

Die **Transposition** ist eine Operation, bei der Zeilen und Spalten einer Matrix vertauscht werden. Die transponierte Matrix entsteht durch Spiegelung der Elemente an der Hauptdiagonale. Diese Operation spielt eine wichtige Rolle bei der Formulierung von Skalarprodukten, quadratischen Formen und in vielen Anwendungen.

## Definition

### Transponierte Matrix

Sei $A$ eine $(m \times n)$-Matrix. Die **transponierte Matrix** $A^T$ ist eine $(n \times m)$-Matrix mit:

$$
(A^T)_{ij} = A_{ji}
$$

Das Element in Zeile $i$ und Spalte $j$ von $A^T$ ist das Element in Zeile $j$ und Spalte $i$ von $A$.

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}_{2 \times 3}
$$

$$
A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}_{3 \times 2}
$$

Die erste Zeile $(1, 2, 3)$ wird zur ersten Spalte, die zweite Zeile $(4, 5, 6)$ zur zweiten Spalte.

### Quadratische Matrix

$$
B = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
\quad \Rightarrow \quad
B^T = \begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix}
$$

## Rechenregeln

Für Matrizen $A, B$ und Skalar $\lambda$ gelten:

| Regel | Formel |
|-------|--------|
| Doppelte Transposition | $(A^T)^T = A$ |
| Transposition der Summe | $(A + B)^T = A^T + B^T$ |
| Skalarmultiplikation | $(\lambda A)^T = \lambda A^T$ |
| Transposition des Produkts | $(A \cdot B)^T = B^T \cdot A^T$ |

### Wichtig: Reihenfolge beim Produkt

Bei der Transposition eines Produkts kehrt sich die Reihenfolge um:

$$
(A \cdot B)^T = B^T \cdot A^T
$$

Dies gilt analog für mehr Faktoren:

$$
(A \cdot B \cdot C)^T = C^T \cdot B^T \cdot A^T
$$

## Symmetrische Matrizen

### Definition

Eine quadratische Matrix $A$ heißt **symmetrisch**, wenn gilt:

$$
A = A^T
$$

Dies bedeutet: $a_{ij} = a_{ji}$ für alle $i, j$.

### Beispiel

$$
S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}
$$

ist symmetrisch, da sie gleich ihrer Transponierten ist.

### Eigenschaften symmetrischer Matrizen

- Die Diagonalelemente können beliebig sein
- Elemente oberhalb und unterhalb der Hauptdiagonale sind gespiegelt
- Symmetrische Matrizen haben nur reelle Eigenwerte
- Eigenvektoren zu verschiedenen Eigenwerten sind orthogonal

## Antisymmetrische (schiefsymmetrische) Matrizen

Eine Matrix heißt **antisymmetrisch**, wenn:

$$
A^T = -A
$$

Dies bedeutet: $a_{ij} = -a_{ji}$ und insbesondere $a_{ii} = 0$ (Diagonale ist null).

### Beispiel

$$
A = \begin{pmatrix} 0 & 2 & -1 \\ -2 & 0 & 3 \\ 1 & -3 & 0 \end{pmatrix}
$$

## Skalarprodukt und Transposition

Das **Skalarprodukt** zweier Vektoren lässt sich mit der Transposition schreiben:

$$
\vec{a} \cdot \vec{b} = \vec{a}^T \cdot \vec{b} = \begin{pmatrix} a_1 & a_2 & a_3 \end{pmatrix} \cdot \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = a_1 b_1 + a_2 b_2 + a_3 b_3
$$

## Zerlegung in symmetrischen und antisymmetrischen Teil

Jede quadratische Matrix $A$ lässt sich eindeutig zerlegen in:

$$
A = \underbrace{\frac{1}{2}(A + A^T)}_{\text{symmetrisch}} + \underbrace{\frac{1}{2}(A - A^T)}_{\text{antisymmetrisch}}
$$

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$

Symmetrischer Teil:
$$
\frac{1}{2}(A + A^T) = \frac{1}{2}\begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix} = \begin{pmatrix} 1 & 2{,}5 \\ 2{,}5 & 4 \end{pmatrix}
$$

Antisymmetrischer Teil:
$$
\frac{1}{2}(A - A^T) = \frac{1}{2}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -0{,}5 \\ 0{,}5 & 0 \end{pmatrix}
$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Grundlagen und Notation
- → [[Matrizenmultiplikation]] — Produktregel bei Transposition
- → [[Determinanten]] — $\det(A) = \det(A^T)$
- → [[Einfuehrung-in-Eigenwerte-und-Eigenvektoren]] — Symmetrische Matrizen und Eigenwerte

> [!warning] **Prüfungsrelevant**
> - Transponierte Matrix korrekt bilden
> - Rechenregeln anwenden, besonders $(AB)^T = B^T A^T$
> - Symmetrische Matrizen erkennen und ihre Eigenschaften kennen
> - Skalarprodukt als $\vec{a}^T \cdot \vec{b}$ schreiben können

> [!question] **Typische Prüfungsfragen**
> - Bilden Sie die Transponierte der gegebenen Matrix.
> - Ist die Matrix symmetrisch? Begründen Sie.
> - Berechnen Sie $(A \cdot B)^T$ mit Hilfe der Rechenregeln.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Determinanten]] — Determinante bleibt bei Transposition gleich
> - [[Einfuehrung-in-Eigenwerte-und-Eigenvektoren]] — Spezielle Eigenschaften symmetrischer Matrizen
