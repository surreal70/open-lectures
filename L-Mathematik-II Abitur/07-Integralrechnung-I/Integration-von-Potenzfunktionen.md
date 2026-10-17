---
author: Andreas Hümmer
title: Integration von Potenzfunktionen
tags:
  - content
  - mathe
  - integralrechnung
  - potenzfunktionen
  - stammfunktion
created: 2026-10-17
modified: 2026-10-17
---

# Integration von Potenzfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Potenzregel für Integration sicher anwenden können
> - Auch mit negativen und gebrochenen Exponenten integrieren können
> - Den Spezialfall $n = -1$ beherrschen
> - Wurzel- und Bruchterme in Potenzschreibweise umwandeln können

---

## Überblick

Die Integration von Potenzfunktionen ist eine der grundlegendsten Techniken der Integralrechnung. Die Potenzregel für Integrale ist die Umkehrung der Potenzregel für Ableitungen. Da viele Funktionen als Summen von Potenzfunktionen dargestellt werden können, ist diese Regel in der Praxis von zentraler Bedeutung.

## Die Potenzregel

### Hauptformel

Für $n \neq -1$ gilt:

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$

### Merkhilfe

**„Exponent um 1 erhöhen, durch den neuen Exponenten teilen."**

### Probe

$$\frac{d}{dx}\left( \frac{x^{n+1}}{n+1} \right) = \frac{1}{n+1} \cdot (n+1) \cdot x^n = x^n \quad \checkmark$$

## Beispiele mit ganzzahligen Exponenten

### Positive Exponenten

$$\int x^2 \, dx = \frac{x^3}{3} + C$$

$$\int x^5 \, dx = \frac{x^6}{6} + C$$

$$\int x^{10} \, dx = \frac{x^{11}}{11} + C$$

### Exponent null

$$\int x^0 \, dx = \int 1 \, dx = x + C$$

Dies stimmt mit der Potenzregel überein: $\frac{x^1}{1} = x$.

### Negative Exponenten

$$\int x^{-2} \, dx = \frac{x^{-1}}{-1} + C = -\frac{1}{x} + C$$

$$\int x^{-3} \, dx = \frac{x^{-2}}{-2} + C = -\frac{1}{2x^2} + C$$

$$\int \frac{1}{x^4} \, dx = \int x^{-4} \, dx = \frac{x^{-3}}{-3} + C = -\frac{1}{3x^3} + C$$

## Der Spezialfall $n = -1$

### Das Problem

Für $n = -1$ würde die Potenzregel $\frac{x^0}{0}$ liefern – Division durch null ist nicht definiert!

### Die Lösung

$$\int x^{-1} \, dx = \int \frac{1}{x} \, dx = \ln|x| + C$$

### Begründung

Die Ableitung des natürlichen Logarithmus ist:
$$\frac{d}{dx} \ln|x| = \frac{1}{x}$$

Der Betrag ist notwendig, damit die Stammfunktion auch für $x < 0$ definiert ist.

## Gebrochene Exponenten

### Wurzelfunktionen

Wurzeln werden in Potenzschreibweise umgewandelt:

$$\sqrt{x} = x^{1/2}, \quad \sqrt[3]{x} = x^{1/3}, \quad \sqrt[n]{x} = x^{1/n}$$

### Beispiele

$$\int \sqrt{x} \, dx = \int x^{1/2} \, dx = \frac{x^{3/2}}{3/2} + C = \frac{2}{3} x^{3/2} + C = \frac{2}{3} \sqrt{x^3} + C$$

$$\int \sqrt[3]{x} \, dx = \int x^{1/3} \, dx = \frac{x^{4/3}}{4/3} + C = \frac{3}{4} x^{4/3} + C$$

$$\int \frac{1}{\sqrt{x}} \, dx = \int x^{-1/2} \, dx = \frac{x^{1/2}}{1/2} + C = 2\sqrt{x} + C$$

### Rechenregel für Bruchexponenten

Bei der Division durch einen Bruch multipliziert man mit dem Kehrwert:

$$\frac{x^{a/b}}{a/b} = x^{a/b} \cdot \frac{b}{a} = \frac{b}{a} x^{a/b}$$

## Umwandlung von Bruchtermen

### Strategie

