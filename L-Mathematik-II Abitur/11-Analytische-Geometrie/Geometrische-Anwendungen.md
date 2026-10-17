---
author: Andreas Hümmer
title: Geometrische Anwendungen
tags:
  - content
  - mathe
  - analytische-geometrie
  - spiegelung
  - projektion
  - anwendungen
created: 2026-10-17
modified: 2026-10-17
---

# Geometrische Anwendungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Spiegelungen von Punkten an Ebenen und Geraden durchführen können
> - Projektionen auf Ebenen und Geraden berechnen
> - Komplexe Anwendungsaufgaben der analytischen Geometrie lösen
> - Geometrische Problemstellungen systematisch bearbeiten

---

## Überblick

Die Methoden der analytischen Geometrie ermöglichen die Lösung komplexer geometrischer Aufgaben. Besonders wichtig sind Spiegelungen und Projektionen, die in Abituraufgaben häufig vorkommen. Dieses Kapitel fasst die Techniken zusammen und zeigt typische Anwendungen.

## Spiegelung eines Punktes an einer Ebene

### Prinzip

Der Spiegelpunkt $P'$ eines Punktes $P$ an einer Ebene $E$ liegt:
1. Auf der Geraden durch $P$ senkrecht zu $E$
2. Im gleichen Abstand zur Ebene wie $P$, aber auf der anderen Seite

### Rechenschritte

1. Bestimme den **Lotfußpunkt** $F$ von $P$ auf $E$
2. Der Spiegelpunkt ist: $P' = P + 2 \cdot \overrightarrow{PF} = 2F - P$

### Formel

Für $E: ax + by + cz = d$ und $P = (p_1, p_2, p_3)$:

**Schritt 1:** Lotgerade
$$\ell: \vec{x} = \vec{p} + t \cdot \vec{n}$$

**Schritt 2:** Lotfußpunkt durch Einsetzen in $E$
$$a(p_1 + ta) + b(p_2 + tb) + c(p_3 + tc) = d$$
$$t = \frac{d - (ap_1 + bp_2 + cp_3)}{a^2 + b^2 + c^2}$$

**Schritt 3:** Spiegelpunkt
$$P' = P + 2t \cdot \vec{n}$$

### Beispiel

$E: x + 2y + 2z = 9$, $P = (1, 1, 1)$

**Lotparameter:**
$$t = \frac{9 - (1 + 2 + 2)}{1 + 4 + 4} = \frac{4}{9}$$

**Spiegelpunkt:**
$$P' = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + 2 \cdot \frac{4}{9} \cdot \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 + \frac{8}{9} \\ 1 + \frac{16}{9} \\ 1 + \frac{16}{9} \end{pmatrix} = \begin{pmatrix} \frac{17}{9} \\ \frac{25}{9} \\ \frac{25}{9} \end{pmatrix}$$

## Spiegelung eines Punktes an einer Geraden

### Prinzip

Der Spiegelpunkt $P'$ an einer Geraden $g$ liegt:
1. Im gleichen Abstand zu $g$ wie $P$
2. $P$ und $P'$ liegen symmetrisch bezüglich $g$

### Rechenschritte

1. Bestimme den **Lotfußpunkt** $F$ von $P$ auf $g$
2. Berechne $P' = 2F - P$

### Beispiel

$g: \vec{x} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ (x-Achse), $P = (3, 4, 0)$

**Lotfußpunkt:** Da $g$ die x-Achse ist, ist $F = (3, 0, 0)$

**Spiegelpunkt:**
$$P' = 2 \cdot \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} - \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ -4 \\ 0 \end{pmatrix}$$

## Projektion eines Punktes auf eine Ebene

Die **orthogonale Projektion** eines Punktes $P$ auf eine Ebene $E$ ist der Lotfußpunkt $F$.

### Formel

$$F = P - \frac{(\vec{p} - \vec{a}) \cdot \vec{n}}{|\vec{n}|^2} \cdot \vec{n}$$

wobei $\vec{a}$ ein Punkt auf $E$ ist.

Bei Koordinatenform $E: ax + by + cz = d$:

$$F = P - \frac{ap_1 + bp_2 + cp_3 - d}{a^2 + b^2 + c^2} \cdot \begin{pmatrix} a \\ b \\ c \end{pmatrix}$$

## Projektion eines Punktes auf eine Gerade

Die Projektion von $P$ auf die Gerade $g: \vec{x} = \vec{a} + t \cdot \vec{u}$ ist:

$$F = \vec{a} + \frac{(\vec{p} - \vec{a}) \cdot \vec{u}}{|\vec{u}|^2} \cdot \vec{u}$$

## Flächenberechnung mit dem Kreuzprodukt

Die Fläche eines **Parallelogramms**, aufgespannt von $\vec{u}$ und $\vec{v}$:

$$A_{\text{Parallelogramm}} = |\vec{u} \times \vec{v}|$$

Die Fläche eines **Dreiecks** mit den Seiten $\vec{u}$ und $\vec{v}$:

$$A_{\text{Dreieck}} = \frac{1}{2} |\vec{u} \times \vec{v}|$$

### Beispiel: Dreiecksfläche

Dreieck $ABC$ mit $A = (1, 0, 0)$, $B = (0, 2, 0)$, $C = (0, 0, 3)$

$$\overrightarrow{AB} = \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}, \quad \overrightarrow{AC} = \begin{pmatrix} -1 \\ 0 \\ 3 \end{pmatrix}$$

$$\overrightarrow{AB} \times \overrightarrow{AC} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix}$$

$$|\overrightarrow{AB} \times \overrightarrow{AC}| = \sqrt{36 + 9 + 4} = 7$$

$$A_{\triangle ABC} = \frac{7}{2} = 3{,}5$$

## Volumenberechnung mit dem Spatprodukt

Das **Volumen eines Spats** (Parallelepipeds), aufgespannt von $\vec{a}$, $\vec{b}$, $\vec{c}$:

$$V_{\text{Spat}} = |(\vec{a} \times \vec{b}) \cdot \vec{c}|$$

Das Volumen eines **Tetraeders** (Pyramide mit Dreiecksgrundseite):

$$V_{\text{Tetraeder}} = \frac{1}{6} |(\vec{a} \times \vec{b}) \cdot \vec{c}|$$

### Beispiel: Tetraedervolumen

Tetraeder $ABCD$ mit $A = (0, 0, 0)$, $B = (2, 0, 0)$, $C = (0, 3, 0)$, $D = (0, 0, 4)$

$$\vec{a} = \overrightarrow{AB} = \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{b} = \overrightarrow{AC} = \begin{pmatrix} 0 \\ 3 \\ 0 \end{pmatrix}, \quad \vec{c} = \overrightarrow{AD} = \begin{pmatrix} 0 \\ 0 \\ 4 \end{pmatrix}$$

$$\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 0 \\ 6 \end{pmatrix}$$

$$(\vec{a} \times \vec{b}) \cdot \vec{c} = 6 \cdot 4 = 24$$

$$V = \frac{1}{6} \cdot |24| = 4$$

## Komplexe Aufgabentypen im Abitur

### Typ 1: Spiegelung einer Geraden an einer Ebene

1. Bestimme den Durchstoßpunkt $D$ der Geraden durch die Ebene
2. Wähle einen zweiten Punkt $P$ auf der Geraden
3. Spiegle $P$ an der Ebene zu $P'$
4. Die gespiegelte Gerade geht durch $D$ und $P'$

### Typ 2: Kürzester Abstand mit Nebenbedingung

Finde den Punkt auf einer Geraden/Ebene, der einen minimalen Abstand zu einem anderen Objekt hat.

**Methode:** Lotfußpunkt-Berechnung oder Extremwertaufgabe mit Parametern.

### Typ 3: Geometrische Örter

Bestimme die Menge aller Punkte, die eine bestimmte Eigenschaft erfüllen (z.B. gleicher Abstand zu zwei Ebenen).

**Ansatz:** Gleichung für die Eigenschaft aufstellen und nach den Koordinaten umformen.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Punkt-Ebene-Abstand]] — Grundlage für Spiegelungen
- → [[Abstaende-zwischen-Punkten-und-Geraden]] — Lotfußpunkt auf Geraden
- → [[Kreuzprodukt]] — Flächen- und Volumenberechnung
- → [[Schnittpunkte-und-Schnittgeraden]] — Durchstoßpunkte
- → [[Normalenform]] — Ebenendarstellung für Spiegelungen

> [!warning] **Prüfungsrelevant**
> - Spiegelung eines Punktes an einer Ebene
> - Flächenberechnung mit dem Kreuzprodukt
> - Volumenberechnung mit dem Spatprodukt
> - Systematische Bearbeitung komplexer Aufgaben

> [!question] **Typische Prüfungsfragen**
> - Spiegeln Sie den Punkt $P(2|3|4)$ an der Ebene $E: x + y + z = 6$.
> - Berechnen Sie den Flächeninhalt des Dreiecks $ABC$.
> - Eine Gerade $g$ wird an der Ebene $E$ gespiegelt. Bestimmen Sie die Gleichung der gespiegelten Geraden.
> - Bestimmen Sie das Volumen des Tetraeders $ABCD$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019
- ISB Bayern: *Abiturprüfungen Mathematik*, diverse Jahrgänge

> [!tip] **Weiterführende Links**
> - [[Winkelberechnungen]] — Ergänzende Berechnungen
> - [[Anwendungen-im-dreidimensionalen-Raum]] — Physikalische Anwendungen
