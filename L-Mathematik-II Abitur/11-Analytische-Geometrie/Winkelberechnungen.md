---
author: Andreas Hümmer
title: Winkelberechnungen
tags:
  - content
  - mathe
  - analytische-geometrie
  - winkel
  - skalarprodukt
created: 2026-10-17
modified: 2026-10-17
---

# Winkelberechnungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Winkel zwischen zwei Geraden berechnen können
> - Den Winkel zwischen zwei Ebenen (Schnittwinkel) bestimmen
> - Den Winkel zwischen einer Geraden und einer Ebene berechnen
> - Die Rolle des Skalarprodukts bei Winkelberechnungen verstehen

---

## Überblick

Winkelberechnungen in der analytischen Geometrie basieren auf dem Skalarprodukt von Vektoren. Je nach Kombination der geometrischen Objekte — Geraden und Ebenen — werden Richtungsvektoren oder Normalenvektoren verwendet. Die Ergebnisse liegen stets im Bereich $[0°, 90°]$, da der Schnittwinkel als kleinster Winkel definiert ist.

## Grundformel: Winkel zwischen Vektoren

Der Winkel $\varphi$ zwischen zwei Vektoren $\vec{a}$ und $\vec{b}$ berechnet sich über:

$$\cos \varphi = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

Dabei ist:
- $\vec{a} \cdot \vec{b}$ das Skalarprodukt
- $|\vec{a}|$ und $|\vec{b}|$ die Beträge der Vektoren

Der Winkel $\varphi$ liegt im Bereich $[0°, 180°]$.

## Winkel zwischen zwei Geraden

Gegeben seien zwei Geraden mit Richtungsvektoren $\vec{u}$ und $\vec{v}$:

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}$$
$$h: \vec{x} = \vec{b} + s \cdot \vec{v}$$

### Schnittwinkel

Der **Schnittwinkel** $\alpha$ ist der kleinere der beiden Winkel, die die Geraden einschließen:

$$\cos \alpha = \frac{|\vec{u} \cdot \vec{v}|}{|\vec{u}| \cdot |\vec{v}|}$$

Die **Betragsstriche** um das Skalarprodukt stellen sicher, dass $\alpha \in [0°, 90°]$.

### Beispiel

$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$

**Berechnung:**

$$\vec{u} \cdot \vec{v} = 1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 = 1$$

$$|\vec{u}| = \sqrt{1 + 0 + 1} = \sqrt{2}$$

$$|\vec{v}| = \sqrt{1 + 1 + 0} = \sqrt{2}$$

$$\cos \alpha = \frac{|1|}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}$$

$$\alpha = \arccos\left(\frac{1}{2}\right) = 60°$$

### Sonderfälle

- $\alpha = 0°$: Die Geraden sind parallel ($\vec{u} \parallel \vec{v}$)
- $\alpha = 90°$: Die Geraden stehen senkrecht aufeinander ($\vec{u} \cdot \vec{v} = 0$)

## Winkel zwischen zwei Ebenen

Gegeben seien zwei Ebenen mit Normalenvektoren $\vec{n}_1$ und $\vec{n}_2$:

$$E_1: \vec{n}_1 \cdot \vec{x} = d_1$$
$$E_2: \vec{n}_2 \cdot \vec{x} = d_2$$

### Schnittwinkel

Der Winkel zwischen den Ebenen entspricht dem Winkel zwischen ihren Normalenvektoren:

$$\cos \alpha = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1| \cdot |\vec{n}_2|}$$

Auch hier garantieren die Betragsstriche $\alpha \in [0°, 90°]$.

### Beispiel

$$E_1: 2x + y - z = 5 \quad \Rightarrow \quad \vec{n}_1 = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$

$$E_2: x - y + z = 3 \quad \Rightarrow \quad \vec{n}_2 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$$

**Berechnung:**

$$\vec{n}_1 \cdot \vec{n}_2 = 2 \cdot 1 + 1 \cdot (-1) + (-1) \cdot 1 = 2 - 1 - 1 = 0$$

$$\cos \alpha = \frac{|0|}{|\vec{n}_1| \cdot |\vec{n}_2|} = 0$$

