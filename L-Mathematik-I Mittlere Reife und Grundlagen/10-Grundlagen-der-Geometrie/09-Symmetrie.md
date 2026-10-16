---
title: "Symmetrie"
created: 2026-10-13
modified: 2025-01-20
chapter: "10"
section: "09"
status: "draft - review pending"
type: lecture
keywords:
  - Symmetrie
  - Achsensymmetrie
  - Punktsymmetrie
  - Spiegelung
  - Drehsymmetrie
---

# Symmetrie

> [!info] Lernziele
> - Achsensymmetrie erkennen und anwenden
> - Punktsymmetrie verstehen und prüfen
> - Symmetrieachsen und -zentren bestimmen
> - Symmetrische Figuren konstruieren

---

## Einführung

Symmetrie ist eines der grundlegendsten Konzepte in Mathematik, Natur und Kunst. Das Wort kommt vom griechischen *symmetria* (Ebenmaß, Gleichmaß). Symmetrische Formen empfinden wir oft als besonders schön und harmonisch.

### Symmetrie in Natur und Technik

Symmetrie begegnet uns überall:
- **Biologie**: Schmetterlingsflügel, menschliches Gesicht, Blütenblätter
- **Kristalle**: Schneeflocken (6-fache Symmetrie), Diamanten, Salzkristalle
- **Architektur**: Schloss Versailles, Taj Mahal, gotische Kirchenfenster
- **Technik**: Räder, Propeller, Flugzeugdesign
- **Kunst**: Mandalas, islamische Ornamente, M.C. Eschers Bilder

> [!note] **Warum ist Symmetrie so verbreitet?**
> In der Natur entsteht Symmetrie oft aus Effizienzgründen: Ein symmetrischer Körper ist stabiler, eine symmetrische Fortbewegung ist energiesparender. Auch unser Gehirn bevorzugt symmetrische Formen – wir empfinden sie als „richtig" und ästhetisch ansprechend.

---

## Achsensymmetrie (Spiegelsymmetrie)

Eine Figur ist **achsensymmetrisch**, wenn sie durch eine Gerade (Symmetrieachse) in zwei deckungsgleiche Hälften geteilt wird, die Spiegelbilder voneinander sind.

### Erkennen von Achsensymmetrie

> [!tip] Test
> Faltet man die Figur entlang der Symmetrieachse, liegen beide Hälften exakt übereinander.

```
      │
   ╱╲ │ ╱╲
  ╱  ╲│╱  ╲
 ╱    │    ╲
      │
 Symmetrieachse
```

### Beispiele achsensymmetrischer Figuren

| Figur | Anzahl Symmetrieachsen |
|---|---|
| Kreis | unendlich viele |
| Quadrat | 4 |
| Rechteck | 2 |
| Gleichseitiges Dreieck | 3 |
| Gleichschenkliges Dreieck | 1 |
| Raute | 2 |
| Gleichschenkliges Trapez | 1 |

### Spiegelung an einer Achse

Bei der Spiegelung eines Punktes $P$ an einer Achse $g$:
- Die Achse steht **senkrecht** auf der Verbindung $PP'$
- Die Achse **halbiert** die Strecke $PP'$

```
        │
   P ●──┼──● P'
        │
        g
```

## Punktsymmetrie (Drehsymmetrie 180°)

Eine Figur ist **punktsymmetrisch**, wenn sie bei einer Drehung um 180° um einen Punkt (Symmetriezentrum) auf sich selbst abgebildet wird.

### Erkennen von Punktsymmetrie

> [!tip] Test
> Dreht man die Figur um 180° um das Zentrum, sieht sie genauso aus wie vorher.

```
      ●───────╮
     ╱         ╲
    ╱     ● Z   ╲
   ╱             ╲
  ╱               ╲
 ╰───────●
```

### Beispiele punktsymmetrischer Figuren

| Figur | Punktsymmetrisch? | Zentrum |
|---|---|---|
| Kreis | ja | Mittelpunkt |
| Quadrat | ja | Schnittpunkt der Diagonalen |
| Rechteck | ja | Schnittpunkt der Diagonalen |
| Parallelogramm | ja | Schnittpunkt der Diagonalen |
| Gleichschenkliges Dreieck | nein | - |
| Buchstabe S | ja | Mitte |
| Buchstabe A | nein | - |

