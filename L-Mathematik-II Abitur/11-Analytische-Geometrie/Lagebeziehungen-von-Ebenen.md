---
author: Andreas Hümmer
title: Lagebeziehungen von Ebenen
tags:
  - content
  - mathe
  - analytische-geometrie
  - ebenen
  - lagebeziehungen
created: 2026-10-17
modified: 2026-10-17
---

# Lagebeziehungen von Ebenen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die drei möglichen Lagebeziehungen zweier Ebenen unterscheiden können
> - Die Lagebeziehung aus den Normalenvektoren und Gleichungen ableiten
> - Lagebeziehungen zwischen Geraden und Ebenen untersuchen können
> - Schnittgeraden paralleler Ebenen und Durchstoßpunkte berechnen

---

## Überblick

Zwei Ebenen im Raum können identisch, parallel oder schneidend sein — anders als bei Geraden gibt es keine "windschiefe" Variante. Die Lagebeziehung lässt sich elegant über die Normalenvektoren und die Ebenengleichungen bestimmen. Darüber hinaus werden hier auch die Lagebeziehungen zwischen Geraden und Ebenen behandelt.

## Lagebeziehungen zweier Ebenen

### Die drei Fälle

| Lagebeziehung | Beschreibung | Schnittmenge |
|---------------|--------------|--------------|
| **Identisch** | dieselbe Ebene | die gesamte Ebene |
| **Parallel** | gleiche Richtung, verschiedene Lage | leer |
| **Schneidend** | gemeinsame Schnittgerade | eine Gerade |

### Bestimmung über Normalenvektoren

Gegeben seien zwei Ebenen in Koordinatenform:

$$E_1: a_1 x + b_1 y + c_1 z = d_1$$
$$E_2: a_2 x + b_2 y + c_2 z = d_2$$

mit Normalenvektoren $\vec{n}_1 = \begin{pmatrix} a_1 \\ b_1 \\ c_1 \end{pmatrix}$ und $\vec{n}_2 = \begin{pmatrix} a_2 \\ b_2 \\ c_2 \end{pmatrix}$.

**Fall 1: Normalenvektoren nicht kollinear**

$$\vec{n}_1 \neq \lambda \cdot \vec{n}_2 \text{ für alle } \lambda$$

Die Ebenen **schneiden sich** in einer Geraden.

**Fall 2: Normalenvektoren kollinear**

$$\vec{n}_1 = \lambda \cdot \vec{n}_2$$

Dann gibt es zwei Unterfälle:
- Wenn auch $d_1 = \lambda \cdot d_2$: Die Ebenen sind **identisch**
- Wenn $d_1 \neq \lambda \cdot d_2$: Die Ebenen sind **parallel** (echt parallel)

### Beispiel: Lagebeziehung bestimmen

**Beispiel 1:**
$$E_1: 2x + 3y - z = 5$$
$$E_2: 4x + 6y - 2z = 10$$

$\vec{n}_2 = \begin{pmatrix} 4 \\ 6 \\ -2 \end{pmatrix} = 2 \cdot \begin{pmatrix} 2 \\ 3 \\ -1 \end{pmatrix} = 2 \cdot \vec{n}_1$ → kollinear

$d_2 = 10 = 2 \cdot 5 = 2 \cdot d_1$ ✓

Die Ebenen sind **identisch**.

**Beispiel 2:**
$$E_1: x + 2y + 3z = 4$$
$$E_2: 2x + 4y + 6z = 5$$

$\vec{n}_2 = 2 \cdot \vec{n}_1$ → kollinear

$d_2 = 5 \neq 2 \cdot 4 = 8$

Die Ebenen sind **parallel** (nicht identisch).

**Beispiel 3:**
$$E_1: x + y + z = 1$$
$$E_2: x - y + z = 2$$

$\vec{n}_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$, $\vec{n}_2 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$ → nicht kollinear

Die Ebenen **schneiden sich** in einer Geraden.

## Lagebeziehungen Gerade-Ebene

Eine Gerade $g: \vec{x} = \vec{a} + t \cdot \vec{u}$ und eine Ebene $E: \vec{n} \cdot \vec{x} = d$ können:

| Lagebeziehung | Bedingung | Beschreibung |
|---------------|-----------|--------------|
| **In E liegend** | $\vec{n} \cdot \vec{u} = 0$ und Punkt von $g$ in $E$ | $g \subset E$ |
| **Parallel zu E** | $\vec{n} \cdot \vec{u} = 0$ und Punkt von $g$ nicht in $E$ | kein Schnittpunkt |
| **Schneidend** | $\vec{n} \cdot \vec{u} \neq 0$ | genau ein Schnittpunkt |

