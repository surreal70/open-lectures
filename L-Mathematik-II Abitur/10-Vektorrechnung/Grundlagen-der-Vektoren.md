---
author: Andreas Hümmer
title: Grundlagen der Vektoren
tags:
  - content
  - mathe
  - vektorrechnung
  - grundlagen
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Grundlagen der Vektoren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff des Vektors als gerichtete Größe verstehen und von Skalaren unterscheiden können
> - Vektoren geometrisch als Pfeile interpretieren und zeichnen können
> - Die Begriffe Repräsentant, Gegenvektor und Nullvektor kennen
> - Vektoren in verschiedenen Anwendungskontexten identifizieren können

---

## Überblick

Vektoren sind mathematische Objekte, die sowohl einen Betrag (eine Größe) als auch eine Richtung besitzen. Im Gegensatz zu **Skalaren** – einfachen Zahlen wie Temperatur oder Masse – beschreiben Vektoren gerichtete Größen wie Geschwindigkeit, Kraft oder Verschiebung. Diese Eigenschaft macht sie zu einem unverzichtbaren Werkzeug in Physik, Technik und Geometrie.

## Was ist ein Vektor?

Ein **Vektor** ist eine Klasse aller Pfeile, die dieselbe Länge, dieselbe Richtung und denselben Orientierungssinn haben. Mathematisch präziser:

> Ein Vektor ist eine Äquivalenzklasse von gerichteten Strecken (Pfeilen), die durch Parallelverschiebung ineinander überführt werden können.

### Wichtige Begriffe

| Begriff | Erklärung |
|---------|-----------|
| **Repräsentant** | Ein konkreter Pfeil, der den Vektor darstellt |
| **Betrag** | Die Länge des Vektors, geschrieben als $\|\vec{a}\|$ |
| **Richtung** | Die Orientierung im Raum |
| **Anfangspunkt** | Der Startpunkt eines Repräsentanten |
| **Endpunkt** | Der Zielpunkt eines Repräsentanten |

### Notation

Vektoren werden üblicherweise durch einen Kleinbuchstaben mit Pfeil bezeichnet:

$$\vec{a}, \quad \vec{b}, \quad \vec{v}$$

In manchen Lehrbüchern und Anwendungen findet man auch die Fettschreibung: $\mathbf{a}, \mathbf{b}, \mathbf{v}$.

Ein Vektor vom Punkt $A$ zum Punkt $B$ wird als **Verbindungsvektor** geschrieben:

$$\vec{AB}$$

## Skalare und Vektoren im Vergleich

Der fundamentale Unterschied zwischen Skalaren und Vektoren liegt in der Richtungsinformation:

| Eigenschaft | Skalar | Vektor |
|-------------|--------|--------|
| Betrag | ✓ | ✓ |
| Richtung | ✗ | ✓ |
| Beispiele | Masse, Temperatur, Zeit | Kraft, Geschwindigkeit, Beschleunigung |
| Darstellung | Einfache Zahl | Pfeil oder Koordinatentupel |

**Beispiel:** Ein Auto fährt mit 50 km/h. Die **Geschwindigkeit** (Skalar) gibt nur an, wie schnell es fährt. Die **Geschwindigkeitsvektor** $\vec{v}$ gibt zusätzlich an, in welche Richtung es fährt.

## Besondere Vektoren

### Der Nullvektor

Der **Nullvektor** $\vec{0}$ ist der einzige Vektor mit Betrag 0:

$$|\vec{0}| = 0$$

Er hat keine definierte Richtung und ist zu sich selbst parallel. Der Nullvektor entsteht, wenn ein Punkt mit sich selbst verbunden wird:

$$\vec{AA} = \vec{0}$$

### Der Gegenvektor

Zu jedem Vektor $\vec{a}$ existiert ein **Gegenvektor** $-\vec{a}$, der:
- denselben Betrag hat: $|-\vec{a}| = |\vec{a}|$
- die entgegengesetzte Richtung hat

$$\vec{a} + (-\vec{a}) = \vec{0}$$

### Kollineare und parallele Vektoren

Zwei Vektoren heißen **kollinear** (oder parallel), wenn sie auf derselben Geraden oder auf parallelen Geraden liegen. Dies ist genau dann der Fall, wenn ein Vektor ein Vielfaches des anderen ist:

$$\vec{a} \parallel \vec{b} \Leftrightarrow \vec{a} = k \cdot \vec{b} \text{ für ein } k \in \mathbb{R}$$

## Geometrische Interpretation

Ein Vektor kann als **Verschiebung** interpretiert werden:

```
    B
    ↑
    |  → Vektor AB
    |
    A
```

Der Vektor $\vec{AB}$ beschreibt die Verschiebung, die den Punkt $A$ auf den Punkt $B$ abbildet. Diese Interpretation ist besonders nützlich bei:

- **Ortsveränderungen** in der Mechanik
- **Kraftwirkungen** in der Physik
- **Translationen** in der Geometrie

## Vektoren in der Praxis

### Physikalische Anwendungen

**Kraftvektoren:** Eine Kraft $\vec{F}$ wirkt in eine bestimmte Richtung mit einem bestimmten Betrag (in Newton).

**Geschwindigkeitsvektoren:** Die Geschwindigkeit $\vec{v}$ eines Körpers gibt sowohl die Schnelligkeit als auch die Bewegungsrichtung an.

### Beispiel: Navigation

Ein Flugzeug fliegt von München nach Hamburg. Der Flugvektor beschreibt:
- **Betrag:** Entfernung von ca. 610 km
- **Richtung:** Etwa 345° (fast genau nach Norden)

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Vektordarstellung]] — Verschiedene Darstellungsformen von Vektoren
- → [[Ortsvektoren]] — Beschreibung von Punkten durch Vektoren
- → [[Vektoraddition]] — Verknüpfung von Vektoren

> [!warning] **Prüfungsrelevant**
> - Unterscheidung zwischen Skalaren und Vektoren mit Beispielen
> - Definition und Eigenschaften des Nullvektors
> - Gegenvektor und seine Beziehung zum Originalvektor
> - Kriterium für Parallelität (Kollinearität) von Vektoren

> [!question] **Typische Prüfungsfragen**
> - Nenne drei physikalische Größen, die durch Vektoren beschrieben werden, und begründe, warum ein Skalar hier nicht ausreicht.
> - Erkläre den Unterschied zwischen einem Vektor und einem Repräsentanten.
> - Wann sind zwei Vektoren kollinear? Gib ein Beispiel mit konkreten Koordinaten.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[Vektordarstellung]] — Koordinatenschreibweise und Komponenten
> - [[02-Funktionen-und-ihre-Eigenschaften-Index|Funktionen und ihre Eigenschaften]] — Vektorfunktionen als Erweiterung
