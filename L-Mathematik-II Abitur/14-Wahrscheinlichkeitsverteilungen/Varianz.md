---
author: Andreas Hümmer
title: Varianz
tags:
  - content
  - mathe
  - stochastik
  - varianz
  - kenngroesse
  - streuung
created: 2026-10-17
modified: 2026-10-17
---

# Varianz

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Varianz als Maß für die Streuung einer Zufallsvariablen verstehen
> - Die Varianz für diskrete Zufallsvariablen berechnen können
> - Den Verschiebungssatz zur vereinfachten Berechnung anwenden
> - Die Varianz der Binomialverteilung kennen und anwenden

---

## Überblick

Die [[Erwartungswert|Erwartungswert]] allein beschreibt eine [[Wahrscheinlichkeitsverteilungen|Verteilung]] nicht vollständig. Zwei Verteilungen können denselben Erwartungswert haben, sich aber stark darin unterscheiden, wie weit die Werte um diesen Mittelwert streuen. Die **Varianz** quantifiziert genau diese Streuung.

## Definition der Varianz

Die **Varianz** einer Zufallsvariablen $X$ ist der Erwartungswert der quadratischen Abweichung vom Erwartungswert:

$$\text{Var}(X) = \sigma^2 = E\left[(X - \mu)^2\right]$$

wobei $\mu = E(X)$ der Erwartungswert ist.

### Für diskrete Zufallsvariablen

$$\text{Var}(X) = \sum_{i} (x_i - \mu)^2 \cdot P(X = x_i)$$

### Alternative Schreibweisen

$\sigma^2$, $\sigma_X^2$, $V(X)$, $\mathbb{V}[X]$

## Berechnung der Varianz

### Methode 1: Direkte Berechnung

1. Erwartungswert $\mu = E(X)$ berechnen
2. Für jeden Wert $x_i$: Abweichung $(x_i - \mu)$ bestimmen
3. Abweichungen quadrieren: $(x_i - \mu)^2$
4. Mit Wahrscheinlichkeiten gewichten und summieren

### Beispiel: Würfelwurf

Mit $\mu = E(X) = 3{,}5$:

| $x$ | $P(X = x)$ | $x - \mu$ | $(x - \mu)^2$ | $(x - \mu)^2 \cdot P(X = x)$ |
|-----|------------|-----------|--------------|------------------------------|
| 1 | $\frac{1}{6}$ | $-2{,}5$ | $6{,}25$ | $\frac{6{,}25}{6}$ |
| 2 | $\frac{1}{6}$ | $-1{,}5$ | $2{,}25$ | $\frac{2{,}25}{6}$ |
| 3 | $\frac{1}{6}$ | $-0{,}5$ | $0{,}25$ | $\frac{0{,}25}{6}$ |
| 4 | $\frac{1}{6}$ | $0{,}5$ | $0{,}25$ | $\frac{0{,}25}{6}$ |
| 5 | $\frac{1}{6}$ | $1{,}5$ | $2{,}25$ | $\frac{2{,}25}{6}$ |
| 6 | $\frac{1}{6}$ | $2{,}5$ | $6{,}25$ | $\frac{6{,}25}{6}$ |

$$\text{Var}(X) = \frac{6{,}25 + 2{,}25 + 0{,}25 + 0{,}25 + 2{,}25 + 6{,}25}{6} = \frac{17{,}5}{6} \approx 2{,}917$$

### Methode 2: Verschiebungssatz

Eine oft einfachere Berechnungsformel ist der **Verschiebungssatz** (Satz von Steiner):

$$\text{Var}(X) = E(X^2) - [E(X)]^2$$

In Worten: „Erwartungswert der Quadrate minus Quadrat des Erwartungswerts"

### Beispiel: Würfelwurf mit Verschiebungssatz

$$E(X) = 3{,}5$$

$$E(X^2) = \frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6}$$

$$\text{Var}(X) = \frac{91}{6} - (3{,}5)^2 = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12} \approx 2{,}917$$

## Rechenregeln für die Varianz

### Varianz einer linearen Transformation

$$\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)$$

**Wichtig**: Die additive Konstante $b$ beeinflusst die Varianz nicht!

### Beispiele

1. $\text{Var}(2X) = 4 \cdot \text{Var}(X)$
2. $\text{Var}(X + 5) = \text{Var}(X)$
3. $\text{Var}(3X - 7) = 9 \cdot \text{Var}(X)$

### Varianz einer Konstanten

$$\text{Var}(c) = 0$$

Eine Konstante streut nicht.

### Varianz einer Summe (bei Unabhängigkeit)

Für unabhängige Zufallsvariablen $X$ und $Y$:

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

## Varianz wichtiger Verteilungen

### Bernoulli-Verteilung

Für $X \sim \text{Ber}(p)$:

$$\text{Var}(X) = p \cdot (1 - p) = p \cdot q$$

Die Varianz ist maximal für $p = 0{,}5$: $\text{Var}(X) = 0{,}25$

### Binomialverteilung

Für $X \sim B(n, p)$ (siehe [[Binomialverteilung]]):

$$\text{Var}(X) = \sigma^2 = n \cdot p \cdot (1 - p) = n \cdot p \cdot q$$

### Beispiel

Bei 100 Würfen einer fairen Münze ($n = 100$, $p = 0{,}5$):

$$\text{Var}(X) = 100 \cdot 0{,}5 \cdot 0{,}5 = 25$$

## Interpretation der Varianz

- **Große Varianz**: Die Werte streuen stark um den Erwartungswert
- **Kleine Varianz**: Die Werte konzentrieren sich nahe beim Erwartungswert
- **Varianz = 0**: Alle Wahrscheinlichkeit liegt auf einem einzigen Wert

### Problem der Einheit

Die Varianz hat die Einheit des Merkmals **zum Quadrat**. Beispiel: Ist $X$ in Metern gemessen, ist $\text{Var}(X)$ in Quadratmetern. Deshalb verwendet man oft die [[Standardabweichung]] $\sigma = \sqrt{\text{Var}(X)}$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Erwartungswert]] — Der Mittelwert, um den die Varianz misst
- → [[Standardabweichung]] — Wurzel der Varianz
- → [[Binomialverteilung]] — Varianz: $\sigma^2 = n \cdot p \cdot q$
- → [[Normalverteilung]] — Parameter $\sigma^2$ der Normalverteilung
- → [[Zufallsvariablen]] — Grundbegriff

> [!warning] **Prüfungsrelevant**
> - Definition: $\text{Var}(X) = E[(X - \mu)^2]$
> - Verschiebungssatz: $\text{Var}(X) = E(X^2) - [E(X)]^2$
> - Formel für Binomialverteilung: $\text{Var}(X) = n \cdot p \cdot q$
> - Rechenregel: $\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)$

> [!question] **Typische Prüfungsfragen**
> - Berechne Erwartungswert und Varianz der gegebenen Zufallsvariablen.
> - Bestimme die Varianz einer binomialverteilten Zufallsvariablen mit den Parametern $n$ und $p$.
> - Wie ändert sich die Varianz, wenn alle Werte verdoppelt werden?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Standardabweichung]] — Die interpretierbare Streuung
> - [[Normalverteilung]] — Verteilung charakterisiert durch $\mu$ und $\sigma^2$
