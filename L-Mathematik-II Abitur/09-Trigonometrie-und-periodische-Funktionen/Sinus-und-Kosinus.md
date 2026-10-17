---
author: Andreas Hümmer
title: Sinus und Kosinus
tags:
  - content
  - mathe
  - trigonometrie
  - sinus
  - kosinus
  - winkelfunktionen
created: 2025-06-20
modified: 2025-06-20
---

# Sinus und Kosinus

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Sinus und Kosinus im rechtwinkligen Dreieck und am Einheitskreis definieren können
> - Die Funktionsgraphen von Sinus und Kosinus skizzieren können
> - Die wichtigsten Eigenschaften (Periodizität, Symmetrie, Wertebereich) kennen
> - Funktionswerte besonderer Winkel ohne Taschenrechner angeben können

---

## Überblick

**Sinus** und **Kosinus** sind die fundamentalen trigonometrischen Funktionen. Sie haben ihren Ursprung in der Geometrie des rechtwinkligen Dreiecks, entfalten aber ihre volle Bedeutung erst durch die Definition am Einheitskreis. Als periodische Funktionen sind sie unverzichtbar für die Beschreibung von Schwingungen und Wellen in Physik und Technik.

## Definition im rechtwinkligen Dreieck

### Bezeichnungen

In einem rechtwinkligen Dreieck mit dem rechten Winkel bei $C$ bezeichnet man für einen spitzen Winkel $\alpha$:

- **Ankathete:** Die am Winkel $\alpha$ anliegende Kathete
- **Gegenkathete:** Die dem Winkel $\alpha$ gegenüberliegende Kathete
- **Hypotenuse:** Die dem rechten Winkel gegenüberliegende Seite (längste Seite)

### Definition für spitze Winkel

$$\sin(\alpha) = \frac{\text{Gegenkathete}}{\text{Hypotenuse}} = \frac{a}{c}$$

$$\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}} = \frac{b}{c}$$

```
         C
         |\
         | \
       a |  \ c (Hypotenuse)
         |   \
         |____\ 
         B  b  A
              α
```

### Merkregel: GAGA-HAHA

- **G**egenkathete durch **H**ypotenuse = **S**inus  
- **A**nkathete durch **H**ypotenuse = **C**osinus

Oder kurz: „**G**eh **A**uf die **H**ohe **A**chse" (für Sinus: Gegenkathete auf Hypotenuse)

## Definition am Einheitskreis

Die allgemeinere Definition erfolgt über den Einheitskreis (siehe [[Einheitskreis]]):

Für einen Punkt $P$ auf dem Einheitskreis, der zum Winkel $\alpha$ gehört:

$$\cos(\alpha) = x\text{-Koordinate von } P$$
$$\sin(\alpha) = y\text{-Koordinate von } P$$

Diese Definition erweitert Sinus und Kosinus auf **alle reellen Zahlen** als Argument.

## Funktionsgraphen

### Der Sinusgraph

Die Sinusfunktion $f(x) = \sin(x)$ (mit $x$ im Bogenmaß):

```
  y
  1 |     *           *
    |   *   *       *   *
  0 +--*-----*-----*-----*---> x
    |         *   *
 -1 |           *
    0    π/2   π   3π/2  2π
```

### Der Kosinusgraph

Die Kosinusfunktion $f(x) = \cos(x)$:

```
  y
  1 |*           *           *
    | *         * *         *
  0 +--*-------*---*-------*---> x
    |   *     *     *     *
 -1 |     * *         * *
    0    π/2   π   3π/2  2π
```

### Zusammenhang der Graphen

Der Kosinusgraph ist der um $\frac{\pi}{2}$ nach links verschobene Sinusgraph:

$$\cos(x) = \sin\left(x + \frac{\pi}{2}\right)$$

## Eigenschaften

### Definitionsbereich und Wertebereich

| Eigenschaft | Sinus | Kosinus |
|-------------|-------|---------|
| Definitionsbereich | $\mathbb{R}$ | $\mathbb{R}$ |
| Wertebereich | $[-1, 1]$ | $[-1, 1]$ |

### Periodizität

