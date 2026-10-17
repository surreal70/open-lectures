---
author: Andreas Hümmer
title: Periodische Vorgänge
tags:
  - content
  - mathe
  - trigonometrie
  - periodizitaet
  - schwingungen
  - anwendungen
created: 2025-06-20
modified: 2025-06-20
---

# Periodische Vorgänge

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Periodische Vorgänge in Natur und Technik erkennen und beschreiben können
> - Die mathematische Modellierung mit trigonometrischen Funktionen verstehen
> - Die Begriffe Periode, Frequenz und Amplitude im Kontext anwenden können
> - Reale Daten durch trigonometrische Funktionen approximieren können

---

## Überblick

**Periodische Vorgänge** sind Prozesse, die sich in regelmäßigen Zeitabständen wiederholen. Sie begegnen uns überall in Natur und Technik: vom Herzschlag über Gezeiten bis zu Wechselstrom. Die mathematische Beschreibung solcher Vorgänge erfolgt durch **periodische Funktionen**, insbesondere durch Sinus- und Kosinusfunktionen.

## Definition der Periodizität

### Mathematische Definition

Eine Funktion $f: \mathbb{R} \to \mathbb{R}$ heißt **periodisch** mit **Periode** $T > 0$, wenn für alle $x \in \mathbb{R}$ gilt:

$$f(x + T) = f(x)$$

Die **kleinste** positive Zahl $T$ mit dieser Eigenschaft heißt **primitive Periode** oder **Grundperiode**.

### Eigenschaften periodischer Funktionen

- Der Graph wiederholt sich alle $T$ Einheiten
- Kennt man die Funktion auf einem Intervall der Länge $T$, kennt man sie überall
- Summen und Produkte periodischer Funktionen mit gleicher Periode sind wieder periodisch

## Kenngrößen periodischer Vorgänge

### Periode $T$

Die **Periode** ist die Zeitdauer für einen vollständigen Zyklus.

**Einheit:** Sekunde (s) bei zeitabhängigen Vorgängen

**Beispiele:**
- Erdrotation: $T = 24$ h
- Herzschlag (Ruhe): $T \approx 1$ s
- Netzfrequenz: $T = 0{,}02$ s (bei 50 Hz)

### Frequenz $f$

Die **Frequenz** ist die Anzahl der Zyklen pro Zeiteinheit:

$$f = \frac{1}{T}$$

**Einheit:** Hertz (Hz) = $\frac{1}{\text{s}}$

**Beispiele:**
- Kammerton A: $f = 440$ Hz
- Netzfrequenz (Europa): $f = 50$ Hz
- Ultraschall: $f > 20\,000$ Hz

### Kreisfrequenz $\omega$

Die **Kreisfrequenz** (Winkelgeschwindigkeit) verbindet Frequenz und Bogenmaß:

$$\omega = 2\pi f = \frac{2\pi}{T}$$

**Einheit:** $\frac{\text{rad}}{\text{s}}$

In physikalischen Formeln erscheint oft:
$$f(t) = A\sin(\omega t + \varphi)$$

### Amplitude $A$

Die **Amplitude** ist die maximale Auslenkung aus der Ruhelage:

$$A = \frac{y_{\max} - y_{\min}}{2}$$

**Beispiele:**
- Meereswellen: $A$ kann mehrere Meter betragen
- Schall: $A$ entspricht dem Schalldruck (bestimmt die Lautstärke)
- Wechselspannung: $A = U_0$ (Scheitelspannung)

## Beispiele periodischer Vorgänge

### Tageslänge im Jahresverlauf

Die Tageslänge schwankt periodisch mit der Periode $T = 1$ Jahr:

$$L(t) = L_0 + A \cdot \cos\left(\frac{2\pi}{365}(t - t_0)\right)$$

wobei:
- $L_0$ = mittlere Tageslänge (ca. 12 h)
- $A$ = Amplitude (abhängig vom Breitengrad)
- $t_0$ = Tag der Sommersonnenwende

### Gezeiten

Ebbe und Flut folgen näherungsweise einer Sinusfunktion:

$$h(t) = h_0 + A \cdot \cos\left(\frac{2\pi}{T}(t - t_{\text{HW}})\right)$$

mit:
- $h_0$ = mittlerer Wasserstand
- $A$ = Tidenhub / 2
- $T \approx 12{,}42$ h (halber Mondtag)
- $t_{\text{HW}}$ = Zeitpunkt des Hochwassers

