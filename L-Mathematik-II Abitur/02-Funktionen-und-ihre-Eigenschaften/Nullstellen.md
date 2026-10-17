---
author: Andreas Hümmer
title: Nullstellen
tags:
  - content
  - mathe
  - funktionen
  - nullstellen
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Nullstellen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Nullstellen einer Funktion analytisch und graphisch bestimmen können
> - Verschiedene Lösungsverfahren für unterschiedliche Funktionstypen anwenden können
> - Vielfachheit von Nullstellen erkennen und interpretieren können
> - Näherungsverfahren für komplexere Fälle kennen

---

## Überblick

Eine **Nullstelle** einer Funktion $f$ ist ein Wert $x_0$, an dem der Funktionsgraph die $x$-Achse schneidet. Das Auffinden von Nullstellen ist eine der grundlegenden Aufgaben der Analysis und hat vielfältige Anwendungen, etwa beim Lösen von Gleichungen oder bei der Kurvendiskussion.

## Definition

### Formale Definition

Ein Wert $x_0 \in D_f$ heißt **Nullstelle** der Funktion $f$, wenn gilt:

$$f(x_0) = 0$$

Die Menge aller Nullstellen bezeichnen wir als **Nullstellenmenge**:

$$N_f = \{x \in D_f \mid f(x) = 0\}$$

### Geometrische Bedeutung

Nullstellen sind die $x$-Koordinaten der Schnittpunkte des Graphen $G_f$ mit der $x$-Achse.

## Lösungsverfahren nach Funktionstyp

### 1. Lineare Funktionen

Für $f(x) = mx + b$ mit $m \neq 0$:

$$mx + b = 0 \quad \Leftrightarrow \quad x = -\frac{b}{m}$$

**Beispiel:** $f(x) = 3x - 6$
$$x_0 = -\frac{-6}{3} = 2$$

### 2. Quadratische Funktionen

Für $f(x) = ax^2 + bx + c$ mit $a \neq 0$:

**Mitternachtsformel (p-q-Formel in Normalform):**

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Die **Diskriminante** $D = b^2 - 4ac$ bestimmt die Anzahl der Nullstellen:
- $D > 0$: zwei verschiedene Nullstellen
- $D = 0$: eine doppelte Nullstelle
- $D < 0$: keine reellen Nullstellen

**Beispiel:** $f(x) = x^2 - 5x + 6$
$$D = 25 - 24 = 1 > 0$$
$$x_{1,2} = \frac{5 \pm 1}{2} \Rightarrow x_1 = 3, \, x_2 = 2$$

### 3. Polynomfunktionen höheren Grades

**Satz von Vieta:** Für ein Polynom $p(x) = a_n(x-x_1)(x-x_2)\cdots(x-x_n)$ gilt:
- Summe der Nullstellen: $x_1 + x_2 + \cdots + x_n = -\frac{a_{n-1}}{a_n}$
- Produkt der Nullstellen: $x_1 \cdot x_2 \cdots x_n = (-1)^n \frac{a_0}{a_n}$

**Verfahren:**
1. **Raten und Verifizieren:** Ganzzahlige Nullstellen sind Teiler von $a_0$
2. **Polynomdivision:** Nach Finden einer Nullstelle $x_0$ durch $(x - x_0)$ dividieren
3. **Substitution:** Bei biquadratischen Gleichungen ($ax^4 + bx^2 + c = 0$)

**Beispiel:** $f(x) = x^3 - 6x^2 + 11x - 6$

Teiler von $a_0 = -6$: $\pm 1, \pm 2, \pm 3, \pm 6$

Test: $f(1) = 1 - 6 + 11 - 6 = 0$ ✓

Polynomdivision: $(x^3 - 6x^2 + 11x - 6) : (x-1) = x^2 - 5x + 6$

Nullstellen von $x^2 - 5x + 6$: $x_2 = 2$, $x_3 = 3$

Also: $N_f = \{1, 2, 3\}$

### 4. Exponential- und Logarithmusfunktionen

**Exponentialfunktionen:** $e^x > 0$ für alle $x$, daher hat $f(x) = e^x$ keine Nullstellen.

Bei kombinierten Funktionen:
$$f(x) = e^x - 2 = 0 \quad \Leftrightarrow \quad e^x = 2 \quad \Leftrightarrow \quad x = \ln 2$$

**Logarithmusfunktionen:** $\ln(x) = 0 \Leftrightarrow x = 1$

### 5. Trigonometrische Funktionen

$$\sin(x) = 0 \quad \Leftrightarrow \quad x = k\pi, \, k \in \mathbb{Z}$$
$$\cos(x) = 0 \quad \Leftrightarrow \quad x = \frac{\pi}{2} + k\pi, \, k \in \mathbb{Z}$$
$$\tan(x) = 0 \quad \Leftrightarrow \quad x = k\pi, \, k \in \mathbb{Z}$$