Beide Funktionen sind **periodisch** mit der Periode $2\pi$:

$$\sin(x + 2\pi) = \sin(x) \quad \text{für alle } x \in \mathbb{R}$$
$$\cos(x + 2\pi) = \cos(x) \quad \text{für alle } x \in \mathbb{R}$$

Die **kleinste positive Periode** ist $T = 2\pi$.

### Symmetrie

**Kosinus** ist eine **gerade Funktion** (achsensymmetrisch zur $y$-Achse):
$$\cos(-x) = \cos(x)$$

**Sinus** ist eine **ungerade Funktion** (punktsymmetrisch zum Ursprung):
$$\sin(-x) = -\sin(x)$$

### Nullstellen

**Sinus:** $\sin(x) = 0$ für $x = k\pi$, $k \in \mathbb{Z}$

Das heißt: $x \in \{..., -2\pi, -\pi, 0, \pi, 2\pi, 3\pi, ...\}$

**Kosinus:** $\cos(x) = 0$ für $x = \frac{\pi}{2} + k\pi$, $k \in \mathbb{Z}$

Das heißt: $x \in \{..., -\frac{3\pi}{2}, -\frac{\pi}{2}, \frac{\pi}{2}, \frac{3\pi}{2}, ...\}$

### Extremwerte

**Sinus:**
- Maximum: $\sin(x) = 1$ bei $x = \frac{\pi}{2} + 2k\pi$
- Minimum: $\sin(x) = -1$ bei $x = -\frac{\pi}{2} + 2k\pi$

**Kosinus:**
- Maximum: $\cos(x) = 1$ bei $x = 2k\pi$
- Minimum: $\cos(x) = -1$ bei $x = \pi + 2k\pi$

## Wichtige Funktionswerte

Diese Werte sollten **auswendig** beherrscht werden:

| $x$ (rad) | $x$ (Grad) | $\sin(x)$ | $\cos(x)$ |
|-----------|------------|-----------|-----------|
| $0$ | $0°$ | $0$ | $1$ |
| $\frac{\pi}{6}$ | $30°$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $\frac{\pi}{4}$ | $45°$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| $\frac{\pi}{3}$ | $60°$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ |
| $\frac{\pi}{2}$ | $90°$ | $1$ | $0$ |
| $\pi$ | $180°$ | $0$ | $-1$ |
| $\frac{3\pi}{2}$ | $270°$ | $-1$ | $0$ |

## Ableitung und Stammfunktion

Die Ableitungen (nur im **Bogenmaß** gültig!):

$$\frac{d}{dx}\sin(x) = \cos(x)$$
$$\frac{d}{dx}\cos(x) = -\sin(x)$$

Die Stammfunktionen:

$$\int \sin(x) \, dx = -\cos(x) + C$$
$$\int \cos(x) \, dx = \sin(x) + C$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Einheitskreis]] – Geometrische Definition
- → [[Tangens]] – Quotient aus Sinus und Kosinus
- → [[Trigonometrische-Identitaeten]] – Beziehungen zwischen den Funktionen
- → [[Sinus--und-Kosinusfunktionen]] – Allgemeine Sinusfunktionen mit Parametern

> [!warning] **Prüfungsrelevant**
> - Die Werte für $0°$, $30°$, $45°$, $60°$, $90°$ **auswendig** können
> - Die Graphen skizzieren können (Nullstellen, Extrema, Wendepunkte)
> - Die Ableitungsregeln $(\sin)' = \cos$ und $(\cos)' = -\sin$ sicher anwenden
> - Symmetrieeigenschaften (gerade/ungerade) für Vereinfachungen nutzen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle Nullstellen von $f(x) = \sin(x)$ im Intervall $[0, 4\pi]$.
> - Skizzieren Sie den Graphen von $f(x) = \cos(x)$ und geben Sie Periode, Wertebereich und Symmetrie an.
> - Berechnen Sie $\sin(150°)$ ohne Taschenrechner.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett Verlag, 2019.

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Gleichungen]] – Gleichungen mit Sinus und Kosinus lösen
> - [[Phasenverschiebung]] – Verschiebung der Graphen
