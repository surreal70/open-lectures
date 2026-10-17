---
author: Andreas Hümmer
title: Trigonometrische Funktionen
tags:
  - content
  - mathe
  - funktionen
  - trigonometrie
  - sinus
  - kosinus
created: 2025-06-19
modified: 2025-06-19
---

# Trigonometrische Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definitionen von Sinus, Kosinus und Tangens am Einheitskreis verstehen
> - Graphen trigonometrischer Funktionen analysieren und transformieren können
> - Wichtige trigonometrische Identitäten kennen und anwenden können
> - Trigonometrische Gleichungen lösen können

---

## Überblick

Trigonometrische Funktionen beschreiben periodische Zusammenhänge und entstammen ursprünglich der Geometrie des Dreiecks. Am Einheitskreis definiert, sind Sinus und Kosinus fundamentale Funktionen der Analysis mit Anwendungen in Physik (Schwingungen, Wellen), Elektrotechnik (Wechselstrom) und Signalverarbeitung. Sie bilden die Grundlage der Fourier-Analysis, mit der beliebige periodische Funktionen dargestellt werden können.

## Definition am Einheitskreis

### Der Einheitskreis

Der Einheitskreis ist der Kreis um den Ursprung mit Radius 1:

$$x^2 + y^2 = 1$$

Ein Punkt $P$ auf dem Einheitskreis wird durch den Winkel $\varphi$ (im Bogenmaß) beschrieben, gemessen von der positiven x-Achse gegen den Uhrzeigersinn.

### Sinus und Kosinus

Für einen Punkt $P$ auf dem Einheitskreis mit Winkel $\varphi$:

$$\cos(\varphi) = x\text{-Koordinate von } P$$
$$\sin(\varphi) = y\text{-Koordinate von } P$$

```
        y
        │    P(cos φ, sin φ)
        │   /
      sin φ │  /
        │ /φ
   ─────┼────────── x
        │  cos φ
        │
```

### Tangens und Kotangens

$$\tan(\varphi) = \frac{\sin(\varphi)}{\cos(\varphi)} \quad \text{für } \cos(\varphi) \neq 0$$

$$\cot(\varphi) = \frac{\cos(\varphi)}{\sin(\varphi)} \quad \text{für } \sin(\varphi) \neq 0$$

## Wichtige Funktionswerte

| $\varphi$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ |
|-----------|-----|-----------------|-----------------|-----------------|-----------------|-------|
| Grad | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ |
| $\sin(\varphi)$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ |
| $\cos(\varphi)$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ |
| $\tan(\varphi)$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | — | $0$ |

## Die Sinusfunktion

### Eigenschaften

$$f(x) = \sin(x)$$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R}$ |
| Wertebereich | $W_f = [-1, 1]$ |
| Periode | $T = 2\pi$ |
| Nullstellen | $x = k\pi$, $k \in \mathbb{Z}$ |
| Maxima | $x = \frac{\pi}{2} + 2k\pi$, Wert $1$ |
| Minima | $x = -\frac{\pi}{2} + 2k\pi$, Wert $-1$ |
| Symmetrie | Punktsymmetrisch zum Ursprung (ungerade) |

### Graph

```
     1 ┼    ╭──╮        ╭──╮
       │   ╱    ╲      ╱    ╲
   ────┼──╱──────╲────╱──────╲──── x
       │          ╲  ╱
    -1 ┼           ╰──╯
       0    π    2π    3π
```

## Die Kosinusfunktion

### Eigenschaften

$$f(x) = \cos(x)$$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R}$ |
| Wertebereich | $W_f = [-1, 1]$ |
| Periode | $T = 2\pi$ |
| Nullstellen | $x = \frac{\pi}{2} + k\pi$, $k \in \mathbb{Z}$ |
| Maxima | $x = 2k\pi$, Wert $1$ |
| Minima | $x = \pi + 2k\pi$, Wert $-1$ |
| Symmetrie | Achsensymmetrisch zur y-Achse (gerade) |

### Zusammenhang mit Sinus

$$\cos(x) = \sin\left(x + \frac{\pi}{2}\right)$$

Der Kosinus ist ein um $\frac{\pi}{2}$ nach links verschobener Sinus.

## Die Tangensfunktion

### Eigenschaften

$$f(x) = \tan(x) = \frac{\sin(x)}{\cos(x)}$$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi \mid k \in \mathbb{Z}\right\}$ |
| Wertebereich | $W_f = \mathbb{R}$ |
| Periode | $T = \pi$ |
| Nullstellen | $x = k\pi$, $k \in \mathbb{Z}$ |
| Polstellen | $x = \frac{\pi}{2} + k\pi$ |
| Symmetrie | Punktsymmetrisch zum Ursprung (ungerade) |
| Monotonie | streng monoton steigend in jedem Ast |

## Trigonometrische Identitäten

### Fundamentale Identität (Pythagoras)

