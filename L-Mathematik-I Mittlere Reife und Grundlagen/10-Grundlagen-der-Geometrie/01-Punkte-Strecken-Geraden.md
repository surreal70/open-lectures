---
title: "Punkte, Strecken und Geraden"
created: 2026-10-13
modified: 2025-01-20
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

---

## Einführung

Punkte, Strecken und Geraden sind die **Grundbausteine der Geometrie** – ähnlich wie Buchstaben für die Sprache oder Atome für die Chemie. Alle komplexeren Figuren wie Dreiecke, Kreise oder Würfel lassen sich auf diese einfachen Elemente zurückführen.

Bereits **Euklid** definierte in seinen „Elementen" (ca. 300 v. Chr.) diese Grundbegriffe – allerdings auf philosophische Weise: „Ein Punkt ist, was keine Teile hat. Eine Linie ist Länge ohne Breite." Diese Definitionen zeigen, dass Punkte und Linien **Idealisierungen** sind: Ein gezeichneter Punkt hat immer eine gewisse Ausdehnung, aber in der Mathematik denken wir ihn uns unendlich klein.

> [!note] **Vom Konkreten zum Abstrakten**
> In der realen Welt gibt es keine perfekten Punkte oder Geraden. Jeder Stift hinterlässt eine Spur mit Breite, jedes Lineal hat minimale Unebenheiten. Die mathematischen Objekte sind ideale Modelle, die uns erlauben, präzise zu rechnen.

---

## Der Punkt

Ein **Punkt** ist das einfachste geometrische Objekt. Er hat:
- Keine Ausdehnung (keine Länge, Breite oder Höhe)
- Nur eine **Position**

In der Praxis markieren wir Punkte durch kleine Kreuze oder Punkte – diese sind natürlich größer als „nichts", aber sie repräsentieren eine exakte Position im Raum.

### Bezeichnung

Punkte werden mit **Großbuchstaben** bezeichnet: $A$, $B$, $C$, $P$, $Q$, ...

```
         • A
    
    • B        • C
```

> [!tip] **Koordinaten geben Punkten eine Adresse**
> Im [[01-Kartesisches-Koordinatensystem|Koordinatensystem]] erhält jeder Punkt eine eindeutige „Adresse" durch seine Koordinaten, z.B. $P(3, 2)$. So können wir Punkte nicht nur benennen, sondern auch rechnerisch verarbeiten.

---

## Die Strecke

Eine **Strecke** ist die kürzeste Verbindung zwischen zwei Punkten.

### Eigenschaften

- Hat einen **Anfangs-** und einen **Endpunkt**
- Hat eine **begrenzte Länge**
- Ist **gerade** (keine Kurve)

Im Alltag begegnen uns Strecken überall: Die Kante eines Tisches, der Rand eines Blattes Papier, ein gespanntes Seil zwischen zwei Pfosten – all das sind (annähernd) Strecken.

### Bezeichnung

Die Strecke von $A$ nach $B$: $\overline{AB}$ oder $[AB]$

Die Länge der Strecke: $|\overline{AB}|$ oder einfach $AB$

```
    A •────────────• B
         Strecke AB
```

> [!note] **Warum ist die Strecke „die kürzeste Verbindung"?**
> Dies ist ein Grundsatz der euklidischen Geometrie: Zwischen zwei Punkten gibt es unendlich viele Wege, aber nur einer ist der kürzeste – die gerade Verbindung. In der Praxis nutzen wir dieses Prinzip unbewusst, wenn wir „Abkürzungen" nehmen.

---

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

Wenn wir zwei Geraden in einer Ebene betrachten, gibt es genau drei Möglichkeiten, wie sie zueinander liegen können. Das Verständnis dieser Lagebeziehungen ist fundamental für viele geometrische Beweise und Konstruktionen.

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

> [!note] **Parallelität im Alltag**
> Parallele Geraden begegnen uns täglich: Eisenbahnschienen, die Linien auf einem Collegeblock, gegenüberliegende Kanten eines Rechtecks. In der euklidischen Geometrie treffen sich parallele Geraden niemals – auch wenn sie ins Unendliche verlängert werden.

### Senkrechte (orthogonale) Geraden

Zwei Geraden sind **senkrecht** (orthogonal), wenn sie sich im **rechten Winkel** (90°) schneiden.

Schreibweise: $g \perp h$

```
         g
         │
    ─────┼───── h
         │
```

Senkrechte Geraden spielen eine besondere Rolle in Architektur und Technik: Wände stehen senkrecht zum Boden, Fensterrahmen haben rechte Winkel, Koordinatenachsen stehen senkrecht aufeinander.

### Parallele Geraden

Schreibweise: $g \parallel h$

Parallele Geraden haben überall denselben **Abstand**.

> [!tip] **Parallelität prüfen**
> Zwei Geraden sind parallel, wenn sie mit einer dritten Geraden (Transversale) gleich große [[03-Winkelberechnungen|Stufenwinkel oder Wechselwinkel]] bilden.

## Abstand

Der Begriff „Abstand" ist zentral in der Geometrie und bedeutet immer: die **kürzeste Entfernung**. Diese kürzeste Entfernung verläuft stets senkrecht.

### Abstand zweier Punkte

Der Abstand ist die **Länge der Verbindungsstrecke**:

$$d(A, B) = |\overline{AB}|$$

Im [[01-Kartesisches-Koordinatensystem|Koordinatensystem]] kann der Abstand mit dem [[02-Satz-des-Pythagoras|Satz des Pythagoras]] berechnet werden:

$$d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

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

> [!warning] **Häufiger Fehler**
> Der Abstand eines Punktes zu einer Geraden ist **nicht** der Abstand zu irgendeinem Punkt auf der Geraden, sondern immer der kürzeste Abstand – und der verläuft senkrecht!

### Abstand paralleler Geraden

Der Abstand paralleler Geraden ist der **Abstand eines beliebigen Punktes der einen Gerade zur anderen**.

Da parallele Geraden überall den gleichen Abstand haben, kann man jeden beliebigen Punkt wählen – das Ergebnis ist immer dasselbe.

---

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

## Zusammenhänge

Diese Grundbegriffe bilden das Fundament für alle weiteren geometrischen Themen:

- → [[02-Winkel-und-Winkelarten|Winkel]] entstehen, wenn sich zwei Strahlen in einem Punkt treffen
- → [[03-Winkelberechnungen|Winkelberechnungen]] nutzen Lagebeziehungen bei parallelen Geraden
- → [[04-Dreiecke|Dreiecke]] werden durch drei Punkte definiert, die nicht auf einer Geraden liegen
- → [[12-Geometrische-Konstruktionen|Konstruktionen]] verwenden Geraden und deren Schnittpunkte
- → [[01-Kartesisches-Koordinatensystem|Koordinatensysteme]] ermöglichen die rechnerische Behandlung von Punkten und Geraden

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
