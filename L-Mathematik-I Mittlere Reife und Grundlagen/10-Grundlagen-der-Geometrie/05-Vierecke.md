---
title: "Vierecke"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "05"
status: "draft - review pending"
type: lecture
keywords:
  - Viereck
  - Quadrat
  - Rechteck
  - Parallelogramm
  - Trapez
---

# Vierecke

> [!info] Lernziele
> - Die verschiedenen Vierecktypen und ihre Eigenschaften kennen
> - Die Innenwinkelsumme anwenden
> - Hierarchie der Vierecke verstehen
> - Vierecke anhand ihrer Eigenschaften identifizieren

## Allgemeines Viereck

Ein **Viereck** ist eine geschlossene Figur mit vier Seiten und vier Ecken.

### Bezeichnung

```
    D ●────────────● C
     ╱              ╲
    ╱                ╲
   ╱                  ╲
  ●────────────────────●
  A                     B
```

- Eckpunkte: $A$, $B$, $C$, $D$ (gegen den Uhrzeigersinn)
- Seiten: $a = \overline{AB}$, $b = \overline{BC}$, $c = \overline{CD}$, $d = \overline{DA}$
- Diagonalen: $e = \overline{AC}$, $f = \overline{BD}$

### Innenwinkelsumme

> [!warning] Satz
> Die Summe der Innenwinkel eines Vierecks beträgt immer **360°**:
> $$\alpha + \beta + \gamma + \delta = 360°$$

## Spezielle Vierecke

### Das Quadrat

Das **Quadrat** ist das regelmäßigste Viereck.

**Eigenschaften**:
- Alle vier Seiten gleich lang: $a = b = c = d$
- Alle vier Winkel sind rechte Winkel: $\alpha = \beta = \gamma = \delta = 90°$
- Diagonalen gleich lang, halbieren sich rechtwinklig
- Achsensymmetrisch (4 Achsen), punktsymmetrisch

```
    ┌────────┐
    │        │
    │        │
    │        │
    └────────┘
```

### Das Rechteck

**Eigenschaften**:
- Gegenüberliegende Seiten gleich lang: $a = c$, $b = d$
- Alle Winkel rechte Winkel: $90°$
- Diagonalen gleich lang, halbieren sich
- Achsensymmetrisch (2 Achsen), punktsymmetrisch

```
    ┌────────────────┐
    │                │
    │                │
    └────────────────┘
```

### Das Parallelogramm

**Eigenschaften**:
- Gegenüberliegende Seiten parallel und gleich lang
- Gegenüberliegende Winkel gleich groß
- Benachbarte Winkel ergeben zusammen 180°
- Diagonalen halbieren sich
- Punktsymmetrisch

```
        ┌─────────────┐
       ╱             ╱
      ╱             ╱
     └─────────────┘
```

### Die Raute (Rhombus)

**Eigenschaften**:
- Alle vier Seiten gleich lang: $a = b = c = d$
- Gegenüberliegende Winkel gleich groß
- Diagonalen halbieren sich rechtwinklig
- Achsensymmetrisch (2 Achsen), punktsymmetrisch

```
        ◇
       ╱ ╲
      ╱   ╲
     ╱     ╲
    ◇       ◇
     ╲     ╱
      ╲   ╱
       ╲ ╱
        ◇
```

### Das Trapez

**Eigenschaften**:
- Genau ein Paar paralleler Seiten
- Die parallelen Seiten heißen **Grundseiten**
- Die anderen heißen **Schenkel**

```
      ┌────────┐
     ╱          ╲
    ╱            ╲
   └──────────────┘
```

### Das gleichschenklige Trapez

**Eigenschaften**:
- Ein Paar paralleler Seiten
- Die Schenkel sind gleich lang
- Die Basiswinkel sind gleich groß
- Achsensymmetrisch (1 Achse)

### Der Drachen

**Eigenschaften**:
- Zwei Paare benachbarter Seiten sind gleich lang
- Eine Diagonale ist Symmetrieachse
- Die Diagonalen stehen senkrecht aufeinander
- Achsensymmetrisch (1 Achse)

```
        ◇
       ╱ ╲
      ╱   ╲
     ╱     ╲
    ◇───────◇
      ╲   ╱
       ╲ ╱
        ◇
```

## Hierarchie der Vierecke

```
                    Viereck
                       │
           ┌───────────┼───────────┐
           │           │           │
        Trapez    Parallelogramm  Drachen
           │           │           │
    gleichschenkliges  │           │
        Trapez    ┌────┴────┐      │
                  │         │      │
              Rechteck    Raute────┘
                  │         │
                  └────┬────┘
                       │
                    Quadrat
```

> [!note] Vererbung
> Ein Quadrat ist ein spezielles Rechteck und eine spezielle Raute.
> Ein Rechteck ist ein spezielles Parallelogramm.

## Übersichtstabelle

| Viereck | Seiten | Winkel | Diagonalen |
|---|---|---|---|
| Quadrat | alle gleich | alle 90° | gleich lang, ⊥, halbieren sich |
| Rechteck | je 2 gleich | alle 90° | gleich lang, halbieren sich |
| Raute | alle gleich | je 2 gleich | ⊥, halbieren sich |
| Parallelogramm | je 2 gleich | je 2 gleich | halbieren sich |
| Trapez | - | - | - |
| Drachen | je 2 benachbarte gleich | 1 Paar gleich | ⊥ |

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Innenwinkelsumme im Viereck beträgt 360°
> - Quadrat: alle Seiten gleich, alle Winkel 90°
> - Rechteck: rechte Winkel, gegenüberliegende Seiten gleich
> - Parallelogramm: gegenüberliegende Seiten parallel und gleich
> - Raute: alle Seiten gleich (wie Quadrat, aber ohne rechte Winkel)
> - Trapez: genau ein Paar paralleler Seiten
> - Vierecke bilden eine Hierarchie von allgemein zu speziell

## Übungsaufgaben

1. Bestimme den fehlenden Winkel im Viereck:
   - $\alpha = 80°$, $\beta = 100°$, $\gamma = 70°$
   - In einem Parallelogramm ist $\alpha = 65°$

2. Welches Viereck hat diese Eigenschaften?
   - Alle Seiten gleich lang, keine rechten Winkel
   - Alle Winkel 90°, alle Seiten gleich lang
   - Genau ein Paar paralleler Seiten, Schenkel gleich lang

3. Ein Rechteck hat die Seitenlängen 6 cm und 8 cm. Wie lang sind die Diagonalen?

4. Beweise: In einem Parallelogramm sind die gegenüberliegenden Winkel gleich groß.

5. Zeichne:
   - Ein Quadrat mit Seitenlänge 4 cm
   - Eine Raute mit Diagonalen 6 cm und 4 cm
   - Ein Trapez mit parallelen Seiten 8 cm und 4 cm

---

**Navigation**: [[04-Dreiecke|← Dreiecke]] | [[00-Geometrie-Index|Übersicht]] | [[06-Kreise|Kreise →]]
