---
author: Andreas Hümmer
title: Orthogonalität
tags:
  - content
  - mathe
  - vektorrechnung
  - orthogonalitaet
  - senkrecht
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Orthogonalität

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Orthogonalitätskriterium für Vektoren kennen und anwenden können
> - Orthogonale Vektoren konstruieren können
> - Den Begriff des Orthonormalsystems verstehen
> - Orthogonale Zerlegung von Vektoren durchführen können

---

## Überblick

Zwei Vektoren heißen **orthogonal** (oder **senkrecht**), wenn sie einen rechten Winkel einschließen. Die Orthogonalität ist ein zentrales Konzept der Vektorrechnung mit vielfältigen Anwendungen – von der Bestimmung von Normalenvektoren bis zur Konstruktion orthogonaler Koordinatensysteme.

## Definition und Kriterium

> Zwei Vektoren $\vec{a}$ und $\vec{b}$ sind genau dann orthogonal (senkrecht), wenn ihr Skalarprodukt null ist:
> $$\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0$$

### Schreibweise

- $\vec{a} \perp \vec{b}$ bedeutet: „$\vec{a}$ ist orthogonal zu $\vec{b}$"
- Das Symbol $\perp$ steht für „senkrecht zu"

### Beweis des Kriteriums

Aus der geometrischen Formel für das Skalarprodukt:

$$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos\varphi$$

Für $\vec{a}, \vec{b} \neq \vec{0}$ gilt $\vec{a} \cdot \vec{b} = 0$ genau dann, wenn $\cos\varphi = 0$, also wenn $\varphi = 90°$.

## Beispiele zur Orthogonalitätsprüfung

### Beispiel 1: Orthogonale Vektoren

Prüfe, ob $\vec{a} = \begin{pmatrix} 3 \\ 1 \\ -2 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 2 \\ 4 \\ 5 \end{pmatrix}$ orthogonal sind.

$$\vec{a} \cdot \vec{b} = 3 \cdot 2 + 1 \cdot 4 + (-2) \cdot 5 = 6 + 4 - 10 = 0$$

Da das Skalarprodukt null ist: $\vec{a} \perp \vec{b}$ ✓

### Beispiel 2: Nicht orthogonale Vektoren

Prüfe, ob $\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ und $\vec{v} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$ orthogonal sind.

$$\vec{u} \cdot \vec{v} = 4 + 10 + 18 = 32 \neq 0$$

Die Vektoren sind **nicht orthogonal**.

## Orthogonale Vektoren konstruieren

### In der Ebene ($\mathbb{R}^2$)

Zu $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$ ist der Vektor $\vec{a}^{\perp} = \begin{pmatrix} -a_2 \\ a_1 \end{pmatrix}$ orthogonal.

**Probe:** $\vec{a} \cdot \vec{a}^{\perp} = a_1 \cdot (-a_2) + a_2 \cdot a_1 = 0$ ✓

**Beispiel:** Zu $\vec{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ ist $\vec{a}^{\perp} = \begin{pmatrix} -4 \\ 3 \end{pmatrix}$ orthogonal.

### Im Raum ($\mathbb{R}^3$)

Zu einem gegebenen Vektor $\vec{a}$ gibt es unendlich viele orthogonale Vektoren (sie bilden eine Ebene). Ein orthogonaler Vektor kann durch das Kreuzprodukt mit einem beliebigen nicht-parallelen Vektor gefunden werden.

**Systematische Methode:** Setze eine Gleichung auf mit Parametern.

**Beispiel:** Finde einen Vektor orthogonal zu $\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.

Ansatz: $\vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$ mit $\vec{a} \cdot \vec{b} = 0$

$$1 \cdot b_1 + 2 \cdot b_2 + 3 \cdot b_3 = 0$$

Wähle $b_1 = 1, b_2 = 1$, dann: $1 + 2 + 3b_3 = 0 \Rightarrow b_3 = -1$

Also: $\vec{b} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$ ist orthogonal zu $\vec{a}$.

## Orthogonale Zerlegung

Ein Vektor $\vec{v}$ kann in zwei Komponenten zerlegt werden: eine parallel zu einem gegebenen Vektor $\vec{a}$ und eine orthogonal dazu.

### Formel für die orthogonale Zerlegung

$$\vec{v} = \vec{v}_{\parallel} + \vec{v}_{\perp}$$

wobei:

$$\vec{v}_{\parallel} = \frac{\vec{v} \cdot \vec{a}}{|\vec{a}|^2} \cdot \vec{a}$$

$$\vec{v}_{\perp} = \vec{v} - \vec{v}_{\parallel}$$

### Beispielrechnung

Zerlege $\vec{v} = \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix}$ bezüglich $\vec{a} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.

