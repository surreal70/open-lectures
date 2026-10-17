---
author: Andreas Hümmer
title: Winkel zwischen Vektoren
tags:
  - content
  - mathe
  - vektorrechnung
  - winkel
  - skalarprodukt
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Winkel zwischen Vektoren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Winkel zwischen zwei Vektoren mit dem Skalarprodukt berechnen können
> - Die Winkelformel sicher anwenden können
> - Spezialfälle (orthogonal, parallel) erkennen können
> - Winkel in Grad und Bogenmaß angeben können

---

## Überblick

Die Berechnung des **Winkels zwischen zwei Vektoren** ist eine der wichtigsten Anwendungen des Skalarprodukts. Der Winkel gibt an, wie stark zwei Richtungen im Raum voneinander abweichen, und spielt eine zentrale Rolle in der Geometrie, Physik und Technik.

## Die Winkelformel

Der Winkel $\varphi$ zwischen zwei Vektoren $\vec{a}$ und $\vec{b}$ (mit $\vec{a}, \vec{b} \neq \vec{0}$) berechnet sich durch:

$$\cos\varphi = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

Daraus folgt:

$$\varphi = \arccos\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}\right)$$

Der Winkel liegt immer im Bereich $0° \leq \varphi \leq 180°$ (bzw. $0 \leq \varphi \leq \pi$).

## Herleitung der Formel

Aus der geometrischen Definition des Skalarprodukts:

$$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos\varphi$$

Umstellung nach $\cos\varphi$:

$$\cos\varphi = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

## Berechnungsschema

Um den Winkel zwischen zwei Vektoren zu berechnen:

1. **Skalarprodukt** berechnen: $\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3$
2. **Beträge** berechnen: $|\vec{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$, $|\vec{b}| = \sqrt{b_1^2 + b_2^2 + b_3^2}$
3. **Kosinus** des Winkels bestimmen: $\cos\varphi = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$
4. **Winkel** mit $\arccos$ berechnen: $\varphi = \arccos(\cos\varphi)$

## Beispielrechnungen

### Beispiel 1: Vollständige Berechnung

Berechne den Winkel zwischen $\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 3 \\ 0 \\ 4 \end{pmatrix}$.

**Schritt 1: Skalarprodukt**
$$\vec{a} \cdot \vec{b} = 1 \cdot 3 + 2 \cdot 0 + 2 \cdot 4 = 3 + 0 + 8 = 11$$

**Schritt 2: Beträge**
$$|\vec{a}| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$
$$|\vec{b}| = \sqrt{9 + 0 + 16} = \sqrt{25} = 5$$

**Schritt 3: Kosinus**
$$\cos\varphi = \frac{11}{3 \cdot 5} = \frac{11}{15} \approx 0{,}7333$$

**Schritt 4: Winkel**
$$\varphi = \arccos(0{,}7333) \approx 42{,}8°$$

### Beispiel 2: Orthogonale Vektoren

Berechne den Winkel zwischen $\vec{u} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$ und $\vec{v} = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$.

$$\vec{u} \cdot \vec{v} = -1 + 1 + 0 = 0$$

$$\cos\varphi = \frac{0}{|\vec{u}| \cdot |\vec{v}|} = 0$$

$$\varphi = \arccos(0) = 90°$$

Die Vektoren sind **orthogonal** (senkrecht zueinander).

### Beispiel 3: Parallele Vektoren

Berechne den Winkel zwischen $\vec{p} = \begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}$ und $\vec{q} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.

$$\vec{p} \cdot \vec{q} = 2 + 8 + 18 = 28$$

$$|\vec{p}| = \sqrt{4 + 16 + 36} = \sqrt{56} = 2\sqrt{14}$$

$$|\vec{q}| = \sqrt{1 + 4 + 9} = \sqrt{14}$$

$$\cos\varphi = \frac{28}{2\sqrt{14} \cdot \sqrt{14}} = \frac{28}{28} = 1$$

$$\varphi = \arccos(1) = 0°$$

Die Vektoren sind **parallel** (gleichgerichtet).

## Spezialfälle im Überblick

