---
title: "Das kartesische Koordinatensystem"
created: 2026-10-13
modified: 2025-07-18
chapter: "09"
section: "01"
status: "draft - review pending"
type: lecture
keywords:
  - Koordinatensystem
  - Achsen
  - Ursprung
  - Quadranten
  - René Descartes
---

# Das kartesische Koordinatensystem

> [!info] Lernziele
> - Das kartesische Koordinatensystem verstehen und beschreiben können
> - Die Bestandteile (Achsen, Ursprung, Quadranten) benennen können
> - Ein Koordinatensystem korrekt zeichnen und beschriften
> - Die historische Bedeutung kennen

## Historischer Hintergrund

Das kartesische Koordinatensystem ist nach dem französischen Mathematiker und Philosophen **René Descartes** (1596–1650) benannt. Die lateinische Form seines Namens lautet „Cartesius", daher „kartesisch".

Der Legende nach kam Descartes auf diese Idee, als er im Bett lag und eine Fliege an der Zimmerdecke beobachtete. Er fragte sich: Wie könnte man die Position dieser Fliege exakt beschreiben? Seine Antwort war genial einfach – durch zwei Zahlen, die den Abstand zu zwei senkrechten Wänden angeben.

> [!note] Historische Bedeutung
> Descartes gelang mit diesem System die Verbindung von **Geometrie** und **Algebra**. Geometrische Formen können nun durch Gleichungen beschrieben werden – die Geburt der analytischen Geometrie.
>
> Diese Verbindung war revolutionär: Vor Descartes waren Geometrie (das Studium von Formen und Räumen) und Algebra (das Rechnen mit Unbekannten) völlig getrennte Disziplinen. Nach ihm konnte man einen Kreis sowohl zeichnen als auch durch eine Gleichung wie $x^2 + y^2 = r^2$ beschreiben.

> [!tip] **Warum ist das wichtig?**
> Das Koordinatensystem ist heute allgegenwärtig: GPS-Navigation, Computergrafik, Architekturpläne, medizinische Bildgebung (CT, MRT) – all das basiert auf Descartes' Idee, Positionen durch Zahlenpaare zu beschreiben.

## Aufbau des Koordinatensystems

### Die Koordinatenachsen

Das kartesische Koordinatensystem besteht aus zwei **senkrecht aufeinander stehenden** Zahlengeraden:

```
          y
          ↑
          │
          │      Positive y-Werte
          │
──────────┼──────────→ x
   Neg.   │   Positive x-Werte
   x-Werte│
          │      Negative y-Werte
          │
```

| Achse | Name | Richtung |
|---|---|---|
| Horizontal | **x-Achse** (Abszisse) | Nach rechts positiv |
| Vertikal | **y-Achse** (Ordinate) | Nach oben positiv |

### Der Ursprung

Der **Ursprung** (auch **Nullpunkt**) ist der Schnittpunkt beider Achsen. Er hat die Koordinaten $(0, 0)$.

### Die vier Quadranten

Das Koordinatensystem wird durch die Achsen in vier Bereiche geteilt:

```
          y
          ↑
    II    │    I
          │
  (−,+)   │  (+,+)
──────────┼──────────→ x
  (−,−)   │  (+,−)
          │
   III    │    IV
```

| Quadrant | x-Werte | y-Werte | Beispiel |
|---|---|---|---|
| I (rechts oben) | positiv | positiv | $(3, 2)$ |
| II (links oben) | negativ | positiv | $(-4, 5)$ |
| III (links unten) | negativ | negativ | $(-2, -3)$ |
| IV (rechts unten) | positiv | negativ | $(1, -4)$ |

> [!tip] Merkregel
> Die Quadranten werden **gegen den Uhrzeigersinn** nummeriert, beginnend rechts oben.
>
> **Eselsbrücke**: Stell dir vor, du schaust auf eine Uhr. Der Stundenzeiger wandert im Uhrzeigersinn – die Quadranten aber genau andersherum!

> [!warning] **Häufiger Fehler**
> Viele Schüler verwechseln die Nummerierung der Quadranten. Ein häufiger Irrtum ist, bei Quadrant I links oben zu beginnen oder im Uhrzeigersinn zu zählen. Merke: **Rechts oben ist der erste Quadrant**, dann gegen den Uhrzeigersinn weiter.

## Einheiten und Skalierung

### Einheitsstrecken

Auf beiden Achsen wird eine **Einheitsstrecke** festgelegt. Diese Einheitsstrecke ist willkürlich wählbar – in der Praxis richtet sie sich nach dem Problem, das dargestellt werden soll.

