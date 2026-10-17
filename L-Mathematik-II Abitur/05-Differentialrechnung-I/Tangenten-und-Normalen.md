---
author: Andreas Hümmer
title: Tangenten und Normalen
tags:
  - content
  - mathe
  - differentialrechnung
  - tangente
  - normale
  - geradengleichung
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Tangenten und Normalen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Tangentengleichung an einer Kurve aufstellen können
> - Die Normalengleichung senkrecht zur Tangente bestimmen können
> - Tangenten mit vorgegebener Steigung oder durch einen externen Punkt finden können
> - Berührpunkte und Schnittpunkte von Tangenten berechnen können

---

## Überblick

Die Tangente an eine Kurve im Punkt $P$ ist die Gerade, die die Kurve in $P$ berührt und dort dieselbe Steigung wie die Kurve hat. Die Normale steht senkrecht auf der Tangente. Das Aufstellen von Tangenten- und Normalengleichungen ist eine der wichtigsten Anwendungen der Ableitung und gehört zum Standardrepertoire der Analysis.

## Die Tangentengleichung

### Herleitung

Eine Tangente an den Graphen von $f$ im Punkt $P(x_0 | f(x_0))$ ist eine Gerade mit:
- **Steigung:** $m = f'(x_0)$
- **Punkt:** $P(x_0 | f(x_0))$

Mit der Punkt-Steigungsform einer Geraden $y - y_1 = m(x - x_1)$:

> [!note] **Tangentengleichung**
> Die Tangente an den Graphen von $f$ im Punkt $P(x_0 | f(x_0))$ hat die Gleichung:
> $$t(x) = f'(x_0) \cdot (x - x_0) + f(x_0)$$
> oder ausgeschrieben:
> $$y = f(x_0) + f'(x_0) \cdot (x - x_0)$$

### Beispiel 1: Einfache Tangente

Bestimme die Tangentengleichung an $f(x) = x^2$ im Punkt $P(2 | 4)$.

**Lösung:**
1. Funktionswert: $f(2) = 4$ ✓
2. Ableitung: $f'(x) = 2x$
3. Steigung bei $x_0 = 2$: $f'(2) = 4$
4. Tangentengleichung:
   $$t(x) = f(2) + f'(2)(x - 2) = 4 + 4(x - 2) = 4x - 4$$

### Beispiel 2: Tangente an Exponentialfunktion

Bestimme die Tangentengleichung an $f(x) = e^x$ im Punkt $P(0 | 1)$.

**Lösung:**
1. Funktionswert: $f(0) = e^0 = 1$ ✓
2. Ableitung: $f'(x) = e^x$
3. Steigung bei $x_0 = 0$: $f'(0) = 1$
4. Tangentengleichung:
   $$t(x) = 1 + 1 \cdot (x - 0) = x + 1$$

### Beispiel 3: Tangente an trigonometrische Funktion

Bestimme die Tangentengleichung an $f(x) = \sin(x)$ im Punkt $P(\frac{\pi}{4} | \frac{\sqrt{2}}{2})$.

**Lösung:**
1. $f(\frac{\pi}{4}) = \sin(\frac{\pi}{4}) = \frac{\sqrt{2}}{2}$ ✓
2. $f'(x) = \cos(x)$
3. $f'(\frac{\pi}{4}) = \cos(\frac{\pi}{4}) = \frac{\sqrt{2}}{2}$
4. Tangentengleichung:
   $$t(x) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}\left(x - \frac{\pi}{4}\right)$$
   $$= \frac{\sqrt{2}}{2}x + \frac{\sqrt{2}}{2}\left(1 - \frac{\pi}{4}\right)$$

## Die Normalengleichung

Die Normale steht senkrecht auf der Tangente. Für senkrechte Geraden gilt:
$$m_1 \cdot m_2 = -1$$

