---
author: Andreas Hümmer
title: Gebrochenrationale Funktionen
tags:
  - content
  - mathe
  - funktionen
  - gebrochenrationale-funktion
  - asymptoten
created: 2025-06-19
modified: 2025-06-19
---

# Gebrochenrationale Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Definitionsbereich gebrochenrationaler Funktionen bestimmen können
> - Polstellen und hebbare Definitionslücken unterscheiden können
> - Horizontale, vertikale und schiefe Asymptoten berechnen können
> - Graphen gebrochenrationaler Funktionen analysieren und skizzieren können

---

## Überblick

Gebrochenrationale Funktionen sind Quotienten zweier Polynomfunktionen. Im Gegensatz zu ganzrationalen Funktionen haben sie einen eingeschränkten Definitionsbereich und können Asymptoten aufweisen — Geraden, denen sich der Graph für große $|x|$ oder in der Nähe von Definitionslücken beliebig nähert. Diese Funktionen modellieren viele physikalische Zusammenhänge wie elektrische Widerstände in Parallelschaltung oder Mischungsprobleme.

## Definition

Eine **gebrochenrationale Funktion** hat die Form:

$$f(x) = \frac{p(x)}{q(x)} = \frac{a_m x^m + a_{m-1} x^{m-1} + \ldots + a_0}{b_n x^n + b_{n-1} x^{n-1} + \ldots + b_0}$$

mit Polynomen $p(x)$ (Zählerpolynom, Grad $m$) und $q(x)$ (Nennerpolynom, Grad $n$), wobei $q(x)$ kein Nullpolynom ist.

### Klassifikation

| Bezeichnung | Bedingung | Beispiel |
|-------------|-----------|----------|
| **Echt gebrochenrational** | $m < n$ | $\frac{x+1}{x^2-1}$ |
| **Unecht gebrochenrational** | $m \geq n$ | $\frac{x^2+1}{x-1}$ |

## Definitionsbereich

Der Definitionsbereich umfasst alle $x \in \mathbb{R}$, für die der Nenner nicht null wird:

$$D_f = \mathbb{R} \setminus \{x \mid q(x) = 0\}$$

**Beispiel:**
$$f(x) = \frac{x+2}{x^2-4} = \frac{x+2}{(x-2)(x+2)}$$

Nenner-Nullstellen: $x = 2$ und $x = -2$
Definitionsbereich: $D_f = \mathbb{R} \setminus \{-2, 2\}$

## Definitionslücken

### Polstellen

Eine **Polstelle** liegt vor, wenn der Nenner eine Nullstelle hat, die nicht durch den Zähler gekürzt werden kann.

$$f(x) = \frac{1}{x-2}$$

Bei $x = 2$ liegt eine Polstelle vor: $\lim_{x \to 2^+} f(x) = +\infty$ und $\lim_{x \to 2^-} f(x) = -\infty$

**Vorzeichenwechsel:**
- Polstelle mit Vorzeichenwechsel (ungerade Vielfachheit im Nenner)
- Polstelle ohne Vorzeichenwechsel (gerade Vielfachheit im Nenner)

### Hebbare Definitionslücken

Eine **hebbare Definitionslücke** liegt vor, wenn Zähler und Nenner eine gemeinsame Nullstelle haben, die sich kürzen lässt.

$$f(x) = \frac{x^2-4}{x-2} = \frac{(x-2)(x+2)}{x-2} = x+2 \quad \text{für } x \neq 2$$

Die Funktion lässt sich zu $\tilde{f}(x) = x + 2$ stetig fortsetzen.

**Erkennungsmerkmal:** $\lim_{x \to x_0} f(x)$ existiert und ist endlich.

## Asymptoten

### Vertikale Asymptoten (Polgeraden)

An jeder Polstelle $x_0$ verläuft der Graph asymptotisch zur vertikalen Geraden $x = x_0$.

### Horizontale Asymptoten

Für das Verhalten $x \to \pm\infty$:

| Gradverhältnis | Grenzwert | Horizontale Asymptote |
|----------------|-----------|----------------------|
| $m < n$ | $\lim_{x \to \pm\infty} f(x) = 0$ | $y = 0$ (x-Achse) |
| $m = n$ | $\lim_{x \to \pm\infty} f(x) = \frac{a_m}{b_n}$ | $y = \frac{a_m}{b_n}$ |
| $m > n$ | Grenzwert $\pm\infty$ | keine horizontale Asymptote |

**Beispiele:**

