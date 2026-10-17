---
author: Andreas Hümmer
title: Schnittpunkte
tags:
  - content
  - mathe
  - funktionen
  - schnittpunkte
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Schnittpunkte

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Schnittpunkte zweier Funktionen analytisch bestimmen können
> - Schnittpunkte mit den Koordinatenachsen berechnen können
> - Die geometrische und anwendungsbezogene Bedeutung von Schnittpunkten verstehen
> - Schnittprobleme als Gleichungssysteme formulieren und lösen können

---

## Überblick

**Schnittpunkte** sind Punkte, an denen sich zwei Graphen treffen oder ein Graph eine der Koordinatenachsen schneidet. Die Bestimmung von Schnittpunkten ist ein zentrales Werkzeug in der Analysis, das bei Optimierungsproblemen, Flächenberechnungen und Modellierungen eine wichtige Rolle spielt.

## Schnittpunkte mit den Koordinatenachsen

### Schnittpunkt mit der y-Achse

Der Graph einer Funktion $f$ schneidet die $y$-Achse am Punkt $(0, f(0))$, sofern $0 \in D_f$.

**Berechnung:**
$$S_y = (0, f(0))$$

**Beispiel:** Für $f(x) = x^2 - 3x + 2$:
$$f(0) = 0 - 0 + 2 = 2$$
$$S_y = (0, 2)$$

### Schnittpunkte mit der x-Achse

Die Schnittpunkte mit der $x$-Achse sind die **Nullstellen** der Funktion.

$$f(x) = 0 \quad \Rightarrow \quad S_x = (x_0, 0)$$

Siehe → [[Nullstellen]] für Lösungsverfahren.

## Schnittpunkte zweier Funktionen

### Allgemeines Verfahren

Zwei Funktionen $f$ und $g$ schneiden sich in den Punkten, an denen ihre Funktionswerte übereinstimmen:

$$f(x) = g(x)$$

Die Lösungen $x_1, x_2, \ldots$ dieser Gleichung liefern die Schnittpunkte:
$$S_i = (x_i, f(x_i)) = (x_i, g(x_i))$$

### Beispiel: Zwei Polynome

Bestimme die Schnittpunkte von $f(x) = x^2$ und $g(x) = 2x + 3$.

**Gleichsetzen:**
$$x^2 = 2x + 3$$
$$x^2 - 2x - 3 = 0$$
$$(x-3)(x+1) = 0$$
$$x_1 = 3, \quad x_2 = -1$$

**Schnittpunkte berechnen:**
$$S_1 = (3, f(3)) = (3, 9)$$
$$S_2 = (-1, f(-1)) = (-1, 1)$$

### Beispiel: Exponential- und lineare Funktion

Bestimme die Schnittpunkte von $f(x) = e^x$ und $g(x) = x + 2$.

**Gleichsetzen:**
$$e^x = x + 2$$

Diese Gleichung ist nicht algebraisch lösbar. Wir können:
1. **Graphisch:** Zeichnen beider Funktionen
2. **Numerisch:** Newton-Verfahren oder Näherung

Durch Probieren: $f(0) = 1$ und $g(0) = 2$, also $f(0) < g(0)$

Bei $x = 1$: $f(1) = e \approx 2.718$ und $g(1) = 3$, also $f(1) < g(1)$

Bei $x = 2$: $f(2) = e^2 \approx 7.39$ und $g(2) = 4$, also $f(2) > g(2)$

Es gibt einen Schnittpunkt zwischen $x = 1$ und $x = 2$.

Numerische Lösung: $x \approx 1.146$, also $S \approx (1.146, 3.146)$

## Spezialfälle

### Tangentialer Berührpunkt

Wenn zwei Graphen sich nur berühren (nicht schneiden), liegt ein **Berührpunkt** vor. Dort gilt:

$$f(x_0) = g(x_0) \quad \text{und} \quad f'(x_0) = g'(x_0)$$

**Beispiel:** Wann berührt die Parabel $f(x) = x^2$ die Gerade $g(x) = mx$?

Bedingungen:
1. $x^2 = mx \Rightarrow x^2 - mx = 0 \Rightarrow x(x-m) = 0$
2. $2x = m$

Aus (2): $x = \frac{m}{2}$

Einsetzen in (1): $\frac{m}{2} \cdot (\frac{m}{2} - m) = \frac{m}{2} \cdot (-\frac{m}{2}) = -\frac{m^2}{4}$

