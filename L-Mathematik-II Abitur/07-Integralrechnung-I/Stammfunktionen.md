---
author: Andreas Hümmer
title: Stammfunktionen
tags:
  - content
  - mathe
  - integralrechnung
  - stammfunktion
  - antiderivative
created: 2026-10-17
modified: 2026-10-17
---

# Stammfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Stammfunktion definieren können
> - Verstehen, warum Stammfunktionen nur bis auf eine Konstante eindeutig sind
> - Einfache Stammfunktionen durch Rückwärtsableiten finden können
> - Die Notation für Stammfunktionen korrekt verwenden

---

## Überblick

Eine Stammfunktion ist gewissermaßen die „Umkehrung" einer Ableitung. Während wir beim Differenzieren von einer Funktion $f(x)$ ausgehen und ihre Ableitung $f'(x)$ suchen, stellen wir bei Stammfunktionen die umgekehrte Frage: Welche Funktion $F(x)$ hat als Ableitung die gegebene Funktion $f(x)$? Diese Fragestellung ist fundamental für die Integralrechnung.

## Definition der Stammfunktion

### Formale Definition

> Eine Funktion $F(x)$ heißt **Stammfunktion** von $f(x)$ auf einem Intervall $I$, wenn für alle $x \in I$ gilt:
> $$F'(x) = f(x)$$

Anders ausgedrückt: Die Ableitung der Stammfunktion ergibt die ursprüngliche Funktion.

### Beispiele

| Funktion $f(x)$ | Stammfunktion $F(x)$ | Probe: $F'(x)$ |
|----------------|---------------------|----------------|
| $f(x) = 2x$ | $F(x) = x^2$ | $(x^2)' = 2x$ ✓ |
| $f(x) = 3x^2$ | $F(x) = x^3$ | $(x^3)' = 3x^2$ ✓ |
| $f(x) = \cos(x)$ | $F(x) = \sin(x)$ | $(\sin(x))' = \cos(x)$ ✓ |
| $f(x) = e^x$ | $F(x) = e^x$ | $(e^x)' = e^x$ ✓ |

## Die Integrationskonstante

### Mehrdeutigkeit von Stammfunktionen

Ein entscheidender Unterschied zur Differentiation: Die Stammfunktion ist **nicht eindeutig**. Ist $F(x)$ eine Stammfunktion von $f(x)$, so ist auch $F(x) + C$ für jede Konstante $C \in \mathbb{R}$ eine Stammfunktion, denn:

$$(F(x) + C)' = F'(x) + 0 = f(x)$$

### Die allgemeine Stammfunktion

Die Menge aller Stammfunktionen von $f(x)$ bildet eine **Funktionenschar**:

$$\{F(x) + C \mid C \in \mathbb{R}\}$$

Man schreibt die allgemeine Stammfunktion als:

$$F(x) + C$$

wobei $C$ die **Integrationskonstante** heißt.

### Geometrische Interpretation

Grafisch betrachtet unterscheiden sich alle Stammfunktionen nur durch eine vertikale Verschiebung. Ihre Graphen sind zueinander **parallel** in dem Sinne, dass sie an jeder Stelle $x$ dieselbe Steigung haben.

## Das Finden von Stammfunktionen

### Strategie: Rückwärts ableiten

Der grundlegende Ansatz besteht darin, den Differentiationsprozess „rückwärts" zu denken:

1. **Analysiere** die gegebene Funktion $f(x)$
2. **Frage**: Welche Funktion ergibt beim Ableiten $f(x)$?
3. **Überprüfe** durch Differentiation

### Beispiel: Potenzfunktionen

Für $f(x) = x^n$ mit $n \neq -1$:

**Überlegung**: Da $(x^{n+1})' = (n+1) \cdot x^n$, muss die Stammfunktion den Faktor $\frac{1}{n+1}$ enthalten.

**Stammfunktion**: 
$$F(x) = \frac{x^{n+1}}{n+1} + C$$