1. $f(x) = \frac{2x-1}{3x+5}$: Asymptote $y = \frac{2}{3}$

2. $f(x) = \frac{x}{x^2+1}$: Asymptote $y = 0$

### Schiefe (schräge) Asymptoten

Für $m = n + 1$ existiert eine schiefe Asymptote. Sie ergibt sich durch Polynomdivision:

$$f(x) = \frac{p(x)}{q(x)} = g(x) + \frac{r(x)}{q(x)}$$

wobei $g(x)$ ein lineares Polynom (die schiefe Asymptote) und $\frac{r(x)}{q(x)}$ für $|x| \to \infty$ gegen 0 geht.

**Beispiel:**
$$f(x) = \frac{x^2 + 2x - 1}{x - 1}$$

Polynomdivision:
$$(x^2 + 2x - 1) : (x-1) = x + 3 + \frac{2}{x-1}$$

Schiefe Asymptote: $y = x + 3$

## Wichtige Standardfunktionen

### Hyperbel $f(x) = \frac{1}{x}$

- Definitionsbereich: $D = \mathbb{R} \setminus \{0\}$
- Polstelle: $x = 0$ mit Vorzeichenwechsel
- Horizontale Asymptote: $y = 0$
- Punktsymmetrisch zum Ursprung
- Streng monoton fallend auf $(-\infty, 0)$ und $(0, +\infty)$

### Allgemeine Hyperbel $f(x) = \frac{a}{x-b} + c$

- Vertikale Asymptote: $x = b$
- Horizontale Asymptote: $y = c$
- Symmetriezentrum: $(b|c)$

## Kurvendiskussion

### Systematisches Vorgehen

1. **Definitionsbereich**: Nenner-Nullstellen bestimmen
2. **Art der Definitionslücken**: Kürzen möglich? → hebbar oder Pol?
3. **Symmetrie**: $f(-x) = f(x)$? oder $f(-x) = -f(x)$?
4. **Nullstellen**: Zähler-Nullstellen (die nicht auch Nenner-Nullstellen sind)
5. **Asymptoten**: vertikal, horizontal, schief
6. **Vorzeichen**: Vorzeichentabelle erstellen
7. **Extrempunkte und Wendepunkte**: Mit Ableitungen (falls verlangt)

### Beispiel

$$f(x) = \frac{x^2 - 1}{x^2 - 4} = \frac{(x-1)(x+1)}{(x-2)(x+2)}$$

**Analyse:**
- $D_f = \mathbb{R} \setminus \{-2, 2\}$
- Polstellen bei $x = -2$ und $x = 2$ (beide mit VZW)
- Nullstellen: $x = -1$ und $x = 1$
- Horizontale Asymptote: $y = 1$ (Zähler- und Nennergrad gleich)
- Achsensymmetrisch (nur gerade Potenzen nach Ausmultiplizieren)

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Polynomfunktionen]] — Zähler und Nenner sind Polynome
- → [[Polynomdivision]] — Zur Bestimmung schiefer Asymptoten
- → [[Grenzwerte-von-Funktionen]] — Asymptotisches Verhalten
- → [[Definitionsbereich]] — Einschränkungen des Definitionsbereichs
- → [[Nullstellen]] — Nullstellen des Zählers
- → [[Stetigkeit]] — Hebbare Definitionslücken und stetige Fortsetzung

> [!warning] **Prüfungsrelevant**
> - Unterscheidung zwischen Polstellen und hebbaren Definitionslücken
> - Berechnung horizontaler und schiefer Asymptoten
> - Vorzeichenverhalten an Polstellen (mit/ohne Vorzeichenwechsel)
> - Polynomdivision zur Asymptotenbstimmung
> - Vollständige Kurvendiskussion gebrochenrationaler Funktionen

> [!question] **Typische Prüfungsfragen**
> - Untersuchen Sie die Funktion $f(x) = \frac{x^2-4x+3}{x^2-9}$ auf Definitionslücken und bestimmen Sie deren Art.
> - Bestimmen Sie alle Asymptoten der Funktion $f(x) = \frac{2x^2+x-1}{x+1}$.
> - Skizzieren Sie den Graphen von $f(x) = \frac{x}{x^2-1}$ unter Angabe aller charakteristischen Punkte und Asymptoten.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Abiturprüfungsaufgaben Mathematik*, verschiedene Jahrgänge

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] — Ableitung gebrochenrationaler Funktionen
> - [[Partialbruchzerlegung]] — Wichtig für die Integration

