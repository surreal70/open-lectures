---
author: Andreas Hümmer
title: Integration trigonometrischer Funktionen
tags:
  - content
  - mathe
  - integralrechnung
  - trigonometrie
  - sinus
  - kosinus
created: 2026-10-17
modified: 2026-10-17
---

# Integration trigonometrischer Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Stammfunktionen von Sinus und Kosinus kennen und anwenden können
> - Trigonometrische Funktionen mit linearem Argument integrieren können
> - Das Vorzeichen bei der Integration von Sinusfunktionen beachten
> - Bestimmte Integrale trigonometrischer Funktionen berechnen können

---

## Überblick

Trigonometrische Funktionen beschreiben periodische Vorgänge wie Schwingungen, Wellen oder Kreisbewegungen. Ihre Integration ist für viele Anwendungen in Physik und Technik unerlässlich. Die Grundintegrale von Sinus und Kosinus folgen direkt aus den bekannten Ableitungsregeln – allerdings mit besonderer Aufmerksamkeit auf die Vorzeichen.

## Grundintegrale

### Sinus und Kosinus

$$\int \sin(x) \, dx = -\cos(x) + C$$

$$\int \cos(x) \, dx = \sin(x) + C$$

### Merkregel für das Vorzeichen

Beim Ableiten gilt:
- $(\sin x)' = \cos x$ (kein Vorzeichenwechsel)
- $(\cos x)' = -\sin x$ (Vorzeichenwechsel)

Beim Integrieren ist es „umgekehrt":
- $\int \cos x \, dx = \sin x + C$ (kein Vorzeichenwechsel)
- $\int \sin x \, dx = -\cos x + C$ (Vorzeichenwechsel)

### Probe

$$\frac{d}{dx}(-\cos x) = -(-\sin x) = \sin x \quad \checkmark$$

$$\frac{d}{dx}(\sin x) = \cos x \quad \checkmark$$

## Integration mit linearem Argument

### Allgemeine Formeln

Für $a \neq 0$ gilt:

$$\int \sin(ax) \, dx = -\frac{1}{a}\cos(ax) + C$$

$$\int \cos(ax) \, dx = \frac{1}{a}\sin(ax) + C$$

### Erweiterung auf $ax + b$

$$\int \sin(ax + b) \, dx = -\frac{1}{a}\cos(ax + b) + C$$

$$\int \cos(ax + b) \, dx = \frac{1}{a}\sin(ax + b) + C$$

### Begründung

Der Faktor $\frac{1}{a}$ kompensiert die innere Ableitung bei der Kettenregel.

**Probe** für $\int \sin(ax + b) \, dx$:
$$\frac{d}{dx}\left(-\frac{1}{a}\cos(ax+b)\right) = -\frac{1}{a} \cdot (-\sin(ax+b)) \cdot a = \sin(ax+b) \quad \checkmark$$

## Beispiele

### Einfache Integrale

$$\int \sin(2x) \, dx = -\frac{1}{2}\cos(2x) + C$$

$$\int \cos(3x) \, dx = \frac{1}{3}\sin(3x) + C$$

$$\int \sin\left(\frac{x}{2}\right) dx = -2\cos\left(\frac{x}{2}\right) + C$$

### Mit Verschiebung

$$\int \sin(2x - \pi) \, dx = -\frac{1}{2}\cos(2x - \pi) + C$$

$$\int \cos\left(4x + \frac{\pi}{3}\right) dx = \frac{1}{4}\sin\left(4x + \frac{\pi}{3}\right) + C$$

### Mit konstantem Faktor

$$\int 5\sin(x) \, dx = -5\cos(x) + C$$

$$\int 3\cos(2x) \, dx = \frac{3}{2}\sin(2x) + C$$

## Bestimmte Integrale

### Beispiel 1: Sinus über eine Halbperiode

$$\int_0^{\pi} \sin(x) \, dx = \Big[-\cos(x)\Big]_0^{\pi} = -\cos(\pi) - (-\cos(0))$$
$$= -(-1) + 1 = 2$$

### Beispiel 2: Kosinus über eine Viertelperiode

$$\int_0^{\pi/2} \cos(x) \, dx = \Big[\sin(x)\Big]_0^{\pi/2} = \sin\left(\frac{\pi}{2}\right) - \sin(0)$$
$$= 1 - 0 = 1$$