$$\sin^2(x) + \cos^2(x) = 1$$

### Additionstheoreme

$$\sin(x \pm y) = \sin(x)\cos(y) \pm \cos(x)\sin(y)$$
$$\cos(x \pm y) = \cos(x)\cos(y) \mp \sin(x)\sin(y)$$
$$\tan(x \pm y) = \frac{\tan(x) \pm \tan(y)}{1 \mp \tan(x)\tan(y)}$$

### Doppelwinkelformeln

$$\sin(2x) = 2\sin(x)\cos(x)$$
$$\cos(2x) = \cos^2(x) - \sin^2(x) = 2\cos^2(x) - 1 = 1 - 2\sin^2(x)$$

### Halbwinkelformeln

$$\sin^2(x) = \frac{1 - \cos(2x)}{2}$$
$$\cos^2(x) = \frac{1 + \cos(2x)}{2}$$

### Symmetriebeziehungen

$$\sin(-x) = -\sin(x) \quad \text{(ungerade)}$$
$$\cos(-x) = \cos(x) \quad \text{(gerade)}$$
$$\sin(\pi - x) = \sin(x)$$
$$\cos(\pi - x) = -\cos(x)$$

## Transformierte trigonometrische Funktionen

### Allgemeine Sinusfunktion

$$f(x) = a \cdot \sin(b(x - c)) + d$$

| Parameter | Bedeutung |
|-----------|-----------|
| $a$ | **Amplitude**: $\|a\|$ (Maximalauslenkung) |
| $b$ | **Frequenz**: Anzahl der Perioden pro $2\pi$ |
| $T = \frac{2\pi}{\|b\|}$ | **Periode**: Länge einer Schwingung |
| $c$ | **Phasenverschiebung**: Verschiebung nach rechts |
| $d$ | **Mittellinie**: vertikale Verschiebung |

### Beispiel

$f(x) = 3\sin(2x - \pi) + 1 = 3\sin\left(2\left(x - \frac{\pi}{2}\right)\right) + 1$

- Amplitude: $3$
- Periode: $T = \frac{2\pi}{2} = \pi$
- Phasenverschiebung: $\frac{\pi}{2}$ nach rechts
- Mittellinie: $y = 1$
- Wertebereich: $[-2, 4]$

## Trigonometrische Gleichungen

### Grundform $\sin(x) = a$ (mit $|a| \leq 1$)

$$x_1 = \arcsin(a) + 2k\pi$$
$$x_2 = \pi - \arcsin(a) + 2k\pi$$

für $k \in \mathbb{Z}$

### Grundform $\cos(x) = a$ (mit $|a| \leq 1$)

$$x = \pm \arccos(a) + 2k\pi$$

### Beispiel

$\sin(x) = \frac{1}{2}$ für $x \in [0, 2\pi]$

$$x_1 = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$$
$$x_2 = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$$

Lösungen: $x \in \left\{\frac{\pi}{6}, \frac{5\pi}{6}\right\}$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Trigonometrie-und-periodische-Funktionen|Modul 9: Trigonometrie]] — Vertiefung
- → [[Periodizitaet]] — Periodische Funktionen allgemein
- → [[Umkehrtrigonometrische-Funktionen]] — Arkusfunktionen
- → [[Symmetrie]] — Gerade und ungerade Funktionen
- → [[05-Differentialrechnung-I|Differentialrechnung]] — $(\sin x)' = \cos x$
- → [[07-Integralrechnung-I|Integralrechnung]] — $\int \sin x \, dx = -\cos x + C$

> [!warning] **Prüfungsrelevant**
> - Werte von $\sin$ und $\cos$ für Standardwinkel auswendig kennen
> - Fundamentalidentität $\sin^2 + \cos^2 = 1$
> - Additionstheoreme und Doppelwinkelformeln
> - Analyse transformierter Sinusfunktionen (Amplitude, Periode, Phasenverschiebung)
> - Lösen trigonometrischer Gleichungen in gegebenen Intervallen
> - Unterscheidung: Bogenmaß vs. Gradmaß

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle Lösungen von $2\sin^2(x) - \sin(x) - 1 = 0$ im Intervall $[0, 2\pi)$.
> - Geben Sie für $f(x) = 2\cos(3x - \frac{\pi}{2}) - 1$ Amplitude, Periode und Phasenverschiebung an.
> - Zeigen Sie: $\cos(x) + \cos(y) = 2\cos\left(\frac{x+y}{2}\right)\cos\left(\frac{x-y}{2}\right)$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Abiturprüfungsaufgaben Mathematik*, verschiedene Jahrgänge

> [!tip] **Weiterführende Links**
> - [[Umkehrtrigonometrische-Funktionen]] — Arkusfunktionen
> - [[09-Trigonometrie-und-periodische-Funktionen|Trigonometrie-Modul]] — Anwendungen und Vertiefung

