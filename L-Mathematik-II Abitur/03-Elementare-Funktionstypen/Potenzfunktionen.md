---
author: Andreas Hümmer
title: Potenzfunktionen
tags:
  - content
  - mathe
  - funktionen
  - potenzfunktion
created: 2025-06-19
modified: 2025-06-19
---

# Potenzfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Potenzfunktionen für verschiedene Exponententypen unterscheiden können
> - Das Verhalten von Potenzfunktionen für natürliche, negative und rationale Exponenten analysieren können
> - Graphen von Potenzfunktionen skizzieren und ihre Eigenschaften beschreiben können
> - Den Zusammenhang zu Wurzel- und gebrochenrationalen Funktionen verstehen

---

## Überblick

Potenzfunktionen haben die Form $f(x) = x^n$, wobei der Exponent $n$ eine feste Zahl und die Basis $x$ die Variable ist. Je nach Wert des Exponenten ergeben sich unterschiedliche Funktionstypen mit charakteristischen Eigenschaften. Potenzfunktionen bilden die Grundbausteine der Polynomfunktionen und sind eng mit Wurzelfunktionen und Hyperbeln verknüpft.

## Definition

Eine **Potenzfunktion** ist eine Funktion der Form:

$$f(x) = x^n$$

wobei $n \in \mathbb{R}$ ein fester Exponent ist.

Die allgemeinere Form mit Vorfaktor:

$$f(x) = a \cdot x^n \quad (a \neq 0)$$

## Potenzfunktionen mit natürlichen Exponenten

### Gerade Exponenten $n = 2, 4, 6, \ldots$

$$f(x) = x^n \quad \text{für } n \in \{2, 4, 6, \ldots\}$$

**Eigenschaften:**
- Definitionsbereich: $D_f = \mathbb{R}$
- Wertebereich: $W_f = [0, +\infty)$
- **Achsensymmetrisch** zur y-Achse: $f(-x) = f(x)$
- Nullstelle: $x = 0$ (mit Vielfachheit $n$)
- Minimum bei $x = 0$ mit $f(0) = 0$
- Streng monoton fallend auf $(-\infty, 0]$, steigend auf $[0, +\infty)$

**Vergleich der Graphen:**
- Für $|x| < 1$: Je größer $n$, desto flacher der Graph
- Für $|x| > 1$: Je größer $n$, desto steiler der Graph
- Alle Graphen gehen durch $(0|0)$, $(1|1)$ und $(-1|1)$

### Ungerade Exponenten $n = 1, 3, 5, \ldots$

$$f(x) = x^n \quad \text{für } n \in \{1, 3, 5, \ldots\}$$

**Eigenschaften:**
- Definitionsbereich: $D_f = \mathbb{R}$
- Wertebereich: $W_f = \mathbb{R}$
- **Punktsymmetrisch** zum Ursprung: $f(-x) = -f(x)$
- Nullstelle: $x = 0$
- Kein Extremum
- Streng monoton steigend auf ganz $\mathbb{R}$
- Wendepunkt bei $x = 0$ (für $n \geq 3$)

**Gemeinsame Punkte:** $(0|0)$, $(1|1)$ und $(-1|-1)$

## Potenzfunktionen mit negativen Exponenten

### Gerade negative Exponenten $n = -2, -4, -6, \ldots$

$$f(x) = x^{-n} = \frac{1}{x^n} \quad \text{für } n \in \{2, 4, 6, \ldots\}$$

**Eigenschaften:**
- Definitionsbereich: $D_f = \mathbb{R} \setminus \{0\}$
- Wertebereich: $W_f = (0, +\infty)$
- **Achsensymmetrisch** zur y-Achse
- Keine Nullstellen
- Polstelle bei $x = 0$ (ohne Vorzeichenwechsel)
- Horizontale Asymptote: $y = 0$
- Streng monoton steigend auf $(-\infty, 0)$, fallend auf $(0, +\infty)$

### Ungerade negative Exponenten $n = -1, -3, -5, \ldots$

$$f(x) = x^{-n} = \frac{1}{x^n} \quad \text{für } n \in \{1, 3, 5, \ldots\}$$

**Eigenschaften:**
- Definitionsbereich: $D_f = \mathbb{R} \setminus \{0\}$
- Wertebereich: $W_f = \mathbb{R} \setminus \{0\}$
- **Punktsymmetrisch** zum Ursprung
- Keine Nullstellen
- Polstelle bei $x = 0$ (mit Vorzeichenwechsel)
- Horizontale Asymptote: $y = 0$
- Streng monoton fallend auf $(-\infty, 0)$ und $(0, +\infty)$

