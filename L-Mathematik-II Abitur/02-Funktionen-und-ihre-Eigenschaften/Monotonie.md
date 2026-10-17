---
author: Andreas Hümmer
title: Monotonie
tags:
  - content
  - mathe
  - funktionen
  - monotonie
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Monotonie

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Arten der Monotonie definieren und unterscheiden können
> - Monotoniebereiche einer Funktion bestimmen können
> - Den Zusammenhang zwischen Monotonie und Ableitung verstehen
> - Monotonie zur Untersuchung von Funktionseigenschaften nutzen können

---

## Überblick

Die **Monotonie** beschreibt das Wachstumsverhalten einer Funktion. Eine Funktion kann auf einem Intervall steigen, fallen oder konstant sein. Die Untersuchung der Monotonie ist ein wesentlicher Bestandteil der Kurvendiskussion und liefert wichtige Informationen über den Funktionsverlauf.

## Definitionen

### Monoton wachsend

Eine Funktion $f$ heißt auf einem Intervall $I$ **monoton wachsend** (oder monoton steigend), wenn für alle $x_1, x_2 \in I$ gilt:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) \leq f(x_2)$$

### Streng monoton wachsend

Eine Funktion $f$ heißt auf $I$ **streng monoton wachsend**, wenn für alle $x_1, x_2 \in I$ gilt:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) < f(x_2)$$

### Monoton fallend

Eine Funktion $f$ heißt auf $I$ **monoton fallend**, wenn für alle $x_1, x_2 \in I$ gilt:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) \geq f(x_2)$$

### Streng monoton fallend

Eine Funktion $f$ heißt auf $I$ **streng monoton fallend**, wenn für alle $x_1, x_2 \in I$ gilt:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) > f(x_2)$$

## Zusammenhang mit der Ableitung

### Monotoniekriterium

Für eine auf dem Intervall $I$ differenzierbare Funktion $f$ gilt:

| Ableitung | Monotonie |
|-----------|-----------|
| $f'(x) > 0$ für alle $x \in I$ | streng monoton wachsend |
| $f'(x) \geq 0$ für alle $x \in I$ | monoton wachsend |
| $f'(x) < 0$ für alle $x \in I$ | streng monoton fallend |
| $f'(x) \leq 0$ für alle $x \in I$ | monoton fallend |

### Beweis der Hinrichtung (Idee)

Wenn $f'(x) > 0$ auf $I$, dann ist die Funktion wachsend:

Für $x_1 < x_2$ gilt nach dem Mittelwertsatz:
$$\frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(\xi) > 0 \quad \text{für ein } \xi \in (x_1, x_2)$$

Da $x_2 - x_1 > 0$, folgt $f(x_2) - f(x_1) > 0$, also $f(x_2) > f(x_1)$.

## Bestimmung der Monotoniebereiche

### Algorithmus

1. **Ableitung bilden:** $f'(x)$ berechnen
2. **Nullstellen finden:** $f'(x) = 0$ lösen
3. **Vorzeichen untersuchen:** In jedem Intervall zwischen den Nullstellen das Vorzeichen von $f'(x)$ bestimmen
4. **Monotonieaussage:** Vorzeichen in Monotonieverhalten übersetzen

### Beispiel 1: Polynomfunktion

$$f(x) = x^3 - 3x^2 + 2$$

**Schritt 1:** Ableitung
$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

**Schritt 2:** Nullstellen der Ableitung
$$f'(x) = 0 \Leftrightarrow x = 0 \text{ oder } x = 2$$

**Schritt 3:** Vorzeichentabelle

| Intervall | Testpunkt | $3x$ | $x-2$ | $f'(x)$ |
|-----------|-----------|------|-------|---------|
| $(-\infty, 0)$ | $x = -1$ | $-$ | $-$ | $+$ |
| $(0, 2)$ | $x = 1$ | $+$ | $-$ | $-$ |
| $(2, \infty)$ | $x = 3$ | $+$ | $+$ | $+$ |

**Schritt 4:** Monotonieverhalten
- $f$ ist streng monoton wachsend auf $(-\infty, 0]$
- $f$ ist streng monoton fallend auf $[0, 2]$
- $f$ ist streng monoton wachsend auf $[2, \infty)$

### Beispiel 2: Rationale Funktion

$$f(x) = \frac{x}{x^2 + 1}$$

