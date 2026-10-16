---
title: "Parabeln und ihre Eigenschaften"
created: 2026-10-13
modified: 2026-10-13
chapter: "09"
section: "09"
status: "draft - review pending"
type: lecture
keywords:
  - Parabel
  - Scheitelpunkt
  - Symmetrieachse
  - Verschiebung
  - Streckung
---

# Parabeln und ihre Eigenschaften

> [!info] Lernziele
> - Parabeln systematisch analysieren können
> - Verschiebungen und Streckungen verstehen
> - Aus dem Graphen die Funktionsgleichung ableiten
> - Parabeln skizzieren können

## Verschiebungen der Normalparabel

### Vertikale Verschiebung

$$f(x) = x^2 + e$$

Die Parabel wird um $e$ Einheiten **nach oben** (wenn $e > 0$) oder **nach unten** (wenn $e < 0$) verschoben.

```
    y
    ↑     x² + 2
  4 ┤    ╱╲
    │   ╱  ╲      x²
  2 ┤  ╱╲╱──╲╱╲
    │ ╱        ╲
────┼╱──────────╲──→ x
    │            x² - 2
 -2 ┤  ╱╲
    │ ╱  ╲
```

### Horizontale Verschiebung

$$f(x) = (x - d)^2$$

Die Parabel wird um $d$ Einheiten **nach rechts** (wenn $d > 0$) oder **nach links** (wenn $d < 0$) verschoben.

> [!warning] Achtung: Vorzeichen!
> $(x - 3)^2$ verschiebt nach **rechts** (zu $x = 3$)
> $(x + 2)^2 = (x - (-2))^2$ verschiebt nach **links** (zu $x = -2$)

```
    y
    ↑    (x+2)²     x²    (x-3)²
    │      ╱╲      ╱╲      ╱╲
    │     ╱  ╲    ╱  ╲    ╱  ╲
    │    ╱    ╲  ╱    ╲  ╱    ╲
────┼───●──────●───────●────────→ x
       -2      0       3
```

### Kombinierte Verschiebung

$$f(x) = (x - d)^2 + e$$

Scheitelpunkt: $S(d, e)$

> [!example] Beispiel
> $f(x) = (x - 2)^2 + 3$
> 
> - Verschiebung: 2 nach rechts, 3 nach oben
> - Scheitelpunkt: $S(2, 3)$

## Streckung und Stauchung

### Vertikale Streckung/Stauchung

$$f(x) = a \cdot x^2$$

| $|a|$ | Wirkung |
|---|---|
| $|a| > 1$ | Parabel wird **schmaler** (gestreckt in y-Richtung) |
| $|a| = 1$ | Normalparabel |
| $0 < |a| < 1$ | Parabel wird **weiter** (gestaucht in y-Richtung) |

### Spiegelung an der x-Achse

$$f(x) = -x^2$$

Bei $a < 0$ wird die Parabel an der x-Achse **gespiegelt** und öffnet nach unten.

## Vollständige Analyse einer Parabel

### Gegebene Gleichung analysieren

$f(x) = -2(x + 1)^2 + 4$

**Schritt 1**: Parameter identifizieren
- $a = -2$ (negativ → Öffnung nach unten, Betrag > 1 → schmaler)
- $d = -1$ (Verschiebung 1 nach links)
- $e = 4$ (Verschiebung 4 nach oben)

**Schritt 2**: Eigenschaften bestimmen

| Eigenschaft | Wert |
|---|---|
| Scheitelpunkt | $S(-1, 4)$ |
| Symmetrieachse | $x = -1$ |
| Öffnungsrichtung | nach unten |
| Weite | schmaler als Normalparabel |
| Maximum/Minimum | Maximum bei $y = 4$ |

**Schritt 3**: Weitere Punkte berechnen

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
|---|---|---|---|---|---|
| $f(x)$ | $-4$ | $2$ | $4$ | $2$ | $-4$ |

## Parabel aus Graph bestimmen

### Methode 1: Scheitelpunkt und weiterer Punkt

1. Scheitelpunkt $S(d, e)$ ablesen
2. Weiteren Punkt $P(x_1, y_1)$ ablesen
3. In Scheitelpunktform einsetzen und $a$ berechnen

> [!example] Beispiel
> Scheitelpunkt $S(2, -1)$, weiterer Punkt $P(4, 3)$
> 
> Ansatz: $f(x) = a(x - 2)^2 - 1$
> 
> Mit $P(4, 3)$: $3 = a(4 - 2)^2 - 1$
> $3 = 4a - 1$
> $a = 1$
> 
> Gleichung: $f(x) = (x - 2)^2 - 1$

### Methode 2: Drei Punkte

Drei Punkte in $f(x) = ax^2 + bx + c$ einsetzen und das Gleichungssystem lösen.

## Transformationen zusammenfassen

Die allgemeine Form mit allen Transformationen:

$$f(x) = a(x - d)^2 + e$$

| Parameter | Wirkung |
|---|---|
| $a > 0$ | Öffnung nach oben |
| $a < 0$ | Öffnung nach unten |
| $|a| > 1$ | Parabel schmaler |
| $|a| < 1$ | Parabel weiter |
| $d > 0$ | Verschiebung nach rechts |
| $d < 0$ | Verschiebung nach links |
| $e > 0$ | Verschiebung nach oben |
| $e < 0$ | Verschiebung nach unten |

## Parabeln zeichnen

### Schnelle Skizze

1. Scheitelpunkt einzeichnen
2. Symmetrieachse markieren
3. Weitere Punkte symmetrisch berechnen
4. Parabel durch die Punkte zeichnen

### Standardpunkte

Für $f(x) = a(x - d)^2 + e$:
- $x = d$: $y = e$ (Scheitelpunkt)
- $x = d \pm 1$: $y = e + a$
- $x = d \pm 2$: $y = e + 4a$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Scheitelpunktform: $f(x) = a(x - d)^2 + e$
> - $d$ bestimmt die horizontale, $e$ die vertikale Verschiebung
> - $|a|$ bestimmt die Weite, Vorzeichen von $a$ die Öffnungsrichtung
> - Scheitelpunkt: $S(d, e)$
> - Symmetrieachse: $x = d$
> - Zur Bestimmung der Gleichung: Scheitelpunkt + 1 weiterer Punkt genügen

## Übungsaufgaben

1. Beschreibe die Transformation ausgehend von der Normalparabel:
   - $f(x) = (x - 4)^2$
   - $g(x) = x^2 + 5$
   - $h(x) = 3x^2$
   - $k(x) = -(x + 2)^2 - 1$

2. Bestimme den Scheitelpunkt und skizziere:
   - $f(x) = (x - 1)^2 - 4$
   - $g(x) = -0{,}5(x + 3)^2 + 2$

3. Bestimme die Funktionsgleichung:
   - Scheitelpunkt $S(3, 2)$, durch $P(5, 6)$
   - Scheitelpunkt $S(-1, 4)$, Öffnung nach unten, durch $P(1, 0)$

4. Ordne die Parabeln nach Weite (schmalste zuerst):
   $f(x) = 2x^2$, $g(x) = \frac{1}{3}x^2$, $h(x) = x^2$, $k(x) = 0{,}5x^2$

---

**Navigation**: [[08-Quadratische-Funktionen|← Quadratische Funktionen]] | [[00-Funktionen-Index|Übersicht]] | [[10-Schnittpunkte|Schnittpunkte →]]