### Punktspiegelung

Bei der Spiegelung eines Punktes $P$ am Zentrum $Z$:
- $Z$ liegt **auf der Verbindung** $PP'$
- $Z$ ist der **Mittelpunkt** von $\overline{PP'}$

$$|\overline{PZ}| = |\overline{ZP'}|$$

## Drehsymmetrie

Eine Figur ist **n-fach drehsymmetrisch**, wenn sie bei einer Drehung um $\frac{360°}{n}$ auf sich selbst abgebildet wird.

### Beispiele

| Figur | Drehsymmetrie |
|---|---|
| Gleichseitiges Dreieck | 3-fach (120°) |
| Quadrat | 4-fach (90°) |
| Regelmäßiges Fünfeck | 5-fach (72°) |
| Regelmäßiges n-Eck | n-fach ($\frac{360°}{n}$) |

## Symmetrien kombiniert

Das **Quadrat** hat besonders viele Symmetrien:
- 4 Symmetrieachsen (2 durch Seitenmitten, 2 durch Ecken)
- Punktsymmetrie
- 4-fache Drehsymmetrie

```
      │
      │
  ╲   │   ╱
   ╲  │  ╱
────╲─│─╱────
    ╱─│─╲
   ╱  │  ╲
  ╱   │   ╲
      │
```

## Symmetrie im Koordinatensystem

### Achsensymmetrie zur y-Achse

Bedingung für Punkte: $P(x, y)$ → $P'(-x, y)$

Bedingung für Funktionen: $f(-x) = f(x)$ (gerade Funktion)

Beispiel: $f(x) = x^2$

### Punktsymmetrie zum Ursprung

Bedingung für Punkte: $P(x, y)$ → $P'(-x, -y)$

Bedingung für Funktionen: $f(-x) = -f(x)$ (ungerade Funktion)

Beispiel: $f(x) = x^3$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Achsensymmetrie: Spiegelung an einer Geraden
> - Punktsymmetrie: Drehung um 180° um einen Punkt
> - Drehsymmetrie: Deckung bei Drehung um bestimmten Winkel
> - Im Koordinatensystem: Achsensymmetrie (y-Achse) ↔ $f(-x) = f(x)$
> - Im Koordinatensystem: Punktsymmetrie (Ursprung) ↔ $f(-x) = -f(x)$

## Zusammenhänge

Symmetrie verbindet Geometrie mit anderen mathematischen Bereichen:

- → [[05-Vierecke|Vierecke]] – Quadrate haben die meisten Symmetrien
- → [[04-Dreiecke|Dreiecke]] – Gleichseitige Dreiecke sind 3-fach drehsymmetrisch
- → [[06-Kreise|Kreise]] – Der Kreis ist unendlich-fach symmetrisch
- → [[05-Lineare-Funktionen|Lineare Funktionen]] – Punktsymmetrie bei Ursprungsgeraden
- → [[08-Quadratische-Funktionen|Quadratische Funktionen]] – Achsensymmetrie zur Scheitelgeraden
- → [[12-Geometrische-Konstruktionen|Konstruktionen]] – Symmetrische Punkte konstruieren

> [!tip] **Symmetrie als Rechenhilfe**
> Wenn du weißt, dass eine Figur symmetrisch ist, musst du oft nur die Hälfte berechnen und kannst das Ergebnis spiegeln. Das spart Arbeit!

## Übungsaufgaben

1. Bestimme die Anzahl der Symmetrieachsen:
   - Regelmäßiges Sechseck
   - Buchstabe H
   - Buchstabe B
   - Ellipse

2. Welche Figuren sind punktsymmetrisch?
   - Raute
   - Trapez
   - Parallelogramm
   - Gleichseitiges Dreieck

3. Spiegle den Punkt $P(3, 2)$:
   - An der y-Achse
   - An der x-Achse
   - Am Ursprung

4. Konstruiere das Spiegelbild eines Dreiecks $ABC$ an einer gegebenen Achse.

5. Prüfe, ob die Funktion $f(x) = x^4 - 2x^2$ achsensymmetrisch zur y-Achse ist.

---

**Navigation**: [[08-Flaechenberechnungen|← Flächen]] | [[00-Geometrie-Index|Übersicht]] | [[10-Kongruenz|Kongruenz →]]
