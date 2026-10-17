---
author: Andreas Hümmer
title: Stetigkeit
tags:
  - content
  - mathe
  - funktionen
  - stetigkeit
  - grenzwert
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Stetigkeit

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Stetigkeit anschaulich und formal verstehen
> - Stetigkeitsuntersuchungen an gegebenen Stellen durchführen können
> - Verschiedene Arten von Unstetigkeitsstellen unterscheiden können
> - Den Zwischenwertsatz kennen und anwenden können
> - Wissen, welche Standardfunktionen stetig sind

---

## Überblick

**Stetigkeit** ist ein zentrales Konzept der Analysis, das beschreibt, wann der Graph einer Funktion "ohne Lücken oder Sprünge" ist. Anschaulich kann man eine stetige Funktion zeichnen, ohne den Stift abzusetzen. Formal bedeutet Stetigkeit, dass kleine Änderungen im Argument nur kleine Änderungen im Funktionswert bewirken – der Funktionswert verhält sich "vorhersagbar".

Stetigkeit ist eine Voraussetzung für viele wichtige Sätze der Analysis (Zwischenwertsatz, Extremwertsatz) und wird bei der Kurvendiskussion und Differentialrechnung vorausgesetzt.

## Anschauliche Definition

Eine Funktion $f$ ist **stetig an der Stelle $x_0$**, wenn:

1. $f(x_0)$ existiert (die Funktion ist an $x_0$ definiert)
2. Der Grenzwert $\lim_{x \to x_0} f(x)$ existiert
3. Grenzwert und Funktionswert stimmen überein: $\lim_{x \to x_0} f(x) = f(x_0)$

**Merkregel:** "Die Funktion hat keinen Sprung an $x_0$."

## Formale Definition (Epsilon-Delta)

Eine Funktion $f$ ist **stetig an der Stelle $x_0$**, wenn gilt:

$$\forall \varepsilon > 0 \; \exists \delta > 0 : |x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \varepsilon$$

**Interpretation:** Zu jeder "Toleranz" $\varepsilon$ für den Funktionswert gibt es eine "Toleranz" $\delta$ für das Argument, sodass Punkte im $\delta$-Umfeld von $x_0$ auf Funktionswerte im $\varepsilon$-Umfeld von $f(x_0)$ abgebildet werden.

## Definition für Intervalle

Eine Funktion $f$ heißt **stetig auf einem Intervall $I$**, wenn sie an jeder Stelle $x_0 \in I$ stetig ist.

**Randpunkte:** An den Randpunkten eines abgeschlossenen Intervalls $[a, b]$ wird nur einseitige Stetigkeit gefordert.

## Stetige Grundfunktionen

Folgende Funktionen sind auf ihrem gesamten Definitionsbereich stetig:

| Funktionstyp | Beispiele |
|--------------|-----------|
| Polynomfunktionen | $f(x) = x^3 - 2x + 1$ |
| Rationale Funktionen | $f(x) = \frac{x^2 + 1}{x - 1}$ (außer bei Nullstellen des Nenners) |
| Wurzelfunktionen | $f(x) = \sqrt{x}$ (für $x \geq 0$) |
| Exponentialfunktionen | $f(x) = e^x$, $f(x) = 2^x$ |
| Logarithmusfunktionen | $f(x) = \ln(x)$ (für $x > 0$) |
| Trigonometrische Funktionen | $\sin(x)$, $\cos(x)$, $\tan(x)$ (außer bei Polstellen) |
| Betragsfunktion | $f(x) = |x|$ |

## Rechenregeln für stetige Funktionen

Sind $f$ und $g$ stetig an der Stelle $x_0$, dann sind auch stetig an $x_0$:

- **Summe:** $f + g$
- **Differenz:** $f - g$
- **Produkt:** $f \cdot g$
- **Quotient:** $\frac{f}{g}$ (falls $g(x_0) \neq 0$)
- **Verkettung:** $f \circ g$ (falls $g$ stetig an $x_0$ und $f$ stetig an $g(x_0)$)
- **Skalierung:** $c \cdot f$ für $c \in \mathbb{R}$

## Arten von Unstetigkeitsstellen

### 1. Sprungstelle (Unstetigkeitsstelle 1. Art)

Beide einseitigen Grenzwerte existieren, sind aber verschieden:

$$\lim_{x \to x_0^-} f(x) \neq \lim_{x \to x_0^+} f(x)$$

**Beispiel:** Vorzeichenfunktion $\text{sgn}(x)$ bei $x = 0$

**Sprunghöhe:** $s = \left|\lim_{x \to x_0^+} f(x) - \lim_{x \to x_0^-} f(x)\right|$

### 2. Hebbare Unstetigkeitsstelle

Der Grenzwert existiert, aber $f(x_0)$ ist nicht definiert oder hat einen anderen Wert:

