---
author: Andreas Hümmer
title: Inverse Matrizen
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - inverse
created: 2025-07-01
modified: 2025-07-01
---

# Inverse Matrizen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der inversen Matrix verstehen
> - Die Existenzbedingung (Determinante ≠ 0) kennen
> - Die Inverse einer 2×2-Matrix mit der Formel berechnen können
> - Das Gauß-Jordan-Verfahren zur Berechnung der Inversen anwenden können
> - Anwendungen der Inversen bei der Lösung von LGS kennen

---

## Überblick

Die **inverse Matrix** $A^{-1}$ einer quadratischen Matrix $A$ ist das multiplikative Gegenstück zur Einheitsmatrix: $A \cdot A^{-1} = A^{-1} \cdot A = I$. Die Inverse existiert genau dann, wenn die Determinante von $A$ ungleich null ist. Mit der Inversen lassen sich lineare Gleichungssysteme elegant lösen.

## Definition

### Inverse Matrix

Eine quadratische Matrix $A$ heißt **invertierbar** (oder **regulär**), wenn eine Matrix $A^{-1}$ existiert mit:

$$
A \cdot A^{-1} = A^{-1} \cdot A = I
$$

Die Matrix $A^{-1}$ heißt **inverse Matrix** zu $A$.

### Existenzbedingung

$$
A^{-1} \text{ existiert} \Leftrightarrow \det(A) \neq 0
$$

Matrizen mit $\det(A) = 0$ heißen **singulär** und besitzen keine Inverse.

## Inverse einer 2×2-Matrix

### Formel

Für eine $(2 \times 2)$-Matrix mit $\det(A) \neq 0$:

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

$$
A^{-1} = \frac{1}{\det(A)} \cdot \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{ad - bc} \cdot \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

**Merkregel:**
1. Hauptdiagonalelemente tauschen
2. Nebendiagonalelemente mit $-1$ multiplizieren
3. Durch Determinante dividieren

### Beispiel

$$
A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}
$$

$\det(A) = 3 \cdot 4 - 1 \cdot 2 = 12 - 2 = 10$

$$
A^{-1} = \frac{1}{10} \cdot \begin{pmatrix} 4 & -1 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 0{,}4 & -0{,}1 \\ -0{,}2 & 0{,}3 \end{pmatrix}
$$

**Probe:** $A \cdot A^{-1} = I$

$$
\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} \cdot \begin{pmatrix} 0{,}4 & -0{,}1 \\ -0{,}2 & 0{,}3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \checkmark
$$

## Gauß-Jordan-Verfahren

Für größere Matrizen verwendet man das **Gauß-Jordan-Verfahren**:

1. Schreibe $(A | I)$ als erweiterte Matrix
2. Bringe $A$ durch Zeilenumformungen auf die Einheitsmatrix
3. Die rechte Seite wird dabei zur Inversen

### Beispiel

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$

**Schritt 1:** Erweiterte Matrix aufstellen

$$
\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array}\right)
$$

**Schritt 2:** $Z_2 \leftarrow Z_2 - 3 \cdot Z_1$

$$
\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array}\right)
$$

**Schritt 3:** $Z_2 \leftarrow -\frac{1}{2} \cdot Z_2$

$$
\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & \frac{3}{2} & -\frac{1}{2} \end{array}\right)
$$

**Schritt 4:** $Z_1 \leftarrow Z_1 - 2 \cdot Z_2$

$$
\left(\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & \frac{3}{2} & -\frac{1}{2} \end{array}\right)
$$

**Ergebnis:**

$$
A^{-1} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}
$$

## Eigenschaften der Inversen

| Eigenschaft | Formel |
|-------------|--------|
| Doppelte Inversion | $(A^{-1})^{-1} = A$ |
| Inverse eines Produkts | $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ |
| Inverse der Transponierten | $(A^T)^{-1} = (A^{-1})^T$ |
| Determinante der Inversen | $\det(A^{-1}) = \frac{1}{\det(A)}$ |
| Inverse einer Diagonalmatrix | Kehrwerte auf der Diagonale |

### Beachte: Reihenfolge beim Produkt

$$
(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}
$$

Die Reihenfolge kehrt sich um!

## Lösung von Gleichungssystemen mit der Inversen

Das lineare Gleichungssystem $A \cdot \vec{x} = \vec{b}$ hat, falls $A$ invertierbar ist, die eindeutige Lösung:

$$
\vec{x} = A^{-1} \cdot \vec{b}
$$

### Beispiel

$$
\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} \cdot \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 10 \end{pmatrix}
$$

Mit $A^{-1}$ von oben:

$$
\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0{,}4 & -0{,}1 \\ -0{,}2 & 0{,}3 \end{pmatrix} \cdot \begin{pmatrix} 5 \\ 10 \end{pmatrix} = \begin{pmatrix} 2 - 1 \\ -1 + 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

## Wann existiert keine Inverse?

Die Inverse existiert **nicht**, wenn:

- $\det(A) = 0$
- Die Zeilen (oder Spalten) linear abhängig sind
- Die Matrix beim Gauß-Verfahren eine Nullzeile im linken Teil erzeugt

### Beispiel: Singuläre Matrix

$$
A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
$$

$\det(A) = 1 \cdot 4 - 2 \cdot 2 = 0$ → **nicht invertierbar**

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Grundlagen
- → [[Determinanten]] — Existenzbedingung
- → [[Lineare-Gleichungssysteme]] — Lösung über Inverse
- → [[Gausssches-Eliminationsverfahren]] — Gauß-Jordan-Verfahren

> [!warning] **Prüfungsrelevant**
> - Formel für die Inverse einer 2×2-Matrix
> - Prüfung der Existenz über die Determinante
> - Gauß-Jordan-Verfahren zur Berechnung
> - Lösung von LGS mittels $\vec{x} = A^{-1} \cdot \vec{b}$
> - Rechenregeln für Inverse (besonders $(AB)^{-1} = B^{-1}A^{-1}$)

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie die Inverse der gegebenen 2×2-Matrix.
> - Zeigen Sie, dass die Matrix nicht invertierbar ist.
> - Lösen Sie das LGS mithilfe der inversen Matrix.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Lineare-Abbildungen]] — Inverse Abbildungen
> - [[Anwendungen-von-Matrizen]] — Praktische Anwendungen
