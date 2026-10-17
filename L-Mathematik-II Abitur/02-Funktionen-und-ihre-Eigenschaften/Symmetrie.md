---
author: Andreas Hümmer
title: Symmetrie
tags:
  - content
  - mathe
  - funktionen
  - symmetrie
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Symmetrie

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Achsensymmetrie und Punktsymmetrie von Funktionsgraphen erkennen und nachweisen können
> - Die algebraischen Kriterien für gerade und ungerade Funktionen anwenden können
> - Symmetrie zur Vereinfachung von Berechnungen nutzen können
> - Symmetrie bei zusammengesetzten Funktionen analysieren können

---

## Überblick

**Symmetrie** ist eine fundamentale Eigenschaft von Funktionen, die den Funktionsgraph charakterisiert und Berechnungen erheblich vereinfachen kann. In diesem Kapitel betrachten wir die beiden wichtigsten Symmetriearten: Achsensymmetrie zur $y$-Achse und Punktsymmetrie zum Ursprung.

## Achsensymmetrie zur y-Achse

### Definition

Eine Funktion $f$ heißt **achsensymmetrisch zur $y$-Achse** (oder **gerade Funktion**), wenn für alle $x \in D_f$ gilt:

$$f(-x) = f(x)$$

**Voraussetzung:** Der Definitionsbereich muss symmetrisch zum Ursprung sein, d.h. $x \in D_f \Leftrightarrow -x \in D_f$.

### Geometrische Bedeutung

Der Graph ist spiegelbildlich zur $y$-Achse. Jeder Punkt $(x, y)$ auf dem Graphen hat einen Spiegelpunkt $(-x, y)$.

### Beispiele gerader Funktionen

- $f(x) = x^2$ (und allgemein $x^{2n}$)
- $f(x) = |x|$
- $f(x) = \cos(x)$
- $f(x) = x^4 - 3x^2 + 1$
- $f(x) = e^{x^2}$

### Nachweis

**Beispiel:** Zeige, dass $f(x) = x^4 - 2x^2 + 5$ eine gerade Funktion ist.

$$f(-x) = (-x)^4 - 2(-x)^2 + 5 = x^4 - 2x^2 + 5 = f(x) \quad \checkmark$$

## Punktsymmetrie zum Ursprung

### Definition

Eine Funktion $f$ heißt **punktsymmetrisch zum Ursprung** (oder **ungerade Funktion**), wenn für alle $x \in D_f$ gilt:

$$f(-x) = -f(x)$$

**Voraussetzung:** Auch hier muss $D_f$ symmetrisch zum Ursprung sein.

### Geometrische Bedeutung

Der Graph ist punktsymmetrisch zum Koordinatenursprung $(0, 0)$. Jeder Punkt $(x, y)$ hat einen Spiegelpunkt $(-x, -y)$.

**Konsequenz:** Wenn $0 \in D_f$, dann muss $f(0) = 0$ gelten, denn:
$$f(-0) = f(0) = -f(0) \quad \Rightarrow \quad 2f(0) = 0 \quad \Rightarrow \quad f(0) = 0$$

### Beispiele ungerader Funktionen

- $f(x) = x$ (und allgemein $x^{2n+1}$)
- $f(x) = x^3$
- $f(x) = \sin(x)$
- $f(x) = \tan(x)$
- $f(x) = \frac{x}{x^2 + 1}$

### Nachweis

**Beispiel:** Zeige, dass $f(x) = x^3 - 4x$ eine ungerade Funktion ist.

$$f(-x) = (-x)^3 - 4(-x) = -x^3 + 4x = -(x^3 - 4x) = -f(x) \quad \checkmark$$

## Kriterium für Polynome

Bei **Polynomfunktionen** lässt sich die Symmetrie direkt an den Exponenten ablesen:

| Exponentenart | Symmetrie |
|--------------|-----------|
| Nur gerade Exponenten (inkl. 0) | gerade Funktion (achsensymmetrisch) |
| Nur ungerade Exponenten | ungerade Funktion (punktsymmetrisch) |
| Gemischte Exponenten | keine Symmetrie |

