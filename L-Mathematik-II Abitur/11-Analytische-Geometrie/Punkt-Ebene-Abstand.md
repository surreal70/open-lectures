---
author: Andreas Hümmer
title: Punkt-Ebene-Abstand
tags:
  - content
  - mathe
  - analytische-geometrie
  - abstaende
  - hessesche-normalform
created: 2026-10-17
modified: 2026-10-17
---

# Punkt-Ebene-Abstand

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen
> - Die Abstandsformel herleiten und interpretieren können
> - Den Abstand zweier paralleler Ebenen bestimmen
> - Die Bedeutung des Vorzeichens bei der Abstandsberechnung verstehen

---

## Überblick

Die Berechnung des Abstands eines Punktes von einer Ebene gehört zu den häufigsten Aufgaben in der analytischen Geometrie. Die eleganteste Methode nutzt die Hessesche Normalform, bei der der Abstand durch einfaches Einsetzen der Punktkoordinaten berechnet werden kann.

## Die Abstandsformel

### Herleitung

Gegeben sei eine Ebene in Koordinatenform:

$$E: ax + by + cz = d$$

mit Normalenvektor $\vec{n} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$

Der Abstand eines Punktes $P = (p_1, p_2, p_3)$ von der Ebene beträgt:

$$d(P, E) = \frac{|ap_1 + bp_2 + cp_3 - d|}{\sqrt{a^2 + b^2 + c^2}}$$

### Interpretation

- Der **Zähler** ist der Betrag der "Abweichung": Setzt man $P$ in die linke Seite der Ebenengleichung ein, erhält man $ap_1 + bp_2 + cp_3$. Die Differenz zu $d$ gibt an, wie weit $P$ von der Ebene entfernt ist (skaliert mit $|\vec{n}|$).
- Der **Nenner** ist der Betrag des Normalenvektors und normiert das Ergebnis auf den tatsächlichen Abstand.

### Abstandsformel mit Hessescher Normalform

Die Hessesche Normalform verwendet den Einheitsnormalenvektor $\vec{n}_0$:

$$E: \vec{n}_0 \cdot \vec{x} = d_0$$

Dann ist der Abstand direkt:

$$d(P, E) = |\vec{n}_0 \cdot \vec{p} - d_0|$$

## Beispiele

### Beispiel 1: Standardberechnung

Gegeben: $E: 2x - 2y + z = 6$ und $P = (3, 1, 4)$

**Einsetzen in die Abstandsformel:**

$$d(P, E) = \frac{|2 \cdot 3 + (-2) \cdot 1 + 1 \cdot 4 - 6|}{\sqrt{4 + 4 + 1}}$$

$$= \frac{|6 - 2 + 4 - 6|}{\sqrt{9}} = \frac{|2|}{3} = \frac{2}{3}$$

### Beispiel 2: Mit Hessescher Normalform

Dieselbe Ebene $E: 2x - 2y + z = 6$

**Schritt 1:** Betrag des Normalenvektors
$$|\vec{n}| = \sqrt{4 + 4 + 1} = 3$$

**Schritt 2:** Hessesche Normalform
$$E: \frac{2x - 2y + z}{3} = 2$$

**Schritt 3:** Abstand von $P = (3, 1, 4)$
$$d(P, E) = \left| \frac{2 \cdot 3 - 2 \cdot 1 + 4}{3} - 2 \right| = \left| \frac{8}{3} - 2 \right| = \left| \frac{2}{3} \right| = \frac{2}{3}$$

### Beispiel 3: Punkt in der Ebene

Für $P = (1, 0, 4)$ und $E: 2x - 2y + z = 6$:

$$d(P, E) = \frac{|2 \cdot 1 - 2 \cdot 0 + 1 \cdot 4 - 6|}{3} = \frac{|2 + 4 - 6|}{3} = \frac{0}{3} = 0$$

$P$ liegt **in** der Ebene.

## Orientierter Abstand

Ohne Betragsstriche liefert die Formel einen **orientierten Abstand**:

$$d_{\text{orient}}(P, E) = \frac{ap_1 + bp_2 + cp_3 - d}{\sqrt{a^2 + b^2 + c^2}}$$

- $d_{\text{orient}} > 0$: $P$ liegt auf der Seite, in die $\vec{n}$ zeigt
- $d_{\text{orient}} < 0$: $P$ liegt auf der gegenüberliegenden Seite
- $d_{\text{orient}} = 0$: $P$ liegt in der Ebene

