---
author: Andreas Hümmer
title: Binomialkoeffizienten
tags:
  - content
  - mathe
  - kombinatorik
  - binomialkoeffizient
  - pascal
created: 2025-07-01
modified: 2025-07-01
---

# Binomialkoeffizienten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Binomialkoeffizienten berechnen und interpretieren können
> - Das Pascalsche Dreieck kennen und nutzen
> - Die wichtigsten Rechenregeln für Binomialkoeffizienten beherrschen
> - Den binomischen Lehrsatz anwenden können

---

## Überblick

Der Binomialkoeffizient $\binom{n}{k}$ (gesprochen: „$n$ über $k$") gibt die Anzahl der Möglichkeiten an, $k$ Objekte aus $n$ verschiedenen Objekten auszuwählen, ohne Beachtung der Reihenfolge. Er ist eines der wichtigsten Werkzeuge in der Kombinatorik und bildet die Grundlage für viele Berechnungen in der Wahrscheinlichkeitsrechnung.

## Definition und Berechnung

### Formale Definition

Der Binomialkoeffizient ist definiert als:

$$\binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}$$

für $n \geq k \geq 0$ mit $n, k \in \mathbb{N}_0$.

### Alternative Schreibweise

$$\binom{n}{k} = \frac{n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n-k+1)}{k!}$$

Diese Form ist oft praktischer für die Berechnung ohne Taschenrechner.

### Beispielrechnungen

**Beispiel 1:** $\binom{5}{2}$
$$\binom{5}{2} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \cdot 6} = \frac{120}{12} = 10$$

Oder: $\binom{5}{2} = \frac{5 \cdot 4}{2 \cdot 1} = \frac{20}{2} = 10$

**Beispiel 2:** $\binom{10}{3}$
$$\binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = \frac{720}{6} = 120$$

**Beispiel 3:** $\binom{7}{4}$
$$\binom{7}{4} = \frac{7 \cdot 6 \cdot 5 \cdot 4}{4 \cdot 3 \cdot 2 \cdot 1} = \frac{840}{24} = 35$$

## Das Pascalsche Dreieck

Das **Pascalsche Dreieck** ist eine geometrische Anordnung der Binomialkoeffizienten:

```
n=0:                    1
n=1:                  1   1
n=2:                1   2   1
n=3:              1   3   3   1
n=4:            1   4   6   4   1
n=5:          1   5  10  10   5   1
n=6:        1   6  15  20  15   6   1
n=7:      1   7  21  35  35  21   7   1
```

### Bildungsgesetz

Jede Zahl im Pascalschen Dreieck ist die Summe der beiden darüberstehenden Zahlen:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

Diese Beziehung heißt **Additionstheorem** oder **Pascalsche Regel**.

### Ablesung

Um $\binom{n}{k}$ abzulesen:
- Gehe zur $n$-ten Zeile (beginnend bei $n=0$)
- Lese die $k$-te Zahl (beginnend bei $k=0$)

**Beispiel:** $\binom{6}{2} = 15$ (6. Zeile, 3. Eintrag von links)

## Wichtige Rechenregeln

### Symmetrie

$$\binom{n}{k} = \binom{n}{n-k}$$

**Beispiel:** $\binom{10}{3} = \binom{10}{7} = 120$

### Randelemente

$$\binom{n}{0} = \binom{n}{n} = 1$$

### Benachbarte Elemente

$$\binom{n}{k} = \frac{n-k+1}{k} \cdot \binom{n}{k-1}$$

### Zeilensumme

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

**Beispiel:** $\binom{3}{0} + \binom{3}{1} + \binom{3}{2} + \binom{3}{3} = 1 + 3 + 3 + 1 = 8 = 2^3$

### Alternierende Zeilensumme

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$$

## Der binomische Lehrsatz

Der Binomialkoeffizient hat seinen Namen vom **binomischen Lehrsatz**, der die Potenzen eines Binoms $(a+b)^n$ entwickelt:

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

### Ausgeschrieben

$$(a+b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \ldots + \binom{n}{n}b^n$$

### Beispiele

**$(a+b)^2:$**
$$= \binom{2}{0}a^2 + \binom{2}{1}ab + \binom{2}{2}b^2 = a^2 + 2ab + b^2$$

**$(a+b)^3:$**
$$= a^3 + 3a^2b + 3ab^2 + b^3$$

**$(a+b)^4:$**
$$= a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$$

### Anwendungsbeispiel

Berechne $(1{,}02)^5$ mit dem binomischen Lehrsatz:

$$(1 + 0{,}02)^5 = \sum_{k=0}^{5} \binom{5}{k} \cdot 1^{5-k} \cdot (0{,}02)^k$$

$$= 1 + 5 \cdot 0{,}02 + 10 \cdot 0{,}0004 + 10 \cdot 0{,}000008 + \ldots$$
$$\approx 1 + 0{,}1 + 0{,}004 + 0{,}00008 = 1{,}10408$$

## Kombinatorische Interpretation

### Grundbedeutung

$\binom{n}{k}$ = Anzahl der Möglichkeiten, aus $n$ Objekten $k$ auszuwählen

### Teilmengen

$\binom{n}{k}$ = Anzahl der $k$-elementigen Teilmengen einer $n$-elementigen Menge

**Beispiel:** Die Menge $\{a, b, c\}$ hat $\binom{3}{2} = 3$ zweielementige Teilmengen:
$\{a,b\}$, $\{a,c\}$, $\{b,c\}$

### Wege im Gitter

$\binom{n+m}{n}$ = Anzahl der kürzesten Wege von $(0,0)$ nach $(n,m)$ im Koordinatengitter (nur Schritte nach rechts oder oben)

## Verallgemeinerung: Multinomialkoeffizient

Für die Aufteilung von $n$ Objekten in Gruppen der Größen $k_1, k_2, \ldots, k_r$ mit $\sum k_i = n$:

$$\binom{n}{k_1, k_2, \ldots, k_r} = \frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_r!}$$

**Beispiel:** Auf wie viele Arten können 12 Studenten in 3 Gruppen mit 4, 5 und 3 Personen aufgeteilt werden?

$$\binom{12}{4, 5, 3} = \frac{12!}{4! \cdot 5! \cdot 3!} = 27720$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Kombinationen]] — Binomialkoeffizient als Anzahl der Kombinationen
- → [[Fakultaeten]] — Grundlage der Definition
- → [[Bernoulli-Ketten]] — Binomialkoeffizienten in der Binomialverteilung
- → [[Permutationen]] — Zusammenhang mit Permutationen mit Wiederholung

> [!warning] **Prüfungsrelevant**
> - Sichere Berechnung von $\binom{n}{k}$ ohne und mit Taschenrechner
> - Die Symmetrie $\binom{n}{k} = \binom{n}{n-k}$
> - Das Pascalsche Dreieck und das Additionstheorem
> - Der binomische Lehrsatz und seine Anwendung

> [!question] **Typische Prüfungsfragen**
> - Berechne $\binom{8}{3}$ und gib eine kombinatorische Interpretation.
> - Entwickle $(2x - 1)^4$ mit dem binomischen Lehrsatz.
> - Zeige mithilfe des Pascalschen Dreiecks, dass $\binom{6}{3} = \binom{5}{2} + \binom{5}{3}$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik, Springer, 2019

> [!tip] **Weiterführende Links**
> - [[Bernoulli-Experimente]] — Anwendung in der Wahrscheinlichkeitsrechnung
> - [[Bernoulli-Ketten]] — Binomialverteilung
