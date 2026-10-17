---
author: Andreas Hümmer
title: Kreuzprodukt
tags:
  - content
  - mathe
  - vektorrechnung
  - kreuzprodukt
  - vektorprodukt
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Kreuzprodukt

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Kreuzprodukt zweier Vektoren berechnen können
> - Die geometrische Bedeutung des Kreuzprodukts verstehen (Normalenvektor, Flächeninhalt)
> - Die Rechte-Hand-Regel anwenden können
> - Rechenregeln und Spezialfälle des Kreuzprodukts kennen

---

## Überblick

Das **Kreuzprodukt** (auch Vektorprodukt oder äußeres Produkt genannt) ist eine Verknüpfung zweier Vektoren, deren Ergebnis wieder ein Vektor ist – im Gegensatz zum Skalarprodukt, das eine Zahl liefert. Der resultierende Vektor steht senkrecht auf beiden Ausgangsvektoren und hat einen Betrag, der dem Flächeninhalt des aufgespannten Parallelogramms entspricht.

## Definition

Das Kreuzprodukt zweier Vektoren $\vec{a}$ und $\vec{b}$ ist definiert als:

$$\vec{a} \times \vec{b} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \times \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{pmatrix} a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3 \\ a_1 b_2 - a_2 b_1 \end{pmatrix}$$

### Merkregel: Schema der „Kreuzung"

Die Komponenten entstehen durch „Kreuzung" der jeweils anderen Komponenten:

| Komponente | Berechnung |
|------------|------------|
| 1. Komponente | $a_2 \cdot b_3 - a_3 \cdot b_2$ (aus 2. und 3.) |
| 2. Komponente | $a_3 \cdot b_1 - a_1 \cdot b_3$ (aus 3. und 1.) |
| 3. Komponente | $a_1 \cdot b_2 - a_2 \cdot b_1$ (aus 1. und 2.) |

### Determinanten-Schreibweise

$$\vec{a} \times \vec{b} = \begin{vmatrix} \vec{e}_1 & \vec{e}_2 & \vec{e}_3 \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$$

## Beispielrechnungen

### Beispiel 1

Berechne $\vec{a} \times \vec{b}$ für $\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$.

$$\vec{a} \times \vec{b} = \begin{pmatrix} 2 \cdot 6 - 3 \cdot 5 \\ 3 \cdot 4 - 1 \cdot 6 \\ 1 \cdot 5 - 2 \cdot 4 \end{pmatrix} = \begin{pmatrix} 12 - 15 \\ 12 - 6 \\ 5 - 8 \end{pmatrix} = \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}$$

**Probe:** Orthogonalität prüfen
- $\vec{a} \cdot (\vec{a} \times \vec{b}) = 1 \cdot (-3) + 2 \cdot 6 + 3 \cdot (-3) = -3 + 12 - 9 = 0$ ✓
- $\vec{b} \cdot (\vec{a} \times \vec{b}) = 4 \cdot (-3) + 5 \cdot 6 + 6 \cdot (-3) = -12 + 30 - 18 = 0$ ✓

### Beispiel 2: Standardbasisvektoren

$$\vec{e}_1 \times \vec{e}_2 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \cdot 0 - 0 \cdot 1 \\ 0 \cdot 0 - 1 \cdot 0 \\ 1 \cdot 1 - 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \vec{e}_3$$

## Geometrische Interpretation

### Richtung: Rechte-Hand-Regel

Der Vektor $\vec{a} \times \vec{b}$ steht **senkrecht** auf $\vec{a}$ und $\vec{b}$. Die Richtung wird durch die **Rechte-Hand-Regel** bestimmt:

1. Zeigefinger in Richtung von $\vec{a}$
2. Mittelfinger in Richtung von $\vec{b}$
3. Daumen zeigt in Richtung von $\vec{a} \times \vec{b}$

```
        ↑ a × b (Daumen)
        |
        |
        +──────→ a (Zeigefinger)
       /
      /
     ↙ b (Mittelfinger)
```

### Betrag: Flächeninhalt des Parallelogramms

Der Betrag des Kreuzprodukts entspricht dem Flächeninhalt des von $\vec{a}$ und $\vec{b}$ aufgespannten Parallelogramms:

$$|\vec{a} \times \vec{b}| = |\vec{a}| \cdot |\vec{b}| \cdot \sin\varphi$$

wobei $\varphi$ der Winkel zwischen $\vec{a}$ und $\vec{b}$ ist.

### Flächenberechnung eines Dreiecks

Die Fläche eines Dreiecks mit den Seitenvektoren $\vec{a}$ und $\vec{b}$ ist:

