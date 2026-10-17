---
author: Andreas Hümmer
title: Fakultäten
tags:
  - content
  - mathe
  - kombinatorik
  - fakultaet
  - zaehlen
created: 2025-07-01
modified: 2025-07-01
---

# Fakultäten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Fakultät definieren und berechnen können
> - Den kombinatorischen Hintergrund der Fakultät verstehen
> - Fakultäten in praktischen Anwendungen einsetzen können
> - Rechenregeln für Fakultäten kennen und anwenden

---

## Überblick

Die Fakultät ist eine fundamentale Funktion in der Kombinatorik, die angibt, auf wie viele verschiedene Arten man $n$ unterscheidbare Objekte anordnen kann. Sie bildet die Grundlage für die Berechnung von Permutationen, Variationen und Kombinationen und ist damit ein unverzichtbares Werkzeug für die Wahrscheinlichkeitsrechnung.

## Definition der Fakultät

Die **Fakultät** einer natürlichen Zahl $n$ wird mit $n!$ (gesprochen: „n Fakultät") bezeichnet und ist definiert als:

$$n! = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 2 \cdot 1 = \prod_{k=1}^{n} k$$

### Beispiele

| $n$ | Berechnung | $n!$ |
|-----|------------|------|
| 1 | $1$ | 1 |
| 2 | $2 \cdot 1$ | 2 |
| 3 | $3 \cdot 2 \cdot 1$ | 6 |
| 4 | $4 \cdot 3 \cdot 2 \cdot 1$ | 24 |
| 5 | $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$ | 120 |
| 6 | $6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$ | 720 |
| 10 | $10 \cdot 9 \cdot \ldots \cdot 1$ | 3.628.800 |

### Die Fakultät von Null

Per Definition gilt:
$$0! = 1$$

Diese Festlegung ist sinnvoll, weil:
1. Es gibt genau **eine** Möglichkeit, null Objekte anzuordnen (nämlich die leere Anordnung)
2. Sie die Rekursionsformel $n! = n \cdot (n-1)!$ auch für $n = 1$ erfüllt
3. Der Binomialkoeffizient $\binom{n}{0} = \frac{n!}{0! \cdot n!} = 1$ korrekt bleibt

## Rekursive Definition

Die Fakultät kann auch rekursiv definiert werden:

$$n! = \begin{cases} 1 & \text{falls } n = 0 \\ n \cdot (n-1)! & \text{falls } n \geq 1 \end{cases}$$

### Beispiel

$$5! = 5 \cdot 4! = 5 \cdot 24 = 120$$

Diese rekursive Darstellung ist besonders nützlich für:
- Programmierung (rekursive Funktionen)
- Kürzen von Brüchen mit Fakultäten

## Wachstum der Fakultät

Die Fakultät wächst extrem schnell – schneller als jede Exponentialfunktion:

| $n$ | $n!$ | $2^n$ | $n^n$ |
|-----|------|-------|-------|
| 5 | 120 | 32 | 3.125 |
| 10 | 3.628.800 | 1.024 | 10.000.000.000 |
| 15 | $\approx 1{,}3 \cdot 10^{12}$ | 32.768 | $\approx 4{,}4 \cdot 10^{17}$ |
| 20 | $\approx 2{,}4 \cdot 10^{18}$ | $\approx 1 \cdot 10^6$ | $\approx 1 \cdot 10^{26}$ |

Für große $n$ gilt die **Stirling-Approximation**:
$$n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$$

## Rechenregeln für Fakultäten

### Kürzen von Quotienten

Viele Formeln in der Kombinatorik enthalten Quotienten von Fakultäten. Diese lassen sich oft elegant vereinfachen:

$$\frac{n!}{(n-k)!} = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n-k+1)$$

**Beispiel:**
$$\frac{10!}{7!} = \frac{10!}{7!} = 10 \cdot 9 \cdot 8 = 720$$

### Wichtige Umformungen

1. $\frac{n!}{n} = (n-1)!$

