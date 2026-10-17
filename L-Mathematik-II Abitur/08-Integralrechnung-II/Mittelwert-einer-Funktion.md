---
author: Andreas Hümmer
title: Mittelwert einer Funktion – Der integrale Mittelwert
tags:
  - content
  - mathe
  - integralrechnung
  - mittelwert
  - analysis
created: 2025-06-26
modified: 2025-06-26
---

# Mittelwert einer Funktion

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den integralen Mittelwert einer Funktion berechnen können
> - Die geometrische Interpretation des Mittelwerts verstehen
> - Den Mittelwertsatz der Integralrechnung kennen und anwenden können
> - Anwendungen des integralen Mittelwerts in Physik und Technik verstehen

---

## Überblick

Der **integrale Mittelwert** (auch: **Flächenmittelwert**) einer Funktion verallgemeinert den Begriff des arithmetischen Mittels auf kontinuierliche Funktionen. Er gibt den "durchschnittlichen Funktionswert" über ein Intervall an und findet vielfältige Anwendungen in Physik, Technik und Wirtschaft.

---

## Definition des integralen Mittelwerts

### Die Formel

Der **integrale Mittelwert** einer stetigen Funktion $f$ über dem Intervall $[a, b]$ ist definiert als:

$$\bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$$

### Herleitung aus dem arithmetischen Mittel

Beim arithmetischen Mittel von $n$ Werten $y_1, y_2, \ldots, y_n$ gilt:

$$\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$$

Für eine stetige Funktion unterteilen wir $[a, b]$ in $n$ Teilintervalle der Breite $\Delta x = \frac{b-a}{n}$:

$$\bar{f} \approx \frac{1}{n} \sum_{i=1}^{n} f(x_i) = \frac{1}{n} \sum_{i=1}^{n} f(x_i) \cdot \frac{b-a}{b-a} = \frac{1}{b-a} \sum_{i=1}^{n} f(x_i) \cdot \Delta x$$

Für $n \to \infty$ wird die Summe zum Integral:

$$\bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$$

---

## Geometrische Interpretation

### Das flächengleiche Rechteck

Der Mittelwert $\bar{f}$ hat eine anschauliche geometrische Bedeutung:

> Das Rechteck mit Höhe $\bar{f}$ und Breite $(b-a)$ hat **dieselbe Fläche** wie die Fläche unter dem Funktionsgraphen im Intervall $[a, b]$.

```
    y ↑
      │     ╭───╮
  f̄  │─────┼───┼─────── Mittelwert
      │    ╱│   │╲
      │  ╱  │   │  ╲
      │╱    │   │    ╲
    ──┼─────┴───┴─────→ x
      a             b
      
      Fläche unter Graph = Fläche des Rechtecks
```

Formal: $\int_a^b f(x) \, dx = \bar{f} \cdot (b-a)$

---

## Der Mittelwertsatz der Integralrechnung

### Satz

Ist $f$ stetig auf $[a, b]$, so existiert mindestens ein $\xi \in [a, b]$ mit:

$$f(\xi) = \bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$$

### Interpretation

Der Funktionsgraph einer stetigen Funktion nimmt seinen Mittelwert mindestens einmal an.

> [!tip] **Merksatz**
> Eine stetige Funktion "durchläuft" ihren Mittelwert – es gibt also immer eine Stelle, an der der Funktionswert gleich dem Durchschnitt ist.

---

## Beispiele

### Beispiel 1: Lineare Funktion

Berechne den Mittelwert von $f(x) = 2x + 1$ im Intervall $[0, 4]$.

**Lösung:**

$$\bar{f} = \frac{1}{4-0} \int_0^4 (2x + 1) \, dx = \frac{1}{4} \left[x^2 + x\right]_0^4$$

$$= \frac{1}{4} (16 + 4 - 0) = \frac{20}{4} = 5$$

**Kontrolle:** Bei einer linearen Funktion ist der Mittelwert der Durchschnitt der Randwerte:
$$\frac{f(0) + f(4)}{2} = \frac{1 + 9}{2} = 5 \checkmark$$

### Beispiel 2: Quadratische Funktion

Berechne den Mittelwert von $f(x) = x^2$ im Intervall $[0, 3]$.

**Lösung:**

$$\bar{f} = \frac{1}{3-0} \int_0^3 x^2 \, dx = \frac{1}{3} \left[\frac{x^3}{3}\right]_0^3 = \frac{1}{3} \cdot 9 = 3$$

