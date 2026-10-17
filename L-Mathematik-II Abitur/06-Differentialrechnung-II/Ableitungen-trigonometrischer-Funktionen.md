---
author: Andreas Hümmer
title: Ableitungen trigonometrischer Funktionen
tags:
  - content
  - mathe
  - differentialrechnung
  - trigonometrie
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Ableitungen trigonometrischer Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Ableitungen von Sinus, Kosinus und Tangens kennen und anwenden können
> - Verkettete trigonometrische Funktionen ableiten können
> - Die Ableitungen der Arkusfunktionen kennen
> - Trigonometrische Funktionen in Kurvendiskussionen untersuchen können

---

## Überblick

Die **trigonometrischen Funktionen** Sinus, Kosinus und Tangens sowie ihre Umkehrfunktionen (Arkusfunktionen) haben charakteristische Ableitungen, die in vielen Bereichen der Mathematik, Physik und Technik benötigt werden. Die periodische Natur dieser Funktionen spiegelt sich auch in ihren Ableitungen wider – die Ableitungen von Sinus und Kosinus bilden einen Zyklus.

## Grundlegende Ableitungen

> [!note] **Satz: Ableitungen der Grundfunktionen**
> $$\frac{d}{dx} \sin x = \cos x$$
> $$\frac{d}{dx} \cos x = -\sin x$$
> $$\frac{d}{dx} \tan x = \frac{1}{\cos^2 x} = 1 + \tan^2 x$$

### Der Ableitungszyklus

Die Ableitungen von Sinus und Kosinus bilden einen Zyklus:

$$\sin x \xrightarrow{\frac{d}{dx}} \cos x \xrightarrow{\frac{d}{dx}} -\sin x \xrightarrow{\frac{d}{dx}} -\cos x \xrightarrow{\frac{d}{dx}} \sin x$$

Nach viermaligem Ableiten erhält man wieder die Ausgangsfunktion.

### Herleitung für Tangens

$$\frac{d}{dx} \tan x = \frac{d}{dx} \frac{\sin x}{\cos x}$$

Mit Quotientenregel:
$$= \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}$$

### Weitere trigonometrische Funktionen

| Funktion | Ableitung |
|----------|-----------|
| $\cot x$ | $-\frac{1}{\sin^2 x}$ |
| $\sec x = \frac{1}{\cos x}$ | $\frac{\sin x}{\cos^2 x} = \sec x \tan x$ |
| $\csc x = \frac{1}{\sin x}$ | $-\frac{\cos x}{\sin^2 x} = -\csc x \cot x$ |

## Anwendung der Kettenregel

Für verkettete trigonometrische Funktionen:

