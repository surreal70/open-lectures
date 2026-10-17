---
author: Andreas Hümmer
title: Wurzelfunktionen
tags:
  - content
  - mathe
  - funktionen
  - wurzelfunktion
created: 2025-06-19
modified: 2025-06-19
---

# Wurzelfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Wurzelfunktionen als Umkehrfunktionen von Potenzfunktionen verstehen
> - Definitions- und Wertebereich verschiedener Wurzelfunktionen bestimmen können
> - Graphen von Wurzelfunktionen skizzieren und transformieren können
> - Gleichungen mit Wurzeln lösen und Lösungen auf Gültigkeit prüfen können

---

## Überblick

Wurzelfunktionen sind die Umkehrfunktionen der Potenzfunktionen mit natürlichen Exponenten. Die bekannteste Vertreterin ist die Quadratwurzelfunktion $f(x) = \sqrt{x}$. Im Gegensatz zu Potenzfunktionen haben Wurzelfunktionen einen eingeschränkten Definitionsbereich, da negative Argumente unter geraden Wurzeln im Reellen nicht definiert sind. Wurzelfunktionen spielen in Physik und Technik eine wichtige Rolle, etwa bei der Berechnung von Pendelperioden oder Flugzeiten.

## Definition

### Die n-te Wurzel

Die **n-te Wurzelfunktion** ist definiert als:

$$f(x) = \sqrt[n]{x} = x^{\frac{1}{n}}$$

Sie ist die Umkehrfunktion von $g(x) = x^n$ (eingeschränkt auf geeignete Bereiche).

### Definitionsbereich

| Wurzelindex $n$ | Definitionsbereich |
|-----------------|-------------------|
| gerade ($n = 2, 4, 6, \ldots$) | $D_f = [0, +\infty)$ |
| ungerade ($n = 3, 5, 7, \ldots$) | $D_f = \mathbb{R}$ |

**Grund:** Bei geradem $n$ hat die Gleichung $x^n = a$ für $a < 0$ keine reelle Lösung.

## Die Quadratwurzelfunktion

### Definition und Eigenschaften

$$f(x) = \sqrt{x} = x^{\frac{1}{2}} \quad \text{für } x \geq 0$$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = [0, +\infty)$ |
| Wertebereich | $W_f = [0, +\infty)$ |
| Nullstelle | $x = 0$ |
| Monotonie | streng monoton steigend |
| Symmetrie | keine |
| Asymptote | keine |

### Graph

Der Graph von $f(x) = \sqrt{x}$ ist die obere Hälfte einer nach rechts geöffneten Parabel:

```
  y
  │     ╱
  │   ╱
  │ ╱
  │╱
  └────────── x
  0
```

### Charakteristische Punkte

- $(0|0)$ — Startpunkt
- $(1|1)$ — immer auf dem Graphen jeder Wurzelfunktion
- $(4|2)$, $(9|3)$, $(16|4)$ — Quadratzahlen liefern ganzzahlige Werte

## Höhere Wurzelfunktionen

### Kubikwurzelfunktion $f(x) = \sqrt[3]{x}$

- Definitionsbereich: $D_f = \mathbb{R}$
- Wertebereich: $W_f = \mathbb{R}$
- **Punktsymmetrisch** zum Ursprung
- Streng monoton steigend auf ganz $\mathbb{R}$

**Besonderheit:** Die Kubikwurzel aus negativen Zahlen ist definiert:
$$\sqrt[3]{-8} = -2 \quad \text{da } (-2)^3 = -8$$

### Allgemeine n-te Wurzelfunktion

Für beliebiges $n \in \mathbb{N}$:

$$f(x) = \sqrt[n]{x} = x^{\frac{1}{n}}$$

**Vergleich der Graphen für $x \geq 0$:**
- Alle Graphen gehen durch $(0|0)$ und $(1|1)$
- Für $0 < x < 1$: Je größer $n$, desto größer $\sqrt[n]{x}$
- Für $x > 1$: Je größer $n$, desto kleiner $\sqrt[n]{x}$

## Zusammenhang mit Potenzfunktionen

### Umkehrrelation

Die Wurzelfunktion $f(x) = \sqrt[n]{x}$ ist die Umkehrfunktion der Potenzfunktion $g(x) = x^n$:

$$\sqrt[n]{x^n} = x \quad \text{für geeignete } x$$
$$\left(\sqrt[n]{x}\right)^n = x \quad \text{für } x \geq 0$$

