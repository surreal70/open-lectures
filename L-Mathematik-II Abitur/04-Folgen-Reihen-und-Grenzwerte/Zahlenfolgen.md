---
author: Andreas Hümmer
title: Zahlenfolgen
tags:
  - content
  - mathe
  - folgen
  - analysis
  - grundlagen
created: 2025-06-17
modified: 2025-06-17
---

# Zahlenfolgen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Zahlenfolge verstehen und formal definieren können
> - Verschiedene Darstellungsformen von Folgen (explizit, rekursiv, grafisch) beherrschen
> - Grundlegende Eigenschaften von Folgen wie Monotonie und Beschränktheit erkennen
> - Folgenglieder berechnen und Bildungsgesetze aus gegebenen Gliedern ableiten können

---

## Überblick

Eine **Zahlenfolge** ist eine geordnete Auflistung von Zahlen nach einer bestimmten Regel. Im Gegensatz zu einer Menge spielt bei Folgen die Reihenfolge eine entscheidende Rolle, und Elemente können mehrfach auftreten. Folgen bilden das mathematische Fundament für das Verständnis von Grenzwerten und damit für die gesamte Analysis.

In der Praxis begegnen uns Folgen überall: Die monatlichen Kontostände eines Sparkontos, die Bevölkerungszahlen eines Landes über die Jahre oder die Näherungswerte bei iterativen Berechnungsverfahren – all das sind Beispiele für Zahlenfolgen.

## Definition und Notation

### Formale Definition

Eine **Zahlenfolge** $(a_n)_{n \in \mathbb{N}}$ ist eine Funktion

$$a: \mathbb{N} \to \mathbb{R}, \quad n \mapsto a_n$$

die jeder natürlichen Zahl $n$ genau eine reelle Zahl $a_n$ zuordnet.

### Notation

- **Folge**: $(a_n)$ oder $(a_n)_{n=1}^{\infty}$ oder $(a_1, a_2, a_3, \ldots)$
- **Folgenglied**: $a_n$ (das $n$-te Glied der Folge)
- **Index**: $n$ (gibt die Position in der Folge an)
- **Startindex**: Meist $n = 1$ oder $n = 0$

**Beispiel:** Die Folge der Quadratzahlen

$$a_n = n^2 \quad \text{ergibt} \quad (1, 4, 9, 16, 25, \ldots)$$

## Darstellungsformen

### Explizite Darstellung

Bei der **expliziten Darstellung** gibt eine Formel direkt den Wert des $n$-ten Glieds an:

$$a_n = f(n)$$

**Beispiele:**
- Quadratzahlen: $a_n = n^2$
- Kehrwerte: $a_n = \frac{1}{n}$
- Alternierende Folge: $a_n = (-1)^n$

**Vorteil:** Jedes Glied kann direkt berechnet werden, ohne die vorherigen zu kennen.

### Rekursive Darstellung

Bei der **rekursiven Darstellung** wird ein Glied aus einem oder mehreren Vorgängern berechnet:

$$a_{n+1} = g(a_n, a_{n-1}, \ldots) \quad \text{mit Startwert(en)}$$

**Beispiele:**
- Verdopplung: $a_{n+1} = 2 \cdot a_n$ mit $a_1 = 1$
- Fibonacci-Folge: $a_{n+2} = a_{n+1} + a_n$ mit $a_1 = a_2 = 1$

**Vorteil:** Natürliche Beschreibung von Prozessen, bei denen der nächste Zustand vom aktuellen abhängt.

### Grafische Darstellung

Folgen können im Koordinatensystem dargestellt werden:

- **x-Achse**: Index $n$
- **y-Achse**: Folgenwert $a_n$
- **Punkte**: $(n, a_n)$

Da $n$ nur natürliche Zahlen annimmt, entsteht eine **diskrete Punktmenge** (keine durchgezogene Linie).

## Eigenschaften von Folgen

### Monotonie

Eine Folge $(a_n)$ heißt:

| Eigenschaft | Definition | Beispiel |
|-------------|------------|----------|
| **monoton wachsend** | $a_{n+1} \geq a_n$ für alle $n$ | $(1, 2, 2, 3, 4, \ldots)$ |
| **streng monoton wachsend** | $a_{n+1} > a_n$ für alle $n$ | $(1, 2, 3, 4, 5, \ldots)$ |
| **monoton fallend** | $a_{n+1} \leq a_n$ für alle $n$ | $(5, 4, 4, 3, 2, \ldots)$ |
| **streng monoton fallend** | $a_{n+1} < a_n$ für alle $n$ | $\left(1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots\right)$ |

**Prüfmethode:** Untersuche das Vorzeichen von $a_{n+1} - a_n$ oder den Quotienten $\frac{a_{n+1}}{a_n}$ (bei positiven Gliedern).

### Beschränktheit

Eine Folge $(a_n)$ heißt:

- **nach oben beschränkt**: Es gibt ein $K \in \mathbb{R}$ mit $a_n \leq K$ für alle $n$
- **nach unten beschränkt**: Es gibt ein $k \in \mathbb{R}$ mit $a_n \geq k$ für alle $n$
- **beschränkt**: Sie ist sowohl nach oben als auch nach unten beschränkt

**Beispiel:** Die Folge $a_n = \frac{1}{n}$ ist:
- nach unten beschränkt durch $k = 0$
- nach oben beschränkt durch $K = 1$
- also beschränkt mit $0 < a_n \leq 1$

### Alternierende Folgen

Eine Folge heißt **alternierend**, wenn aufeinanderfolgende Glieder verschiedene Vorzeichen haben:

$$a_n \cdot a_{n+1} < 0 \quad \text{für alle } n$$

**Typische Form:** $a_n = (-1)^n \cdot b_n$ mit $b_n > 0$

**Beispiel:** $a_n = \frac{(-1)^n}{n}$ ergibt $\left(-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, \ldots\right)$

## Bestimmung von Bildungsgesetzen

### Systematische Vorgehensweise

1. **Differenzen bilden**: $d_n = a_{n+1} - a_n$
   - Konstante Differenz → arithmetische Folge
   
2. **Quotienten bilden**: $q_n = \frac{a_{n+1}}{a_n}$
   - Konstanter Quotient → geometrische Folge
   
3. **Muster erkennen**: Quadratzahlen, Potenzen, Fakultäten, ...

**Beispiel:** Gegeben ist $(2, 5, 10, 17, 26, \ldots)$

Differenzen: $5-2=3$, $10-5=5$, $17-10=7$, $26-17=9$

Die Differenzen $(3, 5, 7, 9, \ldots)$ bilden eine arithmetische Folge!

Die zweiten Differenzen sind konstant ($= 2$), also ist $a_n$ ein quadratisches Polynom:

$$a_n = n^2 + 1$$

**Probe:** $a_1 = 2$, $a_2 = 5$, $a_3 = 10$ ✓

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Arithmetische-Folgen]] – Spezialfall mit konstanter Differenz
- → [[Geometrische-Folgen]] – Spezialfall mit konstantem Quotienten
- → [[Rekursive-Folgen]] – Alternative Darstellungsform
- → [[Konvergenz]] – Grenzwertverhalten von Folgen
- → [[Wiederholung-des-Funktionsbegriffs]] – Folgen als spezielle Funktionen

> [!warning] **Prüfungsrelevant**
> - Unterscheidung explizite/rekursive Darstellung ist Grundwissen
> - Monotonie- und Beschränktheitsuntersuchungen kommen regelmäßig vor
> - Bildungsgesetze aus gegebenen Gliedern ableiten ist eine typische Aufgabe
> - Die Darstellung im Koordinatensystem wird oft zur Veranschaulichung verlangt

> [!question] **Typische Prüfungsfragen**
> - Gib die ersten fünf Glieder der Folge $a_n = \frac{2n+1}{n}$ an und untersuche die Monotonie.
> - Bestimme das Bildungsgesetz der Folge $(3, 7, 11, 15, 19, \ldots)$.
> - Zeige, dass die Folge $a_n = \frac{n}{n+1}$ streng monoton wachsend und beschränkt ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2020.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Grenzwerte-von-Folgen]] – Was passiert mit Folgen "im Unendlichen"?
> - [[Exponentialfunktionen]] – Kontinuierliche Version geometrischer Folgen