$$\frac{d}{dx} \sin(g(x)) = \cos(g(x)) \cdot g'(x)$$
$$\frac{d}{dx} \cos(g(x)) = -\sin(g(x)) \cdot g'(x)$$
$$\frac{d}{dx} \tan(g(x)) = \frac{g'(x)}{\cos^2(g(x))}$$

### Wichtige Beispiele

| Funktion | Ableitung |
|----------|-----------|
| $\sin(2x)$ | $2\cos(2x)$ |
| $\cos(3x)$ | $-3\sin(3x)$ |
| $\sin(x^2)$ | $2x\cos(x^2)$ |
| $\cos(\sqrt{x})$ | $-\frac{\sin(\sqrt{x})}{2\sqrt{x}}$ |
| $\tan(e^x)$ | $\frac{e^x}{\cos^2(e^x)}$ |
| $\sin^2(x) = (\sin x)^2$ | $2\sin x \cdot \cos x = \sin(2x)$ |

### Allgemeine Sinusfunktion

Für $f(x) = A \sin(\omega x + \varphi)$ gilt:

$$f'(x) = A\omega \cos(\omega x + \varphi)$$

**Parameter:**
- $A$: Amplitude
- $\omega$: Kreisfrequenz
- $\varphi$: Phasenverschiebung

## Ableitungen der Arkusfunktionen

Die Umkehrfunktionen der trigonometrischen Funktionen heißen **Arkusfunktionen**.

> [!note] **Satz: Ableitungen der Arkusfunktionen**
> $$\frac{d}{dx} \arcsin x = \frac{1}{\sqrt{1-x^2}} \quad \text{für } |x| < 1$$
> $$\frac{d}{dx} \arccos x = -\frac{1}{\sqrt{1-x^2}} \quad \text{für } |x| < 1$$
> $$\frac{d}{dx} \arctan x = \frac{1}{1+x^2}$$

### Herleitung für Arkussinus

Aus $y = \arcsin x$ folgt $x = \sin y$.

Implizites Ableiten:
$$1 = \cos y \cdot y' \implies y' = \frac{1}{\cos y}$$

Mit $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$ (für $y \in [-\frac{\pi}{2}, \frac{\pi}{2}]$):
$$\frac{d}{dx} \arcsin x = \frac{1}{\sqrt{1-x^2}}$$

## Beispiel: Kurvendiskussion

**Funktion:** $f(x) = \sin x \cdot \cos x$ auf $[0, 2\pi]$

**Vereinfachung:** Mit $\sin x \cos x = \frac{1}{2}\sin(2x)$:
$$f(x) = \frac{1}{2}\sin(2x)$$

**Ableitung:**
$$f'(x) = \frac{1}{2} \cdot 2\cos(2x) = \cos(2x)$$

**Nullstellen von f:**
$$\sin(2x) = 0 \implies 2x = k\pi \implies x = \frac{k\pi}{2}$$

Auf $[0, 2\pi]$: $x \in \{0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi\}$

**Extrema:**
$$f'(x) = 0 \implies \cos(2x) = 0 \implies 2x = \frac{\pi}{2} + k\pi$$
$$x = \frac{\pi}{4} + \frac{k\pi}{2}$$

Auf $[0, 2\pi]$: $x \in \{\frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}\}$

**Klassifikation:**

| $x$ | $f(x)$ | Art |
|-----|--------|-----|
| $\frac{\pi}{4}$ | $\frac{1}{2}$ | Maximum |
| $\frac{3\pi}{4}$ | $-\frac{1}{2}$ | Minimum |
| $\frac{5\pi}{4}$ | $\frac{1}{2}$ | Maximum |
| $\frac{7\pi}{4}$ | $-\frac{1}{2}$ | Minimum |

## Physikalische Anwendung: Harmonische Schwingung

Die Position eines harmonischen Oszillators wird beschrieben durch:
$$x(t) = A \cos(\omega t + \varphi_0)$$

**Geschwindigkeit:**
$$v(t) = x'(t) = -A\omega \sin(\omega t + \varphi_0)$$

**Beschleunigung:**
$$a(t) = x''(t) = -A\omega^2 \cos(\omega t + \varphi_0) = -\omega^2 x(t)$$

Die Beschleunigung ist proportional zur Auslenkung mit negativem Vorzeichen – charakteristisch für Schwingungen.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Trigonometrische-Funktionen]] – Grundlegende Eigenschaften
- → [[Kettenregel]] – Verkettete Ableitungen
- → [[Umkehrtrigonometrische-Funktionen]] – Arkusfunktionen
- → [[Anwendungen-in-Physik-und-Technik]] – Schwingungen
- → [[Periodizitaet]] – Periodische Funktionen

> [!warning] **Prüfungsrelevant**
> - $(\sin x)' = \cos x$, $(\cos x)' = -\sin x$
> - $(\tan x)' = \frac{1}{\cos^2 x}$
> - Kettenregel: $(\sin(g(x)))' = \cos(g(x)) \cdot g'(x)$
> - $(\arctan x)' = \frac{1}{1+x^2}$ – häufig bei Integralen
> - Bogenmaß verwenden (nicht Grad!)

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Ableitung von $f(x) = \sin(2x) \cdot \cos x$
> - Führen Sie eine Kurvendiskussion für $f(x) = x + \sin x$ durch
> - Zeigen Sie: $(\tan x)' = 1 + \tan^2 x$
> - Bestimmen Sie die Extrema von $f(x) = \sin x + \cos x$

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Anwendungen-in-Physik-und-Technik]] – Schwingungen und Wellen
> - [[Vollstaendige-Kurvendiskussion]] – Analyse trigonometrischer Funktionen