### 6. Produkte von Funktionen

Für $f(x) = g(x) \cdot h(x)$ gilt nach dem **Nullproduktsatz**:

$$f(x) = 0 \quad \Leftrightarrow \quad g(x) = 0 \text{ oder } h(x) = 0$$

**Beispiel:** $f(x) = x \cdot e^x$
- $x = 0$ liefert Nullstelle (da $e^0 = 1 \neq 0$)
- $e^x = 0$ hat keine Lösung

Einzige Nullstelle: $x_0 = 0$

## Vielfachheit von Nullstellen

### Definition

Eine Nullstelle $x_0$ hat die **Vielfachheit** (oder Ordnung) $k$, wenn gilt:

$$f(x) = (x - x_0)^k \cdot g(x) \quad \text{mit } g(x_0) \neq 0$$

### Charakterisierung über Ableitungen

Eine Nullstelle $x_0$ hat genau die Vielfachheit $k$, wenn:
$$f(x_0) = f'(x_0) = \cdots = f^{(k-1)}(x_0) = 0 \quad \text{und} \quad f^{(k)}(x_0) \neq 0$$

### Graphisches Verhalten

| Vielfachheit | Verhalten am Graphen |
|-------------|---------------------|
| $k = 1$ (einfach) | Graph schneidet die $x$-Achse |
| $k = 2$ (doppelt) | Graph berührt die $x$-Achse (Wendepunkt mit horizontaler Tangente) |
| $k = 3$ (dreifach) | Graph schneidet die $x$-Achse mit Wendepunkt |
| $k$ gerade | Graph berührt, kein Vorzeichenwechsel |
| $k$ ungerade | Graph schneidet, Vorzeichenwechsel |

**Beispiel:** $f(x) = (x-1)^2(x+2)$

- $x_1 = 1$ ist doppelte Nullstelle (Graph berührt)
- $x_2 = -2$ ist einfache Nullstelle (Graph schneidet)

## Näherungsverfahren

### Newton-Verfahren

Für Funktionen, deren Nullstellen nicht analytisch bestimmbar sind:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**Voraussetzungen:**
- $f$ ist differenzierbar
- Startwert $x_0$ nahe genug an der Nullstelle
- $f'(x) \neq 0$ in der Nähe der Nullstelle

**Beispiel:** $f(x) = x^3 - 2$ (Nullstelle ist $\sqrt[3]{2}$)

Mit $x_0 = 1$:
$$x_1 = 1 - \frac{1-2}{3 \cdot 1} = 1 + \frac{1}{3} = \frac{4}{3} \approx 1.333$$
$$x_2 = \frac{4}{3} - \frac{(\frac{4}{3})^3 - 2}{3(\frac{4}{3})^2} \approx 1.264$$

Exakter Wert: $\sqrt[3]{2} \approx 1.2599$

### Intervallhalbierungsverfahren (Bisektionsmethode)

Wenn $f$ stetig ist und $f(a) \cdot f(b) < 0$ (Vorzeichenwechsel), dann existiert mindestens eine Nullstelle im Intervall $(a, b)$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Schnittpunkte]] – Nullstellen sind Spezialfall: Schnitt mit der $x$-Achse
- → [[Faktorisierung-von-Polynomen]] – Zerlegung in Linearfaktoren mithilfe von Nullstellen
- → [[Polynomdivision]] – Technik zur Reduktion des Grades nach Finden einer Nullstelle
- → [[Gleichungen-hoeheren-Grades]] – Lösen von Polynomgleichungen

> [!warning] **Prüfungsrelevant**
> - Systematisches Finden von Nullstellen bei Polynomen (Teiler von $a_0$ testen)
> - Anwendung der Mitternachtsformel und Interpretation der Diskriminante
> - Nullproduktsatz bei Produkten von Funktionen
> - Erkennen und Interpretieren der Vielfachheit von Nullstellen

> [!question] **Typische Prüfungsfragen**
> - Bestimme alle Nullstellen von $f(x) = x^4 - 5x^2 + 4$ und gib deren Vielfachheit an.
> - Für welche Werte von $a$ hat $f(x) = x^2 + ax + 9$ genau eine (doppelte) Nullstelle?
> - Zeige, dass $f(x) = e^x - x - 2$ genau eine positive Nullstelle besitzt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Polynomfunktionen]] – Systematische Behandlung von Polynomen
> - [[Exponentialfunktionen]] – Nullstellen bei Exponentialgleichungen
> - [[Konvergenz]] – Konvergenz von Näherungsverfahren
