---
author: Andreas Hümmer
title: Weg, Geschwindigkeit und Beschleunigung – Kinematik mit Integralen
tags:
  - content
  - mathe
  - integralrechnung
  - kinematik
  - physik
created: 2025-06-26
modified: 2025-06-26
---

# Weg, Geschwindigkeit und Beschleunigung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Zusammenhang zwischen Weg, Geschwindigkeit und Beschleunigung verstehen
> - Aus der Beschleunigung die Geschwindigkeit durch Integration berechnen können
> - Aus der Geschwindigkeit den Weg durch Integration bestimmen können
> - Anfangsbedingungen korrekt einsetzen können

---

## Überblick

Die **Kinematik** beschreibt die Bewegung von Körpern ohne Berücksichtigung der Ursachen (Kräfte). Die drei fundamentalen Größen – **Weg** $s(t)$, **Geschwindigkeit** $v(t)$ und **Beschleunigung** $a(t)$ – sind durch Differentiation und Integration verknüpft:

```
    Differenzieren →
    
s(t)  ──────────→  v(t)  ──────────→  a(t)
      
      ←──────────       ←──────────
      
    ← Integrieren
```

Diese Zusammenhänge sind die Grundlage für alle Bewegungsberechnungen.

---

## Mathematische Zusammenhänge

### Von der Position zur Beschleunigung (Differenzieren)

$$v(t) = \frac{ds}{dt} = s'(t)$$

$$a(t) = \frac{dv}{dt} = v'(t) = s''(t)$$

### Von der Beschleunigung zur Position (Integrieren)

$$v(t) = \int a(t) \, dt + C_1$$

$$s(t) = \int v(t) \, dt + C_2$$

> [!warning] **Wichtig**
> Die Integrationskonstanten $C_1$ und $C_2$ werden durch **Anfangsbedingungen** bestimmt:
> - $v(t_0) = v_0$ (Anfangsgeschwindigkeit)
> - $s(t_0) = s_0$ (Anfangsposition)

---

## Gleichmäßig beschleunigte Bewegung

### Herleitung der Bewegungsgleichungen

Bei **konstanter Beschleunigung** $a(t) = a = \text{const.}$:

**Schritt 1: Integration zur Geschwindigkeit**

$$v(t) = \int a \, dt = at + C_1$$

Mit Anfangsbedingung $v(0) = v_0$:

$$v_0 = a \cdot 0 + C_1 \Rightarrow C_1 = v_0$$

$$\boxed{v(t) = v_0 + at}$$

**Schritt 2: Integration zum Weg**

$$s(t) = \int (v_0 + at) \, dt = v_0 t + \frac{1}{2}at^2 + C_2$$

Mit Anfangsbedingung $s(0) = s_0$:

$$s_0 = 0 + 0 + C_2 \Rightarrow C_2 = s_0$$

$$\boxed{s(t) = s_0 + v_0 t + \frac{1}{2}at^2}$$

### Die drei Bewegungsgleichungen

| Gleichung | Zusammenhang |
|-----------|--------------|
| $v(t) = v_0 + at$ | Geschwindigkeit-Zeit |
| $s(t) = s_0 + v_0 t + \frac{1}{2}at^2$ | Weg-Zeit |
| $v^2 = v_0^2 + 2a(s - s_0)$ | Geschwindigkeit-Weg |

Die dritte Gleichung ergibt sich durch Elimination von $t$.

---

## Beispiele

### Beispiel 1: Freier Fall

Ein Stein fällt aus 45 m Höhe. Wann erreicht er den Boden und mit welcher Geschwindigkeit?

**Gegeben:** $s_0 = 45$ m, $v_0 = 0$, $a = -g = -10$ m/s² (nach unten positiv: $a = g$)

**Annahme:** Koordinatensystem mit positiver Richtung nach unten

$$s(t) = \frac{1}{2}gt^2$$

**Aufprallzeit:**
$$45 = \frac{1}{2} \cdot 10 \cdot t^2 \Rightarrow t^2 = 9 \Rightarrow t = 3 \text{ s}$$

**Aufprallgeschwindigkeit:**
$$v(3) = g \cdot t = 10 \cdot 3 = 30 \text{ m/s}$$

### Beispiel 2: Bremsweg

Ein Auto fährt mit 100 km/h und bremst mit $a = -8$ m/s². Wie lang ist der Bremsweg?

**Umrechnung:** $v_0 = 100 \text{ km/h} = \frac{100}{3{,}6} \approx 27{,}78$ m/s

**Mit der dritten Bewegungsgleichung** (da $v = 0$ am Ende):

$$0 = v_0^2 + 2a \cdot s_{\text{Brems}}$$

$$s_{\text{Brems}} = -\frac{v_0^2}{2a} = -\frac{(27{,}78)^2}{2 \cdot (-8)} = \frac{771{,}6}{16} \approx 48{,}2 \text{ m}$$