### Schnittwinkel und Orthogonalität

- $g$ steht **senkrecht** auf $E$, wenn $\vec{u} \parallel \vec{n}$ (Richtungsvektor parallel zum Normalenvektor)
- $g$ liegt in $E$ oder ist parallel zu $E$, wenn $\vec{u} \perp \vec{n}$

### Durchstoßpunkt berechnen

Bei $\vec{n} \cdot \vec{u} \neq 0$ gibt es einen Durchstoßpunkt (Schnittpunkt).

**Methode:** Setze die Parameterdarstellung der Geraden in die Ebenengleichung ein und löse nach $t$.

### Beispiel: Durchstoßpunkt

$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$$

$$E: 2x + y - z = 4$$

**Einsetzen:**
$$2(1 + t) + (2 + t) - (3 - t) = 4$$
$$2 + 2t + 2 + t - 3 + t = 4$$
$$1 + 4t = 4$$
$$t = \frac{3}{4}$$

**Durchstoßpunkt:**
$$D = \begin{pmatrix} 1 + \frac{3}{4} \\ 2 + \frac{3}{4} \\ 3 - \frac{3}{4} \end{pmatrix} = \begin{pmatrix} \frac{7}{4} \\ \frac{11}{4} \\ \frac{9}{4} \end{pmatrix}$$

## Schnittgerade zweier Ebenen

Wenn zwei Ebenen sich schneiden, ist die Schnittmenge eine Gerade. Zur Berechnung:

### Methode 1: Gleichungssystem lösen

Löse das System aus beiden Ebenengleichungen. Da zwei Gleichungen mit drei Unbekannten vorliegen, erhält man eine einparametrige Lösungsmenge (die Gerade).

### Methode 2: Richtungsvektor über Kreuzprodukt

Der Richtungsvektor der Schnittgeraden steht senkrecht auf beiden Normalenvektoren:

$$\vec{u} = \vec{n}_1 \times \vec{n}_2$$

Dann bestimmt man einen Punkt auf der Schnittgeraden durch Einsetzen (z.B. $z = 0$ setzen, falls möglich).

### Beispiel: Schnittgerade

$$E_1: x + y + z = 3$$
$$E_2: x - y + 2z = 1$$

**Richtungsvektor:**
$$\vec{u} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \times \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \cdot 2 - 1 \cdot (-1) \\ 1 \cdot 1 - 1 \cdot 2 \\ 1 \cdot (-1) - 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 3 \\ -1 \\ -2 \end{pmatrix}$$

**Punkt auf der Schnittgeraden** (setze $z = 0$):

$x + y = 3$ und $x - y = 1$

Addition: $2x = 4 \Rightarrow x = 2$

Subtraktion: $2y = 2 \Rightarrow y = 1$

Punkt: $P = (2, 1, 0)$

**Schnittgerade:**
$$g: \vec{x} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 3 \\ -1 \\ -2 \end{pmatrix}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ebenen-in-Koordinatenform]] — Normalenvektor aus Koordinatenform
- → [[Normalenform]] — Alternative Ebenendarstellung
- → [[Kreuzprodukt]] — Richtungsvektor der Schnittgeraden
- → [[Lagebeziehungen-von-Geraden]] — Analoge Untersuchung für Geraden
- → [[Schnittpunkte-und-Schnittgeraden]] — Ausführliche Berechnungen

> [!warning] **Prüfungsrelevant**
> - Lagebeziehung aus Normalenvektoren bestimmen
> - Unterscheidung identisch vs. parallel bei kollinearen Normalenvektoren
> - Durchstoßpunkt Gerade-Ebene berechnen
> - Schnittgerade zweier Ebenen bestimmen

> [!question] **Typische Prüfungsfragen**
> - Untersuchen Sie die Lagebeziehung der Ebenen $E_1: 2x - y + 3z = 6$ und $E_2: 4x - 2y + 6z = 12$.
> - Bestimmen Sie den Durchstoßpunkt der Geraden $g$ mit der Ebene $E$.
> - Berechnen Sie die Schnittgerade der Ebenen $E_1$ und $E_2$ in Parameterform.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Winkelberechnungen]] — Schnittwinkel zweier Ebenen
> - [[Punkt-Ebene-Abstand]] — Abstand paralleler Ebenen
