---
author: Andreas Hümmer
title: Rotationskörper – Volumen durch Rotation
tags:
  - content
  - mathe
  - integralrechnung
  - rotationskoerper
  - volumen
created: 2025-06-26
modified: 2025-06-26
---

# Rotationskörper

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept eines Rotationskörpers verstehen und visualisieren können
> - Die Scheibenformel zur Volumenberechnung anwenden können
> - Zwischen Rotation um die x-Achse und um die y-Achse unterscheiden können
> - Rotationskörper aus der Rotation einer Fläche zwischen zwei Graphen berechnen können

---

## Überblick

Ein **Rotationskörper** entsteht, wenn eine ebene Fläche um eine Achse rotiert. Diese geometrischen Körper begegnen uns überall im Alltag: Vasen, Flaschen, Kegel, Kugeln, Trichter und viele technische Bauteile sind Rotationskörper.

Die Integralrechnung ermöglicht es uns, das **Volumen** solcher Körper exakt zu berechnen, selbst wenn keine einfachen geometrischen Formeln existieren.

---

## Rotation um die x-Achse

### Die Scheibenformel (Prinzip von Cavalieri)

Rotiert der Graph einer Funktion $f(x) \geq 0$ im Intervall $[a, b]$ um die $x$-Achse, entsteht ein Rotationskörper.

Das Volumen berechnet sich durch Aufsummieren infinitesimal dünner Kreisscheiben:

$$V = \pi \int_a^b [f(x)]^2 \, dx$$

### Herleitung

Eine dünne Scheibe bei $x$ hat:
- **Radius**: $r = f(x)$
- **Dicke**: $dx$
- **Volumen**: $dV = \pi \cdot r^2 \cdot dx = \pi \cdot [f(x)]^2 \cdot dx$

```
      │ f(x)         Kreisscheibe
      │  ●━━━━━━━━┓    bei x
      │  │        ┃
    ──┼──┼────────╂───→ x
      │  │        ┃
      │  ●━━━━━━━━┛
      │           dx
```

Das Gesamtvolumen ist die Summe aller Scheiben:

$$V = \int_a^b \pi \cdot [f(x)]^2 \, dx = \pi \int_a^b [f(x)]^2 \, dx$$

### Beispiel 1: Kegel

Ein Kegel entsteht durch Rotation der Geraden $f(x) = \frac{r}{h} \cdot x$ um die $x$-Achse im Intervall $[0, h]$.

**Berechnung:**

$$V = \pi \int_0^h \left(\frac{r}{h} \cdot x\right)^2 \, dx = \pi \cdot \frac{r^2}{h^2} \int_0^h x^2 \, dx$$

$$= \pi \cdot \frac{r^2}{h^2} \cdot \left[\frac{x^3}{3}\right]_0^h = \pi \cdot \frac{r^2}{h^2} \cdot \frac{h^3}{3} = \frac{1}{3}\pi r^2 h$$

Dies ist die bekannte Kegelvolumenformel! ✓

### Beispiel 2: Kugel

Eine Kugel mit Radius $R$ entsteht durch Rotation des Halbkreises $f(x) = \sqrt{R^2 - x^2}$ um die $x$-Achse.

**Berechnung:**

$$V = \pi \int_{-R}^{R} (\sqrt{R^2 - x^2})^2 \, dx = \pi \int_{-R}^{R} (R^2 - x^2) \, dx$$

$$= \pi \left[R^2 x - \frac{x^3}{3}\right]_{-R}^{R}$$

$$= \pi \left[\left(R^3 - \frac{R^3}{3}\right) - \left(-R^3 + \frac{R^3}{3}\right)\right]$$

$$= \pi \left[\frac{2R^3}{3} + \frac{2R^3}{3}\right] = \frac{4}{3}\pi R^3$$

Dies ist die bekannte Kugelvolumenformel! ✓

---

## Rotation um die y-Achse

### Formel für Rotation um die y-Achse

Rotiert ein Funktionsgraph um die $y$-Achse, verwenden wir die Umkehrfunktion oder die Mantelmethode.

**Mit Umkehrfunktion** (wenn $x = g(y)$ gegeben ist):

$$V = \pi \int_c^d [g(y)]^2 \, dy$$

wobei $[c, d]$ das Intervall auf der $y$-Achse ist.

### Beispiel: Paraboloid

Gegeben: $f(x) = x^2$ für $x \in [0, 2]$, Rotation um die $y$-Achse.

Die Umkehrfunktion ist $g(y) = \sqrt{y}$ mit $y \in [0, 4]$.

