---
author: Andreas Hümmer
title: Exponentialfunktionen
tags:
  - content
  - mathe
  - funktionen
  - exponentialfunktion
  - wachstum
  - zerfall
created: 2025-06-19
modified: 2025-06-19
---

# Exponentialfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Exponentialfunktionen von Potenzfunktionen unterscheiden können
> - Die natürliche Exponentialfunktion $e^x$ und ihre besondere Bedeutung kennen
> - Wachstums- und Zerfallsprozesse mathematisch modellieren können
> - Graphen von Exponentialfunktionen analysieren und transformieren können

---

## Überblick

Exponentialfunktionen haben die Basis als feste Zahl und die Variable im Exponenten — das Gegenteil von Potenzfunktionen. Sie beschreiben Prozesse mit konstanter prozentualer Änderungsrate wie Bevölkerungswachstum, radioaktiven Zerfall oder Zinseszins. Die natürliche Exponentialfunktion $e^x$ nimmt dabei eine Sonderstellung ein: Sie ist die einzige Funktion, die mit ihrer eigenen Ableitung übereinstimmt.

## Definition

### Allgemeine Exponentialfunktion

$$f(x) = a^x \quad \text{mit } a > 0, \, a \neq 1$$

| Parameter | Bedingung | Verhalten |
|-----------|-----------|-----------|
| $a > 1$ | Wachstum | streng monoton steigend |
| $0 < a < 1$ | Zerfall | streng monoton fallend |
| $a = 1$ | — | konstant $f(x) = 1$ (Sonderfall) |

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R}$ |
| Wertebereich | $W_f = (0, +\infty)$ |
| Nullstellen | keine |
| y-Achsenabschnitt | $f(0) = 1$ |
| Asymptote | $y = 0$ (horizontale Asymptote) |
| Stetigkeit | stetig auf ganz $\mathbb{R}$ |

### Graph

Für $a > 1$:

```
     y
     │         ╱
     │       ╱
     │     ╱
   1─┼───•
     │  ╱
─────┼──────────── x
     │
```

Der Graph liegt stets oberhalb der x-Achse und schneidet die y-Achse bei $(0|1)$.

## Die Eulersche Zahl und die natürliche Exponentialfunktion

### Definition der Eulerschen Zahl

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2{,}71828...$$

Die Eulersche Zahl $e$ ist eine irrationale, transzendente Zahl.

### Die natürliche Exponentialfunktion

$$f(x) = e^x = \exp(x)$$

**Besondere Eigenschaft:**

$$\frac{d}{dx} e^x = e^x$$

Die natürliche Exponentialfunktion ist die einzige Funktion, die gleich ihrer eigenen Ableitung ist (bis auf konstante Faktoren).

### Funktionswerte

| $x$ | $e^x$ (gerundet) |
|-----|------------------|
| $-2$ | $0{,}135$ |
| $-1$ | $0{,}368$ |
| $0$ | $1$ |
| $1$ | $2{,}718$ |
| $2$ | $7{,}389$ |

## Rechenregeln

### Potenzgesetze für Exponentialfunktionen

Für $a > 0$ und $x, y \in \mathbb{R}$:

$$a^{x+y} = a^x \cdot a^y$$
$$a^{x-y} = \frac{a^x}{a^y}$$
$$\left(a^x\right)^y = a^{x \cdot y}$$
$$a^0 = 1$$
$$a^{-x} = \frac{1}{a^x}$$

### Basiswechsel

Jede Exponentialfunktion lässt sich auf die Basis $e$ umschreiben:

$$a^x = e^{x \ln(a)}$$

**Beispiel:** $2^x = e^{x \ln 2} \approx e^{0{,}693x}$

## Transformationen

### Allgemeine Form

$$f(x) = c \cdot a^{k(x-b)} + d$$

| Parameter | Wirkung |
|-----------|---------|
| $c$ | Streckung/Stauchung in y-Richtung, Spiegelung für $c < 0$ |
| $a$ | Basis: bestimmt Wachstums-/Zerfallsrate |
| $k$ | Streckung/Stauchung in x-Richtung |
| $b$ | Verschiebung in x-Richtung |
| $d$ | Verschiebung in y-Richtung (neue Asymptote) |

### Wichtige Spezialfälle

$$f(x) = e^{-x} = \frac{1}{e^x}$$

Graph von $e^x$ an der y-Achse gespiegelt → Zerfallsfunktion.

