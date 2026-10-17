---
author: Andreas Hümmer
title: Bewegungsmodelle
tags:
  - content
  - mathe
  - modellierung
  - kinematik
  - physik
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Bewegungsmodelle

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Kinematische Größen (Weg, Geschwindigkeit, Beschleunigung) mathematisch verknüpfen
> - Bewegungsgleichungen durch Integration und Differentiation herleiten
> - Wurf- und Fallbewegungen analysieren
> - Reale Bewegungsvorgänge mathematisch modellieren

---

## Überblick

Bewegungsmodelle beschreiben, wie sich Objekte im Raum bewegen. Sie sind ein klassisches Beispiel für die Anwendung der Analysis: Die **Geschwindigkeit** ist die Ableitung des Weges, die **Beschleunigung** ist die Ableitung der Geschwindigkeit. Umgekehrt erhält man durch Integration aus der Beschleunigung die Geschwindigkeit und aus dieser den Weg.

Dieses Kapitel verbindet Differential- und Integralrechnung mit physikalischen Anwendungen und zeigt, wie mathematische Modelle reale Bewegungen beschreiben.

## Grundlegende Zusammenhänge

### Das kinematische Grundprinzip

Für eine eindimensionale Bewegung mit Orts-Zeit-Funktion $s(t)$ gilt:

$$v(t) = \frac{ds}{dt} = s'(t) \quad \text{(Momentangeschwindigkeit)}$$

$$a(t) = \frac{dv}{dt} = v'(t) = s''(t) \quad \text{(Momentanbeschleunigung)}$$

Umgekehrt durch Integration:

$$v(t) = v_0 + \int_0^t a(\tau)\,d\tau$$

$$s(t) = s_0 + \int_0^t v(\tau)\,d\tau$$

### Interpretation der Vorzeichen

| Größe | Positiv | Negativ |
|-------|---------|---------|
| $s(t)$ | Rechts/oben vom Ursprung | Links/unten vom Ursprung |
| $v(t)$ | Bewegung in positive Richtung | Bewegung in negative Richtung |
| $a(t)$ | Beschleunigung | Verzögerung (bei $v > 0$) |

## Gleichförmige Bewegung

### Modell

Bei konstanter Geschwindigkeit $v_0$:

$$a(t) = 0$$
$$v(t) = v_0$$
$$s(t) = s_0 + v_0 \cdot t$$

### Beispiel: Autofahrt

Ein Auto fährt mit konstanter Geschwindigkeit $v = 100\,\frac{\text{km}}{\text{h}} = 27{,}78\,\frac{\text{m}}{\text{s}}$.

Nach $t = 2\,\text{h}$: $s = 100 \cdot 2 = 200\,\text{km}$

## Gleichmäßig beschleunigte Bewegung

### Modell

Bei konstanter Beschleunigung $a$:

$$a(t) = a = \text{const}$$
$$v(t) = v_0 + a \cdot t$$
$$s(t) = s_0 + v_0 \cdot t + \frac{1}{2}a \cdot t^2$$

### Wichtige Spezialfälle

**Freier Fall** (aus der Ruhe, $v_0 = 0$, $s_0 = 0$):
$$v(t) = g \cdot t$$
$$s(t) = \frac{1}{2}g \cdot t^2$$

mit $g \approx 9{,}81\,\frac{\text{m}}{\text{s}^2}$

**Geschwindigkeit-Weg-Beziehung** (eliminiert die Zeit):
$$v^2 = v_0^2 + 2a \cdot s$$

### Beispiel: Bremsung

Ein Auto fährt mit $v_0 = 50\,\frac{\text{km}}{\text{h}} = 13{,}89\,\frac{\text{m}}{\text{s}}$ und bremst mit $a = -5\,\frac{\text{m}}{\text{s}^2}$.

**Bremszeit**: $v(t) = 0 \Rightarrow t = \frac{v_0}{|a|} = \frac{13{,}89}{5} \approx 2{,}78\,\text{s}$

