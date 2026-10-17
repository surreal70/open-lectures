---
author: Andreas Hümmer
title: Faktorisierung von Polynomen
tags:
  - content
  - mathe
  - algebra
  - polynome
  - faktorisierung
  - nullstellen
created: 2025-01-13
modified: 2025-01-13
---

# Faktorisierung von Polynomen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Polynome systematisch in Linearfaktoren zerlegen können
> - Den Zusammenhang zwischen Nullstellen und Faktorisierung verstehen
> - Vielfachheiten von Nullstellen erkennen und interpretieren können
> - Den Fundamentalsatz der Algebra kennen

---

## Überblick

Die Faktorisierung eines Polynoms in ein Produkt einfacherer Faktoren ist eine zentrale Technik der Algebra. Sie ermöglicht das Lösen von Polynomgleichungen, die Untersuchung des Verhaltens von Polynomfunktionen und die Vereinfachung von Bruchtermen. Jedes Polynom lässt sich (über den komplexen Zahlen) vollständig in Linearfaktoren zerlegen.

## Zusammenhang zwischen Nullstellen und Faktoren

### Fundamentale Beziehung

Ein Polynom $p(x)$ hat genau dann eine Nullstelle bei $x = x_0$, wenn $(x - x_0)$ ein Faktor von $p(x)$ ist:

$$p(x_0) = 0 \quad \Leftrightarrow \quad p(x) = (x - x_0) \cdot q(x)$$

wobei $q(x)$ ein Polynom vom Grad $n-1$ ist, wenn $p(x)$ den Grad $n$ hat.

### Fundamentalsatz der Algebra

> Jedes Polynom $n$-ten Grades mit komplexen Koeffizienten hat genau $n$ Nullstellen in $\mathbb{C}$ (mit Vielfachheiten gezählt).

**Konsequenz für reelle Polynome:**
- Ein Polynom $n$-ten Grades hat **höchstens** $n$ reelle Nullstellen
- Komplexe Nullstellen treten bei reellen Polynomen immer als **konjugierte Paare** auf

## Vielfachheit von Nullstellen

### Definition

Eine Nullstelle $x_0$ hat die **Vielfachheit** (oder Ordnung) $k$, wenn gilt:

$$p(x) = (x - x_0)^k \cdot q(x) \quad \text{mit } q(x_0) \neq 0$$

| Vielfachheit | Bezeichnung | Verhalten am Graphen |
|--------------|-------------|---------------------|
| $k = 1$ | einfache Nullstelle | Graph schneidet x-Achse |
| $k = 2$ | doppelte Nullstelle | Graph berührt x-Achse |
| $k = 3$ | dreifache Nullstelle | Graph schneidet mit Wendepunkt |
| $k$ gerade | - | Graph berührt x-Achse |
| $k$ ungerade | - | Graph schneidet x-Achse |

**Beispiel:** $p(x) = (x - 1)^2(x + 2)$

- $x = 1$ ist doppelte Nullstelle (Berührpunkt)
- $x = -2$ ist einfache Nullstelle (Schnittpunkt)

## Methoden zur Faktorisierung

### Methode 1: Ausklammern

Gemeinsame Faktoren identifizieren:

$$2x^3 + 6x^2 = 2x^2(x + 3)$$

$$x^4 - x^3 + x^2 - x = x(x^3 - x^2 + x - 1) = x(x - 1)(x^2 + 1)$$

### Methode 2: Binomische Formeln

**Dritte binomische Formel:**
$$x^2 - 9 = (x + 3)(x - 3)$$

**Erste/Zweite binomische Formel:**
$$x^2 + 6x + 9 = (x + 3)^2$$

### Methode 3: Quadratische Ergänzung

Für $p(x) = x^2 + px + q$:

$$x^2 + px + q = \left(x + \frac{p}{2}\right)^2 - \frac{p^2}{4} + q$$

**Beispiel:**
$$x^2 + 4x + 3 = (x + 2)^2 - 4 + 3 = (x + 2)^2 - 1 = (x + 1)(x + 3)$$

### Methode 4: Substitution

Bei bestimmten Strukturen kann eine Substitution helfen:

**Beispiel:** $p(x) = x^4 - 5x^2 + 4$

Substitution: $u = x^2$

$$p = u^2 - 5u + 4 = (u - 1)(u - 4) = (x^2 - 1)(x^2 - 4)$$

$$= (x - 1)(x + 1)(x - 2)(x + 2)$$

### Methode 5: Raten und Polynomdivision

**Schritt 1:** Nullstelle raten (Teiler des konstanten Glieds probieren)

**Schritt 2:** Linearfaktor abspalten mittels Polynomdivision

**Schritt 3:** Mit dem Restpolynom fortfahren

**Beispiel:** $p(x) = x^3 + 2x^2 - 5x - 6$

Teste $x = -1$: $p(-1) = -1 + 2 + 5 - 6 = 0$ ✓

Nach Division durch $(x + 1)$: $p(x) = (x + 1)(x^2 + x - 6) = (x + 1)(x + 3)(x - 2)$

### Methode 6: Summen und Differenzen von Potenzen

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$

$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

**Beispiel:**
$$x^3 - 8 = x^3 - 2^3 = (x - 2)(x^2 + 2x + 4)$$

## Vollständige Faktorisierung

### Über den reellen Zahlen

Ein reelles Polynom lässt sich faktorisieren in:
- **Linearfaktoren** $(x - x_i)$ für reelle Nullstellen
- **Irreduzible quadratische Faktoren** $(x^2 + px + q)$ mit $\frac{p^2}{4} - q < 0$ (negative Diskriminante)

**Beispiel:** $p(x) = x^4 + 4$

Dieses Polynom hat keine reellen Nullstellen, aber:
$$x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$$

### Über den komplexen Zahlen

Jedes Polynom vom Grad $n$ mit Leitkoeffizient $a_n$ lässt sich schreiben als:

$$p(x) = a_n (x - x_1)(x - x_2) \cdots (x - x_n)$$

wobei $x_1, \ldots, x_n \in \mathbb{C}$ die Nullstellen sind (mit Vielfachheiten).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Polynomdivision]] – Technik zum Abspalten von Faktoren
- → [[Gleichungen-hoeheren-Grades]] – Anwendung auf Gleichungslösung
- → [[Polynomfunktionen]] – Graphisches Verhalten an Nullstellen
- → [[Einfuehrung-in-komplexe-Zahlen]] – Komplexe Nullstellen

> [!warning] **Prüfungsrelevant**
> - Systematische Faktorisierung von Polynomen
> - Erkennen und Nutzen besonderer Strukturen (Binome, Substitution)
> - Vielfachheit von Nullstellen und graphische Interpretation
> - Zusammenhang zwischen Nullstellen und Faktoren

> [!question] **Typische Prüfungsfragen**
> - Faktorisiere $p(x) = x^4 - 16$ vollständig über $\mathbb{R}$.
> - Bestimme alle Nullstellen von $p(x) = x^3 - 3x^2 - 4x + 12$ und gib die Faktorisierung an.
> - Welche Vielfachheit hat die Nullstelle $x = 2$ bei $p(x) = (x-2)^3(x+1)^2$? Beschreibe das Verhalten des Graphen dort.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Faktorisierung|Glossar: Faktorisierung]]
> - [[Glossar#Vielfachheit|Glossar: Vielfachheit]]
