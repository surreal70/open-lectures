---
author: Andreas Hümmer
title: Binomialverteilung
tags:
  - content
  - mathe
  - stochastik
  - binomialverteilung
  - verteilung
  - bernoulli
created: 2026-10-17
modified: 2026-10-17
---

# Binomialverteilung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Voraussetzungen für die Binomialverteilung kennen und prüfen können
> - Wahrscheinlichkeiten mit der Binomialformel berechnen
> - Erwartungswert und Standardabweichung der Binomialverteilung bestimmen
> - Die Binomialverteilung auf praktische Probleme anwenden

---

## Überblick

Die **Binomialverteilung** ist die wichtigste diskrete [[Wahrscheinlichkeitsverteilungen|Wahrscheinlichkeitsverteilung]] im Abitur. Sie beschreibt die Anzahl der Treffer bei $n$ unabhängigen Wiederholungen eines [[Bernoulli-Experimente|Bernoulli-Experiments]] mit konstanter Trefferwahrscheinlichkeit $p$.

## Voraussetzungen (Bernoulli-Kette)

Die Binomialverteilung liegt vor, wenn folgende Bedingungen erfüllt sind:

1. **Zwei mögliche Ausgänge**: Jedes Experiment hat genau zwei Ausgänge („Treffer" und „Niete")
2. **Konstante Wahrscheinlichkeit**: Die Trefferwahrscheinlichkeit $p$ ist bei jedem Versuch gleich
3. **Unabhängigkeit**: Die einzelnen Versuche beeinflussen sich nicht gegenseitig
4. **Feste Anzahl**: Die Anzahl $n$ der Versuche ist fest vorgegeben

Eine Folge von $n$ solchen Experimenten heißt **[[Bernoulli-Ketten|Bernoulli-Kette]]** der Länge $n$.

## Die Binomialformel

Für eine binomialverteilte Zufallsvariable $X \sim B(n, p)$ gilt:

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

wobei:
- $n$ = Anzahl der Versuche
- $k$ = Anzahl der Treffer ($k = 0, 1, 2, \ldots, n$)
- $p$ = Trefferwahrscheinlichkeit
- $q = 1 - p$ = Nietenwahrscheinlichkeit
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ = [[Binomialkoeffizienten|Binomialkoeffizient]]

### Herleitung der Formel

- $p^k$: Wahrscheinlichkeit für $k$ Treffer
- $(1-p)^{n-k}$: Wahrscheinlichkeit für $n-k$ Nieten
- $\binom{n}{k}$: Anzahl der Möglichkeiten, $k$ Treffer auf $n$ Plätze zu verteilen

## Beispiele

### Beispiel 1: Münzwurf

Bei 5 Würfen einer fairen Münze ($n = 5$, $p = 0{,}5$): Wie groß ist die Wahrscheinlichkeit für genau 3-mal „Kopf"?

$$P(X = 3) = \binom{5}{3} \cdot 0{,}5^3 \cdot 0{,}5^2 = 10 \cdot 0{,}125 \cdot 0{,}25 = 0{,}3125$$

### Beispiel 2: Qualitätskontrolle

Ein Produkt hat eine Ausschussrate von 5%. Bei einer Stichprobe von 20 Stück:

a) Wahrscheinlichkeit für genau 2 defekte Teile:

$$P(X = 2) = \binom{20}{2} \cdot 0{,}05^2 \cdot 0{,}95^{18}$$
$$= 190 \cdot 0{,}0025 \cdot 0{,}3972 \approx 0{,}189$$

b) Wahrscheinlichkeit für höchstens 1 defektes Teil:

$$P(X \leq 1) = P(X = 0) + P(X = 1)$$
$$= \binom{20}{0} \cdot 0{,}05^0 \cdot 0{,}95^{20} + \binom{20}{1} \cdot 0{,}05^1 \cdot 0{,}95^{19}$$
$$= 0{,}3585 + 0{,}3774 \approx 0{,}736$$

## Erwartungswert und Standardabweichung

### Erwartungswert

$$\mu = E(X) = n \cdot p$$

### Varianz

$$\sigma^2 = \text{Var}(X) = n \cdot p \cdot (1-p) = n \cdot p \cdot q$$

### Standardabweichung

$$\sigma = \sqrt{n \cdot p \cdot q}$$

### Beispiel

