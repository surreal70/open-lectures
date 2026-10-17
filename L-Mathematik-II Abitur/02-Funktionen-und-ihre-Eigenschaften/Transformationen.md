---
author: Andreas Hümmer
title: Transformationen
tags:
  - content
  - mathe
  - funktionen
  - transformationen
  - verschiebung
  - streckung
created: 2025-01-22
modified: 2025-01-22
---

# Transformationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die vier Grundtransformationen (Verschiebung, Streckung in x- und y-Richtung) verstehen und anwenden können
> - Aus einem Grundgraphen transformierte Graphen konstruieren können
> - Transformationsparameter aus gegebenen Graphen ablesen können
> - Mehrere Transformationen korrekt kombinieren können

---

## Überblick

**Transformationen** verändern den Graphen einer Funktion durch Verschiebungen, Streckungen, Stauchungen oder Spiegelungen. Das Verständnis dieser Operationen ermöglicht es, aus wenigen Grundfunktionen eine Vielzahl von Funktionen abzuleiten und ihre Graphen schnell zu skizzieren.

## Die vier Grundtransformationen

### Übersicht

Ausgehend von einer Funktion $f(x)$ erhält man durch Parameter $a$, $b$, $c$, $d$:

$$g(x) = a \cdot f(b(x - c)) + d$$

| Parameter | Transformation | Richtung |
|-----------|----------------|----------|
| $d$ | Verschiebung | vertikal ($y$-Richtung) |
| $c$ | Verschiebung | horizontal ($x$-Richtung) |
| $a$ | Streckung/Stauchung | vertikal ($y$-Richtung) |
| $b$ | Streckung/Stauchung | horizontal ($x$-Richtung) |

## Verschiebungen

### Vertikale Verschiebung

$$g(x) = f(x) + d$$

- $d > 0$: Verschiebung um $d$ Einheiten nach **oben**
- $d < 0$: Verschiebung um $|d|$ Einheiten nach **unten**

**Beispiel:** $f(x) = x^2$, $g(x) = x^2 + 3$

Der Graph wird um 3 Einheiten nach oben verschoben.

### Horizontale Verschiebung

$$g(x) = f(x - c)$$

- $c > 0$: Verschiebung um $c$ Einheiten nach **rechts**
- $c < 0$: Verschiebung um $|c|$ Einheiten nach **links**

**Achtung:** Das Vorzeichen wirkt „umgekehrt"!

**Beispiel:** $f(x) = x^2$, $g(x) = (x-2)^2$

Der Graph wird um 2 Einheiten nach **rechts** verschoben (nicht nach links!).

**Merkregel:** Bei $f(x - c)$ steht der Scheitelpunkt bei $x = c$.

## Streckungen und Stauchungen

### Vertikale Streckung/Stauchung

$$g(x) = a \cdot f(x)$$

