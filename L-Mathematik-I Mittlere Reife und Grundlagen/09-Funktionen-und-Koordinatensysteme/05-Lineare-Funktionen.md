---
title: "Lineare Funktionen"
created: 2026-10-13
modified: 2026-10-13
chapter: "09"
section: "05"
status: "draft - review pending"
type: lecture
keywords:
  - Lineare Funktion
  - Gerade
  - Steigung
  - y-Achsenabschnitt
  - Proportionalität
---

# Lineare Funktionen

> [!info] Lernziele
> - Lineare Funktionen erkennen und beschreiben
> - Den Graphen als Gerade identifizieren
> - Steigung und y-Achsenabschnitt aus der Gleichung ablesen
> - Den Unterschied zwischen proportionalen und allgemeinen linearen Funktionen verstehen

## Definition

Eine **lineare Funktion** hat die allgemeine Form:

$$f(x) = mx + b$$

| Parameter | Bedeutung | Andere Namen |
|---|---|---|
| $m$ | **Steigung** | Anstieg, Steigungsfaktor |
| $b$ | **y-Achsenabschnitt** | Ordinatenabschnitt |

> [!note] Eigenschaft
> Der Graph einer linearen Funktion ist immer eine **Gerade**.

## Proportionale Funktionen (Sonderfall)

Wenn $b = 0$, heißt die Funktion **proportional** oder **direkt proportional**:

$$f(x) = mx$$

**Eigenschaften**:
- Die Gerade geht durch den **Ursprung** $(0, 0)$
- $f(x)$ ist proportional zu $x$
- Verdoppelt sich $x$, verdoppelt sich auch $f(x)$

> [!example] Beispiel
> $f(x) = 3x$
> 
> | $x$ | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|
> | $f(x)$ | 3 | 6 | 9 | 12 |
> 
> Der Quotient $\frac{f(x)}{x} = 3$ ist konstant.

## Steigung $m$

Die **Steigung** gibt an, um wie viel der y-Wert zunimmt, wenn x um 1 zunimmt.

### Interpretation

| Steigung | Bedeutung | Graph |
|---|---|---|
| $m > 0$ | Funktion steigt | von links unten nach rechts oben |
| $m < 0$ | Funktion fällt | von links oben nach rechts unten |
| $m = 0$ | konstant | horizontale Gerade |
| $|m|$ groß | steile Gerade | |
| $|m|$ klein | flache Gerade | |

### Grafische Darstellung

```
    y                           y
    ↑                           ↑
    │    ╱ m > 0                │╲     m < 0
    │  ╱                        │ ╲
    │╱                          │  ╲
────┼──────→ x              ────┼────╲──→ x
    │                           │     ╲
```

### Berechnung der Steigung

Aus zwei Punkten $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

> [!example] Beispiel
> $P_1(1, 2)$ und $P_2(4, 8)$
> 
> $$m = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2$$

## y-Achsenabschnitt $b$

Der **y-Achsenabschnitt** ist der y-Wert, an dem die Gerade die y-Achse schneidet.

$$b = f(0)$$

> [!example] Beispiel
> $f(x) = 2x + 3$
> 
> $f(0) = 2 \cdot 0 + 3 = 3$
> 
> Die Gerade schneidet die y-Achse bei $(0, 3)$.

## Beispiele linearer Funktionen

### Verschiedene Steigungen

```
    y
    ↑
    │      ╱ m = 2
    │    ╱
    │  ╱    ╱ m = 1
    │╱  ──╱── m = 0.5
────┼────────→ x
    │
```

### Verschiedene y-Achsenabschnitte

```
    y
    ↑       ╱
  3 ┤     ╱    f(x) = x + 3
    │   ╱
  1 ┤ ╱ ╱      g(x) = x + 1
────┼╱───────→ x
   ╱│
 -2╱┤          h(x) = x - 2
```

> [!note] Beobachtung
> Geraden mit **gleicher Steigung** sind **parallel** zueinander.

## Gleichung aufstellen

### Aus Steigung und y-Achsenabschnitt

Gegeben: $m = 2$, $b = -1$

$$f(x) = 2x - 1$$

### Aus zwei Punkten

1. Steigung berechnen: $m = \frac{y_2 - y_1}{x_2 - x_1}$
2. Einen Punkt einsetzen und $b$ berechnen
3. Gleichung aufstellen

> [!example] Beispiel
> $P_1(2, 5)$ und $P_2(4, 9)$
> 
> **Schritt 1**: $m = \frac{9 - 5}{4 - 2} = \frac{4}{2} = 2$
> 
> **Schritt 2**: $f(x) = 2x + b$, mit $P_1$: $5 = 2 \cdot 2 + b$ → $b = 1$
> 
> **Schritt 3**: $f(x) = 2x + 1$

## Nullstelle

Die **Nullstelle** ist der x-Wert, an dem $f(x) = 0$.

$$mx + b = 0$$
$$x = -\frac{b}{m}$$

> [!example] Beispiel
> $f(x) = 3x - 6$
> 
> $3x - 6 = 0$
> $x = 2$
> 
> Die Gerade schneidet die x-Achse bei $(2, 0)$.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Lineare Funktionen: $f(x) = mx + b$
> - Der Graph ist eine Gerade
> - $m$ = Steigung (positiv: steigend, negativ: fallend)
> - $b$ = y-Achsenabschnitt (wo die Gerade die y-Achse schneidet)
> - Proportionale Funktionen gehen durch den Ursprung ($b = 0$)
> - Parallele Geraden haben die gleiche Steigung

## Übungsaufgaben

1. Gib Steigung und y-Achsenabschnitt an:
   - $f(x) = 4x + 2$
   - $g(x) = -2x + 5$
   - $h(x) = \frac{1}{2}x$

2. Zeichne die Graphen von $f(x) = 2x - 3$ und $g(x) = -x + 1$.

3. Bestimme die Gleichung der Geraden durch:
   - $P(0, 4)$ mit Steigung $m = 3$
   - $A(1, 3)$ und $B(3, 7)$

4. Berechne die Nullstelle von:
   - $f(x) = 5x - 15$
   - $g(x) = -2x + 8$

---

**Navigation**: [[04-Funktionstabellen-und-Graphen|← Funktionstabellen]] | [[00-Funktionen-Index|Übersicht]] | [[06-Steigung-und-Achsenabschnitt|Steigung und Achsenabschnitt →]]