**Bremsweg**: $s = \frac{v_0^2}{2|a|} = \frac{13{,}89^2}{10} \approx 19{,}3\,\text{m}$

## Der senkrechte Wurf

### Wurf nach oben

Ein Körper wird mit Anfangsgeschwindigkeit $v_0 > 0$ senkrecht nach oben geworfen:

$$a(t) = -g$$
$$v(t) = v_0 - g \cdot t$$
$$h(t) = v_0 \cdot t - \frac{1}{2}g \cdot t^2$$

**Steigzeit** (bis $v = 0$):
$$t_S = \frac{v_0}{g}$$

**Maximale Höhe**:
$$h_{\max} = \frac{v_0^2}{2g}$$

**Gesamtflugzeit** (bis zur Rückkehr):
$$t_G = 2t_S = \frac{2v_0}{g}$$

### Beispiel

Ein Ball wird mit $v_0 = 20\,\frac{\text{m}}{\text{s}}$ senkrecht nach oben geworfen.

- Steigzeit: $t_S = \frac{20}{9{,}81} \approx 2{,}04\,\text{s}$
- Maximale Höhe: $h_{\max} = \frac{400}{2 \cdot 9{,}81} \approx 20{,}4\,\text{m}$
- Gesamtflugzeit: $t_G \approx 4{,}08\,\text{s}$

## Der waagerechte Wurf

### Modell

Ein Körper wird aus Höhe $h$ horizontal mit $v_0$ abgeworfen:

**Horizontal** (keine Beschleunigung):
$$x(t) = v_0 \cdot t$$

**Vertikal** (freier Fall):
$$y(t) = h - \frac{1}{2}g \cdot t^2$$

**Bahnkurve** (durch Elimination von $t$):
$$y = h - \frac{g}{2v_0^2} \cdot x^2$$

Die Bahn ist eine nach unten geöffnete Parabel.

### Auftreffgeschwindigkeit

$$v = \sqrt{v_x^2 + v_y^2} = \sqrt{v_0^2 + (gt)^2}$$

### Beispiel

Von einer $5\,\text{m}$ hohen Klippe wird ein Stein horizontal mit $v_0 = 10\,\frac{\text{m}}{\text{s}}$ geworfen.

**Fallzeit**: $5 = \frac{1}{2} \cdot 9{,}81 \cdot t^2 \Rightarrow t \approx 1{,}01\,\text{s}$

**Wurfweite**: $x = 10 \cdot 1{,}01 \approx 10{,}1\,\text{m}$

**Auftreffgeschwindigkeit**: $v = \sqrt{100 + 9{,}81^2 \cdot 1{,}01^2} \approx 14{,}2\,\frac{\text{m}}{\text{s}}$

## Der schiefe Wurf

### Modell

Ein Körper wird unter dem Winkel $\alpha$ zur Horizontalen mit $v_0$ abgeworfen:

**Anfangsgeschwindigkeiten**:
$$v_{0x} = v_0 \cos\alpha, \quad v_{0y} = v_0 \sin\alpha$$

**Bewegungsgleichungen**:
$$x(t) = v_0 \cos\alpha \cdot t$$
$$y(t) = v_0 \sin\alpha \cdot t - \frac{1}{2}g t^2$$

**Bahnkurve**:
$$y = x \tan\alpha - \frac{g}{2v_0^2 \cos^2\alpha} \cdot x^2$$

### Charakteristische Größen

**Wurfweite** (bei Start und Landung auf gleicher Höhe):
$$W = \frac{v_0^2 \sin(2\alpha)}{g}$$

**Maximale Wurfweite** bei $\alpha = 45°$:
$$W_{\max} = \frac{v_0^2}{g}$$

**Maximale Höhe**:
$$H = \frac{v_0^2 \sin^2\alpha}{2g}$$

### Beispiel

