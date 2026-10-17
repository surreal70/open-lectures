---
author: Andreas Hümmer
title: Bernoulli-Ketten
tags:
  - content
  - mathe
  - stochastik
  - bernoulli
  - binomialverteilung
created: 2025-07-01
modified: 2025-07-01
---

# Bernoulli-Ketten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Eine Bernoulli-Kette definieren und ihre Eigenschaften kennen
> - Die Formel für P(X = k) anwenden können (Binomialverteilung)
> - Kumulierte Wahrscheinlichkeiten berechnen können
> - Erwartungswert und Standardabweichung bestimmen können

---

## Überblick

Eine Bernoulli-Kette entsteht durch die $n$-fache unabhängige Wiederholung eines Bernoulli-Experiments. Die Anzahl der Erfolge in einer Bernoulli-Kette folgt der Binomialverteilung – einer der wichtigsten Verteilungen in der Stochastik und ein zentrales Thema der Abiturprüfung.

## Definition

Eine **Bernoulli-Kette der Länge $n$** ist die $n$-fache unabhängige Wiederholung eines Bernoulli-Experiments mit Erfolgswahrscheinlichkeit $p$.

### Voraussetzungen

1. Es gibt genau zwei mögliche Ausgänge pro Versuch (Erfolg/Misserfolg)
2. Die Erfolgswahrscheinlichkeit $p$ ist bei jedem Versuch gleich
3. Die einzelnen Versuche sind voneinander unabhängig

### Notation

- $n$: Anzahl der Versuche (Kettenlänge)
- $p$: Erfolgswahrscheinlichkeit
- $q = 1 - p$: Misserfolgswahrscheinlichkeit
- $X$: Zufallsvariable „Anzahl der Erfolge"
- $k$: konkrete Anzahl der Erfolge ($k \in \{0, 1, 2, \ldots, n\}$)

## Die Bernoulli-Formel

### Wahrscheinlichkeit für genau $k$ Erfolge

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

### Herleitung

**Schritt 1:** Ein bestimmter Pfad mit $k$ Erfolgen und $(n-k)$ Misserfolgen hat die Wahrscheinlichkeit:
$$p^k \cdot q^{n-k}$$

**Schritt 2:** Die Anzahl solcher Pfade entspricht der Anzahl der Möglichkeiten, $k$ Positionen für Erfolge aus $n$ Positionen zu wählen:
$$\binom{n}{k}$$

**Schritt 3:** Multiplikation ergibt die Bernoulli-Formel.

### Beispiel: Viermaliger Münzwurf

Wie groß ist die Wahrscheinlichkeit, bei 4 Würfen einer fairen Münze genau 2-mal Kopf zu erhalten?

**Gegeben:** $n = 4$, $p = 0{,}5$, $k = 2$

$$P(X = 2) = \binom{4}{2} \cdot 0{,}5^2 \cdot 0{,}5^2 = 6 \cdot 0{,}25 \cdot 0{,}25 = 6 \cdot 0{,}0625 = 0{,}375$$

Die Wahrscheinlichkeit beträgt **37,5%**.

## Kumulierte Wahrscheinlichkeiten

### Höchstens $k$ Erfolge

$$P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} \cdot p^i \cdot (1-p)^{n-i}$$

### Mindestens $k$ Erfolge

$$P(X \geq k) = 1 - P(X \leq k-1) = \sum_{i=k}^{n} \binom{n}{i} \cdot p^i \cdot (1-p)^{n-i}$$

### Zwischen $a$ und $b$ Erfolge

$$P(a \leq X \leq b) = P(X \leq b) - P(X \leq a-1)$$

### Beispiel: Multiple-Choice-Test

Ein Test hat 10 Fragen mit je 4 Antwortmöglichkeiten. Man rät bei allen Fragen zufällig. Wie groß ist die Wahrscheinlichkeit für mindestens 3 richtige Antworten?

**Gegeben:** $n = 10$, $p = 0{,}25$

$$P(X \geq 3) = 1 - P(X \leq 2)$$
$$= 1 - [P(X=0) + P(X=1) + P(X=2)]$$

Berechnung:
- $P(X=0) = \binom{10}{0} \cdot 0{,}25^0 \cdot 0{,}75^{10} \approx 0{,}0563$
- $P(X=1) = \binom{10}{1} \cdot 0{,}25^1 \cdot 0{,}75^9 \approx 0{,}1877$
- $P(X=2) = \binom{10}{2} \cdot 0{,}25^2 \cdot 0{,}75^8 \approx 0{,}2816$

$$P(X \geq 3) = 1 - (0{,}0563 + 0{,}1877 + 0{,}2816) = 1 - 0{,}5256 \approx 0{,}474$$

Die Wahrscheinlichkeit beträgt etwa **47,4%**.

## Kenngrößen der Binomialverteilung

### Erwartungswert

Der Erwartungswert gibt die „im Mittel" zu erwartende Anzahl von Erfolgen an:

$$\mu = E(X) = n \cdot p$$

### Varianz

$$\sigma^2 = \text{Var}(X) = n \cdot p \cdot (1-p) = n \cdot p \cdot q$$