$$V = \pi \int_0^4 (\sqrt{y})^2 \, dy = \pi \int_0^4 y \, dy = \pi \left[\frac{y^2}{2}\right]_0^4 = \pi \cdot 8 = 8\pi$$

---

## Rotation einer Fläche zwischen zwei Graphen

### Hohlkörper (Ringscheiben-Methode)

Rotiert die Fläche zwischen $f(x)$ (außen) und $g(x)$ (innen) um die $x$-Achse, entsteht ein **Hohlkörper**.

$$V = \pi \int_a^b \left([f(x)]^2 - [g(x)]^2\right) \, dx$$

```
    Querschnitt:
       ╭─────────╮  f(x)
      ╱           ╲
     │   ╭─────╮   │
     │   │     │   │  g(x)
     │   │     │   │
     │   ╰─────╯   │
      ╲           ╱
       ╰─────────╯
       Ringscheibe
```

### Beispiel: Hohlzylinder

Zwischen $f(x) = 3$ und $g(x) = 1$ im Intervall $[0, 5]$:

$$V = \pi \int_0^5 (3^2 - 1^2) \, dx = \pi \int_0^5 8 \, dx = \pi \cdot 8 \cdot 5 = 40\pi$$

**Kontrolle mit Zylinderformeln:**
$$V = \pi \cdot 3^2 \cdot 5 - \pi \cdot 1^2 \cdot 5 = 45\pi - 5\pi = 40\pi \checkmark$$

---

## Die Mantelmethode (Zylinderschalen)

Für die Rotation um die $y$-Achse kann alternativ die **Mantelmethode** verwendet werden:

$$V = 2\pi \int_a^b x \cdot f(x) \, dx$$

### Herleitung

Statt Scheiben betrachten wir dünne zylindrische Schalen:
- **Radius**: $x$
- **Höhe**: $f(x)$
- **Dicke**: $dx$
- **Volumen**: $dV = 2\pi x \cdot f(x) \cdot dx$

### Beispiel

Berechne das Volumen des Körpers, der durch Rotation von $f(x) = x^2$ im Intervall $[0, 1]$ um die $y$-Achse entsteht.

**Mit Mantelmethode:**

$$V = 2\pi \int_0^1 x \cdot x^2 \, dx = 2\pi \int_0^1 x^3 \, dx = 2\pi \left[\frac{x^4}{4}\right]_0^1 = 2\pi \cdot \frac{1}{4} = \frac{\pi}{2}$$

---

## Übersicht: Welche Formel wann?

| Situation | Methode | Formel |
|-----------|---------|--------|
| Rotation um x-Achse, $f(x)$ gegeben | Scheiben | $V = \pi \int_a^b [f(x)]^2 \, dx$ |
| Rotation um y-Achse, $x = g(y)$ gegeben | Scheiben | $V = \pi \int_c^d [g(y)]^2 \, dy$ |
| Rotation um y-Achse, $f(x)$ gegeben | Mantel | $V = 2\pi \int_a^b x \cdot f(x) \, dx$ |
| Hohlkörper, Rotation um x-Achse | Ringscheiben | $V = \pi \int_a^b ([f(x)]^2 - [g(x)]^2) \, dx$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Volumenberechnungen|Volumenberechnungen]] – Allgemeine Volumenberechnung mit Integralen
- → [[Flaechen-zwischen-Funktionsgraphen|Flächen zwischen Funktionsgraphen]] – Grundlage für Hohlkörper
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Mathematische Basis
- → [[Umkehrfunktionen|Umkehrfunktionen]] – Für Rotation um die y-Achse
- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Trägheitsmomente

> [!warning] **Prüfungsrelevant**
> - Merke: Bei Rotation um die x-Achse wird $[f(x)]^2$ integriert (nicht $f(x)$!)
> - Der Faktor $\pi$ steht **vor** dem Integral
> - Bei Hohlkörpern: "außen² minus innen²"
> - Wähle die Methode (Scheiben/Mantel) je nach Rotationsachse und gegebener Funktion

> [!question] **Typische Prüfungsfragen**
> - Berechne das Volumen des Körpers, der durch Rotation von $f(x) = \sqrt{x}$ im Intervall $[0, 4]$ um die $x$-Achse entsteht.
> - Welches Volumen hat der Körper, der durch Rotation der Fläche zwischen $f(x) = x$ und $g(x) = x^2$ um die $x$-Achse entsteht?
> - Erkläre den Unterschied zwischen der Scheiben- und der Mantelmethode.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Volumenberechnungen|Volumenberechnungen]] – Weitere Methoden zur Volumenberechnung
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Schwerpunkte und Trägheitsmomente von Rotationskörpern