$$\vec{v}_{\parallel} = \frac{\vec{v} \cdot \vec{a}}{|\vec{a}|^2} \cdot \vec{a} = \frac{3}{1} \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}$$

$$\vec{v}_{\perp} = \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} - \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix}$$

**Probe:** $\vec{v}_{\perp} \cdot \vec{a} = 0$ ✓

## Orthonormalsysteme

Eine Menge von Vektoren $\{\vec{e}_1, \vec{e}_2, \vec{e}_3, \ldots\}$ heißt **Orthonormalsystem** (ONS), wenn:

1. Alle Vektoren paarweise orthogonal sind: $\vec{e}_i \cdot \vec{e}_j = 0$ für $i \neq j$
2. Alle Vektoren Einheitsvektoren sind: $|\vec{e}_i| = 1$

Zusammengefasst: $\vec{e}_i \cdot \vec{e}_j = \delta_{ij}$ (Kronecker-Delta)

### Die Standardbasis als Orthonormalsystem

Die Standardbasisvektoren bilden ein Orthonormalsystem:

$$\vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

Prüfung:
- $\vec{e}_1 \cdot \vec{e}_2 = 0$, $\vec{e}_1 \cdot \vec{e}_3 = 0$, $\vec{e}_2 \cdot \vec{e}_3 = 0$ ✓
- $|\vec{e}_1| = |\vec{e}_2| = |\vec{e}_3| = 1$ ✓

## Anwendungen der Orthogonalität

### 1. Normalenvektoren

Ein **Normalenvektor** einer Ebene steht senkrecht auf allen Vektoren in dieser Ebene. In der Ebenengleichung $\vec{n} \cdot (\vec{x} - \vec{p}) = 0$ ist $\vec{n}$ der Normalenvektor.

### 2. Lotfußpunkt

Der Lotfußpunkt $F$ ist der Punkt auf einer Geraden $g$, der einem gegebenen Punkt $P$ am nächsten liegt. Der Vektor $\vec{PF}$ steht senkrecht zur Geraden.

### 3. Abstandsberechnungen

Viele Abstandsformeln basieren auf orthogonalen Projektionen.

## Besondere Eigenschaften

| Eigenschaft | Formel/Aussage |
|-------------|----------------|
| Der Nullvektor | $\vec{0} \perp \vec{a}$ für alle $\vec{a}$ |
| Symmetrie | $\vec{a} \perp \vec{b} \Leftrightarrow \vec{b} \perp \vec{a}$ |
| Skalierung | $\vec{a} \perp \vec{b} \Rightarrow (k\vec{a}) \perp \vec{b}$ für alle $k \in \mathbb{R}$ |
| Satz des Pythagoras | $\vec{a} \perp \vec{b} \Rightarrow |\vec{a} + \vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Skalarprodukt]] — Grundlage des Orthogonalitätskriteriums
- → [[Winkel-zwischen-Vektoren]] — Orthogonalität als Spezialfall ($90°$)
- → [[Einheitsvektoren]] — Orthonormalsysteme
- → [[Kreuzprodukt]] — Erzeugung orthogonaler Vektoren

> [!warning] **Prüfungsrelevant**
> - Orthogonalitätskriterium: $\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0$
> - Prüfung auf Orthogonalität durch Skalarprodukt
> - Konstruktion orthogonaler Vektoren (besonders in $\mathbb{R}^2$)
> - Orthogonale Zerlegung eines Vektors
> - Satz des Pythagoras für orthogonale Vektoren

> [!question] **Typische Prüfungsfragen**
> - Prüfe, ob die Vektoren $\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ und $\begin{pmatrix} 1 \\ 5 \\ 1 \end{pmatrix}$ orthogonal sind.
> - Bestimme einen Vektor, der sowohl zu $\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$ als auch zu $\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ orthogonal ist.
> - Für welchen Wert von $t$ sind $\begin{pmatrix} 2 \\ t \\ -1 \end{pmatrix}$ und $\begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}$ orthogonal?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Normalenvektoren und Lotfußpunkte
> - [[12-Einfuehrung-in-die-lineare-Algebra-Index|Lineare Algebra]] — Orthogonale Matrizen
