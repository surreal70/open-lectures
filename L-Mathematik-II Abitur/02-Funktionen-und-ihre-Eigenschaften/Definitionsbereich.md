---
author: Andreas Hümmer
title: Definitionsbereich
tags:
  - content
  - mathe
  - funktionen
  - definitionsbereich
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Definitionsbereich

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Definitionsbereich einer Funktion bestimmen können
> - Einschränkungen durch Division, Wurzeln und Logarithmen erkennen
> - Die natürliche (maximale) Definitionsmenge angeben können
> - Definitionslücken identifizieren und klassifizieren können

---

## Überblick

Der **Definitionsbereich** (auch Definitionsmenge) einer Funktion gibt an, für welche Werte des Arguments die Funktion definiert ist. Die korrekte Bestimmung des Definitionsbereichs ist ein grundlegender Schritt bei der Funktionsuntersuchung und für viele weitere Analysen essentiell.

## Definition und Notation

### Formale Definition

Der **Definitionsbereich** $D_f$ einer Funktion $f$ ist die Menge aller Werte, für die die Funktion einen Funktionswert liefert:

$$D_f = \{x \mid f(x) \text{ ist definiert}\}$$

**Notation:**
- $D_f$, $D(f)$ oder $\mathcal{D}_f$
- Im englischen: domain, geschrieben als $\text{dom}(f)$

### Maximaler Definitionsbereich

Der **maximale** oder **natürliche Definitionsbereich** ist die größtmögliche Menge, auf der $f$ definiert werden kann. Ohne weitere Angaben wird meist der maximale Definitionsbereich angenommen.

## Einschränkungen des Definitionsbereichs

### 1. Division durch Null

Bei Bruchtermen muss der Nenner ungleich Null sein:

$$f(x) = \frac{1}{x-2} \quad \Rightarrow \quad D_f = \mathbb{R} \setminus \{2\}$$

**Allgemein:** Für $f(x) = \frac{p(x)}{q(x)}$ gilt:
$$D_f = \{x \in \mathbb{R} \mid q(x) \neq 0\}$$

**Beispiel:** 
$$f(x) = \frac{x+1}{x^2-4} = \frac{x+1}{(x-2)(x+2)}$$
$$D_f = \mathbb{R} \setminus \{-2, 2\}$$

### 2. Wurzeln aus negativen Zahlen

Bei geraden Wurzeln muss der Radikand nicht-negativ sein:

$$f(x) = \sqrt{x-3} \quad \Rightarrow \quad x - 3 \geq 0 \quad \Rightarrow \quad D_f = [3, \infty)$$

**Allgemein:** Für $f(x) = \sqrt[n]{g(x)}$ mit geradem $n$ gilt:
$$D_f = \{x \in \mathbb{R} \mid g(x) \geq 0\}$$

**Beispiel:**
$$f(x) = \sqrt{4-x^2}$$
$$4 - x^2 \geq 0 \quad \Leftrightarrow \quad x^2 \leq 4 \quad \Leftrightarrow \quad -2 \leq x \leq 2$$
$$D_f = [-2, 2]$$

### 3. Logarithmus

Das Argument des Logarithmus muss positiv sein:

$$f(x) = \ln(x+1) \quad \Rightarrow \quad x + 1 > 0 \quad \Rightarrow \quad D_f = (-1, \infty)$$

**Allgemein:** Für $f(x) = \log_a(g(x))$ gilt:
$$D_f = \{x \in \mathbb{R} \mid g(x) > 0\}$$

### 4. Kombinierte Einschränkungen

Bei zusammengesetzten Funktionen müssen alle Bedingungen gleichzeitig erfüllt sein:

**Beispiel:**
$$f(x) = \frac{\sqrt{x-1}}{x-3}$$

Bedingungen:
1. Wurzel: $x - 1 \geq 0 \Rightarrow x \geq 1$
2. Nenner: $x - 3 \neq 0 \Rightarrow x \neq 3$

$$D_f = [1, 3) \cup (3, \infty) = [1, \infty) \setminus \{3\}$$

## Systematische Bestimmung

### Algorithmus

1. **Identifiziere** alle kritischen Stellen im Funktionsterm
2. **Formuliere** die Bedingungen für jede Einschränkung
3. **Löse** die entstehenden Ungleichungen bzw. Gleichungen
4. **Bilde** den Durchschnitt aller Bedingungen

