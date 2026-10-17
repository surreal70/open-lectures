---
author: Andreas Hümmer
title: Bestimmte Integrale
tags:
  - content
  - mathe
  - integralrechnung
  - bestimmtes-integral
  - fläche
created: 2026-10-17
modified: 2026-10-17
---

# Bestimmte Integrale

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das bestimmte Integral als Grenzwert von Summen definieren können
> - Die Notation mit Integrationsgrenzen korrekt anwenden
> - Bestimmte Integrale mithilfe von Stammfunktionen berechnen können
> - Die geometrische Bedeutung als (orientierte) Fläche verstehen

---

## Überblick

Das bestimmte Integral $\int_a^b f(x) \, dx$ ordnet einer Funktion $f$ und einem Intervall $[a, b]$ eine reelle Zahl zu. Diese Zahl entspricht anschaulich der orientierten Fläche zwischen dem Graphen von $f$, der $x$-Achse und den senkrechten Geraden $x = a$ und $x = b$. Im Gegensatz zum unbestimmten Integral ist das Ergebnis keine Funktion, sondern ein konkreter Zahlenwert.

## Definition über Riemann-Summen

### Die Idee der Zerlegung

Sei $f$ eine auf $[a, b]$ definierte Funktion. Wir zerlegen das Intervall in $n$ Teilintervalle gleicher Breite:

$$\Delta x = \frac{b - a}{n}$$

Die Stützstellen sind $x_i = a + i \cdot \Delta x$ für $i = 0, 1, 2, \ldots, n$.

### Die Riemann-Summe

Die **Riemann-Summe** ist definiert als:

$$S_n = \sum_{i=1}^{n} f(x_i^*) \cdot \Delta x$$

wobei $x_i^*$ ein beliebiger Punkt im $i$-ten Teilintervall $[x_{i-1}, x_i]$ ist.

### Definition des bestimmten Integrals

Existiert der Grenzwert der Riemann-Summen für $n \to \infty$ unabhängig von der Wahl der Stützstellen $x_i^*$, so heißt die Funktion $f$ **integrierbar** auf $[a, b]$, und man definiert:

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \cdot \Delta x$$

## Notation und Terminologie

### Bestandteile des bestimmten Integrals

$$\int_a^b f(x) \, dx$$

| Element | Bezeichnung |
|---------|-------------|
| $\int$ | Integralzeichen |
| $a$ | Untere Integrationsgrenze |
| $b$ | Obere Integrationsgrenze |
| $f(x)$ | Integrand |
| $dx$ | Differential der Integrationsvariablen |

### Schreibweise der Auswertung

$$\int_a^b f(x) \, dx = \Big[ F(x) \Big]_a^b = F(b) - F(a)$$

Die eckige Klammer mit den Grenzen bezeichnet man als **Substitutionsklammer** oder **Auswertungsklammer**.

## Berechnung mit Stammfunktionen

### Der praktische Weg

Ist $F(x)$ eine Stammfunktion von $f(x)$, so gilt:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

Dies ist eine direkte Anwendung des Hauptsatzes der Differential- und Integralrechnung.

### Rechenbeispiel 1

Berechne $\int_1^3 x^2 \, dx$.

**Stammfunktion**: $F(x) = \frac{x^3}{3}$

**Auswertung**:
$$\int_1^3 x^2 \, dx = \left[ \frac{x^3}{3} \right]_1^3 = \frac{3^3}{3} - \frac{1^3}{3} = \frac{27}{3} - \frac{1}{3} = \frac{26}{3}$$

### Rechenbeispiel 2

Berechne $\int_0^{\pi} \sin(x) \, dx$.

**Stammfunktion**: $F(x) = -\cos(x)$

**Auswertung**:
$$\int_0^{\pi} \sin(x) \, dx = \Big[ -\cos(x) \Big]_0^{\pi} = -\cos(\pi) - (-\cos(0)) = -(-1) + 1 = 2$$