$$\alpha = 90°$$

Die Ebenen stehen **senkrecht** aufeinander.

### Sonderfälle

- $\alpha = 0°$: Die Ebenen sind parallel oder identisch ($\vec{n}_1 \parallel \vec{n}_2$)
- $\alpha = 90°$: Die Ebenen stehen senkrecht aufeinander

## Winkel zwischen Gerade und Ebene

Gegeben:

$$g: \vec{x} = \vec{a} + t \cdot \vec{u} \quad \text{(Richtungsvektor } \vec{u}\text{)}$$
$$E: \vec{n} \cdot \vec{x} = d \quad \text{(Normalenvektor } \vec{n}\text{)}$$

### Der Neigungswinkel

Der Winkel $\beta$ zwischen Gerade und Ebene ist der **Komplementwinkel** zum Winkel zwischen $\vec{u}$ und $\vec{n}$:

$$\sin \beta = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}| \cdot |\vec{n}|}$$

Alternativ:

$$\beta = 90° - \gamma$$

wobei $\gamma$ der Winkel zwischen $\vec{u}$ und $\vec{n}$ ist.

### Beispiel

$$g: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$$

$$E: x + 2y + 2z = 6 \quad \Rightarrow \quad \vec{n} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$

**Berechnung:**

$$\vec{u} \cdot \vec{n} = 1 \cdot 1 + 1 \cdot 2 + 1 \cdot 2 = 5$$

$$|\vec{u}| = \sqrt{1 + 1 + 1} = \sqrt{3}$$

$$|\vec{n}| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$

$$\sin \beta = \frac{|5|}{\sqrt{3} \cdot 3} = \frac{5}{3\sqrt{3}} = \frac{5\sqrt{3}}{9} \approx 0{,}962$$

$$\beta = \arcsin\left(\frac{5\sqrt{3}}{9}\right) \approx 74{,}2°$$

### Sonderfälle

- $\beta = 0°$: Die Gerade liegt in der Ebene oder ist parallel zu ihr ($\vec{u} \perp \vec{n}$)
- $\beta = 90°$: Die Gerade steht senkrecht auf der Ebene ($\vec{u} \parallel \vec{n}$)

## Übersicht: Winkelformeln

| Objekte | Verwendete Vektoren | Formel |
|---------|---------------------|--------|
| Gerade-Gerade | Richtungsvektoren $\vec{u}$, $\vec{v}$ | $\cos \alpha = \frac{|\vec{u} \cdot \vec{v}|}{|\vec{u}||\vec{v}|}$ |
| Ebene-Ebene | Normalenvektoren $\vec{n}_1$, $\vec{n}_2$ | $\cos \alpha = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}$ |
| Gerade-Ebene | Richtungsvektor $\vec{u}$, Normalenvektor $\vec{n}$ | $\sin \beta = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}||\vec{n}|}$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Skalarprodukt]] — Grundlage aller Winkelberechnungen
- → [[Geraden-in-Parameterform]] — Richtungsvektoren von Geraden
- → [[Normalenform]] — Normalenvektoren von Ebenen
- → [[Orthogonalitaet]] — Sonderfall des rechten Winkels
- → [[Winkel-zwischen-Vektoren]] — Allgemeine Vektorwinkel

> [!warning] **Prüfungsrelevant**
> - Die drei Winkelformeln und ihre korrekte Anwendung
> - Unterscheidung: wann Cosinus, wann Sinus
> - Betragsstriche für den kleineren Winkel ($\leq 90°$)
> - Erkennen von Orthogonalität (Skalarprodukt $= 0$)

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie den Schnittwinkel der Geraden $g$ und $h$.
> - Unter welchem Winkel schneidet die Gerade $g$ die Ebene $E$?
> - Zeigen Sie, dass die Ebenen $E_1$ und $E_2$ senkrecht aufeinander stehen.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Abstaende-zwischen-Punkten-und-Geraden]] — Geometrische Anwendungen
> - [[Geometrische-Anwendungen]] — Komplexe Aufgabenstellungen
