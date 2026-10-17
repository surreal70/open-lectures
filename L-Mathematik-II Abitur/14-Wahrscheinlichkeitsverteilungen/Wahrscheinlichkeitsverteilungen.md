---
author: Andreas Hümmer
title: Wahrscheinlichkeitsverteilungen
tags:
  - content
  - mathe
  - stochastik
  - verteilung
  - grundlagen
created: 2026-10-17
modified: 2026-10-17
---

# Wahrscheinlichkeitsverteilungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Wahrscheinlichkeitsverteilung formal verstehen
> - Die Verteilungsfunktion definieren und anwenden können
> - Zwischen Wahrscheinlichkeitsfunktion und Verteilungsfunktion unterscheiden
> - Eigenschaften von Verteilungen grafisch und rechnerisch analysieren

---

## Überblick

Eine Wahrscheinlichkeitsverteilung beschreibt vollständig, wie die Wahrscheinlichkeiten auf die möglichen Werte einer [[Zufallsvariablen]] verteilt sind. Sie ist das zentrale Objekt der Stochastik und bildet die Grundlage für alle weiteren Berechnungen wie [[Erwartungswert]] oder [[Varianz]].

## Definition der Wahrscheinlichkeitsverteilung

Die **Wahrscheinlichkeitsverteilung** einer Zufallsvariablen $X$ ist die vollständige Angabe aller Wahrscheinlichkeiten $P(X \in A)$ für alle relevanten Ereignisse $A$.

### Für diskrete Zufallsvariablen

Bei [[Diskrete-Zufallsvariablen|diskreten Zufallsvariablen]] ist die Verteilung durch die **Wahrscheinlichkeitsfunktion** gegeben:

$$f: W_X \to [0,1], \quad f(x) = P(X = x)$$

mit der Normierungsbedingung:

$$\sum_{x \in W_X} f(x) = 1$$

### Für stetige Zufallsvariablen

Bei stetigen Zufallsvariablen wird die Verteilung durch eine **Dichtefunktion** $f(x)$ beschrieben:

$$P(a \leq X \leq b) = \int_a^b f(x) \, dx$$

mit $f(x) \geq 0$ und $\displaystyle\int_{-\infty}^{\infty} f(x) \, dx = 1$.

## Verteilungsfunktion

Die **Verteilungsfunktion** (kumulative Verteilungsfunktion) gibt für jeden Wert $x$ die Wahrscheinlichkeit an, dass $X$ höchstens diesen Wert annimmt:

$$F(x) = P(X \leq x)$$

### Eigenschaften der Verteilungsfunktion

1. **Monotonie**: $F$ ist monoton steigend
2. **Grenzwerte**: $\lim_{x \to -\infty} F(x) = 0$ und $\lim_{x \to \infty} F(x) = 1$
3. **Rechtsstetigkeit**: $F$ ist rechtsseitig stetig

### Berechnung für diskrete Verteilungen

$$F(x) = P(X \leq x) = \sum_{k \leq x} P(X = k)$$

### Beispiel: Zweimaliger Münzwurf

Sei $X$ die Anzahl von „Kopf" bei zweimaligem Münzwurf.

| $x$ | $P(X = x)$ | $F(x) = P(X \leq x)$ |
|-----|------------|---------------------|
| 0 | $\frac{1}{4}$ | $\frac{1}{4}$ |
| 1 | $\frac{2}{4}$ | $\frac{3}{4}$ |
| 2 | $\frac{1}{4}$ | $\frac{4}{4} = 1$ |

Die Verteilungsfunktion ist eine Treppenfunktion:

```
F(x)
  |
1 +                    ●────────
  |             ●──────○
3/4+            │
  |      ●──────○
1/4+     │
  |──────○
0 +────────────────────────────
     -1   0    1    2    3    x
```

## Zusammenhang zwischen f und F

### Von f zu F (Summation)

$$F(x) = \sum_{k \leq x} f(k)$$

### Von F zu f (Differenzbildung)

$$f(k) = F(k) - F(k-1)$$

bzw. für $k = 0$ als kleinsten Wert: $f(0) = F(0)$

## Berechnung von Wahrscheinlichkeiten mit F

Die Verteilungsfunktion ermöglicht die schnelle Berechnung beliebiger Wahrscheinlichkeiten:

| Ereignis | Berechnung |
|----------|------------|
| $P(X \leq k)$ | $F(k)$ |
| $P(X < k)$ | $F(k-1)$ |
| $P(X > k)$ | $1 - F(k)$ |
| $P(X \geq k)$ | $1 - F(k-1)$ |
| $P(a \leq X \leq b)$ | $F(b) - F(a-1)$ |
| $P(a < X < b)$ | $F(b-1) - F(a)$ |

### Beispiel

Mit der obigen Verteilung des Münzwurfs:

$$P(X \geq 1) = 1 - F(0) = 1 - \frac{1}{4} = \frac{3}{4}$$

$$P(1 \leq X \leq 2) = F(2) - F(0) = 1 - \frac{1}{4} = \frac{3}{4}$$

## Wichtige Verteilungsfamilien

### Diskrete Verteilungen

| Verteilung | Anwendung | Parameter |
|------------|-----------|-----------|
| Gleichverteilung | Alle Werte gleich wahrscheinlich | $n$ (Anzahl Werte) |
| Bernoulli-Verteilung | Ein Experiment, zwei Ausgänge | $p$ (Erfolgswahrscheinlichkeit) |
| [[Binomialverteilung]] | $n$ Bernoulli-Experimente | $n$, $p$ |
| Poisson-Verteilung | Seltene Ereignisse | $\lambda$ (Rate) |

### Stetige Verteilungen

| Verteilung | Anwendung | Parameter |
|------------|-----------|-----------|
| Gleichverteilung | Gleichmäßig über Intervall | $a$, $b$ (Grenzen) |
| [[Normalverteilung]] | Viele natürliche Phänomene | $\mu$, $\sigma$ |
| Exponentialverteilung | Wartezeiten | $\lambda$ (Rate) |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zufallsvariablen]] — Grundbegriff der Zufallsvariablen
- → [[Diskrete-Zufallsvariablen]] — Spezialfall diskreter Verteilungen
- → [[Kumulative-Wahrscheinlichkeiten]] — Vertiefung der Verteilungsfunktion
- → [[Binomialverteilung]] — Wichtigste diskrete Verteilung
- → [[Normalverteilung]] — Wichtigste stetige Verteilung

> [!warning] **Prüfungsrelevant**
> - Aufstellen der Wahrscheinlichkeitsverteilung in Tabellenform
> - Berechnung der Verteilungsfunktion $F(x)$
> - Umrechnung zwischen $P(X = k)$, $P(X \leq k)$, $P(X \geq k)$
> - Interpretation von Wahrscheinlichkeiten im Sachkontext

> [!question] **Typische Prüfungsfragen**
> - Gib die Wahrscheinlichkeitsverteilung der Zufallsvariablen $X$ an.
> - Berechne die Verteilungsfunktion $F$ und zeichne ihren Graphen.
> - Bestimme $P(2 \leq X \leq 5)$ mithilfe der Verteilungsfunktion.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Georgii, H.-O.: Stochastik: Einführung in die Wahrscheinlichkeitstheorie und Statistik. De Gruyter, 2015.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Erwartungswert]] — Charakterisierung von Verteilungen durch Kenngrößen
> - [[Binomialverteilung]] — Parametrische Verteilung für Bernoulli-Ketten