**Mittelwertsatz:** Wo nimmt $f(x) = x^2$ den Wert 3 an?
$$x^2 = 3 \Rightarrow x = \sqrt{3} \approx 1{,}73 \in [0, 3] \checkmark$$

### Beispiel 3: Sinusfunktion über eine Periode

Berechne den Mittelwert von $f(x) = \sin x$ im Intervall $[0, 2\pi]$.

**Lösung:**

$$\bar{f} = \frac{1}{2\pi - 0} \int_0^{2\pi} \sin x \, dx = \frac{1}{2\pi} \left[-\cos x\right]_0^{2\pi}$$

$$= \frac{1}{2\pi} (-\cos(2\pi) + \cos(0)) = \frac{1}{2\pi} (-1 + 1) = 0$$

Der Mittelwert der Sinusfunktion über eine volle Periode ist 0 – die positiven und negativen Flächen heben sich auf.

### Beispiel 4: Effektivwert einer Wechselspannung

Für den **Effektivwert** (RMS) einer periodischen Funktion wird das **quadratische Mittel** verwendet:

$$f_{\text{eff}} = \sqrt{\frac{1}{T} \int_0^T [f(t)]^2 \, dt}$$

Für $u(t) = U_0 \sin(\omega t)$:

$$U_{\text{eff}} = \sqrt{\frac{1}{T} \int_0^T U_0^2 \sin^2(\omega t) \, dt}$$

Mit $\sin^2(\omega t) = \frac{1}{2}(1 - \cos(2\omega t))$ und $T = \frac{2\pi}{\omega}$:

$$U_{\text{eff}} = U_0 \sqrt{\frac{1}{2}} = \frac{U_0}{\sqrt{2}} \approx 0{,}707 \cdot U_0$$

Die Netzspannung von 230 V ist ein Effektivwert; die Amplitude beträgt etwa 325 V.

---

## Anwendungen

### Durchschnittstemperatur

Die Temperatur eines Tages sei durch $T(t) = 15 + 8\sin\left(\frac{\pi}{12}(t-6)\right)$ °C beschrieben, wobei $t$ die Stunde ist.

**Durchschnittstemperatur** über 24 Stunden:

$$\bar{T} = \frac{1}{24} \int_0^{24} \left[15 + 8\sin\left(\frac{\pi}{12}(t-6)\right)\right] dt = 15 \text{ °C}$$

(Der Sinusanteil mittelt sich über eine Periode zu null.)

### Durchschnittsgeschwindigkeit

Bewegt sich ein Objekt mit $v(t) = 3t^2$ m/s für $t \in [0, 4]$ s, so ist die Durchschnittsgeschwindigkeit:

$$\bar{v} = \frac{1}{4} \int_0^4 3t^2 \, dt = \frac{1}{4} \cdot \left[t^3\right]_0^4 = \frac{64}{4} = 16 \text{ m/s}$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Grundlage der Mittelwertberechnung
- → [[Stetigkeit|Stetigkeit]] – Voraussetzung für den Mittelwertsatz
- → [[Weg-Geschwindigkeit-und-Beschleunigung|Weg, Geschwindigkeit und Beschleunigung]] – Anwendung in der Kinematik
- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Effektivwert in der Elektrotechnik
- → [[Trigonometrische-Funktionen|Trigonometrische Funktionen]] – Mittelwerte periodischer Funktionen

> [!warning] **Prüfungsrelevant**
> - Die Formel $\bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$ muss sicher beherrscht werden
> - Geometrische Interpretation: Rechteck mit gleicher Fläche
> - Der Mittelwert einer Sinusfunktion über eine volle Periode ist 0
> - Der Effektivwert ist die Wurzel des quadratischen Mittelwerts

> [!question] **Typische Prüfungsfragen**
> - Berechne den Mittelwert der Funktion $f(x) = e^x$ im Intervall $[0, 1]$.
> - Erkläre die geometrische Bedeutung des integralen Mittelwerts.
> - Warum ist der Mittelwert von $\sin x$ über $[0, \pi]$ positiv, aber über $[0, 2\pi]$ gleich null?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Effektivwerte und Mittelwerte in der Elektrotechnik
> - [[Numerische-Integration-Grundlagen|Numerische Integration]] – Näherungsweise Berechnung von Mittelwerten