$$f(x) = e^x + d$$

Horizontale Asymptote verschiebt sich von $y = 0$ zu $y = d$.

## Wachstums- und Zerfallsprozesse

### Exponentielles Wachstum

$$N(t) = N_0 \cdot e^{kt} \quad \text{mit } k > 0$$

- $N_0$ — Anfangswert zum Zeitpunkt $t = 0$
- $k$ — Wachstumskonstante (Wachstumsrate)
- $N(t)$ — Wert zum Zeitpunkt $t$

**Verdopplungszeit:**

$$t_2 = \frac{\ln 2}{k} \approx \frac{0{,}693}{k}$$

### Exponentieller Zerfall

$$N(t) = N_0 \cdot e^{-\lambda t} \quad \text{mit } \lambda > 0$$

- $\lambda$ — Zerfallskonstante

**Halbwertszeit:**

$$t_{1/2} = \frac{\ln 2}{\lambda}$$

### Beispiel: Radioaktiver Zerfall

Kohlenstoff-14 hat eine Halbwertszeit von ca. 5730 Jahren.

$$\lambda = \frac{\ln 2}{5730} \approx 0{,}000121 \text{ pro Jahr}$$

Nach 10000 Jahren ist der Anteil:

$$\frac{N(10000)}{N_0} = e^{-0{,}000121 \cdot 10000} \approx 0{,}298 = 29{,}8\%$$

### Begrenztes Wachstum

$$f(t) = S - (S - f_0) \cdot e^{-kt}$$

- $S$ — Sättigungsgrenze (obere Schranke)
- $f_0$ — Anfangswert
- Asymptotische Annäherung an $S$

## Vergleich mit anderen Funktionen

### Exponentielles vs. lineares Wachstum

| Eigenschaft | Linear $f(x) = mx + n$ | Exponentiell $f(x) = a \cdot b^x$ |
|-------------|------------------------|-----------------------------------|
| Änderungsrate | konstant (absolut) | proportional zum Bestand |
| Zunahme pro Schritt | additiv ($+m$) | multiplikativ ($\cdot b$) |
| Langzeitverhalten | unbegrenzt linear | unbegrenzt beschleunigt |

### Wachstumsvergleich für $x \to \infty$

$$\lim_{x \to \infty} \frac{e^x}{x^n} = \infty \quad \text{für jedes } n \in \mathbb{N}$$

Exponentialfunktionen wachsen schneller als jede Polynomfunktion.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Logarithmusfunktionen]] — Umkehrfunktion
- → [[Potenzfunktionen]] — Unterschied: Variable in Basis vs. Exponent
- → [[Grenzwerte-von-Funktionen]] — Definition von $e$
- → [[Geometrische-Folgen]] — Diskrete Version des exponentiellen Wachstums
- → [[05-Differentialrechnung-I|Differentialrechnung]] — $\frac{d}{dx}e^x = e^x$
- → [[14-Wahrscheinlichkeitsverteilungen|Wahrscheinlichkeitsverteilungen]] — Exponentialverteilung

> [!warning] **Prüfungsrelevant**
> - Unterscheidung: Exponentialfunktion $a^x$ vs. Potenzfunktion $x^a$
> - Die Eulersche Zahl $e$ und ihre Definition als Grenzwert
> - Modellierung von Wachstums- und Zerfallsprozessen
> - Berechnung von Verdopplungszeit und Halbwertszeit
> - Basiswechsel: $a^x = e^{x \ln a}$
> - Asymptotisches Verhalten: $e^x$ dominiert jedes Polynom

> [!question] **Typische Prüfungsfragen**
> - Eine Bakterienkultur verdoppelt sich alle 3 Stunden. Stellen Sie die Wachstumsfunktion auf und bestimmen Sie, nach wie viel Stunden sich der Bestand verachtfacht hat.
> - Skizzieren Sie $f(x) = e^{-x} + 2$ und geben Sie alle Asymptoten an.
> - Ein radioaktives Präparat hat nach 10 Tagen noch 60% seiner ursprünglichen Aktivität. Bestimmen Sie die Halbwertszeit.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- Arens, T. et al.: *Mathematik*, Springer Spektrum, 2018

> [!tip] **Weiterführende Links**
> - [[Logarithmusfunktionen]] — Umkehrfunktion der Exponentialfunktion
> - [[07-Integralrechnung-I|Integralrechnung]] — Integration von $e^x$