### Anwendung: Lage von Punkten bestimmen

Man kann prüfen, ob zwei Punkte auf derselben Seite einer Ebene liegen, indem man ihre orientierten Abstände vergleicht:
- Gleiches Vorzeichen: dieselbe Seite
- Verschiedene Vorzeichen: verschiedene Seiten

## Abstand paralleler Ebenen

Zwei parallele Ebenen haben kollineare Normalenvektoren. Der Abstand zwischen ihnen kann berechnet werden, indem man einen beliebigen Punkt der einen Ebene nimmt und seinen Abstand zur anderen berechnet.

### Beispiel

$$E_1: 2x + y - 2z = 3$$
$$E_2: 4x + 2y - 4z = 14 \quad \Leftrightarrow \quad 2x + y - 2z = 7$$

Die Ebenen sind parallel (gleicher Normalenvektor).

**Punkt auf $E_1$** (z.B. $x = 0$, $y = 3$, $z = 0$): $P = (0, 3, 0)$

**Abstand von $P$ zu $E_2$:**

$$d = \frac{|2 \cdot 0 + 1 \cdot 3 - 2 \cdot 0 - 7|}{\sqrt{4 + 1 + 4}} = \frac{|3 - 7|}{3} = \frac{4}{3}$$

### Schnellformel für parallele Ebenen

Wenn beide Ebenen in der Form $ax + by + cz = d_1$ und $ax + by + cz = d_2$ gegeben sind (gleiche Koeffizienten):

$$d(E_1, E_2) = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}$$

Im Beispiel: $d = \frac{|3 - 7|}{3} = \frac{4}{3}$

## Lotfußpunkt auf der Ebene

Der **Lotfußpunkt** $F$ ist der Punkt auf der Ebene, der $P$ am nächsten liegt.

**Berechnung:** $F$ liegt auf der Geraden durch $P$ mit Richtung $\vec{n}$:

$$\ell: \vec{x} = \vec{p} + t \cdot \vec{n}$$

Setze in die Ebenengleichung ein und löse nach $t$.

### Beispiel

$E: x + 2y + 2z = 9$, $P = (1, 1, 1)$

**Lotgerade:**
$$\ell: \vec{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$

**Einsetzen:**
$$(1 + t) + 2(1 + 2t) + 2(1 + 2t) = 9$$
$$1 + t + 2 + 4t + 2 + 4t = 9$$
$$5 + 9t = 9 \Rightarrow t = \frac{4}{9}$$

**Lotfußpunkt:**
$$F = \begin{pmatrix} 1 + \frac{4}{9} \\ 1 + \frac{8}{9} \\ 1 + \frac{8}{9} \end{pmatrix} = \begin{pmatrix} \frac{13}{9} \\ \frac{17}{9} \\ \frac{17}{9} \end{pmatrix}$$

**Kontrolle:** $d = |t| \cdot |\vec{n}| = \frac{4}{9} \cdot 3 = \frac{4}{3}$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Normalenform]] — Hessesche Normalform der Ebene
- → [[Ebenen-in-Koordinatenform]] — Koordinatenform und Normalenvektor
- → [[Abstaende-zwischen-Punkten-und-Geraden]] — Analoge Abstandsberechnung
- → [[Lagebeziehungen-von-Ebenen]] — Parallele Ebenen erkennen
- → [[Geometrische-Anwendungen]] — Praktische Anwendungen

> [!warning] **Prüfungsrelevant**
> - Die Abstandsformel $d = \frac{|ap_1 + bp_2 + cp_3 - d|}{|\vec{n}|}$
> - Hessesche Normalform für direkte Abstandsberechnung
> - Abstand paralleler Ebenen über Punktabstand
> - Lotfußpunkt auf einer Ebene bestimmen

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie den Abstand des Punktes $P(2|3|1)$ von der Ebene $E: 3x - 4z = 10$.
> - Bestimmen Sie den Abstand der parallelen Ebenen $E_1: x + y + z = 5$ und $E_2: x + y + z = 8$.
> - Ermitteln Sie den Lotfußpunkt des Punktes $P$ auf der Ebene $E$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Geometrische-Anwendungen]] — Spiegelungen an Ebenen
> - [[Winkelberechnungen]] — Winkel bei Abstandsproblemen
