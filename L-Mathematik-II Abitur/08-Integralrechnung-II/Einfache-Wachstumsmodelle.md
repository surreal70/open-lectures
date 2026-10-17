---
author: Andreas Hümmer
title: Einfache Wachstumsmodelle – Differentialgleichungen und exponentielles Wachstum
tags:
  - content
  - mathe
  - integralrechnung
  - differentialgleichungen
  - wachstum
created: 2025-06-26
modified: 2025-06-26
---

# Einfache Wachstumsmodelle

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Einfache Differentialgleichungen erster Ordnung verstehen und lösen können
> - Das Modell des exponentiellen Wachstums/Zerfalls anwenden können
> - Das begrenzte Wachstum (Sättigungsmodell) beschreiben können
> - Halbwertszeit und Verdopplungszeit berechnen können

---

## Überblick

**Wachstumsmodelle** beschreiben, wie sich Größen über die Zeit verändern. Mathematisch werden sie oft durch **Differentialgleichungen** ausgedrückt – Gleichungen, die eine Funktion und ihre Ableitung(en) enthalten.

Die Integration ist das Werkzeug zur **Lösung** dieser Gleichungen und ermöglicht Vorhersagen über zukünftige Entwicklungen.

Typische Anwendungen:
- Bevölkerungswachstum
- Radioaktiver Zerfall
- Abkühlung/Erwärmung
- Wirtschaftswachstum
- Medikamentenabbau im Körper

---

## Exponentielles Wachstum und Zerfall

### Die Differentialgleichung

Das einfachste Wachstumsmodell basiert auf der Annahme:

> Die **Änderungsrate** einer Größe ist **proportional** zu ihrem aktuellen Wert.

Mathematisch:

$$\frac{dN}{dt} = k \cdot N$$

wobei:
- $N(t)$ = Bestand zur Zeit $t$
- $k$ = Wachstumskonstante ($k > 0$: Wachstum, $k < 0$: Zerfall)

### Lösung durch Trennung der Variablen

**Schritt 1:** Variablen trennen

$$\frac{dN}{N} = k \, dt$$

**Schritt 2:** Beide Seiten integrieren

$$\int \frac{1}{N} \, dN = \int k \, dt$$

$$\ln|N| = kt + C$$

**Schritt 3:** Nach $N$ auflösen

$$N = e^{kt + C} = e^C \cdot e^{kt}$$

**Schritt 4:** Anfangsbedingung einsetzen

Mit $N(0) = N_0$: $N_0 = e^C$

$$\boxed{N(t) = N_0 \cdot e^{kt}}$$

### Exponentielles Wachstum ($k > 0$)

```
  N ↑
    │                    ╱
    │                  ╱
    │                ╱
    │            ╱──
    │        ╱──
    │    ╱──
    │╱──
  ──┼───────────────────→ t
   N₀
```

**Verdopplungszeit** $T_2$:

$$N(T_2) = 2N_0 \Rightarrow N_0 e^{kT_2} = 2N_0 \Rightarrow T_2 = \frac{\ln 2}{k}$$

### Exponentieller Zerfall ($k < 0$)

Mit $k = -\lambda$ ($\lambda > 0$ = Zerfallskonstante):

$$N(t) = N_0 \cdot e^{-\lambda t}$$

```
  N ↑
   N₀ ●──╲
    │     ╲──
    │         ╲──
    │             ╲──────
    │                    ───
  ──┼───────────────────────→ t
```

**Halbwertszeit** $T_{1/2}$:

$$N(T_{1/2}) = \frac{N_0}{2} \Rightarrow e^{-\lambda T_{1/2}} = \frac{1}{2} \Rightarrow T_{1/2} = \frac{\ln 2}{\lambda}$$

---

## Beispiele

### Beispiel 1: Bakterienwachstum

Eine Bakterienkultur verdoppelt sich alle 3 Stunden. Zu Beginn sind 1000 Bakterien vorhanden.

**Wachstumskonstante:**
$$k = \frac{\ln 2}{T_2} = \frac{\ln 2}{3} \approx 0{,}231 \text{ h}^{-1}$$

**Wachstumsfunktion:**
$$N(t) = 1000 \cdot e^{0{,}231t}$$

**Nach 10 Stunden:**
$$N(10) = 1000 \cdot e^{2{,}31} \approx 10\,079 \text{ Bakterien}$$

### Beispiel 2: Radioaktiver Zerfall

Kohlenstoff-14 hat eine Halbwertszeit von 5730 Jahren. Ein Fossil enthält noch 25% des ursprünglichen C-14-Gehalts.

**Zerfallskonstante:**
$$\lambda = \frac{\ln 2}{5730} \approx 1{,}21 \cdot 10^{-4} \text{ a}^{-1}$$

**Alter bestimmen:**
$$\frac{N}{N_0} = e^{-\lambda t} = 0{,}25$$

