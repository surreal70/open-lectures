---
author: Andreas Hümmer
title: Matrizenmultiplikation
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - multiplikation
created: 2025-07-01
modified: 2025-07-01
---

# Matrizenmultiplikation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Bedingung für die Multiplikation zweier Matrizen kennen (Spalten = Zeilen)
> - Das Produkt zweier Matrizen korrekt berechnen können
> - Die Dimension des Produkts bestimmen können
> - Verstehen, dass Matrizenmultiplikation **nicht kommutativ** ist
> - Die Bedeutung der Einheitsmatrix als neutrales Element kennen

---

## Überblick

Die **Matrizenmultiplikation** ist eine zentrale Operation der linearen Algebra. Anders als die Addition wird sie **nicht elementweise** durchgeführt, sondern nach der "Zeile-mal-Spalte"-Regel. Eine wichtige Besonderheit: Die Matrizenmultiplikation ist im Allgemeinen **nicht kommutativ**, d.h. $A \cdot B \neq B \cdot A$.

## Voraussetzung für die Multiplikation

Zwei Matrizen $A$ und $B$ können nur multipliziert werden, wenn die **Spaltenanzahl von $A$** gleich der **Zeilenanzahl von $B$** ist:

$$
A_{m \times \boxed{n}} \cdot B_{\boxed{n} \times p} = C_{m \times p}
$$

Die inneren Dimensionen müssen übereinstimmen, die äußeren bestimmen die Dimension des Produkts.

### Beispiel zur Dimensionsprüfung

| $A$ | $B$ | $A \cdot B$ möglich? | Ergebnis-Dimension |
|-----|-----|----------------------|-------------------|
| $2 \times 3$ | $3 \times 2$ | Ja | $2 \times 2$ |
| $3 \times 2$ | $2 \times 3$ | Ja | $3 \times 3$ |
| $2 \times 3$ | $2 \times 3$ | Nein | — |
| $2 \times 2$ | $2 \times 2$ | Ja | $2 \times 2$ |

## Die "Zeile-mal-Spalte"-Regel

Das Element $c_{ij}$ der Produktmatrix $C = A \cdot B$ berechnet sich als **Skalarprodukt** der $i$-ten Zeile von $A$ mit der $j$-ten Spalte von $B$:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj} = a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{2j} + \ldots + a_{in} \cdot b_{nj}
$$

### Visualisierung

```
        B
      ┌───┐
      │ * │ ← j-te Spalte
      │ * │
      └───┘
A     
┌─────┐
│*****│ ← i-te Zeile  ──→  c_ij
└─────┘
```

## Ausführliches Beispiel

Gegeben:
$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \quad
B = \begin{pmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{pmatrix}
$$

$A$ ist $(2 \times 3)$, $B$ ist $(3 \times 2)$ → Produkt ist $(2 \times 2)$

**Berechnung:**

$c_{11} = 1 \cdot 7 + 2 \cdot 9 + 3 \cdot 11 = 7 + 18 + 33 = 58$

$c_{12} = 1 \cdot 8 + 2 \cdot 10 + 3 \cdot 12 = 8 + 20 + 36 = 64$

$c_{21} = 4 \cdot 7 + 5 \cdot 9 + 6 \cdot 11 = 28 + 45 + 66 = 139$

$c_{22} = 4 \cdot 8 + 5 \cdot 10 + 6 \cdot 12 = 32 + 50 + 72 = 154$

**Ergebnis:**
$$
A \cdot B = \begin{pmatrix} 58 & 64 \\ 139 & 154 \end{pmatrix}
$$

## Nicht-Kommutativität

Im Allgemeinen gilt $A \cdot B \neq B \cdot A$:

$$
A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad
B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

$$
A \cdot B = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}, \quad
B \cdot A = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}
$$

Offensichtlich: $A \cdot B \neq B \cdot A$

## Rechengesetze

Für passende Matrizen $A, B, C$ und Skalar $\lambda$ gilt:

| Gesetz | Formel |
|--------|--------|
| Assoziativgesetz | $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ |
| Distributivgesetz (links) | $A \cdot (B + C) = A \cdot B + A \cdot C$ |
| Distributivgesetz (rechts) | $(A + B) \cdot C = A \cdot C + B \cdot C$ |
| Skalare Verträglichkeit | $\lambda \cdot (A \cdot B) = (\lambda \cdot A) \cdot B = A \cdot (\lambda \cdot B)$ |
| Einheitsmatrix | $A \cdot I = I \cdot A = A$ |

**Achtung:** Das Kommutativgesetz gilt **nicht**!

## Einheitsmatrix als neutrales Element

Die Einheitsmatrix $I$ (oder $E$) ist das neutrale Element:

$$
I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

$$
A \cdot I = I \cdot A = A
$$

## Matrix-Vektor-Produkt

Ein wichtiger Spezialfall ist die Multiplikation einer Matrix mit einem Spaltenvektor:

$$
A \cdot \vec{x} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \cdot \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} a_{11} x_1 + a_{12} x_2 \\ a_{21} x_1 + a_{22} x_2 \end{pmatrix}
$$

Dies entspricht der Darstellung eines linearen Gleichungssystems.

## Potenzen von Matrizen

Für quadratische Matrizen sind Potenzen definiert:

$$
A^0 = I, \quad A^1 = A, \quad A^2 = A \cdot A, \quad A^n = \underbrace{A \cdot A \cdot \ldots \cdot A}_{n \text{ Faktoren}}
$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Grundlagen und Notation
- → [[Matrizenaddition]] — Weitere Matrizenoperation
- → [[Lineare-Gleichungssysteme]] — LGS als Matrixgleichung
- → [[Lineare-Abbildungen]] — Verkettung von Abbildungen

> [!warning] **Prüfungsrelevant**
> - Dimensionsbedingung für Multiplikation prüfen
> - Zeile-mal-Spalte-Regel korrekt anwenden
> - Nicht-Kommutativität beachten ($AB \neq BA$)
> - Dimension des Ergebnisses bestimmen
> - Matrix-Vektor-Produkt berechnen können

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie das Produkt $A \cdot B$.
> - Ist $B \cdot A$ ebenfalls definiert? Wenn ja, berechnen Sie es.
> - Zeigen Sie an einem Beispiel, dass $A \cdot B \neq B \cdot A$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Inverse-Matrizen]] — Die "Division" bei Matrizen
> - [[Determinanten]] — Wichtig für Invertierbarkeit
