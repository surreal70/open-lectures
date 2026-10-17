---
author: Andreas Hümmer
title: Volumenberechnungen mit Integralen
tags:
  - content
  - mathe
  - integralrechnung
  - volumen
  - anwendung
created: 2025-06-26
modified: 2025-06-26
---

# Volumenberechnungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Prinzip der Volumenberechnung durch Integration von Querschnittsflächen verstehen
> - Volumina von Körpern mit bekannter Querschnittsfunktion berechnen können
> - Die Cavalieri-Methode anwenden können
> - Verschiedene Körper durch geeignete Integrale beschreiben können

---

## Überblick

Die Integralrechnung ermöglicht die Berechnung von Volumina auch dann, wenn keine einfachen geometrischen Formeln existieren. Das Grundprinzip beruht auf dem **Cavalieri-Prinzip**: Ein Körper wird in unendlich viele, infinitesimal dünne Scheiben zerlegt, deren Flächen aufsummiert werden.

Diese Methode ist universell anwendbar und umfasst:
- Rotationskörper (Spezialfall mit kreisförmigem Querschnitt)
- Körper mit beliebigen Querschnittsflächen
- Körper mit veränderlichem Querschnitt

---

## Das Cavalieri-Prinzip

### Grundidee

Das **Cavalieri-Prinzip** (nach Bonaventura Cavalieri, 1598–1647) besagt:

> Haben zwei Körper in jeder Höhe gleich große Querschnittsflächen, so haben sie das gleiche Volumen.

### Volumenformel

Ist $A(x)$ die Querschnittsfläche eines Körpers senkrecht zur $x$-Achse an der Stelle $x$, so gilt:

$$V = \int_a^b A(x) \, dx$$

```
    y ↑
      │    A(x₁)     A(x₂)     A(x₃)
      │   ┌───┐    ┌─────┐   ┌───┐
      │   │   │    │     │   │   │
    ──┼───┴───┴────┴─────┴───┴───┴───→ x
      a    x₁       x₂        x₃    b
          dx       dx        dx
```

Das Volumen ergibt sich als Grenzwert der Summe:
$$V = \lim_{\Delta x \to 0} \sum_i A(x_i) \cdot \Delta x = \int_a^b A(x) \, dx$$

---

## Spezialfall: Rotationskörper

Bei einem Rotationskörper (Rotation um die $x$-Achse) ist der Querschnitt ein **Kreis** mit Radius $f(x)$:

$$A(x) = \pi \cdot [f(x)]^2$$

Damit ergibt sich die bekannte Formel:

$$V = \pi \int_a^b [f(x)]^2 \, dx$$

---

## Körper mit anderen Querschnitten

### Beispiel 1: Quadratischer Querschnitt

Ein Körper hat quadratische Querschnitte mit Seitenlänge $s(x) = 2\sqrt{x}$ für $x \in [0, 4]$.

**Querschnittsfläche:**
$$A(x) = [s(x)]^2 = [2\sqrt{x}]^2 = 4x$$

**Volumen:**
$$V = \int_0^4 4x \, dx = 4 \cdot \left[\frac{x^2}{2}\right]_0^4 = 4 \cdot 8 = 32$$

### Beispiel 2: Dreieckiger Querschnitt

Ein Körper hat gleichseitige dreieckige Querschnitte mit Seitenlänge $s(x) = x$ für $x \in [0, 3]$.

**Querschnittsfläche eines gleichseitigen Dreiecks:**
$$A(x) = \frac{\sqrt{3}}{4} \cdot [s(x)]^2 = \frac{\sqrt{3}}{4} \cdot x^2$$

**Volumen:**
$$V = \int_0^3 \frac{\sqrt{3}}{4} x^2 \, dx = \frac{\sqrt{3}}{4} \cdot \left[\frac{x^3}{3}\right]_0^3 = \frac{\sqrt{3}}{4} \cdot 9 = \frac{9\sqrt{3}}{4} \approx 3{,}90$$

### Beispiel 3: Halbkreisförmiger Querschnitt

Ein Körper hat halbkreisförmige Querschnitte mit Radius $r(x) = 1 - x^2$ für $x \in [-1, 1]$.

**Querschnittsfläche:**
$$A(x) = \frac{1}{2}\pi [r(x)]^2 = \frac{\pi}{2}(1 - x^2)^2$$

**Volumen:**
$$V = \frac{\pi}{2} \int_{-1}^{1} (1 - x^2)^2 \, dx = \frac{\pi}{2} \int_{-1}^{1} (1 - 2x^2 + x^4) \, dx$$

