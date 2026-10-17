---
author: Andreas Hümmer
title: Numerische Integration – Grundlagen
tags:
  - content
  - mathe
  - integralrechnung
  - numerik
  - naeherungsverfahren
created: 2025-06-26
modified: 2025-06-26
---

# Numerische Integration – Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verstehen, wann numerische Integration notwendig ist
> - Die Rechteck- und Trapezregel anwenden können
> - Die Simpson-Regel kennen und anwenden können
> - Die Genauigkeit der verschiedenen Verfahren einschätzen können

---

## Überblick

Nicht jedes Integral lässt sich analytisch (mit einer Formel) berechnen. Integrale wie:

$$\int e^{-x^2} \, dx, \quad \int \frac{\sin x}{x} \, dx, \quad \int \sqrt{1 + x^4} \, dx$$

besitzen keine elementaren Stammfunktionen. Hier benötigt man **numerische Verfahren** zur näherungsweisen Berechnung.

Auch bei Messdaten, die nur als diskrete Werte vorliegen, ist numerische Integration der einzige Weg.

---

## Grundprinzip: Zerlegung und Approximation

Alle numerischen Integrationsverfahren basieren auf demselben Prinzip:

1. **Zerlege** das Intervall $[a, b]$ in $n$ Teilintervalle
2. **Approximiere** die Fläche in jedem Teilintervall durch einfache geometrische Formen
3. **Summiere** alle Teilflächen

Je feiner die Zerlegung (größeres $n$), desto genauer das Ergebnis.

---

## Die Rechteckregel

### Linke Rechteckregel

Approximiere die Funktion in jedem Teilintervall durch eine Konstante (den linken Randwert):

$$\int_a^b f(x) \, dx \approx \sum_{i=0}^{n-1} f(x_i) \cdot h$$

mit Schrittweite $h = \frac{b-a}{n}$ und Stützstellen $x_i = a + i \cdot h$.

```
  f(x) ↑
       │  ┌──┐     ┌──┐
       │  │  │┌──┐ │  │
       │  │  ││  │ │  │
       │  │  ││  │ │  │
     ──┼──┴──┴┴──┴─┴──┴──→ x
       a            b
```

### Mittelpunktsregel (genauer)

Verwende den Funktionswert in der Mitte jedes Teilintervalls:

$$\int_a^b f(x) \, dx \approx \sum_{i=0}^{n-1} f\left(x_i + \frac{h}{2}\right) \cdot h$$

### Beispiel

Berechne $\int_0^1 x^2 \, dx$ mit der linken Rechteckregel und $n = 4$.

**Schrittweite:** $h = \frac{1-0}{4} = 0{,}25$

**Stützstellen und Funktionswerte:**

| $i$ | $x_i$ | $f(x_i) = x_i^2$ |
|-----|-------|------------------|
| 0 | 0,00 | 0,0000 |
| 1 | 0,25 | 0,0625 |
| 2 | 0,50 | 0,2500 |
| 3 | 0,75 | 0,5625 |

**Näherung:**
$$I \approx 0{,}25 \cdot (0 + 0{,}0625 + 0{,}25 + 0{,}5625) = 0{,}25 \cdot 0{,}875 = 0{,}21875$$

**Exakter Wert:** $\int_0^1 x^2 \, dx = \frac{1}{3} \approx 0{,}3333$

**Fehler:** ca. 34% – die Rechteckregel ist recht ungenau.

---

## Die Trapezregel

### Prinzip

Verbinde benachbarte Funktionswerte durch Geraden und berechne die Fläche der entstehenden Trapeze:

$$\int_a^b f(x) \, dx \approx h \cdot \left(\frac{f(a) + f(b)}{2} + \sum_{i=1}^{n-1} f(x_i)\right)$$

Oder kurz:

$$T_n = \frac{h}{2} \left(f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right)$$

```
  f(x) ↑
       │    ╱╲
       │   ╱  ╲    Trapeze statt Rechtecke
       │  ╱    ╲
       │ ╱      ╲
     ──┼─────────────→ x
       a          b
```

### Beispiel

Berechne $\int_0^1 x^2 \, dx$ mit der Trapezregel und $n = 4$.

**Stützstellen und Funktionswerte:**

| $i$ | $x_i$ | $f(x_i)$ | Gewicht |
|-----|-------|----------|---------|
| 0 | 0,00 | 0,0000 | 1 |
| 1 | 0,25 | 0,0625 | 2 |
| 2 | 0,50 | 0,2500 | 2 |
| 3 | 0,75 | 0,5625 | 2 |
| 4 | 1,00 | 1,0000 | 1 |