### Beispiel 3: Mit linearem Argument

$$\int_0^{\pi/2} \sin(2x) \, dx = \left[-\frac{1}{2}\cos(2x)\right]_0^{\pi/2}$$
$$= -\frac{1}{2}\cos(\pi) + \frac{1}{2}\cos(0) = -\frac{1}{2}(-1) + \frac{1}{2}(1) = 1$$

### Beispiel 4: Vollständige Periode

$$\int_0^{2\pi} \sin(x) \, dx = \Big[-\cos(x)\Big]_0^{2\pi} = -\cos(2\pi) + \cos(0) = -1 + 1 = 0$$

Die Flächenbilanz ist null, da sich positive und negative Anteile aufheben!

## Weitere trigonometrische Integrale

### Tangens

$$\int \tan(x) \, dx = \int \frac{\sin x}{\cos x} \, dx = -\ln|\cos x| + C = \ln|\sec x| + C$$

### Kotangens

$$\int \cot(x) \, dx = \int \frac{\cos x}{\sin x} \, dx = \ln|\sin x| + C$$

### $\frac{1}{\cos^2 x}$ und $\frac{1}{\sin^2 x}$

$$\int \frac{1}{\cos^2 x} \, dx = \tan(x) + C$$

$$\int \frac{1}{\sin^2 x} \, dx = -\cot(x) + C$$

Diese Formeln folgen direkt daraus, dass $(\tan x)' = \frac{1}{\cos^2 x}$ und $(\cot x)' = -\frac{1}{\sin^2 x}$.

## Tabelle wichtiger Integrale

| Funktion $f(x)$ | Stammfunktion $F(x)$ |
|-----------------|---------------------|
| $\sin(x)$ | $-\cos(x) + C$ |
| $\cos(x)$ | $\sin(x) + C$ |
| $\sin(ax+b)$ | $-\frac{1}{a}\cos(ax+b) + C$ |
| $\cos(ax+b)$ | $\frac{1}{a}\sin(ax+b) + C$ |
| $\tan(x)$ | $-\ln|\cos x| + C$ |
| $\frac{1}{\cos^2 x}$ | $\tan(x) + C$ |
| $\frac{1}{\sin^2 x}$ | $-\cot(x) + C$ |

## Häufige Fehler

### Fehler 1: Vorzeichen bei Sinus vergessen

❌ $\int \sin(x) \, dx = \cos(x) + C$

✅ $\int \sin(x) \, dx = -\cos(x) + C$

### Fehler 2: Faktor bei linearem Argument vergessen

❌ $\int \cos(3x) \, dx = \sin(3x) + C$

✅ $\int \cos(3x) \, dx = \frac{1}{3}\sin(3x) + C$

### Fehler 3: Vorzeichen und Faktor vertauschen

❌ $\int \sin(2x) \, dx = \frac{1}{2}\cos(2x) + C$

✅ $\int \sin(2x) \, dx = -\frac{1}{2}\cos(2x) + C$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Trigonometrische-Funktionen]] – Eigenschaften von Sinus und Kosinus
- → [[Ableitungen-trigonometrischer-Funktionen]] – Die Umkehroperation
- → [[Grundlegende-Integrationsregeln]] – Lineare Verkettungen
- → [[Flaechenbilanz]] – Warum $\int_0^{2\pi} \sin x \, dx = 0$
- → [[Periodizitaet]] – Periodische Eigenschaften nutzen

> [!warning] **Prüfungsrelevant**
> - $\int \sin x \, dx = -\cos x + C$ – das Minus nicht vergessen!
> - $\int \cos x \, dx = \sin x + C$
> - Bei linearem Argument: Faktor $\frac{1}{a}$ beachten
> - Bei bestimmten Integralen über volle Perioden: Flächenbilanz oft null!

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int_0^{\pi/4} \cos(2x) \, dx$.
> - Bestimme die Stammfunktion von $f(x) = 3\sin(4x - \pi)$.
> - Erkläre, warum $\int_0^{2\pi} \cos(x) \, dx = 0$ ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Flaechenberechnung]] – Flächen mit trigonometrischen Funktionen
> - [[Integrale-im-Sachzusammenhang]] – Anwendung auf Schwingungen
