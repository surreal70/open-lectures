---
author: Andreas Hümmer
title: Abstände zwischen Punkten und Geraden
tags:
  - content
  - mathe
  - analytische-geometrie
  - abstaende
  - lotfusspunkt
created: 2026-10-17
modified: 2026-10-17
---

# Abstände zwischen Punkten und Geraden

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Abstand eines Punktes von einer Geraden berechnen können
> - Das Lotfußpunktverfahren verstehen und anwenden
> - Die Kreuzprodukt-Methode als Alternative beherrschen
> - Den Abstand windschiefer Geraden bestimmen können

---

## Überblick

Die Berechnung von Abständen zwischen Punkten und Geraden ist eine zentrale Aufgabe der analytischen Geometrie. Es gibt mehrere Methoden: das Lotfußpunktverfahren mit dem Skalarprodukt, die elegante Kreuzprodukt-Methode, sowie die Hilfsebenen-Methode für den Abstand windschiefer Geraden.

## Abstand Punkt-Gerade

### Das Problem

Gegeben: Ein Punkt $P$ und eine Gerade $g: \vec{x} = \vec{a} + t \cdot \vec{u}$

Gesucht: Der kürzeste Abstand $d(P, g)$

Der kürzeste Abstand wird entlang des **Lots** von $P$ auf $g$ gemessen. Der Fußpunkt dieses Lots heißt **Lotfußpunkt** $F$.

### Methode 1: Lotfußpunktverfahren

**Idee:** Der Vektor $\overrightarrow{FP}$ steht senkrecht auf dem Richtungsvektor $\vec{u}$.

**Vorgehen:**

1. Setze den Lotfußpunkt an: $F = \vec{a} + t_0 \cdot \vec{u}$ (mit unbekanntem $t_0$)
2. Fordere Orthogonalität: $\overrightarrow{FP} \cdot \vec{u} = 0$
3. Löse nach $t_0$ auf
4. Berechne $F$ und dann $d = |{\overrightarrow{FP}}|$

**Ausführlich:**

$$\overrightarrow{FP} = \vec{OP} - \vec{OF} = \vec{p} - (\vec{a} + t_0 \cdot \vec{u})$$

Orthogonalitätsbedingung:

$$(\vec{p} - \vec{a} - t_0 \cdot \vec{u}) \cdot \vec{u} = 0$$

$$(\vec{p} - \vec{a}) \cdot \vec{u} = t_0 \cdot (\vec{u} \cdot \vec{u})$$

$$t_0 = \frac{(\vec{p} - \vec{a}) \cdot \vec{u}}{|\vec{u}|^2}$$

### Beispiel: Lotfußpunktverfahren

$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}, \quad P = (5, 6, 3)$$

**Schritt 1:** Verbindungsvektor $\vec{p} - \vec{a}$:
$$\vec{p} - \vec{a} = \begin{pmatrix} 5 \\ 6 \\ 3 \end{pmatrix} - \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ 0 \end{pmatrix}$$

**Schritt 2:** $t_0$ berechnen:
$$t_0 = \frac{\begin{pmatrix} 4 \\ 4 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}}{|\begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}|^2} = \frac{8 + 4 + 0}{4 + 1 + 4} = \frac{12}{9} = \frac{4}{3}$$

**Schritt 3:** Lotfußpunkt:
$$F = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \frac{4}{3} \cdot \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 + \frac{8}{3} \\ 2 + \frac{4}{3} \\ 3 + \frac{8}{3} \end{pmatrix} = \begin{pmatrix} \frac{11}{3} \\ \frac{10}{3} \\ \frac{17}{3} \end{pmatrix}$$

**Schritt 4:** Abstand:
$$\overrightarrow{FP} = \begin{pmatrix} 5 \\ 6 \\ 3 \end{pmatrix} - \begin{pmatrix} \frac{11}{3} \\ \frac{10}{3} \\ \frac{17}{3} \end{pmatrix} = \begin{pmatrix} \frac{4}{3} \\ \frac{8}{3} \\ -\frac{8}{3} \end{pmatrix}$$

$$d = |\overrightarrow{FP}| = \sqrt{\frac{16}{9} + \frac{64}{9} + \frac{64}{9}} = \sqrt{\frac{144}{9}} = \frac{12}{3} = 4$$

