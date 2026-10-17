---
author: Andreas Hümmer
title: Anwendungen der Integralrechnung in der Physik
tags:
  - content
  - mathe
  - integralrechnung
  - physik
  - anwendung
created: 2025-06-26
modified: 2025-06-26
---

# Anwendungen in der Physik

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die physikalische Arbeit als Integral der Kraft berechnen können
> - Energie bei veränderlicher Kraft bestimmen können
> - Den Schwerpunkt eines Körpers mit Integralen berechnen können
> - Physikalische Größen durch Integration von Raten ermitteln können

---

## Überblick

Die Integralrechnung ist eines der wichtigsten mathematischen Werkzeuge der Physik. Viele physikalische Größen sind als **Integrale** definiert oder lassen sich durch Integration berechnen:

- **Arbeit** = Integral der Kraft über den Weg
- **Impuls** = Integral der Kraft über die Zeit
- **Ladung** = Integral des Stroms über die Zeit
- **Schwerpunkt** = gewichtetes Integral der Koordinaten

Die Integralrechnung verbindet **differentielle** (lokale, momentane) Größen mit **globalen** (akkumulierten) Größen.

---

## Arbeit bei veränderlicher Kraft

### Konstante Kraft (Wiederholung)

Bei konstanter Kraft $F$ und Verschiebung $s$ gilt:

$$W = F \cdot s$$

### Ortsabhängige Kraft

Wenn die Kraft vom Ort abhängt, $F = F(x)$, ergibt sich die Arbeit als:

$$W = \int_a^b F(x) \, dx$$

```
  F(x) ↑
       │    ╭──────╮
       │   ╱        ╲
       │  ╱   W      ╲
       │ ╱            ╲
     ──┼──────────────────→ x
       a              b
       
    Arbeit = Fläche unter der Kraft-Weg-Kurve
```

### Beispiel: Federarbeit

