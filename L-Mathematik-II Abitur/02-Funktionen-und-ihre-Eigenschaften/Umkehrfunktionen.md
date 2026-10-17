---
author: Andreas Hümmer
title: Umkehrfunktionen
tags:
  - content
  - mathe
  - funktionen
  - umkehrfunktion
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Umkehrfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Bedingungen für die Existenz einer Umkehrfunktion kennen
> - Umkehrfunktionen analytisch bestimmen können
> - Den Zusammenhang zwischen Funktion und Umkehrfunktion graphisch verstehen
> - Definitions- und Wertebereich bei der Umkehrung korrekt vertauschen können

---

## Überblick

Die **Umkehrfunktion** kehrt die Zuordnung einer Funktion um: Aus $y = f(x)$ wird $x = f^{-1}(y)$. Umkehrfunktionen spielen eine zentrale Rolle in der Analysis, etwa beim Lösen von Gleichungen, bei Integrationstechniken und in der Definition wichtiger Funktionen wie Logarithmus und Arkusfunktionen.

## Existenzbedingungen

### Notwendige Voraussetzung: Injektivität

Eine Funktion $f: D_f \to W_f$ besitzt genau dann eine Umkehrfunktion, wenn sie **injektiv** (eineindeutig) ist:

$$f(x_1) = f(x_2) \quad \Rightarrow \quad x_1 = x_2$$

### Strenge Monotonie als hinreichende Bedingung

Eine **streng monotone** Funktion ist stets injektiv und besitzt daher eine Umkehrfunktion.

**Wichtig:** Nicht jede injektive Funktion ist streng monoton (z.B. diskrete Funktionen), aber für stetige Funktionen auf Intervallen gilt die Äquivalenz.

### Einschränkung des Definitionsbereichs

Ist eine Funktion nicht injektiv, kann man durch Einschränkung des Definitionsbereichs Injektivität erreichen.

**Beispiel:** $f(x) = x^2$ auf $\mathbb{R}$

- Nicht injektiv, da $f(-2) = f(2) = 4$
- Eingeschränkt auf $[0, \infty)$: streng monoton wachsend → umkehrbar
- Die Umkehrfunktion ist $f^{-1}(x) = \sqrt{x}$

## Definition der Umkehrfunktion

### Formale Definition

Sei $f: D_f \to W_f$ eine bijektive Funktion. Die **Umkehrfunktion** $f^{-1}: W_f \to D_f$ ist definiert durch:

$$f^{-1}(y) = x \quad \Leftrightarrow \quad f(x) = y$$

### Eigenschaften

Für $f$ und $f^{-1}$ gilt:

$$f^{-1}(f(x)) = x \quad \text{für alle } x \in D_f$$
$$f(f^{-1}(y)) = y \quad \text{für alle } y \in W_f$$

### Vertauschung von Definition und Wertebereich

| Funktion | Definitionsbereich | Wertebereich |
|----------|-------------------|--------------|
| $f$ | $D_f$ | $W_f$ |
| $f^{-1}$ | $W_f$ | $D_f$ |

## Bestimmung der Umkehrfunktion

### Algorithmisches Vorgehen

1. **Prüfe Injektivität:** Ist $f$ streng monoton?
2. **Gleichung aufstellen:** $y = f(x)$
3. **Nach $x$ auflösen:** Isoliere $x$
4. **Variablen tauschen:** Ersetze $x \leftrightarrow y$
5. **Definitionsbereich angeben:** $D_{f^{-1}} = W_f$

### Beispiel 1: Lineare Funktion

$$f(x) = 2x + 3$$

**Schritt 1:** Linear mit Steigung $\neq 0$ → streng monoton → umkehrbar

**Schritt 2-3:**
$$y = 2x + 3$$
$$y - 3 = 2x$$
$$x = \frac{y-3}{2}$$

**Schritt 4-5:**
$$f^{-1}(x) = \frac{x-3}{2}$$
$$D_{f^{-1}} = \mathbb{R}$$

### Beispiel 2: Exponentialfunktion

$$f(x) = e^x, \quad D_f = \mathbb{R}, \quad W_f = (0, \infty)$$

**Auflösen:**
$$y = e^x$$
$$x = \ln(y)$$

**Umkehrfunktion:**
$$f^{-1}(x) = \ln(x), \quad D_{f^{-1}} = (0, \infty)$$

