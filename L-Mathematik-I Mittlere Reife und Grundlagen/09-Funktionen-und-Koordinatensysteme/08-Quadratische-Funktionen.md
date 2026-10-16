---
title: "Quadratische Funktionen"
created: 2026-10-13
modified: 2026-10-13
chapter: "09"
section: "08"
status: "draft - review pending"
type: lecture
keywords:
  - Quadratische Funktion
  - Parabel
  - Scheitelpunkt
  - Normalform
  - Öffnung
---

# Quadratische Funktionen

> [!info] Lernziele
> - Quadratische Funktionen erkennen und beschreiben
> - Die verschiedenen Darstellungsformen kennen
> - Den Graphen (Parabel) skizzieren können
> - Den Einfluss der Parameter auf den Graphen verstehen

## Definition

Eine **quadratische Funktion** hat die allgemeine Form:

$$f(x) = ax^2 + bx + c \quad \text{mit } a \neq 0$$

| Parameter | Bedeutung |
|---|---|
| $a$ | Öffnungsfaktor (bestimmt Weite und Richtung) |
| $b$ | Beeinflusst die Lage der Parabel |
| $c$ | y-Achsenabschnitt |

> [!note] Merkmal
> Der Graph einer quadratischen Funktion ist eine **Parabel**.

## Die Normalparabel

Die einfachste quadratische Funktion ist:

$$f(x) = x^2$$

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $9$ | $4$ | $1$ | $0$ | $1$ | $4$ | $9$ |

```
    y
    ↑
  9 ┤ ●             ●
    │
    │
  4 ┤   ●       ●
    │
  1 ┤     ●   ●
    │       ●
────┼───┬───┬───┬───→ x
   -3  -2  -1  0   1   2   3
```

**Eigenschaften der Normalparabel**:
- Scheitelpunkt bei $(0, 0)$
- Achsensymmetrisch zur y-Achse
- Öffnung nach oben

## Der Öffnungsfaktor $a$

### Einfluss auf die Öffnungsrichtung

| Wert von $a$ | Öffnungsrichtung | Graph |
|---|---|---|
| $a > 0$ | Nach **oben** (Minimum) | ⌣ |
| $a < 0$ | Nach **unten** (Maximum) | ⌢ |

### Einfluss auf die Weite

| Wert von $|a|$ | Erscheinung |
|---|---|
| $|a| > 1$ | Schmaler als Normalparabel |
| $|a| = 1$ | Wie Normalparabel |
| $0 < |a| < 1$ | Weiter als Normalparabel |

```
    y
    ↑        a = 2 (schmal)
    │        ╱╲
    │       ╱  ╲
    │      ╱    ╲   a = 1 (normal)
    │   ╱╲╱      ╲╱╲
    │  ╱  ╲      ╱  ╲
    │ ╱    ╲    ╱    ╲  a = 0.5 (weit)
────┼╱──────╲──╱──────╲──→ x
   ╱│        ╲╱        ╲
```

## Formen der quadratischen Funktion

### 1. Allgemeine Form (Normalform)

$$f(x) = ax^2 + bx + c$$

- Leicht erkennbar: ist es eine quadratische Funktion?
- y-Achsenabschnitt direkt ablesbar: $c = f(0)$

### 2. Scheitelpunktform

$$f(x) = a(x - d)^2 + e$$

Scheitelpunkt: $S(d, e)$

> [!tip] Merkhilfe
> In der Klammer steht $(x - d)$, der Scheitelpunkt hat aber $x = d$ (nicht $-d$!).

### 3. Faktorisierte Form (Nullstellenform)

$$f(x) = a(x - x_1)(x - x_2)$$

Nullstellen: $x_1$ und $x_2$

## Umrechnung zwischen den Formen

### Von Scheitelpunktform zu Normalform

$$f(x) = a(x - d)^2 + e$$

Ausmultiplizieren:
$$f(x) = a(x^2 - 2dx + d^2) + e$$
$$f(x) = ax^2 - 2adx + ad^2 + e$$

> [!example] Beispiel
> $f(x) = 2(x - 3)^2 + 1$
> 
> $= 2(x^2 - 6x + 9) + 1$
> $= 2x^2 - 12x + 18 + 1$
> $= 2x^2 - 12x + 19$

### Von Normalform zu Scheitelpunktform

Die Koordinaten des Scheitelpunkts:

$$x_S = -\frac{b}{2a}$$
$$y_S = f(x_S) = c - \frac{b^2}{4a}$$

> [!example] Beispiel
> $f(x) = x^2 - 4x + 7$
> 
> $x_S = -\frac{-4}{2 \cdot 1} = 2$
> 
> $y_S = 7 - \frac{(-4)^2}{4 \cdot 1} = 7 - 4 = 3$
> 
> Scheitelpunkt: $S(2, 3)$
> 
> Scheitelpunktform: $f(x) = (x - 2)^2 + 3$

## Wichtige Eigenschaften einer Parabel

| Eigenschaft | Berechnung/Ablesen |
|---|---|
| Scheitelpunkt | $S\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)$ |
| Symmetrieachse | $x = -\frac{b}{2a}$ |
| y-Achsenabschnitt | $f(0) = c$ |
| Nullstellen | $f(x) = 0$ lösen (p-q-Formel) |
| Öffnungsrichtung | Vorzeichen von $a$ |

## Nullstellen

Die **Nullstellen** einer quadratischen Funktion $f(x) = ax^2 + bx + c$ sind die Lösungen von $f(x) = 0$.

Mit der p-q-Formel (nach Division durch $a$):

$$x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}$$

| Diskriminante $D$ | Anzahl Nullstellen |
|---|---|
| $D > 0$ | 2 verschiedene |
| $D = 0$ | 1 (Doppelnullstelle = Scheitelpunkt auf x-Achse) |
| $D < 0$ | keine reellen |

## Zusammenfassung

> [!abstract] Kernpunkte
> - Quadratische Funktion: $f(x) = ax^2 + bx + c$ mit $a \neq 0$
> - Der Graph ist eine Parabel
> - $a > 0$: Öffnung nach oben; $a < 0$: nach unten
> - $|a|$ bestimmt die Weite der Parabel
> - Scheitelpunktform: $f(x) = a(x - d)^2 + e$ mit $S(d, e)$
> - Scheitelpunkt: $x_S = -\frac{b}{2a}$

## Übungsaufgaben

1. Bestimme die Öffnungsrichtung und vergleiche mit der Normalparabel:
   - $f(x) = 3x^2$
   - $g(x) = -x^2$
   - $h(x) = \frac{1}{4}x^2$

2. Forme in Normalform um:
   - $f(x) = (x - 2)^2 + 5$
   - $g(x) = -2(x + 1)^2 - 3$

3. Bestimme den Scheitelpunkt:
   - $f(x) = x^2 - 6x + 5$
   - $g(x) = 2x^2 + 8x + 10$

4. Bestimme die Nullstellen:
   - $f(x) = x^2 - 4$
   - $g(x) = x^2 - 6x + 9$
   - $h(x) = x^2 + 4$

---

**Navigation**: [[07-Geradengleichungen|← Geradengleichungen]] | [[00-Funktionen-Index|Übersicht]] | [[09-Parabeln|Parabeln →]]
