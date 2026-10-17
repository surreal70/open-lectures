---
author: Andreas Hümmer
title: Polynomdivision
tags:
  - content
  - mathe
  - algebra
  - polynome
  - polynomdivision
  - nullstellen
created: 2025-01-13
modified: 2025-01-13
---

# Polynomdivision

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Polynomdivision algorithmisch durchführen können
> - Linearfaktoren abspalten können, wenn eine Nullstelle bekannt ist
> - Den Zusammenhang zwischen Nullstellen und Linearfaktoren verstehen
> - Das Horner-Schema als effiziente Alternative anwenden können

---

## Überblick

Die Polynomdivision ist ein Verfahren zur Division von Polynomen, analog zur schriftlichen Division bei natürlichen Zahlen. Sie ist ein wichtiges Werkzeug, um Polynome höheren Grades zu faktorisieren und deren Nullstellen zu bestimmen. Besonders beim Abspalten von Linearfaktoren, wenn eine Nullstelle bekannt ist, kommt sie häufig zum Einsatz.

## Grundlagen

### Was ist ein Polynom?

Ein **Polynom** in $x$ vom Grad $n$ hat die Form:

$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$$

wobei $a_n \neq 0$ (Leitkoeffizient) und $a_0, a_1, \ldots, a_n \in \mathbb{R}$.

**Beispiele:**
- $p(x) = 2x^3 - 5x^2 + 3x - 1$ (Grad 3)
- $q(x) = x^2 + 2x + 1$ (Grad 2)

### Division von Polynomen

Für Polynome $p(x)$ und $d(x)$ mit $\text{Grad}(d) \leq \text{Grad}(p)$ gibt es eindeutige Polynome $q(x)$ (Quotient) und $r(x)$ (Rest) mit:

$$p(x) = d(x) \cdot q(x) + r(x) \quad \text{wobei } \text{Grad}(r) < \text{Grad}(d)$$

## Der Divisionsalgorithmus

Die Polynomdivision verläuft analog zur schriftlichen Division.

### Beispiel: $(2x^3 + 3x^2 - 5x + 6) : (x - 2)$

```
 2x³ + 3x² - 5x + 6  :  (x - 2)  =  2x² + 7x + 9
-( 2x³ - 4x²)
 ─────────────
        7x² - 5x
      -(7x² - 14x)
       ───────────
              9x + 6
            -(9x - 18)
             ─────────
                   24
```

**Ergebnis:** $(2x^3 + 3x^2 - 5x + 6) : (x - 2) = 2x^2 + 7x + 9 + \frac{24}{x-2}$

**Schrittweise Vorgehensweise:**

1. **Teile** den führenden Term des Dividenden durch den führenden Term des Divisors: $2x^3 : x = 2x^2$

2. **Multipliziere** das Ergebnis mit dem gesamten Divisor: $2x^2 \cdot (x - 2) = 2x^3 - 4x^2$

3. **Subtrahiere** vom Dividenden: $(2x^3 + 3x^2) - (2x^3 - 4x^2) = 7x^2$

4. **Hole** den nächsten Term herunter und wiederhole ab Schritt 1

## Abspalten von Linearfaktoren

### Satz über Linearfaktoren

> Ist $x_0$ eine Nullstelle von $p(x)$, so ist $(x - x_0)$ ein Teiler von $p(x)$.

Das bedeutet: Wenn $p(x_0) = 0$, dann geht die Division $p(x) : (x - x_0)$ **ohne Rest** auf.

### Beispiel: Faktorisierung von $p(x) = x^3 - 6x^2 + 11x - 6$

**Schritt 1:** Nullstelle raten (Teiler des konstanten Glieds probieren)

Kandidaten: $\pm 1, \pm 2, \pm 3, \pm 6$

$p(1) = 1 - 6 + 11 - 6 = 0$ ✓

**Schritt 2:** Polynomdivision durchführen

```
 x³ - 6x² + 11x - 6  :  (x - 1)  =  x² - 5x + 6
-(x³ - x²)
 ─────────
     -5x² + 11x
    -(-5x² + 5x)
     ──────────
           6x - 6
          -(6x - 6)
           ───────
               0
```

**Schritt 3:** Restpolynom weiter faktorisieren

$x^2 - 5x + 6 = (x - 2)(x - 3)$

**Ergebnis:**
$$p(x) = x^3 - 6x^2 + 11x - 6 = (x - 1)(x - 2)(x - 3)$$

## Das Horner-Schema

Das **Horner-Schema** ist eine effiziente Methode zur Polynomdivision durch Linearfaktoren $(x - x_0)$.

### Aufbau des Schemas

Für $p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$ und Division durch $(x - x_0)$:

| | $a_n$ | $a_{n-1}$ | $a_{n-2}$ | $\ldots$ | $a_1$ | $a_0$ |
|---|---|---|---|---|---|---|
| $x_0$ | | $\cdot x_0$ | $\cdot x_0$ | $\ldots$ | $\cdot x_0$ | $\cdot x_0$ |
| | $b_n$ | $b_{n-1}$ | $b_{n-2}$ | $\ldots$ | $b_1$ | $r$ |

Dabei ist $b_n = a_n$ und $b_k = a_k + b_{k+1} \cdot x_0$.

### Beispiel: $(2x^3 + 3x^2 - 5x + 6) : (x - 2)$

| | 2 | 3 | -5 | 6 |
|---|---|---|---|---|
| 2 | | 4 | 14 | 18 |
| | 2 | 7 | 9 | **24** |

**Ergebnis:** Quotient $2x^2 + 7x + 9$, Rest $24$

> [!tip] **Vorteil des Horner-Schemas**
> Das Horner-Schema ist schneller als die klassische Polynomdivision und zeigt sofort den Funktionswert $p(x_0)$ im Rest an. Ist der Rest 0, ist $x_0$ eine Nullstelle.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Faktorisierung-von-Polynomen]] – Systematische Zerlegung in Faktoren
- → [[Gleichungen-hoeheren-Grades]] – Lösen von Polynomgleichungen
- → [[Polynomfunktionen]] – Eigenschaften von Polynomfunktionen
- → [[Nullstellen]] – Bestimmung von Nullstellen

> [!warning] **Prüfungsrelevant**
> - Durchführung der Polynomdivision (ohne Taschenrechner)
> - Abspalten von Linearfaktoren bei bekannter Nullstelle
> - Vollständige Faktorisierung von Polynomen
> - Anwendung des Horner-Schemas

> [!question] **Typische Prüfungsfragen**
> - Führe die Division $(x^4 - 3x^3 + 2x^2 - x + 3) : (x^2 - 2)$ durch.
> - Zeige, dass $x = 2$ eine Nullstelle von $p(x) = x^3 - 7x + 6$ ist, und faktorisiere vollständig.
> - Bestimme mit dem Horner-Schema den Wert von $p(3)$ für $p(x) = 2x^4 - 3x^3 + x - 5$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Polynom|Glossar: Polynom]]
> - [[Glossar#Linearfaktor|Glossar: Linearfaktor]]