### Rechenbeispiel 3

Berechne $\int_1^e \frac{1}{x} \, dx$.

**Stammfunktion**: $F(x) = \ln|x| = \ln(x)$ für $x > 0$

**Auswertung**:
$$\int_1^e \frac{1}{x} \, dx = \Big[ \ln(x) \Big]_1^e = \ln(e) - \ln(1) = 1 - 0 = 1$$

## Eigenschaften des bestimmten Integrals

### Linearität

$$\int_a^b \big( \alpha f(x) + \beta g(x) \big) \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$$

### Grenzen vertauschen

$$\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$$

Das Vertauschen der Grenzen kehrt das Vorzeichen um.

### Intervalladditivität

$$\int_a^b f(x) \, dx + \int_b^c f(x) \, dx = \int_a^c f(x) \, dx$$

### Gleiche Grenzen

$$\int_a^a f(x) \, dx = 0$$

### Abschätzung

Ist $m \leq f(x) \leq M$ für alle $x \in [a, b]$, so gilt:

$$m(b-a) \leq \int_a^b f(x) \, dx \leq M(b-a)$$

## Geometrische Interpretation

### Fläche unter der Kurve

Für $f(x) \geq 0$ auf $[a, b]$ entspricht das bestimmte Integral der Fläche zwischen dem Graphen, der $x$-Achse und den Grenzen:

$$A = \int_a^b f(x) \, dx$$

### Orientierte Fläche

Allgemein liefert das bestimmte Integral eine **orientierte Fläche**:
- Bereiche oberhalb der $x$-Achse: positiver Beitrag
- Bereiche unterhalb der $x$-Achse: negativer Beitrag

Das Integral kann daher auch negative Werte oder null annehmen.

### Beispiel: Sinusfunktion

$$\int_0^{2\pi} \sin(x) \, dx = \Big[ -\cos(x) \Big]_0^{2\pi} = -\cos(2\pi) + \cos(0) = -1 + 1 = 0$$

Die positive Fläche im Intervall $[0, \pi]$ und die negative Fläche in $[\pi, 2\pi]$ heben sich exakt auf.

## Die Integrationskonstante beim bestimmten Integral

Ein wichtiger Unterschied zum unbestimmten Integral: Die Integrationskonstante spielt beim bestimmten Integral **keine Rolle**, da sie sich bei der Differenzbildung weghebt:

$$\Big[ F(x) + C \Big]_a^b = (F(b) + C) - (F(a) + C) = F(b) - F(a)$$

Daher wird beim bestimmten Integral die Konstante $C$ nicht geschrieben.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Unbestimmte-Integrale]] – Der Zusammenhang zur Stammfunktion
- → [[Hauptsatz-der-Differential--und-Integralrechnung]] – Die theoretische Begründung
- → [[Flaechenberechnung]] – Anwendung auf Flächenprobleme
- → [[Flaechenbilanz]] – Umgang mit negativen Flächen
- → [[Konvergenz]] – Der Grenzwertbegriff bei Folgen

> [!warning] **Prüfungsrelevant**
> - Die Formel $\int_a^b f(x) \, dx = F(b) - F(a)$ sicher beherrschen
> - Die Auswertungsklammer $\Big[ F(x) \Big]_a^b$ korrekt anwenden
> - Beachten: Beim bestimmten Integral keine Konstante $+C$
> - Die geometrische Interpretation als orientierte Fläche kennen

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int_0^2 (x^3 - x) \, dx$.
> - Erkläre, warum $\int_0^{2\pi} \sin(x) \, dx = 0$ ist, obwohl die Sinusfunktion nicht identisch null ist.
> - Welchen Wert hat $\int_2^5 3 \, dx$? Interpretiere das Ergebnis geometrisch.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Flaechenberechnung]] – Praktische Anwendungen
> - [[Hauptsatz-der-Differential--und-Integralrechnung]] – Der theoretische Hintergrund
