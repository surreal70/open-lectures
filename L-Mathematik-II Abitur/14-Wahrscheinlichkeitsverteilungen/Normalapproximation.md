---
author: Andreas Hümmer
title: Normalapproximation
tags:
  - content
  - mathe
  - stochastik
  - normalapproximation
  - binomialverteilung
  - grenzwertsatz
created: 2026-10-17
modified: 2026-10-17
---

# Normalapproximation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Faustregel für die Anwendbarkeit der Normalapproximation kennen
> - Die Stetigkeitskorrektur verstehen und anwenden
> - Wahrscheinlichkeiten der Binomialverteilung mit der Normalverteilung approximieren
> - Den Grenzwertsatz von de Moivre-Laplace kennen

---

## Überblick

Für große $n$ nähert sich die [[Binomialverteilung]] der [[Normalverteilung]] an. Diese **Normalapproximation** ermöglicht es, Wahrscheinlichkeiten für binomialverteilte Zufallsvariablen näherungsweise mit der [[Standardnormalverteilung]] zu berechnen — ein wichtiges Werkzeug, wenn exakte Berechnungen zu aufwendig werden.

## Grenzwertsatz von de Moivre-Laplace

### Aussage

Ist $X \sim B(n, p)$, so gilt für $n \to \infty$:

$$\frac{X - np}{\sqrt{npq}} \xrightarrow{d} Z \sim N(0, 1)$$

In Worten: Die standardisierte Binomialverteilung konvergiert gegen die Standardnormalverteilung.

### Konsequenz

Für große $n$ gilt näherungsweise:

$$X \sim B(n, p) \approx N(\mu, \sigma^2) \quad \text{mit} \quad \mu = np, \; \sigma = \sqrt{npq}$$

## Faustregel für die Anwendbarkeit

Die Normalapproximation liefert gute Ergebnisse, wenn:

$$\sigma^2 = n \cdot p \cdot (1-p) > 9$$

Äquivalente Formulierungen:

$$npq > 9 \quad \Leftrightarrow \quad \sigma > 3$$

Alternative Faustregeln in der Literatur:

- $np > 5$ **und** $n(1-p) > 5$
- $np(1-p) \geq 9$

### Beispiel: Anwendbarkeit prüfen

Bei $n = 100$ und $p = 0{,}3$:

$$\sigma^2 = 100 \cdot 0{,}3 \cdot 0{,}7 = 21 > 9 \quad \checkmark$$

Die Normalapproximation ist anwendbar.

Bei $n = 20$ und $p = 0{,}1$:

$$\sigma^2 = 20 \cdot 0{,}1 \cdot 0{,}9 = 1{,}8 < 9 \quad \times$$

Die Normalapproximation sollte **nicht** angewendet werden.

## Die Stetigkeitskorrektur

### Problem

Die Binomialverteilung ist **diskret**, die Normalverteilung **stetig**. Bei der Approximation entsteht ein systematischer Fehler, da die diskrete Wahrscheinlichkeit $P(X = k)$ durch eine Fläche der Breite 0 approximiert würde.

### Lösung: Stetigkeitskorrektur

Die Einzelwahrscheinlichkeit $P(X = k)$ wird durch das Intervall $[k - 0{,}5; k + 0{,}5]$ approximiert:

$$P(X = k) \approx \Phi\left(\frac{k + 0{,}5 - \mu}{\sigma}\right) - \Phi\left(\frac{k - 0{,}5 - \mu}{\sigma}\right)$$

### Korrekturregeln für Ungleichungen

| Binomial | Korrigiert | Approximation |
|----------|------------|---------------|
| $P(X \leq k)$ | $P(X \leq k + 0{,}5)$ | $\Phi\left(\frac{k + 0{,}5 - \mu}{\sigma}\right)$ |
| $P(X < k)$ | $P(X \leq k - 0{,}5)$ | $\Phi\left(\frac{k - 0{,}5 - \mu}{\sigma}\right)$ |
| $P(X \geq k)$ | $P(X \geq k - 0{,}5)$ | $1 - \Phi\left(\frac{k - 0{,}5 - \mu}{\sigma}\right)$ |
| $P(X > k)$ | $P(X \geq k + 0{,}5)$ | $1 - \Phi\left(\frac{k + 0{,}5 - \mu}{\sigma}\right)$ |