Bruchterme mit Potenzen von $x$ im Nenner können als negative Potenzen geschrieben werden:

$$\frac{1}{x^n} = x^{-n}$$

$$\frac{a}{x^n} = a \cdot x^{-n}$$

### Beispiele

$$\int \frac{3}{x^2} \, dx = 3 \int x^{-2} \, dx = 3 \cdot \frac{x^{-1}}{-1} + C = -\frac{3}{x} + C$$

$$\int \frac{5}{x^4} \, dx = 5 \int x^{-4} \, dx = 5 \cdot \frac{x^{-3}}{-3} + C = -\frac{5}{3x^3} + C$$

$$\int \frac{1}{\sqrt[4]{x^3}} \, dx = \int x^{-3/4} \, dx = \frac{x^{1/4}}{1/4} + C = 4x^{1/4} + C = 4\sqrt[4]{x} + C$$

## Kombinierte Beispiele

### Beispiel 1: Polynom

$$\int (x^4 - 3x^2 + 2x - 7) \, dx = \frac{x^5}{5} - x^3 + x^2 - 7x + C$$

### Beispiel 2: Gemischte Terme

$$\int \left( x^3 + \frac{2}{x^2} - \sqrt{x} \right) dx = \int \left( x^3 + 2x^{-2} - x^{1/2} \right) dx$$

$$= \frac{x^4}{4} + 2 \cdot \frac{x^{-1}}{-1} - \frac{x^{3/2}}{3/2} + C = \frac{x^4}{4} - \frac{2}{x} - \frac{2}{3}\sqrt{x^3} + C$$

### Beispiel 3: Vereinfachung vor Integration

$$\int \frac{x^3 - 2x^2 + x}{x} \, dx = \int (x^2 - 2x + 1) \, dx = \frac{x^3}{3} - x^2 + x + C$$

## Bestimmte Integrale mit Potenzfunktionen

### Beispiel

Berechne $\int_1^4 \sqrt{x} \, dx$.

**Stammfunktion**: $F(x) = \frac{2}{3}x^{3/2}$

**Auswertung**:
$$\int_1^4 \sqrt{x} \, dx = \left[ \frac{2}{3}x^{3/2} \right]_1^4 = \frac{2}{3} \cdot 4^{3/2} - \frac{2}{3} \cdot 1^{3/2}$$

$$= \frac{2}{3} \cdot 8 - \frac{2}{3} \cdot 1 = \frac{16}{3} - \frac{2}{3} = \frac{14}{3}$$

## Häufige Fehler

### Fehler 1: Spezialfall vergessen

❌ $\int \frac{1}{x} \, dx = \frac{x^0}{0} + C$

✅ $\int \frac{1}{x} \, dx = \ln|x| + C$

### Fehler 2: Falscher Exponent

❌ $\int x^3 \, dx = \frac{x^3}{3} + C$

✅ $\int x^3 \, dx = \frac{x^4}{4} + C$

### Fehler 3: Wurzel falsch umgewandelt

❌ $\sqrt{x} = x^2$

✅ $\sqrt{x} = x^{1/2}$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Potenzregel]] – Die Umkehrung für Ableitungen
- → [[Grundlegende-Integrationsregeln]] – Faktor- und Summenregel
- → [[Potenzfunktionen]] – Eigenschaften von Potenzfunktionen
- → [[Wurzelfunktionen]] – Wurzeln als Potenzen
- → [[Potenzen-mit-rationalen-Exponenten]] – Bruchexponenten verstehen

> [!warning] **Prüfungsrelevant**
> - Die Potenzregel: $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$ für $n \neq -1$
> - Der Spezialfall: $\int \frac{1}{x} \, dx = \ln|x| + C$
> - Wurzeln in Potenzschreibweise umwandeln können
> - Negative Exponenten bei Bruchtermen richtig einsetzen

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int \left( x^3 - \frac{4}{x^2} + \sqrt[3]{x} \right) dx$.
> - Bestimme $\int_1^9 \frac{1}{\sqrt{x}} \, dx$.
> - Warum gilt die Potenzregel nicht für $n = -1$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Integration-von-Exponentialfunktionen]] – Das nächste wichtige Integral
> - [[Flaechenberechnung]] – Anwendung auf Flächenprobleme