**Berechnung:**
$$T_4 = \frac{0{,}25}{2} (0 + 2 \cdot 0{,}0625 + 2 \cdot 0{,}25 + 2 \cdot 0{,}5625 + 1)$$
$$= 0{,}125 \cdot (0 + 0{,}125 + 0{,}5 + 1{,}125 + 1) = 0{,}125 \cdot 2{,}75 = 0{,}34375$$

**Fehler:** ca. 3% – deutlich besser als die Rechteckregel!

---

## Die Simpson-Regel (Keplersche Fassregel)

### Prinzip

Approximiere die Funktion durch **Parabeln** statt durch Geraden. Dazu werden je drei aufeinanderfolgende Punkte durch eine Parabel verbunden.

$$\int_a^b f(x) \, dx \approx \frac{h}{3} \left(f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)\right)$$

> [!warning] **Wichtig**
> Die Simpson-Regel erfordert eine **gerade Anzahl** von Teilintervallen ($n$ gerade).

### Gewichtsmuster

Die Gewichte folgen dem Muster: $1, 4, 2, 4, 2, 4, \ldots, 4, 2, 4, 1$

### Beispiel

Berechne $\int_0^1 x^2 \, dx$ mit der Simpson-Regel und $n = 4$.

| $i$ | $x_i$ | $f(x_i)$ | Gewicht |
|-----|-------|----------|---------|
| 0 | 0,00 | 0,0000 | 1 |
| 1 | 0,25 | 0,0625 | 4 |
| 2 | 0,50 | 0,2500 | 2 |
| 3 | 0,75 | 0,5625 | 4 |
| 4 | 1,00 | 1,0000 | 1 |

**Berechnung:**
$$S_4 = \frac{0{,}25}{3} (1 \cdot 0 + 4 \cdot 0{,}0625 + 2 \cdot 0{,}25 + 4 \cdot 0{,}5625 + 1 \cdot 1)$$
$$= \frac{0{,}25}{3} (0 + 0{,}25 + 0{,}5 + 2{,}25 + 1) = \frac{0{,}25}{3} \cdot 4 = \frac{1}{3} \approx 0{,}3333$$

**Fehler:** 0% – die Simpson-Regel liefert für Polynome bis Grad 3 das exakte Ergebnis!

---

## Vergleich der Verfahren

| Verfahren | Approximation durch | Fehlerordnung | Genauigkeit |
|-----------|---------------------|---------------|-------------|
| Rechteckregel | Konstanten | $O(h)$ | niedrig |
| Trapezregel | Geraden | $O(h^2)$ | mittel |
| Simpson-Regel | Parabeln | $O(h^4)$ | hoch |

**Fehlerordnung $O(h^k)$** bedeutet: Halbiert man die Schrittweite $h$, reduziert sich der Fehler um den Faktor $2^k$.

---

## Praktische Anwendung

### Bei Messdaten

Liegen nur diskrete Messwerte vor (z.B. Geschwindigkeit zu bestimmten Zeitpunkten), ist die numerische Integration der einzige Weg:

| Zeit $t$ [s] | 0 | 1 | 2 | 3 | 4 |
|--------------|---|---|---|---|---|
| Geschw. $v$ [m/s] | 0 | 5 | 12 | 18 | 20 |

**Weg mit Trapezregel:**
$$s = 1 \cdot \left(\frac{0+20}{2} + 5 + 12 + 18\right) = 10 + 35 = 45 \text{ m}$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Die analytische Alternative
- → [[Flaechenberechnung|Flächenberechnung]] – Motivation für Integration
- → [[Mittelwert-einer-Funktion|Mittelwert einer Funktion]] – Numerische Berechnung von Mittelwerten
- → [[Weg-Geschwindigkeit-und-Beschleunigung|Weg, Geschwindigkeit und Beschleunigung]] – Praktische Anwendung
- → [[Zahlenfolgen|Zahlenfolgen]] – Grundlage diskreter Daten

> [!warning] **Prüfungsrelevant**
> - Die **Trapezregel** ist die wichtigste Formel: Randwerte einfach, innere Werte doppelt gewichten
> - Bei der **Simpson-Regel**: Gewichte 1-4-2-4-...-4-1 und $n$ muss gerade sein
> - Je mehr Stützstellen, desto genauer das Ergebnis
> - Die Simpson-Regel ist genau für Polynome bis Grad 3

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int_0^2 e^x \, dx$ näherungsweise mit der Trapezregel und $n = 4$ Teilintervallen.
> - Erkläre, warum die Simpson-Regel genauer ist als die Trapezregel.
> - Ein Auto beschleunigt mit gemessenen Geschwindigkeiten. Berechne den zurückgelegten Weg mit der Trapezregel.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Bestimmte-Integrale|Bestimmte Integrale]] – Analytische Integrationsmethoden
> - [[Mittelwert-einer-Funktion|Mittelwert einer Funktion]] – Anwendung auf Mittelwertberechnung
