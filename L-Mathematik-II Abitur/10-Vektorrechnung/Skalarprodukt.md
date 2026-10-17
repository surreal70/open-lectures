---
author: Andreas Hümmer
title: Skalarprodukt
tags:
  - content
  - mathe
  - vektorrechnung
  - skalarprodukt
  - inneres-produkt
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Skalarprodukt

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Skalarprodukt zweier Vektoren berechnen können (Koordinatenform)
> - Die geometrische Interpretation des Skalarprodukts verstehen
> - Den Zusammenhang zwischen Skalarprodukt und Winkel kennen
> - Die Rechenregeln des Skalarprodukts anwenden können

---

## Überblick

Das **Skalarprodukt** (auch inneres Produkt oder Punktprodukt genannt) ist eine Verknüpfung zweier Vektoren, deren Ergebnis eine reelle Zahl (ein Skalar) ist – kein Vektor. Es verbindet die algebraische Rechnung mit geometrischen Eigenschaften und ist fundamental für Winkelberechnungen und Orthogonalitätsprüfungen.

## Definition in Koordinatenform

Das Skalarprodukt zweier Vektoren $\vec{a}$ und $\vec{b}$ ist definiert als:

$$\vec{a} \cdot \vec{b} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \cdot \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = a_1 b_1 + a_2 b_2 + a_3 b_3$$

Das Ergebnis ist die Summe der Produkte der entsprechenden Komponenten.

### Alternative Schreibweisen

- $\vec{a} \cdot \vec{b}$ (Punktschreibweise, am häufigsten)
- $\langle \vec{a}, \vec{b} \rangle$ (Klammerschreibweise)
- $\vec{a}^T \vec{b}$ (Matrixschreibweise)

## Beispielrechnungen

### Beispiel 1

$$\vec{a} = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 4 \\ -1 \\ 2 \end{pmatrix}$$

$$\vec{a} \cdot \vec{b} = 2 \cdot 4 + 3 \cdot (-1) + 1 \cdot 2 = 8 - 3 + 2 = 7$$

### Beispiel 2

$$\vec{u} = \begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}, \quad \vec{v} = \begin{pmatrix} 4 \\ 1 \\ 3 \end{pmatrix}$$

$$\vec{u} \cdot \vec{v} = 1 \cdot 4 + 2 \cdot 1 + (-2) \cdot 3 = 4 + 2 - 6 = 0$$

Das Skalarprodukt ist null – die Vektoren sind **orthogonal** (senkrecht zueinander)!

## Geometrische Interpretation

Das Skalarprodukt kann auch über die Beträge und den eingeschlossenen Winkel definiert werden:

$$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos\varphi$$

wobei $\varphi$ der Winkel zwischen den Vektoren ist.

### Interpretation des Ergebnisses

| Skalarprodukt | Winkel $\varphi$ | Beziehung |
|---------------|------------------|-----------|
| $\vec{a} \cdot \vec{b} > 0$ | $0° \leq \varphi < 90°$ | spitzer Winkel |
| $\vec{a} \cdot \vec{b} = 0$ | $\varphi = 90°$ | orthogonal |
| $\vec{a} \cdot \vec{b} < 0$ | $90° < \varphi \leq 180°$ | stumpfer Winkel |

### Projektion

Das Skalarprodukt steht in engem Zusammenhang mit der **Projektion** eines Vektors auf einen anderen:

$$\text{proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|^2} \cdot \vec{b}$$

Die Länge der Projektion ist:

$$|\text{proj}_{\vec{b}} \vec{a}| = \frac{|\vec{a} \cdot \vec{b}|}{|\vec{b}|}$$

## Rechenregeln

Das Skalarprodukt erfüllt folgende Gesetze:

