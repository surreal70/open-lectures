---
author: Andreas Hümmer
title: Ortsvektoren
tags:
  - content
  - mathe
  - vektorrechnung
  - ortsvektoren
  - koordinatengeometrie
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Ortsvektoren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Ortsvektor eines Punktes bestimmen können
> - Die Beziehung zwischen Punkten, Ortsvektoren und freien Vektoren verstehen
> - Punkte durch ihre Ortsvektoren beschreiben können
> - Den Mittelpunkt einer Strecke mit Ortsvektoren berechnen können

---

## Überblick

Ein **Ortsvektor** ist ein spezieller Vektor, der einen Punkt im Raum eindeutig festlegt. Er beginnt immer im Ursprung des Koordinatensystems und endet im betrachteten Punkt. Ortsvektoren bilden die Brücke zwischen der Punktgeometrie und der Vektorrechnung und sind fundamental für die analytische Geometrie.

## Definition des Ortsvektors

Der **Ortsvektor** $\vec{r}_P$ (oder kurz $\vec{p}$) eines Punktes $P(p_1|p_2|p_3)$ ist der Vektor vom Ursprung $O$ zum Punkt $P$:

$$\vec{r}_P = \vec{OP} = \begin{pmatrix} p_1 \\ p_2 \\ p_3 \end{pmatrix}$$

Die Komponenten des Ortsvektors entsprechen genau den Koordinaten des Punktes.

### Beispiele

| Punkt | Ortsvektor |
|-------|------------|
| $A(3|2|1)$ | $\vec{a} = \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}$ |
| $B(-1|4|0)$ | $\vec{b} = \begin{pmatrix} -1 \\ 4 \\ 0 \end{pmatrix}$ |
| $O(0|0|0)$ | $\vec{o} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = \vec{0}$ |

## Ortsvektoren und Verbindungsvektoren

Eine zentrale Beziehung verknüpft Ortsvektoren mit Verbindungsvektoren:

> Der Verbindungsvektor $\vec{AB}$ ergibt sich aus der Differenz der Ortsvektoren:
> $$\vec{AB} = \vec{b} - \vec{a}$$

### Herleitung

Mit der Kettenregel für Vektoren gilt:

$$\vec{AB} = \vec{AO} + \vec{OB} = -\vec{OA} + \vec{OB} = \vec{b} - \vec{a}$$

Dies entspricht der bekannten Regel „Spitze minus Fuß".

### Beispielrechnung

Gegeben: $A(2|3|1)$ und $B(5|1|4)$

Ortsvektoren: $\vec{a} = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$, $\vec{b} = \begin{pmatrix} 5 \\ 1 \\ 4 \end{pmatrix}$

Verbindungsvektor:
$$\vec{AB} = \vec{b} - \vec{a} = \begin{pmatrix} 5 \\ 1 \\ 4 \end{pmatrix} - \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ -2 \\ 3 \end{pmatrix}$$

## Mittelpunkt einer Strecke

Der Mittelpunkt $M$ einer Strecke $\overline{AB}$ hat den Ortsvektor:

$$\vec{m} = \frac{1}{2}(\vec{a} + \vec{b})$$

Oder in Koordinaten ausgedrückt:

$$M\left(\frac{a_1 + b_1}{2} \;\middle|\; \frac{a_2 + b_2}{2} \;\middle|\; \frac{a_3 + b_3}{2}\right)$$

### Beispielrechnung

Für $A(1|5|3)$ und $B(7|1|9)$:

$$\vec{m} = \frac{1}{2}\left(\begin{pmatrix} 1 \\ 5 \\ 3 \end{pmatrix} + \begin{pmatrix} 7 \\ 1 \\ 9 \end{pmatrix}\right) = \frac{1}{2}\begin{pmatrix} 8 \\ 6 \\ 12 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \\ 6 \end{pmatrix}$$

Also: $M(4|3|6)$

## Teilpunkte einer Strecke

Allgemeiner kann man den Punkt $T$ bestimmen, der die Strecke $\overline{AB}$ im Verhältnis $t:(1-t)$ teilt:

$$\vec{t} = \vec{a} + t \cdot (\vec{b} - \vec{a}) = (1-t) \cdot \vec{a} + t \cdot \vec{b}$$

| Wert von $t$ | Lage von $T$ |
|--------------|--------------|
| $t = 0$ | $T = A$ |
| $t = 0{,}5$ | $T = M$ (Mittelpunkt) |
| $t = 1$ | $T = B$ |
| $0 < t < 1$ | $T$ liegt zwischen $A$ und $B$ |
| $t < 0$ oder $t > 1$ | $T$ liegt außerhalb der Strecke |

### Beispiel: Teilpunkt im Verhältnis 1:2

Gesucht ist der Punkt $T$, der $\overline{AB}$ im Verhältnis $1:2$ teilt (von $A$ aus gesehen).

Mit $t = \frac{1}{3}$:

$$\vec{t} = \vec{a} + \frac{1}{3}(\vec{b} - \vec{a}) = \frac{2}{3}\vec{a} + \frac{1}{3}\vec{b}$$

## Schwerpunkt eines Dreiecks

Der **Schwerpunkt** $S$ eines Dreiecks $ABC$ hat den Ortsvektor:

$$\vec{s} = \frac{1}{3}(\vec{a} + \vec{b} + \vec{c})$$

Dies ist das arithmetische Mittel der drei Ortsvektoren.

### Beispielrechnung

Für das Dreieck mit $A(0|0|0)$, $B(6|0|0)$, $C(3|6|0)$:

$$\vec{s} = \frac{1}{3}\left(\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 6 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 3 \\ 6 \\ 0 \end{pmatrix}\right) = \frac{1}{3}\begin{pmatrix} 9 \\ 6 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix}$$

Der Schwerpunkt liegt bei $S(3|2|0)$.

## Ortsvektoren vs. freie Vektoren

| Eigenschaft | Ortsvektor | Freier Vektor |
|-------------|------------|---------------|
| Anfangspunkt | Fest im Ursprung | Beliebig |
| Beschreibt | Position eines Punktes | Richtung und Länge |
| Notation | $\vec{OP}$ oder $\vec{r}_P$ | $\vec{v}$, $\vec{a}$, ... |
| Verschiebbar | Nein | Ja (Repräsentanten) |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Vektorbegriff und Grundlagen
- → [[Vektordarstellung]] — Koordinatendarstellung von Vektoren
- → [[Vektoraddition]] — Addition für Mittelpunkt- und Schwerpunktberechnung
- → [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Geraden- und Ebenengleichungen mit Ortsvektoren

> [!warning] **Prüfungsrelevant**
> - Zusammenhang zwischen Punktkoordinaten und Ortsvektoren
> - Berechnung von Verbindungsvektoren über Ortsvektoren: $\vec{AB} = \vec{b} - \vec{a}$
> - Mittelpunktformel mit Ortsvektoren
> - Schwerpunktberechnung für Dreiecke
> - Teilpunktberechnung mit Parameter $t$

> [!question] **Typische Prüfungsfragen**
> - Berechne den Mittelpunkt der Strecke $\overline{AB}$ mit $A(-2|4|3)$ und $B(6|0|5)$.
> - Bestimme den Punkt $T$, der die Strecke $\overline{AB}$ im Verhältnis $2:3$ teilt.
> - Ein Dreieck hat die Eckpunkte $A(1|2|3)$, $B(4|5|6)$ und $C(7|2|0)$. Berechne den Schwerpunkt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[Anwendungen-im-dreidimensionalen-Raum]] — Praktische Anwendungen der Ortsvektor-Rechnung
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Parameterdarstellung von Geraden