2. $(n+1)! = (n+1) \cdot n!$

3. $\frac{(n+k)!}{n!} = (n+k)(n+k-1) \cdot \ldots \cdot (n+1)$

## Der kombinatorische Hintergrund

### Anordnungsproblem

Die Fakultät $n!$ gibt die Anzahl der Möglichkeiten an, $n$ verschiedene Objekte in einer Reihe anzuordnen.

**Beispiel: Anordnung von 4 Büchern**

Wie viele Möglichkeiten gibt es, 4 verschiedene Bücher nebeneinander ins Regal zu stellen?

```
Position:    1.     2.     3.     4.
Auswahl:     4   ·  3   ·  2   ·  1  = 24 Möglichkeiten
```

- Für die 1. Position: 4 Bücher zur Auswahl
- Für die 2. Position: 3 Bücher zur Auswahl
- Für die 3. Position: 2 Bücher zur Auswahl
- Für die 4. Position: 1 Buch zur Auswahl

Also: $4! = 24$ verschiedene Anordnungen

### Allgemeine Überlegung

Bei $n$ verschiedenen Objekten:
- Für den 1. Platz gibt es $n$ Möglichkeiten
- Für den 2. Platz gibt es $n-1$ Möglichkeiten
- ...
- Für den $n$-ten Platz gibt es 1 Möglichkeit

Insgesamt: $n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1 = n!$

## Anwendungsbeispiele

### Beispiel 1: Sitzordnung

Auf wie viele Arten können sich 6 Personen an einer Reihe von 6 Stühlen setzen?

**Lösung:**
$$6! = 720 \text{ Möglichkeiten}$$

### Beispiel 2: Reihenfolge von Ereignissen

Ein Wettbewerb hat 8 Teilnehmer. Auf wie viele Arten können die ersten drei Plätze belegt werden?

**Lösung:**
$$\frac{8!}{5!} = 8 \cdot 7 \cdot 6 = 336 \text{ Möglichkeiten}$$

Oder direkt: $8 \cdot 7 \cdot 6 = 336$

### Beispiel 3: Passwörter

Wie viele verschiedene Passwörter aus genau 4 verschiedenen Ziffern (0-9) gibt es, wenn jede Ziffer nur einmal vorkommen darf?

**Lösung:**
$$\frac{10!}{6!} = 10 \cdot 9 \cdot 8 \cdot 7 = 5040 \text{ Möglichkeiten}$$

## Fakultät auf dem Taschenrechner

Die Fakultätsfunktion ist auf wissenschaftlichen Taschenrechnern meist über:
- Die Taste `n!` oder `x!` direkt verfügbar
- Oder über das Menü: `MATH` → `PRB` → `n!`

**Hinweis:** Die meisten Taschenrechner können Fakultäten nur bis etwa $n = 69$ exakt berechnen, da $70! > 10^{100}$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Permutationen]] — Anordnungen, die direkt auf Fakultäten basieren
- → [[Variationen]] — Verwenden Quotienten von Fakultäten
- → [[Binomialkoeffizienten]] — Sind durch Fakultäten definiert
- → [[Kombinationen]] — Nutzen Fakultäten in der Formel

> [!warning] **Prüfungsrelevant**
> - Sichere Berechnung von Fakultäten (auch $0! = 1$)
> - Kürzen von Quotienten wie $\frac{n!}{(n-k)!}$
> - Erkennen, wann ein Problem auf die Fakultät führt
> - Interpretation der Fakultät als Anzahl von Anordnungen

> [!question] **Typische Prüfungsfragen**
> - Berechne $\frac{12!}{9! \cdot 3!}$ ohne Taschenrechner.
> - Auf wie viele Arten können 5 Personen in einer Reihe aufgestellt werden?
> - Warum ist $0! = 1$ eine sinnvolle Definition?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium

> [!tip] **Weiterführende Links**
> - [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Grundlagen der Wahrscheinlichkeit
> - [[Permutationen]] — Direkte Anwendung der Fakultät
