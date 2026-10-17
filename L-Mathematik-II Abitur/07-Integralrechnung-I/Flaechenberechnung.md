---
author: Andreas Hümmer
title: Flächenberechnung
tags:
  - content
  - mathe
  - integralrechnung
  - fläche
  - anwendung
created: 2026-10-17
modified: 2026-10-17
---

# Flächenberechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Flächen zwischen Funktionsgraph und $x$-Achse berechnen können
> - Flächen zwischen zwei Funktionsgraphen bestimmen können
> - Schnittpunkte als Integrationsgrenzen ermitteln können
> - Das korrekte Vorgehen bei Vorzeichenwechseln anwenden können

---

## Überblick

Die Berechnung von Flächen ist eine der wichtigsten Anwendungen der Integralrechnung. Während das bestimmte Integral die orientierte Fläche liefert, müssen für den tatsächlichen Flächeninhalt oft Beträge berücksichtigt werden. In diesem Kapitel systematisieren wir die verschiedenen Typen von Flächenberechnungen.

## Fläche zwischen Graph und $x$-Achse

### Fall 1: Funktion ist nichtnegativ

Ist $f(x) \geq 0$ für alle $x \in [a, b]$, so gilt für die Fläche:

$$A = \int_a^b f(x) \, dx$$

### Fall 2: Funktion ist nichtpositiv

Ist $f(x) \leq 0$ für alle $x \in [a, b]$, so gilt:

$$A = -\int_a^b f(x) \, dx = \int_a^b |f(x)| \, dx$$

### Fall 3: Funktion wechselt das Vorzeichen

Hat $f(x)$ Nullstellen im Intervall $[a, b]$, muss das Intervall an den Nullstellen aufgeteilt werden. Sei $f(c) = 0$ mit $a < c < b$:

$$A = \left|\int_a^c f(x) \, dx\right| + \left|\int_c^b f(x) \, dx\right|$$

### Beispiel: Vorzeichenwechsel

Berechne die Fläche zwischen dem Graphen von $f(x) = x^2 - 1$ und der $x$-Achse im Intervall $[-2, 2]$.

**Schritt 1**: Nullstellen bestimmen
$$x^2 - 1 = 0 \Rightarrow x = \pm 1$$

**Schritt 2**: Vorzeichen in den Teilintervallen
- In $[-2, -1]$: $f(x) > 0$
- In $[-1, 1]$: $f(x) < 0$
- In $[1, 2]$: $f(x) > 0$

**Schritt 3**: Stammfunktion: $F(x) = \frac{x^3}{3} - x$

**Schritt 4**: Teilintegrale
$$\int_{-2}^{-1} (x^2-1) \, dx = \left[\frac{x^3}{3} - x\right]_{-2}^{-1} = \left(-\frac{1}{3}+1\right) - \left(-\frac{8}{3}+2\right) = \frac{2}{3} + \frac{2}{3} = \frac{4}{3}$$

$$\int_{-1}^{1} (x^2-1) \, dx = \left[\frac{x^3}{3} - x\right]_{-1}^{1} = \left(\frac{1}{3}-1\right) - \left(-\frac{1}{3}+1\right) = -\frac{4}{3}$$

$$\int_{1}^{2} (x^2-1) \, dx = \left[\frac{x^3}{3} - x\right]_{1}^{2} = \left(\frac{8}{3}-2\right) - \left(\frac{1}{3}-1\right) = \frac{4}{3}$$

**Schritt 5**: Flächeninhalt
$$A = \frac{4}{3} + \left|-\frac{4}{3}\right| + \frac{4}{3} = \frac{4}{3} + \frac{4}{3} + \frac{4}{3} = 4$$

## Fläche zwischen zwei Funktionsgraphen

### Grundprinzip

Die Fläche zwischen den Graphen von $f(x)$ und $g(x)$ im Intervall $[a, b]$ berechnet sich als:

$$A = \int_a^b |f(x) - g(x)| \, dx$$

### Fall: Eine Funktion liegt immer oberhalb

Gilt $f(x) \geq g(x)$ für alle $x \in [a, b]$, vereinfacht sich die Formel zu:

$$A = \int_a^b \big(f(x) - g(x)\big) \, dx$$

### Schritt-für-Schritt-Vorgehen

1. **Schnittpunkte bestimmen**: Löse $f(x) = g(x)$
2. **Lage prüfen**: Bestimme in jedem Teilintervall, welche Funktion oben liegt
3. **Integrale berechnen**: Integriere $(\text{obere} - \text{untere})$ über jedes Teilintervall
4. **Summieren**: Addiere alle Teilflächen

### Beispiel: Fläche zwischen zwei Parabeln

Berechne die Fläche zwischen $f(x) = x^2$ und $g(x) = 2x$.