### Die Hyperbel $f(x) = \frac{1}{x}$

Als wichtigster Vertreter:

$$f(x) = x^{-1} = \frac{1}{x}$$

```
     y
     │     ╲
     │      ╲
     │       ╲
     │        ╲__
─────┼────────────── x
   __│
  ╱  │
 ╱   │
╱    │
```

## Potenzfunktionen mit rationalen Exponenten

### Positive rationale Exponenten

Für $n = \frac{p}{q}$ mit $p, q \in \mathbb{N}$:

$$f(x) = x^{\frac{p}{q}} = \sqrt[q]{x^p} = \left(\sqrt[q]{x}\right)^p$$

**Definitionsbereich:**
- Für $q$ gerade: $D_f = [0, +\infty)$
- Für $q$ ungerade: $D_f = \mathbb{R}$

**Beispiele:**
- $f(x) = x^{1/2} = \sqrt{x}$ (Wurzelfunktion)
- $f(x) = x^{3/2} = x \cdot \sqrt{x}$
- $f(x) = x^{2/3} = \sqrt[3]{x^2}$

### Negative rationale Exponenten

$$f(x) = x^{-\frac{p}{q}} = \frac{1}{x^{\frac{p}{q}}} = \frac{1}{\sqrt[q]{x^p}}$$

**Definitionsbereich:** Zusätzlich muss $x \neq 0$ gelten.

## Zusammenfassung der Eigenschaften

| Exponent $n$ | $D_f$ | $W_f$ | Symmetrie | Asymptoten |
|--------------|-------|-------|-----------|------------|
| gerade $> 0$ | $\mathbb{R}$ | $[0, +\infty)$ | Achsensymm. | keine |
| ungerade $> 0$ | $\mathbb{R}$ | $\mathbb{R}$ | Punktsymm. | keine |
| gerade $< 0$ | $\mathbb{R} \setminus \{0\}$ | $(0, +\infty)$ | Achsensymm. | $x=0$, $y=0$ |
| ungerade $< 0$ | $\mathbb{R} \setminus \{0\}$ | $\mathbb{R} \setminus \{0\}$ | Punktsymm. | $x=0$, $y=0$ |
| $0 < n < 1$ | $[0, +\infty)$ | $[0, +\infty)$ | keine | keine |

## Transformationen

Die allgemeine Potenzfunktion $f(x) = a(x-b)^n + c$ entsteht aus $g(x) = x^n$ durch:

- Streckung/Stauchung mit Faktor $|a|$
- Spiegelung an der x-Achse für $a < 0$
- Verschiebung um $b$ in x-Richtung
- Verschiebung um $c$ in y-Richtung

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Potenzen-mit-rationalen-Exponenten]] — Algebraische Grundlagen
- → [[Wurzelfunktionen]] — Spezialfall für $n = 1/q$
- → [[Gebrochenrationale-Funktionen]] — Spezialfall für negative ganzzahlige $n$
- → [[Polynomfunktionen]] — Linearkombinationen von Potenzfunktionen
- → [[Symmetrie]] — Achsen- und Punktsymmetrie
- → [[Transformationen]] — Verschiebung und Streckung

> [!warning] **Prüfungsrelevant**
> - Zuordnung von Graphen zu Potenzfunktionen anhand charakteristischer Eigenschaften
> - Symmetrieverhalten bei geraden und ungeraden Exponenten
> - Definitions- und Wertebereich bei verschiedenen Exponententypen
> - Verhalten für $x \to 0$ und $x \to \pm\infty$
> - Transformierte Potenzfunktionen erkennen und analysieren

> [!question] **Typische Prüfungsfragen**
> - Ordnen Sie die Graphen den Funktionen $f(x) = x^2$, $g(x) = x^4$ und $h(x) = x^{-2}$ zu und begründen Sie.
> - Bestimmen Sie den maximalen Definitionsbereich von $f(x) = x^{-3/4}$.
> - Skizzieren Sie $f(x) = -2(x+1)^3 + 3$ und geben Sie die Transformation ausgehend von $g(x) = x^3$ an.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, 2023

> [!tip] **Weiterführende Links**
> - [[Exponentialfunktionen]] — Exponenten als Variable: $f(x) = a^x$
> - [[05-Differentialrechnung-I|Differentialrechnung]] — Ableitung von Potenzfunktionen

