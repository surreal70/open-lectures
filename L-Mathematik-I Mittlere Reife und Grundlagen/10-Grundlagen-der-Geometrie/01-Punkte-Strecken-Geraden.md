---
title: "Punkte, Strecken und Geraden"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "01"
status: "draft - review pending"
type: lecture
keywords:
  - Punkt
  - Strecke
  - Gerade
  - Strahl
  - Lagebeziehung
---

# Punkte, Strecken und Geraden

> [!info] Lernziele
> - Die geometrischen Grundobjekte kennen und unterscheiden
> - Lagebeziehungen zwischen Geraden beschreiben
> - Den Abstand korrekt definieren und berechnen
> - Die korrekte mathematische Notation verwenden

## Der Punkt

Ein **Punkt** ist das einfachste geometrische Objekt. Er hat:
- Keine Ausdehnung (keine Länge, Breite oder Höhe)
- Nur eine **Position**

### Bezeichnung

Punkte werden mit **Großbuchstaben** bezeichnet: $A$, $B$, $C$, $P$, $Q$, ...

```
         • A
    
    • B        • C
```

## Die Strecke

Eine **Strecke** ist die kürzeste Verbindung zwischen zwei Punkten.

### Eigenschaften

- Hat einen **Anfangs-** und einen **Endpunkt**
- Hat eine **begrenzte Länge**
- Ist **gerade** (keine Kurve)

### Bezeichnung

Die Strecke von $A$ nach $B$: $\overline{AB}$ oder $[AB]$

Die Länge der Strecke: $|\overline{AB}|$ oder einfach $AB$

```
    A •────────────• B
         Strecke AB
```

## Der Strahl (Halbgerade)

Ein **Strahl** hat:
- Einen **Anfangspunkt**
- Keine **Endpunkt** (geht ins Unendliche)

### Bezeichnung

Der Strahl von $A$ durch $B$: $\overrightarrow{AB}$

```
    A •────────────────────→
         Strahl AB
```

> [!note] Unterschied Strahl/Strecke
> - Strecke: zwei Endpunkte, endliche Länge
> - Strahl: ein Anfangspunkt, unendlich lang

## Die Gerade

Eine **Gerade** ist beidseitig unbegrenzt.

### Eigenschaften

- Kein Anfangs- oder Endpunkt
- Unendlich lang in beide Richtungen
- Durch **zwei Punkte** eindeutig bestimmt

### Bezeichnung

Die Gerade durch $A$ und $B$: $AB$ oder $g_{AB}$

Allgemein: kleine Buchstaben: $g$, $h$, $k$, ...

```
    ←────────•────────•────────→
             A        B
             Gerade g
```

## Übersicht: Grundobjekte

| Objekt | Anfang | Ende | Länge | Symbol |
|---|---|---|---|---|
| Punkt | – | – | 0 | $A$ |
| Strecke | ja | ja | endlich | $\overline{AB}$ |
| Strahl | ja | nein | unendlich | $\overrightarrow{AB}$ |
| Gerade | nein | nein | unendlich | $g$ |

## Lagebeziehungen zwischen Geraden

### Zwei Geraden in der Ebene

```
parallel:           schneidend:         identisch:
                    
g ─────────         g ─────╲            g ═══════
                           ╲
h ─────────         h ──────╳────       h ═══════
                            ╲
```

| Lagebeziehung | Beschreibung | Gemeinsame Punkte |
|---|---|---|
| **Parallel** | Gleiche Richtung, kein Schnittpunkt | 0 |
| **Schneidend** | Genau ein Schnittpunkt | 1 |
| **Identisch** | Dieselbe Gerade | unendlich viele |

### Senkrechte (orthogonale) Geraden

Zwei Geraden sind **senkrecht** (orthogonal), wenn sie sich im **rechten Winkel** (90°) schneiden.

Schreibweise: $g \perp h$

```
         g
         │
    ─────┼───── h
         │
```

### Parallele Geraden

Schreibweise: $g \parallel h$

Parallele Geraden haben überall denselben **Abstand**.

## Abstand

### Abstand zweier Punkte

Der Abstand ist die **Länge der Verbindungsstrecke**:

$$d(A, B) = |\overline{AB}|$$

### Abstand Punkt – Gerade

Der Abstand eines Punktes $P$ zu einer Geraden $g$ ist die **Länge des Lots** von $P$ auf $g$.

```
         P •
           │
           │ d (Lot)
           │
    ───────•────── g
         Fußpunkt F
```

### Abstand paralleler Geraden

Der Abstand paralleler Geraden ist der **Abstand eines beliebigen Punktes der einen Gerade zur anderen**.

## Mittelpunkt einer Strecke

Der **Mittelpunkt** $M$ einer Strecke $\overline{AB}$ teilt diese in zwei gleich lange Teile:

$$|\overline{AM}| = |\overline{MB}| = \frac{1}{2} |\overline{AB}|$$

Mit Koordinaten:
$$M = \left(\frac{x_A + x_B}{2}, \frac{y_A + y_B}{2}\right)$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Punkte haben nur Position, keine Ausdehnung
> - Strecken sind begrenzt durch zwei Endpunkte
> - Strahlen haben einen Anfangspunkt und sind einseitig unbegrenzt
> - Geraden sind beidseitig unbegrenzt
> - Geraden können parallel, schneidend oder identisch sein
> - Der Abstand ist immer die kürzeste Verbindung (senkrecht)

## Übungsaufgaben

1. Zeichne eine Strecke $\overline{AB}$ mit Länge 5 cm und bestimme ihren Mittelpunkt $M$.

2. Zeichne zwei parallele Geraden im Abstand von 2 cm.

3. Zeichne eine Gerade $g$ und einen Punkt $P$ außerhalb. Konstruiere das Lot von $P$ auf $g$.

4. Gegeben sind $A(1, 2)$ und $B(5, 6)$. Berechne:
   - Die Länge von $\overline{AB}$
   - Den Mittelpunkt $M$

5. Entscheide: Sind die folgenden Aussagen wahr oder falsch?
   - Jede Strecke ist Teil einer Geraden.
   - Zwei verschiedene Punkte bestimmen genau eine Gerade.
   - Eine Gerade enthält unendlich viele Punkte.

---

**Navigation**: [[00-Geometrie-Index|← Übersicht]] | [[02-Winkel-und-Winkelarten|Winkel →]]
