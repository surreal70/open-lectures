---
author: Andreas Hümmer
title: Determinanten
tags:
  - content
  - mathe
  - lineare-algebra
  - determinanten
  - matrizen
created: 2025-07-01
modified: 2025-07-01
---

# Determinanten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Determinante einer 2×2- und 3×3-Matrix berechnen können
> - Die geometrische Bedeutung der Determinante verstehen (Flächeninhalt, Volumen)
> - Den Zusammenhang zwischen Determinante und Invertierbarkeit kennen
> - Wichtige Eigenschaften der Determinante anwenden können
> - Die Regel von Sarrus für 3×3-Matrizen beherrschen

---

## Überblick

Die **Determinante** ist eine wichtige Kennzahl, die nur für quadratische Matrizen definiert ist. Sie gibt Auskunft über die Invertierbarkeit einer Matrix, die Lösbarkeit linearer Gleichungssysteme und hat eine anschauliche geometrische Bedeutung als Flächen- oder Volumenfaktor bei linearen Abbildungen.

## Determinante einer 2×2-Matrix

### Definition

Für eine $(2 \times 2)$-Matrix:

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

ist die Determinante:

$$
\det(A) = |A| = ad - bc
$$

(Produkt der Hauptdiagonale minus Produkt der Nebendiagonale)

### Beispiel

$$
A = \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}
$$

$$
\det(A) = 3 \cdot 4 - 2 \cdot 1 = 12 - 2 = 10
$$

### Geometrische Deutung

Die Determinante einer 2×2-Matrix entspricht dem **orientierten Flächeninhalt** des Parallelogramms, das von den Spaltenvektoren aufgespannt wird.

```
    │      ╱
    │    ╱  ╲
    │  ╱      ╲
    │╱    A    ╲
    ┼───────────→
   O│
```

- $|\det(A)| > 0$: Parallelogramm hat positive Fläche
- $\det(A) = 0$: Vektoren sind linear abhängig (Fläche = 0)
- $\det(A) < 0$: Orientierung ist umgekehrt (Spiegelung)

## Determinante einer 3×3-Matrix

### Die Regel von Sarrus

Für eine $(3 \times 3)$-Matrix:

$$
A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}
$$

erweitert man die Matrix um die ersten zwei Spalten rechts daneben und bildet Produkte entlang der Diagonalen:

$$
\det(A) = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}
$$
$$
- a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}
$$

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
$$

**Positive Diagonalen (↘):**
- $1 \cdot 5 \cdot 9 = 45$
- $2 \cdot 6 \cdot 7 = 84$
- $3 \cdot 4 \cdot 8 = 96$

**Negative Diagonalen (↗):**
- $3 \cdot 5 \cdot 7 = 105$
- $1 \cdot 6 \cdot 8 = 48$
- $2 \cdot 4 \cdot 9 = 72$

$$
\det(A) = (45 + 84 + 96) - (105 + 48 + 72) = 225 - 225 = 0
$$

Da $\det(A) = 0$, ist diese Matrix **nicht invertierbar**.

## Eigenschaften der Determinante

| Eigenschaft | Formel |
|-------------|--------|
| Transposition | $\det(A^T) = \det(A)$ |
| Produkt | $\det(A \cdot B) = \det(A) \cdot \det(B)$ |
| Inverse | $\det(A^{-1}) = \frac{1}{\det(A)}$ |
| Skalierung | $\det(\lambda A) = \lambda^n \cdot \det(A)$ (für $n \times n$-Matrix) |
| Einheitsmatrix | $\det(I) = 1$ |

### Auswirkung von Zeilenoperationen

| Operation | Auswirkung auf Determinante |
|-----------|----------------------------|
| Zeilen vertauschen | Vorzeichen wechselt |
| Zeile mit $\lambda$ multiplizieren | Determinante wird mit $\lambda$ multipliziert |
| Vielfaches einer Zeile zu anderer addieren | Determinante bleibt gleich |

## Invertierbarkeit und Determinante

**Fundamentaler Zusammenhang:**

$$
A \text{ ist invertierbar} \Leftrightarrow \det(A) \neq 0
$$

- $\det(A) \neq 0$: Matrix ist regulär (invertierbar)
- $\det(A) = 0$: Matrix ist singulär (nicht invertierbar)

### Für lineare Gleichungssysteme

Das System $A \cdot \vec{x} = \vec{b}$ hat:
- **Eindeutige Lösung**, wenn $\det(A) \neq 0$
- **Keine oder unendlich viele Lösungen**, wenn $\det(A) = 0$

## Berechnung durch Entwicklung

Für größere Matrizen (und auch für 3×3) kann die Determinante durch **Entwicklung nach einer Zeile oder Spalte** berechnet werden (Laplace-Entwicklung):

$$
\det(A) = \sum_{j=1}^{n} (-1)^{i+j} \cdot a_{ij} \cdot \det(A_{ij})
$$

wobei $A_{ij}$ die Untermatrix ist, die durch Streichen der $i$-ten Zeile und $j$-ten Spalte entsteht.

### Beispiel: Entwicklung nach der 1. Zeile

$$
A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 2 \end{pmatrix}
$$

$$
\det(A) = 2 \cdot \det\begin{pmatrix} 4 & 5 \\ 0 & 2 \end{pmatrix} - 1 \cdot \det\begin{pmatrix} 0 & 5 \\ 1 & 2 \end{pmatrix} + 3 \cdot \det\begin{pmatrix} 0 & 4 \\ 1 & 0 \end{pmatrix}
$$

$$
= 2 \cdot (8 - 0) - 1 \cdot (0 - 5) + 3 \cdot (0 - 4) = 16 + 5 - 12 = 9
$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Grundlagen quadratischer Matrizen
- → [[Inverse-Matrizen]] — Invertierbarkeit über Determinante prüfen
- → [[Lineare-Gleichungssysteme]] — Lösbarkeitsanalyse
- → [[Gausssches-Eliminationsverfahren]] — Alternative zur Determinantenberechnung

> [!warning] **Prüfungsrelevant**
> - Berechnung von 2×2- und 3×3-Determinanten
> - Regel von Sarrus korrekt anwenden
> - Zusammenhang Determinante ↔ Invertierbarkeit
> - Auswirkung von Zeilenoperationen auf die Determinante
> - Geometrische Interpretation (Fläche/Volumen)

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie die Determinante der gegebenen Matrix.
> - Für welchen Wert von $a$ ist die Matrix nicht invertierbar?
> - Welche geometrische Bedeutung hat $\det(A) = 0$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Inverse-Matrizen]] — Berechnung der Inversen
> - [[Einfuehrung-in-Eigenwerte-und-Eigenvektoren]] — Charakteristisches Polynom
