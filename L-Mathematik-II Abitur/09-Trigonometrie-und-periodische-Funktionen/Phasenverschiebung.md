---
author: Andreas Hümmer
title: Phasenverschiebung
tags:
  - content
  - mathe
  - trigonometrie
  - phasenverschiebung
  - phase
  - schwingungen
created: 2025-06-20
modified: 2025-06-20
---

# Phasenverschiebung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Phasenverschiebung mathematisch und physikalisch verstehen
> - Phasenverschiebungen aus Funktionsgleichungen und Graphen ablesen können
> - Die Phasendifferenz zweier Schwingungen bestimmen können
> - Phasenverschiebungen in Anwendungen interpretieren können

---

## Überblick

Die **Phasenverschiebung** (auch **Phasenlage** oder kurz **Phase**) beschreibt die zeitliche oder räumliche Verschiebung einer periodischen Funktion. Zwei Schwingungen mit gleicher Frequenz können unterschiedliche Phasen haben – sie „schwingen versetzt" zueinander. Das Verständnis der Phasenverschiebung ist essentiell für das Arbeiten mit Wechselstrom, Wellen und allgemeinen Überlagerungen von Schwingungen.

## Mathematische Definition

### Phase einer Sinusfunktion

Bei einer allgemeinen Sinusfunktion

$$f(t) = A \cdot \sin(\omega t + \varphi_0)$$

heißt das Argument $\omega t + \varphi_0$ die **Phase** zum Zeitpunkt $t$.

Der konstante Anteil $\varphi_0$ heißt **Anfangsphase** oder **Nullphasenwinkel**.

### Phasenverschiebung als Verschiebung

Die Funktion $f(t) = \sin(t - c)$ ist gegenüber $g(t) = \sin(t)$ um $c$ Einheiten nach **rechts** verschoben.

**Allgemein:**

$$f(t) = A \cdot \sin(\omega(t - t_0))$$

ist um $t_0$ Zeiteinheiten nach rechts verschoben.

### Umrechnung zwischen den Darstellungen

$$\sin(\omega t + \varphi_0) = \sin\left(\omega\left(t + \frac{\varphi_0}{\omega}\right)\right)$$

Die zeitliche Verschiebung beträgt also:

$$\Delta t = -\frac{\varphi_0}{\omega} = -\frac{\varphi_0 \cdot T}{2\pi}$$

## Phasendifferenz zweier Schwingungen

### Definition

Die **Phasendifferenz** $\Delta \varphi$ zweier Schwingungen

$$f_1(t) = A_1 \sin(\omega t + \varphi_1)$$
$$f_2(t) = A_2 \sin(\omega t + \varphi_2)$$

ist:

$$\Delta \varphi = \varphi_2 - \varphi_1$$

### Besondere Fälle

| Phasendifferenz | Bezeichnung | Beschreibung |
|-----------------|-------------|--------------|
| $\Delta \varphi = 0$ | Gleichphasig | Schwingungen im Gleichtakt |
| $\Delta \varphi = \pi$ | Gegenphasig | Schwingungen gegensätzlich |
| $\Delta \varphi = \frac{\pi}{2}$ | In Quadratur | 90° versetzt |

### Grafische Darstellung

```
     Gleichphasig (Δφ = 0)      Gegenphasig (Δφ = π)
         ___                        ___
        /   \                      /   \
    ___/     \___              ___/     \___
                 \___/                       
                                    \___/
```

## Phasenverschiebung aus dem Graphen ablesen

### Methode 1: Nulldurchgang mit positivem Anstieg

1. Finde den ersten Nulldurchgang mit positivem Anstieg bei der Referenzfunktion $\sin(t)$: bei $t = 0$
2. Finde denselben Punkt bei der verschobenen Funktion: bei $t = t_0$
3. Phasenverschiebung: $c = t_0$ (nach rechts, wenn $t_0 > 0$)

### Methode 2: Aus Maximum oder Minimum

1. Bei $\sin(t)$: erstes Maximum bei $t = \frac{\pi}{2}$
2. Bei der verschobenen Funktion: Maximum bei $t = t_M$
3. Phasenverschiebung: $c = t_M - \frac{\pi}{2}$

### Beispiel

Die Funktion $f(t) = \sin(2t - \frac{\pi}{3})$

Umformen in Standardform:
$$f(t) = \sin\left(2\left(t - \frac{\pi}{6}\right)\right)$$

Die Phasenverschiebung beträgt $c = \frac{\pi}{6}$ nach rechts.

