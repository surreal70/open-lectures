---
title: "Einfache lineare Gleichungssysteme"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "11"
status: "draft - review pending"
type: lecture
keywords:
  - Gleichungssystem
  - Einsetzungsverfahren
  - Gleichsetzungsverfahren
  - Additionsverfahren
---

# Einfache lineare Gleichungssysteme

> [!info] Lernziele
> - Lineare Gleichungssysteme mit zwei Variablen erkennen
> - Das Einsetzungsverfahren anwenden können
> - Das Gleichsetzungsverfahren anwenden können
> - Das Additionsverfahren anwenden können
> - Sonderfälle (keine/unendlich viele Lösungen) erkennen

## Was ist ein Gleichungssystem?

Ein **lineares Gleichungssystem (LGS)** besteht aus mehreren linearen Gleichungen, die gleichzeitig erfüllt sein müssen.

### Beispiel mit zwei Gleichungen und zwei Variablen

$$\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$$

**Lösung**: Das Wertepaar $(x, y)$, das **beide** Gleichungen erfüllt.

## Das Einsetzungsverfahren

### Prinzip

1. Eine Gleichung nach einer Variablen auflösen
2. Diesen Ausdruck in die andere Gleichung einsetzen
3. Entstehende Gleichung lösen
4. Zweite Variable berechnen

### Beispiel

$$\begin{cases} y = 2x + 1 & (I) \\ 3x + y = 11 & (II) \end{cases}$$

**Schritt 1**: Gleichung (I) ist bereits nach $y$ aufgelöst.

**Schritt 2**: $y$ aus (I) in (II) einsetzen:
$$3x + (2x + 1) = 11$$

**Schritt 3**: Nach $x$ lösen:
$$5x + 1 = 11$$
$$5x = 10$$
$$x = 2$$

**Schritt 4**: $x$ in (I) einsetzen:
$$y = 2 \cdot 2 + 1 = 5$$

**Lösung**: $(x, y) = (2, 5)$

**Probe in beiden Gleichungen**:
- (I): $5 = 2 \cdot 2 + 1 = 5$ ✓
- (II): $3 \cdot 2 + 5 = 6 + 5 = 11$ ✓

## Das Gleichsetzungsverfahren

### Prinzip

1. Beide Gleichungen nach derselben Variablen auflösen
2. Die Ausdrücke gleichsetzen
3. Entstehende Gleichung lösen
4. Zweite Variable berechnen

### Beispiel

$$\begin{cases} 2x + y = 10 & (I) \\ x + y = 7 & (II) \end{cases}$$

**Schritt 1**: Beide nach $y$ auflösen:
- Aus (I): $y = 10 - 2x$
- Aus (II): $y = 7 - x$

**Schritt 2**: Gleichsetzen:
$$10 - 2x = 7 - x$$

**Schritt 3**: Nach $x$ lösen:
$$10 - 7 = -x + 2x$$
$$3 = x$$

**Schritt 4**: $x$ einsetzen:
$$y = 7 - 3 = 4$$

**Lösung**: $(x, y) = (3, 4)$

## Das Additionsverfahren

### Prinzip

1. Gleichungen so multiplizieren, dass eine Variable beim Addieren/Subtrahieren wegfällt
2. Gleichungen addieren oder subtrahieren
3. Entstehende Gleichung lösen
4. Zweite Variable berechnen

### Beispiel

$$\begin{cases} 3x + 2y = 12 & (I) \\ x - 2y = 4 & (II) \end{cases}$$

**Schritt 1**: Die $y$-Terme haben entgegengesetzte Vorzeichen ($+2y$ und $-2y$).

**Schritt 2**: Gleichungen addieren:
$$\begin{array}{rcl}
3x + 2y &=& 12 \\
x - 2y &=& 4 \\
\hline
4x &=& 16
\end{array}$$

**Schritt 3**: Nach $x$ lösen:
$$x = 4$$

**Schritt 4**: $x$ in (II) einsetzen:
$$4 - 2y = 4$$
$$-2y = 0$$
$$y = 0$$

**Lösung**: $(x, y) = (4, 0)$

### Erweitertes Beispiel (mit Multiplikation)

$$\begin{cases} 2x + 3y = 13 & (I) \\ 5x + 2y = 16 & (II) \end{cases}$$

**Ziel**: $y$ eliminieren

**Schritt 1**: (I) mit 2 und (II) mit 3 multiplizieren:
$$\begin{cases} 4x + 6y = 26 & (I') \\ 15x + 6y = 48 & (II') \end{cases}$$

**Schritt 2**: (II') - (I'):
$$11x = 22$$
$$x = 2$$

**Schritt 3**: In (I) einsetzen:
$$2 \cdot 2 + 3y = 13$$
$$4 + 3y = 13$$
$$3y = 9$$
$$y = 3$$

**Lösung**: $(x, y) = (2, 3)$

## Vergleich der Verfahren

| Verfahren | Wann besonders geeignet |
|---|---|
| Einsetzung | Eine Gleichung ist nach $x$ oder $y$ aufgelöst |
| Gleichsetzung | Beide Gleichungen lassen sich leicht umformen |
| Addition | Koeffizienten sind gleich oder leicht anzugleichen |

## Grafische Interpretation

Jede lineare Gleichung mit zwei Variablen beschreibt eine **Gerade** im Koordinatensystem. Die Lösung des Gleichungssystems ist der **Schnittpunkt** der Geraden.

```
  y
  ↑
  │     ╱
  │    ╱  Gerade 2
  │   ●───── Schnittpunkt (Lösung)
  │  ╱╲
  │ ╱  ╲ Gerade 1
  │╱    ╲
──┼───────→ x
```

## Sonderfälle

### Keine Lösung (parallele Geraden)

$$\begin{cases} x + y = 3 \\ x + y = 5 \end{cases}$$

Beim Lösen: $3 = 5$ → **Widerspruch**

$$\mathbb{L} = \emptyset$$

### Unendlich viele Lösungen (identische Geraden)

$$\begin{cases} x + y = 4 \\ 2x + 2y = 8 \end{cases}$$

Beim Lösen: $0 = 0$ → **Identität**

$$\mathbb{L} = \{(x, y) \mid x + y = 4\}$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ein LGS besteht aus mehreren Gleichungen mit gemeinsamen Variablen
> - Drei Lösungsverfahren: Einsetzen, Gleichsetzen, Addition
> - Die Lösung ist der Schnittpunkt der Geraden
> - Sonderfälle: Keine Lösung (parallel) oder unendlich viele (identisch)
> - Immer Probe in **beiden** Ausgangsgleichungen!

## Übungsaufgaben

Löse die Gleichungssysteme mit einem geeigneten Verfahren:

1. $\begin{cases} y = 3x - 2 \\ y = x + 4 \end{cases}$

2. $\begin{cases} x + y = 10 \\ x - y = 2 \end{cases}$

3. $\begin{cases} 2x + y = 8 \\ x + 2y = 7 \end{cases}$

4. $\begin{cases} 3x - 2y = 4 \\ 6x - 4y = 8 \end{cases}$

5. $\begin{cases} 4x + 3y = 11 \\ 2x - y = 1 \end{cases}$

---

**Navigation**: [[10-Faktorisierung-quadratischer-Gleichungen|← Faktorisierung]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[12-Textaufgaben|Textaufgaben →]]
