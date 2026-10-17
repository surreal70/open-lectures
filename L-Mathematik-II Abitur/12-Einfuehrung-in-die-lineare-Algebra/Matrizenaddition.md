---
author: Andreas Hümmer
title: Matrizenaddition
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - addition
  - skalarmultiplikation
created: 2025-07-01
modified: 2025-07-01
---

# Matrizenaddition

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Addition zweier Matrizen durchführen können
> - Die Subtraktion von Matrizen beherrschen
> - Die Skalarmultiplikation verstehen und anwenden können
> - Die Rechengesetze (Kommutativ-, Assoziativ-, Distributivgesetz) kennen
> - Wissen, wann Addition/Subtraktion möglich ist (gleiche Dimension)

---

## Überblick

Die **Addition** und **Subtraktion** von Matrizen sowie die **Skalarmultiplikation** (Multiplikation mit einer Zahl) sind grundlegende Operationen der Matrizenrechnung. Sie werden elementweise durchgeführt und erfordern, dass die beteiligten Matrizen die gleiche Dimension haben.

## Addition von Matrizen

### Definition

Zwei Matrizen $A$ und $B$ können nur addiert werden, wenn sie **dieselbe Dimension** haben. Die Summe $C = A + B$ entsteht durch elementweise Addition:

$$
c_{ij} = a_{ij} + b_{ij}
$$

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad
B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
$$

$$
A + B = \begin{pmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}
$$

### Nicht erlaubte Addition

Matrizen verschiedener Dimension können **nicht** addiert werden:

$$
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \quad \text{nicht definiert!}
$$

## Subtraktion von Matrizen

### Definition

Die Differenz $C = A - B$ wird ebenfalls elementweise berechnet:

$$
c_{ij} = a_{ij} - b_{ij}
$$

### Beispiel

$$
A - B = \begin{pmatrix} 1-5 & 2-6 \\ 3-7 & 4-8 \end{pmatrix} = \begin{pmatrix} -4 & -4 \\ -4 & -4 \end{pmatrix}
$$

## Skalarmultiplikation

### Definition

Bei der **Skalarmultiplikation** wird jedes Element einer Matrix mit einem Skalar (einer reellen Zahl) $\lambda$ multipliziert:

$$
\lambda \cdot A = \lambda \cdot \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} \lambda \cdot a_{11} & \lambda \cdot a_{12} \\ \lambda \cdot a_{21} & \lambda \cdot a_{22} \end{pmatrix}
$$

### Beispiel

$$
3 \cdot \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}
$$

### Negative einer Matrix

Die **negative Matrix** $-A$ erhält man durch Multiplikation mit $-1$:

$$
-A = (-1) \cdot A = \begin{pmatrix} -a_{11} & -a_{12} \\ -a_{21} & -a_{22} \end{pmatrix}
$$

Damit gilt: $A - B = A + (-B)$

## Rechengesetze

Für Matrizen gleicher Dimension $A, B, C$ und Skalare $\lambda, \mu \in \mathbb{R}$ gelten:

### Addition

| Gesetz | Formel |
|--------|--------|
| Kommutativgesetz | $A + B = B + A$ |
| Assoziativgesetz | $(A + B) + C = A + (B + C)$ |
| Neutrales Element | $A + O = A$ (Nullmatrix) |
| Inverses Element | $A + (-A) = O$ |

### Skalarmultiplikation

| Gesetz | Formel |
|--------|--------|
| Assoziativgesetz | $\lambda \cdot (\mu \cdot A) = (\lambda \cdot \mu) \cdot A$ |
| Distributivgesetz I | $\lambda \cdot (A + B) = \lambda \cdot A + \lambda \cdot B$ |
| Distributivgesetz II | $(\lambda + \mu) \cdot A = \lambda \cdot A + \mu \cdot A$ |
| Neutrales Element | $1 \cdot A = A$ |

## Linearkombination von Matrizen

Eine **Linearkombination** von Matrizen ist eine Summe von skalar-multiplizierten Matrizen:

$$
\lambda_1 \cdot A_1 + \lambda_2 \cdot A_2 + \ldots + \lambda_k \cdot A_k
$$

### Beispiel

$$
2 \cdot \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + 3 \cdot \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} + \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 3 & 2 \end{pmatrix}
$$

## Anwendungsbeispiel: Datenverarbeitung

Matrizen können Datentabellen darstellen. Die Addition ermöglicht das Zusammenführen von Daten.

**Verkaufszahlen Januar:**
$$
J = \begin{pmatrix} 100 & 50 \\ 80 & 120 \end{pmatrix}
$$

**Verkaufszahlen Februar:**
$$
F = \begin{pmatrix} 90 & 60 \\ 110 & 100 \end{pmatrix}
$$

**Gesamtverkauf:**
$$
J + F = \begin{pmatrix} 190 & 110 \\ 190 & 220 \end{pmatrix}
$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Definition und Grundlagen
- → [[Matrizenmultiplikation]] — Multiplikation von Matrizen
- → [[Transponierte-Matrizen]] — Transposition
- → [[Lineare-Abbildungen]] — Matrizen als Abbildungen

> [!warning] **Prüfungsrelevant**
> - Addition nur bei gleicher Dimension möglich
> - Elementweise Durchführung der Operationen
> - Skalarmultiplikation korrekt anwenden
> - Rechengesetze kennen (besonders Kommutativität der Addition)
> - Unterschied zur Matrizenmultiplikation beachten

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie $A + B$ und $3A - 2B$ für gegebene Matrizen.
> - Warum ist die Addition der gegebenen Matrizen nicht definiert?
> - Bestimmen Sie die Matrix $X$, sodass $A + X = B$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Matrizenmultiplikation]] — Die nächste wichtige Operation
> - [[Lineare-Abbildungen]] — Anwendung in der Geometrie
