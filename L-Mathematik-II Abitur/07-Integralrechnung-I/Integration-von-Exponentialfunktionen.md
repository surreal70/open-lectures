---
author: Andreas Hümmer
title: Integration von Exponentialfunktionen
tags:
  - content
  - mathe
  - integralrechnung
  - exponentialfunktionen
  - e-funktion
created: 2026-10-17
modified: 2026-10-17
---

# Integration von Exponentialfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die natürliche Exponentialfunktion $e^x$ integrieren können
> - Exponentialfunktionen mit linearem Argument integrieren können
> - Allgemeine Exponentialfunktionen $a^x$ integrieren können
> - Die Formeln sicher auf Aufgaben anwenden können

---

## Überblick

Exponentialfunktionen spielen in der Mathematik und den Naturwissenschaften eine herausragende Rolle, da sie Wachstums- und Zerfallsprozesse beschreiben. Die Integration von Exponentialfunktionen ist verhältnismäßig einfach, da die natürliche Exponentialfunktion $e^x$ die besondere Eigenschaft hat, ihre eigene Stammfunktion zu sein.

## Die natürliche Exponentialfunktion

### Grundformel

Die einfachste Exponentialintegration:

$$\int e^x \, dx = e^x + C$$

### Besonderheit

Die Funktion $e^x$ ist die **einzige Funktion** (bis auf konstante Vielfache), die beim Ableiten und Integrieren unverändert bleibt.

### Probe

$$\frac{d}{dx}(e^x) = e^x \quad \checkmark$$

## Exponentialfunktionen mit linearem Argument

### Allgemeine Formel

Für $k \neq 0$ gilt:

$$\int e^{kx} \, dx = \frac{1}{k} e^{kx} + C$$

### Begründung

Der Faktor $\frac{1}{k}$ kompensiert die innere Ableitung bei der Kettenregel:

$$\frac{d}{dx}\left(\frac{1}{k} e^{kx}\right) = \frac{1}{k} \cdot k \cdot e^{kx} = e^{kx} \quad \checkmark$$

### Beispiele

$$\int e^{2x} \, dx = \frac{1}{2} e^{2x} + C$$

$$\int e^{-x} \, dx = \frac{1}{-1} e^{-x} + C = -e^{-x} + C$$

$$\int e^{3x} \, dx = \frac{1}{3} e^{3x} + C$$

$$\int e^{-0{,}5x} \, dx = \frac{1}{-0{,}5} e^{-0{,}5x} + C = -2e^{-0{,}5x} + C$$

## Erweiterung: Lineares Argument $ax + b$

### Formel

$$\int e^{ax+b} \, dx = \frac{1}{a} e^{ax+b} + C \quad (a \neq 0)$$

### Beispiele

$$\int e^{2x-3} \, dx = \frac{1}{2} e^{2x-3} + C$$

$$\int e^{-4x+1} \, dx = -\frac{1}{4} e^{-4x+1} + C$$

$$\int e^{\frac{x}{2}+5} \, dx = 2e^{\frac{x}{2}+5} + C$$

## Kombination mit konstantem Faktor

### Anwendung der Faktorregel

$$\int c \cdot e^{kx} \, dx = c \cdot \frac{1}{k} e^{kx} + C = \frac{c}{k} e^{kx} + C$$

### Beispiele

$$\int 5e^{2x} \, dx = \frac{5}{2} e^{2x} + C$$

$$\int 3e^{-x} \, dx = -3e^{-x} + C$$

$$\int \frac{1}{2}e^{4x} \, dx = \frac{1}{8} e^{4x} + C$$

## Allgemeine Exponentialfunktion $a^x$

### Formel

Für $a > 0$ und $a \neq 1$ gilt:

$$\int a^x \, dx = \frac{a^x}{\ln a} + C$$

### Herleitung

Da $a^x = e^{x \ln a}$, folgt:

$$\int a^x \, dx = \int e^{x \ln a} \, dx = \frac{1}{\ln a} e^{x \ln a} + C = \frac{a^x}{\ln a} + C$$

### Beispiele

$$\int 2^x \, dx = \frac{2^x}{\ln 2} + C$$