### Vollständiges Beispiel

Bestimme den Definitionsbereich von:
$$f(x) = \frac{\ln(x^2-1)}{\sqrt{5-x}}$$

**Schritt 1:** Kritische Stellen identifizieren
- Logarithmus: Argument muss positiv sein
- Wurzel im Nenner: Radikand muss positiv sein (nicht nur ≥ 0!)

**Schritt 2:** Bedingungen formulieren
1. $x^2 - 1 > 0$
2. $5 - x > 0$

**Schritt 3:** Ungleichungen lösen

Für (1): $x^2 - 1 > 0 \Leftrightarrow (x-1)(x+1) > 0$
- Lösung: $x < -1$ oder $x > 1$
- In Intervallschreibweise: $(-\infty, -1) \cup (1, \infty)$

Für (2): $5 - x > 0 \Leftrightarrow x < 5$
- In Intervallschreibweise: $(-\infty, 5)$

**Schritt 4:** Durchschnitt bilden
$$D_f = \left[(-\infty, -1) \cup (1, \infty)\right] \cap (-\infty, 5)$$
$$D_f = (-\infty, -1) \cup (1, 5)$$

## Definitionslücken

### Arten von Definitionslücken

**Hebbare Lücke:** Der Grenzwert existiert, aber die Funktion ist an der Stelle nicht definiert.

**Beispiel:** 
$$f(x) = \frac{x^2-1}{x-1} = \frac{(x-1)(x+1)}{x-1}$$

Für $x \neq 1$ gilt $f(x) = x + 1$. Bei $x = 1$ liegt eine hebbare Definitionslücke vor, da $\lim_{x \to 1} f(x) = 2$ existiert.

**Polstelle:** Die Funktion strebt gegen $\pm\infty$.

**Beispiel:** $f(x) = \frac{1}{x}$ hat bei $x = 0$ eine Polstelle.

## Spezielle Funktionen

| Funktionstyp | Einschränkung | Maximaler Definitionsbereich |
|-------------|---------------|------------------------------|
| $f(x) = \frac{1}{x}$ | $x \neq 0$ | $\mathbb{R} \setminus \{0\}$ |
| $f(x) = \sqrt{x}$ | $x \geq 0$ | $[0, \infty)$ |
| $f(x) = \ln(x)$ | $x > 0$ | $(0, \infty)$ |
| $f(x) = \tan(x)$ | $x \neq \frac{\pi}{2} + k\pi$ | $\mathbb{R} \setminus \{\frac{\pi}{2} + k\pi \mid k \in \mathbb{Z}\}$ |
| $f(x) = \arcsin(x)$ | $-1 \leq x \leq 1$ | $[-1, 1]$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wertebereich]] – Bestimmung der Bildmenge einer Funktion
- → [[Wiederholung-des-Funktionsbegriffs]] – Grundlegende Definition von Funktionen
- → [[Reelle-Zahlen-und-Intervalle]] – Intervallschreibweise und Zahlenmengen
- → [[Ungleichungen]] – Lösen von Ungleichungen für die Definitionsbereichsbestimmung

> [!warning] **Prüfungsrelevant**
> - Systematische Bestimmung des Definitionsbereichs bei kombinierten Funktionen
> - Erkennen aller kritischen Stellen (Division, Wurzeln, Logarithmen)
> - Korrekte Verwendung der Intervallschreibweise
> - Unterscheidung zwischen hebbaren Lücken und Polstellen

> [!question] **Typische Prüfungsfragen**
> - Bestimme den maximalen Definitionsbereich von $f(x) = \frac{\sqrt{x+2}}{\ln(x-1)}$.
> - Für welche Werte von $a$ ist die Funktion $f(x) = \sqrt{x^2 - ax + 4}$ auf ganz $\mathbb{R}$ definiert?
> - Erkläre, warum bei $f(x) = \frac{x^2-4}{x-2}$ eine hebbare Definitionslücke vorliegt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Gebrochenrationale-Funktionen]] – Detaillierte Behandlung von Bruchfunktionen
> - [[Logarithmusfunktionen]] – Eigenschaften des Logarithmus
> - [[Wurzelfunktionen]] – Wurzelfunktionen und ihre Eigenschaften
