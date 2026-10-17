---
author: Andreas Hümmer
title: Periodizität
tags:
  - content
  - mathe
  - funktionen
  - periodizitaet
  - analysis
created: 2025-01-22
modified: 2025-01-22
---

# Periodizität

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Periodizität formal definieren und anwenden können
> - Die Periode einer Funktion bestimmen können
> - Periodische Funktionen graphisch erkennen und analysieren können
> - Den Zusammenhang zwischen Periodizität und trigonometrischen Funktionen verstehen

---

## Überblick

Eine **periodische Funktion** wiederholt ihr Verhalten in regelmäßigen Abständen. Dieses Konzept ist fundamental für die Beschreibung von Schwingungen, Wellen und zyklischen Phänomenen in Natur und Technik. Die wichtigsten Beispiele sind die trigonometrischen Funktionen.

## Definition

### Formale Definition

Eine Funktion $f: D_f \to \mathbb{R}$ heißt **periodisch**, wenn es eine Zahl $p > 0$ gibt, sodass für alle $x \in D_f$ gilt:

$$f(x + p) = f(x)$$

und $x + p \in D_f$.

### Periode und Grundperiode

- Jede solche Zahl $p$ heißt **Periode** der Funktion.
- Die **kleinste positive** Periode heißt **Grundperiode** (oder primitive Periode) und wird meist mit $T$ oder $p$ bezeichnet.

**Wichtig:** Wenn $p$ eine Periode ist, dann sind auch $2p$, $3p$, ... und allgemein $np$ ($n \in \mathbb{N}$) Perioden.

### Geometrische Bedeutung

Der Graph einer periodischen Funktion kann durch Verschiebung um die Periode $p$ in $x$-Richtung mit sich selbst zur Deckung gebracht werden.

## Periodizität der trigonometrischen Funktionen

### Sinus und Kosinus

$$\sin(x + 2\pi) = \sin(x) \quad \text{für alle } x \in \mathbb{R}$$
$$\cos(x + 2\pi) = \cos(x) \quad \text{für alle } x \in \mathbb{R}$$

**Grundperiode:** $T = 2\pi$

### Tangens und Kotangens

$$\tan(x + \pi) = \tan(x)$$
$$\cot(x + \pi) = \cot(x)$$

**Grundperiode:** $T = \pi$

### Tabelle der Grundperioden

| Funktion | Grundperiode |
|----------|-------------|
| $\sin(x)$ | $2\pi$ |
| $\cos(x)$ | $2\pi$ |
| $\tan(x)$ | $\pi$ |
| $\cot(x)$ | $\pi$ |
| $\sin(kx)$ | $\frac{2\pi}{|k|}$ |
| $\cos(kx)$ | $\frac{2\pi}{|k|}$ |

## Bestimmung der Periode

### Bei transformierten trigonometrischen Funktionen

Für $f(x) = A \sin(Bx + C) + D$ oder $f(x) = A \cos(Bx + C) + D$ gilt:

$$\text{Periode } T = \frac{2\pi}{|B|}$$

**Beispiele:**

1. $f(x) = \sin(2x)$
   $$T = \frac{2\pi}{2} = \pi$$

2. $f(x) = \cos\left(\frac{x}{3}\right)$
   $$T = \frac{2\pi}{1/3} = 6\pi$$

3. $f(x) = 3\sin(4x - \pi) + 2$
   $$T = \frac{2\pi}{4} = \frac{\pi}{2}$$

### Nachweis der Periodizität

Um zu zeigen, dass eine Funktion die Periode $p$ hat, beweist man:
$$f(x + p) = f(x) \quad \text{für alle } x \in D_f$$

**Beispiel:** Zeige, dass $f(x) = \sin^2(x)$ die Periode $\pi$ hat.

$$f(x + \pi) = \sin^2(x + \pi) = (\sin(x + \pi))^2 = (-\sin(x))^2 = \sin^2(x) = f(x)$$

Also ist $\pi$ eine Periode. Es ist sogar die Grundperiode, da $\sin^2(x)$ bei $x = \frac{\pi}{2}$ bereits seinen Maximalwert erreicht.

## Nicht-periodische Funktionen

### Konstante Funktion

