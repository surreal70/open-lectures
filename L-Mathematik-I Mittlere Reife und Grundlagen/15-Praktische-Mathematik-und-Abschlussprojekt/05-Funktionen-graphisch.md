---
title: Graphische Darstellung von Funktionen
chapter: "15"
section: "15.5"
type: lecture
created: 2026-10-13
modified: 2025-07-18
status: draft - review pending
tags:
  - mathematik/funktionen
  - graphen
---

# Graphische Darstellung von Funktionen

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Wertetabellen erstellen
> - Funktionen im Koordinatensystem zeichnen
> - Graphen interpretieren

Die graphische Darstellung von Funktionen ist eine der mächtigsten Methoden, um mathematische Zusammenhänge zu verstehen. Ein Bild sagt mehr als tausend Worte – und ein Graph oft mehr als eine Formel. Die Visualisierung macht Eigenschaften wie Wachstum, Nullstellen oder Extremwerte sofort sichtbar.

### Warum Graphen so wichtig sind

Graphen begegnen uns überall:
- **Wirtschaft**: Aktienkurse, Umsatzentwicklung, Konjunkturzyklen
- **Wissenschaft**: Temperaturverlauf, Wachstumskurven, physikalische Messungen
- **Medien**: Infografiken, Statistiken, Wahlprognosen
- **Alltag**: Navigationsapps (Höhenprofil), Fitness-Tracker (Pulsverlauf)

> [!note] **René Descartes (1596–1650)**
> Das kartesische Koordinatensystem ist nach dem französischen Philosophen und Mathematiker René Descartes benannt. Seine Idee, geometrische Formen durch Gleichungen zu beschreiben, war revolutionär und legte den Grundstein für die analytische Geometrie.

---

## Wertetabelle erstellen

> [!example] f(x) = 2x - 1
> | x | -2 | -1 | 0 | 1 | 2 |
> |---|----|----|---|---|---|
> | f(x) | -5 | -3 | -1 | 1 | 3 |

### Systematisches Vorgehen

1. **Wertebereich festlegen**: Welche x-Werte sind sinnvoll?
2. **Tabelle anlegen**: x-Werte und f(x)-Zeile
3. **Werte berechnen**: Jeden x-Wert in die Funktion einsetzen
4. **Kontrollrechnung**: Mindestens einen Wert überprüfen

> [!tip] **Clevere Wertewahl**
> Wählen Sie x-Werte strategisch:
> - Bei linearen Funktionen genügen 2-3 Punkte
> - Bei quadratischen Funktionen: Symmetrieachse berücksichtigen
> - Nullstellen und besondere Punkte mit einbeziehen
> - Ganzzahlige x-Werte sind einfacher zu rechnen

> [!warning] **Häufiger Fehler: Zu wenige Punkte**
> Bei nichtlinearen Funktionen (z.B. Parabeln) führen zu wenige Punkte zu einer ungenauen Darstellung. Eine Parabel benötigt mindestens 5 Punkte, um die Krümmung korrekt darzustellen.

---

## Zeichenschritte

1. Wertetabelle anlegen
2. Koordinatensystem mit passender Skalierung
3. Punkte einzeichnen
4. Punkte verbinden

### Das Koordinatensystem richtig einrichten

```
        y
        │
    4 ──┼──────────────
        │
    2 ──┼──────────────
        │
  ──┼───┼───┼───┼───┼──▶ x
   -2  -1   0   1   2
        │
   -2 ──┼──────────────
        │
```

> [!tip] **Tipps für gute Graphen**
> - **Skalierung**: Beide Achsen müssen nicht gleich skaliert sein
> - **Beschriftung**: Achsen und Einheiten angeben
> - **Pfeile**: Zeigen die Richtung der positiven Werte
> - **Ursprung**: Mit 0 oder O markieren

### Verschiedene Funktionstypen erkennen

| Funktionstyp | Graphenform | Beispiel |
|--------------|-------------|----------|
| Linear | Gerade | $f(x) = 2x + 1$ |
| Quadratisch | Parabel | $f(x) = x^2 - 4$ |
| Exponentiell | Wachstumskurve | $f(x) = 2^x$ |
| Wurzel | Halbe Parabel | $f(x) = \sqrt{x}$ |

---

## Ablesen aus Graphen

- **Nullstellen:** Schnittpunkte mit x-Achse
- **y-Achsenabschnitt:** Schnittpunkt mit y-Achse
- **Steigung:** Anstieg pro Einheit

### Nullstellen ablesen

Die Nullstellen sind die x-Werte, an denen der Graph die x-Achse schneidet. Hier gilt: $f(x) = 0$

> [!example] Nullstelle einer Parabel
> Für $f(x) = x^2 - 4$ schneidet der Graph die x-Achse bei $x = -2$ und $x = 2$.
> Probe: $f(2) = 2^2 - 4 = 0$ ✓

### Steigung ablesen

Bei linearen Funktionen kann die Steigung direkt aus dem Graphen abgelesen werden:

```
        │      /
        │     /
        │    /   Δy = 2
        │   ╱────
        │  /    Δx = 1
        │ /
   ─────┼─────────▶
```

$$m = \frac{\Delta y}{\Delta x} = \frac{\text{Änderung in y}}{\text{Änderung in x}}$$

> [!tip] **Steigungsdreieck**
> Wählen Sie zwei Punkte auf der Geraden und zeichnen Sie ein rechtwinkliges Dreieck. Die Steigung ist das Verhältnis von Höhe zu Breite.

---

## Eigenschaften aus dem Graphen lesen

Der Graph verrät auf einen Blick viele Eigenschaften:

| Eigenschaft | Bedeutung | Beispiel |
|-------------|-----------|----------|
| **Monotonie** | Steigend oder fallend? | Temperaturverlauf: morgens steigend, abends fallend |
| **Maximum/Minimum** | Höchster/tiefster Punkt | Wurfparabel: Scheitelpunkt = höchster Punkt |
| **Symmetrie** | Achsen- oder Punktsymmetrie? | Parabeln sind achsensymmetrisch |
| **Definitionsbereich** | Für welche x existiert f(x)? | Wurzelfunktion: nur für x ≥ 0 |

> [!example] Graph interpretieren
> Der Graph zeigt den Wasserstand eines Flusses über 24 Stunden:
> - **Maximum** bei ca. 14 Uhr → Hochwasser am Nachmittag
> - **Minimum** bei ca. 2 Uhr → Niedrigwasser nachts
> - **Steigend** von 2 Uhr bis 14 Uhr → Zufluss überwiegt
> - **Fallend** von 14 Uhr bis 2 Uhr → Abfluss überwiegt

---

## Zusammenhänge

Die graphische Darstellung verbindet verschiedene Themenbereiche:

- → [[../09-Funktionen-und-Koordinatensysteme/01-Kartesisches-Koordinatensystem|Koordinatensystem]] – Grundlagen
- → [[../09-Funktionen-und-Koordinatensysteme/05-Lineare-Funktionen|Lineare Funktionen]] – Geraden zeichnen
- → [[../09-Funktionen-und-Koordinatensysteme/08-Quadratische-Funktionen|Quadratische Funktionen]] – Parabeln zeichnen
- → [[06-Tabellenkalkulation|Tabellenkalkulation]] – Diagramme digital erstellen

---

**Navigation:** [[04-Wirtschaftliche-Berechnungen|← Wirtschaft]] | [[06-Tabellenkalkulation|Tabellenkalkulation →]]