### Merkhilfe

- Bei **$\leq$** und **$<$**: Grenze **erweitern** (um 0,5 nach rechts)
- Bei **$\geq$** und **$>$**: Grenze **erweitern** (um 0,5 nach links)

## Beispiel: Vollständige Berechnung

### Aufgabenstellung

Eine Münze wird 200-mal geworfen. Wie groß ist die Wahrscheinlichkeit für mindestens 110 Mal „Kopf"?

### Lösung

**Schritt 1: Parameter bestimmen**

$n = 200$, $p = 0{,}5$

$$\mu = np = 200 \cdot 0{,}5 = 100$$
$$\sigma = \sqrt{npq} = \sqrt{200 \cdot 0{,}5 \cdot 0{,}5} = \sqrt{50} \approx 7{,}07$$

**Schritt 2: Faustregel prüfen**

$$\sigma^2 = 50 > 9 \quad \checkmark$$

**Schritt 3: Stetigkeitskorrektur anwenden**

$$P(X \geq 110) \approx P(X \geq 109{,}5) \quad \text{(korrigiert)}$$

**Schritt 4: z-Transformation**

$$z = \frac{109{,}5 - 100}{7{,}07} = \frac{9{,}5}{7{,}07} \approx 1{,}34$$

**Schritt 5: Wahrscheinlichkeit berechnen**

$$P(X \geq 110) \approx 1 - \Phi(1{,}34) = 1 - 0{,}9099 = 0{,}0901$$

Die Wahrscheinlichkeit für mindestens 110-mal „Kopf" beträgt etwa 9%.

## Sigma-Umgebungen der Binomialverteilung

Mit der Normalapproximation lassen sich Sigma-Umgebungen für große $n$ bestimmen:

$$P(\mu - k\sigma \leq X \leq \mu + k\sigma) \approx \Phi(k) - \Phi(-k) = 2\Phi(k) - 1$$

### Standardwerte

| $k$ | Wahrscheinlichkeit |
|-----|-------------------|
| 1 | $\approx 68{,}3\%$ |
| 1,64 | $\approx 90\%$ |
| 1,96 | $\approx 95\%$ |
| 2 | $\approx 95{,}4\%$ |
| 2,58 | $\approx 99\%$ |
| 3 | $\approx 99{,}7\%$ |

## Grafischer Vergleich

Die Normalverteilung approximiert die Binomialverteilung umso besser, je größer $n$ ist:

```
                 B(20, 0,5)              N(10, √5)
P(X=k)                                  f(x)
  |                                       |
  |         █ █ █                         |        ╭──╮
  |       █ ║ ║ ║ █                       |      ╭╯    ╲
  |     █ ║ ║ ║ ║ ║ █                     |    ╭╯      ╲
  |   █ ║ ║ ║ ║ ║ ║ ║ █                   |  ╭╯          ╲
  +─█─║─║─║─║─║─║─║─║─║─█─              +─╯              ╲─
    0   5    10    15   20                  5    10    15
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Binomialverteilung]] — Exakte Verteilung, die approximiert wird
- → [[Normalverteilung]] — Die approximierende Verteilung
- → [[Standardnormalverteilung]] — Tabelle für die Berechnung
- → [[Standardabweichung]] — Faustregel: $\sigma > 3$
- → [[Grenzwerte-von-Folgen]] — Konvergenz im Grenzwertsatz

> [!warning] **Prüfungsrelevant**
> - Faustregel: $\sigma^2 = npq > 9$
> - Stetigkeitskorrektur: $\pm 0{,}5$ an den Grenzen
> - Berechnung mit z-Transformation: $z = \frac{k \pm 0{,}5 - \mu}{\sigma}$
> - Bestimmung von Sigma-Umgebungen

> [!question] **Typische Prüfungsfragen**
> - Prüfe, ob die Normalapproximation angewendet werden darf. Begründe.
> - Berechne die Wahrscheinlichkeit $P(X \geq k)$ mit der Normalapproximation.
> - Bestimme das Intervall, in dem mit 95%-iger Wahrscheinlichkeit die Trefferanzahl liegt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[15-Statistik-und-Hypothesentests-Index|Modul 15: Statistik]] — Anwendung bei Hypothesentests
> - [[Anwendungen-der-Wahrscheinlichkeitsrechnung]] — Praktische Beispiele
