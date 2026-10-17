---
author: Andreas Hümmer
title: Schnittpunkte und Schnittgeraden
tags:
  - content
  - mathe
  - analytische-geometrie
  - schnittpunkte
  - schnittgeraden
created: 2026-10-17
modified: 2026-10-17
---

# Schnittpunkte und Schnittgeraden

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Schnittpunkte zweier Geraden im Raum berechnen können
> - Durchstoßpunkte von Geraden durch Ebenen bestimmen
> - Schnittgeraden zweier Ebenen berechnen können
> - Schnitte von drei Ebenen untersuchen und lösen

---

## Überblick

Die Berechnung von Schnittmengen geometrischer Objekte gehört zu den wichtigsten Anwendungen der analytischen Geometrie. Je nach Kombination der Objekte ergeben sich Punkte, Geraden oder auch leere Schnittmengen. Dieses Kapitel systematisiert die verschiedenen Fälle und stellt die Berechnungsmethoden vor.

## Schnittpunkt zweier Geraden

Gegeben seien zwei Geraden in Parameterform:

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}$$
$$h: \vec{x} = \vec{b} + s \cdot \vec{v}$$

### Voraussetzung

Die Geraden müssen sich schneiden (nicht parallel, nicht windschief). Dies ist vorher zu prüfen (siehe [[Lagebeziehungen-von-Geraden]]).

### Berechnung

Setze die Gleichungen gleich:

$$\vec{a} + t \cdot \vec{u} = \vec{b} + s \cdot \vec{v}$$

Dies ergibt ein lineares Gleichungssystem mit drei Gleichungen für zwei Unbekannte. Löse zwei Gleichungen und prüfe mit der dritten.

### Beispiel

$$g: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 5 \\ 3 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$$

**Gleichungssystem:**
1. $1 + 2t = 5 + s$
2. $0 + t = 3 + s$
3. $2 + t = 0 - s$

Aus (2): $t = 3 + s$

Einsetzen in (1): $1 + 2(3 + s) = 5 + s \Rightarrow 7 + 2s = 5 + s \Rightarrow s = -2$

Damit: $t = 3 + (-2) = 1$

**Probe in (3):** $2 + 1 = 0 - (-2) \Rightarrow 3 = 2$ ✗

Die Probe schlägt fehl. Die Geraden sind **windschief**, kein Schnittpunkt.

Neues Beispiel mit schneidenden Geraden:

$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 3 \\ 0 \\ 3 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$

**Gleichungssystem:**
1. $1 + t = 3 \Rightarrow t = 2$
2. $2 + t = 0 + s \Rightarrow s = 2 + 2 = 4$
3. $3 + 0 = 3 + 0$ ✓

**Schnittpunkt:** $S = (1 + 2, 2 + 2, 3) = (3, 4, 3)$

## Durchstoßpunkt: Gerade und Ebene

Gegeben:

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}$$
$$E: n_1 x + n_2 y + n_3 z = d$$

### Berechnung

1. Setze die Parameterdarstellung von $g$ in die Ebenengleichung ein
2. Löse nach $t$ auf
3. Berechne den Durchstoßpunkt durch Einsetzen von $t$

### Beispiel

$$g: \vec{x} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix}$$

$$E: 3x + y - z = 8$$

**Einsetzen:**
$$3(2 + t) + (1 + 2t) - (4 - 2t) = 8$$
$$6 + 3t + 1 + 2t - 4 + 2t = 8$$
$$3 + 7t = 8$$
$$t = \frac{5}{7}$$

**Durchstoßpunkt:**
$$D = \begin{pmatrix} 2 + \frac{5}{7} \\ 1 + \frac{10}{7} \\ 4 - \frac{10}{7} \end{pmatrix} = \begin{pmatrix} \frac{19}{7} \\ \frac{17}{7} \\ \frac{18}{7} \end{pmatrix}$$

## Schnittgerade zweier Ebenen

Gegeben:

$$E_1: a_1 x + b_1 y + c_1 z = d_1$$
$$E_2: a_2 x + b_2 y + c_2 z = d_2$$

### Voraussetzung

Die Ebenen dürfen nicht parallel sein. Der Richtungsvektor der Schnittgeraden ist:

$$\vec{u} = \vec{n}_1 \times \vec{n}_2$$