## Phasenverschiebung zwischen Sinus und Kosinus

### Fundamentale Beziehung

$$\cos(t) = \sin\left(t + \frac{\pi}{2}\right)$$

Der Kosinus **eilt dem Sinus um $\frac{\pi}{2}$ (90°) voraus**.

Äquivalent:

$$\sin(t) = \cos\left(t - \frac{\pi}{2}\right)$$

Der Sinus **hinkt dem Kosinus um $\frac{\pi}{2}$ (90°) hinterher**.

### Grafische Veranschaulichung

```
     cos(t)  sin(t)
         |     |
  -------|-----|-----------> t
         0    π/2

Der Kosinus erreicht sein Maximum
bei t = 0, der Sinus erst bei t = π/2.
```

## Anwendungen in der Physik

### Wechselstromkreise

In einem Wechselstromkreis mit Spule oder Kondensator sind Strom und Spannung **phasenverschoben**:

**Ohmsche Last:** $\Delta \varphi = 0$ (Strom und Spannung gleichphasig)

**Induktive Last (Spule):** $\Delta \varphi = +\frac{\pi}{2}$ (Spannung eilt vor)

**Kapazitive Last (Kondensator):** $\Delta \varphi = -\frac{\pi}{2}$ (Strom eilt vor)

### Merkregel für Wechselstrom

> „Bei Induktivitäten die Ströme sich verspäten,
> bei Kapazitäten sie sich vor eilen täten."

### Mechanische Schwingungen

Beim harmonischen Oszillator:

$$x(t) = A\cos(\omega_0 t + \varphi_0)$$
$$v(t) = -A\omega_0\sin(\omega_0 t + \varphi_0) = A\omega_0\cos\left(\omega_0 t + \varphi_0 + \frac{\pi}{2}\right)$$

Die Geschwindigkeit eilt der Auslenkung um $\frac{\pi}{2}$ voraus.

## Überlagerung phasenverschobener Schwingungen

### Gleiche Amplitude, beliebige Phasendifferenz

$$A\sin(\omega t) + A\sin(\omega t + \Delta\varphi) = 2A\cos\left(\frac{\Delta\varphi}{2}\right)\sin\left(\omega t + \frac{\Delta\varphi}{2}\right)$$

**Spezialfälle:**
- $\Delta\varphi = 0$: Amplitude verdoppelt sich
- $\Delta\varphi = \pi$: Auslöschung (Amplitude = 0)
- $\Delta\varphi = \frac{\pi}{2}$: Amplitude wird $\sqrt{2}$-fach

### Beispiel: Konstruktive und destruktive Interferenz

Zwei Wellen mit gleicher Amplitude:
- **Konstruktiv** ($\Delta\varphi = 0$): $A + A = 2A$
- **Destruktiv** ($\Delta\varphi = \pi$): $A - A = 0$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus--und-Kosinusfunktionen]] – Die allgemeinen Parameter
- → [[Periodische-Vorgaenge]] – Zeitliche Verschiebung
- → [[Anwendungen-bei-Schwingungen-und-Wellen]] – Physikalische Kontexte
- → [[Additionstheoreme]] – Mathematik der Überlagerung

> [!warning] **Prüfungsrelevant**
> - Die Beziehung $\cos(t) = \sin(t + \frac{\pi}{2})$ kennen
> - Phasenverschiebung aus $f(t) = \sin(bt + \varphi)$ berechnen: $\Delta t = -\frac{\varphi}{b}$
> - Phasendifferenz zweier Schwingungen bestimmen können
> - Gleichphasig ($\Delta\varphi = 0$) und gegenphasig ($\Delta\varphi = \pi$) unterscheiden

> [!question] **Typische Prüfungsfragen**
> - Um wie viel ist $f(t) = \sin(2t - \frac{\pi}{4})$ gegenüber $g(t) = \sin(2t)$ verschoben?
> - Zwei Schwingungen $\sin(3t)$ und $\cos(3t)$ werden überlagert. Wie groß ist die Phasendifferenz?
> - Beschreiben Sie, was passiert, wenn zwei gegenphasige Schwingungen gleicher Amplitude überlagert werden.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Tipler, P.A. & Mosca, G.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.

> [!tip] **Weiterführende Links**
> - [[Anwendungen-bei-Schwingungen-und-Wellen]] – Interferenz und Überlagerung
> - [[Additionstheoreme]] – Mathematische Grundlagen