### Wechselstrom

Die Netzspannung in Europa:

$$u(t) = U_0 \cdot \sin(2\pi \cdot 50 \cdot t)$$

mit:
- $U_0 = 325$ V (Scheitelspannung)
- Frequenz: 50 Hz
- Effektivwert: $U_{\text{eff}} = \frac{U_0}{\sqrt{2}} \approx 230$ V

### Federpendel

Die Auslenkung eines schwingenden Federpendels:

$$x(t) = A \cdot \cos(\omega_0 t + \varphi_0)$$

mit der Eigenkreisfrequenz:

$$\omega_0 = \sqrt{\frac{k}{m}}$$

wobei $k$ die Federkonstante und $m$ die Masse ist.

## Modellierung mit trigonometrischen Funktionen

### Allgemeines Vorgehen

1. **Daten erfassen:** Messwerte über mindestens eine Periode sammeln
2. **Parameter bestimmen:**
   - Mittelwert: $d = \frac{y_{\max} + y_{\min}}{2}$
   - Amplitude: $A = \frac{y_{\max} - y_{\min}}{2}$
   - Periode: Abstand zwischen gleichen Zuständen
3. **Phasenlage festlegen:** Wo beginnt der Zyklus?
4. **Funktionsgleichung aufstellen:**
   $$f(t) = A \cdot \sin\left(\frac{2\pi}{T}(t - t_0)\right) + d$$

### Beispiel: Temperaturverlauf

Die Tagesdurchschnittstemperatur in einer Stadt schwankt im Jahresverlauf:
- Maximum im Juli: 22°C
- Minimum im Januar: 2°C

Modell:
- $d = \frac{22 + 2}{2} = 12°C$
- $A = \frac{22 - 2}{2} = 10°C$
- $T = 365$ Tage
- Maximum bei Tag 200 (ca. 20. Juli)

$$T(t) = 10 \cdot \cos\left(\frac{2\pi}{365}(t - 200)\right) + 12$$

## Superposition von Schwingungen

### Gleiche Frequenz

Die Summe zweier Sinusschwingungen gleicher Frequenz ist wieder eine Sinusschwingung:

$$A_1\sin(\omega t) + A_2\cos(\omega t) = A\sin(\omega t + \varphi)$$

mit:
$$A = \sqrt{A_1^2 + A_2^2}$$
$$\tan(\varphi) = \frac{A_2}{A_1}$$

### Schwebung (leicht verschiedene Frequenzen)

Bei Überlagerung von Schwingungen mit leicht unterschiedlichen Frequenzen entsteht eine **Schwebung**:

$$\sin(\omega_1 t) + \sin(\omega_2 t) = 2\cos\left(\frac{\omega_1 - \omega_2}{2}t\right) \cdot \sin\left(\frac{\omega_1 + \omega_2}{2}t\right)$$

Die Amplitude schwankt mit der **Schwebungsfrequenz** $f_S = |f_1 - f_2|$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus--und-Kosinusfunktionen]] – Mathematische Grundlagen
- → [[Phasenverschiebung]] – Verschiebung im Zeitverlauf
- → [[Anwendungen-bei-Schwingungen-und-Wellen]] – Physikalische Vertiefung
- → [[Einheitskreis]] – Geometrische Interpretation

> [!warning] **Prüfungsrelevant**
> - Zusammenhang $f = \frac{1}{T}$ und $\omega = 2\pi f$
> - Parameter aus Beschreibungen oder Graphen ablesen können
> - Funktionsgleichungen für reale periodische Vorgänge aufstellen
> - Amplitude und Mittelwert aus Maximum/Minimum berechnen

> [!question] **Typische Prüfungsfragen**
> - Die Temperatur schwankt zwischen 5°C und 25°C mit einer Periode von 24 Stunden. Stellen Sie eine passende Funktion auf.
> - Ein Ton hat die Frequenz 440 Hz. Wie groß ist die Periode?
> - Beschreiben Sie, wie sich die Graphen zweier Sinusschwingungen mit leicht verschiedenen Frequenzen überlagern.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Tipler, P.A. & Mosca, G.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.

> [!tip] **Weiterführende Links**
> - [[Anwendungen-bei-Schwingungen-und-Wellen]] – Physikalische Anwendungen
> - [[Sinus--und-Kosinusfunktionen]] – Detaillierte Parameteranalyse
