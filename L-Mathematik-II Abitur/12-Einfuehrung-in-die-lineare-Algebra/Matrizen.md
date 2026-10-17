---
author: Andreas Hümmer
title: Matrizen
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - grundlagen
created: 2025-07-01
modified: 2025-07-01
---

# Matrizen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Matrix und ihre Notation verstehen
> - Verschiedene Matrixtypen (quadratisch, diagonal, Einheitsmatrix, Nullmatrix) kennen
> - Matrizen aus dem Kontext von Gleichungssystemen und Daten aufstellen können
> - Die Dimension einer Matrix angeben können
> - Besondere Elemente (Hauptdiagonale, Nebendiagonale) identifizieren können

---

## Überblick

Eine **Matrix** ist ein rechteckiges Schema von Zahlen, die in Zeilen und Spalten angeordnet sind. Matrizen sind fundamentale Objekte der linearen Algebra und dienen als kompakte Darstellung von linearen Gleichungssystemen, linearen Abbildungen, Daten und vielem mehr. Die Matrizenrechnung ermöglicht es, komplexe Berechnungen systematisch durchzuführen.

## Definition und Notation

### Allgemeine Definition

Eine **Matrix** $A$ mit $m$ Zeilen und $n$ Spalten (eine $(m \times n)$-Matrix) hat die Form:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$

Die Elemente $a_{ij}$ werden durch zwei Indizes beschrieben:
- **Erster Index $i$**: Zeilennummer
- **Zweiter Index $j$**: Spaltennummer

### Kurzschreibweise

$A = (a_{ij})_{m \times n}$ oder $A \in \mathbb{R}^{m \times n}$

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}
$$

ist eine $(2 \times 3)$-Matrix mit $a_{12} = 2$ und $a_{21} = 4$.

## Besondere Matrixtypen

### Quadratische Matrix

Eine Matrix heißt **quadratisch**, wenn die Anzahl der Zeilen gleich der Anzahl der Spalten ist ($m = n$).

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \quad (2 \times 2)
$$

### Hauptdiagonale und Nebendiagonale

Bei einer quadratischen Matrix:

- **Hauptdiagonale**: Elemente $a_{11}, a_{22}, \ldots, a_{nn}$ (von links oben nach rechts unten)
- **Nebendiagonale**: Elemente $a_{1n}, a_{2(n-1)}, \ldots, a_{n1}$ (von rechts oben nach links unten)

### Diagonalmatrix

Eine quadratische Matrix, bei der alle Elemente außerhalb der Hauptdiagonale null sind:

$$
D = \begin{pmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{pmatrix}
$$

### Einheitsmatrix (Identitätsmatrix)

Eine Diagonalmatrix mit Einsen auf der Hauptdiagonale:

$$
I_3 = E_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

Die Einheitsmatrix ist das **neutrale Element der Matrizenmultiplikation**: $A \cdot I = I \cdot A = A$

### Nullmatrix

Eine Matrix, bei der alle Elemente null sind:

$$
O = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

### Dreiecksmatrizen

**Obere Dreiecksmatrix** (alle Elemente unterhalb der Hauptdiagonale sind null):

$$
U = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}
$$

**Untere Dreiecksmatrix** (alle Elemente oberhalb der Hauptdiagonale sind null):

$$
L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix}
$$

### Symmetrische Matrix

Eine quadratische Matrix heißt **symmetrisch**, wenn $a_{ij} = a_{ji}$ für alle $i, j$ gilt:

$$
S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}
$$

Symmetrische Matrizen sind gleich ihrer Transponierten: $S = S^T$

## Vektoren als spezielle Matrizen

### Spaltenvektor

Eine $(n \times 1)$-Matrix:

$$
\vec{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}
$$

### Zeilenvektor

Eine $(1 \times n)$-Matrix:

$$
\vec{w}^T = \begin{pmatrix} w_1 & w_2 & w_3 \end{pmatrix}
$$

## Gleichheit von Matrizen

Zwei Matrizen $A$ und $B$ sind **gleich** ($A = B$), wenn:
1. Sie dieselbe Dimension haben
2. Alle entsprechenden Elemente gleich sind: $a_{ij} = b_{ij}$ für alle $i, j$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Lineare-Gleichungssysteme]] — Matrizen als Darstellung von LGS
- → [[Matrizenaddition]] — Addition von Matrizen
- → [[Matrizenmultiplikation]] — Produkt von Matrizen
- → [[Transponierte-Matrizen]] — Vertauschen von Zeilen und Spalten

> [!warning] **Prüfungsrelevant**
> - Definition und Notation von Matrizen
> - Bestimmung der Dimension einer Matrix
> - Kenntnis der besonderen Matrixtypen (Einheitsmatrix, Diagonalmatrix, Dreiecksmatrix)
> - Unterscheidung von Zeilen- und Spaltenvektoren
> - Identifikation von Haupt- und Nebendiagonale

> [!question] **Typische Prüfungsfragen**
> - Geben Sie die Dimension der Matrix an und nennen Sie das Element $a_{23}$.
> - Welche der gegebenen Matrizen sind symmetrisch/quadratisch/diagonal?
> - Schreiben Sie das LGS in Matrixform $A \cdot \vec{x} = \vec{b}$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Matrizenaddition]] — Rechenoperationen mit Matrizen
> - [[Determinanten]] — Kennzahl quadratischer Matrizen