$$\lim_{x \to x_0} f(x) = L \neq f(x_0) \quad \text{oder} \quad f(x_0) \text{ nicht definiert}$$

**Beispiel:** $f(x) = \frac{x^2 - 1}{x - 1}$ bei $x = 1$

Der Grenzwert ist $\lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = 2$, aber $f(1)$ ist nicht definiert.

**Behebung:** Definiere $f(1) := 2$, dann ist die Funktion stetig.

### 3. Polstelle (Unstetigkeitsstelle 2. Art)

Mindestens ein einseitiger Grenzwert ist $\pm\infty$:

$$\lim_{x \to x_0^+} f(x) = \pm\infty \quad \text{oder} \quad \lim_{x \to x_0^-} f(x) = \pm\infty$$

**Beispiel:** $f(x) = \frac{1}{x}$ bei $x = 0$

### 4. Wesentliche Unstetigkeitsstelle

Weder beidseitiger noch einseitige Grenzwerte existieren (auch nicht als $\pm\infty$).

**Beispiel:** $f(x) = \sin\left(\frac{1}{x}\right)$ bei $x = 0$

## Der Zwischenwertsatz

> Sei $f$ stetig auf $[a, b]$ und $y$ ein Wert zwischen $f(a)$ und $f(b)$. Dann existiert mindestens ein $c \in (a, b)$ mit $f(c) = y$.

**Anschaulich:** Eine stetige Funktion nimmt auf einem Intervall jeden Wert zwischen den Randwerten an.

### Anwendung: Nullstellennachweis

Ist $f$ stetig auf $[a, b]$ mit $f(a) \cdot f(b) < 0$ (verschiedene Vorzeichen), dann hat $f$ mindestens eine Nullstelle in $(a, b)$.

**Beispiel:** $f(x) = x^3 - x - 1$ auf $[1, 2]$
- $f(1) = 1 - 1 - 1 = -1 < 0$
- $f(2) = 8 - 2 - 1 = 5 > 0$

Also hat $f$ eine Nullstelle in $(1, 2)$.

## Untersuchung auf Stetigkeit

### Methode bei stückweise definierten Funktionen

Gegeben sei:
$$f(x) = \begin{cases} g(x) & x < x_0 \\ h(x) & x \geq x_0 \end{cases}$$

**Prüfschritte:**
1. Ist $f$ in den einzelnen Bereichen stetig? (Meist ja, wenn $g$ und $h$ stetig)
2. Stimmen die einseitigen Grenzwerte an der Nahtstelle überein?
   - $\lim_{x \to x_0^-} g(x) = \lim_{x \to x_0^+} h(x) = h(x_0)$?

**Beispiel:**
$$f(x) = \begin{cases} x^2 & x < 1 \\ 2x - 1 & x \geq 1 \end{cases}$$

- $\lim_{x \to 1^-} x^2 = 1$
- $\lim_{x \to 1^+} (2x - 1) = 1$
- $f(1) = 2 \cdot 1 - 1 = 1$

Alle drei Werte stimmen überein → $f$ ist stetig bei $x = 1$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grenzwerte-von-Funktionen]] – Stetigkeit basiert auf dem Grenzwertbegriff
- → [[Konvergenz]] – Grundlage für die Grenzwertdefinition
- → [[Definition-der-Ableitung]] – Differenzierbarkeit impliziert Stetigkeit
- → [[Extremstellen]] – Extremwertsatz erfordert Stetigkeit
- → [[Gebrochenrationale-Funktionen]] – Unstetigkeitsstellen bei Polstellen

> [!warning] **Prüfungsrelevant**
> - Stetigkeitsuntersuchung an Nahtstellen stückweiser Funktionen ist Standard
> - Unterscheidung der Unstetigkeitstypen (Sprung, hebbar, Pol) wird oft gefragt
> - Der Zwischenwertsatz zum Nullstellennachweis ist ein wichtiges Werkzeug
> - "Differenzierbar ⇒ stetig" (aber nicht umgekehrt!) ist ein wichtiger Zusammenhang
> - Stetige Fortsetzung bei hebbaren Unstetigkeitsstellen

> [!question] **Typische Prüfungsfragen**
> - Untersuche die Funktion $f(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & x \neq 2 \\ 5 & x = 2 \end{cases}$ auf Stetigkeit bei $x = 2$.
> - Zeige mit dem Zwischenwertsatz, dass $e^x = 3x$ eine Lösung im Intervall $[0, 2]$ hat.
> - Bestimme den Parameter $a$ so, dass $f(x) = \begin{cases} ax + 1 & x \leq 2 \\ x^2 & x > 2 \end{cases}$ stetig ist.

## Quellen

- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.

> [!tip] **Weiterführende Links**
> - [[Differentialquotient]] – Übergang zur Differenzierbarkeit
> - [[Monotonie]] – Zusammenhang mit Stetigkeit und Umkehrbarkeit