| Winkel | $\cos\varphi$ | Skalarprodukt | Beziehung |
|--------|---------------|---------------|-----------|
| $\varphi = 0°$ | $1$ | $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}|$ | gleichgerichtet |
| $\varphi = 90°$ | $0$ | $\vec{a} \cdot \vec{b} = 0$ | orthogonal |
| $\varphi = 180°$ | $-1$ | $\vec{a} \cdot \vec{b} = -|\vec{a}| \cdot |\vec{b}|$ | entgegengesetzt |
| $0° < \varphi < 90°$ | $> 0$ | $\vec{a} \cdot \vec{b} > 0$ | spitzer Winkel |
| $90° < \varphi < 180°$ | $< 0$ | $\vec{a} \cdot \vec{b} < 0$ | stumpfer Winkel |

## Winkel mit Koordinatenachsen

Der Winkel $\alpha$ eines Vektors $\vec{a}$ mit der $x$-Achse (bzw. $\vec{e}_1$) ist:

$$\cos\alpha = \frac{\vec{a} \cdot \vec{e}_1}{|\vec{a}| \cdot |\vec{e}_1|} = \frac{a_1}{|\vec{a}|}$$

Analog für die anderen Achsen:

| Achse | Winkel | Formel |
|-------|--------|--------|
| $x$-Achse | $\alpha$ | $\cos\alpha = \frac{a_1}{|\vec{a}|}$ |
| $y$-Achse | $\beta$ | $\cos\beta = \frac{a_2}{|\vec{a}|}$ |
| $z$-Achse | $\gamma$ | $\cos\gamma = \frac{a_3}{|\vec{a}|}$ |

Diese Werte heißen **Richtungskosinus**, und es gilt:

$$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$$

### Beispiel: Richtungswinkel

Für $\vec{a} = \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix}$ mit $|\vec{a}| = 5$:

- $\cos\alpha = \frac{3}{5} = 0{,}6$ → $\alpha \approx 53{,}1°$
- $\cos\beta = \frac{4}{5} = 0{,}8$ → $\beta \approx 36{,}9°$
- $\cos\gamma = \frac{0}{5} = 0$ → $\gamma = 90°$

## Praktische Hinweise

### Taschenrechner-Einstellung

- Für Winkel in **Grad**: Taschenrechner auf DEG stellen
- Für Winkel im **Bogenmaß**: Taschenrechner auf RAD stellen

### Umrechnung

$$\text{Grad} = \text{Bogenmaß} \cdot \frac{180°}{\pi}$$

$$\text{Bogenmaß} = \text{Grad} \cdot \frac{\pi}{180°}$$

### Häufige Werte

| $\cos\varphi$ | $\varphi$ (Grad) | $\varphi$ (Bogenmaß) |
|---------------|------------------|----------------------|
| $1$ | $0°$ | $0$ |
| $\frac{\sqrt{3}}{2}$ | $30°$ | $\frac{\pi}{6}$ |
| $\frac{\sqrt{2}}{2}$ | $45°$ | $\frac{\pi}{4}$ |
| $\frac{1}{2}$ | $60°$ | $\frac{\pi}{3}$ |
| $0$ | $90°$ | $\frac{\pi}{2}$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Skalarprodukt]] — Grundlage der Winkelberechnung
- → [[Orthogonalitaet]] — Spezialfall $\varphi = 90°$
- → [[Einheitsvektoren]] — Richtungskosinus als Komponenten

> [!warning] **Prüfungsrelevant**
> - Winkelformel: $\cos\varphi = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$
> - Vollständiges Berechnungsschema (Skalarprodukt, Beträge, Kosinus, Winkel)
> - Erkennen von Spezialfällen (orthogonal, parallel)
> - Richtungswinkel zu den Koordinatenachsen

> [!question] **Typische Prüfungsfragen**
> - Berechne den Winkel zwischen $\vec{a} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}$.
> - Unter welchem Winkel schneidet der Vektor $\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ die $x$-Achse?
> - Bestimme alle Vektoren $\vec{v} = \begin{pmatrix} t \\ 1 \\ 2 \end{pmatrix}$, die mit $\begin{pmatrix} 2 \\ -4 \\ 1 \end{pmatrix}$ einen Winkel von $90°$ einschließen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[09-Trigonometrie-und-periodische-Funktionen-Index|Trigonometrie]] — Arkuskosinus und Winkelbeziehungen
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Schnittwinkel von Geraden und Ebenen