$$t = -\frac{\ln 0{,}25}{\lambda} = \frac{\ln 4}{1{,}21 \cdot 10^{-4}} \approx 11\,460 \text{ Jahre}$$

(Das entspricht zwei Halbwertszeiten: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.)

---

## Begrenztes Wachstum (Sättigungsmodell)

### Die Differentialgleichung

In vielen realen Situationen ist das Wachstum durch eine **Kapazitätsgrenze** $G$ begrenzt:

$$\frac{dN}{dt} = k \cdot (G - N)$$

Die Änderungsrate ist proportional zum "Abstand" zur Grenze.

### Lösung

Durch Trennung der Variablen und Integration:

$$\int \frac{dN}{G - N} = \int k \, dt$$

$$-\ln|G - N| = kt + C$$

Mit $N(0) = N_0$:

$$\boxed{N(t) = G - (G - N_0) \cdot e^{-kt}}$$

Oder äquivalent:

$$N(t) = G \cdot (1 - e^{-kt}) + N_0 \cdot e^{-kt}$$

### Graphische Darstellung

```
  N ↑
  G │─────────────────────────
    │            ──────────
    │        ────
    │      ╱
    │    ╱
    │  ╱
    │╱
  ──┼───────────────────────→ t
   N₀
   
   Sättigung: N → G für t → ∞
```

### Beispiel: Newton'sches Abkühlungsgesetz

Ein Körper mit Anfangstemperatur $T_0$ kühlt in einer Umgebung mit Temperatur $T_U$ ab:

$$\frac{dT}{dt} = -k(T - T_U)$$

**Lösung:**
$$T(t) = T_U + (T_0 - T_U) \cdot e^{-kt}$$

**Beispiel:** Kaffee ($T_0 = 90°$C) kühlt bei Raumtemperatur ($T_U = 20°$C) mit $k = 0{,}1$ min$^{-1}$ ab.

$$T(t) = 20 + 70 \cdot e^{-0{,}1t}$$

Nach 10 Minuten: $T(10) = 20 + 70 \cdot e^{-1} \approx 45{,}8°$C

---

## Logistisches Wachstum (Ausblick)

Für noch realistischere Modelle kombiniert man exponentielles und begrenztes Wachstum:

$$\frac{dN}{dt} = k \cdot N \cdot \left(1 - \frac{N}{G}\right)$$

Die Lösung ist die **logistische Funktion** (S-Kurve):

$$N(t) = \frac{G}{1 + \left(\frac{G - N_0}{N_0}\right) e^{-kt}}$$

---

## Übersicht: Wachstumsmodelle

| Modell | Differentialgleichung | Lösung | Anwendung |
|--------|----------------------|--------|-----------|
| Exponentielles Wachstum | $\frac{dN}{dt} = kN$ | $N = N_0 e^{kt}$ | Bakterien, Zinsen |
| Exponentieller Zerfall | $\frac{dN}{dt} = -\lambda N$ | $N = N_0 e^{-\lambda t}$ | Radioaktivität |
| Begrenztes Wachstum | $\frac{dN}{dt} = k(G-N)$ | $N = G - (G-N_0)e^{-kt}$ | Abkühlung, Lernen |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentielles-Wachstum|Exponentielles Wachstum]] – Differentialrechnung-Perspektive
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Die zugrundeliegende Funktionsklasse
- → [[Logarithmusfunktionen|Logarithmusfunktionen]] – Zur Lösung der Gleichungen
- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Radioaktivität, Abkühlung
- → [[Substitution|Substitution]] – Integrationstechnik für Differentialgleichungen

> [!warning] **Prüfungsrelevant**
> - $N(t) = N_0 \cdot e^{kt}$ ist die Lösung von $\frac{dN}{dt} = kN$
> - Verdopplungszeit: $T_2 = \frac{\ln 2}{k}$, Halbwertszeit: $T_{1/2} = \frac{\ln 2}{\lambda}$
> - Begrenztes Wachstum strebt gegen die Sättigungsgrenze $G$
> - Bei der C-14-Methode wird das Alter aus dem Restgehalt berechnet

> [!question] **Typische Prüfungsfragen**
> - Eine Bakterienkultur wächst exponentiell mit $k = 0{,}5$ h⁻¹. Nach wie vielen Stunden hat sich der Bestand verzehnfacht?
> - Radium-226 hat eine Halbwertszeit von 1600 Jahren. Wie viel Prozent sind nach 4000 Jahren noch vorhanden?
> - Ein Körper kühlt von 80°C auf 50°C in einer 20°C warmen Umgebung in 10 Minuten ab. Wann erreicht er 30°C?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Exponentialfunktionen|Exponentialfunktionen]] – Eigenschaften der $e$-Funktion
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Weitere physikalische Modelle