$$\int 10^x \, dx = \frac{10^x}{\ln 10} + C$$

$$\int \left(\frac{1}{2}\right)^x \, dx = \frac{(1/2)^x}{\ln(1/2)} + C = -\frac{(1/2)^x}{\ln 2} + C$$

## Bestimmte Integrale

### Beispiel 1

Berechne $\int_0^1 e^{2x} \, dx$.

**Stammfunktion**: $F(x) = \frac{1}{2}e^{2x}$

**Auswertung**:
$$\int_0^1 e^{2x} \, dx = \left[\frac{1}{2}e^{2x}\right]_0^1 = \frac{1}{2}e^2 - \frac{1}{2}e^0 = \frac{1}{2}(e^2 - 1) \approx 3{,}19$$

### Beispiel 2

Berechne $\int_0^{\ln 2} e^{-x} \, dx$.

**Stammfunktion**: $F(x) = -e^{-x}$

**Auswertung**:
$$\int_0^{\ln 2} e^{-x} \, dx = \left[-e^{-x}\right]_0^{\ln 2} = -e^{-\ln 2} + e^0 = -\frac{1}{2} + 1 = \frac{1}{2}$$

### Beispiel 3

Berechne $\int_1^2 3 \cdot 2^x \, dx$.

**Stammfunktion**: $F(x) = \frac{3 \cdot 2^x}{\ln 2}$

**Auswertung**:
$$\int_1^2 3 \cdot 2^x \, dx = \left[\frac{3 \cdot 2^x}{\ln 2}\right]_1^2 = \frac{3}{\ln 2}(2^2 - 2^1) = \frac{3}{\ln 2} \cdot 2 = \frac{6}{\ln 2} \approx 8{,}66$$

## Zusammengesetzte Funktionen

### Typ: $f(x) \cdot e^{g(x)}$

Funktionen der Form $f(x) \cdot e^{g(x)}$ können oft nicht elementar integriert werden. Ausnahme: Wenn $f(x) = g'(x)$ ist, liegt eine einfache Verkettung vor.

$$\int g'(x) \cdot e^{g(x)} \, dx = e^{g(x)} + C$$

### Beispiel

$$\int 2x \cdot e^{x^2} \, dx = e^{x^2} + C$$

**Probe**: $(e^{x^2})' = 2x \cdot e^{x^2}$ ✓

## Tabelle wichtiger Integrale

| Integral | Stammfunktion |
|----------|---------------|
| $\int e^x \, dx$ | $e^x + C$ |
| $\int e^{kx} \, dx$ | $\frac{1}{k}e^{kx} + C$ |
| $\int e^{ax+b} \, dx$ | $\frac{1}{a}e^{ax+b} + C$ |
| $\int a^x \, dx$ | $\frac{a^x}{\ln a} + C$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentialfunktionen]] – Eigenschaften der Exponentialfunktion
- → [[Exponentielles-Wachstum]] – Anwendung: Wachstum und Zerfall
- → [[Grundlegende-Integrationsregeln]] – Lineare Verkettungen
- → [[Kettenregel]] – Begründung für den Faktor $\frac{1}{k}$
- → [[Logarithmusfunktionen]] – Der natürliche Logarithmus

> [!warning] **Prüfungsrelevant**
> - $\int e^x \, dx = e^x + C$ – die einfachste Formel
> - $\int e^{kx} \, dx = \frac{1}{k}e^{kx} + C$ – den Faktor $\frac{1}{k}$ nicht vergessen!
> - $\int a^x \, dx = \frac{a^x}{\ln a} + C$ – für allgemeine Basen
> - Bei bestimmten Integralen: exakte Werte mit $e$ stehen lassen, nicht numerisch auswerten

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int_0^2 e^{-0{,}5x} \, dx$.
> - Bestimme die Stammfunktion von $f(x) = 4e^{3x-1}$.
> - Berechne $\int 5 \cdot 3^x \, dx$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Integration-trigonometrischer-Funktionen]] – Weitere wichtige Integrale
> - [[Integrale-im-Sachzusammenhang]] – Anwendungen auf Wachstumsprozesse