### Standardabweichung

$$\sigma = \sqrt{n \cdot p \cdot (1-p)}$$

### Beispiel: Würfelspiel

Ein Würfel wird 60-mal geworfen. Berechne Erwartungswert und Standardabweichung für die Anzahl der Sechsen.

**Gegeben:** $n = 60$, $p = \frac{1}{6}$

$$\mu = 60 \cdot \frac{1}{6} = 10$$

$$\sigma = \sqrt{60 \cdot \frac{1}{6} \cdot \frac{5}{6}} = \sqrt{60 \cdot \frac{5}{36}} = \sqrt{\frac{300}{36}} = \sqrt{\frac{25}{3}} \approx 2{,}89$$

Im Mittel erwartet man **10 Sechsen** mit einer Standardabweichung von etwa **2,9**.

## Sigma-Regeln

Für hinreichend großes $n$ (Faustregel: $n \cdot p \cdot (1-p) > 9$) kann die Binomialverteilung durch die Normalverteilung approximiert werden. Es gelten dann näherungsweise:

| Intervall | Wahrscheinlichkeit |
|-----------|-------------------|
| $[\mu - \sigma, \mu + \sigma]$ | $\approx 68{,}3\%$ |
| $[\mu - 2\sigma, \mu + 2\sigma]$ | $\approx 95{,}4\%$ |
| $[\mu - 3\sigma, \mu + 3\sigma]$ | $\approx 99{,}7\%$ |

### Beispiel

Bei $n = 100$ und $p = 0{,}5$:
- $\mu = 50$
- $\sigma = \sqrt{100 \cdot 0{,}5 \cdot 0{,}5} = 5$

Mit etwa 95% Wahrscheinlichkeit liegt die Anzahl der Erfolge im Intervall $[40, 60]$.

## Typische Aufgabentypen

### Typ 1: Exakte Wahrscheinlichkeit

„Wie groß ist P(X = k)?"

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

### Typ 2: Kumulierte Wahrscheinlichkeit

„Wie groß ist P(X ≤ k) bzw. P(X ≥ k)?"

Summieren oder über Gegenereignis.

### Typ 3: Mindestanzahl bestimmen

„Wie oft muss man würfeln, damit mit 95% Wahrscheinlichkeit mindestens eine 6 kommt?"

$$P(X \geq 1) \geq 0{,}95 \Leftrightarrow 1 - P(X = 0) \geq 0{,}95$$
$$\Leftrightarrow \left(\frac{5}{6}\right)^n \leq 0{,}05$$
$$n \geq \frac{\ln(0{,}05)}{\ln(5/6)} \approx 16{,}4$$

Also: mindestens **17 Würfe**.

### Typ 4: Erfolgswahrscheinlichkeit bestimmen

„Bei welcher Trefferquote erzielt ein Spieler mit 80% Wahrscheinlichkeit mindestens 7 von 10 Treffern?"

Numerische Lösung oder Tabelle/CAS erforderlich.

## Visualisierung

### Histogramm für $n = 10$, $p = 0{,}3$

```
P(X=k)
0.30 |
0.25 |       ██
0.20 |    ██ ██ ██
0.15 | ██ ██ ██ ██ ██
0.10 | ██ ██ ██ ██ ██ ██
0.05 | ██ ██ ██ ██ ██ ██ ██
     └─────────────────────────
     0  1  2  3  4  5  6  7  8  9 10  k
```

Die Verteilung ist rechtsschief, da $p < 0{,}5$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bernoulli-Experimente]] — Grundlage der Bernoulli-Kette
- → [[Binomialkoeffizienten]] — In der Bernoulli-Formel
- → [[Kombinationen]] — Anzahl der Pfade
- → [[Unabhaengigkeit-von-Ereignissen]] — Voraussetzung

> [!warning] **Prüfungsrelevant**
> - Die Bernoulli-Formel sicher anwenden können
> - Kumulierte Wahrscheinlichkeiten berechnen (auch über Gegenereignis)
> - Erwartungswert $\mu = n \cdot p$ und Standardabweichung $\sigma = \sqrt{npq}$
> - Die Sigma-Regeln kennen und anwenden

> [!question] **Typische Prüfungsfragen**
> - Ein Glücksrad mit 8 gleichen Sektoren wird 5-mal gedreht. Berechne P(genau 2-mal Sektor 1).
> - Bei 100 Würfen eines fairen Würfels: In welchem Intervall liegt die Anzahl der Sechsen mit 95% Wahrscheinlichkeit?
> - Wie oft muss man eine Münze werfen, damit mit mindestens 99% Wahrscheinlichkeit mindestens einmal Kopf erscheint?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik

> [!tip] **Weiterführende Links**
> - [[14-Wahrscheinlichkeitsverteilungen/Binomialverteilung|Binomialverteilung]] — Vertiefung im Wahrscheinlichkeitsverteilungs-Kapitel
> - [[15-Statistik-und-Hypothesentests/Hypothesentests|Hypothesentests]] — Anwendung der Binomialverteilung