Bei 100 Münzwürfen ($n = 100$, $p = 0{,}5$):

$$\mu = 100 \cdot 0{,}5 = 50$$
$$\sigma = \sqrt{100 \cdot 0{,}5 \cdot 0{,}5} = \sqrt{25} = 5$$

Im Mittel erwartet man 50 Treffer mit einer Standardabweichung von 5.

## Grafische Darstellung

Die Binomialverteilung lässt sich als Stabdiagramm darstellen:

```
P(X=k) bei n=10, p=0,5
  |
0,25 +         █ █
     |       █ ║ ║ █
0,20 +       ║ ║ ║ ║
     |     █ ║ ║ ║ ║ █
0,15 +     ║ ║ ║ ║ ║ ║
     |   █ ║ ║ ║ ║ ║ ║ █
0,10 +   ║ ║ ║ ║ ║ ║ ║ ║
     | █ ║ ║ ║ ║ ║ ║ ║ ║ █
0,05 + ║ ║ ║ ║ ║ ║ ║ ║ ║ ║
     +─║─║─║─║─║─║─║─║─║─║──
       0 1 2 3 4 5 6 7 8 9 10  k
```

### Eigenschaften der Form

- **Symmetrisch** für $p = 0{,}5$
- **Linkssteil (rechtsschief)** für $p > 0{,}5$
- **Rechtssteil (linksschief)** für $p < 0{,}5$
- Maximum nahe bei $\mu = n \cdot p$

## Berechnung mit dem Taschenrechner

Die meisten Taschenrechner haben Funktionen für die Binomialverteilung:

| Funktion | Bedeutung | Formel |
|----------|-----------|--------|
| `binompdf(n,p,k)` | Einzelwahrscheinlichkeit | $P(X = k)$ |
| `binomcdf(n,p,k)` | Kumulative Wahrscheinlichkeit | $P(X \leq k)$ |

### Typische Berechnungen

| Wahrscheinlichkeit | Berechnung |
|-------------------|------------|
| $P(X = k)$ | `binompdf(n,p,k)` |
| $P(X \leq k)$ | `binomcdf(n,p,k)` |
| $P(X < k)$ | `binomcdf(n,p,k-1)` |
| $P(X \geq k)$ | `1 - binomcdf(n,p,k-1)` |
| $P(X > k)$ | `1 - binomcdf(n,p,k)` |
| $P(a \leq X \leq b)$ | `binomcdf(n,p,b) - binomcdf(n,p,a-1)` |

## Sigma-Umgebungen

Für binomialverteilte Zufallsvariablen gilt approximativ:

$$P(\mu - k\sigma \leq X \leq \mu + k\sigma) \approx \begin{cases} 68\% & k = 1 \\ 95\% & k = 2 \\ 99{,}7\% & k = 3 \end{cases}$$

Diese Regel wird umso genauer, je größer $n$ ist (siehe [[Normalapproximation]]).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bernoulli-Experimente]] — Grundlage der Binomialverteilung
- → [[Bernoulli-Ketten]] — Wiederholte Bernoulli-Experimente
- → [[Binomialkoeffizienten]] — Der kombinatorische Faktor
- → [[Kumulative-Wahrscheinlichkeiten]] — $P(X \leq k)$ und Verteilungsfunktion
- → [[Normalapproximation]] — Approximation für große $n$
- → [[Erwartungswert]] — $\mu = n \cdot p$
- → [[Standardabweichung]] — $\sigma = \sqrt{npq}$

> [!warning] **Prüfungsrelevant**
> - Prüfung der Voraussetzungen (Bernoulli-Kette)
> - Binomialformel: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
> - Formeln für $\mu = np$ und $\sigma = \sqrt{npq}$
> - Berechnung von „mindestens"- und „höchstens"-Wahrscheinlichkeiten
> - Anwendung auf Sachkontexte

> [!question] **Typische Prüfungsfragen**
> - Begründe, dass die Situation durch eine Binomialverteilung modelliert werden kann.
> - Berechne die Wahrscheinlichkeit für genau/mindestens/höchstens $k$ Treffer.
> - Bestimme Erwartungswert und Standardabweichung und interpretiere sie im Sachkontext.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Kumulative-Wahrscheinlichkeiten]] — Effiziente Berechnung mit Tabellen
> - [[Normalapproximation]] — Approximation für große $n$
