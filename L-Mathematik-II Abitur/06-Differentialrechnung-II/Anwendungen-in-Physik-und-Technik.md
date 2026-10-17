---
author: Andreas Hümmer
title: Anwendungen in Physik und Technik
tags:
  - content
  - mathe
  - differentialrechnung
  - physik
  - anwendungen
created: 2025-06-20
modified: 2025-06-20
---

# Anwendungen in Physik und Technik

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Ableitung als momentane Änderungsrate in physikalischen Kontexten interpretieren können
> - Bewegungsgleichungen analysieren und Geschwindigkeit sowie Beschleunigung berechnen können
> - Differentialrechnung auf technische Problemstellungen anwenden können
> - Den Zusammenhang zwischen mathematischen Konzepten und ihrer physikalischen Bedeutung verstehen

---

## Überblick

Die **Differentialrechnung** wurde ursprünglich zur Lösung physikalischer Probleme entwickelt. Sie ist das zentrale mathematische Werkzeug zur Beschreibung von Bewegungen, Änderungsraten und optimalen Prozessen in Naturwissenschaft und Technik. In diesem Kapitel werden die wichtigsten Anwendungen systematisch vorgestellt.

## Kinematik: Bewegung von Körpern

### Grundbegriffe der Bewegung

Wenn $s(t)$ die Position eines Körpers zur Zeit $t$ beschreibt:

| Größe | Symbol | Definition | Einheit |
|-------|--------|------------|---------|
| Ort (Position) | $s$ | $s(t)$ | m |
| Geschwindigkeit | $v$ | $v(t) = s'(t) = \frac{ds}{dt}$ | m/s |
| Beschleunigung | $a$ | $a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}$ | m/s² |
| Ruck | $j$ | $j(t) = a'(t) = s'''(t)$ | m/s³ |

### Beispiel 1: Freier Fall

Ein Körper fällt aus der Höhe $h_0$ ohne Anfangsgeschwindigkeit.

**Weg-Zeit-Gesetz:**
$$s(t) = h_0 - \frac{1}{2}gt^2$$

**Geschwindigkeit:**
$$v(t) = s'(t) = -gt$$

**Beschleunigung:**
$$a(t) = v'(t) = -g \approx -9{,}81 \, \frac{\text{m}}{\text{s}^2}$$

Die konstante negative Beschleunigung zeigt die gleichmäßige Beschleunigung nach unten.

### Beispiel 2: Schiefer Wurf

Ein Körper wird mit Anfangsgeschwindigkeit $v_0$ unter dem Winkel $\alpha$ geworfen.

**Bahnkurve (parametrisch):**
$$x(t) = v_0 \cos(\alpha) \cdot t$$
$$y(t) = v_0 \sin(\alpha) \cdot t - \frac{1}{2}gt^2$$

**Geschwindigkeitskomponenten:**
$$v_x(t) = x'(t) = v_0 \cos(\alpha) = \text{const.}$$
$$v_y(t) = y'(t) = v_0 \sin(\alpha) - gt$$

**Betrag der Geschwindigkeit:**
$$|v(t)| = \sqrt{v_x^2 + v_y^2}$$

**Höchster Punkt:** $v_y = 0$
$$t_{\text{max}} = \frac{v_0 \sin(\alpha)}{g}$$

### Beispiel 3: Gedämpfte Schwingung

Position eines gedämpft schwingenden Körpers:
$$s(t) = A \cdot e^{-\delta t} \cdot \cos(\omega t)$$

**Geschwindigkeit (Produktregel):**
$$v(t) = A \cdot e^{-\delta t} \cdot (-\delta \cos(\omega t) - \omega \sin(\omega t))$$

Die Amplitude nimmt exponentiell ab – typisch für gedämpfte Systeme.

## Wachstums- und Zerfallsprozesse

### Radioaktiver Zerfall

Die Anzahl $N(t)$ der radioaktiven Kerne folgt:
$$\frac{dN}{dt} = -\lambda N$$

**Lösung:**
$$N(t) = N_0 \cdot e^{-\lambda t}$$

wobei $\lambda$ die Zerfallskonstante ist.

