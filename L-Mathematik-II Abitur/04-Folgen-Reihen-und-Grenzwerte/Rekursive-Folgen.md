---
author: Andreas Hümmer
title: Rekursive Folgen
tags:
  - content
  - mathe
  - folgen
  - rekursion
  - fibonacci
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Rekursive Folgen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Prinzip der rekursiven Definition verstehen und anwenden können
> - Folgenglieder aus einer Rekursionsvorschrift berechnen können
> - Verschiedene Typen rekursiver Folgen unterscheiden können
> - Die Fibonacci-Folge und ihre Eigenschaften kennen
> - Rekursive Folgen in explizite umwandeln (in einfachen Fällen)

---

## Überblick

Eine **rekursive Folge** ist eine Folge, bei der jedes Glied aus einem oder mehreren Vorgängern berechnet wird. Im Gegensatz zur expliziten Darstellung, die jeden Folgenwert direkt aus $n$ berechnet, beschreibt die rekursive Darstellung den "Prozess" der Folgenbildung.

Rekursive Definitionen sind in der Informatik allgegenwärtig (rekursive Algorithmen) und modellieren natürliche Prozesse, bei denen der nächste Zustand vom aktuellen abhängt: Populationsdynamik, Spinnweben, iterative Näherungsverfahren.

## Definition und Struktur

### Bestandteile einer rekursiven Definition

Eine rekursive Folgendefinition besteht aus:

1. **Startwert(en)**: Ein oder mehrere Anfangsglieder $a_1, a_2, \ldots$
2. **Rekursionsvorschrift**: Eine Formel, die $a_{n+1}$ (oder $a_n$) aus Vorgängern berechnet

### Rekursionsordnung

Die **Ordnung** einer Rekursion gibt an, wie viele Vorgänger zur Berechnung des nächsten Glieds benötigt werden:

| Ordnung | Vorschrift | Startwerte |
|---------|------------|------------|
| 1. Ordnung | $a_{n+1} = f(a_n)$ | $a_1$ |
| 2. Ordnung | $a_{n+1} = f(a_n, a_{n-1})$ | $a_1, a_2$ |
| k. Ordnung | $a_{n+1} = f(a_n, a_{n-1}, \ldots, a_{n-k+1})$ | $a_1, \ldots, a_k$ |

## Rekursionen 1. Ordnung

### Lineare Rekursionen

Die allgemeine Form lautet:
$$a_{n+1} = c \cdot a_n + d$$

**Spezialfälle:**
- $d = 0$: Geometrische Folge mit $q = c$
- $c = 1$: Arithmetische Folge mit Differenz $d$

**Beispiel:** $a_{n+1} = 2a_n + 1$ mit $a_1 = 1$

Berechnung der ersten Glieder:
- $a_1 = 1$
- $a_2 = 2 \cdot 1 + 1 = 3$
- $a_3 = 2 \cdot 3 + 1 = 7$
- $a_4 = 2 \cdot 7 + 1 = 15$
- $a_5 = 2 \cdot 15 + 1 = 31$

**Explizite Formel:** $a_n = 2^n - 1$

### Nichtlineare Rekursionen

**Beispiel: Logistische Rekursion** (Populationsmodell)

$$a_{n+1} = r \cdot a_n \cdot (1 - a_n)$$

Diese Rekursion modelliert begrenztes Wachstum und zeigt für verschiedene Werte von $r$ unterschiedliches Verhalten (Konvergenz, Oszillation, Chaos).

## Rekursionen 2. Ordnung

### Die Fibonacci-Folge

Die berühmteste Rekursion 2. Ordnung:

$$a_{n+2} = a_{n+1} + a_n \quad \text{mit } a_1 = 1, a_2 = 1$$

Die Folge lautet: $(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \ldots)$

**Eigenschaften der Fibonacci-Folge:**

1. **Goldener Schnitt:** Der Quotient $\frac{a_{n+1}}{a_n}$ konvergiert gegen $\phi = \frac{1 + \sqrt{5}}{2} \approx 1,618$

2. **Summenformel:** $\sum_{k=1}^{n} a_k = a_{n+2} - 1$

3. **Explizite Formel (Binet):**
$$a_n = \frac{1}{\sqrt{5}} \left[ \left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n \right]$$

### Allgemeine lineare Rekursion 2. Ordnung

$$a_{n+2} = p \cdot a_{n+1} + q \cdot a_n$$

**Lösungsansatz über charakteristische Gleichung:**

$$x^2 = p \cdot x + q \quad \Leftrightarrow \quad x^2 - px - q = 0$$

Die Lösungen $x_1, x_2$ bestimmen die explizite Form:
- Verschiedene Lösungen: $a_n = A \cdot x_1^n + B \cdot x_2^n$
- Doppelte Lösung $x_0$: $a_n = (A + Bn) \cdot x_0^n$