> [!note] **Normalengleichung**
> Die Normale an den Graphen von $f$ im Punkt $P(x_0 | f(x_0))$ hat die Gleichung:
> $$n(x) = -\frac{1}{f'(x_0)} \cdot (x - x_0) + f(x_0)$$
> **Voraussetzung:** $f'(x_0) \neq 0$

### Beispiel: Tangente und Normale

Bestimme Tangente und Normale an $f(x) = x^3$ im Punkt $P(1 | 1)$.

**Lösung:**
1. $f(1) = 1$ ✓
2. $f'(x) = 3x^2$, also $f'(1) = 3$

**Tangente:**
$$t(x) = 1 + 3(x - 1) = 3x - 2$$

**Normale:** Steigung $m_n = -\frac{1}{3}$
$$n(x) = 1 - \frac{1}{3}(x - 1) = -\frac{1}{3}x + \frac{4}{3}$$

## Spezielle Tangentenprobleme

### Tangente mit vorgegebener Steigung

**Aufgabe:** Finde alle Punkte auf dem Graphen von $f$, in denen die Tangente die Steigung $m$ hat.

**Vorgehen:**
1. Setze $f'(x) = m$
2. Löse nach $x$ auf
3. Berechne die zugehörigen $y$-Werte

**Beispiel:** An welchen Stellen hat die Tangente an $f(x) = x^3 - 3x$ die Steigung 0?

**Lösung:**
$$f'(x) = 3x^2 - 3 = 0$$
$$3x^2 = 3 \Rightarrow x^2 = 1 \Rightarrow x = \pm 1$$

Die Tangente hat Steigung 0 in den Punkten $P_1(1 | -2)$ und $P_2(-1 | 2)$.

### Tangente durch einen externen Punkt

**Aufgabe:** Finde alle Tangenten an $f$, die durch einen gegebenen Punkt $Q(x_Q | y_Q)$ verlaufen (der nicht auf dem Graphen liegt).

**Vorgehen:**
1. Ansatz: Tangente im Berührpunkt $P(x_0 | f(x_0))$
   $$t(x) = f(x_0) + f'(x_0)(x - x_0)$$
2. Bedingung: $Q$ liegt auf der Tangente
   $$y_Q = f(x_0) + f'(x_0)(x_Q - x_0)$$
3. Löse nach $x_0$ auf

**Beispiel:** Welche Tangenten an $f(x) = x^2$ gehen durch den Punkt $Q(2 | -3)$?

**Lösung:**
- Tangente bei $x_0$: $t(x) = x_0^2 + 2x_0(x - x_0) = 2x_0 x - x_0^2$
- Bedingung $Q \in t$:
  $$-3 = 2x_0 \cdot 2 - x_0^2 = 4x_0 - x_0^2$$
  $$x_0^2 - 4x_0 - 3 = 0$$
  $$x_0 = \frac{4 \pm \sqrt{16 + 12}}{2} = \frac{4 \pm \sqrt{28}}{2} = 2 \pm \sqrt{7}$$

Die zwei Tangenten berühren den Graphen bei $x_0 = 2 + \sqrt{7}$ und $x_0 = 2 - \sqrt{7}$.

### Gemeinsame Tangente zweier Kurven

**Aufgabe:** Finde eine Gerade, die zwei Kurven $f$ und $g$ jeweils berührt.

**Vorgehen:**
1. Berührpunkt bei $f$: $P(a | f(a))$ mit Steigung $f'(a)$
2. Berührpunkt bei $g$: $Q(b | g(b))$ mit Steigung $g'(b)$
3. Bedingungen:
   - Gleiche Steigung: $f'(a) = g'(b)$
   - Beide Punkte auf derselben Geraden: $\frac{g(b) - f(a)}{b - a} = f'(a)$

## Schnittpunkt Tangente mit Koordinatenachsen

Die Tangente $t(x) = f(x_0) + f'(x_0)(x - x_0)$ schneidet:

- **$y$-Achse** bei $x = 0$:
  $$y_S = f(x_0) - f'(x_0) \cdot x_0$$

- **$x$-Achse** bei $y = 0$:
  $$x_S = x_0 - \frac{f(x_0)}{f'(x_0)}$$ (falls $f'(x_0) \neq 0$)

## Zusammenfassung der Formeln

| Objekt | Formel |
|--------|--------|
| Tangentensteigung | $m_t = f'(x_0)$ |
| Tangentengleichung | $t(x) = f(x_0) + f'(x_0)(x - x_0)$ |
| Normalensteigung | $m_n = -\frac{1}{f'(x_0)}$ |
| Normalengleichung | $n(x) = f(x_0) - \frac{1}{f'(x_0)}(x - x_0)$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Geometrische-Bedeutung-der-Ableitung|Geometrische Bedeutung der Ableitung]] – Tangente als Steigung
- → [[Ableitungsregeln|Ableitungsregeln]] – Berechnung von $f'(x_0)$
- → [[Lineare-Funktionen|Lineare Funktionen]] – Die Tangente als lineare Funktion
- → [[Nullstellen|Nullstellen]] – Schnittpunkt mit der $x$-Achse
- → [[Definition-der-Ableitung|Definition der Ableitung]] – Theoretische Grundlage

> [!warning] **Prüfungsrelevant**
> - Die Tangentengleichung $t(x) = f(x_0) + f'(x_0)(x - x_0)$ ist **Standardwissen**
> - Die Normalensteigung als negativer Kehrwert der Tangentensteigung
> - Tangenten mit vorgegebener Steigung oder durch externe Punkte sind häufige Aufgaben
> - Schnittpunkte der Tangente mit den Achsen berechnen können

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Gleichung der Tangente an den Graphen von $f$ im Punkt $P$."
> - "In welchen Punkten hat die Tangente die Steigung $m$?"
> - "Welche Tangenten an den Graphen von $f$ verlaufen durch den Punkt $Q$?"
> - "Bestimmen Sie Tangente und Normale in $P$ und berechnen Sie deren Schnittpunkt mit der $x$-Achse."

## Quellen

- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Lineare-Funktionen|Lineare Funktionen]] – Vertiefung zu Geradengleichungen
> - [[Schnittpunkte|Schnittpunkte]] – Allgemeine Schnittpunktberechnung