| Regel | Formel |
|-------|--------|
| **Kommutativgesetz** | $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$ |
| **Distributivgesetz** | $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$ |
| **Homogenität** | $(r \cdot \vec{a}) \cdot \vec{b} = r \cdot (\vec{a} \cdot \vec{b}) = \vec{a} \cdot (r \cdot \vec{b})$ |
| **Positiv-Definitheit** | $\vec{a} \cdot \vec{a} \geq 0$, mit $\vec{a} \cdot \vec{a} = 0 \Leftrightarrow \vec{a} = \vec{0}$ |

### Wichtige Spezialfälle

- $\vec{a} \cdot \vec{a} = |\vec{a}|^2$ (Quadrat des Betrags)
- $\vec{a} \cdot \vec{0} = 0$
- $\vec{e}_i \cdot \vec{e}_j = \delta_{ij}$ (Kronecker-Delta: 1 wenn $i=j$, sonst 0)

## Zusammenhang mit dem Betrag

Eine wichtige Formel verbindet das Skalarprodukt mit dem Betrag:

$$|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}}$$

### Beweis der Betragsformel

$$\vec{a} \cdot \vec{a} = a_1^2 + a_2^2 + a_3^2 = |\vec{a}|^2$$

## Anwendung: Arbeit in der Physik

Die **Arbeit** $W$, die eine Kraft $\vec{F}$ entlang eines Weges $\vec{s}$ verrichtet, ist:

$$W = \vec{F} \cdot \vec{s} = |\vec{F}| \cdot |\vec{s}| \cdot \cos\varphi$$

### Beispiel

Eine Kraft $\vec{F} = \begin{pmatrix} 50 \\ 30 \\ 0 \end{pmatrix}$ N wirkt auf einen Körper, der sich um $\vec{s} = \begin{pmatrix} 4 \\ 0 \\ 0 \end{pmatrix}$ m verschiebt.

$$W = \vec{F} \cdot \vec{s} = 50 \cdot 4 + 30 \cdot 0 + 0 \cdot 0 = 200 \text{ J}$$

## Berechnung des Betrags über das Skalarprodukt

Für den Betrag der Summe zweier Vektoren gilt:

$$|\vec{a} + \vec{b}|^2 = (\vec{a} + \vec{b}) \cdot (\vec{a} + \vec{b}) = |\vec{a}|^2 + 2(\vec{a} \cdot \vec{b}) + |\vec{b}|^2$$

Dies ist analog zur binomischen Formel $(a+b)^2 = a^2 + 2ab + b^2$.

### Polarisationsidentität

$$\vec{a} \cdot \vec{b} = \frac{1}{4}\left(|\vec{a} + \vec{b}|^2 - |\vec{a} - \vec{b}|^2\right)$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Betrag-eines-Vektors]] — Betragsberechnung über $|\vec{a}|^2 = \vec{a} \cdot \vec{a}$
- → [[Winkel-zwischen-Vektoren]] — Winkelberechnung mit Skalarprodukt
- → [[Orthogonalitaet]] — Senkrechte Vektoren erkennen
- → [[Einheitsvektoren]] — Skalarprodukt mit Standardbasisvektoren

> [!warning] **Prüfungsrelevant**
> - Berechnung des Skalarprodukts in Koordinatenform
> - Geometrische Formel: $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos\varphi$
> - Zusammenhang $\vec{a} \cdot \vec{a} = |\vec{a}|^2$
> - Orthogonalitätskriterium: $\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0$
> - Rechenregeln (Kommutativ-, Distributivgesetz, Homogenität)

> [!question] **Typische Prüfungsfragen**
> - Berechne das Skalarprodukt von $\vec{a} = \begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 2 \\ 4 \\ -1 \end{pmatrix}$.
> - Für welchen Wert von $t$ stehen die Vektoren $\begin{pmatrix} 1 \\ t \\ 3 \end{pmatrix}$ und $\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$ senkrecht aufeinander?
> - Berechne $|\vec{a}|$ mithilfe des Skalarprodukts für $\vec{a} = \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[Kreuzprodukt]] — Das Vektorprodukt als Alternative
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Anwendungen bei Geraden und Ebenen