$$= \frac{\pi}{2} \left[x - \frac{2x^3}{3} + \frac{x^5}{5}\right]_{-1}^{1}$$

$$= \frac{\pi}{2} \cdot 2 \cdot \left(1 - \frac{2}{3} + \frac{1}{5}\right) = \pi \cdot \frac{8}{15} = \frac{8\pi}{15}$$

---

## Pyramide und Kegel

### Pyramide mit quadratischer Grundfläche

Eine Pyramide mit Höhe $h$ und quadratischer Grundfläche (Seitenlänge $a$).

**Querschnitt in Höhe $x$:**
$$s(x) = \frac{a}{h} \cdot x$$

$$A(x) = [s(x)]^2 = \frac{a^2}{h^2} \cdot x^2$$

**Volumen:**
$$V = \int_0^h \frac{a^2}{h^2} \cdot x^2 \, dx = \frac{a^2}{h^2} \cdot \frac{h^3}{3} = \frac{1}{3} a^2 h$$

Dies entspricht der bekannten Formel $V = \frac{1}{3} \cdot G \cdot h$ mit $G = a^2$. ✓

### Allgemeine Pyramide/Kegel

Für jede Pyramide oder jeden Kegel mit Grundfläche $G$ und Höhe $h$ gilt:

$$V = \frac{1}{3} \cdot G \cdot h$$

Dies lässt sich zeigen, indem man die Ähnlichkeit der Querschnitte nutzt: In Höhe $x$ ist der Querschnitt ähnlich zur Grundfläche mit Skalierungsfaktor $\frac{x}{h}$, also:

$$A(x) = G \cdot \left(\frac{x}{h}\right)^2$$

---

## Zusammengesetzte Körper

### Beispiel: Kugelsegment (Kugelkappe)

Eine Kugel mit Radius $R$ wird in Höhe $h$ geschnitten. Das Volumen der Kugelkappe ist:

Der Kugelquerschnitt bei $y$ ist ein Kreis mit Radius $r(y) = \sqrt{R^2 - y^2}$.

Für die Kappe von $y = R - h$ bis $y = R$:

$$V = \pi \int_{R-h}^{R} (R^2 - y^2) \, dy$$

$$= \pi \left[R^2 y - \frac{y^3}{3}\right]_{R-h}^{R}$$

Nach Ausrechnung erhält man:

$$V = \frac{\pi h^2}{3}(3R - h)$$

---

## Übersicht: Querschnittsformeln

| Querschnittsform | Fläche $A$ in Abhängigkeit von Länge/Radius |
|------------------|---------------------------------------------|
| Kreis | $A = \pi r^2$ |
| Quadrat | $A = s^2$ |
| Gleichseitiges Dreieck | $A = \frac{\sqrt{3}}{4} s^2$ |
| Rechteck (festes Seitenverhältnis $k$) | $A = k \cdot s^2$ |
| Halbkreis | $A = \frac{\pi}{2} r^2$ |
| Ellipse | $A = \pi a b$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Rotationskoerper|Rotationskörper]] – Spezialfall mit kreisförmigem Querschnitt
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Mathematische Grundlage
- → [[Flaechen-zwischen-Funktionsgraphen|Flächen zwischen Funktionsgraphen]] – Zur Bestimmung von Querschnittsflächen
- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Schwerpunkte und Trägheitsmomente
- → [[Flaechenberechnung|Flächenberechnung]] – Berechnung der Querschnittsflächen

> [!warning] **Prüfungsrelevant**
> - Das Cavalieri-Prinzip: $V = \int_a^b A(x) \, dx$
> - Bei Rotationskörpern: $A(x) = \pi [f(x)]^2$
> - Bei ähnlichen Querschnitten (Pyramide, Kegel): Skalierung mit Quadrat des Verhältnisses
> - Kenne die Flächenformeln für Kreis, Quadrat, Dreieck!

> [!question] **Typische Prüfungsfragen**
> - Ein Körper hat kreisförmige Querschnitte mit Radius $r(x) = e^{-x}$ für $x \in [0, 2]$. Berechne sein Volumen.
> - Erkläre das Cavalieri-Prinzip und wende es auf die Herleitung der Kugelvolumenformel an.
> - Ein Körper hat quadratische Querschnitte, deren Diagonale durch die Parabel $y = 4 - x^2$ begrenzt wird. Berechne das Volumen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Rotationskoerper|Rotationskörper]] – Vertiefung für Drehkörper
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Praktische Anwendungen