- $|a| > 1$: Streckung (Graph wird „steiler")
- $0 < |a| < 1$: Stauchung (Graph wird „flacher")
- $a < 0$: zusätzliche Spiegelung an der $x$-Achse

**Beispiel:** $f(x) = x^2$
- $g(x) = 2x^2$: vertikal gestreckt (Faktor 2)
- $h(x) = 0.5x^2$: vertikal gestaucht (Faktor 0.5)
- $k(x) = -x^2$: an $x$-Achse gespiegelt

### Horizontale Streckung/Stauchung

$$g(x) = f(bx)$$

- $|b| > 1$: Stauchung (Graph wird „schmaler")
- $0 < |b| < 1$: Streckung (Graph wird „breiter")
- $b < 0$: zusätzliche Spiegelung an der $y$-Achse

**Achtung:** Auch hier wirkt der Faktor „umgekehrt"!

**Beispiel:** $f(x) = \sin(x)$
- $g(x) = \sin(2x)$: horizontal gestaucht → Periode halbiert
- $h(x) = \sin(\frac{x}{2})$: horizontal gestreckt → Periode verdoppelt

## Spiegelungen

### Spiegelung an der x-Achse

$$g(x) = -f(x)$$

Jeder Punkt $(x, y)$ wird auf $(x, -y)$ abgebildet.

### Spiegelung an der y-Achse

$$g(x) = f(-x)$$

Jeder Punkt $(x, y)$ wird auf $(-x, y)$ abgebildet.

### Spiegelung am Ursprung

$$g(x) = -f(-x)$$

Kombination beider Spiegelungen. Jeder Punkt $(x, y)$ wird auf $(-x, -y)$ abgebildet.

## Kombinierte Transformationen

### Allgemeine Form

$$g(x) = a \cdot f(b(x - c)) + d$$

**Reihenfolge der Anwendung** (von innen nach außen):
1. Horizontale Verschiebung um $c$
2. Horizontale Streckung mit Faktor $\frac{1}{|b|}$ (und evtl. Spiegelung)
3. Vertikale Streckung mit Faktor $|a|$ (und evtl. Spiegelung)
4. Vertikale Verschiebung um $d$

### Beispiel: Quadratische Funktion

$$g(x) = 2(x-1)^2 + 3$$

Ausgehend von $f(x) = x^2$:
1. Verschiebung um 1 nach rechts: $(x-1)^2$
2. Vertikale Streckung um Faktor 2: $2(x-1)^2$
3. Verschiebung um 3 nach oben: $2(x-1)^2 + 3$

**Scheitelpunkt:** $(1, 3)$

### Beispiel: Sinusfunktion

$$g(x) = 3\sin(2(x - \frac{\pi}{4})) + 1$$

Ausgehend von $f(x) = \sin(x)$:
- Amplitude: $|a| = 3$
- Periode: $T = \frac{2\pi}{|b|} = \frac{2\pi}{2} = \pi$
- Phasenverschiebung: $c = \frac{\pi}{4}$ nach rechts
- Vertikale Verschiebung: $d = 1$ nach oben

## Auswirkungen auf Definitions- und Wertebereich

### Definitionsbereich

Für $g(x) = f(b(x-c))$ mit $D_f$ als Definitionsbereich von $f$:

$$D_g = \{x \mid b(x-c) \in D_f\} = \frac{1}{b}D_f + c$$

**Beispiel:** $f(x) = \sqrt{x}$ mit $D_f = [0, \infty)$

$g(x) = \sqrt{2(x-3)}$

Bedingung: $2(x-3) \geq 0 \Leftrightarrow x \geq 3$

Also: $D_g = [3, \infty)$

### Wertebereich

Für $g(x) = a \cdot f(\ldots) + d$ mit $W_f$ als Wertebereich von $f$:

$$W_g = a \cdot W_f + d$$

**Beispiel:** $f(x) = \sin(x)$ mit $W_f = [-1, 1]$

$g(x) = 2\sin(x) + 3$

$W_g = 2 \cdot [-1, 1] + 3 = [-2, 2] + 3 = [1, 5]$

## Transformation und Funktionseigenschaften

| Eigenschaft | Erhaltung bei Transformation |
|------------|------------------------------|
| Nullstellen | Verschieben sich mit dem Graphen |
| Extrema | Verschieben sich, Werte skalieren |
| Monotonie | Bleibt erhalten (außer bei Spiegelung) |
| Symmetrie | Kann sich ändern |
| Periodizität | Periode ändert sich bei horizontaler Streckung |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Verkettung-von-Funktionen]] – Transformationen als Verkettung mit linearen Funktionen
- → [[Quadratische-Funktionen]] – Scheitelpunktform als Transformation von $x^2$
- → [[Periodizitaet]] – Änderung der Periode durch horizontale Streckung
- → [[Symmetrie]] – Spiegelungen und Symmetrieeigenschaften

> [!warning] **Prüfungsrelevant**
> - Alle vier Grundtransformationen mit korrekten Vorzeichen
> - Ableitung von Transformationsparametern aus Graphen
> - Scheitelpunktform quadratischer Funktionen
> - Amplitude, Periode und Phasenverschiebung bei trigonometrischen Funktionen

> [!question] **Typische Prüfungsfragen**
> - Beschreibe die Transformationen, die $f(x) = x^2$ in $g(x) = -2(x+1)^2 + 4$ überführen.
> - Gib die Funktion an, deren Graph aus dem Graphen von $f(x) = e^x$ durch Spiegelung an der $y$-Achse und Verschiebung um 2 nach oben entsteht.
> - Bestimme Amplitude, Periode und Phasenverschiebung von $f(x) = 4\cos(3x - \pi)$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Funktionen]] – Transformierte Sinus- und Kosinusfunktionen
> - [[Exponentialfunktionen]] – Wachstums- und Zerfallsprozesse
> - [[Parameterabhaengige-Funktionen]] – Parameter als Transformationsgrößen
