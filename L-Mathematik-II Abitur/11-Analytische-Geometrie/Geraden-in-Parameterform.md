---
author: Andreas Hümmer
title: Geraden in Parameterform
tags:
  - content
  - mathe
  - analytische-geometrie
  - geraden
  - parameterform
created: 2026-10-17
modified: 2026-10-17
---

# Geraden in Parameterform

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Geraden im Raum durch Parametergleichungen beschreiben können
> - Den Stützvektor und Richtungsvektor einer Geraden identifizieren
> - Prüfen können, ob ein Punkt auf einer Geraden liegt
> - Geraden aus zwei Punkten oder einem Punkt und einer Richtung aufstellen

---

## Überblick

Geraden im dreidimensionalen Raum lassen sich nicht wie in der Ebene durch eine einzige Gleichung $y = mx + b$ beschreiben. Stattdessen verwendet man die **Parameterform**, bei der jeder Punkt der Geraden durch einen Parameter $t$ erzeugt wird. Diese Darstellung ist flexibel und eignet sich hervorragend für Berechnungen in der analytischen Geometrie.

## Die Parametergleichung einer Geraden

Eine Gerade $g$ im Raum wird durch einen **Stützvektor** $\vec{a}$ (Ortsvektor eines Punktes auf der Geraden) und einen **Richtungsvektor** $\vec{u}$ beschrieben:

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}, \quad t \in \mathbb{R}$$

Dabei ist:
- $\vec{a}$ der **Stützvektor** (Aufpunkt der Geraden)
- $\vec{u}$ der **Richtungsvektor** (gibt die Richtung der Geraden an)
- $t$ der **Parameter** (durchläuft alle reellen Zahlen)

### Komponentenweise Darstellung

In Koordinatenschreibweise:

$$g: \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} + t \cdot \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}$$

Dies entspricht dem Gleichungssystem:

$$x = a_1 + t \cdot u_1$$
$$y = a_2 + t \cdot u_2$$
$$z = a_3 + t \cdot u_3$$

## Aufstellen einer Geradengleichung

### Aus zwei Punkten

Sind zwei verschiedene Punkte $A$ und $B$ gegeben, so verläuft durch sie genau eine Gerade:

$$g: \vec{x} = \vec{OA} + t \cdot \overrightarrow{AB}$$

Der Richtungsvektor ist der Verbindungsvektor:

$$\overrightarrow{AB} = \vec{OB} - \vec{OA} = \begin{pmatrix} b_1 - a_1 \\ b_2 - a_2 \\ b_3 - a_3 \end{pmatrix}$$

### Beispiel: Gerade durch zwei Punkte

Gegeben: $A = (1, 2, 3)$ und $B = (4, 6, 1)$

**Richtungsvektor:**
$$\overrightarrow{AB} = \begin{pmatrix} 4-1 \\ 6-2 \\ 1-3 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -2 \end{pmatrix}$$

**Geradengleichung:**
$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 3 \\ 4 \\ -2 \end{pmatrix}, \quad t \in \mathbb{R}$$

### Aus Punkt und Richtung

Ist ein Punkt $P$ und eine Richtung $\vec{u}$ gegeben (etwa parallel zu einer anderen Geraden oder orthogonal zu einer Ebene), setzt man direkt:

$$g: \vec{x} = \vec{OP} + t \cdot \vec{u}$$

## Punktprobe

Um zu prüfen, ob ein Punkt $P = (p_1, p_2, p_3)$ auf der Geraden $g: \vec{x} = \vec{a} + t \cdot \vec{u}$ liegt, setzt man die Koordinaten ein und prüft, ob ein gemeinsamer Parameterwert $t$ existiert.

### Beispiel: Punktprobe

Gegeben: $g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$

Liegt $P = (5, 4, 1)$ auf $g$?

Aus den drei Gleichungen:
- $5 = 1 + 2t \Rightarrow t = 2$
- $4 = 2 + 1t \Rightarrow t = 2$
- $1 = 3 - 1t \Rightarrow t = 2$

