---
author: Andreas Hümmer
title: Substitution – Integration durch Variablenwechsel
tags:
  - content
  - mathe
  - integralrechnung
  - substitution
  - integrationstechnik
created: 2025-06-26
modified: 2025-06-26
---

# Substitution

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Prinzip der Substitution als Umkehrung der Kettenregel verstehen
> - Die Substitutionsmethode systematisch auf Integrale anwenden können
> - Geeignete Substitutionen für verschiedene Integraltypen erkennen
> - Sowohl bestimmte als auch unbestimmte Integrale mit Substitution lösen können

---

## Überblick

Die **Substitution** (auch: **Integration durch Variablenwechsel**) ist die wichtigste und am häufigsten verwendete Integrationstechnik. Sie basiert auf der Umkehrung der **Kettenregel** der Differentialrechnung und ermöglicht die Berechnung von Integralen, die sich nicht direkt durch Grundintegrale lösen lassen.

Das Grundprinzip: Wir ersetzen einen Teil des Integranden durch eine neue Variable, um das Integral in eine einfachere Form zu bringen.

---

## Mathematische Grundlage

### Herleitung aus der Kettenregel

Die Kettenregel besagt für eine verkettete Funktion $F(g(x))$:

$$\frac{d}{dx}[F(g(x))] = F'(g(x)) \cdot g'(x)$$

Umgekehrt gilt für die Integration:

$$\int f(g(x)) \cdot g'(x) \, dx = F(g(x)) + C$$

wobei $F$ eine Stammfunktion von $f$ ist.

### Das Substitutionsprinzip

Setzen wir $u = g(x)$, dann ist $\frac{du}{dx} = g'(x)$, also formal $du = g'(x) \cdot dx$.

Das Integral wird zu:

$$\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du$$

> [!tip] **Merksatz**
> Die Substitution verwandelt ein kompliziertes Integral in $x$ in ein einfacheres Integral in $u$.

---

## Systematisches Vorgehen

### Schritt-für-Schritt-Anleitung

