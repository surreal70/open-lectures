---
author: Andreas Hümmer
title: Ebenen in Koordinatenform
tags:
  - content
  - mathe
  - analytische-geometrie
  - ebenen
  - koordinatenform
created: 2026-10-17
modified: 2026-10-17
---

# Ebenen in Koordinatenform

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Ebenen durch eine lineare Gleichung $ax + by + cz = d$ beschreiben können
> - Die Koordinatenform aus der Parameterform herleiten
> - Den Zusammenhang zwischen Koeffizienten und Normalenvektor verstehen
> - Spurpunkte und Achsenabschnitte einer Ebene berechnen können

---

## Überblick

Die Koordinatenform (auch Normalform oder implizite Form genannt) beschreibt eine Ebene durch eine einzige lineare Gleichung in $x$, $y$ und $z$. Diese Darstellung ist besonders geeignet für Abstandsberechnungen und Lageuntersuchungen, da der Normalenvektor direkt ablesbar ist.

## Die Koordinatengleichung einer Ebene

Jede Ebene im Raum lässt sich durch eine lineare Gleichung beschreiben:

$$E: ax + by + cz = d$$

oder äquivalent:

$$E: ax + by + cz - d = 0$$

Dabei ist:
- $(a, b, c)$ der **Normalenvektor** der Ebene (steht senkrecht auf der Ebene)
- $d$ bestimmt die **Lage** der Ebene im Raum (Verschiebung vom Ursprung)

### Wichtig

- Mindestens einer der Koeffizienten $a$, $b$, $c$ muss von Null verschieden sein
- Die Gleichung kann mit jedem $\lambda \neq 0$ multipliziert werden und beschreibt dieselbe Ebene

## Der Normalenvektor

Der Normalenvektor $\vec{n} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$ steht **senkrecht** auf der Ebene, d.h. senkrecht auf jedem Vektor, der in der Ebene liegt.

### Herleitung aus der Parameterform

Gegeben sei eine Ebene in Parameterform:

$$E: \vec{x} = \vec{a} + r \cdot \vec{u} + s \cdot \vec{v}$$

Der Normalenvektor ist das **Kreuzprodukt** der Spannvektoren:

$$\vec{n} = \vec{u} \times \vec{v}$$

### Beispiel: Umrechnung Parameter- zu Koordinatenform

Gegeben: $E: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + r \cdot \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$

**Schritt 1: Normalenvektor berechnen**

$$\vec{n} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \times \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 - 0 \cdot 0 \\ 0 \cdot 1 - 2 \cdot 1 \\ 2 \cdot 0 - 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -2 \\ -1 \end{pmatrix}$$

**Schritt 2: Koordinatenform aufstellen**

$$E: 1 \cdot x + (-2) \cdot y + (-1) \cdot z = d$$

**Schritt 3: $d$ durch Einsetzen des Aufpunkts bestimmen**

$$d = 1 \cdot 1 + (-2) \cdot 2 + (-1) \cdot 3 = 1 - 4 - 3 = -6$$

**Ergebnis:**
$$E: x - 2y - z = -6$$

## Spurpunkte und Achsenabschnitte

Die **Spurpunkte** sind die Schnittpunkte der Ebene mit den Koordinatenachsen.

Für die Ebene $ax + by + cz = d$ mit $a, b, c, d \neq 0$:

| Spurpunkt | Achse | Koordinaten | Berechnung |
|-----------|-------|-------------|------------|
| $S_x$ | x-Achse | $\left(\frac{d}{a}, 0, 0\right)$ | $y = z = 0$ setzen |
| $S_y$ | y-Achse | $\left(0, \frac{d}{b}, 0\right)$ | $x = z = 0$ setzen |
| $S_z$ | z-Achse | $\left(0, 0, \frac{d}{c}\right)$ | $x = y = 0$ setzen |

### Achsenabschnittsform

Wenn alle Spurpunkte existieren, kann die Ebene in **Achsenabschnittsform** geschrieben werden:

