---
author: Andreas Hümmer
title: Betrag eines Vektors
tags:
  - content
  - mathe
  - vektorrechnung
  - betrag
  - norm
  - laenge
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Betrag eines Vektors

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Betrag (die Länge) eines Vektors berechnen können
> - Die Formel für den Betrag aus dem Satz des Pythagoras herleiten können
> - Abstände zwischen Punkten mit Vektoren berechnen können
> - Die Eigenschaften der Betragsfunktion kennen

---

## Überblick

Der **Betrag** eines Vektors – auch **Norm** oder **Länge** genannt – ist ein Maß für die „Größe" des Vektors, unabhängig von seiner Richtung. Er entspricht geometrisch der Länge des Pfeils, der den Vektor darstellt. Die Betragsberechnung ist fundamental für viele Anwendungen, von der Abstandsberechnung bis zur Normierung von Vektoren.

## Definition des Betrags

Der **Betrag** eines Vektors $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ ist definiert als:

$$|\vec{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$$

Alternative Schreibweisen: $\|\vec{a}\|$ oder $\lVert\vec{a}\rVert$

### In der Ebene ($\mathbb{R}^2$)

$$|\vec{a}| = \sqrt{a_1^2 + a_2^2}$$

## Herleitung über den Satz des Pythagoras

### Im zweidimensionalen Fall

Der Vektor $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$ bildet mit seinen Komponenten ein rechtwinkliges Dreieck:

```
        ↑
   a₂   |        ● (a₁, a₂)
        |       /|
        |      / |
        |  |a|/  | a₂
        |    /   |
        |   /    |
        |  /     |
        | /      |
        +--------+---→
            a₁
```

Nach dem Satz des Pythagoras: $|\vec{a}|^2 = a_1^2 + a_2^2$

### Im dreidimensionalen Fall

Man wendet den Satz des Pythagoras zweimal an:

1. Erst in der $xy$-Ebene: $d_{xy} = \sqrt{a_1^2 + a_2^2}$
2. Dann mit der $z$-Komponente: $|\vec{a}| = \sqrt{d_{xy}^2 + a_3^2} = \sqrt{a_1^2 + a_2^2 + a_3^2}$

## Beispielrechnungen

### Beispiel 1: Vektor in der Ebene

$$\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$

$$|\vec{v}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

### Beispiel 2: Vektor im Raum

$$\vec{w} = \begin{pmatrix} 2 \\ -3 \\ 6 \end{pmatrix}$$

$$|\vec{w}| = \sqrt{2^2 + (-3)^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$$

### Beispiel 3: Vektor mit Wurzeln

$$\vec{u} = \begin{pmatrix} 1 \\ \sqrt{2} \\ \sqrt{5} \end{pmatrix}$$

$$|\vec{u}| = \sqrt{1^2 + (\sqrt{2})^2 + (\sqrt{5})^2} = \sqrt{1 + 2 + 5} = \sqrt{8} = 2\sqrt{2}$$

## Abstand zwischen zwei Punkten

Der **Abstand** $d$ zwischen zwei Punkten $A$ und $B$ ist der Betrag des Verbindungsvektors:

$$d(A, B) = |\vec{AB}| = |\vec{b} - \vec{a}|$$

### Abstandsformel in Koordinaten

Für $A(a_1|a_2|a_3)$ und $B(b_1|b_2|b_3)$:

$$d(A, B) = \sqrt{(b_1 - a_1)^2 + (b_2 - a_2)^2 + (b_3 - a_3)^2}$$

### Beispielrechnung: Punktabstand

Gegeben: $A(1|2|3)$ und $B(4|6|3)$

$$d(A, B) = \sqrt{(4-1)^2 + (6-2)^2 + (3-3)^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$$

## Eigenschaften der Betragsfunktion

Die Betragsfunktion hat folgende wichtige Eigenschaften:

| Eigenschaft | Formel | Bedeutung |
|-------------|--------|-----------|
| **Nichtnegativität** | $|\vec{a}| \geq 0$ | Der Betrag ist nie negativ |
| **Definitheit** | $|\vec{a}| = 0 \Leftrightarrow \vec{a} = \vec{0}$ | Nur der Nullvektor hat Betrag 0 |
| **Homogenität** | $|k \cdot \vec{a}| = |k| \cdot |\vec{a}|$ | Skalierung wirkt auf Betrag |
| **Dreiecksungleichung** | $|\vec{a} + \vec{b}| \leq |\vec{a}| + |\vec{b}|$ | Summe der Seiten ≥ dritte Seite |

### Die Dreiecksungleichung

Die Dreiecksungleichung besagt: Der direkte Weg ist nie länger als ein Umweg.

Geometrisch: In einem Dreieck ist die Länge einer Seite höchstens so groß wie die Summe der beiden anderen.

$$|\vec{a} + \vec{b}| \leq |\vec{a}| + |\vec{b}|$$

Gleichheit gilt genau dann, wenn $\vec{a}$ und $\vec{b}$ gleichgerichtet sind (oder einer der Vektoren der Nullvektor ist).

## Praktische Anwendungen

### Geschwindigkeitsbetrag

Die Geschwindigkeit $\vec{v} = \begin{pmatrix} v_x \\ v_y \\ v_z \end{pmatrix}$ eines Körpers hat den Betrag (die Schnelligkeit):

$$v = |\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$$

### Beispiel: Flugzeug

Ein Flugzeug fliegt mit $\vec{v} = \begin{pmatrix} 200 \\ 150 \\ 10 \end{pmatrix}$ km/h.

Geschwindigkeit: $v = \sqrt{200^2 + 150^2 + 10^2} = \sqrt{62600} \approx 250{,}2$ km/h

### Kraftbetrag

Der Betrag einer Kraft $\vec{F}$ gibt die Stärke der Kraft in Newton an.

## Berechnung des Betrags mit dem Skalarprodukt

Es gilt ein wichtiger Zusammenhang:

$$|\vec{a}|^2 = \vec{a} \cdot \vec{a}$$

Oder: $|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}}$

Diese Formel wird bei komplexeren Berechnungen oft verwendet.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Vektordarstellung]] — Komponenten für die Betragsberechnung
- → [[Einheitsvektoren]] — Vektoren mit Betrag 1
- → [[Skalarprodukt]] — Zusammenhang $|\vec{a}|^2 = \vec{a} \cdot \vec{a}$
- → [[Skalarmultiplikation]] — Auswirkung auf den Betrag: $|k\vec{a}| = |k| \cdot |\vec{a}|$

> [!warning] **Prüfungsrelevant**
> - Betragsformel für zwei- und dreidimensionale Vektoren
> - Abstandsberechnung zwischen zwei Punkten
> - Eigenschaften der Betragsfunktion (insbesondere Homogenität)
> - Dreiecksungleichung und ihre geometrische Bedeutung
> - Zusammenhang mit dem Skalarprodukt: $|\vec{a}|^2 = \vec{a} \cdot \vec{a}$

> [!question] **Typische Prüfungsfragen**
> - Berechne den Betrag von $\vec{a} = \begin{pmatrix} -2 \\ 6 \\ 3 \end{pmatrix}$.
> - Bestimme den Abstand der Punkte $P(3|1|4)$ und $Q(-1|4|0)$.
> - Für welche Werte von $t$ hat der Vektor $\vec{v} = \begin{pmatrix} t \\ 2 \\ 2t \end{pmatrix}$ den Betrag 6?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[Winkel-zwischen-Vektoren]] — Winkel über Skalarprodukt und Beträge
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Abstandsberechnungen in der Geometrie