## Umwandlung: Rekursiv ↔ Explizit

### Von rekursiv zu explizit

**Strategie 1: Musterkennung**
Berechne mehrere Glieder und suche ein Muster.

**Beispiel:** $a_{n+1} = a_n + 2n + 1$ mit $a_1 = 1$

| $n$ | $a_n$ | Differenz |
|-----|-------|-----------|
| 1 | 1 | — |
| 2 | 4 | 3 |
| 3 | 9 | 5 |
| 4 | 16 | 7 |
| 5 | 25 | 9 |

Vermutung: $a_n = n^2$

**Probe:** $a_{n+1} = (n+1)^2 = n^2 + 2n + 1 = a_n + 2n + 1$ ✓

**Strategie 2: Teleskopsumme**

Für $a_{n+1} = a_n + f(n)$:

$$a_n = a_1 + \sum_{k=1}^{n-1} f(k)$$

### Von explizit zu rekursiv

**Beispiel:** $a_n = 3^n$

Rekursive Form: $a_{n+1} = 3 \cdot a_n$ mit $a_1 = 3$

**Beweis:** $a_{n+1} = 3^{n+1} = 3 \cdot 3^n = 3 \cdot a_n$ ✓

## Fixpunkte und Konvergenz

### Definition Fixpunkt

Ein **Fixpunkt** der Rekursion $a_{n+1} = f(a_n)$ ist ein Wert $x^*$ mit:

$$f(x^*) = x^*$$

**Interpretation:** Wenn die Folge den Wert $x^*$ erreicht, bleibt sie dort.

### Konvergenzverhalten

Für eine konvergente Folge mit $\lim_{n \to \infty} a_n = L$ gilt:

$$L = f(L)$$

Der Grenzwert muss ein Fixpunkt sein!

**Beispiel:** $a_{n+1} = \sqrt{2 + a_n}$ mit $a_1 = 0$

Fixpunktgleichung: $x = \sqrt{2 + x}$
$$x^2 = 2 + x \quad \Rightarrow \quad x^2 - x - 2 = 0 \quad \Rightarrow \quad x = 2 \text{ (da } x \geq 0\text{)}$$

Die Folge konvergiert gegen $L = 2$.

## Anwendungsbeispiel: Heron-Verfahren

Das **Heron-Verfahren** zur Berechnung von $\sqrt{a}$:

$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right) \quad \text{mit } x_1 > 0$$

**Berechnung von $\sqrt{2}$ mit $x_1 = 1$:**

| $n$ | $x_n$ |
|-----|-------|
| 1 | 1 |
| 2 | 1,5 |
| 3 | 1,41667 |
| 4 | 1,41422 |
| 5 | 1,41421... |

Das Verfahren konvergiert sehr schnell (quadratische Konvergenz).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zahlenfolgen]] – Allgemeiner Folgenbegriff und explizite Darstellung
- → [[Arithmetische-Folgen]] – Spezialfall rekursiver Folgen mit $a_{n+1} = a_n + d$
- → [[Geometrische-Folgen]] – Spezialfall rekursiver Folgen mit $a_{n+1} = q \cdot a_n$
- → [[Konvergenz]] – Grenzwertverhalten rekursiver Folgen
- → [[Grenzwerte-von-Folgen]] – Berechnung von Grenzwerten über Fixpunkte

> [!warning] **Prüfungsrelevant**
> - Berechnung von Folgengliedern aus Rekursionsvorschrift ist Grundwissen
> - Die Fibonacci-Folge und ihre Eigenschaften werden gerne abgefragt
> - Fixpunktberechnung zur Grenzwertbestimmung ist ein wichtiges Werkzeug
> - Umwandlung einfacher Rekursionen in explizite Form kann verlangt werden
> - Iterative Näherungsverfahren (wie Heron) erscheinen in Anwendungsaufgaben

> [!question] **Typische Prüfungsfragen**
> - Berechne die ersten 6 Glieder der Folge $a_{n+1} = 3a_n - 2$ mit $a_1 = 1$. Finde das explizite Bildungsgesetz.
> - Zeige, dass die Folge $a_{n+1} = \frac{1}{2}(a_n + 3)$ gegen einen Grenzwert konvergiert, und bestimme diesen.
> - Die Fibonacci-Folge ist definiert durch $F_{n+2} = F_{n+1} + F_n$ mit $F_1 = F_2 = 1$. Zeige, dass $F_1 + F_2 + \ldots + F_n = F_{n+2} - 1$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Aigner, M.: Diskrete Mathematik. Vieweg+Teubner, 2006.

> [!tip] **Weiterführende Links**
> - [[Wachstumsprozesse]] – Rekursive Modelle in der Anwendung
> - [[Einfuehrung-in-die-mathematische-Grenzwertbildung]] – Formale Konvergenzbeweise