```
    y
    ↑
  3 ┼
  2 ┼
  1 ┼
    ┼───┼───┼───→ x
    0   1   2   3
```

- Die Einheitsstrecken können auf beiden Achsen **gleich** oder **unterschiedlich** sein
- Bei unterschiedlichen Einheiten spricht man von verschiedenen **Maßstäben**

> [!info] **Alltags-Beispiel: Unterschiedliche Maßstäbe**
> Wenn du den Benzinverbrauch eines Autos über die Zeit darstellst, könntest du auf der x-Achse Tage (1, 2, 3, ...) und auf der y-Achse Liter (10, 20, 30, ...) abtragen. Die Einheiten sind völlig unterschiedlich – das ist in Anwendungen völlig normal!

### Wahl der Skalierung

> [!tip] Praktischer Hinweis
> Die Skalierung sollte so gewählt werden, dass die darzustellenden Punkte gut sichtbar sind:
> - Nicht zu große Einheiten (Punkte liegen zu dicht)
> - Nicht zu kleine Einheiten (Punkte außerhalb des Blattes)
>
> **Faustregel**: Wähle die Skalierung so, dass der interessante Bereich etwa 70–80% des verfügbaren Platzes ausfüllt.

### Koordinatensysteme im Alltag

Koordinatensysteme begegnen uns überall:

| Anwendung | x-Achse | y-Achse |
|---|---|---|
| Stadtplan | West-Ost | Süd-Nord |
| Kinosessel | Reihe | Sitznummer |
| Schachbrett | Buchstabe (a–h) | Zahl (1–8) |
| Excel-Tabelle | Spalte (A, B, C, ...) | Zeile (1, 2, 3, ...) |
| GPS-Navigation | Längengrad | Breitengrad |

## Ein Koordinatensystem zeichnen

### Schritt-für-Schritt-Anleitung

1. **Achsen zeichnen**: Zwei senkrechte Linien mit Pfeilen am Ende
2. **Achsen beschriften**: $x$ und $y$ an die Pfeilspitzen
3. **Ursprung markieren**: Mit $O$ oder $(0,0)$ beschriften
4. **Einheiten markieren**: Regelmäßige Markierungen auf beiden Achsen
5. **Zahlen eintragen**: Wichtige Werte beschriften

### Beispiel eines vollständigen Koordinatensystems

```
        y
        ↑
      4 ┤
        │
      2 ┤
        │
────┬───┼───┬───┬───→ x
   -2   O   2   4
        │
     -2 ┤
        │
```

## Punkte auf den Achsen

Besondere Punkte liegen direkt **auf einer der Achsen**:

| Punkt | Position | Koordinate |
|---|---|---|
| Auf der x-Achse | $y = 0$ | z.B. $(3, 0)$ |
| Auf der y-Achse | $x = 0$ | z.B. $(0, 5)$ |
| Im Ursprung | $x = 0$ und $y = 0$ | $(0, 0)$ |

## Zusammenfassung

> [!abstract] Kernpunkte
> - Das kartesische Koordinatensystem besteht aus zwei senkrechten Achsen
> - Die x-Achse ist horizontal, die y-Achse vertikal
> - Der Ursprung hat die Koordinaten $(0, 0)$
> - Die vier Quadranten werden gegen den Uhrzeigersinn nummeriert
> - Durch dieses System werden Geometrie und Algebra verbunden

## Zusammenhänge

Das kartesische Koordinatensystem ist die Grundlage für viele weitere Themen:

- → [[02-Punkte-und-Koordinaten|Punkte und Koordinaten]] – Das Einzeichnen und Ablesen von Punkten
- → [[03-Einfuehrung-Funktionen|Funktionen]] – Darstellung von Zusammenhängen als Graphen
- → [[../10-Grundlagen-der-Geometrie/01-Punkte-Strecken-Geraden|Geometrie]] – Konstruktionen im Koordinatensystem
- → [[../11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]] – Abstandsberechnung zwischen Punkten

## Übungsaufgaben

1. Zeichne ein Koordinatensystem mit Einheitslänge 1 cm und beschrifte die Achsen von $-5$ bis $+5$.

2. In welchem Quadranten liegen die folgenden Punkte?
   - $A(3, 4)$
   - $B(-2, 5)$
   - $C(-3, -1)$
   - $D(4, -2)$

3. Welche Punkte liegen auf der x-Achse, welche auf der y-Achse?
   - $P(0, 3)$
   - $Q(5, 0)$
   - $R(0, 0)$
   - $S(-2, 0)$

---

**Navigation**: [[00-Funktionen-Index|← Übersicht]] | [[02-Punkte-und-Koordinaten|Punkte und Koordinaten →]]
