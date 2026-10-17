---
author: Andreas Hümmer
title: Einheitskreis
tags:
  - content
  - mathe
  - trigonometrie
  - einheitskreis
  - koordinaten
created: 2025-06-20
modified: 2025-06-20
---

# Einheitskreis

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Einheitskreis und seine Bedeutung für die Trigonometrie verstehen
> - Sinus und Kosinus als Koordinaten am Einheitskreis interpretieren können
> - Die Werte von Sinus und Kosinus für besondere Winkel ablesen können
> - Die Vorzeichen der Winkelfunktionen in den vier Quadranten kennen

---

## Überblick

Der **Einheitskreis** ist ein Kreis mit Radius $r = 1$ und Mittelpunkt im Koordinatenursprung. Er ist das zentrale Werkzeug zur Definition der trigonometrischen Funktionen für beliebige Winkel – nicht nur für spitze Winkel wie im rechtwinkligen Dreieck.

Am Einheitskreis werden Sinus und Kosinus als **Koordinaten** eines Punktes interpretiert, was ihre Eigenschaften besonders anschaulich macht.

## Definition des Einheitskreises

### Kreisgleichung

Der Einheitskreis ist die Menge aller Punkte $(x, y)$ mit:

$$x^2 + y^2 = 1$$

### Parametrisierung

Ein Punkt $P$ auf dem Einheitskreis, der durch Drehung um den Winkel $\alpha$ (im Bogenmaß, von der positiven $x$-Achse aus gemessen) erreicht wird, hat die Koordinaten:

$$P = (\cos(\alpha), \sin(\alpha))$$

## Sinus und Kosinus am Einheitskreis

### Geometrische Definition

Für einen Winkel $\alpha$ (gemessen von der positiven $x$-Achse gegen den Uhrzeigersinn):

- **Kosinus:** $x$-Koordinate des Punktes auf dem Einheitskreis
- **Sinus:** $y$-Koordinate des Punktes auf dem Einheitskreis

```
            y
            |
            |  P(cos α, sin α)
            | /
    sin α ──|/
            +────────── x
               cos α
```

### Der trigonometrische Pythagoras

Aus der Kreisgleichung $x^2 + y^2 = 1$ folgt unmittelbar:

$$\boxed{\sin^2(\alpha) + \cos^2(\alpha) = 1}$$

Diese fundamentale Identität gilt für **alle** Winkel $\alpha$.

## Besondere Winkel am Einheitskreis

### Die wichtigsten Funktionswerte

| $\alpha$ (Grad) | $\alpha$ (rad) | $\cos(\alpha)$ | $\sin(\alpha)$ |
|-----------------|----------------|----------------|----------------|
| $0°$ | $0$ | $1$ | $0$ |
| $30°$ | $\frac{\pi}{6}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ |
| $45°$ | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| $60°$ | $\frac{\pi}{3}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $90°$ | $\frac{\pi}{2}$ | $0$ | $1$ |
| $180°$ | $\pi$ | $-1$ | $0$ |
| $270°$ | $\frac{3\pi}{2}$ | $0$ | $-1$ |

### Merkregel für die Werte

Für die Winkel $0°, 30°, 45°, 60°, 90°$ gilt:

$$\sin(\alpha) = \frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$$

Das heißt:
- $\sin(0°) = 0$
- $\sin(30°) = \frac{1}{2}$
- $\sin(45°) = \frac{\sqrt{2}}{2}$
- $\sin(60°) = \frac{\sqrt{3}}{2}$
- $\sin(90°) = 1$

Für den Kosinus gilt dieselbe Reihe **rückwärts**.

## Die vier Quadranten

### Vorzeichen der Winkelfunktionen

Das Vorzeichen von Sinus und Kosinus hängt vom Quadranten ab:

| Quadrant | Winkelbereich | $\cos(\alpha)$ | $\sin(\alpha)$ |
|----------|---------------|----------------|----------------|
| I | $0° < \alpha < 90°$ | $+$ | $+$ |
| II | $90° < \alpha < 180°$ | $-$ | $+$ |
| III | $180° < \alpha < 270°$ | $-$ | $-$ |
| IV | $270° < \alpha < 360°$ | $+$ | $-$ |

### Merkregel: „All Students Take Calculus"

- **A**ll (I. Quadrant): Alle positiv
- **S**tudents (II. Quadrant): Nur Sinus positiv
- **T**ake (III. Quadrant): Nur Tangens positiv
- **C**alculus (IV. Quadrant): Nur Cosinus positiv

## Symmetrien am Einheitskreis

### Punktsymmetrie zum Ursprung

$$\sin(\alpha + \pi) = -\sin(\alpha)$$
$$\cos(\alpha + \pi) = -\cos(\alpha)$$

### Achsensymmetrie zur $y$-Achse (Kosinus)

$$\cos(-\alpha) = \cos(\alpha) \quad \text{(gerade Funktion)}$$

### Punktsymmetrie zum Ursprung (Sinus)

$$\sin(-\alpha) = -\sin(\alpha) \quad \text{(ungerade Funktion)}$$

### Komplementärwinkel

$$\sin\left(\frac{\pi}{2} - \alpha\right) = \cos(\alpha)$$
$$\cos\left(\frac{\pi}{2} - \alpha\right) = \sin(\alpha)$$

## Werte im II., III. und IV. Quadranten

### Reduktionsformeln

Um Funktionswerte für Winkel außerhalb des ersten Quadranten zu bestimmen:

**II. Quadrant ($90° < \alpha < 180°$):**
$$\sin(\pi - \alpha) = \sin(\alpha)$$
$$\cos(\pi - \alpha) = -\cos(\alpha)$$

**III. Quadrant ($180° < \alpha < 270°$):**
$$\sin(\pi + \alpha) = -\sin(\alpha)$$
$$\cos(\pi + \alpha) = -\cos(\alpha)$$

**IV. Quadrant ($270° < \alpha < 360°$):**
$$\sin(2\pi - \alpha) = -\sin(\alpha)$$
$$\cos(2\pi - \alpha) = \cos(\alpha)$$

### Beispiel

Berechne $\sin(150°)$:

$150° = 180° - 30°$, also im II. Quadrant.

$$\sin(150°) = \sin(180° - 30°) = \sin(30°) = \frac{1}{2}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Winkelmasse]] – Winkelmessung als Grundlage
- → [[Gradmass-und-Bogenmass]] – Umrechnung für den Einheitskreis
- → [[Sinus-und-Kosinus]] – Detaillierte Behandlung der Funktionen
- → [[Trigonometrische-Identitaeten]] – Identitäten aus dem Einheitskreis

> [!warning] **Prüfungsrelevant**
> - Die Koordinateninterpretation: $\cos(\alpha) = x$, $\sin(\alpha) = y$
> - Die Werte für $0°, 30°, 45°, 60°, 90°$ **auswendig** können
> - Die Vorzeichen in den vier Quadranten sicher beherrschen
> - Die fundamentale Identität $\sin^2(\alpha) + \cos^2(\alpha) = 1$

> [!question] **Typische Prüfungsfragen**
> - In welchem Quadranten liegt ein Winkel $\alpha$ mit $\sin(\alpha) < 0$ und $\cos(\alpha) > 0$?
> - Berechnen Sie $\sin(225°)$ ohne Taschenrechner.
> - Ein Punkt auf dem Einheitskreis hat die $x$-Koordinate $-\frac{1}{2}$. Welche möglichen $y$-Koordinaten gibt es?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett Verlag, 2019.

> [!tip] **Weiterführende Links**
> - [[Sinus-und-Kosinus]] – Funktionsgraphen und Eigenschaften
> - [[Tangens]] – Weitere trigonometrische Funktion