1. **Substitution wählen**: Identifiziere einen geeigneten Ausdruck $u = g(x)$
2. **Ableitung bilden**: Berechne $\frac{du}{dx} = g'(x)$
3. **dx ersetzen**: Forme um zu $dx = \frac{du}{g'(x)}$
4. **Integral umschreiben**: Ersetze alle $x$-Ausdrücke durch $u$
5. **Integral lösen**: Berechne das Integral in $u$
6. **Rücksubstitution**: Ersetze $u$ wieder durch $g(x)$

### Beispiel 1: Lineare Substitution

Berechne $\int (2x + 3)^5 \, dx$

**Lösung:**

Substitution: $u = 2x + 3$

Ableitung: $\frac{du}{dx} = 2$, also $dx = \frac{du}{2}$

Einsetzen:
$$\int (2x + 3)^5 \, dx = \int u^5 \cdot \frac{du}{2} = \frac{1}{2} \int u^5 \, du$$

Stammfunktion:
$$= \frac{1}{2} \cdot \frac{u^6}{6} + C = \frac{u^6}{12} + C$$

Rücksubstitution:
$$= \frac{(2x + 3)^6}{12} + C$$

### Beispiel 2: Wurzel im Nenner

Berechne $\int \frac{x}{\sqrt{x^2 + 1}} \, dx$

**Lösung:**

Substitution: $u = x^2 + 1$

Ableitung: $\frac{du}{dx} = 2x$, also $x \, dx = \frac{du}{2}$

Einsetzen:
$$\int \frac{x}{\sqrt{x^2 + 1}} \, dx = \int \frac{1}{\sqrt{u}} \cdot \frac{du}{2} = \frac{1}{2} \int u^{-1/2} \, du$$

Stammfunktion:
$$= \frac{1}{2} \cdot 2u^{1/2} + C = \sqrt{u} + C$$

Rücksubstitution:
$$= \sqrt{x^2 + 1} + C$$

---

## Substitution bei bestimmten Integralen

Bei bestimmten Integralen müssen auch die **Integrationsgrenzen** angepasst werden!

### Vorgehensweise

Wenn $u = g(x)$ und die ursprünglichen Grenzen $a$ und $b$ sind:
- Untere Grenze: $u_1 = g(a)$
- Obere Grenze: $u_2 = g(b)$

$$\int_a^b f(g(x)) \cdot g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du$$

### Beispiel: Bestimmtes Integral

Berechne $\int_0^2 x \cdot e^{x^2} \, dx$

**Lösung:**

Substitution: $u = x^2$

Ableitung: $\frac{du}{dx} = 2x$, also $x \, dx = \frac{du}{2}$

Grenzen anpassen:
- Für $x = 0$: $u = 0^2 = 0$
- Für $x = 2$: $u = 2^2 = 4$

Einsetzen:
$$\int_0^2 x \cdot e^{x^2} \, dx = \frac{1}{2} \int_0^4 e^u \, du$$

Berechnung:
$$= \frac{1}{2} \left[e^u\right]_0^4 = \frac{1}{2}(e^4 - e^0) = \frac{1}{2}(e^4 - 1) \approx 26{,}80$$

---

## Typische Substitutionsmuster

### Muster 1: Innere Funktion und ihre Ableitung

Wenn der Integrand die Form $f(g(x)) \cdot g'(x)$ hat:

| Integral | Substitution | Ergebnis |
|----------|--------------|----------|
| $\int \cos(3x) \, dx$ | $u = 3x$ | $\frac{1}{3}\sin(3x) + C$ |
| $\int e^{2x} \, dx$ | $u = 2x$ | $\frac{1}{2}e^{2x} + C$ |
| $\int \frac{2x}{x^2+1} \, dx$ | $u = x^2 + 1$ | $\ln|x^2+1| + C$ |

### Muster 2: Logarithmische Integration

$$\int \frac{f'(x)}{f(x)} \, dx = \ln|f(x)| + C$$

**Beispiel:** $\int \frac{2x + 1}{x^2 + x} \, dx$

Mit $u = x^2 + x$ und $\frac{du}{dx} = 2x + 1$:

$$= \ln|x^2 + x| + C$$

### Muster 3: Wurzel-Substitution

Für Integrale mit $\sqrt{ax + b}$ setze $u = \sqrt{ax + b}$, also $u^2 = ax + b$.

**Beispiel:** $\int x \sqrt{x + 1} \, dx$

Substitution: $u = \sqrt{x + 1}$, also $x = u^2 - 1$ und $dx = 2u \, du$

$$\int x \sqrt{x + 1} \, dx = \int (u^2 - 1) \cdot u \cdot 2u \, du = 2 \int (u^4 - u^2) \, du$$

$$= 2 \left(\frac{u^5}{5} - \frac{u^3}{3}\right) + C = \frac{2(x+1)^{5/2}}{5} - \frac{2(x+1)^{3/2}}{3} + C$$

---

## Tipps zur Wahl der Substitution

> [!tip] **Erkennungsmerkmale**
> 1. Suche nach einer "inneren Funktion" $g(x)$, deren Ableitung $g'(x)$ (oder ein Vielfaches davon) als Faktor auftritt
> 2. Komplizierte Ausdrücke in Wurzeln, Exponenten oder Argumenten sind gute Kandidaten für $u$
> 3. Bei $\int \frac{f'(x)}{f(x)} \, dx$ ist $u = f(x)$ die richtige Wahl
> 4. Bei trigonometrischen Funktionen: oft ist das Argument die passende Substitution

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Partielle-Integration|Partielle Integration]] – Alternative Integrationstechnik für Produkte
- → [[Kettenregel|Kettenregel]] – Die Differentiationsregel, die der Substitution zugrunde liegt
- → [[Stammfunktionen|Stammfunktionen]] – Grundlage der unbestimmten Integration
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Grenzenanpassung bei Substitution
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Häufige Anwendung der Substitution

> [!warning] **Prüfungsrelevant**
> - Die Substitution ist die **zentrale Integrationstechnik** im Abitur
> - Achte bei bestimmten Integralen **immer** auf die Grenzenanpassung
> - Vergiss nicht die **Rücksubstitution** bei unbestimmten Integralen
> - Die logarithmische Integration $\int \frac{f'(x)}{f(x)} \, dx = \ln|f(x)| + C$ wird häufig geprüft

> [!question] **Typische Prüfungsfragen**
> - Berechne das Integral $\int \sin(2x) \cdot \cos(2x) \, dx$ durch Substitution.
> - Bestimme $\int_1^e \frac{\ln x}{x} \, dx$ mit geeigneter Substitution.
> - Warum muss man bei bestimmten Integralen die Grenzen anpassen? Was passiert, wenn man die Rücksubstitution vergisst?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Partielle-Integration|Partielle Integration]] – Die zweite wichtige Integrationstechnik
> - [[Grundlegende-Integrationsregeln|Grundlegende Integrationsregeln]] – Basiswissen zur Integration
