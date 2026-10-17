---
author: Andreas Hümmer
title: Vergleich verschiedener Funktionstypen
tags:
  - content
  - mathe
  - funktionen
  - uebersicht
  - vergleich
created: 2025-06-19
modified: 2025-06-19
---

# Vergleich verschiedener Funktionstypen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Funktionstypen anhand ihrer charakteristischen Eigenschaften erkennen können
> - Das Wachstumsverhalten verschiedener Funktionsklassen vergleichen können
> - Geeignete Funktionstypen für Modellierungsaufgaben auswählen können
> - Systematisch die Eigenschaften einer unbekannten Funktion analysieren können

---

## Überblick

Dieses Kapitel bietet eine systematische Gegenüberstellung aller behandelten Funktionstypen. Das Erkennen des Funktionstyps ist oft der erste Schritt bei der Analyse eines Problems. Die Wahl des richtigen Modells — ob linear, exponentiell oder periodisch — bestimmt maßgeblich die Qualität einer mathematischen Beschreibung realer Phänomene.

## Klassifikation nach algebraischer Struktur

### Algebraische Funktionen

Funktionen, die durch endlich viele algebraische Operationen (Addition, Subtraktion, Multiplikation, Division, Wurzelziehen) aus der Variablen $x$ gebildet werden:

| Typ | Form | Beispiel |
|-----|------|----------|
| [[Lineare-Funktionen\|Linear]] | $ax + b$ | $f(x) = 2x - 3$ |
| [[Quadratische-Funktionen\|Quadratisch]] | $ax^2 + bx + c$ | $f(x) = x^2 - 4x + 3$ |
| [[Polynomfunktionen\|Polynome]] | $\sum a_k x^k$ | $f(x) = x^3 - 2x$ |
| [[Gebrochenrationale-Funktionen\|Gebrochenrational]] | $\frac{p(x)}{q(x)}$ | $f(x) = \frac{x+1}{x-2}$ |
| [[Potenzfunktionen\|Potenz]] | $x^n$ | $f(x) = x^{-2}$ |
| [[Wurzelfunktionen\|Wurzel]] | $\sqrt[n]{x}$ | $f(x) = \sqrt{x+1}$ |

### Transzendente Funktionen

Funktionen, die nicht durch endlich viele algebraische Operationen darstellbar sind:

| Typ | Form | Beispiel |
|-----|------|----------|
| [[Exponentialfunktionen\|Exponentiell]] | $a^x$ | $f(x) = e^{2x}$ |
| [[Logarithmusfunktionen\|Logarithmisch]] | $\log_a(x)$ | $f(x) = \ln(x+1)$ |
| [[Trigonometrische-Funktionen\|Trigonometrisch]] | $\sin, \cos, \tan$ | $f(x) = 2\sin(3x)$ |
| [[Umkehrtrigonometrische-Funktionen\|Arkusfunktionen]] | $\arcsin, \arccos, \arctan$ | $f(x) = \arctan(x)$ |

## Vergleich der Definitionsbereiche

| Funktionstyp | Definitionsbereich | Einschränkungen |
|--------------|-------------------|-----------------|
| Polynome | $\mathbb{R}$ | keine |
| Gebrochenrational | $\mathbb{R} \setminus \{x \mid q(x) = 0\}$ | Nenner ≠ 0 |
| Wurzeln (gerade) | $[0, +\infty)$ oder Teilmenge | Radikand ≥ 0 |
| Logarithmus | $(0, +\infty)$ | Argument > 0 |
| Arkussinus/-kosinus | $[-1, 1]$ | $\|x\| \leq 1$ |
| Exponentiell | $\mathbb{R}$ | keine |
| Trigonometrisch | $\mathbb{R}$ (meist) | tan: $\cos x \neq 0$ |

## Vergleich der Wertebereiche

| Funktionstyp | Wertebereich | Beschränkung |
|--------------|--------------|--------------|
| Linear ($m \neq 0$) | $\mathbb{R}$ | unbeschränkt |
| Quadratisch ($a > 0$) | $[y_S, +\infty)$ | nach unten beschränkt |
| Exponentiell | $(0, +\infty)$ | positiv |
| Logarithmus | $\mathbb{R}$ | unbeschränkt |
| Sinus/Kosinus | $[-1, 1]$ | beschränkt |
| Arkustangens | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ | beschränkt |

## Wachstumsverhalten für $x \to +\infty$

### Wachstumshierarchie

Für $x \to +\infty$ gilt die Ordnung:

$$\ln(x) \ll x^a \ll b^x \ll x! \ll x^x$$

(mit $a > 0$ und $b > 1$)

Das bedeutet:

$$\lim_{x \to \infty} \frac{\ln(x)}{x^a} = 0, \quad \lim_{x \to \infty} \frac{x^a}{b^x} = 0$$

### Vergleichstabelle für $x = 10$

| Funktion | $f(10)$ | Wachstumstyp |
|----------|---------|--------------|
| $\ln(x)$ | $2{,}3$ | logarithmisch (langsam) |
| $\sqrt{x}$ | $3{,}2$ | sublinear |
| $x$ | $10$ | linear |
| $x^2$ | $100$ | polynomial |
| $2^x$ | $1024$ | exponentiell |
| $e^x$ | $\approx 22000$ | exponentiell |
| $10^x$ | $10^{10}$ | exponentiell (schnell) |

## Symmetrieverhalten