**Ableitung mit Quotientenregel:**
$$f'(x) = \frac{1 \cdot (x^2+1) - x \cdot 2x}{(x^2+1)^2} = \frac{x^2 + 1 - 2x^2}{(x^2+1)^2} = \frac{1-x^2}{(x^2+1)^2}$$

**Nullstellen:** $1 - x^2 = 0 \Leftrightarrow x = \pm 1$

**Vorzeichen:** Der Nenner $(x^2+1)^2$ ist stets positiv.

- Für $x \in (-1, 1)$: $1 - x^2 > 0$, also $f'(x) > 0$
- Für $|x| > 1$: $1 - x^2 < 0$, also $f'(x) < 0$

**Monotonie:**
- Streng monoton fallend auf $(-\infty, -1]$
- Streng monoton wachsend auf $[-1, 1]$
- Streng monoton fallend auf $[1, \infty)$

## Monotonie und andere Eigenschaften

### Monotonie und Injektivität

Eine **streng monotone** Funktion ist auf ihrem gesamten Definitionsbereich **injektiv** (eineindeutig).

**Beweis:** Wenn $f$ streng monoton wachsend ist und $x_1 \neq x_2$, dann ist:
- Für $x_1 < x_2$: $f(x_1) < f(x_2)$
- Für $x_1 > x_2$: $f(x_1) > f(x_2)$

In beiden Fällen ist $f(x_1) \neq f(x_2)$.

### Monotonie und Umkehrbarkeit

Eine streng monotone Funktion besitzt eine **Umkehrfunktion**. Diese hat dieselbe Monotonieart:
- $f$ streng monoton wachsend $\Rightarrow$ $f^{-1}$ streng monoton wachsend
- $f$ streng monoton fallend $\Rightarrow$ $f^{-1}$ streng monoton fallend

### Monotonie und Extrema

An Stellen, wo die Monotonie wechselt, liegen **lokale Extrema**:
- Wechsel von steigend zu fallend: lokales Maximum
- Wechsel von fallend zu steigend: lokales Minimum

## Wichtige Beispiele

| Funktion | Monotonieverhalten |
|----------|-------------------|
| $f(x) = x$ | streng mon. wachsend auf $\mathbb{R}$ |
| $f(x) = x^2$ | streng mon. fallend auf $(-\infty, 0]$, streng mon. wachsend auf $[0, \infty)$ |
| $f(x) = x^3$ | streng mon. wachsend auf $\mathbb{R}$ |
| $f(x) = e^x$ | streng mon. wachsend auf $\mathbb{R}$ |
| $f(x) = \ln(x)$ | streng mon. wachsend auf $(0, \infty)$ |
| $f(x) = \frac{1}{x}$ | streng mon. fallend auf $(-\infty, 0)$ und $(0, \infty)$ |

**Achtung:** $f(x) = \frac{1}{x}$ ist **nicht** monoton auf $\mathbb{R} \setminus \{0\}$, da der Definitionsbereich nicht zusammenhängend ist!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Umkehrfunktionen]] – Streng monotone Funktionen sind umkehrbar
- → [[Wiederholung-des-Funktionsbegriffs]] – Injektivität als Grundeigenschaft
- → [[05-Differentialrechnung-I|Differentialrechnung]] – Ableitung als Werkzeug zur Monotoniebestimmung
- → [[Symmetrie]] – Zusammenspiel von Symmetrie und Monotonie

> [!warning] **Prüfungsrelevant**
> - Formale Definitionen der vier Monotoniearten
> - Zusammenhang zwischen Vorzeichen der Ableitung und Monotonie
> - Systematische Bestimmung von Monotoniebereichen
> - Schlussfolgerungen: Monotonie → Injektivität → Umkehrbarkeit

> [!question] **Typische Prüfungsfragen**
> - Bestimme die Monotoniebereiche von $f(x) = x \cdot e^{-x}$.
> - Zeige, dass $f(x) = x + \sin(x)$ auf ganz $\mathbb{R}$ streng monoton wachsend ist.
> - Warum ist $f(x) = x^3 - 3x$ auf $\mathbb{R}$ nicht monoton? Gib die Monotoniebereiche an.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[06-Differentialrechnung-II|Differentialrechnung II]] – Extremwertbestimmung mit Ableitungen
> - [[Exponentialfunktionen]] – Monotonie der $e$-Funktion
> - [[Logarithmusfunktionen]] – Monotonie des Logarithmus