Die konstante Funktion $f(x) = c$ ist streng genommen periodisch mit **jeder** positiven Zahl als Periode. Sie hat daher keine Grundperiode.

### Polynome und Exponentialfunktionen

Funktionen wie $f(x) = x^2$, $f(x) = e^x$ oder $f(x) = \ln(x)$ sind **nicht periodisch**.

**Beweis für** $f(x) = x^2$:
Angenommen, es gäbe ein $p > 0$ mit $f(x+p) = f(x)$ für alle $x$.
$$(x+p)^2 = x^2$$
$$x^2 + 2px + p^2 = x^2$$
$$2px + p^2 = 0$$

Dies müsste für alle $x$ gelten, was für $p \neq 0$ unmöglich ist.

## Eigenschaften periodischer Funktionen

### Beschränktheit

Viele periodische Funktionen sind **beschränkt**, aber nicht alle.

**Beispiel einer unbeschränkten periodischen Funktion:**
$$f(x) = \tan(x)$$
ist periodisch mit $T = \pi$, aber unbeschränkt (hat Polstellen).

### Mittelwert

Der **Mittelwert** einer periodischen Funktion über eine Periode ist:

$$\bar{f} = \frac{1}{T} \int_a^{a+T} f(x) \, dx$$

Das Ergebnis ist unabhängig von $a$.

**Beispiel:** Mittelwert von $\sin(x)$ über eine Periode:
$$\bar{f} = \frac{1}{2\pi} \int_0^{2\pi} \sin(x) \, dx = \frac{1}{2\pi} \cdot 0 = 0$$

### Stammfunktion

Die Stammfunktion einer periodischen Funktion ist im Allgemeinen **nicht** periodisch.

**Beispiel:**
- $f(x) = \cos(x)$ ist periodisch
- $F(x) = \sin(x)$ ist ebenfalls periodisch

Aber:
- $g(x) = 1 + \cos(x)$ ist periodisch (Periode $2\pi$)
- $G(x) = x + \sin(x)$ ist **nicht** periodisch

## Anwendungen

### Schwingungen und Wellen

Die allgemeine harmonische Schwingung:
$$y(t) = A \sin(\omega t + \varphi)$$

mit:
- $A$: Amplitude
- $\omega$: Kreisfrequenz
- $\varphi$: Phasenverschiebung
- Periode: $T = \frac{2\pi}{\omega}$
- Frequenz: $f = \frac{1}{T} = \frac{\omega}{2\pi}$

### Wechselstrom

Die Netzspannung in Europa:
$$U(t) = 325 \, \text{V} \cdot \sin(2\pi \cdot 50 \, \text{Hz} \cdot t)$$

- Frequenz: $f = 50$ Hz
- Periode: $T = 0.02$ s = 20 ms

### Fourierreihen

Jede „vernünftige" periodische Funktion lässt sich als Summe von Sinus- und Kosinusfunktionen darstellen:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Trigonometrische-Funktionen]] – Wichtigste periodische Funktionen
- → [[Transformationen]] – Einfluss von Streckung und Verschiebung auf die Periode
- → [[Symmetrie]] – Periodische Funktionen können zusätzlich symmetrisch sein
- → [[09-Trigonometrie-und-periodische-Funktionen|Trigonometrie und periodische Funktionen]] – Vertiefung

> [!warning] **Prüfungsrelevant**
> - Formale Definition der Periodizität
> - Berechnung der Periode bei transformierten trigonometrischen Funktionen
> - Nachweis der Periodizität durch Einsetzen
> - Zusammenhang zwischen Kreisfrequenz und Periode

> [!question] **Typische Prüfungsfragen**
> - Bestimme die Grundperiode von $f(x) = \sin(3x) + \cos(2x)$.
> - Zeige, dass $f(x) = |\sin(x)|$ die Periode $\pi$ hat.
> - Eine Schwingung hat die Frequenz 440 Hz. Wie groß ist die Periode?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[04-Folgen-Reihen-und-Grenzwerte-Index|Folgen, Reihen und Grenzwerte]] – Fourierreihen als unendliche Reihen
> - [[Exponentialfunktionen]] – Eulersche Formel und komplexe Darstellung
> - [[Glossar]] – Fachbegriffe zu Schwingungen
