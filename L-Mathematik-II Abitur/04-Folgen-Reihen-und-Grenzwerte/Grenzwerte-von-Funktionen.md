---
author: Andreas Hümmer
title: Grenzwerte von Funktionen
tags:
  - content
  - mathe
  - funktionen
  - grenzwert
  - limes
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Grenzwerte von Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen Folgengrenzwerten und Funktionsgrenzwerten verstehen
> - Grenzwerte von Funktionen für $x \to x_0$ und $x \to \pm\infty$ berechnen können
> - Einseitige Grenzwerte bestimmen können
> - Unbestimmte Ausdrücke bei Funktionen auflösen können
> - Asymptotisches Verhalten von Funktionen analysieren können

---

## Überblick

Während wir bei Folgen nur diskrete Werte ($n = 1, 2, 3, \ldots$) betrachten, können bei Funktionen die Eingabewerte kontinuierlich variieren. Der **Grenzwert einer Funktion** beschreibt, welchem Wert sich $f(x)$ annähert, wenn $x$ gegen einen bestimmten Wert oder gegen Unendlich strebt. Dieses Konzept ist fundamental für die Definition der Ableitung und der Stetigkeit.

## Grenzwert für $x \to x_0$

### Definition

Der Grenzwert $\lim_{x \to x_0} f(x) = L$ existiert, wenn sich die Funktionswerte $f(x)$ beliebig nahe an $L$ annähern, sobald $x$ hinreichend nahe bei $x_0$ liegt (aber $x \neq x_0$).

**Formale Definition (Epsilon-Delta):**

$$\lim_{x \to x_0} f(x) = L \quad \Leftrightarrow \quad \forall \varepsilon > 0 \; \exists \delta > 0 : 0 < |x - x_0| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

### Wichtig: $x \neq x_0$

Der Grenzwert hängt nur davon ab, wie sich $f$ in der **Nähe** von $x_0$ verhält, nicht vom Wert $f(x_0)$ selbst (der muss nicht einmal existieren).

### Beispiel

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$$

Direkt einsetzen ergibt $\frac{0}{0}$ (unbestimmt). Umformen:

$$\frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x - 2} = x + 2 \quad \text{(für } x \neq 2\text{)}$$

Also: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 2 + 2 = 4$

## Einseitige Grenzwerte

### Rechtsseitiger Grenzwert

$$\lim_{x \to x_0^+} f(x) = L \quad \text{(Annäherung von rechts, } x > x_0\text{)}$$

### Linksseitiger Grenzwert

$$\lim_{x \to x_0^-} f(x) = L \quad \text{(Annäherung von links, } x < x_0\text{)}$$

### Zusammenhang

Der (beidseitige) Grenzwert existiert genau dann, wenn beide einseitigen Grenzwerte existieren und gleich sind:

$$\lim_{x \to x_0} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L$$

### Beispiel: Vorzeichenfunktion

$$\text{sgn}(x) = \begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}$$

- $\lim_{x \to 0^+} \text{sgn}(x) = 1$
- $\lim_{x \to 0^-} \text{sgn}(x) = -1$
- $\lim_{x \to 0} \text{sgn}(x)$ existiert nicht (da $1 \neq -1$)

## Grenzwert für $x \to \pm\infty$

### Definition

$$\lim_{x \to +\infty} f(x) = L \quad \text{und} \quad \lim_{x \to -\infty} f(x) = L$$

bedeutet, dass sich $f(x)$ dem Wert $L$ beliebig annähert, wenn $x$ über alle Grenzen wächst bzw. fällt.

### Rechenregeln (wie bei Folgen)

- Summen-, Differenz-, Produkt-, Quotientenregel gelten analog
- Ausklammern der höchsten Potenz bei rationalen Funktionen

### Beispiel: Rationale Funktion

$$\lim_{x \to \infty} \frac{3x^2 + x - 1}{2x^2 + 5}$$

Ausklammern von $x^2$:

$$= \lim_{x \to \infty} \frac{x^2(3 + \frac{1}{x} - \frac{1}{x^2})}{x^2(2 + \frac{5}{x^2})} = \frac{3 + 0 - 0}{2 + 0} = \frac{3}{2}$$

## Asymptotisches Verhalten

### Horizontale Asymptoten

Eine Funktion $f$ hat eine **horizontale Asymptote** $y = L$, wenn:

$$\lim_{x \to +\infty} f(x) = L \quad \text{oder} \quad \lim_{x \to -\infty} f(x) = L$$