**Schritt 1**: Schnittpunkte
$$x^2 = 2x \Rightarrow x^2 - 2x = 0 \Rightarrow x(x-2) = 0$$
$$x_1 = 0, \quad x_2 = 2$$

**Schritt 2**: Lage prüfen (z.B. bei $x = 1$)
$$f(1) = 1, \quad g(1) = 2$$

Da $g(1) > f(1)$, liegt $g$ im Intervall $[0, 2]$ oberhalb von $f$.

**Schritt 3**: Integral berechnen
$$A = \int_0^2 \big(g(x) - f(x)\big) \, dx = \int_0^2 (2x - x^2) \, dx$$

$$= \left[x^2 - \frac{x^3}{3}\right]_0^2 = \left(4 - \frac{8}{3}\right) - 0 = \frac{4}{3}$$

## Eingeschlossene Fläche

### Typische Aufgabenstellung

„Berechne die von den Graphen von $f$ und $g$ eingeschlossene Fläche."

### Vorgehen

1. **Alle Schnittpunkte** der beiden Funktionen bestimmen
2. Diese Schnittpunkte bilden automatisch die **Integrationsgrenzen**
3. Die Fläche zwischen benachbarten Schnittpunkten berechnen
4. Alle Teilflächen addieren

### Beispiel: Parabel und Gerade

Die Graphen von $f(x) = -x^2 + 4$ und $g(x) = x$ schließen eine Fläche ein. Berechne diese.

**Schritt 1**: Schnittpunkte
$$-x^2 + 4 = x \Rightarrow x^2 + x - 4 = 0$$
$$x = \frac{-1 \pm \sqrt{1 + 16}}{2} = \frac{-1 \pm \sqrt{17}}{2}$$

Also $x_1 = \frac{-1 - \sqrt{17}}{2} \approx -2{,}56$ und $x_2 = \frac{-1 + \sqrt{17}}{2} \approx 1{,}56$.

**Schritt 2**: Lage prüfen (z.B. bei $x = 0$)
$$f(0) = 4, \quad g(0) = 0$$

Die Parabel liegt oberhalb der Geraden.

**Schritt 3**: Integral
$$A = \int_{x_1}^{x_2} \big(f(x) - g(x)\big) \, dx = \int_{x_1}^{x_2} (-x^2 - x + 4) \, dx$$

$$= \left[-\frac{x^3}{3} - \frac{x^2}{2} + 4x\right]_{x_1}^{x_2}$$

Nach Einsetzen und Vereinfachen: $A = \frac{17\sqrt{17}}{6} \approx 11{,}69$

## Fläche mit gegebenen Grenzen

### Aufgabentyp

„Berechne die Fläche zwischen $f(x)$ und der $x$-Achse im Intervall $[a, b]$."

### Wichtig

Auch wenn die Grenzen gegeben sind, müssen Nullstellen im Inneren des Intervalls berücksichtigt werden!

## Zusammenfassung: Checkliste

| Situation | Formel |
|-----------|--------|
| $f(x) \geq 0$ auf $[a,b]$ | $A = \int_a^b f(x) \, dx$ |
| $f(x) \leq 0$ auf $[a,b]$ | $A = -\int_a^b f(x) \, dx$ |
| $f(x)$ mit Vorzeichenwechsel | Aufteilen, Beträge addieren |
| Fläche zwischen $f$ und $g$ | $A = \int_a^b |f(x) - g(x)| \, dx$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bestimmte-Integrale]] – Grundlage der Flächenberechnung
- → [[Flaechenbilanz]] – Orientierte vs. absolute Fläche
- → [[Nullstellen]] – Bestimmung der Nullstellen
- → [[Schnittpunkte]] – Berechnung von Schnittpunkten
- → [[Quadratische-Funktionen]] – Typische Beispielfunktionen

> [!warning] **Prüfungsrelevant**
> - Bei Vorzeichenwechsel: Intervall aufteilen, Beträge addieren!
> - Fläche zwischen zwei Kurven: $\int (\text{obere} - \text{untere}) \, dx$
> - Schnittpunkte bestimmen die Integrationsgrenzen
> - Immer prüfen, welche Funktion wo oberhalb liegt

> [!question] **Typische Prüfungsfragen**
> - Berechne die Fläche, die der Graph von $f(x) = x^3 - 4x$ mit der $x$-Achse einschließt.
> - Bestimme den Flächeninhalt zwischen den Graphen von $f(x) = x^2$ und $g(x) = \sqrt{x}$.
> - Die Gerade $g$ und die Parabel $f(x) = 4 - x^2$ schließen eine Fläche ein. Berechne diese.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Abiturprüfungsaufgaben Mathematik.

> [!tip] **Weiterführende Links**
> - [[Integrale-im-Sachzusammenhang]] – Praktische Anwendungen
> - [[Flaechenbilanz]] – Umgang mit orientierten Flächen
