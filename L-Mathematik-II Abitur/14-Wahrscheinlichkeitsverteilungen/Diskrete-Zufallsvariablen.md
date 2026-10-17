---
author: Andreas Hümmer
title: Diskrete Zufallsvariablen
tags:
  - content
  - mathe
  - stochastik
  - zufallsvariable
  - diskret
created: 2026-10-17
modified: 2026-10-17
---

# Diskrete Zufallsvariablen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Diskrete Zufallsvariablen erkennen und von stetigen unterscheiden
> - Die Wahrscheinlichkeitsverteilung einer diskreten Zufallsvariablen angeben können
> - Wahrscheinlichkeiten für zusammengesetzte Ereignisse berechnen
> - Wahrscheinlichkeitstabellen und Stabdiagramme erstellen und interpretieren

---

## Überblick

Diskrete Zufallsvariablen nehmen nur isolierte Werte an — typischerweise ganze Zahlen wie 0, 1, 2, 3 usw. Sie beschreiben Situationen, in denen man Ergebnisse zählt oder klassifiziert. Im Abitur sind diskrete Zufallsvariablen der Schwerpunkt, insbesondere im Zusammenhang mit der [[Binomialverteilung]].

## Definition

Eine Zufallsvariable $X$ heißt **diskret**, wenn ihr Wertebereich $W_X$ endlich oder abzählbar unendlich ist:

$$W_X = \{x_1, x_2, x_3, \ldots\}$$

Für jedes $x_i \in W_X$ existiert eine Wahrscheinlichkeit $P(X = x_i) \geq 0$ mit:

$$\sum_{i} P(X = x_i) = 1$$

## Wahrscheinlichkeitsfunktion

Die **Wahrscheinlichkeitsfunktion** (auch: Zähldichte) ordnet jedem möglichen Wert seine Wahrscheinlichkeit zu:

$$f(x) = P(X = x)$$

### Eigenschaften der Wahrscheinlichkeitsfunktion

1. $f(x) \geq 0$ für alle $x \in W_X$
2. $f(x) = 0$ für alle $x \notin W_X$
3. $\displaystyle\sum_{x \in W_X} f(x) = 1$

## Darstellungsformen

### Wertetabelle

Die übersichtlichste Darstellung für diskrete Verteilungen mit wenigen Werten:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| $P(X = x)$ | 0,10 | 0,25 | 0,35 | 0,20 | 0,10 |

### Stabdiagramm

Im Stabdiagramm wird über jedem Wert $x$ ein Stab der Höhe $P(X = x)$ eingezeichnet:

```
P(X=x)
  |
0,35 +          █
0,30 +          ║
0,25 +     █    ║
0,20 +     ║    ║    █
0,15 +     ║    ║    ║
0,10 + █   ║    ║    ║    █
0,05 + ║   ║    ║    ║    ║
     +─║───║────║────║────║───
       0   1    2    3    4   x
```

## Berechnung von Wahrscheinlichkeiten

### Einzelwahrscheinlichkeiten

Direkt aus der Wahrscheinlichkeitsfunktion: $P(X = k) = f(k)$

### Bereichswahrscheinlichkeiten

Für zusammengesetzte Ereignisse summiert man die Einzelwahrscheinlichkeiten:

$$P(a \leq X \leq b) = \sum_{k=a}^{b} P(X = k)$$

### Beispiel

Mit der obigen Verteilung:

$$P(X \leq 2) = P(X = 0) + P(X = 1) + P(X = 2) = 0,10 + 0,25 + 0,35 = 0,70$$

$$P(X \geq 3) = P(X = 3) + P(X = 4) = 0,20 + 0,10 = 0,30$$

### Komplementregel

$$P(X > k) = 1 - P(X \leq k)$$

Diese Regel ist besonders nützlich, wenn „mindestens"-Wahrscheinlichkeiten gefragt sind:

$$P(X \geq 1) = 1 - P(X = 0)$$

## Wichtige diskrete Verteilungen

### Gleichverteilung

Bei einer **diskreten Gleichverteilung** auf $\{1, 2, \ldots, n\}$ gilt:

$$P(X = k) = \frac{1}{n} \quad \text{für } k = 1, 2, \ldots, n$$

**Beispiel**: Ein fairer Würfel mit $n = 6$: $P(X = k) = \frac{1}{6}$

### Bernoulli-Verteilung

Die einfachste nicht-triviale Verteilung für ein Experiment mit zwei Ausgängen:

$$P(X = 1) = p \quad \text{(Treffer)}$$
$$P(X = 0) = 1 - p = q \quad \text{(Niete)}$$

### Binomialverteilung

Die Verteilung der Trefferanzahl bei $n$ unabhängigen [[Bernoulli-Experimente|Bernoulli-Experimenten]] — siehe [[Binomialverteilung]].

## Zusammenfassung der Rechenregeln

| Ereignis | Berechnung |
|----------|------------|
| $P(X = k)$ | Direkt ablesen oder berechnen |
| $P(X \leq k)$ | $\sum_{i=0}^{k} P(X = i)$ |
| $P(X < k)$ | $P(X \leq k-1)$ |
| $P(X \geq k)$ | $1 - P(X \leq k-1)$ |
| $P(X > k)$ | $1 - P(X \leq k)$ |
| $P(a \leq X \leq b)$ | $P(X \leq b) - P(X \leq a-1)$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zufallsvariablen]] — Allgemeiner Begriff der Zufallsvariablen
- → [[Wahrscheinlichkeitsverteilungen]] — Verteilungsbegriff allgemein
- → [[Binomialverteilung]] — Wichtigste diskrete Verteilung im Abitur
- → [[Erwartungswert]] — Berechnung des Erwartungswerts diskreter Verteilungen
- → [[Kumulative-Wahrscheinlichkeiten]] — Verteilungsfunktion für kumulierte Wahrscheinlichkeiten

> [!warning] **Prüfungsrelevant**
> - Erstellen und Interpretieren von Wahrscheinlichkeitstabellen
> - Umrechnung zwischen verschiedenen Wahrscheinlichkeitsaussagen (≤, <, ≥, >)
> - Anwendung der Komplementregel $P(X \geq k) = 1 - P(X \leq k-1)$
> - Bereichswahrscheinlichkeiten korrekt berechnen

> [!question] **Typische Prüfungsfragen**
> - Stelle die Wahrscheinlichkeitsverteilung der Zufallsvariablen $X$ in einer Tabelle dar.
> - Berechne $P(X \geq 2)$ und $P(1 \leq X \leq 4)$ für die gegebene Verteilung.
> - Zeichne ein Stabdiagramm für die Wahrscheinlichkeitsverteilung.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Wahrscheinlichkeitsverteilungen]] — Formale Behandlung von Verteilungen
> - [[Binomialverteilung]] — Die wichtigste diskrete Verteilung im Abitur
