---
author: Andreas Hümmer
title: Schwingungsmodelle
tags:
  - content
  - mathe
  - modellierung
  - schwingung
  - trigonometrie
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Schwingungsmodelle

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Harmonische Schwingungen mathematisch beschreiben können
> - Amplitude, Frequenz, Periode und Phase interpretieren
> - Schwingungsgleichungen aus Beschreibungen aufstellen
> - Überlagerung von Schwingungen verstehen

---

## Überblick

Schwingungen sind periodische Vorgänge, die in Natur und Technik allgegenwärtig sind: Pendelbewegungen, Schallwellen, Wechselstrom, Lichtwellen und sogar Börsenzyklen folgen schwingungsartigen Mustern. Die mathematische Beschreibung erfolgt durch **trigonometrische Funktionen**, insbesondere Sinus und Kosinus.

Dieses Kapitel verbindet die Trigonometrie mit der Differentialrechnung und zeigt, wie Schwingungen als Lösungen von Differentialgleichungen auftreten.

## Die harmonische Schwingung

### Grundform

Die allgemeine harmonische Schwingung wird beschrieben durch:

$$y(t) = A \sin(\omega t + \varphi_0)$$

oder äquivalent:

$$y(t) = A \cos(\omega t + \varphi_0)$$

### Parameter und ihre Bedeutung

| Parameter | Symbol | Bedeutung | Einheit |
|-----------|--------|-----------|---------|
| Amplitude | $A$ | Maximale Auslenkung | je nach Größe |
| Kreisfrequenz | $\omega$ | $\omega = 2\pi f = \frac{2\pi}{T}$ | $\text{rad/s}$ |
| Frequenz | $f$ | Schwingungen pro Sekunde | $\text{Hz}$ |
| Periode | $T$ | Dauer einer Schwingung | $\text{s}$ |
| Phase | $\varphi_0$ | Anfangsphase | $\text{rad}$ |

### Zusammenhänge

$$T = \frac{1}{f}, \quad \omega = 2\pi f = \frac{2\pi}{T}$$

### Beispiel

Ein Federpendel schwingt mit $A = 5\,\text{cm}$ und $T = 2\,\text{s}$:

$$\omega = \frac{2\pi}{2} = \pi\,\frac{\text{rad}}{\text{s}}$$

$$y(t) = 5 \sin(\pi t)\,\text{cm}$$

(Bei Anfangsauslenkung $y(0) = 0$ und Bewegung nach oben)

## Geschwindigkeit und Beschleunigung

### Ableitung der Schwingungsfunktion

Für $y(t) = A \sin(\omega t)$ gilt:

$$v(t) = y'(t) = A\omega \cos(\omega t)$$

$$a(t) = y''(t) = -A\omega^2 \sin(\omega t) = -\omega^2 y(t)$$

### Wichtige Erkenntnisse

1. **Geschwindigkeit und Auslenkung sind phasenverschoben um $\frac{\pi}{2}$**
2. **Beschleunigung ist proportional zur Auslenkung, aber entgegengesetzt gerichtet**
3. **Maximale Geschwindigkeit**: $v_{\max} = A\omega$ (bei $y = 0$)
4. **Maximale Beschleunigung**: $a_{\max} = A\omega^2$ (bei $y = \pm A$)

### Die Schwingungsgleichung

Die Beschleunigung erfüllt die Differentialgleichung:

$$y''(t) + \omega^2 y(t) = 0$$

oder

$$\ddot{y} + \omega^2 y = 0$$

Dies ist die **charakteristische Gleichung der harmonischen Schwingung**.

## Physikalische Schwingungssysteme

### Federpendel

Ein Körper der Masse $m$ an einer Feder mit Federkonstante $D$:

$$\omega = \sqrt{\frac{D}{m}}, \quad T = 2\pi\sqrt{\frac{m}{D}}$$

**Beispiel**: $m = 0{,}5\,\text{kg}$, $D = 50\,\frac{\text{N}}{\text{m}}$:

$$T = 2\pi\sqrt{\frac{0{,}5}{50}} = 2\pi \cdot 0{,}1 = 0{,}628\,\text{s}$$

### Fadenpendel (kleine Auslenkungen)

Ein Pendel der Länge $l$:

$$\omega = \sqrt{\frac{g}{l}}, \quad T = 2\pi\sqrt{\frac{l}{g}}$$

**Beispiel**: $l = 1\,\text{m}$:

$$T = 2\pi\sqrt{\frac{1}{9{,}81}} \approx 2{,}01\,\text{s}$$

Das Sekundenpendel ($T = 2\,\text{s}$) hat $l \approx 99{,}4\,\text{cm}$.

## Phasenverschiebung

### Verschiedene Anfangsbedingungen

Je nach Anfangsbedingungen ändert sich die Phase $\varphi_0$:

| Anfangsbedingung | Funktion |
|------------------|----------|
| $y(0) = 0$, $v(0) > 0$ | $y = A\sin(\omega t)$ |
| $y(0) = A$, $v(0) = 0$ | $y = A\cos(\omega t)$ |
| $y(0) = 0$, $v(0) < 0$ | $y = -A\sin(\omega t) = A\sin(\omega t + \pi)$ |
| $y(0) = -A$, $v(0) = 0$ | $y = -A\cos(\omega t) = A\cos(\omega t + \pi)$ |

### Allgemeine Anfangswerte

Bei $y(0) = y_0$ und $v(0) = v_0$:

$$A = \sqrt{y_0^2 + \left(\frac{v_0}{\omega}\right)^2}$$

$$\tan\varphi_0 = \frac{\omega y_0}{v_0}$$

## Gedämpfte Schwingung

### Modell

In realen Systemen wirkt Reibung. Bei geschwindigkeitsproportionaler Dämpfung:

$$y''(t) + 2\gamma y'(t) + \omega_0^2 y(t) = 0$$

wobei $\gamma$ der Dämpfungsfaktor ist.

### Lösung (schwache Dämpfung, $\gamma < \omega_0$)

$$y(t) = A_0 e^{-\gamma t} \sin(\omega_d t + \varphi_0)$$

mit der gedämpften Kreisfrequenz:

$$\omega_d = \sqrt{\omega_0^2 - \gamma^2}$$

### Eigenschaften

- Die Amplitude nimmt exponentiell ab: $A(t) = A_0 e^{-\gamma t}$
- Die Schwingung ist langsamer als ohne Dämpfung: $\omega_d < \omega_0$
- Die **Abklingzeit** $\tau = \frac{1}{\gamma}$ gibt an, nach welcher Zeit die Amplitude auf $\frac{1}{e} \approx 37\%$ gesunken ist

## Erzwungene Schwingung

### Modell

Ein Oszillator wird periodisch angeregt:

$$y''(t) + 2\gamma y'(t) + \omega_0^2 y(t) = F_0 \cos(\omega_E t)$$

### Resonanz

Die Amplitude der erzwungenen Schwingung wird maximal, wenn die Erregerfrequenz $\omega_E$ nahe der Eigenfrequenz $\omega_0$ liegt:

$$A(\omega_E) = \frac{F_0}{\sqrt{(\omega_0^2 - \omega_E^2)^2 + 4\gamma^2 \omega_E^2}}$$

Bei schwacher Dämpfung liegt das Maximum nahe bei $\omega_E \approx \omega_0$ (Resonanzkatastrophe bei $\gamma \to 0$).

## Überlagerung von Schwingungen

### Gleiche Frequenz

Zwei Schwingungen gleicher Frequenz überlagern sich zu einer Schwingung derselben Frequenz:

$$y_1 = A_1 \sin(\omega t + \varphi_1)$$
$$y_2 = A_2 \sin(\omega t + \varphi_2)$$
$$y = y_1 + y_2 = A \sin(\omega t + \varphi)$$

**Spezialfälle**:
- **Gleichphasig** ($\varphi_1 = \varphi_2$): $A = A_1 + A_2$ (konstruktive Interferenz)
- **Gegenphasig** ($|\varphi_1 - \varphi_2| = \pi$): $A = |A_1 - A_2|$ (destruktive Interferenz)

### Schwebung (ähnliche Frequenzen)

Bei $\omega_1 \approx \omega_2$:

$$y = y_1 + y_2 = 2A \cos\left(\frac{\omega_1 - \omega_2}{2}t\right) \sin\left(\frac{\omega_1 + \omega_2}{2}t\right)$$

Die Schwebungsfrequenz ist $f_S = |f_1 - f_2|$.

## Anwendungen

### Wechselstrom

Die Netzspannung in Deutschland:

$$U(t) = U_0 \sin(2\pi \cdot 50 \cdot t) = 325 \sin(100\pi t)\,\text{V}$$

- Amplitude: $U_0 = 325\,\text{V}$
- Effektivwert: $U_{\text{eff}} = \frac{U_0}{\sqrt{2}} = 230\,\text{V}$
- Frequenz: $f = 50\,\text{Hz}$

### Akustik

Ein Kammerton A hat $f = 440\,\text{Hz}$:

$$T = \frac{1}{440} \approx 2{,}27\,\text{ms}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus-und-Kosinus]] — Mathematische Grundlagen
- → [[Trigonometrische-Funktionen]] — Eigenschaften von Sinus und Kosinus
- → [[Periodische-Vorgaenge]] — Allgemeine periodische Funktionen
- → [[Anwendungen-bei-Schwingungen-und-Wellen]] — Physikalische Vertiefung
- → [[Bewegungsmodelle]] — Kinematik und Dynamik

> [!warning] **Prüfungsrelevant**
> - Schwingungsgleichung aus Parametern aufstellen
> - Amplitude, Periode und Frequenz aus Funktionsgleichung ablesen
> - Zusammenhang zwischen Auslenkung, Geschwindigkeit und Beschleunigung
> - Phasenverschiebung interpretieren
> - Graphen von Schwingungsfunktionen zeichnen und analysieren

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie Amplitude, Periode und Frequenz der Schwingung $y(t) = 3\sin(4\pi t + \frac{\pi}{3})$.
> - Zu welchen Zeitpunkten erreicht die Schwingung ihre Maxima?
> - Stellen Sie die Schwingungsgleichung für ein Federpendel mit gegebenen Daten auf.
> - Wie ändert sich die Periode, wenn die Masse verdoppelt wird?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2. Springer Vieweg, 2015
- Tipler, P.A.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019
- ISB Bayern: Lehrplan Mathematik und Physik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Bewegungsmodelle]] — Lineare Bewegungen
> - [[Numerische-Naeherungsverfahren]] — Numerische Lösung von Schwingungsgleichungen
> - [[Vorbereitung-auf-Hochschulmathematik]] — Differentialgleichungen an der Hochschule
