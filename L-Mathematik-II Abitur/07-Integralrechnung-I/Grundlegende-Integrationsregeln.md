---
author: Andreas Hümmer
title: Grundlegende Integrationsregeln
tags:
  - content
  - mathe
  - integralrechnung
  - integrationsregeln
  - rechenregeln
created: 2026-10-17
modified: 2026-10-17
---

# Grundlegende Integrationsregeln

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Summenregel und Faktorregel für Integrale anwenden können
> - Lineare Verkettungen integrieren können
> - Die Regeln auf verschiedene Funktionstypen anwenden
> - Komplexere Integrale systematisch vereinfachen können

---

## Überblick

Die Integrationsregeln ermöglichen es, komplexere Integrale auf einfachere zurückzuführen. Sie sind die „Umkehrungen" der Ableitungsregeln und bilden das Handwerkszeug für systematisches Integrieren. In diesem Kapitel behandeln wir die grundlegenden Regeln, die für die meisten Abituraufgaben ausreichen.

## Die Faktorregel

### Formulierung

Ist $c \in \mathbb{R}$ eine Konstante, so gilt:

$$\int c \cdot f(x) \, dx = c \cdot \int f(x) \, dx$$

Ein konstanter Faktor kann vor das Integralzeichen gezogen werden.

### Beispiele

$$\int 5x^3 \, dx = 5 \int x^3 \, dx = 5 \cdot \frac{x^4}{4} + C = \frac{5x^4}{4} + C$$

$$\int \frac{1}{2} \cos(x) \, dx = \frac{1}{2} \int \cos(x) \, dx = \frac{1}{2} \sin(x) + C$$

### Wichtig

Die Faktorregel gilt **nur für Konstanten**, nicht für Funktionen!

❌ $\int x \cdot e^x \, dx \neq x \cdot \int e^x \, dx$

## Die Summenregel

### Formulierung

$$\int \big( f(x) + g(x) \big) \, dx = \int f(x) \, dx + \int g(x) \, dx$$

Das Integral einer Summe ist die Summe der Integrale.

### Erweiterung: Differenzregel

$$\int \big( f(x) - g(x) \big) \, dx = \int f(x) \, dx - \int g(x) \, dx$$

### Beispiel

$$\int (x^2 + 3x - 5) \, dx = \int x^2 \, dx + \int 3x \, dx - \int 5 \, dx$$

$$= \frac{x^3}{3} + 3 \cdot \frac{x^2}{2} - 5x + C = \frac{x^3}{3} + \frac{3x^2}{2} - 5x + C$$

## Linearität des Integrals

### Zusammenfassung

Die Faktor- und Summenregel zusammen ergeben die **Linearität des Integrals**:

$$\int \big( \alpha f(x) + \beta g(x) \big) \, dx = \alpha \int f(x) \, dx + \beta \int g(x) \, dx$$

für alle Konstanten $\alpha, \beta \in \mathbb{R}$.

### Anwendung auf Polynome

Jedes Polynom kann gliedweise integriert werden:

$$\int (a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0) \, dx$$

$$= a_n \cdot \frac{x^{n+1}}{n+1} + a_{n-1} \cdot \frac{x^n}{n} + \cdots + a_1 \cdot \frac{x^2}{2} + a_0 x + C$$

## Integration linearer Verkettungen

### Das Prinzip

Für eine Funktion der Form $f(ax + b)$ mit $a \neq 0$ gilt:

$$\int f(ax + b) \, dx = \frac{1}{a} \cdot F(ax + b) + C$$

wobei $F$ eine Stammfunktion von $f$ ist.

### Begründung

Die innere Ableitung $(ax + b)' = a$ muss kompensiert werden, daher der Faktor $\frac{1}{a}$.

**Probe mit Kettenregel**:
$$\frac{d}{dx}\left( \frac{1}{a} F(ax + b) \right) = \frac{1}{a} \cdot F'(ax + b) \cdot a = F'(ax + b) = f(ax + b) \quad \checkmark$$

### Wichtige Spezialfälle

