---
author: Andreas Hümmer
title: Standardnormalverteilung
tags:
  - content
  - mathe
  - stochastik
  - normalverteilung
  - standardnormalverteilung
  - z-transformation
created: 2026-10-17
modified: 2026-10-17
---

# Standardnormalverteilung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Standardnormalverteilung als spezielle Normalverteilung kennen
> - Die z-Transformation durchführen können
> - Wahrscheinlichkeiten mit der Φ-Tabelle berechnen
> - Quantile der Standardnormalverteilung bestimmen

---

## Überblick

Die **Standardnormalverteilung** ist die [[Normalverteilung]] mit Erwartungswert $\mu = 0$ und Standardabweichung $\sigma = 1$. Sie dient als Referenzverteilung: Jede Normalverteilung kann durch **Standardisierung** (z-Transformation) auf die Standardnormalverteilung zurückgeführt werden.

## Definition

Eine Zufallsvariable $Z$ heißt **standardnormalverteilt** (Schreibweise: $Z \sim N(0, 1)$), wenn ihre Dichtefunktion gegeben ist durch:

$$\varphi(z) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{z^2}{2}}$$

### Eigenschaften

- Erwartungswert: $E(Z) = 0$
- Varianz: $\text{Var}(Z) = 1$
- Standardabweichung: $\sigma = 1$
- Symmetrisch um $z = 0$: $\varphi(-z) = \varphi(z)$

## Die Verteilungsfunktion Φ

Die **Verteilungsfunktion** der Standardnormalverteilung wird mit dem griechischen Buchstaben Φ (Phi) bezeichnet:

$$\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z} \varphi(t) \, dt$$

### Eigenschaften von Φ

1. $\Phi(-\infty) = 0$ und $\Phi(\infty) = 1$
2. $\Phi(0) = 0{,}5$ (Symmetrie)
3. $\Phi(-z) = 1 - \Phi(z)$ (Symmetrieregel)
4. $\Phi$ ist streng monoton steigend

### Wichtige Werte

| $z$ | $\Phi(z)$ |
|-----|-----------|
| $-3$ | $0{,}0013$ |
| $-2$ | $0{,}0228$ |
| $-1$ | $0{,}1587$ |
| $0$ | $0{,}5000$ |
| $1$ | $0{,}8413$ |
| $2$ | $0{,}9772$ |
| $3$ | $0{,}9987$ |

## Die z-Transformation

### Standardisierung

Ist $X \sim N(\mu, \sigma^2)$, so ist die standardisierte Variable

$$Z = \frac{X - \mu}{\sigma}$$

standardnormalverteilt: $Z \sim N(0, 1)$

### Interpretation

Der z-Wert gibt an, wie viele Standardabweichungen ein Wert $x$ vom Erwartungswert entfernt ist:

- $z > 0$: Wert liegt über dem Erwartungswert
- $z < 0$: Wert liegt unter dem Erwartungswert
- $|z| = 1$: Wert ist genau eine Standardabweichung entfernt

## Berechnung von Wahrscheinlichkeiten

### Grundformel

Für $X \sim N(\mu, \sigma^2)$ gilt:

$$P(X \leq x) = \Phi\left(\frac{x - \mu}{\sigma}\right)$$

### Bereichswahrscheinlichkeiten

