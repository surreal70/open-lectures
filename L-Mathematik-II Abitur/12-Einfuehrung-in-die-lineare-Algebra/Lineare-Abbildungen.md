---
author: Andreas Hümmer
title: Lineare Abbildungen
tags:
  - content
  - mathe
  - lineare-algebra
  - abbildungen
  - transformationen
  - matrizen
created: 2025-07-01
modified: 2025-07-01
---

# Lineare Abbildungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition einer linearen Abbildung kennen (Additivität und Homogenität)
> - Verstehen, wie Matrizen lineare Abbildungen darstellen
> - Wichtige geometrische Transformationen (Drehung, Skalierung, Spiegelung) als Matrizen schreiben können
> - Die Verkettung von Abbildungen durch Matrizenmultiplikation verstehen
> - Bild und Kern einer linearen Abbildung interpretieren können

---

## Überblick

Eine **lineare Abbildung** ist eine Funktion zwischen Vektorräumen, die die Vektorraumstruktur erhält. Das Besondere: Jede lineare Abbildung zwischen endlichdimensionalen Vektorräumen kann durch eine Matrix dargestellt werden. Geometrische Transformationen wie Drehungen, Spiegelungen und Skalierungen sind wichtige Beispiele linearer Abbildungen.

## Definition

### Lineare Abbildung

Eine Abbildung $f: \mathbb{R}^n \to \mathbb{R}^m$ heißt **linear**, wenn für alle Vektoren $\vec{u}, \vec{v} \in \mathbb{R}^n$ und alle Skalare $\lambda \in \mathbb{R}$ gilt:

1. **Additivität:** $f(\vec{u} + \vec{v}) = f(\vec{u}) + f(\vec{v})$
2. **Homogenität:** $f(\lambda \cdot \vec{u}) = \lambda \cdot f(\vec{u})$

Äquivalent kann man beide Eigenschaften zusammenfassen:

$$
f(\lambda \vec{u} + \mu \vec{v}) = \lambda \cdot f(\vec{u}) + \mu \cdot f(\vec{v})
$$

### Wichtige Konsequenz

Für jede lineare Abbildung gilt: $f(\vec{0}) = \vec{0}$

## Darstellung durch Matrizen

### Hauptsatz

Jede lineare Abbildung $f: \mathbb{R}^n \to \mathbb{R}^m$ kann durch eine $(m \times n)$-Matrix $A$ dargestellt werden:

$$
f(\vec{x}) = A \cdot \vec{x}
$$

Die Spalten von $A$ sind die Bilder der Standardbasisvektoren:

$$
A = \begin{pmatrix} | & | & & | \\ f(\vec{e}_1) & f(\vec{e}_2) & \cdots & f(\vec{e}_n) \\ | & | & & | \end{pmatrix}
$$

### Beispiel

Die Abbildung $f: \mathbb{R}^2 \to \mathbb{R}^2$ mit $f(x, y) = (2x + y, x - y)$

Bilder der Basisvektoren:
- $f(\vec{e}_1) = f(1, 0) = (2, 1)$
- $f(\vec{e}_2) = f(0, 1) = (1, -1)$

Matrix:
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}
$$

## Geometrische Transformationen in 2D

### Skalierung

Streckung/Stauchung um Faktoren $s_x$ und $s_y$:

$$
S = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}
$$

**Gleichmäßige Skalierung** (um Faktor $k$):

$$
S = \begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix} = k \cdot I
$$

### Spiegelung

**An der x-Achse:**
$$
M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**An der y-Achse:**
$$
M_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}
$$

**Am Ursprung (Punktspiegelung):**
$$
M_O = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**An der Geraden $y = x$:**
$$
M_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

### Drehung um den Ursprung

Drehung um den Winkel $\varphi$ (gegen den Uhrzeigersinn):

$$
D_\varphi = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}
$$

**Beispiel:** Drehung um 90°

$$
D_{90°} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$

### Scherung

**Horizontale Scherung:**
$$
H_k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}
$$

**Vertikale Scherung:**
$$
V_k = \begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}
$$

## Verkettung von Abbildungen

Die **Hintereinanderausführung** (Verkettung) von linearen Abbildungen entspricht der **Matrizenmultiplikation**:

$$
(g \circ f)(\vec{x}) = g(f(\vec{x})) = B \cdot (A \cdot \vec{x}) = (B \cdot A) \cdot \vec{x}
$$

**Achtung:** Die Reihenfolge der Matrizen ist umgekehrt zur Reihenfolge der Ausführung!

### Beispiel

Erst Drehung um 90°, dann Spiegelung an der x-Achse:

$$
M_x \cdot D_{90°} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \cdot \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}
$$

## Bild und Kern

### Kern (Nullraum)

Der **Kern** einer linearen Abbildung $f$ (mit Matrix $A$) ist:

$$
\text{Kern}(f) = \text{ker}(A) = \{\vec{x} \in \mathbb{R}^n \mid A \cdot \vec{x} = \vec{0}\}
$$

Der Kern ist die Lösungsmenge des homogenen Gleichungssystems.

### Bild

Das **Bild** einer linearen Abbildung $f$ ist:

$$
\text{Bild}(f) = \text{im}(A) = \{A \cdot \vec{x} \mid \vec{x} \in \mathbb{R}^n\}
$$

Das Bild ist der Spann der Spaltenvektoren von $A$.

### Dimensionsformel

$$
\dim(\text{Kern}(f)) + \dim(\text{Bild}(f)) = n
$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizen]] — Matrixdarstellung
- → [[Matrizenmultiplikation]] — Verkettung von Abbildungen
- → [[Determinanten]] — Flächenfaktor bei Abbildungen
- → [[Trigonometrische-Funktionen]] — Drehmatrizen

> [!warning] **Prüfungsrelevant**
> - Definition der linearen Abbildung (Additivität, Homogenität)
> - Aufstellen der Abbildungsmatrix aus den Bildern der Basisvektoren
> - Matrizen für Skalierung, Spiegelung und Drehung
> - Verkettung von Abbildungen als Matrizenprodukt
> - Reihenfolge bei Verkettung beachten

> [!question] **Typische Prüfungsfragen**
> - Geben Sie die Matrix der beschriebenen linearen Abbildung an.
> - Welche geometrische Transformation beschreibt die gegebene Matrix?
> - Berechnen Sie die Matrix für die Hintereinanderausführung zweier Transformationen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Einfuehrung-in-Eigenwerte-und-Eigenvektoren]] — Eigenvektoren bleiben bei Abbildung auf ihrer Richtung
> - [[Anwendungen-von-Matrizen]] — Computergrafik und Bildverarbeitung