Ein Fußball wird mit $v_0 = 25\,\frac{\text{m}}{\text{s}}$ unter $\alpha = 30°$ geschossen.

- Wurfweite: $W = \frac{625 \cdot \sin 60°}{9{,}81} = \frac{625 \cdot 0{,}866}{9{,}81} \approx 55{,}2\,\text{m}$
- Maximale Höhe: $H = \frac{625 \cdot 0{,}25}{19{,}62} \approx 7{,}97\,\text{m}$

## Nicht-konstante Beschleunigung

### Geschwindigkeitsabhängiger Luftwiderstand

In der Realität wirkt oft ein Luftwiderstand proportional zur Geschwindigkeit:

$$a(t) = g - k \cdot v(t)$$

Das führt zur Differentialgleichung:
$$\frac{dv}{dt} = g - kv$$

**Lösung**:
$$v(t) = \frac{g}{k}(1 - e^{-kt})$$

**Grenzgeschwindigkeit**:
$$v_{\infty} = \lim_{t \to \infty} v(t) = \frac{g}{k}$$

### Beispiel: Fallschirmspringer

Mit $g = 9{,}81\,\frac{\text{m}}{\text{s}^2}$ und $k = 0{,}2\,\text{s}^{-1}$:

$$v_{\infty} = \frac{9{,}81}{0{,}2} = 49{,}05\,\frac{\text{m}}{\text{s}} \approx 177\,\frac{\text{km}}{\text{h}}$$

## Kreisbewegung

### Gleichförmige Kreisbewegung

Bei konstantem Radius $r$ und konstanter Winkelgeschwindigkeit $\omega$:

$$x(t) = r \cos(\omega t)$$
$$y(t) = r \sin(\omega t)$$

**Bahngeschwindigkeit**: $v = r \omega$

**Zentripetalbeschleunigung**: $a_z = \frac{v^2}{r} = r\omega^2$

### Beispiel: Karussell

Ein Karussell mit $r = 5\,\text{m}$ dreht sich mit $\omega = 1\,\frac{\text{rad}}{\text{s}}$.

- Bahngeschwindigkeit: $v = 5 \cdot 1 = 5\,\frac{\text{m}}{\text{s}}$
- Zentripetalbeschleunigung: $a_z = 5 \cdot 1^2 = 5\,\frac{\text{m}}{\text{s}^2}$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Weg-Geschwindigkeit-und-Beschleunigung]] — Grundlagen in der Integralrechnung
- → [[Definition-der-Ableitung]] — Mathematische Herleitung
- → [[Trigonometrische-Funktionen]] — Für Kreisbewegungen
- → [[Schwingungsmodelle]] — Periodische Bewegungen
- → [[Anwendungen-in-Physik-und-Technik]] — Weitere physikalische Modelle

> [!warning] **Prüfungsrelevant**
> - Zusammenhang $s \leftrightarrow v \leftrightarrow a$ durch Ableitung/Integration
> - Bewegungsgleichungen für Wurf und Fall aufstellen und lösen
> - Maximale Höhe und Wurfweite berechnen
> - Graphen von $s(t)$, $v(t)$, $a(t)$ interpretieren und zuordnen
> - Anfangsbedingungen korrekt einsetzen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie den Zeitpunkt, an dem der Körper seine maximale Höhe erreicht.
> - Unter welchem Winkel muss geworfen werden, um eine bestimmte Weite zu erreichen?
> - Ordnen Sie die Graphen den kinematischen Größen zu.
> - Berechnen Sie die Auftreffgeschwindigkeit beim Auftreffen auf den Boden.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2014
- Tipler, P.A.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019
- ISB Bayern: Lehrplan Mathematik und Physik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Schwingungsmodelle]] — Harmonische Bewegungen
> - [[Numerische-Naeherungsverfahren]] — Numerische Lösung von Bewegungsgleichungen
> - [[Mathematische-Simulationen]] — Bewegungen simulieren
