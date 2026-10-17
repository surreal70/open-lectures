---
author: Andreas Hümmer
title: Polynomfunktionen
tags:
  - content
  - mathe
  - funktionen
  - polynome
  - ganzrationale-funktionen
created: 2025-06-19
modified: 2025-06-19
---

# Polynomfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Polynomfunktionen anhand ihrer Struktur erkennen und klassifizieren können
> - Das Verhalten von Polynomen für $x \to \pm\infty$ analysieren können
> - Nullstellen mit verschiedenen Verfahren bestimmen (Polynomdivision, Substitution, Faktorisierung)
> - Graphen von Polynomfunktionen skizzieren und qualitativ beschreiben können

---

## Überblick

Polynomfunktionen, auch **ganzrationale Funktionen** genannt, sind eine fundamentale Funktionsklasse der Analysis. Sie entstehen durch Addition von Potenzfunktionen mit natürlichen Exponenten und konstanten Koeffizienten. Lineare und quadratische Funktionen sind Spezialfälle. Polynomfunktionen sind auf ganz $\mathbb{R}$ definiert, stetig und beliebig oft differenzierbar, was sie zu idealen Objekten für die Analysis macht.

## Definition und Terminologie

### Allgemeine Form

Eine **Polynomfunktion n-ten Grades** hat die Form:

$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 = \sum_{k=0}^{n} a_k x^k$$

mit $a_n \neq 0$ (Leitkoeffizient) und $n \in \mathbb{N}_0$ (Grad des Polynoms).

### Terminologie

| Begriff | Bedeutung |
|---------|-----------|
| **Grad** $\deg(p)$ | Höchster vorkommender Exponent ($n$) |
| **Leitkoeffizient** | Koeffizient $a_n$ des Terms höchsten Grades |
| **Konstanter Term** | $a_0 = p(0)$ |
| **Monisch** | Polynom mit $a_n = 1$ |

### Beispiele nach Grad

- Grad 0: $p(x) = c$ (Konstante)
- Grad 1: $p(x) = ax + b$ (linear)
- Grad 2: $p(x) = ax^2 + bx + c$ (quadratisch)
- Grad 3: $p(x) = ax^3 + bx^2 + cx + d$ (kubisch)
- Grad 4: $p(x) = ax^4 + \ldots$ (quartisch)

## Eigenschaften

### Definitionsbereich und Wertebereich

- **Definitionsbereich**: $D_p = \mathbb{R}$
- **Wertebereich**: 
  - Grad ungerade: $W_p = \mathbb{R}$
  - Grad gerade: abhängig vom Vorzeichen von $a_n$

### Globalverhalten (Verhalten für $|x| \to \infty$)

Das Verhalten für große $|x|$ wird vom Term höchsten Grades dominiert:

| Grad | $a_n > 0$ | $a_n < 0$ |
|------|-----------|-----------|
| **gerade** | $\lim_{x \to \pm\infty} p(x) = +\infty$ | $\lim_{x \to \pm\infty} p(x) = -\infty$ |
| **ungerade** | $\lim_{x \to -\infty} p(x) = -\infty$, $\lim_{x \to +\infty} p(x) = +\infty$ | $\lim_{x \to -\infty} p(x) = +\infty$, $\lim_{x \to +\infty} p(x) = -\infty$ |

**Merkregel:** Bei ungeradem Grad verlaufen die Äste in entgegengesetzte Richtungen.

### Symmetrie

- **Achsensymmetrie** (zur y-Achse): wenn nur gerade Exponenten auftreten
  - $p(-x) = p(x)$ für alle $x$
  - Beispiel: $p(x) = x^4 - 3x^2 + 2$
  
- **Punktsymmetrie** (zum Ursprung): wenn nur ungerade Exponenten auftreten
  - $p(-x) = -p(x)$ für alle $x$
  - Beispiel: $p(x) = x^3 - 2x$

## Nullstellen

### Fundamentalsatz der Algebra

Ein Polynom $n$-ten Grades hat (über $\mathbb{C}$) genau $n$ Nullstellen, mit Vielfachheit gezählt. Über $\mathbb{R}$ hat es höchstens $n$ Nullstellen.

### Linearfaktorzerlegung

Jedes Polynom kann in Linearfaktoren zerlegt werden:

$$p(x) = a_n (x - x_1)^{k_1} (x - x_2)^{k_2} \cdots (x - x_r)^{k_r}$$

wobei $k_1 + k_2 + \ldots + k_r = n$ (Summe der Vielfachheiten).

### Vielfachheit von Nullstellen

Die **Vielfachheit** (Ordnung) einer Nullstelle beeinflusst das Verhalten des Graphen:

| Vielfachheit | Graphverhalten |
|--------------|----------------|
| Einfach (1) | Graph durchquert die x-Achse |
| Doppelt (2) | Graph berührt die x-Achse (Tangente horizontal) |
| Dreifach (3) | Graph durchquert mit Wendepunkt |
| Gerade | Berührung |
| Ungerade | Durchquerung |