| Integral | Stammfunktion |
|----------|---------------|
| $\int (ax + b)^n \, dx$ | $\frac{1}{a} \cdot \frac{(ax+b)^{n+1}}{n+1} + C$ |
| $\int e^{ax+b} \, dx$ | $\frac{1}{a} e^{ax+b} + C$ |
| $\int \sin(ax + b) \, dx$ | $-\frac{1}{a} \cos(ax+b) + C$ |
| $\int \cos(ax + b) \, dx$ | $\frac{1}{a} \sin(ax+b) + C$ |
| $\int \frac{1}{ax + b} \, dx$ | $\frac{1}{a} \ln|ax+b| + C$ |

### Beispiele

**Beispiel 1**:
$$\int (2x - 3)^4 \, dx = \frac{1}{2} \cdot \frac{(2x-3)^5}{5} + C = \frac{(2x-3)^5}{10} + C$$

**Beispiel 2**:
$$\int e^{-3x+1} \, dx = \frac{1}{-3} e^{-3x+1} + C = -\frac{1}{3} e^{-3x+1} + C$$

**Beispiel 3**:
$$\int \cos(4x) \, dx = \frac{1}{4} \sin(4x) + C$$

## Zusammenstellung der Grundintegrale

### Potenzfunktionen

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$$

$$\int \frac{1}{x} \, dx = \ln|x| + C$$

### Exponentialfunktionen

$$\int e^x \, dx = e^x + C$$

$$\int a^x \, dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)$$

### Trigonometrische Funktionen

$$\int \sin(x) \, dx = -\cos(x) + C$$

$$\int \cos(x) \, dx = \sin(x) + C$$

$$\int \frac{1}{\cos^2(x)} \, dx = \tan(x) + C$$

$$\int \frac{1}{\sin^2(x)} \, dx = -\cot(x) + C$$

## Systematisches Vorgehen

### Strategie bei komplexeren Integralen

1. **Vereinfachen**: Terme ausmultiplizieren oder kürzen, wo möglich
2. **Aufteilen**: Summenregel anwenden
3. **Konstanten herausziehen**: Faktorregel anwenden
4. **Grundintegral erkennen**: Passt ein bekanntes Integral?
5. **Lineare Verkettung**: Liegt die Form $f(ax + b)$ vor?
6. **Probe**: Durch Ableiten überprüfen

### Beispiel: Vollständige Berechnung

Berechne $\int \frac{6x^2 - 2}{x} \, dx$ für $x > 0$.

**Schritt 1**: Vereinfachen durch Division
$$\frac{6x^2 - 2}{x} = 6x - \frac{2}{x}$$

**Schritt 2**: Aufteilen
$$\int \left( 6x - \frac{2}{x} \right) dx = \int 6x \, dx - \int \frac{2}{x} \, dx$$

**Schritt 3 & 4**: Integrieren
$$= 6 \cdot \frac{x^2}{2} - 2 \ln|x| + C = 3x^2 - 2\ln x + C$$

(Der Betrag bei $\ln$ entfällt wegen $x > 0$.)

**Probe**: $(3x^2 - 2\ln x)' = 6x - \frac{2}{x} = \frac{6x^2 - 2}{x}$ ✓

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln]] – Die „Umkehrungen" der Integrationsregeln
- → [[Stammfunktionen]] – Grundbegriff für die Integration
- → [[Kettenregel]] – Grundlage für die Integration linearer Verkettungen
- → [[Integration-von-Potenzfunktionen]] – Vertiefung für Potenzen
- → [[Integration-von-Exponentialfunktionen]] – Vertiefung für Exponentialfunktionen

> [!warning] **Prüfungsrelevant**
> - Die Linearität des Integrals: Faktor- und Summenregel
> - Integration linearer Verkettungen mit dem Faktor $\frac{1}{a}$
> - Die Grundintegrale auswendig können
> - Immer durch Ableiten kontrollieren!

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int (3x^2 - 2x + 4) \, dx$ und überprüfe durch Ableiten.
> - Bestimme $\int \cos(3x - \pi) \, dx$.
> - Warum ist $\int \frac{1}{2x + 1} \, dx = \frac{1}{2} \ln|2x + 1| + C$ und nicht $\ln|2x + 1| + C$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Integration-von-Potenzfunktionen]] – Spezielle Techniken für Potenzen
> - [[Integration-von-Exponentialfunktionen]] – Exponentialfunktionen integrieren
