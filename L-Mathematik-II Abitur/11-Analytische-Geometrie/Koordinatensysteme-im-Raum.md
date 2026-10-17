---
author: Andreas Hümmer
title: Koordinatensysteme im Raum
tags:
  - content
  - mathe
  - analytische-geometrie
  - koordinatensystem
  - dreidimensional
created: 2026-10-17
modified: 2026-10-17
---

# Koordinatensysteme im Raum

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das kartesische Koordinatensystem im dreidimensionalen Raum verstehen und anwenden können
> - Punkte durch Koordinatentripel $(x, y, z)$ eindeutig beschreiben
> - Die Rechte-Hand-Regel zur Orientierung der Achsen kennen
> - Abstände zwischen Punkten im Raum berechnen können

---

## Überblick

Das dreidimensionale kartesische Koordinatensystem bildet das Fundament der analytischen Geometrie. Es ermöglicht die eindeutige Beschreibung jedes Punktes im Raum durch ein geordnetes Tripel reeller Zahlen und schafft damit die Grundlage für rechnerische Untersuchungen geometrischer Objekte.

## Das kartesische Koordinatensystem

Ein kartesisches Koordinatensystem im Raum $\mathbb{R}^3$ besteht aus drei paarweise senkrecht aufeinander stehenden Koordinatenachsen, die sich in einem gemeinsamen Punkt, dem **Ursprung** $O$, schneiden.

Die drei Achsen werden bezeichnet als:
- **x-Achse** (Abszisse): zeigt typischerweise nach rechts
- **y-Achse** (Ordinate): zeigt nach vorne (aus der Zeichenebene heraus)
- **z-Achse** (Applikate): zeigt nach oben

### Die Rechte-Hand-Regel

Die Orientierung eines rechtshändigen Koordinatensystems lässt sich mit der **Rechte-Hand-Regel** bestimmen:

1. Der Daumen zeigt in Richtung der positiven x-Achse
2. Der Zeigefinger zeigt in Richtung der positiven y-Achse
3. Der Mittelfinger (senkrecht abgespreizt) zeigt in Richtung der positiven z-Achse

Diese Konvention ist in Mathematik und Physik Standard und gewährleistet eine einheitliche Orientierung des Raumes.

## Punkte im Raum

Jeder Punkt $P$ im dreidimensionalen Raum wird durch ein geordnetes Tripel reeller Zahlen beschrieben:

$$P = (x_P, y_P, z_P)$$

Die Koordinaten geben die Abstände des Punktes von den Koordinatenebenen an:
- $x_P$: Abstand von der $yz$-Ebene (mit Vorzeichen)
- $y_P$: Abstand von der $xz$-Ebene (mit Vorzeichen)
- $z_P$: Abstand von der $xy$-Ebene (mit Vorzeichen)

### Beispiel: Würfeleckpunkte

Ein Würfel mit Kantenlänge $a = 2$, dessen eine Ecke im Ursprung liegt und dessen Kanten parallel zu den Koordinatenachsen verlaufen, hat die Eckpunkte:

| Punkt | Koordinaten |
|-------|-------------|
| $A$ | $(0, 0, 0)$ |
| $B$ | $(2, 0, 0)$ |
| $C$ | $(2, 2, 0)$ |
| $D$ | $(0, 2, 0)$ |
| $E$ | $(0, 0, 2)$ |
| $F$ | $(2, 0, 2)$ |
| $G$ | $(2, 2, 2)$ |
| $H$ | $(0, 2, 2)$ |

## Die Koordinatenebenen

Die drei Koordinatenachsen spannen paarweise drei Koordinatenebenen auf:

- **xy-Ebene**: alle Punkte mit $z = 0$
- **xz-Ebene**: alle Punkte mit $y = 0$
- **yz-Ebene**: alle Punkte mit $x = 0$

Diese Ebenen teilen den Raum in acht **Oktanten** (analog zu den vier Quadranten in der Ebene).

### Die acht Oktanten

| Oktant | x | y | z |
|--------|---|---|---|
| I      | + | + | + |
| II     | − | + | + |
| III    | − | − | + |
| IV     | + | − | + |
| V      | + | + | − |
| VI     | − | + | − |
| VII    | − | − | − |
| VIII   | + | − | − |

## Abstand zwischen zwei Punkten

Der Abstand zwischen zwei Punkten $P_1 = (x_1, y_1, z_1)$ und $P_2 = (x_2, y_2, z_2)$ wird mit dem **Satz des Pythagoras** in drei Dimensionen berechnet:

$$d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

Diese Formel ist die direkte Verallgemeinerung der Abstandsformel aus der Ebene.

### Beispiel: Abstandsberechnung

Gegeben sind die Punkte $A = (1, 2, 3)$ und $B = (4, 6, 3)$.

$$d(A, B) = \sqrt{(4-1)^2 + (6-2)^2 + (3-3)^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$$

Der Abstand beträgt $5$ Längeneinheiten.

## Mittelpunkt einer Strecke

Der Mittelpunkt $M$ einer Strecke $\overline{P_1 P_2}$ ergibt sich als arithmetisches Mittel der Koordinaten:

$$M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}, \frac{z_1 + z_2}{2} \right)$$

### Beispiel: Mittelpunkt berechnen

Für $P_1 = (2, 4, 6)$ und $P_2 = (8, 10, 2)$:

$$M = \left( \frac{2+8}{2}, \frac{4+10}{2}, \frac{6+2}{2} \right) = (5, 7, 4)$$

## Teilverhältnis

Ein Punkt $T$ teilt die Strecke $\overline{P_1 P_2}$ im Verhältnis $\lambda : (1-\lambda)$ mit $\lambda \in [0, 1]$:

$$T = P_1 + \lambda \cdot (P_2 - P_1) = (1-\lambda) \cdot P_1 + \lambda \cdot P_2$$

Für $\lambda = 0$ erhält man $P_1$, für $\lambda = 1$ erhält man $P_2$, für $\lambda = 0{,}5$ den Mittelpunkt.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Vektoren als Verbindung zwischen Punkten
- → [[Ortsvektoren]] — Darstellung von Punkten durch Ortsvektoren
- → [[Betrag-eines-Vektors]] — Zusammenhang mit der Abstandsformel
- → [[Geraden-in-Parameterform]] — Darstellung von Geraden im Koordinatensystem

> [!warning] **Prüfungsrelevant**
> - Die Abstandsformel im Raum $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$
> - Bestimmung des Mittelpunkts einer Strecke
> - Koordinaten von Punkten aus geometrischen Beschreibungen ablesen
> - Rechte-Hand-Regel zur Achsenorientierung

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie den Abstand zwischen den Punkten $A(2|3|1)$ und $B(5|7|−3)$.
> - Ein Quader hat die Eckpunkte $A(0|0|0)$, $B(4|0|0)$, $D(0|3|0)$ und $E(0|0|2)$. Bestimmen Sie die Koordinaten aller weiteren Eckpunkte.
> - In welchem Verhältnis teilt der Punkt $T(3|5|2)$ die Strecke $\overline{AB}$ mit $A(1|2|4)$ und $B(7|11|−2)$?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, Jahrgangsstufen 11/12

> [!tip] **Weiterführende Links**
> - [[Vektordarstellung]] — Alternative Darstellung mit Ortsvektoren
> - [[Anwendungen-im-dreidimensionalen-Raum]] — Praktische Anwendungen