### Methode 1: Setze eine Variable fest

1. Setze z.B. $z = 0$ (falls möglich)
2. Löse das entstehende $2 \times 2$-System nach $x$ und $y$
3. Der gefundene Punkt plus Richtungsvektor ergibt die Gerade

### Methode 2: Eliminationsverfahren

Löse das unterbestimmte Gleichungssystem durch Elimination. Parametrisiere die freie Variable.

### Beispiel

$$E_1: x + 2y + z = 6$$
$$E_2: 2x - y + z = 3$$

**Richtungsvektor:**
$$\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \times \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 - 1 \cdot (-1) \\ 1 \cdot 2 - 1 \cdot 1 \\ 1 \cdot (-1) - 2 \cdot 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \\ -5 \end{pmatrix}$$

**Punkt auf der Schnittgeraden** (setze $z = 0$):

$x + 2y = 6$ und $2x - y = 3$

Aus der zweiten Gleichung: $y = 2x - 3$

Einsetzen: $x + 2(2x - 3) = 6 \Rightarrow 5x - 6 = 6 \Rightarrow x = \frac{12}{5}$

$y = 2 \cdot \frac{12}{5} - 3 = \frac{24}{5} - \frac{15}{5} = \frac{9}{5}$

**Schnittgerade:**
$$g: \vec{x} = \begin{pmatrix} \frac{12}{5} \\ \frac{9}{5} \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 3 \\ 1 \\ -5 \end{pmatrix}$$

## Schnitt dreier Ebenen

Drei Ebenen im Raum können sich schneiden in:

| Fall | Lösung | Beschreibung |
|------|--------|--------------|
| Einem Punkt | eindeutig | Normalfall bei unabhängigen Ebenen |
| Einer Geraden | einparametrig | Zwei Ebenen identisch oder alle drei durch eine Gerade |
| Einer Ebene | zweiparametrig | Alle drei Ebenen identisch |
| Leer | keine Lösung | Widersprüchliches System |

### Lösung als lineares Gleichungssystem

$$\begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix}$$

Die Lösbarkeit hängt vom Rang der Koeffizientenmatrix und der erweiterten Matrix ab.

### Beispiel: Schnitt in einem Punkt

$$E_1: x + y + z = 6$$
$$E_2: 2x - y + z = 3$$
$$E_3: x + y - z = 2$$

Addition von $E_1$ und $E_3$: $2x + 2y = 8 \Rightarrow x + y = 4$

Subtraktion $E_1 - E_3$: $2z = 4 \Rightarrow z = 2$

Aus $E_2$: $2x - y + 2 = 3 \Rightarrow 2x - y = 1$

Mit $x + y = 4$: Addition $\Rightarrow 3x = 5 \Rightarrow x = \frac{5}{3}$

$y = 4 - \frac{5}{3} = \frac{7}{3}$

**Schnittpunkt:** $S = \left( \frac{5}{3}, \frac{7}{3}, 2 \right)$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Lagebeziehungen-von-Geraden]] — Vorprüfung ob Schnitt existiert
- → [[Lagebeziehungen-von-Ebenen]] — Vorprüfung bei Ebenen
- → [[Kreuzprodukt]] — Richtungsvektor der Schnittgeraden
- → [[Gleichungssysteme]] — Lösungsverfahren für LGS
- → [[Geraden-in-Parameterform]] — Darstellung der Ergebnisse

> [!warning] **Prüfungsrelevant**
> - Durchstoßpunkt Gerade-Ebene durch Einsetzen berechnen
> - Schnittgerade zweier Ebenen mit Kreuzprodukt und Punktbestimmung
> - Interpretation der Lösungsfälle bei drei Ebenen
> - Sonderfälle erkennen (parallel, in Ebene liegend)

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie den Durchstoßpunkt der Geraden $g$ durch die Ebene $E$.
> - Bestimmen Sie die Schnittgerade der Ebenen $E_1: x + y - z = 2$ und $E_2: 2x - y + z = 4$.
> - Untersuchen Sie, ob sich die drei Ebenen in einem Punkt schneiden.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Winkelberechnungen]] — Schnittwinkel bestimmen
> - [[Geometrische-Anwendungen]] — Anwendungsaufgaben