**Beispiele:**
- $f(x) = 3x^4 - x^2 + 7$ (Exponenten: 4, 2, 0) → gerade
- $f(x) = x^5 - 2x^3 + x$ (Exponenten: 5, 3, 1) → ungerade
- $f(x) = x^3 + x^2$ (Exponenten: 3, 2) → keine Symmetrie

## Rechenregeln

### Summen und Differenzen

| $f$ | $g$ | $f + g$ | $f - g$ |
|-----|-----|---------|---------|
| gerade | gerade | gerade | gerade |
| ungerade | ungerade | ungerade | ungerade |
| gerade | ungerade | weder noch | weder noch |

### Produkte

| $f$ | $g$ | $f \cdot g$ |
|-----|-----|-------------|
| gerade | gerade | gerade |
| ungerade | ungerade | gerade |
| gerade | ungerade | ungerade |

**Merkregel:** Wie bei Multiplikation von Vorzeichen:
- gerade × gerade = gerade (+ × + = +)
- ungerade × ungerade = gerade (− × − = +)
- gerade × ungerade = ungerade (+ × − = −)

### Quotienten

Dieselben Regeln wie bei Produkten gelten auch für $\frac{f}{g}$.

### Verkettung

| Äußere $f$ | Innere $g$ | $f \circ g$ |
|------------|------------|-------------|
| gerade | gerade | gerade |
| gerade | ungerade | gerade |
| ungerade | gerade | gerade |
| ungerade | ungerade | ungerade |

## Zerlegung in geraden und ungeraden Anteil

Jede Funktion $f$ mit symmetrischem Definitionsbereich lässt sich eindeutig zerlegen in:

$$f(x) = f_g(x) + f_u(x)$$

mit:
- **gerader Anteil:** $f_g(x) = \frac{f(x) + f(-x)}{2}$
- **ungerader Anteil:** $f_u(x) = \frac{f(x) - f(-x)}{2}$

**Beispiel:** $f(x) = e^x$

$$f_g(x) = \frac{e^x + e^{-x}}{2} = \cosh(x)$$
$$f_u(x) = \frac{e^x - e^{-x}}{2} = \sinh(x)$$

Also: $e^x = \cosh(x) + \sinh(x)$

## Anwendungen

### Vereinfachung von Integralen

Für symmetrische Integrationsgrenzen gilt:

- **Gerade Funktion:**
$$\int_{-a}^{a} f(x) \, dx = 2 \int_{0}^{a} f(x) \, dx$$

- **Ungerade Funktion:**
$$\int_{-a}^{a} f(x) \, dx = 0$$

**Beispiel:** 
$$\int_{-2}^{2} x^3 \, dx = 0 \quad \text{(da } x^3 \text{ ungerade)}$$
$$\int_{-2}^{2} x^2 \, dx = 2 \int_{0}^{2} x^2 \, dx = 2 \cdot \frac{8}{3} = \frac{16}{3}$$

### Fourierreihen

Bei Fourierentwicklungen:
- Gerade Funktionen haben nur Kosinusterme
- Ungerade Funktionen haben nur Sinusterme

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Monotonie]] – Symmetrie beeinflusst das Monotonieverhalten
- → [[Trigonometrische-Funktionen]] – Kosinus ist gerade, Sinus ist ungerade
- → [[Polynomfunktionen]] – Symmetrie anhand der Exponenten
- → [[07-Integralrechnung-I|Integralrechnung]] – Ausnutzen von Symmetrie bei Integralen

> [!warning] **Prüfungsrelevant**
> - Formale Definitionen und Nachweise von Symmetrie
> - Kriterium für Polynome (gerade/ungerade Exponenten)
> - Rechenregeln für Produkte und Verkettungen
> - Ausnutzen der Symmetrie bei Integralen

> [!question] **Typische Prüfungsfragen**
> - Untersuche $f(x) = \frac{x^2}{1+x^4}$ auf Symmetrie.
> - Zeige, dass $f(x) = x \cdot |x|$ eine ungerade Funktion ist.
> - Berechne $\int_{-\pi}^{\pi} x \cdot \cos(x) \, dx$ unter Ausnutzung von Symmetrie.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Transformationen]] – Spiegelungen als Transformation
> - [[08-Integralrechnung-II|Integralrechnung II]] – Fortgeschrittene Integrationstechniken
> - [[Glossar]] – Mathematische Fachbegriffe
