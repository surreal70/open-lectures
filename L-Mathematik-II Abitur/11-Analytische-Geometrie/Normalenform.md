---
author: Andreas Hümmer
title: Normalenform
tags:
  - content
  - mathe
  - analytische-geometrie
  - ebenen
  - normalenform
  - hessesche-normalform
created: 2026-10-17
modified: 2026-10-17
---

# Normalenform

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Normalenform einer Ebene verstehen und aufstellen können
> - Die Hessesche Normalform und ihre Bedeutung kennen
> - Den Normalenvektor zur Charakterisierung von Ebenen nutzen
> - Die Beziehung zwischen den verschiedenen Ebenenformen beherrschen

---

## Überblick

Die Normalenform beschreibt eine Ebene durch einen Punkt auf der Ebene und einen Vektor, der senkrecht auf ihr steht — den Normalenvektor. Die spezielle Variante der Hesseschen Normalform ermöglicht direkte Abstandsberechnungen und ist ein zentrales Werkzeug der analytischen Geometrie.

## Die Normalenform

### Vektorielle Normalenform

Eine Ebene $E$ wird durch einen Aufpunkt $A$ und einen Normalenvektor $\vec{n}$ beschrieben:

$$E: \vec{n} \cdot (\vec{x} - \vec{a}) = 0$$

oder ausgeschrieben:

$$E: \vec{n} \cdot \vec{x} = \vec{n} \cdot \vec{a}$$

**Interpretation:** Ein Punkt $X$ liegt genau dann in der Ebene, wenn der Vektor $\overrightarrow{AX} = \vec{x} - \vec{a}$ senkrecht auf $\vec{n}$ steht.

### Koordinatenschreibweise

Mit $\vec{n} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$ und Aufpunkt $A = (a_1, a_2, a_3)$:

$$E: a(x - a_1) + b(y - a_2) + c(z - a_3) = 0$$

Dies lässt sich zur Koordinatenform umformen:

$$E: ax + by + cz = aa_1 + ba_2 + ca_3 = d$$

### Beispiel: Normalenform aufstellen

Gegeben: Punkt $A = (2, 1, 3)$ und Normalenvektor $\vec{n} = \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix}$

**Normalenform:**
$$E: 1 \cdot (x - 2) + (-2) \cdot (y - 1) + 2 \cdot (z - 3) = 0$$

**Ausmultipliziert:**
$$E: x - 2y + 2z = 2 - 2 + 6 = 6$$

$$E: x - 2y + 2z = 6$$

## Die Hessesche Normalform

Die **Hessesche Normalform** (HNF) verwendet einen **Einheitsnormalenvektor** $\vec{n}_0$ mit $|\vec{n}_0| = 1$:

$$E: \vec{n}_0 \cdot \vec{x} = d_0$$

oder:

$$E: \frac{ax + by + cz}{\sqrt{a^2 + b^2 + c^2}} = d_0$$

wobei $d_0 = \frac{d}{\sqrt{a^2 + b^2 + c^2}}$ der **orientierte Abstand** der Ebene vom Ursprung ist.

### Normierung des Normalenvektors

Aus dem Normalenvektor $\vec{n} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$ erhält man den Einheitsnormalenvektor:

$$\vec{n}_0 = \frac{\vec{n}}{|\vec{n}|} = \frac{1}{\sqrt{a^2 + b^2 + c^2}} \begin{pmatrix} a \\ b \\ c \end{pmatrix}$$

### Beispiel: Hessesche Normalform bestimmen

Gegeben: $E: 2x - 2y + z = 6$

**Schritt 1:** Betrag des Normalenvektors
$$|\vec{n}| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$$

**Schritt 2:** Normierung
$$\vec{n}_0 = \frac{1}{3} \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix}$$

**Schritt 3:** Hessesche Normalform
$$E: \frac{2x - 2y + z}{3} = 2$$

oder:

$$E: \frac{2}{3}x - \frac{2}{3}y + \frac{1}{3}z = 2$$

