---
author: Andreas Hümmer
title: Winkelmaße
tags:
  - content
  - mathe
  - trigonometrie
  - winkel
  - winkelmaße
created: 2025-06-20
modified: 2025-06-20
---

# Winkelmaße

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verschiedene Winkelmaße kennen und unterscheiden können
> - Den Zusammenhang zwischen Winkel und Drehung verstehen
> - Winkel in verschiedenen Kontexten (Geometrie, Analysis) einordnen können
> - Negative Winkel und Winkel größer als 360° interpretieren können

---

## Überblick

Winkelmaße sind fundamentale Größen in der Mathematik, die zur Beschreibung von Drehungen und Richtungen dienen. In der Schulmathematik begegnen uns hauptsächlich zwei Systeme: das **Gradmaß** und das **Bogenmaß**. Beide beschreiben denselben geometrischen Sachverhalt – einen Winkel – auf unterschiedliche Weise.

Das Verständnis verschiedener Winkelmaße ist essentiell für die gesamte Trigonometrie und bildet die Grundlage für das Arbeiten mit trigonometrischen Funktionen, insbesondere in der Analysis.

## Der Winkelbegriff

### Geometrische Definition

Ein **Winkel** wird durch zwei Halbgeraden (Strahlen) gebildet, die einen gemeinsamen Anfangspunkt, den **Scheitelpunkt**, besitzen. Die beiden Halbgeraden heißen **Schenkel** des Winkels.

```
           /
          /
         /  α
        ·--------
   Scheitelpunkt
```

### Winkel als Drehung

Für die Trigonometrie ist es vorteilhaft, einen Winkel als **Drehung** aufzufassen:

- Ein Winkel beschreibt die Drehung eines Strahls um den Scheitelpunkt
- Der **Anfangsschenkel** (Ausgangsstrahl) wird auf den **Endschenkel** gedreht
- Die Drehrichtung bestimmt das Vorzeichen des Winkels

**Konvention:**
- Drehung gegen den Uhrzeigersinn: **positiver Winkel**
- Drehung im Uhrzeigersinn: **negativer Winkel**

## Winkelarten nach Größe

Winkel werden nach ihrer Größe klassifiziert:

| Winkelart | Größe | Beschreibung |
|-----------|-------|--------------|
| Nullwinkel | $0°$ | Beide Schenkel fallen zusammen |
| Spitzer Winkel | $0° < \alpha < 90°$ | Kleiner als ein rechter Winkel |
| Rechter Winkel | $90°$ | Ein Viertel einer Volldrehung |
| Stumpfer Winkel | $90° < \alpha < 180°$ | Größer als rechter Winkel |
| Gestreckter Winkel | $180°$ | Halbe Drehung, Halbgerade |
| Überstumpfer Winkel | $180° < \alpha < 360°$ | Größer als gestreckt |
| Vollwinkel | $360°$ | Vollständige Drehung |

## Besondere Winkelpaare

### Nebenwinkel

Zwei Winkel heißen **Nebenwinkel**, wenn sie einen gemeinsamen Schenkel haben und die anderen beiden Schenkel eine Gerade bilden.

$$\alpha + \beta = 180°$$

### Scheitelwinkel

**Scheitelwinkel** entstehen, wenn sich zwei Geraden schneiden. Sie liegen sich am Schnittpunkt gegenüber und sind stets gleich groß:

$$\alpha = \gamma \quad \text{und} \quad \beta = \delta$$

### Stufenwinkel und Wechselwinkel

Bei parallelen Geraden, die von einer dritten Geraden geschnitten werden:

- **Stufenwinkel** (F-Winkel): gleich groß
- **Wechselwinkel** (Z-Winkel): gleich groß

## Winkel im Koordinatensystem

Im kartesischen Koordinatensystem wird ein Winkel standardmäßig wie folgt gemessen:

1. Der **Anfangsschenkel** liegt auf der positiven $x$-Achse
2. Der **Scheitelpunkt** liegt im Ursprung
3. Der Winkel wird von der positiven $x$-Achse aus gemessen

Diese Standardposition ist fundamental für die Definition der trigonometrischen Funktionen am Einheitskreis.

### Beispiele für Winkellagen

| Winkel | Quadrant | Lage |
|--------|----------|------|
| $30°$ | I. Quadrant | Zwischen $x$- und $y$-Achse |
| $120°$ | II. Quadrant | Links oben |
| $210°$ | III. Quadrant | Links unten |
| $300°$ | IV. Quadrant | Rechts unten |

## Winkel größer als 360° und negative Winkel

In der Trigonometrie sind auch Winkel außerhalb des Intervalls $[0°, 360°)$ sinnvoll:

**Winkel größer als 360°:** Entsprechen mehrfachen Umdrehungen

$$720° = 2 \cdot 360° = \text{zwei volle Umdrehungen}$$

**Negative Winkel:** Drehung im Uhrzeigersinn

$$-90° = 270° \quad \text{(bezüglich Position im Koordinatensystem)}$$

### Koterminalwinkel

Zwei Winkel heißen **koterminal**, wenn ihre Endschenkel in derselben Position liegen:

$$\alpha \text{ und } \beta \text{ sind koterminal} \Leftrightarrow \alpha - \beta = k \cdot 360°, \quad k \in \mathbb{Z}$$

**Beispiel:** Die Winkel $30°$, $390°$ und $-330°$ sind koterminal.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Gradmass-und-Bogenmass]] – Die beiden wichtigsten Winkelmaßsysteme
- → [[Einheitskreis]] – Winkel am Einheitskreis definieren
- → [[Sinus-und-Kosinus]] – Trigonometrische Funktionen basieren auf Winkelmessung
- → [[Periodische-Vorgaenge]] – Winkel und periodische Phänomene

> [!warning] **Prüfungsrelevant**
> - Unterscheidung zwischen positivem (gegen Uhrzeigersinn) und negativem Winkel (im Uhrzeigersinn)
> - Winkel größer als $360°$ auf Winkel im Intervall $[0°, 360°)$ reduzieren können
> - Winkelbeziehungen bei Parallelenschnitt (Stufen- und Wechselwinkel)
> - Standardposition eines Winkels im Koordinatensystem kennen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie den Quadranten, in dem der Endschenkel eines Winkels von $245°$ liegt.
> - Welcher Winkel im Intervall $[0°, 360°)$ ist koterminal zu $-150°$?
> - Zwei Geraden schneiden sich. Ein Winkel beträgt $72°$. Wie groß sind die übrigen drei Winkel?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Gradmass-und-Bogenmass]] – Vertiefte Behandlung der Winkelmaßsysteme
> - [[Einheitskreis]] – Anwendung der Winkelmessung