### Methoden zur Nullstellenbestimmung

#### 1. Ausklammern

$$p(x) = x^3 - 4x = x(x^2 - 4) = x(x-2)(x+2)$$

Nullstellen: $x_1 = 0$, $x_2 = 2$, $x_3 = -2$

#### 2. Substitution (biquadratische Gleichungen)

Für $p(x) = ax^4 + bx^2 + c$ setze $z = x^2$:

$$az^2 + bz + c = 0$$

**Beispiel:** $x^4 - 5x^2 + 4 = 0$

Mit $z = x^2$: $z^2 - 5z + 4 = 0$ → $z_1 = 4$, $z_2 = 1$

Rücksubstitution: $x^2 = 4 \Rightarrow x = \pm 2$ und $x^2 = 1 \Rightarrow x = \pm 1$

#### 3. Polynomdivision

Ist $x_0$ eine Nullstelle von $p(x)$, so gilt:

$$p(x) = (x - x_0) \cdot q(x)$$

wobei $q(x)$ ein Polynom vom Grad $n-1$ ist.

**Beispiel:** $p(x) = x^3 - 6x^2 + 11x - 6$ hat Nullstelle $x_0 = 1$

Polynomdivision $(x^3 - 6x^2 + 11x - 6) : (x-1) = x^2 - 5x + 6$

Weiter: $x^2 - 5x + 6 = (x-2)(x-3)$

Also: $p(x) = (x-1)(x-2)(x-3)$, Nullstellen: $1, 2, 3$

#### 4. Rationale Nullstellen (Satz über rationale Nullstellen)

Für ein Polynom mit ganzzahligen Koeffizienten: Jede rationale Nullstelle $\frac{p}{q}$ erfüllt:
- $p$ teilt $a_0$
- $q$ teilt $a_n$

## Horner-Schema

Das **Horner-Schema** ermöglicht effiziente Auswertung und Division:

Für $p(x) = a_n x^n + \ldots + a_1 x + a_0$ und Stelle $x_0$:

```
     a_n    a_{n-1}    a_{n-2}   ...   a_1    a_0
        ×x_0↘    ×x_0↘     ×x_0↘      ×x_0↘
     ─────────────────────────────────────────────
     a_n    b_{n-1}    b_{n-2}   ...   b_1    p(x_0)
```

**Beispiel:** $p(x) = 2x^3 - 3x^2 + x - 5$ bei $x_0 = 2$

```
     2     -3      1     -5
           4       2      6
     ──────────────────────
     2      1      3      1
```

Also: $p(2) = 1$ und $p(x) = (x-2)(2x^2 + x + 3) + 1$

## Graphen von Polynomfunktionen

### Skizzierstrategie

1. **Globalverhalten** bestimmen (Grad und Vorzeichen von $a_n$)
2. **Symmetrie** prüfen (nur gerade oder nur ungerade Exponenten?)
3. **Nullstellen** berechnen und Vielfachheiten bestimmen
4. **y-Achsenabschnitt** $p(0) = a_0$ einzeichnen
5. **Extrempunkte** und **Wendepunkte** bestimmen (mit Ableitungen)
6. **Kurve** durch bekannte Punkte mit richtigem Verhalten zeichnen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Lineare-Funktionen]] — Polynome ersten Grades
- → [[Quadratische-Funktionen]] — Polynome zweiten Grades
- → [[Polynomdivision]] — Algebraisches Werkzeug
- → [[Faktorisierung-von-Polynomen]] — Zerlegung in Faktoren
- → [[Gleichungen-hoeheren-Grades]] — Lösung polynomialer Gleichungen
- → [[Gebrochenrationale-Funktionen]] — Quotient zweier Polynome

> [!warning] **Prüfungsrelevant**
> - Analyse des Globalverhaltens anhand von Grad und Leitkoeffizient
> - Polynomdivision zur Reduktion des Grades nach Erraten einer Nullstelle
> - Zusammenhang zwischen Vielfachheit der Nullstelle und Graphverhalten
> - Substitution bei biquadratischen Gleichungen
> - Systematisches Vorgehen beim Skizzieren von Polynomgraphen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle Nullstellen von $p(x) = x^4 - 5x^3 + 5x^2 + 5x - 6$.
> - Skizzieren Sie den Graphen von $f(x) = -x^3 + 3x$ und begründen Sie das Globalverhalten.
> - Für welche Werte von $a$ hat $p(x) = x^3 + ax^2 - 4x - 4a$ die Nullstelle $x = 2$?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- Arens, T. et al.: *Mathematik*, Springer Spektrum, 2018

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] — Kurvendiskussion mit Ableitungen
> - [[04-Folgen-Reihen-und-Grenzwerte|Grenzwerte]] — Asymptotisches Verhalten

