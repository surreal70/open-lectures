---
author: Andreas Hümmer
title: Unbestimmte Integrale
tags:
  - content
  - mathe
  - integralrechnung
  - unbestimmtes-integral
  - stammfunktion
created: 2026-10-17
modified: 2026-10-17
---

# Unbestimmte Integrale

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Notation des unbestimmten Integrals verstehen und anwenden können
> - Den Zusammenhang zwischen unbestimmtem Integral und Stammfunktion kennen
> - Einfache unbestimmte Integrale berechnen können
> - Die Bedeutung der Integrationskonstante korrekt wiedergeben

---

## Überblick

Das unbestimmte Integral ist eine kompakte Schreibweise für die Menge aller Stammfunktionen einer gegebenen Funktion. Diese Notation, eingeführt von Leibniz, hat sich als äußerst praktisch erwiesen und bildet die Grundlage für systematisches Integrieren. Im Unterschied zum bestimmten Integral liefert das unbestimmte Integral keine Zahl, sondern eine Funktionenfamilie.

## Definition und Notation

### Das Integralzeichen

Das unbestimmte Integral von $f(x)$ wird geschrieben als:

$$\int f(x) \, dx$$

und bezeichnet die **Menge aller Stammfunktionen** von $f(x)$.

### Bestandteile der Notation

| Symbol | Bezeichnung | Bedeutung |
|--------|-------------|-----------|
| $\int$ | Integralzeichen | Zeigt an, dass integriert wird |
| $f(x)$ | Integrand | Die zu integrierende Funktion |
| $dx$ | Differential | Gibt die Integrationsvariable an |

### Schreibweise des Ergebnisses

Das Ergebnis eines unbestimmten Integrals wird stets mit der Integrationskonstante $C$ angegeben:

$$\int f(x) \, dx = F(x) + C$$

wobei $F(x)$ eine beliebige Stammfunktion von $f(x)$ ist.

## Der Unterschied zum bestimmten Integral

### Vergleich

| Unbestimmtes Integral | Bestimmtes Integral |
|-----------------------|---------------------|
| $\int f(x) \, dx$ | $\int_a^b f(x) \, dx$ |
| Ergebnis: Funktion(enschar) | Ergebnis: Zahl |
| Mit Integrationskonstante $+C$ | Ohne Konstante |
| „Finde die Stammfunktion" | „Berechne die Fläche" |

### Zusammenhang

Das bestimmte Integral kann mithilfe des unbestimmten Integrals berechnet werden. Ist $F(x)$ eine Stammfunktion von $f(x)$, so gilt:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

Dies ist eine Konsequenz des Hauptsatzes der Differential- und Integralrechnung.

## Grundlegende unbestimmte Integrale

### Potenzfunktionen

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$$

**Beispiele**:
- $\int x^2 \, dx = \frac{x^3}{3} + C$
- $\int x^5 \, dx = \frac{x^6}{6} + C$
- $\int \sqrt{x} \, dx = \int x^{1/2} \, dx = \frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C$

### Spezialfall: Konstante Funktion

$$\int a \, dx = ax + C$$

**Beispiel**: $\int 5 \, dx = 5x + C$

### Der Kehrwert

$$\int \frac{1}{x} \, dx = \ln|x| + C \quad (x \neq 0)$$

Der Betrag ist notwendig, da der Logarithmus nur für positive Argumente definiert ist.

### Exponentialfunktionen

$$\int e^x \, dx = e^x + C$$

$$\int e^{kx} \, dx = \frac{1}{k} e^{kx} + C \quad (k \neq 0)$$

$$\int a^x \, dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)$$

### Trigonometrische Funktionen

$$\int \sin(x) \, dx = -\cos(x) + C$$

$$\int \cos(x) \, dx = \sin(x) + C$$

$$\int \frac{1}{\cos^2(x)} \, dx = \tan(x) + C$$

## Rechenbeispiele

### Beispiel 1: Polynomfunktion

Berechne $\int (3x^2 - 4x + 2) \, dx$.

**Lösung**: Integration gliedweise:
$$\int (3x^2 - 4x + 2) \, dx = 3 \cdot \frac{x^3}{3} - 4 \cdot \frac{x^2}{2} + 2x + C = x^3 - 2x^2 + 2x + C$$

**Probe**: $(x^3 - 2x^2 + 2x + C)' = 3x^2 - 4x + 2$ ✓

### Beispiel 2: Wurzelfunktion

Berechne $\int \frac{1}{\sqrt{x}} \, dx$.

**Umformung**: $\frac{1}{\sqrt{x}} = x^{-1/2}$

**Lösung**:
$$\int x^{-1/2} \, dx = \frac{x^{1/2}}{1/2} + C = 2\sqrt{x} + C$$

### Beispiel 3: Exponentialfunktion

Berechne $\int 3e^{2x} \, dx$.

**Lösung**:
$$\int 3e^{2x} \, dx = 3 \cdot \frac{1}{2} e^{2x} + C = \frac{3}{2} e^{2x} + C$$

## Die Bedeutung des Differentials $dx$

### Formale Rolle

Das Symbol $dx$ ist mehr als nur eine Notation. Es gibt an, nach welcher Variable integriert wird. Dies ist besonders wichtig bei:

- **Mehreren Variablen**: $\int xy \, dx$ (hier ist $y$ eine Konstante bezüglich $x$)
- **Substitution**: Das $dx$ transformiert sich entsprechend

### Beispiel mit Parameter

$$\int 2ax \, dx = ax^2 + C$$

Hier wird nur nach $x$ integriert; $a$ ist ein Parameter (Konstante bezüglich $x$).

## Häufige Fehler

### Fehler 1: Integrationskonstante vergessen

❌ $\int 2x \, dx = x^2$

✅ $\int 2x \, dx = x^2 + C$

### Fehler 2: Falscher Exponent

❌ $\int x^3 \, dx = \frac{x^3}{3} + C$

✅ $\int x^3 \, dx = \frac{x^4}{4} + C$

### Fehler 3: Spezialfall $n = -1$ übersehen

❌ $\int \frac{1}{x} \, dx = \frac{x^0}{0} + C$ (Division durch null!)

✅ $\int \frac{1}{x} \, dx = \ln|x| + C$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Stammfunktionen]] – Die theoretische Grundlage des unbestimmten Integrals
- → [[Bestimmte-Integrale]] – Das Integral mit Grenzen
- → [[Grundlegende-Integrationsregeln]] – Systematische Methoden zur Integration
- → [[Definition-der-Ableitung]] – Die Umkehroperation zur Integration
- → [[Polynomfunktionen]] – Einfache Funktionen zum Üben

> [!warning] **Prüfungsrelevant**
> - Die Notation $\int f(x) \, dx = F(x) + C$ korrekt anwenden
> - Die Grundintegrale auswendig kennen
> - Niemals die Integrationskonstante $+C$ vergessen
> - Den Spezialfall $\int \frac{1}{x} \, dx = \ln|x| + C$ beachten

> [!question] **Typische Prüfungsfragen**
> - Berechne das unbestimmte Integral $\int (x^4 - 3x^2 + 5) \, dx$ und überprüfe durch Ableiten.
> - Warum steht beim unbestimmten Integral immer $+C$, beim bestimmten Integral aber nicht?
> - Bestimme $\int \frac{2}{\sqrt[3]{x}} \, dx$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Bestimmte-Integrale]] – Integration mit Grenzen
> - [[Grundlegende-Integrationsregeln]] – Rechenregeln für Integrale
