---
author: Andreas Hümmer
title: Erwartungswert
tags:
  - content
  - mathe
  - stochastik
  - erwartungswert
  - kenngroesse
created: 2026-10-17
modified: 2026-10-17
---

# Erwartungswert

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Erwartungswert als gewichtetes Mittel der Werte einer Zufallsvariablen verstehen
> - Den Erwartungswert für diskrete Zufallsvariablen berechnen können
> - Rechenregeln für Erwartungswerte (Linearität) anwenden
> - Den Erwartungswert der Binomialverteilung kennen und anwenden

---

## Überblick

Der Erwartungswert ist die wichtigste Kenngröße einer [[Zufallsvariablen]]. Er gibt an, welchen Wert man „im Mittel" bei sehr häufiger Wiederholung des Zufallsexperiments erwarten kann. Der Erwartungswert berücksichtigt dabei, dass verschiedene Werte unterschiedlich wahrscheinlich sind.

## Definition des Erwartungswerts

### Für diskrete Zufallsvariablen

Der **Erwartungswert** einer diskreten Zufallsvariablen $X$ mit Wertebereich $W_X = \{x_1, x_2, \ldots\}$ ist definiert als:

$$E(X) = \mu = \sum_{i} x_i \cdot P(X = x_i)$$

Alternative Schreibweisen: $\mu$, $\mu_X$, $\mathbb{E}[X]$

### Interpretation

Der Erwartungswert ist das **mit den Wahrscheinlichkeiten gewichtete Mittel** aller möglichen Werte. Er muss selbst kein möglicher Wert der Zufallsvariablen sein.

## Berechnung des Erwartungswerts

### Beispiel 1: Würfelwurf

Beim Wurf eines fairen Würfels mit $X$ = Augenzahl:

$$E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6}$$

$$E(X) = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \frac{21}{6} = 3{,}5$$

Der Erwartungswert 3,5 ist selbst keine mögliche Augenzahl!

### Beispiel 2: Glücksspiel

Bei einem Glücksspiel gewinnt man mit Wahrscheinlichkeit $\frac{1}{10}$ einen Betrag von 50 € und verliert sonst den Einsatz von 10 €.

Sei $X$ der Gewinn (Verlust als negativer Gewinn):

| Ergebnis | Gewinn $x$ | Wahrscheinlichkeit |
|----------|-----------|-------------------|
| Gewinn | $50 - 10 = 40$ € | $0{,}1$ |
| Verlust | $-10$ € | $0{,}9$ |

$$E(X) = 40 \cdot 0{,}1 + (-10) \cdot 0{,}9 = 4 - 9 = -5 \text{ €}$$

Im Mittel verliert man 5 € pro Spiel — ein **unfaires Spiel**.

### Faires Spiel

Ein Spiel heißt **fair**, wenn $E(X) = 0$, d.h. wenn der erwartete Gewinn null ist.

## Rechenregeln für Erwartungswerte

### Linearität des Erwartungswerts

Für Zufallsvariablen $X$, $Y$ und Konstanten $a$, $b \in \mathbb{R}$:

$$E(aX + b) = a \cdot E(X) + b$$

$$E(X + Y) = E(X) + E(Y)$$

### Beispiele

1. $E(2X + 3) = 2 \cdot E(X) + 3$

2. Ist $E(X) = 4$, dann ist $E(3X - 5) = 3 \cdot 4 - 5 = 7$

### Erwartungswert einer Konstanten

$$E(c) = c$$

Eine Konstante hat sich selbst als Erwartungswert.

## Erwartungswert wichtiger Verteilungen

### Gleichverteilung auf $\{1, 2, \ldots, n\}$

$$E(X) = \frac{n + 1}{2}$$

**Beispiel**: Würfel mit $n = 6$: $E(X) = \frac{7}{2} = 3{,}5$

### Bernoulli-Verteilung

Für $X \sim \text{Ber}(p)$ mit $P(X = 1) = p$ und $P(X = 0) = 1-p$:

$$E(X) = 0 \cdot (1-p) + 1 \cdot p = p$$

### Binomialverteilung

Für $X \sim B(n, p)$ (siehe [[Binomialverteilung]]):

$$E(X) = \mu = n \cdot p$$

**Beispiel**: Bei 100 Würfen einer fairen Münze ist die erwartete Anzahl von „Kopf":

$$E(X) = 100 \cdot 0{,}5 = 50$$

## Anwendung: Mittlere Trefferanzahl

### Beispiel: Qualitätskontrolle

Eine Maschine produziert Teile, von denen 3% fehlerhaft sind. Bei einer Stichprobe von 200 Teilen:

$$E(X) = n \cdot p = 200 \cdot 0{,}03 = 6$$

Im Mittel erwartet man 6 fehlerhafte Teile in der Stichprobe.

### Beispiel: Multiple-Choice-Test

Ein Test hat 20 Fragen mit je 4 Antwortmöglichkeiten. Bei zufälligem Raten:

$$E(X) = n \cdot p = 20 \cdot \frac{1}{4} = 5$$

Durch reines Raten erreicht man im Mittel 5 richtige Antworten.

## Gesetz der großen Zahlen

Das **Gesetz der großen Zahlen** besagt: Bei sehr häufiger Wiederholung eines Experiments nähert sich das arithmetische Mittel der beobachteten Werte dem Erwartungswert an:

$$\frac{1}{n} \sum_{i=1}^{n} x_i \xrightarrow{n \to \infty} E(X)$$

Dies rechtfertigt die Interpretation des Erwartungswerts als „langfristiger Durchschnitt".

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Varianz]] — Maß für die Streuung um den Erwartungswert
- → [[Standardabweichung]] — Interpretierbare Streuung in Originaleinheiten
- → [[Binomialverteilung]] — Anwendung: $E(X) = n \cdot p$
- → [[Zufallsvariablen]] — Grundbegriff
- → [[Grenzwerte-von-Folgen]] — Konvergenz beim Gesetz der großen Zahlen

> [!warning] **Prüfungsrelevant**
> - Definition und Berechnung des Erwartungswerts: $E(X) = \sum x_i \cdot P(X = x_i)$
> - Linearität: $E(aX + b) = a \cdot E(X) + b$
> - Formel für Binomialverteilung: $E(X) = n \cdot p$
> - Interpretation im Sachkontext („im Mittel erwartet man...")

> [!question] **Typische Prüfungsfragen**
> - Berechne den Erwartungswert der gegebenen Zufallsvariablen und interpretiere ihn im Sachkontext.
> - Ist das beschriebene Glücksspiel fair? Begründe mit dem Erwartungswert.
> - Wie viele Treffer erwartet man bei $n$ Versuchen mit Trefferwahrscheinlichkeit $p$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Varianz]] — Die zweite wichtige Kenngröße
> - [[Binomialverteilung]] — Anwendung des Erwartungswerts