Eine Feder mit Federkonstante $k$ übt die Kraft $F(x) = -kx$ aus (Hooke'sches Gesetz).

Die Arbeit, um die Feder von $x = 0$ auf $x = s$ zu dehnen:

$$W = \int_0^s kx \, dx = k \left[\frac{x^2}{2}\right]_0^s = \frac{1}{2}ks^2$$

Dies ist die **Spannenergie** der Feder.

### Beispiel: Gravitationsarbeit

Die Gravitationskraft zwischen zwei Massen ist:

$$F(r) = G \frac{m_1 m_2}{r^2}$$

Die Arbeit, um eine Masse von $r_1$ auf $r_2 > r_1$ zu heben:

$$W = \int_{r_1}^{r_2} G \frac{m_1 m_2}{r^2} \, dr = Gm_1 m_2 \left[-\frac{1}{r}\right]_{r_1}^{r_2}$$

$$= Gm_1 m_2 \left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$

---

## Energie und Potential

### Potentielle Energie

Die potentielle Energie $E_{\text{pot}}$ hängt mit der Kraft durch Integration zusammen:

$$E_{\text{pot}}(x) = -\int F(x) \, dx$$

Oder umgekehrt:

$$F(x) = -\frac{dE_{\text{pot}}}{dx}$$

### Beispiel: Gravitationspotential in Erdnähe

Mit $F = -mg$ (nach unten gerichtet):

$$E_{\text{pot}}(h) = -\int (-mg) \, dh = mgh + C$$

Wählt man $E_{\text{pot}}(0) = 0$, so ist $E_{\text{pot}}(h) = mgh$.

---

## Schwerpunkt

### Schwerpunkt einer eindimensionalen Massenverteilung

Für eine kontinuierliche Massenverteilung mit Dichte $\rho(x)$ auf $[a, b]$:

**Gesamtmasse:**
$$m = \int_a^b \rho(x) \, dx$$

**Schwerpunktkoordinate:**
$$\bar{x} = \frac{1}{m} \int_a^b x \cdot \rho(x) \, dx$$

### Beispiel: Stab mit variabler Dichte

Ein Stab von $x = 0$ bis $x = L$ hat die Dichte $\rho(x) = \rho_0 \cdot x$ (linear zunehmend).

**Gesamtmasse:**
$$m = \int_0^L \rho_0 x \, dx = \rho_0 \frac{L^2}{2}$$

**Schwerpunkt:**
$$\bar{x} = \frac{1}{m} \int_0^L x \cdot \rho_0 x \, dx = \frac{2}{\rho_0 L^2} \cdot \rho_0 \int_0^L x^2 \, dx$$

$$= \frac{2}{L^2} \cdot \frac{L^3}{3} = \frac{2L}{3}$$

Der Schwerpunkt liegt bei $\frac{2}{3}$ der Stablänge (näher am dichteren Ende).

### Flächenschwerpunkt

Für eine Fläche unter $f(x) \geq 0$ auf $[a, b]$:

$$\bar{x} = \frac{\int_a^b x \cdot f(x) \, dx}{\int_a^b f(x) \, dx}, \quad \bar{y} = \frac{\frac{1}{2}\int_a^b [f(x)]^2 \, dx}{\int_a^b f(x) \, dx}$$

---

## Trägheitsmoment

Das **Trägheitsmoment** beschreibt den Widerstand eines Körpers gegen Drehbeschleunigung.

### Definition

$$I = \int r^2 \, dm$$

wobei $r$ der Abstand von der Drehachse ist.

### Beispiel: Vollzylinder

Ein Vollzylinder mit Radius $R$, Länge $L$ und Dichte $\rho$ rotiert um seine Symmetrieachse.

In Zylinderkoordinaten mit $dm = \rho \cdot 2\pi r \cdot L \, dr$:

$$I = \int_0^R r^2 \cdot \rho \cdot 2\pi r \cdot L \, dr = 2\pi \rho L \int_0^R r^3 \, dr$$

$$= 2\pi \rho L \cdot \frac{R^4}{4} = \frac{\pi \rho L R^4}{2}$$

Mit der Masse $m = \rho \cdot \pi R^2 L$:

$$I = \frac{1}{2}mR^2$$

---

## Elektrische Ladung und Strom

### Ladung als Integral des Stroms

Der elektrische Strom $I(t)$ ist die Ladung pro Zeit:

$$I = \frac{dQ}{dt}$$

Umgekehrt:

$$Q = \int_{t_1}^{t_2} I(t) \, dt$$

### Beispiel

Ein zeitabhängiger Strom $I(t) = I_0 e^{-t/\tau}$ fließt ab $t = 0$.

Die nach unendlich langer Zeit geflossene Gesamtladung:

$$Q = \int_0^{\infty} I_0 e^{-t/\tau} \, dt = I_0 \left[-\tau e^{-t/\tau}\right]_0^{\infty} = I_0 \tau$$

---

## Übersicht: Physikalische Integrale

| Physikalische Größe | Integral | Differentialzusammenhang |
|---------------------|----------|--------------------------|
| Arbeit | $W = \int F \, dx$ | $F = \frac{dW}{dx}$ |
| Impuls | $p = \int F \, dt$ | $F = \frac{dp}{dt}$ |
| Ladung | $Q = \int I \, dt$ | $I = \frac{dQ}{dt}$ |
| Weg | $s = \int v \, dt$ | $v = \frac{ds}{dt}$ |
| Geschwindigkeit | $v = \int a \, dt$ | $a = \frac{dv}{dt}$ |
| Energie | $E = -\int F \, dx$ | $F = -\frac{dE}{dx}$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Weg-Geschwindigkeit-und-Beschleunigung|Weg, Geschwindigkeit und Beschleunigung]] – Kinematik mit Integralen
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Mathematische Grundlage
- → [[Mittelwert-einer-Funktion|Mittelwert einer Funktion]] – Effektivwerte in der Elektrotechnik
- → [[Rotationskoerper|Rotationskörper]] – Volumen und Trägheitsmomente
- → [[Einfache-Wachstumsmodelle|Einfache Wachstumsmodelle]] – Zeitliche Entwicklung physikalischer Systeme

> [!warning] **Prüfungsrelevant**
> - Arbeit = Fläche unter der Kraft-Weg-Kurve
> - Federenergie: $E = \frac{1}{2}kx^2$ (aus Integration der Federkraft)
> - Die Beziehung $F = -\frac{dE_{\text{pot}}}{dx}$ verbindet Kraft und Potential
> - Schwerpunktberechnung: $\bar{x} = \frac{\int x \cdot \rho(x) \, dx}{\int \rho(x) \, dx}$

> [!question] **Typische Prüfungsfragen**
> - Eine Kraft $F(x) = 3x^2$ N wirkt auf einen Körper. Berechne die Arbeit bei Verschiebung von $x = 1$ m bis $x = 4$ m.
> - Erkläre, warum die potentielle Energie das negative Integral der Kraft ist.
> - Ein Stab hat die Dichte $\rho(x) = 2 + x$ kg/m für $x \in [0, 3]$ m. Wo liegt sein Schwerpunkt?

## Quellen

- Tipler, P. A. / Mosca, G.: Physik für Studierende der Naturwissenschaften und Technik, Springer Spektrum, 2019
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- ISB Bayern: Lehrplan Mathematik und Physik Gymnasium

> [!tip] **Weiterführende Links**
> - [[Weg-Geschwindigkeit-und-Beschleunigung|Weg, Geschwindigkeit und Beschleunigung]] – Vertiefung der Kinematik
> - [[Einfache-Wachstumsmodelle|Einfache Wachstumsmodelle]] – Differentialgleichungen in der Physik