| Funktionstyp | Symmetrie | Bedingung |
|--------------|-----------|-----------|
| Polynome | Achsensymmetrie | nur gerade Exponenten |
| Polynome | Punktsymmetrie | nur ungerade Exponenten |
| Potenzfunktion $x^n$ | Achsensymmetrie | $n$ gerade |
| Potenzfunktion $x^n$ | Punktsymmetrie | $n$ ungerade |
| $\sin(x)$ | Punktsymmetrie | — |
| $\cos(x)$ | Achsensymmetrie | — |
| $e^x$ | keine | — |
| $\|x\|$ | Achsensymmetrie | — |

## Monotonieverhalten

| Funktionstyp | Monotonie | Bemerkung |
|--------------|-----------|-----------|
| Linear ($m > 0$) | streng steigend | auf ganz $\mathbb{R}$ |
| Exponentiell ($a > 1$) | streng steigend | auf ganz $\mathbb{R}$ |
| Logarithmus | streng steigend | auf $(0, +\infty)$ |
| Arkustangens | streng steigend | auf ganz $\mathbb{R}$ |
| Quadratisch | wechselnd | Minimum/Maximum |
| Trigonometrisch | wechselnd | periodisch |

## Asymptotisches Verhalten

### Funktionen mit Asymptoten

| Funktionstyp | Asymptote | Beispiel |
|--------------|-----------|----------|
| Exponentiell $e^x$ | $y = 0$ (horizontal) | für $x \to -\infty$ |
| Logarithmus $\ln(x)$ | $x = 0$ (vertikal) | für $x \to 0^+$ |
| Gebrochenrational | horizontal, vertikal, schief | je nach Grad |
| Arkustangens | $y = \pm\frac{\pi}{2}$ | für $x \to \pm\infty$ |
| $\frac{1}{x}$ | $x = 0$, $y = 0$ | Hyperbel |

### Funktionen ohne Asymptoten

- Polynome (außer konstanten)
- Trigonometrische Funktionen
- Wurzelfunktionen

## Periodizität

| Funktionstyp | Periode | Bemerkung |
|--------------|---------|-----------|
| $\sin(x)$, $\cos(x)$ | $2\pi$ | Grundperiode |
| $\tan(x)$, $\cot(x)$ | $\pi$ | Grundperiode |
| $\sin(bx)$ | $\frac{2\pi}{b}$ | transformiert |
| Polynome, Exponential-, Logarithmusfunktionen | keine | aperiodisch |

## Entscheidungskriterien für die Modellierung

### Wann welchen Funktionstyp wählen?

| Phänomen | Geeigneter Funktionstyp |
|----------|------------------------|
| Konstante Änderungsrate | Linear |
| Beschleunigung, Bremsen, Wurf | Quadratisch |
| Prozentuales Wachstum/Zerfall | Exponentiell |
| Sättigung, begrenztes Wachstum | $f(t) = S - ae^{-kt}$ |
| Schwingungen, Wellen | Trigonometrisch |
| Reaktionszeit, Lernkurven | Logarithmisch |
| Physikalische Gesetze | Potenzfunktionen |

### Erkennungsmerkmale aus Daten

| Muster in Wertetabelle | Funktionstyp |
|------------------------|--------------|
| Konstante Differenzen | Linear |
| Konstante Quotienten | Exponentiell |
| Konstante zweite Differenzen | Quadratisch |
| Oszillation | Trigonometrisch |

## Checkliste zur Funktionsanalyse

1. **Definitionsbereich** bestimmen (Nenner ≠ 0, Radikand ≥ 0, log-Argument > 0)
2. **Symmetrie** prüfen: $f(-x) = f(x)$? oder $f(-x) = -f(x)$?
3. **Nullstellen** berechnen
4. **Extrema** und **Wendepunkte** (mit Differentialrechnung)
5. **Verhalten für $x \to \pm\infty$** (Asymptoten, Grenzwerte)
6. **Wertebereich** ableiten
7. **Graph** skizzieren

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-des-Funktionsbegriffs]] — Grundlegende Definitionen
- → [[Transformationen]] — Einheitliche Transformationsregeln
- → [[Grenzwerte-von-Funktionen]] — Asymptotisches Verhalten
- → [[05-Differentialrechnung-I|Differentialrechnung]] — Kurvendiskussion
- → [[16-Mathematische-Modellierung-und-Abschlussprojekt|Modellierung]] — Anwendungen

> [!warning] **Prüfungsrelevant**
> - Zuordnung von Graphen zu Funktionsgleichungen
> - Erkennen des Funktionstyps aus Wertetabellen
> - Wachstumshierarchie: Logarithmus < Potenz < Exponential
> - Definitionsbereiche verschiedener Funktionstypen
> - Auswahl geeigneter Modelle für Sachkontexte
> - Systematische Kurvendiskussion mit allen Eigenschaften

> [!question] **Typische Prüfungsfragen**
> - Ordnen Sie die gegebenen Graphen den Funktionsgleichungen zu und begründen Sie Ihre Wahl.
> - Eine Größe verdoppelt sich alle 5 Minuten. Welcher Funktionstyp beschreibt dies? Stellen Sie die Funktionsgleichung auf.
> - Vergleichen Sie das Wachstumsverhalten von $f(x) = x^3$ und $g(x) = 2^x$ für große $x$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Abiturprüfungsaufgaben Mathematik*, verschiedene Jahrgänge

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] — Systematische Kurvendiskussion
> - [[16-Mathematische-Modellierung-und-Abschlussprojekt|Modellierungsprojekt]] — Praktische Anwendungen