$$A_{\triangle} = \frac{1}{2} |\vec{a} \times \vec{b}|$$

## Rechenregeln

Das Kreuzprodukt hat besondere Eigenschaften:

| Eigenschaft | Formel |
|-------------|--------|
| **Antikommutativität** | $\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$ |
| **Distributivgesetz** | $\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}$ |
| **Homogenität** | $(k\vec{a}) \times \vec{b} = k(\vec{a} \times \vec{b}) = \vec{a} \times (k\vec{b})$ |
| **Nicht assoziativ** | $(\vec{a} \times \vec{b}) \times \vec{c} \neq \vec{a} \times (\vec{b} \times \vec{c})$ |

### Wichtige Spezialfälle

| Fall | Ergebnis | Grund |
|------|----------|-------|
| $\vec{a} \times \vec{a}$ | $\vec{0}$ | $\sin(0°) = 0$ |
| $\vec{a} \times \vec{0}$ | $\vec{0}$ | Nullvektor |
| $\vec{a} \times \vec{b}$ mit $\vec{a} \parallel \vec{b}$ | $\vec{0}$ | $\sin(0°) = 0$ oder $\sin(180°) = 0$ |

## Kreuzprodukt der Standardbasisvektoren

$$\vec{e}_1 \times \vec{e}_2 = \vec{e}_3, \quad \vec{e}_2 \times \vec{e}_3 = \vec{e}_1, \quad \vec{e}_3 \times \vec{e}_1 = \vec{e}_2$$

Bei umgekehrter Reihenfolge:

$$\vec{e}_2 \times \vec{e}_1 = -\vec{e}_3, \quad \vec{e}_3 \times \vec{e}_2 = -\vec{e}_1, \quad \vec{e}_1 \times \vec{e}_3 = -\vec{e}_2$$

## Anwendungen

### 1. Normalenvektor einer Ebene

Zwei nicht-parallele Vektoren $\vec{a}$ und $\vec{b}$ in einer Ebene spannen diese auf. Der Normalenvektor ist:

$$\vec{n} = \vec{a} \times \vec{b}$$

**Beispiel:** Finde den Normalenvektor der Ebene durch die Punkte $P(1|0|0)$, $Q(0|1|0)$, $R(0|0|1)$.

Richtungsvektoren:
- $\vec{PQ} = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$
- $\vec{PR} = \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$

$$\vec{n} = \vec{PQ} \times \vec{PR} = \begin{pmatrix} 1 \cdot 1 - 0 \cdot 0 \\ 0 \cdot (-1) - (-1) \cdot 1 \\ (-1) \cdot 0 - 1 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$$

### 2. Flächeninhalt eines Parallelogramms

Das Parallelogramm mit den Seiten $\vec{a} = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ hat den Flächeninhalt:

$$\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 0 \\ 6 \end{pmatrix}$$

$$A = |\vec{a} \times \vec{b}| = 6$$

### 3. Drehmoment in der Physik

Das Drehmoment $\vec{M}$ einer Kraft $\vec{F}$, die am Hebelarm $\vec{r}$ angreift:

$$\vec{M} = \vec{r} \times \vec{F}$$

## Zusammenhang mit dem Skalarprodukt

Die **Lagrange-Identität** verbindet Kreuz- und Skalarprodukt:

$$|\vec{a} \times \vec{b}|^2 = |\vec{a}|^2 \cdot |\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Skalarprodukt]] — Vergleich: Ergebnis ist Zahl vs. Vektor
- → [[Orthogonalitaet]] — Kreuzprodukt steht senkrecht auf beiden Faktoren
- → [[Anwendungen-im-dreidimensionalen-Raum]] — Flächen- und Volumenberechnungen

> [!warning] **Prüfungsrelevant**
> - Berechnung des Kreuzprodukts in Koordinatenform
> - Geometrische Bedeutung: Normalenvektor und Flächeninhalt
> - Rechte-Hand-Regel für die Richtung
> - Antikommutativität: $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$
> - Spezialfall: $\vec{a} \times \vec{a} = \vec{0}$

> [!question] **Typische Prüfungsfragen**
> - Berechne $\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix} \times \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix}$.
> - Bestimme den Flächeninhalt des Dreiecks mit den Eckpunkten $A(1|0|0)$, $B(0|2|0)$, $C(0|0|3)$.
> - Finde den Normalenvektor der Ebene, die durch $\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}$ aufgespannt wird.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Ebenengleichungen mit Normalenvektoren
> - [[12-Einfuehrung-in-die-lineare-Algebra-Index|Lineare Algebra]] — Determinanten und das Kreuzprodukt
