---
author: Andreas Hümmer
title: Parameterabhängige Funktionen
tags:
  - content
  - mathe
  - funktionen
  - parameter
  - funktionenscharen
created: 2025-01-22
modified: 2025-01-22
---

# Parameterabhängige Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Funktionenscharen und ihre Parameter verstehen können
> - Den Einfluss von Parametern auf Funktionseigenschaften analysieren können
> - Ortskurven bestimmen können
> - Parameter aus gegebenen Bedingungen berechnen können

---

## Überblick

**Parameterabhängige Funktionen** (oder Funktionenscharen) sind Familien von Funktionen, die durch einen oder mehrere Parameter beschrieben werden. Die Untersuchung solcher Funktionen verbindet Funktionsanalyse mit Gleichungslösen und ist ein zentrales Thema in Abiturprüfungen.

## Grundbegriffe

### Definition einer Funktionenschar

Eine **Funktionenschar** ist eine Familie von Funktionen, die durch einen oder mehrere Parameter beschrieben wird:

$$f_a(x) = \text{Ausdruck mit } x \text{ und Parameter } a$$

Für jeden konkreten Wert von $a$ erhält man eine bestimmte Funktion der Schar.

### Notation

- $f_a(x)$ oder $f(x; a)$: Funktion mit Parameter $a$
- Der Parameter wird oft mit $a$, $k$, $t$ oder $c$ bezeichnet
- Griechische Buchstaben wie $\lambda$, $\mu$ sind ebenfalls üblich

### Beispiele

1. **Lineare Funktionen:** $f_a(x) = ax + 1$ (Schar von Geraden durch $(0, 1)$)

2. **Quadratische Funktionen:** $f_a(x) = x^2 - ax$ (Schar von Parabeln)

3. **Exponentialfunktionen:** $f_k(x) = e^{kx}$ (Schar mit verschiedenen Wachstumsraten)

## Analyse parameterabhängiger Funktionen

### Nullstellen in Abhängigkeit vom Parameter

**Beispiel:** $f_a(x) = x^2 - ax + 1$

Nullstellen: $x^2 - ax + 1 = 0$

Mit der Mitternachtsformel:
$$x_{1,2} = \frac{a \pm \sqrt{a^2 - 4}}{2}$$

- Für $|a| < 2$: keine reellen Nullstellen
- Für $|a| = 2$: eine doppelte Nullstelle
- Für $|a| > 2$: zwei verschiedene Nullstellen

### Extrema in Abhängigkeit vom Parameter

**Beispiel:** $f_a(x) = x^3 - 3ax$, wobei $a > 0$

**Ableitung:** $f_a'(x) = 3x^2 - 3a = 3(x^2 - a)$

**Nullstellen der Ableitung:** $x^2 = a \Rightarrow x = \pm\sqrt{a}$

**Extremwerte:**
- Maximum bei $x = -\sqrt{a}$: $f_a(-\sqrt{a}) = -a\sqrt{a} + 3a\sqrt{a} = 2a\sqrt{a}$
- Minimum bei $x = \sqrt{a}$: $f_a(\sqrt{a}) = a\sqrt{a} - 3a\sqrt{a} = -2a\sqrt{a}$

Die Extrema hängen von $a$ ab: Je größer $a$, desto weiter außen liegen sie und desto größer sind die Beträge der Extremwerte.

### Symmetrie in Abhängigkeit vom Parameter

**Beispiel:** $f_a(x) = x^4 + ax^2 + 1$

Prüfung auf Symmetrie:
$$f_a(-x) = (-x)^4 + a(-x)^2 + 1 = x^4 + ax^2 + 1 = f_a(x)$$

Die Funktionenschar ist für **alle** Werte von $a$ achsensymmetrisch zur $y$-Achse.

## Ortskurven

### Definition

Eine **Ortskurve** ist die Menge aller Punkte, die eine bestimmte Eigenschaft (z.B. Extremum, Wendepunkt) für alle Funktionen der Schar haben.

### Bestimmung der Ortskurve

1. Bestimme die $x$-Koordinate der betrachteten Punkte in Abhängigkeit von $a$
2. Berechne die zugehörige $y$-Koordinate
3. Eliminiere den Parameter $a$, um $y = y(x)$ zu erhalten

### Beispiel: Ortskurve der Extrema

Für $f_a(x) = x^3 - 3ax$ mit $a > 0$:

**Schritt 1-2:** Extrema bei $x = \pm\sqrt{a}$

Für $x = \sqrt{a}$: $y = -2a\sqrt{a} = -2a^{3/2}$

**Schritt 3:** Eliminiere $a$

Aus $x = \sqrt{a}$ folgt $a = x^2$

Einsetzen: $y = -2(x^2)^{3/2} = -2x^3$ (für $x > 0$)