Für eine Berührung müsste dies $= 0$ sein, also $m = 0$.

Die einzige Gerade durch den Ursprung, die $f(x) = x^2$ berührt, ist die $x$-Achse selbst.

### Kein Schnittpunkt

Wenn $f(x) = g(x)$ keine Lösung hat, schneiden sich die Graphen nicht.

**Beispiel:** $f(x) = e^x$ und $g(x) = -1$

$$e^x = -1$$

Da $e^x > 0$ für alle $x$, existiert keine Lösung.

### Unendlich viele Schnittpunkte

**Beispiel:** $f(x) = \sin(x)$ und $g(x) = 0$

$$\sin(x) = 0 \quad \Leftrightarrow \quad x = k\pi, \, k \in \mathbb{Z}$$

Unendlich viele Schnittpunkte: $S_k = (k\pi, 0)$

## Anwendungen

### Angebot und Nachfrage (Break-Even)

In der Wirtschaftsmathematik schneiden sich Angebots- und Nachfragekurven im **Gleichgewichtspunkt**.

**Beispiel:**
- Nachfrage: $N(p) = 100 - 2p$
- Angebot: $A(p) = 20 + 3p$

Gleichgewicht:
$$100 - 2p = 20 + 3p$$
$$80 = 5p$$
$$p^* = 16$$

Gleichgewichtsmenge: $N(16) = 100 - 32 = 68$

### Flächenberechnung

Bei der Berechnung von Flächen zwischen Funktionsgraphen sind die Schnittpunkte die **Integrationsgrenzen**.

$$A = \int_{x_1}^{x_2} |f(x) - g(x)| \, dx$$

Dabei sind $x_1$ und $x_2$ die Schnittpunkte von $f$ und $g$.

### Physik: Bewegungsaufgaben

Zwei Objekte mit Weg-Zeit-Funktionen $s_1(t)$ und $s_2(t)$ treffen sich, wenn:
$$s_1(t) = s_2(t)$$

**Beispiel:** Ein Auto startet bei $t = 0$ mit $s_1(t) = 20t$ (in m). Ein zweites Auto startet 2 Sekunden später mit $s_2(t) = 30(t-2)$ für $t \geq 2$.

Wann überholt das zweite Auto?
$$20t = 30(t-2)$$
$$20t = 30t - 60$$
$$60 = 10t$$
$$t = 6$$

Nach 6 Sekunden, bei Position $s = 120$ m.

## Systematische Vorgehensweise

1. **Gleichsetzen:** $f(x) = g(x)$
2. **Umformen:** Auf eine Seite bringen: $f(x) - g(x) = 0$
3. **Lösen:** Mit geeignetem Verfahren (abhängig vom Funktionstyp)
4. **Funktionswerte berechnen:** $y_i = f(x_i)$
5. **Schnittpunkte angeben:** $S_i = (x_i, y_i)$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Nullstellen]] – Schnittpunkte mit der $x$-Achse
- → [[Gleichungssysteme]] – Mehrere Bedingungen gleichzeitig lösen
- → [[Gleichungen-hoeheren-Grades]] – Lösen komplexerer Schnittgleichungen
- → [[Lineare-Funktionen]] – Schnittpunkt zweier Geraden

> [!warning] **Prüfungsrelevant**
> - Systematische Berechnung von Schnittpunkten zweier Funktionen
> - Unterscheidung zwischen Schnitt- und Berührpunkten
> - Anwendung bei Flächenberechnungen (Integrationsgrenzen)
> - Interpretation von Schnittpunkten im Sachkontext

> [!question] **Typische Prüfungsfragen**
> - Bestimme alle Schnittpunkte von $f(x) = x^3 - 4x$ und $g(x) = x$.
> - Für welchen Wert von $a$ berührt die Parabel $f(x) = x^2 + a$ die Gerade $g(x) = 2x$?
> - Die Kostenfunktion ist $K(x) = 0.5x^2 + 10$ und die Erlösfunktion $E(x) = 5x$. Bestimme den Break-Even-Punkt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[07-Integralrechnung-I|Integralrechnung I]] – Flächenberechnung zwischen Kurven
> - [[Quadratische-Funktionen]] – Schnitt von Parabeln mit Geraden
> - [[Anwendungen-algebraischer-Methoden]] – Praktische Anwendungen