$$P(a \leq X \leq b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$

### Symmetrieregel anwenden

$$\Phi(-z) = 1 - \Phi(z)$$

Diese Regel ist nötig, da Tabellen oft nur positive z-Werte enthalten.

## Beispiele

### Beispiel 1: Einfache Berechnung

Für $X \sim N(100, 15^2)$: Berechne $P(X \leq 115)$

$$z = \frac{115 - 100}{15} = 1$$

$$P(X \leq 115) = \Phi(1) = 0{,}8413$$

### Beispiel 2: Bereichswahrscheinlichkeit

Für $X \sim N(100, 15^2)$: Berechne $P(85 \leq X \leq 130)$

$$z_1 = \frac{85 - 100}{15} = -1$$
$$z_2 = \frac{130 - 100}{15} = 2$$

$$P(85 \leq X \leq 130) = \Phi(2) - \Phi(-1)$$
$$= \Phi(2) - (1 - \Phi(1))$$
$$= 0{,}9772 - (1 - 0{,}8413)$$
$$= 0{,}9772 - 0{,}1587 = 0{,}8185$$

### Beispiel 3: Komplementwahrscheinlichkeit

Für $X \sim N(100, 15^2)$: Berechne $P(X > 120)$

$$z = \frac{120 - 100}{15} = 1{,}33$$

$$P(X > 120) = 1 - P(X \leq 120) = 1 - \Phi(1{,}33)$$

Aus der Tabelle: $\Phi(1{,}33) \approx 0{,}9082$

$$P(X > 120) = 1 - 0{,}9082 = 0{,}0918$$

## Quantile der Standardnormalverteilung

### Definition

Das **$p$-Quantil** $z_p$ ist der Wert, unterhalb dessen $p \cdot 100\%$ aller Werte liegen:

$$\Phi(z_p) = p$$

### Wichtige Quantile

| $p$ | $z_p$ | Anwendung |
|-----|-------|-----------|
| $0{,}90$ | $1{,}28$ | 90%-Konfidenz, einseitig |
| $0{,}95$ | $1{,}64$ | 90%-Konfidenz, zweiseitig |
| $0{,}975$ | $1{,}96$ | 95%-Konfidenz, zweiseitig |
| $0{,}99$ | $2{,}33$ | 98%-Konfidenz, zweiseitig |
| $0{,}995$ | $2{,}58$ | 99%-Konfidenz, zweiseitig |

### Symmetrie nutzen

$$z_{1-p} = -z_p$$

Beispiel: $z_{0{,}05} = -z_{0{,}95} = -1{,}64$

## Ablesen aus der Φ-Tabelle

### Aufbau der Tabelle

Die Tabelle zeigt $\Phi(z)$ für positive $z$-Werte:

| $z$ | $0{,}00$ | $0{,}01$ | $0{,}02$ | $0{,}03$ | ... |
|-----|----------|----------|----------|----------|-----|
| $0{,}0$ | $0{,}5000$ | $0{,}5040$ | $0{,}5080$ | $0{,}5120$ | ... |
| $0{,}1$ | $0{,}5398$ | $0{,}5438$ | $0{,}5478$ | $0{,}5517$ | ... |
| $1{,}0$ | $0{,}8413$ | $0{,}8438$ | $0{,}8461$ | $0{,}8485$ | ... |
| $1{,}9$ | $0{,}9713$ | $0{,}9719$ | $0{,}9726$ | $0{,}9732$ | ... |

### Beispiel: $\Phi(1{,}96)$ ablesen

- Zeile: $z = 1{,}9$
- Spalte: $0{,}06$
- Ergebnis: $\Phi(1{,}96) = 0{,}9750$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Normalverteilung]] — Allgemeine Normalverteilung $N(\mu, \sigma^2)$
- → [[Normalapproximation]] — z-Transformation bei der Approximation
- → [[Standardabweichung]] — Der Parameter $\sigma$ für die z-Transformation
- → [[Erwartungswert]] — Der Parameter $\mu$ für die z-Transformation
- → [[Kumulative-Wahrscheinlichkeiten]] — Verteilungsfunktion $F(x)$

> [!warning] **Prüfungsrelevant**
> - z-Transformation: $z = \frac{x - \mu}{\sigma}$
> - Symmetrieregel: $\Phi(-z) = 1 - \Phi(z)$
> - Ablesen aus der Φ-Tabelle
> - Berechnung von Bereichswahrscheinlichkeiten
> - Wichtige Quantile: $z_{0{,}975} = 1{,}96$, $z_{0{,}995} = 2{,}58$

> [!question] **Typische Prüfungsfragen**
> - Berechne $P(X \leq x)$ für eine normalverteilte Zufallsvariable.
> - Bestimme das Intervall $[\mu - c, \mu + c]$, in dem 95% der Werte liegen.
> - Welcher z-Wert wird von 90% der Werte unterschritten?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bronstein, I. N., Semendjajew, K. A.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2016.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Normalapproximation]] — Anwendung auf die Binomialverteilung
> - [[15-Statistik-und-Hypothesentests-Index|Modul 15: Statistik]] — Anwendung in der schließenden Statistik