Die Ortskurve der Minima ist $y = -2x^3$ für $x > 0$.

Analog für Maxima ($x = -\sqrt{a}$): $y = 2(-x)^3 = 2|x|^3$ für $x < 0$

Zusammen: Die Ortskurve beider Extrema ist $y = -2x^3$.

## Parameterbestimmung aus Bedingungen

### Typische Aufgabenstellungen

1. **Punkt auf dem Graphen:** „Für welches $a$ geht der Graph durch $P(2, 5)$?"
2. **Bestimmte Nullstelle:** „Für welches $a$ hat $f_a$ die Nullstelle $x = 3$?"
3. **Extremum an bestimmter Stelle:** „Für welches $a$ liegt das Maximum bei $x = 1$?"
4. **Tangentenbedingung:** „Für welches $a$ hat $f_a$ an der Stelle $x = 2$ die Steigung 4?"

### Beispiel: Punkt auf dem Graphen

$f_a(x) = x^2 + ax - 3$ soll durch $P(1, 2)$ gehen.

**Bedingung:** $f_a(1) = 2$

$$1 + a - 3 = 2$$
$$a = 4$$

### Beispiel: Tangentenbedingung

$f_a(x) = ax^2 + x$ soll an der Stelle $x = 2$ eine waagerechte Tangente haben.

**Bedingung:** $f_a'(2) = 0$

$f_a'(x) = 2ax + 1$

$$f_a'(2) = 4a + 1 = 0$$
$$a = -\frac{1}{4}$$

### Beispiel: Berührung zweier Kurven

Wann berührt die Parabel $f_a(x) = x^2 + a$ die Gerade $g(x) = 4x - 4$?

**Bedingungen:**
1. Gleicher Funktionswert: $x^2 + a = 4x - 4$
2. Gleiche Steigung: $2x = 4$

Aus (2): $x = 2$

Einsetzen in (1): $4 + a = 8 - 4 \Rightarrow a = 0$

Die Parabel $f_0(x) = x^2$ berührt die Gerade bei $x = 2$.

## Gemeinsame Punkte einer Funktionenschar

### Definition

Ein Punkt heißt **gemeinsamer Punkt** einer Funktionenschar, wenn er auf den Graphen aller Funktionen der Schar liegt.

### Bestimmung

Setze $f_a(x)$ für zwei verschiedene Parameter $a_1 \neq a_2$ gleich und löse.

### Beispiel

$f_a(x) = ax^2 + x + 1$

Gemeinsame Punkte: $f_{a_1}(x) = f_{a_2}(x)$ für $a_1 \neq a_2$

$$a_1 x^2 + x + 1 = a_2 x^2 + x + 1$$
$$(a_1 - a_2)x^2 = 0$$

Da $a_1 \neq a_2$, folgt $x = 0$.

Der gemeinsame Punkt ist $(0, f_a(0)) = (0, 1)$.

## Anwendungen

### Wachstumsprozesse

Die Schar $f_k(t) = A_0 \cdot e^{kt}$ beschreibt exponentielles Wachstum mit:
- $A_0$: Anfangswert
- $k > 0$: Wachstumsrate
- $k < 0$: Zerfallsrate

### Optimierung mit Nebenbedingungen

Ein Rechteck soll den Umfang $U$ haben. Welche Seitenlängen maximieren die Fläche?

Mit $a + b = \frac{U}{2}$ und $a$ als Parameter:
$$A(a) = a \cdot \left(\frac{U}{2} - a\right) = \frac{U}{2}a - a^2$$

Maximum bei $a = \frac{U}{4}$, also ein Quadrat.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Transformationen]] – Parameter als Transformationsgrößen
- → [[Nullstellen]] – Parameterabhängige Nullstellen
- → [[Monotonie]] – Einfluss von Parametern auf das Monotonieverhalten
- → [[Gleichungssysteme]] – Lösen von Parametergleichungen

> [!warning] **Prüfungsrelevant**
> - Systematische Untersuchung von Funktionenscharen
> - Bestimmung von Ortskurven (besonders für Extrema und Wendepunkte)
> - Parameterbestimmung aus gegebenen Bedingungen
> - Gemeinsame Punkte einer Funktionenschar

> [!question] **Typische Prüfungsfragen**
> - Für welche Werte von $a$ hat $f_a(x) = x^3 - ax$ genau zwei Extremstellen?
> - Bestimme die Ortskurve der Wendepunkte der Schar $f_t(x) = x^3 - 3tx^2$.
> - Die Gerade $g(x) = mx + 2$ soll die Parabel $f(x) = x^2$ in genau einem Punkt berühren. Bestimme $m$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] – Kurvendiskussion
> - [[06-Differentialrechnung-II|Differentialrechnung II]] – Extremwertaufgaben
> - [[Anwendungen-algebraischer-Methoden]] – Praktische Optimierung