$$\frac{x}{x_0} + \frac{y}{y_0} + \frac{z}{z_0} = 1$$

wobei $x_0 = \frac{d}{a}$, $y_0 = \frac{d}{b}$, $z_0 = \frac{d}{c}$ die Achsenabschnitte sind.

### Beispiel: Spurpunkte berechnen

Für $E: 2x + 3y + 6z = 12$:

- $S_x = \left(\frac{12}{2}, 0, 0\right) = (6, 0, 0)$
- $S_y = \left(0, \frac{12}{3}, 0\right) = (0, 4, 0)$
- $S_z = \left(0, 0, \frac{12}{6}\right) = (0, 0, 2)$

Achsenabschnittsform: $\frac{x}{6} + \frac{y}{4} + \frac{z}{2} = 1$

## Spezielle Ebenen

### Ebenen durch den Ursprung

Eine Ebene geht durch den Ursprung genau dann, wenn $d = 0$:

$$E: ax + by + cz = 0$$

### Ebenen parallel zu einer Koordinatenachse

| Bedingung | Beschreibung |
|-----------|--------------|
| $a = 0$ | parallel zur x-Achse |
| $b = 0$ | parallel zur y-Achse |
| $c = 0$ | parallel zur z-Achse |

### Koordinatenebenen

| Ebene | Gleichung |
|-------|-----------|
| $xy$-Ebene | $z = 0$ |
| $xz$-Ebene | $y = 0$ |
| $yz$-Ebene | $x = 0$ |

## Umrechnung von Koordinaten- zu Parameterform

Um aus der Koordinatenform die Parameterform zu erhalten:

1. Löse die Gleichung nach einer Variablen auf (z.B. $z$)
2. Setze die beiden anderen Variablen als Parameter ($x = r$, $y = s$)
3. Bestimme Aufpunkt und Spannvektoren

### Beispiel

Gegeben: $E: 2x + y - z = 4$

**Schritt 1:** Nach $z$ auflösen: $z = 2x + y - 4$

**Schritt 2:** Parameterdarstellung mit $x = r$, $y = s$:
$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} r \\ s \\ 2r + s - 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -4 \end{pmatrix} + r \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + s \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$

## Punktprobe

Ein Punkt $P = (p_1, p_2, p_3)$ liegt in der Ebene $E: ax + by + cz = d$ genau dann, wenn:

$$a \cdot p_1 + b \cdot p_2 + c \cdot p_3 = d$$

Diese Prüfung ist bei der Koordinatenform besonders einfach.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ebenen-in-Parameterform]] — Alternative Darstellung
- → [[Normalenform]] — Variante mit normiertem Normalenvektor
- → [[Kreuzprodukt]] — Berechnung des Normalenvektors
- → [[Punkt-Ebene-Abstand]] — Abstandsformel mit Koordinatenform
- → [[Lagebeziehungen-von-Ebenen]] — Parallelität erkennen

> [!warning] **Prüfungsrelevant**
> - Umrechnung von Parameterform in Koordinatenform
> - Bestimmung des Normalenvektors aus den Koeffizienten
> - Berechnung der Spurpunkte einer Ebene
> - Achsenabschnittsform aufstellen und interpretieren

> [!question] **Typische Prüfungsfragen**
> - Wandeln Sie die Ebene $E: \vec{x} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + r \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} + s \begin{pmatrix} 3 \\ 0 \\ -1 \end{pmatrix}$ in Koordinatenform um.
> - Bestimmen Sie die Spurpunkte der Ebene $E: 3x - 2y + 4z = 12$.
> - Geben Sie die Gleichung einer Ebene an, die durch den Ursprung geht und den Normalenvektor $\vec{n} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ hat.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Schnittpunkte-und-Schnittgeraden]] — Schnitt von Ebenen berechnen
> - [[Winkelberechnungen]] — Winkel zwischen Ebenen