Da alle drei Gleichungen denselben Wert $t = 2$ liefern, liegt $P$ auf $g$. ✓

Liegt $Q = (3, 3, 3)$ auf $g$?

- $3 = 1 + 2t \Rightarrow t = 1$
- $3 = 2 + 1t \Rightarrow t = 1$
- $3 = 3 - 1t \Rightarrow t = 0$

Die Werte für $t$ stimmen nicht überein. $Q$ liegt **nicht** auf $g$. ✗

## Besondere Punkte einer Geraden

### Aufpunkt

Für $t = 0$ erhält man den Aufpunkt $A$ mit Ortsvektor $\vec{a}$.

### Spurpunkte

Die **Spurpunkte** sind die Schnittpunkte der Geraden mit den Koordinatenebenen:

| Spurpunkt | Bedingung | Berechnung |
|-----------|-----------|------------|
| $S_{xy}$ | $z = 0$ | $a_3 + t \cdot u_3 = 0$ lösen |
| $S_{xz}$ | $y = 0$ | $a_2 + t \cdot u_2 = 0$ lösen |
| $S_{yz}$ | $x = 0$ | $a_1 + t \cdot u_1 = 0$ lösen |

### Beispiel: Spurpunkte bestimmen

Für $g: \vec{x} = \begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$

**Spurpunkt $S_{xy}$ (auf der xy-Ebene, $z = 0$):**
$$6 + 3t = 0 \Rightarrow t = -2$$
$$S_{xy} = (2 + 1 \cdot (-2), \, 4 + (-2) \cdot (-2), \, 0) = (0, 8, 0)$$

## Äquivalente Darstellungen

Dieselbe Gerade kann durch verschiedene Parametergleichungen dargestellt werden:

1. **Anderer Aufpunkt:** Jeder Punkt auf der Geraden kann als Stützvektor dienen
2. **Skalierter Richtungsvektor:** $\vec{u}$ kann mit jedem $\lambda \neq 0$ multipliziert werden
3. **Umgekehrte Richtung:** $-\vec{u}$ beschreibt dieselbe Gerade

### Beispiel

Die folgenden Gleichungen beschreiben dieselbe Gerade:

$$g_1: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$

$$g_2: \vec{x} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} + s \cdot \begin{pmatrix} 4 \\ 2 \\ -2 \end{pmatrix}$$

Denn $(3, 1, 1)$ liegt auf $g_1$ (für $t = 1$) und $(4, 2, -2) = 2 \cdot (2, 1, -1)$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Vektorbegriff und Vektorrechnung
- → [[Ortsvektoren]] — Stützvektor als Ortsvektor
- → [[Koordinatensysteme-im-Raum]] — Darstellung im kartesischen System
- → [[Lagebeziehungen-von-Geraden]] — Schnitt, parallel, windschief
- → [[Ebenen-in-Parameterform]] — Verallgemeinerung auf Ebenen

> [!warning] **Prüfungsrelevant**
> - Geradengleichung aus zwei Punkten aufstellen
> - Punktprobe durch Einsetzen und Vergleich der Parameterwerte
> - Berechnung von Spurpunkten
> - Erkennen äquivalenter Darstellungen derselben Geraden

> [!question] **Typische Prüfungsfragen**
> - Stellen Sie die Gleichung der Geraden durch $A(1|2|3)$ und $B(4|5|6)$ in Parameterform auf.
> - Prüfen Sie, ob der Punkt $P(7|8|9)$ auf der Geraden $g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix}$ liegt.
> - Bestimmen Sie den Spurpunkt der Geraden $g$ mit der $xy$-Ebene.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Abstaende-zwischen-Punkten-und-Geraden]] — Abstandsberechnungen
> - [[Schnittpunkte-und-Schnittgeraden]] — Schnittpunktbestimmung