---

## Nicht-konstante Beschleunigung

### Zeitabhängige Beschleunigung

Für $a(t) \neq \text{const.}$ müssen die Integrale explizit berechnet werden.

**Beispiel:** Ein Objekt hat die Beschleunigung $a(t) = 6t$ m/s² mit $v(0) = 2$ m/s und $s(0) = 0$.

**Geschwindigkeit:**
$$v(t) = \int 6t \, dt = 3t^2 + C_1$$
$$v(0) = 2 \Rightarrow C_1 = 2$$
$$v(t) = 3t^2 + 2$$

**Weg:**
$$s(t) = \int (3t^2 + 2) \, dt = t^3 + 2t + C_2$$
$$s(0) = 0 \Rightarrow C_2 = 0$$
$$s(t) = t^3 + 2t$$

**Nach 3 Sekunden:**
- $v(3) = 3 \cdot 9 + 2 = 29$ m/s
- $s(3) = 27 + 6 = 33$ m

### Geschwindigkeitsabhängige Beschleunigung

Bei Luftwiderstand ist $a = a(v)$. Hier führt die Trennung der Variablen:

$$a = \frac{dv}{dt} \Rightarrow dt = \frac{dv}{a(v)} \Rightarrow t = \int \frac{dv}{a(v)}$$

---

## Weg als Integral der Geschwindigkeit

### Zurückgelegter Weg vs. Verschiebung

> [!warning] **Wichtig**
> $\int_{t_1}^{t_2} v(t) \, dt$ gibt die **Verschiebung** (mit Vorzeichen), nicht den zurückgelegten Weg!

**Zurückgelegter Weg** (Gesamtstrecke):
$$\text{Weg} = \int_{t_1}^{t_2} |v(t)| \, dt$$

**Beispiel:** Ein Pendel mit $v(t) = 2\sin(t)$ m/s.

Von $t = 0$ bis $t = 2\pi$:

- **Verschiebung:** $\int_0^{2\pi} 2\sin(t) \, dt = [-2\cos(t)]_0^{2\pi} = -2 + 2 = 0$ m
- **Weg:** $\int_0^{2\pi} |2\sin(t)| \, dt = 2 \cdot 2 \cdot 2 = 8$ m

Das Pendel ist wieder am Ausgangspunkt (Verschiebung = 0), hat aber 8 m zurückgelegt.

---

## Graphische Interpretation

### v-t-Diagramm

Im Geschwindigkeit-Zeit-Diagramm:

- **Steigung** = Beschleunigung
- **Fläche unter der Kurve** = Weg (Verschiebung)

```
  v ↑
    │    ╱╲
    │   ╱  ╲      Fläche = Verschiebung
    │  ╱    ╲
    │ ╱      ╲
  ──┼─────────────→ t
    │         ╲
    │          ╲  (negative Fläche = Rückwärtsbewegung)
```

### a-t-Diagramm

Im Beschleunigung-Zeit-Diagramm:

- **Fläche unter der Kurve** = Geschwindigkeitsänderung $\Delta v$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Weitere physikalische Integrale
- → [[Momentane-aenderungsrate|Momentane Änderungsrate]] – Ableitung als Geschwindigkeit
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Mathematische Grundlage
- → [[Stammfunktionen|Stammfunktionen]] – Unbestimmte Integration
- → [[Einfache-Wachstumsmodelle|Einfache Wachstumsmodelle]] – Differentialgleichungen in der Physik

> [!warning] **Prüfungsrelevant**
> - Die Anfangsbedingungen $v_0$ und $s_0$ bestimmen die Integrationskonstanten
> - Unterscheide **Verschiebung** (vorzeichenbehaftet) und **zurückgelegten Weg** (immer positiv)
> - Im v-t-Diagramm: Fläche = Weg, Steigung = Beschleunigung
> - Die Bewegungsgleichungen gelten nur für **konstante** Beschleunigung

> [!question] **Typische Prüfungsfragen**
> - Ein Ball wird mit $v_0 = 20$ m/s senkrecht nach oben geworfen. Wie hoch steigt er und wann kommt er zurück?
> - Die Geschwindigkeit eines Fahrzeugs ist $v(t) = 10 + 2t$ m/s. Wie weit fährt es in den ersten 5 Sekunden?
> - Erkläre den Unterschied zwischen Verschiebung und zurückgelegtem Weg an einem Beispiel.

## Quellen

- Tipler, P. A. / Mosca, G.: Physik für Studierende der Naturwissenschaften und Technik, Springer Spektrum, 2019
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- ISB Bayern: Lehrplan Mathematik und Physik Gymnasium

> [!tip] **Weiterführende Links**
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Arbeit, Energie und Impuls
> - [[Differentialquotient|Differentialquotient]] – Geschwindigkeit als Grenzwert
