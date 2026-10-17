---
author: Andreas Hümmer
title: Umkehrtrigonometrische Funktionen
tags:
  - content
  - mathe
  - funktionen
  - trigonometrie
  - arkusfunktionen
  - umkehrfunktion
created: 2025-06-19
modified: 2025-06-19
---

# Umkehrtrigonometrische Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Notwendigkeit der Einschränkung für die Umkehrfunktionen verstehen
> - Die Arkusfunktionen und ihre Eigenschaften kennen
> - Definitions- und Wertebereiche der Arkusfunktionen sicher angeben können
> - Gleichungen mit Arkusfunktionen lösen können

---

## Überblick

Da trigonometrische Funktionen periodisch und damit nicht injektiv sind, besitzen sie keine globalen Umkehrfunktionen. Durch Einschränkung auf geeignete Intervalle entstehen die **Arkusfunktionen** (auch Zyklometrische Funktionen genannt): Arkussinus, Arkuskosinus und Arkustangens. Diese beantworten die Frage: „Welcher Winkel hat diesen Funktionswert?" Sie sind essentiell für die Integration bestimmter Funktionstypen und für geometrische Berechnungen.

## Motivation: Warum Einschränkung?

Die Gleichung $\sin(x) = 0{,}5$ hat unendlich viele Lösungen:

$$x \in \left\{\frac{\pi}{6} + 2k\pi \mid k \in \mathbb{Z}\right\} \cup \left\{\frac{5\pi}{6} + 2k\pi \mid k \in \mathbb{Z}\right\}$$

Um eine eindeutige Umkehrfunktion zu definieren, muss der Definitionsbereich so eingeschränkt werden, dass die Funktion bijektiv wird.

## Arkussinus

### Definition

Der **Arkussinus** ist die Umkehrfunktion des Sinus, eingeschränkt auf $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$:

$$y = \arcsin(x) \quad \Leftrightarrow \quad x = \sin(y) \text{ mit } y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$$

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = [-1, 1]$ |
| Wertebereich | $W_f = \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| Nullstelle | $x = 0$ |
| Monotonie | streng monoton steigend |
| Symmetrie | Punktsymmetrisch zum Ursprung (ungerade) |

### Wichtige Werte

| $x$ | $\arcsin(x)$ |
|-----|--------------|
| $-1$ | $-\frac{\pi}{2}$ |
| $-\frac{\sqrt{3}}{2}$ | $-\frac{\pi}{3}$ |
| $-\frac{1}{2}$ | $-\frac{\pi}{6}$ |
| $0$ | $0$ |
| $\frac{1}{2}$ | $\frac{\pi}{6}$ |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ |
| $1$ | $\frac{\pi}{2}$ |

### Graph

Der Graph von $\arcsin(x)$ ist die Spiegelung des eingeschränkten Sinus an der Winkelhalbierenden $y = x$:

```
     y
  π/2┼        ╱
     │      ╱
     │    ╱
   ──┼──•──────── x
     │╱   -1    1
-π/2 ┼
```

## Arkuskosinus

### Definition

Der **Arkuskosinus** ist die Umkehrfunktion des Kosinus, eingeschränkt auf $[0, \pi]$:

$$y = \arccos(x) \quad \Leftrightarrow \quad x = \cos(y) \text{ mit } y \in [0, \pi]$$

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = [-1, 1]$ |
| Wertebereich | $W_f = [0, \pi]$ |
| Nullstelle | $x = 1$ |
| Monotonie | streng monoton fallend |
| Symmetrie | Punktsymmetrisch zu $\left(0, \frac{\pi}{2}\right)$ |

### Wichtige Werte

| $x$ | $\arccos(x)$ |
|-----|--------------|
| $-1$ | $\pi$ |
| $-\frac{1}{2}$ | $\frac{2\pi}{3}$ |
| $0$ | $\frac{\pi}{2}$ |
| $\frac{1}{2}$ | $\frac{\pi}{3}$ |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ |
| $1$ | $0$ |

### Zusammenhang mit Arkussinus

$$\arcsin(x) + \arccos(x) = \frac{\pi}{2} \quad \text{für alle } x \in [-1, 1]$$

## Arkustangens

### Definition

Der **Arkustangens** ist die Umkehrfunktion des Tangens, eingeschränkt auf $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$:

$$y = \arctan(x) \quad \Leftrightarrow \quad x = \tan(y) \text{ mit } y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$$

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R}$ |
| Wertebereich | $W_f = \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |
| Nullstelle | $x = 0$ |
| Asymptoten | $y = \pm\frac{\pi}{2}$ (horizontal) |
| Monotonie | streng monoton steigend |
| Symmetrie | Punktsymmetrisch zum Ursprung (ungerade) |

### Wichtige Werte

| $x$ | $\arctan(x)$ |
|-----|--------------|
| $-\sqrt{3}$ | $-\frac{\pi}{3}$ |
| $-1$ | $-\frac{\pi}{4}$ |
| $-\frac{\sqrt{3}}{3}$ | $-\frac{\pi}{6}$ |
| $0$ | $0$ |
| $\frac{\sqrt{3}}{3}$ | $\frac{\pi}{6}$ |
| $1$ | $\frac{\pi}{4}$ |
| $\sqrt{3}$ | $\frac{\pi}{3}$ |