**Achtung bei geraden $n$:**
$$\sqrt{x^2} = |x| \neq x \quad \text{für } x < 0$$

### Rationale Exponenten

Wurzeln lassen sich als Potenzen mit rationalen Exponenten schreiben:

$$\sqrt[n]{x^m} = x^{\frac{m}{n}}$$

**Beispiele:**
- $\sqrt{x^3} = x^{\frac{3}{2}}$
- $\sqrt[3]{x^2} = x^{\frac{2}{3}}$
- $\frac{1}{\sqrt{x}} = x^{-\frac{1}{2}}$

## Transformationen

Die allgemeine Form einer transformierten Wurzelfunktion:

$$f(x) = a \cdot \sqrt[n]{x - b} + c$$

| Parameter | Transformation |
|-----------|----------------|
| $a > 1$ | Streckung in y-Richtung |
| $0 < a < 1$ | Stauchung in y-Richtung |
| $a < 0$ | Spiegelung an der x-Achse |
| $b > 0$ | Verschiebung um $b$ nach rechts |
| $b < 0$ | Verschiebung um $|b|$ nach links |
| $c$ | Verschiebung um $c$ in y-Richtung |

**Beispiel:**
$f(x) = 2\sqrt{x-3} + 1$
- Verschiebung um 3 nach rechts
- Streckung mit Faktor 2
- Verschiebung um 1 nach oben
- Definitionsbereich: $D_f = [3, +\infty)$

## Gleichungen mit Wurzeln

### Lösungsverfahren

1. Wurzel isolieren
2. Beide Seiten potenzieren
3. **Probe durchführen** (Scheinlösungen ausschließen!)

### Beispiel

$$\sqrt{2x+1} = x - 1$$

**Bedingung:** $2x + 1 \geq 0$ und $x - 1 \geq 0$, also $x \geq 1$

Quadrieren: $2x + 1 = (x-1)^2 = x^2 - 2x + 1$

Umformen: $x^2 - 4x = 0 \Rightarrow x(x-4) = 0$

Lösungskandidaten: $x_1 = 0$, $x_2 = 4$

**Probe:**
- $x = 0$: $\sqrt{1} = -1$ ✗ (falsch, da $-1 < 0$)
- $x = 4$: $\sqrt{9} = 3$ ✓

**Lösung:** $x = 4$

### Scheinlösungen

Beim Potenzieren können Lösungen entstehen, die die ursprüngliche Gleichung nicht erfüllen. Die **Probe ist unerlässlich!**

## Anwendungen

### Freier Fall

Die Fallzeit aus Höhe $h$:
$$t = \sqrt{\frac{2h}{g}}$$

### Pendelschwingung

Die Periodendauer eines mathematischen Pendels:
$$T = 2\pi\sqrt{\frac{l}{g}}$$

### Bremsweg

Der Anhalteweg eines Fahrzeugs ist proportional zu $v^2$, umgekehrt:
$$v = \sqrt{2as}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Potenzfunktionen]] — Umkehrbeziehung
- → [[Potenzen-mit-rationalen-Exponenten]] — Algebraische Grundlagen
- → [[Wurzelterme]] — Rechnen mit Wurzeln
- → [[Umkehrfunktionen]] — Allgemeine Theorie der Umkehrfunktion
- → [[Definitionsbereich]] — Einschränkungen bei Wurzelfunktionen
- → [[Transformationen]] — Verschiebung und Streckung

> [!warning] **Prüfungsrelevant**
> - Definitionsbereich: gerade Wurzeln nur für nicht-negative Argumente
> - Umrechnung zwischen Wurzel- und Potenzschreibweise
> - Bei Wurzelgleichungen: Bedingungen beachten und Probe durchführen
> - Graphen transformierter Wurzelfunktionen skizzieren können
> - $\sqrt{x^2} = |x|$ (nicht $x$!)

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie den Definitionsbereich von $f(x) = \sqrt{4-x^2}$.
> - Lösen Sie die Gleichung $\sqrt{x+5} + 1 = x$ und führen Sie die Probe durch.
> - Skizzieren Sie den Graphen von $f(x) = -\sqrt{x+2} + 3$ und geben Sie Definitions- und Wertebereich an.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, 2023

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] — Ableitung von Wurzelfunktionen
> - [[Betrag-und-Betragsgleichungen]] — Zusammenhang $\sqrt{x^2} = |x|$