### Beispiel 3: Rationale Funktion

$$f(x) = \frac{x+1}{x-1}, \quad D_f = \mathbb{R} \setminus \{1\}$$

**Auflösen:**
$$y = \frac{x+1}{x-1}$$
$$y(x-1) = x+1$$
$$xy - y = x + 1$$
$$xy - x = y + 1$$
$$x(y-1) = y + 1$$
$$x = \frac{y+1}{y-1}$$

**Umkehrfunktion:**
$$f^{-1}(x) = \frac{x+1}{x-1}$$

Interessanterweise ist $f = f^{-1}$! Diese Funktion ist ihre eigene Umkehrfunktion (**Involution**).

## Graphische Darstellung

### Spiegelung an der Winkelhalbierenden

Der Graph von $f^{-1}$ entsteht durch **Spiegelung** des Graphen von $f$ an der Geraden $y = x$ (erste Winkelhalbierende).

**Begründung:** Wenn $(a, b)$ auf dem Graphen von $f$ liegt (d.h. $f(a) = b$), dann liegt $(b, a)$ auf dem Graphen von $f^{-1}$ (d.h. $f^{-1}(b) = a$).

### Skizze (ASCII-Darstellung)

```
    y
    |      /  <- y = x
    |    /   ___/ f(x)
    |  /  __/
    | /__/
    |/
----+--------------> x
   /|
  / |   f^(-1)(x)
 /  |
```

## Wichtige Umkehrfunktionen

| Funktion $f$ | Einschränkung | Umkehrfunktion $f^{-1}$ |
|-------------|---------------|------------------------|
| $f(x) = x^2$ | $[0, \infty)$ | $f^{-1}(x) = \sqrt{x}$ |
| $f(x) = x^3$ | $\mathbb{R}$ | $f^{-1}(x) = \sqrt[3]{x}$ |
| $f(x) = e^x$ | $\mathbb{R}$ | $f^{-1}(x) = \ln(x)$ |
| $f(x) = a^x$ | $\mathbb{R}$ | $f^{-1}(x) = \log_a(x)$ |
| $f(x) = \sin(x)$ | $[-\frac{\pi}{2}, \frac{\pi}{2}]$ | $f^{-1}(x) = \arcsin(x)$ |
| $f(x) = \cos(x)$ | $[0, \pi]$ | $f^{-1}(x) = \arccos(x)$ |
| $f(x) = \tan(x)$ | $(-\frac{\pi}{2}, \frac{\pi}{2})$ | $f^{-1}(x) = \arctan(x)$ |

## Ableitung der Umkehrfunktion

Für differenzierbare, streng monotone Funktionen gilt:

$$(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}$$

Oder in der üblichen Schreibweise mit $x$:

$$(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$$

**Beispiel:** Für $f(x) = e^x$ mit $f^{-1}(x) = \ln(x)$:

$$(\ln x)' = \frac{1}{e^{\ln x}} = \frac{1}{x}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-des-Funktionsbegriffs]] – Injektivität, Surjektivität, Bijektivität
- → [[Monotonie]] – Strenge Monotonie garantiert Umkehrbarkeit
- → [[Logarithmusfunktionen]] – Umkehrfunktion der Exponentialfunktion
- → [[Umkehrtrigonometrische-Funktionen]] – Arkusfunktionen

> [!warning] **Prüfungsrelevant**
> - Bedingungen für die Existenz der Umkehrfunktion
> - Analytisches Bestimmen von Umkehrfunktionen
> - Korrektes Vertauschen von Definitions- und Wertebereich
> - Graphische Konstruktion durch Spiegelung an $y = x$

> [!question] **Typische Prüfungsfragen**
> - Bestimme die Umkehrfunktion von $f(x) = \frac{2x-1}{x+3}$ und gib ihren Definitionsbereich an.
> - Warum muss der Definitionsbereich von $f(x) = \cos(x)$ eingeschränkt werden, um eine Umkehrfunktion zu erhalten?
> - Zeige graphisch, dass $f(x) = x^3 + x$ eine Umkehrfunktion besitzt.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Verkettung-von-Funktionen]] – Umkehrfunktion als inverse Verkettung
> - [[05-Differentialrechnung-I|Differentialrechnung I]] – Ableitung der Umkehrfunktion
> - [[Exponentialfunktionen]] – $e^x$ und $\ln(x)$ als Umkehrpaar