Der Abstand der Ebene vom Ursprung beträgt $d_0 = 2$.

## Abstand eines Punktes von einer Ebene

Die Hessesche Normalform ermöglicht die direkte Berechnung des Abstands eines Punktes $P = (p_1, p_2, p_3)$ von der Ebene:

$$d(P, E) = \left| \frac{ap_1 + bp_2 + cp_3 - d}{\sqrt{a^2 + b^2 + c^2}} \right|$$

Die **Betragsstriche** sind notwendig, da der Ausdruck je nach Lage von $P$ positiv oder negativ sein kann.

### Beispiel: Abstand berechnen

Für $E: 2x - 2y + z = 6$ und $P = (1, 2, 3)$:

$$d(P, E) = \left| \frac{2 \cdot 1 - 2 \cdot 2 + 1 \cdot 3 - 6}{\sqrt{4 + 4 + 1}} \right| = \left| \frac{2 - 4 + 3 - 6}{3} \right| = \left| \frac{-5}{3} \right| = \frac{5}{3}$$

## Normalenvektor aus Parameterform

Gegeben eine Ebene in Parameterform mit Spannvektoren $\vec{u}$ und $\vec{v}$, ist der Normalenvektor:

$$\vec{n} = \vec{u} \times \vec{v}$$

### Rechenbeispiel

Für $\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ und $\vec{v} = \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}$:

$$\vec{n} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \cdot 3 - 0 \cdot 1 \\ 0 \cdot 0 - 1 \cdot 3 \\ 1 \cdot 1 - 2 \cdot 0 \end{pmatrix} = \begin{pmatrix} 6 \\ -3 \\ 1 \end{pmatrix}$$

## Orientierung des Normalenvektors

Der Normalenvektor kann in zwei entgegengesetzte Richtungen zeigen. Die Wahl beeinflusst:

- Das Vorzeichen in der Hesseschen Normalform
- Die Unterscheidung, auf welcher Seite der Ebene sich ein Punkt befindet

**Konvention:** Oft wird $\vec{n}$ so gewählt, dass $d > 0$ (die Ebene liegt auf der vom Ursprung abgewandten Seite).

## Vergleich der Ebenenformen

| Form | Darstellung | Vorteil |
|------|-------------|---------|
| Parameterform | $\vec{x} = \vec{a} + r\vec{u} + s\vec{v}$ | Punkte direkt erzeugen |
| Koordinatenform | $ax + by + cz = d$ | Punktprobe einfach |
| Normalenform | $\vec{n} \cdot (\vec{x} - \vec{a}) = 0$ | Anschaulich, Normalenvektor erkennbar |
| Hessesche NF | $\frac{ax + by + cz}{|\vec{n}|} = d_0$ | Abstandsberechnung |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ebenen-in-Parameterform]] — Ausgangspunkt für Normalenberechnung
- → [[Ebenen-in-Koordinatenform]] — Äquivalente Darstellung
- → [[Kreuzprodukt]] — Berechnung des Normalenvektors
- → [[Skalarprodukt]] — Orthogonalitätsbedingung
- → [[Punkt-Ebene-Abstand]] — Anwendung der Hesseschen Normalform

> [!warning] **Prüfungsrelevant**
> - Normalenvektor aus Koordinatenform ablesen
> - Hessesche Normalform aufstellen und interpretieren
> - Abstand Punkt-Ebene mit der Hesseschen Normalform berechnen
> - Umrechnung zwischen den Ebenenformen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Hessesche Normalform der Ebene $E: 3x + 4z = 10$.
> - Berechnen Sie den Abstand des Punktes $P(1|2|3)$ von der Ebene $E: 2x - y + 2z = 7$.
> - Eine Ebene hat den Normalenvektor $\vec{n} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$ und enthält den Punkt $A(3|0|1)$. Stellen Sie die Gleichung der Ebene in Koordinatenform auf.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Geometrische-Anwendungen]] — Spiegelungen an Ebenen
> - [[Winkelberechnungen]] — Winkel mit Normalenvektoren
