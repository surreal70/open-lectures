---
author: Andreas Hümmer
title: Ungleichungen
tags:
  - content
  - mathe
  - algebra
  - ungleichungen
  - intervalle
  - vorzeichentabelle
created: 2025-01-13
modified: 2025-01-13
---

# Ungleichungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Lineare und quadratische Ungleichungen lösen können
> - Die Vorzeichentabelle als systematische Methode anwenden können
> - Bruchungleichungen lösen können
> - Lösungsmengen in Intervallschreibweise angeben können

---

## Überblick

Ungleichungen beschreiben Bereiche, in denen bestimmte Bedingungen erfüllt sind. Sie spielen eine wichtige Rolle bei der Bestimmung von Definitionsbereichen, Wertebereichen und Extremwertproblemen. Die Lösungsmenge einer Ungleichung ist typischerweise ein Intervall oder eine Vereinigung von Intervallen.

## Grundlagen

### Ungleichungszeichen

| Symbol | Bedeutung |
|--------|-----------|
| $<$ | echt kleiner |
| $>$ | echt größer |
| $\leq$ | kleiner oder gleich |
| $\geq$ | größer oder gleich |

### Rechenregeln für Ungleichungen

**Addition/Subtraktion:** Ungleichungszeichen bleibt erhalten

$$a < b \quad \Rightarrow \quad a + c < b + c$$

**Multiplikation mit positiver Zahl:** Ungleichungszeichen bleibt erhalten

$$a < b \text{ und } c > 0 \quad \Rightarrow \quad a \cdot c < b \cdot c$$

**Multiplikation mit negativer Zahl:** Ungleichungszeichen **kehrt sich um**

$$a < b \text{ und } c < 0 \quad \Rightarrow \quad a \cdot c > b \cdot c$$

> [!warning] **Wichtig: Umkehrung beachten!**
> Beim Multiplizieren oder Dividieren mit negativen Zahlen **dreht sich das Ungleichungszeichen um**!

## Lineare Ungleichungen

Eine lineare Ungleichung hat die Form $ax + b < c$ (oder mit anderem Ungleichungszeichen).

**Beispiel:** $3x - 5 > 7$

$$3x > 12$$
$$x > 4$$

Lösungsmenge: $\mathbb{L} = (4, \infty)$

**Beispiel mit Umkehrung:** $-2x + 3 \leq 9$

$$-2x \leq 6$$
$$x \geq -3$$ (Zeichen umgekehrt!)

Lösungsmenge: $\mathbb{L} = [-3, \infty)$

## Quadratische Ungleichungen

### Methode 1: Faktorisierung

**Beispiel:** $x^2 - 5x + 6 > 0$

**Schritt 1:** Nullstellen bestimmen

$x^2 - 5x + 6 = 0 \Rightarrow (x-2)(x-3) = 0 \Rightarrow x_1 = 2, x_2 = 3$

**Schritt 2:** Vorzeichentabelle erstellen

| Intervall | $(x-2)$ | $(x-3)$ | Produkt |
|-----------|---------|---------|---------|
| $x < 2$ | $-$ | $-$ | $+$ |
| $2 < x < 3$ | $+$ | $-$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ |

**Schritt 3:** Bereiche mit positivem Vorzeichen auswählen

Lösungsmenge: $\mathbb{L} = (-\infty, 2) \cup (3, \infty)$

### Methode 2: Grafische Interpretation

Die Parabel $y = x^2 - 5x + 6$ öffnet nach oben (Koeffizient von $x^2$ positiv).

- Für $x^2 - 5x + 6 > 0$: oberhalb der x-Achse → außerhalb der Nullstellen
- Für $x^2 - 5x + 6 < 0$: unterhalb der x-Achse → zwischen den Nullstellen

> [!tip] **Merkhilfe: Parabel-Regel**
> Bei einer nach oben geöffneten Parabel mit zwei Nullstellen $x_1 < x_2$:
> - $> 0$: außen, also $x < x_1$ oder $x > x_2$
> - $< 0$: innen, also $x_1 < x < x_2$

## Vorzeichentabelle (Allgemeines Verfahren)

Die Vorzeichentabelle ist eine systematische Methode für Produkte und Quotienten.

### Beispiel: $\frac{(x+1)(x-3)}{x-1} \leq 0$

**Schritt 1:** Nullstellen von Zähler und Nenner

- Zähler-Nullstellen: $x = -1, x = 3$
- Nenner-Nullstelle: $x = 1$ (Definitionslücke!)

**Schritt 2:** Zahlenstrahl in Intervalle teilen

Kritische Punkte: $-1, 1, 3$

**Schritt 3:** Vorzeichen in jedem Intervall bestimmen

| Intervall | $(x+1)$ | $(x-3)$ | $(x-1)$ | Gesamt |
|-----------|---------|---------|---------|--------|
| $x < -1$ | $-$ | $-$ | $-$ | $-$ |
| $-1 < x < 1$ | $+$ | $-$ | $-$ | $+$ |
| $1 < x < 3$ | $+$ | $-$ | $+$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ | $+$ |

**Schritt 4:** Bereiche auswählen (hier: $\leq 0$)

Negativ: $x < -1$ und $1 < x < 3$

Nullstellen des Zählers einbeziehen: $x = -1$ und $x = 3$ erfüllen $= 0$

**Aber:** $x = 1$ ist nicht erlaubt (Definitionslücke)

Lösungsmenge: $\mathbb{L} = (-\infty, -1] \cup (1, 3]$

## Bruchungleichungen

Bei Bruchungleichungen nie durch den Nenner multiplizieren, ohne dessen Vorzeichen zu kennen!

**Falsche Methode:**
$$\frac{2}{x-1} > 3 \quad \not\Rightarrow \quad 2 > 3(x-1)$$
(Das Vorzeichen von $(x-1)$ ist unbekannt!)

**Richtige Methode:** Auf eine Seite bringen und Vorzeichentabelle verwenden

$$\frac{2}{x-1} - 3 > 0$$
$$\frac{2 - 3(x-1)}{x-1} > 0$$
$$\frac{2 - 3x + 3}{x-1} > 0$$
$$\frac{5 - 3x}{x-1} > 0$$

Nun Vorzeichentabelle mit Nullstellen $x = \frac{5}{3}$ (Zähler) und $x = 1$ (Nenner).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Reelle-Zahlen-und-Intervalle]] – Intervallschreibweise
- → [[Betrag-und-Betragsgleichungen]] – Betragsungleichungen
- → [[Quadratische-Funktionen]] – Parabel und Vorzeichenverhalten
- → [[Definitionsbereich]] – Ungleichungen zur Bereichsbestimmung

> [!warning] **Prüfungsrelevant**
> - Lineare Ungleichungen mit Vorzeichenumkehr
> - Quadratische Ungleichungen lösen
> - Vorzeichentabellen erstellen und interpretieren
> - Lösungsmengen korrekt in Intervallschreibweise angeben

> [!question] **Typische Prüfungsfragen**
> - Löse die Ungleichung $x^2 - 4x - 5 \leq 0$ und gib die Lösungsmenge an.
> - Für welche $x$ gilt $\frac{x+2}{x-3} < 1$?
> - Bestimme alle $x$ mit $(x-1)(x+2)(x-4) > 0$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Ungleichung|Glossar: Ungleichung]]
> - [[Glossar#Vorzeichentabelle|Glossar: Vorzeichentabelle]]