**Beispiel:** $f(x) = \frac{2x + 1}{x - 1}$ hat die horizontale Asymptote $y = 2$

### Vertikale Asymptoten

Eine Funktion $f$ hat eine **vertikale Asymptote** bei $x = x_0$, wenn:

$$\lim_{x \to x_0^+} f(x) = \pm\infty \quad \text{oder} \quad \lim_{x \to x_0^-} f(x) = \pm\infty$$

**Beispiel:** $f(x) = \frac{1}{x}$ hat eine vertikale Asymptote bei $x = 0$

### Schiefe Asymptoten

Wenn $\lim_{x \to \pm\infty} [f(x) - (mx + b)] = 0$, hat $f$ die **schiefe Asymptote** $y = mx + b$.

**Bestimmung bei rationalen Funktionen:** Polynomdivision, wenn Grad(Zähler) = Grad(Nenner) + 1

## Wichtige Standardgrenzwerte

| Grenzwert | Wert |
|-----------|------|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{1 - \cos x}{x}$ | $0$ |
| $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ |
| $\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{\ln(1 + x)}{x}$ | $1$ |
| $\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$ | $e$ |
| $\lim_{x \to 0^+} x \ln x$ | $0$ |

## Unbestimmte Ausdrücke

### Typ $\frac{0}{0}$: Faktorisieren oder Erweitern

**Beispiel:**
$$\lim_{x \to 1} \frac{x^3 - 1}{x - 1} = \lim_{x \to 1} \frac{(x-1)(x^2 + x + 1)}{x - 1} = \lim_{x \to 1} (x^2 + x + 1) = 3$$

### Typ $\frac{\infty}{\infty}$: Höchste Potenz ausklammern

**Beispiel:**
$$\lim_{x \to \infty} \frac{x^3 + 2x}{x^3 - x^2} = \frac{1}{1} = 1$$

### Typ $\infty - \infty$: Gemeinsamen Nenner bilden

**Beispiel:**
$$\lim_{x \to 0} \left(\frac{1}{x} - \frac{1}{\sin x}\right) = \lim_{x \to 0} \frac{\sin x - x}{x \sin x}$$

(Erfordert weitere Techniken wie Taylorentwicklung oder Regel von l'Hospital)

## Zusammenhang mit Folgengrenzwerten

> Der Funktionsgrenzwert $\lim_{x \to x_0} f(x) = L$ existiert genau dann, wenn für **jede** Folge $(x_n)$ mit $x_n \to x_0$ und $x_n \neq x_0$ gilt: $f(x_n) \to L$.

Diese Charakterisierung ist nützlich für Gegenbeispiele: Findet man eine Folge $(x_n) \to x_0$, für die $(f(x_n))$ nicht gegen $L$ konvergiert, existiert der Funktionsgrenzwert nicht.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grenzwerte-von-Folgen]] – Diskrete Grenzwerte als Grundlage
- → [[Konvergenz]] – Konvergenzbegriff bei Folgen
- → [[Stetigkeit]] – Funktionsgrenzwerte und Stetigkeit
- → [[Definition-der-Ableitung]] – Differenzenquotient als Grenzwert
- → [[Gebrochenrationale-Funktionen]] – Asymptoten und Grenzwerte

> [!warning] **Prüfungsrelevant**
> - Grenzwerte an Definitionslücken (Typ $\frac{0}{0}$) berechnen ist Standard
> - Asymptotisches Verhalten für $x \to \pm\infty$ wird bei Kurvendiskussionen gebraucht
> - Einseitige Grenzwerte bei stückweise definierten Funktionen
> - Der Standardgrenzwert $\lim_{x \to 0} \frac{\sin x}{x} = 1$ ist fundamental
> - Unterscheidung: Grenzwert existiert nicht vs. Grenzwert ist $\pm\infty$

> [!question] **Typische Prüfungsfragen**
> - Bestimme $\lim_{x \to 3} \frac{x^2 - 9}{x^2 - 5x + 6}$.
> - Untersuche das Verhalten von $f(x) = \frac{2x^2 - 1}{x^2 + x}$ für $x \to \pm\infty$ und bestimme alle Asymptoten.
> - Berechne die einseitigen Grenzwerte von $f(x) = \frac{|x|}{x}$ für $x \to 0$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.

> [!tip] **Weiterführende Links**
> - [[Differenzenquotient]] – Grenzwertbildung bei der Ableitung
> - [[Vollstaendige-Kurvendiskussion]] – Anwendung der Grenzwertanalyse
