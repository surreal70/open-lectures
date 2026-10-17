---
author: Andreas Hümmer
title: Normalverteilung
tags:
  - content
  - mathe
  - stochastik
  - normalverteilung
  - gauß
  - stetig
created: 2026-10-17
modified: 2026-10-17
---

# Normalverteilung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Normalverteilung als wichtigste stetige Verteilung verstehen
> - Die Dichtefunktion und ihre Eigenschaften kennen
> - Die Parameter μ und σ interpretieren können
> - Die Sigma-Regeln anwenden und Wahrscheinlichkeiten berechnen

---

## Überblick

Die **Normalverteilung** (auch: Gauß-Verteilung) ist die bedeutendste [[Wahrscheinlichkeitsverteilungen|Wahrscheinlichkeitsverteilung]] der Statistik. Sie beschreibt viele natürliche Phänomene wie Körpergrößen, Messfehler oder IQ-Werte. Ihre charakteristische Glockenkurve ist nach Carl Friedrich Gauß (1777–1855) benannt.

## Definition der Normalverteilung

Eine stetige Zufallsvariable $X$ heißt **normalverteilt** mit Parametern $\mu$ und $\sigma$ (Schreibweise: $X \sim N(\mu, \sigma^2)$), wenn ihre Dichtefunktion gegeben ist durch:

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

### Parameter

| Parameter | Bedeutung | Einfluss auf die Kurve |
|-----------|-----------|----------------------|
| $\mu$ | [[Erwartungswert]] | Lage (Verschiebung) |
| $\sigma$ | [[Standardabweichung]] | Breite (Streuung) |
| $\sigma^2$ | [[Varianz]] | — |

## Die Glockenkurve

Die Dichtefunktion hat die charakteristische Form einer Glocke:

```
f(x)
  |
  |           ████
  |         ██    ██
  |        █        █
  |       █          █
  |      █            █
  |     █              █
  |   ██                ██
  | ██                    ██
  +████████████████████████████
           μ-σ  μ  μ+σ        x
```

### Eigenschaften der Glockenkurve

1. **Symmetrisch** bezüglich $x = \mu$
2. **Maximum** bei $x = \mu$ mit $f(\mu) = \frac{1}{\sigma\sqrt{2\pi}}$
3. **Wendepunkte** bei $x = \mu \pm \sigma$
4. **Asymptotisch**: $f(x) \to 0$ für $x \to \pm\infty$
5. **Normiert**: $\displaystyle\int_{-\infty}^{\infty} f(x) \, dx = 1$

## Einfluss der Parameter

### Einfluss von μ (Erwartungswert)

Der Parameter $\mu$ verschiebt die Kurve entlang der x-Achse:

- Größeres $\mu$ → Kurve nach rechts
- Kleineres $\mu$ → Kurve nach links

### Einfluss von σ (Standardabweichung)

Der Parameter $\sigma$ bestimmt die Breite:

- Größeres $\sigma$ → flachere, breitere Kurve
- Kleineres $\sigma$ → steilere, schmalere Kurve

Die Fläche unter der Kurve bleibt immer 1.

## Die Sigma-Regeln

Die Sigma-Regeln geben an, welcher Anteil der Werte in bestimmten Umgebungen des Erwartungswerts liegt:

### 68-95-99,7-Regel

$$P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 68{,}27\%$$

$$P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 95{,}45\%$$

$$P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 99{,}73\%$$

### Grafische Darstellung

```
         ◄───────── 99,7% ──────────►
         ◄────── 95,45% ──────►
              ◄─ 68,27% ─►
    ─────┼─────┼─────┼─────┼─────┼─────┼─────
       μ-3σ  μ-2σ  μ-σ    μ   μ+σ  μ+2σ μ+3σ
```

### Weitere häufig verwendete Werte

| Intervall | Wahrscheinlichkeit |
|-----------|-------------------|
| $[\mu - 1{,}64\sigma, \mu + 1{,}64\sigma]$ | 90% |
| $[\mu - 1{,}96\sigma, \mu + 1{,}96\sigma]$ | 95% |
| $[\mu - 2{,}58\sigma, \mu + 2{,}58\sigma]$ | 99% |

## Wahrscheinlichkeitsberechnung

Bei stetigen Verteilungen werden Wahrscheinlichkeiten als Flächen unter der Dichtefunktion berechnet:

$$P(a \leq X \leq b) = \int_a^b f(x) \, dx$$

Da dieses Integral für die Normalverteilung nicht elementar lösbar ist, verwendet man:
1. Die [[Standardnormalverteilung]] mit Tabellen
2. Taschenrechner mit Normalverteilungsfunktionen

### Wichtige Eigenschaft

Bei stetigen Verteilungen gilt: $P(X = a) = 0$

Daher ist: $P(a \leq X \leq b) = P(a < X < b) = P(a \leq X < b) = P(a < X \leq b)$

## Beispiel: Körpergröße

Die Körpergröße erwachsener Männer in Deutschland ist annähernd normalverteilt mit $\mu = 178$ cm und $\sigma = 7$ cm.

**a) Welcher Anteil ist größer als 185 cm?**

$185 = 178 + 7 = \mu + \sigma$

Nach der 68-Regel liegen etwa 68% im Intervall $[171, 185]$.

Da die Verteilung symmetrisch ist:
- Etwa 16% sind kleiner als 171 cm
- Etwa 16% sind größer als 185 cm

**b) In welchem Bereich liegen 95% der Körpergrößen?**

Nach der 95-Regel: $[\mu - 2\sigma, \mu + 2\sigma] = [164, 192]$ cm

## Bedeutung der Normalverteilung

### Zentraler Grenzwertsatz

Wenn viele unabhängige Zufallseinflüsse zusammenwirken, ist die resultierende Verteilung oft annähernd normalverteilt — unabhängig von den Einzelverteilungen.

### Anwendungen

- **Naturwissenschaften**: Messfehler, biologische Merkmale
- **Technik**: Qualitätskontrolle, Toleranzen
- **Wirtschaft**: Renditen, Prognosen
- **Psychologie**: Testscores, IQ-Werte
- **Statistik**: Grundlage vieler Testverfahren (siehe [[15-Statistik-und-Hypothesentests-Index]])

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Standardnormalverteilung]] — Normierte Form mit $\mu = 0$, $\sigma = 1$
- → [[Normalapproximation]] — Approximation der Binomialverteilung
- → [[Binomialverteilung]] — Wird für große $n$ durch Normalverteilung approximiert
- → [[Erwartungswert]] — Der Parameter $\mu$
- → [[Standardabweichung]] — Der Parameter $\sigma$

> [!warning] **Prüfungsrelevant**
> - Form und Eigenschaften der Glockenkurve
> - Interpretation der Parameter $\mu$ und $\sigma$
> - Die Sigma-Regeln (68-95-99,7)
> - Berechnung von Wahrscheinlichkeiten mit der Standardnormalverteilung
> - Anwendung auf Sachkontexte

> [!question] **Typische Prüfungsfragen**
> - Skizziere die Dichtefunktion und markiere die Parameter $\mu$ und $\sigma$.
> - Welcher Anteil einer normalverteilten Größe liegt im Intervall $[\mu - 2\sigma, \mu + \sigma]$?
> - Bestimme das Intervall, in dem 90% der Werte liegen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Georgii, H.-O.: Stochastik: Einführung in die Wahrscheinlichkeitstheorie und Statistik. De Gruyter, 2015.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Standardnormalverteilung]] — Berechnung mit z-Transformation
> - [[Normalapproximation]] — Approximation der Binomialverteilung
