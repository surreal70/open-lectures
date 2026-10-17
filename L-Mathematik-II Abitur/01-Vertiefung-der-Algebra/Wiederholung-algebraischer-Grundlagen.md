---
author: Andreas Hümmer
title: Wiederholung algebraischer Grundlagen
tags:
  - content
  - mathe
  - algebra
  - terme
  - binomische-formeln
created: 2025-01-13
modified: 2025-01-13
---

# Wiederholung algebraischer Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Terme sicher zusammenfassen, ausmultiplizieren und faktorisieren können
> - Die drei binomischen Formeln anwenden und erkennen können
> - Bruchterme addieren, multiplizieren und kürzen können
> - Doppelbrüche auflösen und vereinfachen können

---

## Überblick

Die algebraischen Grundlagen bilden das Fundament für alle weiteren mathematischen Inhalte der Oberstufe. Ein sicherer Umgang mit Termen, binomischen Formeln und Bruchrechnung ist unerlässlich für die Analysis, die analytische Geometrie und die Stochastik. Dieses Kapitel wiederholt und festigt die wesentlichen Techniken aus der Mittelstufe.

## Terme und Termumformungen

### Grundlegende Rechenregeln

Ein **Term** ist ein sinnvoller mathematischer Ausdruck, der aus Zahlen, Variablen und Rechenzeichen besteht. Bei Termumformungen gelten die bekannten Rechengesetze:

**Kommutativgesetz:**
$$a + b = b + a \quad \text{und} \quad a \cdot b = b \cdot a$$

**Assoziativgesetz:**
$$(a + b) + c = a + (b + c) \quad \text{und} \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)$$

**Distributivgesetz:**
$$a \cdot (b + c) = a \cdot b + a \cdot c$$

### Ausmultiplizieren und Ausklammern

Das **Ausmultiplizieren** wendet das Distributivgesetz an, um Klammern aufzulösen:

$$3x(2x - 5) = 6x^2 - 15x$$

$$(2x + 3)(x - 4) = 2x^2 - 8x + 3x - 12 = 2x^2 - 5x - 12$$

Das **Ausklammern** ist die Umkehrung und dient der Faktorisierung:

$$6x^2 - 15x = 3x(2x - 5)$$

$$ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)$$

## Die binomischen Formeln

Die drei binomischen Formeln sind fundamentale Werkzeuge der Algebra:

### Erste binomische Formel

$$(a + b)^2 = a^2 + 2ab + b^2$$

**Beispiel:** $(3x + 2)^2 = 9x^2 + 12x + 4$

### Zweite binomische Formel

$$(a - b)^2 = a^2 - 2ab + b^2$$

**Beispiel:** $(5x - 3)^2 = 25x^2 - 30x + 9$

### Dritte binomische Formel

$$(a + b)(a - b) = a^2 - b^2$$

**Beispiel:** $(2x + 7)(2x - 7) = 4x^2 - 49$

> [!tip] **Rückwärts erkennen**
> Besonders wichtig ist das Erkennen der binomischen Formeln in umgekehrter Richtung:
> - $x^2 + 6x + 9 = (x + 3)^2$
> - $4x^2 - 25 = (2x + 5)(2x - 5)$

## Bruchrechnung mit Termen

### Addition und Subtraktion von Brüchen

Brüche werden addiert, indem man sie auf den **Hauptnenner** bringt:

$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$$

**Beispiel:**
$$\frac{2}{x+1} + \frac{3}{x-1} = \frac{2(x-1) + 3(x+1)}{(x+1)(x-1)} = \frac{2x - 2 + 3x + 3}{x^2 - 1} = \frac{5x + 1}{x^2 - 1}$$

### Multiplikation und Division von Brüchen

$$\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd} \qquad \frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{ad}{bc}$$

### Kürzen von Brüchen

Vor dem Kürzen müssen Zähler und Nenner **faktorisiert** werden:

$$\frac{x^2 - 4}{x^2 + 4x + 4} = \frac{(x+2)(x-2)}{(x+2)^2} = \frac{x-2}{x+2} \quad \text{für } x \neq -2$$

> [!warning] **Definitionsbereich beachten**
> Beim Kürzen muss stets angegeben werden, für welche Werte der Term nicht definiert ist (Nullstellen des Nenners).

### Doppelbrüche

Ein **Doppelbruch** wird aufgelöst, indem man mit dem Kehrwert des Nennerbruchs multipliziert:

$$\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \cdot \frac{d}{c} = \frac{ad}{bc}$$

**Beispiel:**
$$\frac{\frac{2x}{x+1}}{\frac{4}{x-1}} = \frac{2x}{x+1} \cdot \frac{x-1}{4} = \frac{2x(x-1)}{4(x+1)} = \frac{x(x-1)}{2(x+1)}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Reelle-Zahlen-und-Intervalle]] – Zahlbereiche und ihre Eigenschaften
- → [[Potenzen-mit-rationalen-Exponenten]] – Erweiterung der Potenzgesetze
- → [[Faktorisierung-von-Polynomen]] – Systematische Faktorisierung
- → [[Definitionsbereich]] – Definitionsbereiche bei Bruchtermen

> [!warning] **Prüfungsrelevant**
> - Sichere Anwendung der binomischen Formeln (ohne Taschenrechner!)
> - Bruchterme kürzen und vereinfachen
> - Hauptnenner bestimmen und Brüche addieren
> - Doppelbrüche auflösen

> [!question] **Typische Prüfungsfragen**
> - Vereinfache den Term $\frac{x^2 - 9}{x^2 - 6x + 9}$ und gib den Definitionsbereich an.
> - Fasse zusammen: $\frac{2}{x-3} - \frac{1}{x+3} + \frac{6}{x^2-9}$
> - Für welche Werte von $a$ ist $(x + a)^2 = x^2 + 10x + 25$?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium, Jahrgangsstufe 10*

> [!tip] **Weiterführende Links**
> - [[Glossar#Term|Glossar: Term]]
> - [[Glossar#Binomische Formeln|Glossar: Binomische Formeln]]