**Halbwertszeit:**
$$T_{1/2} = \frac{\ln 2}{\lambda}$$

### Newton'sches Abkühlungsgesetz

Die Temperatur $T(t)$ eines Körpers in einer Umgebung mit Temperatur $T_U$:
$$\frac{dT}{dt} = -k(T - T_U)$$

**Lösung:**
$$T(t) = T_U + (T_0 - T_U) \cdot e^{-kt}$$

## Elektrotechnik

### Kondensatorentladung

Die Spannung $U(t)$ an einem Kondensator im RC-Glied:
$$U(t) = U_0 \cdot e^{-\frac{t}{RC}}$$

**Strom:**
$$I(t) = C \cdot \frac{dU}{dt} = -\frac{U_0}{R} \cdot e^{-\frac{t}{RC}}$$

Die Zeitkonstante $\tau = RC$ bestimmt die Geschwindigkeit des Entladevorgangs.

### Spule im Gleichstromkreis

Beim Einschalten einer Spule mit Widerstand:
$$I(t) = \frac{U_0}{R}\left(1 - e^{-\frac{R}{L}t}\right)$$

**Änderungsrate des Stroms:**
$$\frac{dI}{dt} = \frac{U_0}{L} \cdot e^{-\frac{R}{L}t}$$

## Technische Optimierung

### Beispiel: Optimaler Anstellwinkel

Ein Flugzeugflügel erzeugt Auftrieb $A(\alpha) = c_A(\alpha) \cdot \frac{\rho}{2} v^2 S$ und Widerstand $W(\alpha)$.

Das optimale Gleiten ergibt sich aus:
$$\frac{d}{d\alpha}\left(\frac{A}{W}\right) = 0$$

### Beispiel: Minimaler Kraftstoffverbrauch

Der Kraftstoffverbrauch pro Kilometer als Funktion der Geschwindigkeit:
$$f(v) = a + bv + \frac{c}{v}$$

**Optimale Geschwindigkeit:**
$$f'(v) = b - \frac{c}{v^2} = 0 \implies v_{\text{opt}} = \sqrt{\frac{c}{b}}$$

## Zusammenfassung: Physikalische Interpretation der Ableitungen

| Stammfunktion | 1. Ableitung | 2. Ableitung |
|---------------|--------------|--------------|
| Weg $s(t)$ | Geschwindigkeit $v(t)$ | Beschleunigung $a(t)$ |
| Ladung $Q(t)$ | Stromstärke $I(t)$ | Änderung der Stromstärke |
| Arbeit $W(s)$ | Kraft $F(s)$ | – |
| Energie | Leistung | – |
| Impuls | Kraft | – |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Hoehere-Ableitungen]] – Beschleunigung als zweite Ableitung
- → [[Exponentielles-Wachstum]] – Wachstums- und Zerfallsprozesse
- → [[Extremwertprobleme]] – Technische Optimierung
- → [[Ableitungen-trigonometrischer-Funktionen]] – Schwingungen
- → [[Momentane-aenderungsrate]] – Grundkonzept

> [!warning] **Prüfungsrelevant**
> - Geschwindigkeit = erste Ableitung des Weges
> - Beschleunigung = zweite Ableitung des Weges = erste Ableitung der Geschwindigkeit
> - Exponentialfunktion bei Wachstum/Zerfall
> - Vorzeichen der Ableitung interpretieren (z.B. negative Beschleunigung = Bremsen)
> - Einheiten bei physikalischen Größen beachten

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie Geschwindigkeit und Beschleunigung aus der Weg-Zeit-Funktion
> - Wann erreicht der Körper die maximale Höhe?
> - Nach welcher Zeit ist die Hälfte der Substanz zerfallen?
> - Interpretieren Sie das Vorzeichen von $s''(t_0)$ im Sachkontext

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Tipler, P.A.; Mosca, G.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019
- ISB Bayern: Lehrplan Mathematik und Physik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Exponentielles-Wachstum]] – Mathematische Grundlagen der Wachstumsmodelle
> - [[Optimierungsaufgaben]] – Weitere technische Anwendungen
