---
author: Andreas Hümmer
title: Standardabweichung
tags:
  - content
  - mathe
  - stochastik
  - standardabweichung
  - kenngroesse
  - streuung
created: 2026-10-17
modified: 2026-10-17
---

# Standardabweichung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Standardabweichung als Wurzel der Varianz verstehen und berechnen
> - Die Standardabweichung im Kontext des Problems interpretieren können
> - Sigma-Umgebungen definieren und deren Bedeutung kennen
> - Die Standardabweichung der Binomialverteilung anwenden

---

## Überblick

Die [[Varianz]] misst die Streuung einer [[Zufallsvariablen]], hat jedoch die Einheit des Merkmals zum Quadrat. Die **Standardabweichung** ist die Wurzel der Varianz und damit in der ursprünglichen Einheit interpretierbar. Sie ist das Standardmaß für die Streuung in der Stochastik.

## Definition der Standardabweichung

Die **Standardabweichung** einer Zufallsvariablen $X$ ist definiert als:

$$\sigma = \sqrt{\text{Var}(X)} = \sqrt{E\left[(X - \mu)^2\right]}$$

### Alternative Schreibweisen

$\sigma$, $\sigma_X$, $\text{SD}(X)$, $\sqrt{\mathbb{V}[X]}$

### Berechnung für diskrete Zufallsvariablen

$$\sigma = \sqrt{\sum_{i} (x_i - \mu)^2 \cdot P(X = x_i)}$$

Oder mit dem Verschiebungssatz:

$$\sigma = \sqrt{E(X^2) - [E(X)]^2}$$

## Beispiel: Würfelwurf

Mit $\text{Var}(X) = \frac{35}{12} \approx 2{,}917$ (siehe [[Varianz]]):

$$\sigma = \sqrt{\frac{35}{12}} = \frac{\sqrt{35}}{\sqrt{12}} \approx 1{,}71$$

Die Augenzahl streut im Mittel um etwa 1,71 um den Erwartungswert 3,5.

## Standardabweichung wichtiger Verteilungen

### Bernoulli-Verteilung

Für $X \sim \text{Ber}(p)$:

$$\sigma = \sqrt{p \cdot (1-p)} = \sqrt{p \cdot q}$$

### Binomialverteilung

Für $X \sim B(n, p)$ (siehe [[Binomialverteilung]]):

$$\sigma = \sqrt{n \cdot p \cdot (1-p)} = \sqrt{n \cdot p \cdot q}$$

### Beispiel: Münzwurf

Bei 100 Würfen einer fairen Münze ($n = 100$, $p = 0{,}5$):

$$\mu = n \cdot p = 50$$
$$\sigma = \sqrt{100 \cdot 0{,}5 \cdot 0{,}5} = \sqrt{25} = 5$$

Die Anzahl von „Kopf" streut im Mittel um 5 um den Erwartungswert 50.

## Rechenregeln für die Standardabweichung

### Lineare Transformation

$$\sigma_{aX+b} = |a| \cdot \sigma_X$$

Die additive Konstante beeinflusst die Standardabweichung nicht, der Faktor geht mit seinem Betrag ein.

### Beispiele

1. $\sigma_{2X} = 2 \cdot \sigma_X$
2. $\sigma_{X+5} = \sigma_X$
3. $\sigma_{-3X+7} = 3 \cdot \sigma_X$

## Sigma-Umgebungen

### Definition

Die **$k$-Sigma-Umgebung** um den Erwartungswert ist das Intervall:

$$[\mu - k\sigma, \mu + k\sigma]$$

### Bedeutung für die Binomialverteilung

Für große $n$ liegen die Werte einer binomialverteilten Zufallsvariablen mit hoher Wahrscheinlichkeit in der Nähe des Erwartungswerts:

| Umgebung | Intervall | Wahrscheinlichkeit (ca.) |
|----------|-----------|-------------------------|
| 1σ | $[\mu - \sigma, \mu + \sigma]$ | ≈ 68% |
| 2σ | $[\mu - 2\sigma, \mu + 2\sigma]$ | ≈ 95% |
| 3σ | $[\mu - 3\sigma, \mu + 3\sigma]$ | ≈ 99,7% |

Diese Werte gelten exakt für die [[Normalverteilung]] und approximativ für andere Verteilungen.

### Beispiel: Qualitätskontrolle

Eine Maschine produziert Schrauben mit Sollmaß 10 mm. Die Längen sind normalverteilt mit $\mu = 10$ mm und $\sigma = 0{,}02$ mm.

- **1σ-Umgebung**: $[9{,}98; 10{,}02]$ mm — etwa 68% der Schrauben
- **2σ-Umgebung**: $[9{,}96; 10{,}04]$ mm — etwa 95% der Schrauben
- **3σ-Umgebung**: $[9{,}94; 10{,}06]$ mm — etwa 99,7% der Schrauben

## Interpretation der Standardabweichung

### Als Streuungsmaß

- **Kleine σ**: Werte konzentrieren sich stark um den Erwartungswert
- **Große σ**: Werte streuen weit um den Erwartungswert

### Als typische Abweichung

Die Standardabweichung gibt an, wie weit ein typischer Wert vom Erwartungswert entfernt ist.

### Im Vergleich

Bei gleichem Erwartungswert ermöglicht die Standardabweichung den Vergleich der Streuung:

```
Verteilung A (σ = 2):    ──────●────────────●──────
                               μ-σ    μ    μ+σ

Verteilung B (σ = 5):    ●─────────────────────────●
                         μ-σ          μ          μ+σ
```

## Anwendung: Beurteilung von Ergebnissen

### Beispiel: Würfeltest

Bei 600 Würfen eines fairen Würfels ist die erwartete Anzahl Sechsen:

$$\mu = 600 \cdot \frac{1}{6} = 100$$
$$\sigma = \sqrt{600 \cdot \frac{1}{6} \cdot \frac{5}{6}} = \sqrt{\frac{500}{6}} \approx 9{,}13$$

Erhält man 85 Sechsen, liegt dieses Ergebnis etwa $\frac{100-85}{9{,}13} \approx 1{,}64$ Standardabweichungen unter dem Erwartungswert — noch im Rahmen der 2σ-Umgebung.

Erhält man nur 70 Sechsen, sind das etwa $\frac{100-70}{9{,}13} \approx 3{,}3$ Standardabweichungen — außerhalb der 3σ-Umgebung, was auf einen unfairen Würfel hindeutet.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Varianz]] — Quadrat der Standardabweichung
- → [[Erwartungswert]] — Zentrum der Verteilung
- → [[Binomialverteilung]] — Formel $\sigma = \sqrt{n \cdot p \cdot q}$
- → [[Normalverteilung]] — Sigma-Regeln gelten exakt
- → [[Normalapproximation]] — Approximation der Binomialverteilung

> [!warning] **Prüfungsrelevant**
> - Definition: $\sigma = \sqrt{\text{Var}(X)}$
> - Formel für Binomialverteilung: $\sigma = \sqrt{n \cdot p \cdot q}$
> - Sigma-Umgebungen und ihre Wahrscheinlichkeiten (68-95-99,7-Regel)
> - Interpretation der Standardabweichung im Sachkontext

> [!question] **Typische Prüfungsfragen**
> - Berechne Erwartungswert und Standardabweichung für die binomialverteilte Zufallsvariable.
> - Bestimme die 2σ-Umgebung und interpretiere sie im Sachkontext.
> - Beurteile, ob das beobachtete Ergebnis ungewöhnlich ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Normalverteilung]] — Sigma-Regeln im Detail
> - [[Normalapproximation]] — Verwendung von σ bei der Approximation