### Graph

```
     y
  π/2┼- - - - - - - - -
     │           ╱
     │        ╱
   ──┼──────•────────── x
     │    ╱
     │ ╱
-π/2 ┼- - - - - - - - -
```

### Grenzwerte

$$\lim_{x \to +\infty} \arctan(x) = \frac{\pi}{2}$$
$$\lim_{x \to -\infty} \arctan(x) = -\frac{\pi}{2}$$

## Zusammenfassung der Umkehrfunktionen

| Funktion | Einschränkung | $D_f$ | $W_f$ |
|----------|---------------|-------|-------|
| $\sin^{-1} = \arcsin$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ | $[-1, 1]$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $\cos^{-1} = \arccos$ | $[0, \pi]$ | $[-1, 1]$ | $[0, \pi]$ |
| $\tan^{-1} = \arctan$ | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |

## Rechenregeln

### Umkehrbeziehungen

$$\sin(\arcsin(x)) = x \quad \text{für } x \in [-1, 1]$$
$$\arcsin(\sin(x)) = x \quad \text{für } x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$$

**Achtung:** $\arcsin(\sin(x)) \neq x$ für $x$ außerhalb von $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$!

**Beispiel:** $\arcsin(\sin(\pi)) = \arcsin(0) = 0 \neq \pi$

### Nützliche Identitäten

$$\arctan(x) + \arctan\left(\frac{1}{x}\right) = \begin{cases} \frac{\pi}{2} & \text{für } x > 0 \\ -\frac{\pi}{2} & \text{für } x < 0 \end{cases}$$

$$\sin(\arccos(x)) = \sqrt{1 - x^2}$$

$$\cos(\arcsin(x)) = \sqrt{1 - x^2}$$

$$\tan(\arcsin(x)) = \frac{x}{\sqrt{1-x^2}}$$

## Gleichungen mit Arkusfunktionen

### Beispiel 1

$\arcsin(2x - 1) = \frac{\pi}{6}$

$$2x - 1 = \sin\left(\frac{\pi}{6}\right) = \frac{1}{2}$$
$$2x = \frac{3}{2}$$
$$x = \frac{3}{4}$$

**Probe:** $\arcsin\left(2 \cdot \frac{3}{4} - 1\right) = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$ ✓

### Beispiel 2

$\arctan(x) + \arctan(2x) = \frac{\pi}{4}$

Sei $\alpha = \arctan(x)$ und $\beta = \arctan(2x)$.
Dann: $\alpha + \beta = \frac{\pi}{4}$

Mit dem Additionstheorem: $\tan(\alpha + \beta) = \tan\left(\frac{\pi}{4}\right) = 1$

$$\frac{x + 2x}{1 - x \cdot 2x} = 1$$
$$3x = 1 - 2x^2$$
$$2x^2 + 3x - 1 = 0$$
$$x = \frac{-3 \pm \sqrt{9 + 8}}{4} = \frac{-3 \pm \sqrt{17}}{4}$$

Nur $x = \frac{-3 + \sqrt{17}}{4} \approx 0{,}28$ liefert die richtige Lösung (Probe erforderlich).

## Anwendungen

### Winkelberechnung in der Geometrie

Der Winkel zwischen zwei Vektoren $\vec{a}$ und $\vec{b}$:

$$\alpha = \arccos\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}\right)$$

### Steigungswinkel

Eine Gerade mit Steigung $m$ hat den Steigungswinkel:

$$\alpha = \arctan(m)$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Trigonometrische-Funktionen]] — Die Originalfunktionen
- → [[Umkehrfunktionen]] — Allgemeine Theorie
- → [[Definitionsbereich]] — Einschränkungen bei Umkehrfunktionen
- → [[05-Differentialrechnung-I|Differentialrechnung]] — $(\arctan x)' = \frac{1}{1+x^2}$
- → [[07-Integralrechnung-I|Integralrechnung]] — Stammfunktionen mit Arkusfunktionen
- → [[11-Analytische-Geometrie|Analytische Geometrie]] — Winkelberechnungen

> [!warning] **Prüfungsrelevant**
> - Definitions- und Wertebereiche der drei Arkusfunktionen
> - Die Einschränkungsintervalle der Originalfunktionen merken
> - $\arcsin(\sin(x)) = x$ gilt nur im Einschränkungsintervall!
> - Zusammenhang: $\arcsin(x) + \arccos(x) = \frac{\pi}{2}$
> - Asymptotisches Verhalten des Arkustangens
> - Lösen von Gleichungen durch „Anwenden" der Originalfunktion

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie $\arcsin\left(\sin\left(\frac{5\pi}{6}\right)\right)$ ohne Taschenrechner.
> - Lösen Sie die Gleichung $2\arccos(x) = \frac{2\pi}{3}$.
> - Bestimmen Sie den Steigungswinkel der Geraden $y = \sqrt{3}x + 2$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, 2023

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Funktionen]] — Die Originalfunktionen
> - [[11-Analytische-Geometrie|Analytische Geometrie]] — Winkel im Raum