### Methode 2: Kreuzprodukt-Formel

Eine direkte Formel ohne Berechnung des Lotfußpunkts:

$$d(P, g) = \frac{|(\vec{p} - \vec{a}) \times \vec{u}|}{|\vec{u}|}$$

**Beispiel mit denselben Daten:**

$$(\vec{p} - \vec{a}) \times \vec{u} = \begin{pmatrix} 4 \\ 4 \\ 0 \end{pmatrix} \times \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \cdot 2 - 0 \cdot 1 \\ 0 \cdot 2 - 4 \cdot 2 \\ 4 \cdot 1 - 4 \cdot 2 \end{pmatrix} = \begin{pmatrix} 8 \\ -8 \\ -4 \end{pmatrix}$$

$$|(\vec{p} - \vec{a}) \times \vec{u}| = \sqrt{64 + 64 + 16} = \sqrt{144} = 12$$

$$d = \frac{12}{|\vec{u}|} = \frac{12}{\sqrt{9}} = \frac{12}{3} = 4$$ ✓

## Abstand windschiefer Geraden

### Das Problem

Gegeben: Zwei windschiefe Geraden $g$ und $h$

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}$$
$$h: \vec{x} = \vec{b} + s \cdot \vec{v}$$

Gesucht: Der kürzeste Abstand $d(g, h)$

### Hilfsebenen-Methode

**Idee:** Konstruiere eine Ebene $E$, die $g$ enthält und parallel zu $h$ ist. Der Abstand $d(g, h)$ entspricht dem Abstand eines beliebigen Punktes von $h$ zur Ebene $E$.

**Vorgehen:**

1. Der Normalenvektor von $E$ ist $\vec{n} = \vec{u} \times \vec{v}$
2. Stelle die Ebene auf: $E: \vec{n} \cdot (\vec{x} - \vec{a}) = 0$
3. Berechne den Abstand eines Punktes von $h$ (z.B. $B$) zu $E$

### Abstandsformel für windschiefe Geraden

$$d(g, h) = \frac{|(\vec{b} - \vec{a}) \cdot (\vec{u} \times \vec{v})|}{|\vec{u} \times \vec{v}|}$$

Der Zähler ist der Betrag des **Spatprodukts** der drei Vektoren $\vec{b} - \vec{a}$, $\vec{u}$, $\vec{v}$.

### Beispiel

$$g: \vec{x} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$ (x-Achse)

$$h: \vec{x} = \begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

**Kreuzprodukt:**
$$\vec{u} \times \vec{v} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix}$$

**Verbindungsvektor:**
$$\vec{b} - \vec{a} = \begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix}$$

**Spatprodukt:**
$$(\vec{b} - \vec{a}) \cdot (\vec{u} \times \vec{v}) = \begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix} = -2$$

**Abstand:**
$$d = \frac{|-2|}{|\begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix}|} = \frac{2}{1} = 2$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Skalarprodukt]] — Orthogonalitätsbedingung
- → [[Kreuzprodukt]] — Alternative Abstandsformel
- → [[Lagebeziehungen-von-Geraden]] — Vorprüfung auf windschief
- → [[Punkt-Ebene-Abstand]] — Verwandte Abstandsberechnung
- → [[Geraden-in-Parameterform]] — Geradendarstellung

> [!warning] **Prüfungsrelevant**
> - Lotfußpunktverfahren mit Skalarprodukt
> - Kreuzprodukt-Formel für Punkt-Gerade-Abstand
> - Abstand windschiefer Geraden mit Spatprodukt
> - Koordinaten des Lotfußpunkts bestimmen

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie den Abstand des Punktes $P(3|4|5)$ von der Geraden $g$.
> - Bestimmen Sie den Lotfußpunkt des Punktes $P$ auf der Geraden $g$.
> - Zeigen Sie, dass die Geraden $g$ und $h$ windschief sind, und berechnen Sie ihren Abstand.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Punkt-Ebene-Abstand]] — Abstandsformel für Ebenen
> - [[Geometrische-Anwendungen]] — Praktische Anwendungen
