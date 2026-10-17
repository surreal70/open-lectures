---
author: Andreas Hümmer
title: Höhere Ableitungen
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitungen
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Höhere Ableitungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Höhere Ableitungen einer Funktion berechnen können
> - Die Notation für höhere Ableitungen sicher verwenden
> - Die physikalische Bedeutung höherer Ableitungen verstehen
> - Höhere Ableitungen bei der Analyse von Funktionen anwenden können

---

## Überblick

Bei der Untersuchung von Funktionen reicht die erste Ableitung oft nicht aus, um alle wichtigen Eigenschaften zu erfassen. Die **höheren Ableitungen** – also die Ableitungen der Ableitung – liefern zusätzliche Informationen über das Verhalten einer Funktion. Besonders die zweite Ableitung spielt eine zentrale Rolle bei der Bestimmung von Krümmungseigenschaften und Wendepunkten.

## Definition höherer Ableitungen

Die **n-te Ableitung** einer Funktion $f$ entsteht durch wiederholtes Ableiten:

$$f'(x) = \frac{df}{dx} \quad \text{(erste Ableitung)}$$

$$f''(x) = \frac{d^2f}{dx^2} = \frac{d}{dx}\left(\frac{df}{dx}\right) \quad \text{(zweite Ableitung)}$$

$$f'''(x) = \frac{d^3f}{dx^3} \quad \text{(dritte Ableitung)}$$

Für $n \geq 4$ schreibt man üblicherweise:

$$f^{(n)}(x) = \frac{d^nf}{dx^n} \quad \text{(n-te Ableitung)}$$

### Notationen im Überblick

| Ableitung | Leibniz-Notation | Lagrange-Notation |
|-----------|------------------|-------------------|
| Erste | $\frac{df}{dx}$ | $f'(x)$ |
| Zweite | $\frac{d^2f}{dx^2}$ | $f''(x)$ |
| Dritte | $\frac{d^3f}{dx^3}$ | $f'''(x)$ |
| n-te | $\frac{d^nf}{dx^n}$ | $f^{(n)}(x)$ |

## Berechnung höherer Ableitungen

### Beispiel 1: Polynomfunktion

Gegeben: $f(x) = x^4 - 3x^3 + 2x^2 - 5x + 1$

Sukzessives Ableiten ergibt:

$$f'(x) = 4x^3 - 9x^2 + 4x - 5$$

$$f''(x) = 12x^2 - 18x + 4$$

$$f'''(x) = 24x - 18$$

$$f^{(4)}(x) = 24$$

$$f^{(5)}(x) = 0$$

Bei Polynomen vom Grad $n$ gilt stets: $f^{(n+1)}(x) = 0$.

### Beispiel 2: Exponentialfunktion

Die e-Funktion hat die besondere Eigenschaft, dass sie gleich ihrer Ableitung ist:

$$f(x) = e^x \implies f'(x) = e^x \implies f''(x) = e^x \implies f^{(n)}(x) = e^x$$

Für $f(x) = e^{ax}$ gilt:

$$f^{(n)}(x) = a^n \cdot e^{ax}$$

### Beispiel 3: Trigonometrische Funktionen

Für $f(x) = \sin(x)$:

$$f'(x) = \cos(x)$$
$$f''(x) = -\sin(x)$$
$$f'''(x) = -\cos(x)$$
$$f^{(4)}(x) = \sin(x) = f(x)$$

Die Ableitungen wiederholen sich mit Periode 4.

## Physikalische Interpretation

In der Physik haben höhere Ableitungen konkrete Bedeutungen, wenn $s(t)$ den Ort eines Körpers zur Zeit $t$ beschreibt:

| Ableitung | Symbol | Physikalische Größe |
|-----------|--------|---------------------|
| $s(t)$ | – | Ort (Position) |
| $s'(t)$ | $v(t)$ | Geschwindigkeit |
| $s''(t)$ | $a(t)$ | Beschleunigung |
| $s'''(t)$ | $j(t)$ | Ruck (jerk) |

**Beispiel:** Freier Fall ohne Luftwiderstand

$$s(t) = \frac{1}{2}gt^2$$

$$v(t) = s'(t) = gt$$

$$a(t) = s''(t) = g \approx 9{,}81 \, \frac{\text{m}}{\text{s}^2}$$

Die konstante zweite Ableitung zeigt die gleichmäßige Beschleunigung.

## Anwendung: Krümmung und Wendepunkte

Die zweite Ableitung gibt Auskunft über die **Krümmung** einer Funktion:

- $f''(x) > 0$: Funktion ist linksgekrümmt (konvex, nach oben geöffnet)
- $f''(x) < 0$: Funktion ist rechtsgekrümmt (konkav, nach unten geöffnet)
- $f''(x) = 0$: Möglicher Wendepunkt

**Beispiel:** Für $f(x) = x^3 - 3x$ ist $f''(x) = 6x$

- Für $x < 0$: $f''(x) < 0$ → rechtsgekrümmt
- Für $x > 0$: $f''(x) > 0$ → linksgekrümmt
- Bei $x = 0$: Vorzeichenwechsel von $f''$ → Wendepunkt

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln]] – Grundlagen für die Berechnung
- → [[Kruemmungsverhalten]] – Interpretation der zweiten Ableitung
- → [[Wendepunkte]] – Bestimmung von Wendestellen
- → [[Vollstaendige-Kurvendiskussion]] – Einbettung in die Funktionsanalyse
- → [[Anwendungen-in-Physik-und-Technik]] – Physikalische Anwendungen

> [!warning] **Prüfungsrelevant**
> - Bei Polynomen vom Grad $n$ verschwindet die $(n+1)$-te Ableitung
> - Die zweite Ableitung bestimmt das Krümmungsverhalten
> - Physikalische Interpretation: Ort → Geschwindigkeit → Beschleunigung
> - Die n-te Ableitung von $e^{ax}$ ist $a^n \cdot e^{ax}$

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie $f''(x)$ und $f'''(x)$ für eine gegebene Funktion
> - Interpretieren Sie die zweite Ableitung einer Weg-Zeit-Funktion physikalisch
> - An welchen Stellen ist die Funktion links- bzw. rechtsgekrümmt?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Kruemmungsverhalten]] – Vertiefung der Krümmungsanalyse
> - [[Anwendungen-in-Physik-und-Technik]] – Praktische Anwendungsbeispiele