**Probe**: 
$$F'(x) = \frac{(n+1) \cdot x^n}{n+1} = x^n = f(x) \quad \checkmark$$

### Beispiel: Exponentialfunktion

Für $f(x) = e^{kx}$ mit $k \neq 0$:

**Überlegung**: Da $(e^{kx})' = k \cdot e^{kx}$, muss der Faktor $\frac{1}{k}$ ausgeglichen werden.

**Stammfunktion**:
$$F(x) = \frac{1}{k} e^{kx} + C$$

**Probe**:
$$F'(x) = \frac{1}{k} \cdot k \cdot e^{kx} = e^{kx} = f(x) \quad \checkmark$$

## Wichtige Grundstammfunktionen

### Tabelle der elementaren Stammfunktionen

| $f(x)$ | $F(x)$ | Bedingung |
|--------|--------|-----------|
| $x^n$ | $\frac{x^{n+1}}{n+1}$ | $n \neq -1$ |
| $\frac{1}{x}$ | $\ln|x|$ | $x \neq 0$ |
| $e^x$ | $e^x$ | — |
| $a^x$ | $\frac{a^x}{\ln a}$ | $a > 0, a \neq 1$ |
| $\sin(x)$ | $-\cos(x)$ | — |
| $\cos(x)$ | $\sin(x)$ | — |

### Merkregel für trigonometrische Funktionen

Beim Integrieren trigonometrischer Funktionen wechselt das Vorzeichen „anders herum" als beim Ableiten:

- $(\sin x)' = \cos x$, aber $\int \cos x \, dx = \sin x + C$
- $(\cos x)' = -\sin x$, aber $\int \sin x \, dx = -\cos x + C$

## Existenz von Stammfunktionen

### Satz über die Existenz

Jede auf einem Intervall $I$ stetige Funktion besitzt dort eine Stammfunktion.

Dieser wichtige Satz garantiert, dass das Suchen nach Stammfunktionen für stetige Funktionen grundsätzlich erfolgreich sein wird – auch wenn man sie nicht immer in geschlossener Form angeben kann.

### Funktionen ohne elementare Stammfunktion

Nicht jede Funktion besitzt eine Stammfunktion, die sich durch elementare Funktionen ausdrücken lässt. Bekannte Beispiele:

- $f(x) = e^{-x^2}$ (Gauß-Funktion)
- $f(x) = \frac{\sin x}{x}$
- $f(x) = \frac{1}{\ln x}$

Für solche Funktionen verwendet man numerische Methoden oder definiert neue, sogenannte „spezielle Funktionen".

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Definition-der-Ableitung]] – Die Ableitung als Umkehroperation zur Stammfunktion
- → [[Ableitungsregeln]] – Regeln, die „rückwärts" für Stammfunktionen gelten
- → [[Unbestimmte-Integrale]] – Alternative Schreibweise für Stammfunktionen
- → [[Grundlegende-Integrationsregeln]] – Systematische Methoden zum Finden von Stammfunktionen
- → [[Polynomfunktionen]] – Einfache Funktionen zum Üben

> [!warning] **Prüfungsrelevant**
> - Definition der Stammfunktion: $F'(x) = f(x)$
> - Die Integrationskonstante $C$ niemals vergessen!
> - Die Grundstammfunktionen auswendig kennen
> - Überprüfung durch Ableiten der Stammfunktion

> [!question] **Typische Prüfungsfragen**
> - Bestimme eine Stammfunktion von $f(x) = 4x^3 - 2x + 1$.
> - Warum gibt es zu einer Funktion unendlich viele Stammfunktionen?
> - Überprüfe durch Ableiten, ob $F(x) = x^2 \cdot e^x$ eine Stammfunktion von $f(x) = e^x(2x + x^2)$ ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Königsberger, K.: Analysis 1. Springer, 2004.

> [!tip] **Weiterführende Links**
> - [[Unbestimmte-Integrale]] – Die Integralschreibweise für Stammfunktionen
> - [[Grundlegende-Integrationsregeln]] – Systematische Methoden
