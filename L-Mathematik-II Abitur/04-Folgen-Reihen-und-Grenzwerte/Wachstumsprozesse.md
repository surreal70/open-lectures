---
author: Andreas Hümmer
title: Wachstumsprozesse
tags:
  - content
  - mathe
  - folgen
  - wachstum
  - modellierung
  - exponentiell
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Wachstumsprozesse

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verschiedene Wachstumsmodelle unterscheiden können
> - Lineares, exponentielles und begrenztes Wachstum mathematisch beschreiben können
> - Wachstumsprozesse mit Folgen und Funktionen modellieren können
> - Parameter aus gegebenen Daten bestimmen können
> - Prognosen auf Basis von Wachstumsmodellen erstellen können

---

## Überblick

**Wachstumsprozesse** beschreiben, wie sich Größen über die Zeit verändern. Die mathematische Modellierung solcher Prozesse ist zentral für Anwendungen in Biologie (Populationen), Wirtschaft (Kapitalentwicklung), Medizin (Medikamentenabbau) und Physik (radioaktiver Zerfall). Je nach Art des Prozesses kommen unterschiedliche Modelle zum Einsatz.

## Lineares Wachstum

### Charakterisierung

Beim **linearen Wachstum** ist die **absolute Änderung pro Zeiteinheit konstant**.

$$\Delta N = N(t+1) - N(t) = m = \text{const.}$$

### Mathematische Beschreibung

**Rekursiv:** $N_{n+1} = N_n + m$ mit Startwert $N_0$

**Explizit (diskret):** $N_n = N_0 + m \cdot n$

**Kontinuierlich:** $N(t) = N_0 + m \cdot t$

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Wachstumsrate | $m$ (konstant) |
| Verdopplung | nicht konstant |
| Graph | Gerade mit Steigung $m$ |
| Typische Anwendung | Gleichmäßige Produktion, konstante Einsparungen |

### Beispiel: Sparplan

Monatliche Einzahlung von 100 € auf ein Konto (ohne Zinsen):

- $N_0 = 0$, $m = 100$
- Nach $n$ Monaten: $N_n = 100n$ €
- Nach 5 Jahren (60 Monaten): $N_{60} = 6000$ €

## Exponentielles Wachstum

### Charakterisierung

Beim **exponentiellen Wachstum** ist die **relative Änderung pro Zeiteinheit konstant** (prozentuale Zunahme/Abnahme).

$$\frac{N(t+1) - N(t)}{N(t)} = r = \text{const.}$$

Äquivalent: $N(t+1) = N(t) \cdot (1 + r) = N(t) \cdot q$

### Mathematische Beschreibung

**Rekursiv:** $N_{n+1} = N_n \cdot q$ mit Startwert $N_0$

**Explizit (diskret):** $N_n = N_0 \cdot q^n$

**Kontinuierlich:** $N(t) = N_0 \cdot e^{kt}$ mit $k = \ln(q)$

### Wachstumsfaktor und Wachstumsrate

| Größe | Symbol | Beziehung |
|-------|--------|-----------|
| Wachstumsrate | $r$ | prozentuale Änderung pro Zeiteinheit |
| Wachstumsfaktor | $q$ | $q = 1 + r$ |
| Wachstumskonstante | $k$ | $k = \ln(q)$ |

**Wachstum:** $q > 1$ (bzw. $r > 0$, $k > 0$)
**Zerfall:** $0 < q < 1$ (bzw. $r < 0$, $k < 0$)

### Verdopplungszeit und Halbwertszeit

**Verdopplungszeit** (bei Wachstum, $q > 1$):
$$T_2 : N_0 \cdot q^{T_2} = 2N_0 \quad \Rightarrow \quad T_2 = \frac{\ln 2}{\ln q}$$

**Halbwertszeit** (bei Zerfall, $0 < q < 1$):
$$T_{1/2} : N_0 \cdot q^{T_{1/2}} = \frac{N_0}{2} \quad \Rightarrow \quad T_{1/2} = \frac{\ln 2}{-\ln q} = \frac{\ln 2}{\ln(1/q)}$$

### Beispiel: Bakterienwachstum

Eine Bakterienkultur verdoppelt sich alle 3 Stunden. Anfangs sind 500 Bakterien vorhanden.

- Verdopplungszeit: $T_2 = 3$ h
- Wachstumsfaktor pro Stunde: $q^3 = 2 \Rightarrow q = \sqrt[3]{2} \approx 1,26$
- Nach $t$ Stunden: $N(t) = 500 \cdot 2^{t/3}$
- Nach 12 Stunden: $N(12) = 500 \cdot 2^4 = 8000$

### Beispiel: Radioaktiver Zerfall

Ein radioaktives Isotop hat eine Halbwertszeit von 5 Jahren. Anfangs sind 200 g vorhanden.

- Nach $t$ Jahren: $N(t) = 200 \cdot \left(\frac{1}{2}\right)^{t/5}$
- Nach 15 Jahren: $N(15) = 200 \cdot \left(\frac{1}{2}\right)^3 = 25$ g
- Wann sind noch 10 g übrig?
  $$10 = 200 \cdot \left(\frac{1}{2}\right)^{t/5} \Rightarrow \frac{1}{20} = \left(\frac{1}{2}\right)^{t/5}$$
  $$t = 5 \cdot \frac{\ln(20)}{\ln(2)} \approx 21,6 \text{ Jahre}$$

## Begrenztes Wachstum

### Charakterisierung

Beim **begrenzten Wachstum** nähert sich die Größe einer **Sättigungsgrenze** $S$ (Kapazität, Schranke). Die Änderung ist proportional zur "Restkapazität" $S - N(t)$.

$$\frac{dN}{dt} = k \cdot (S - N(t))$$

### Mathematische Beschreibung

**Kontinuierlich:** $N(t) = S - (S - N_0) \cdot e^{-kt}$

**Vereinfacht (für $N_0 = 0$):** $N(t) = S \cdot (1 - e^{-kt})$

### Eigenschaften

- Für $t \to \infty$: $N(t) \to S$ (Sättigung)
- Anfangs schnelles, später langsames Wachstum
- Typisch: Lernkurven, Erwärmungsprozesse, Marktdurchdringung

### Beispiel: Aufwärmen einer Tasse Kaffee

Ein Raum hat 20°C, der Kaffee startet bei 90°C und nähert sich der Raumtemperatur:

$$T(t) = 20 + 70 \cdot e^{-kt}$$

(Hier: begrenzte Abkühlung zur Grenze 20°C)

## Logistisches Wachstum

### Charakterisierung

Das **logistische Wachstum** kombiniert exponentielles Wachstum mit Sättigungseffekten. Die Wachstumsrate nimmt ab, je näher die Population der Kapazitätsgrenze kommt.

$$\frac{dN}{dt} = r \cdot N \cdot \left(1 - \frac{N}{K}\right)$$

### Mathematische Beschreibung

$$N(t) = \frac{K}{1 + \left(\frac{K - N_0}{N_0}\right) \cdot e^{-rt}}$$

### Eigenschaften

- S-förmiger Verlauf (Sigmoidkurve)
- Anfangs exponentiell, dann Abflachung zur Kapazität $K$
- Wendepunkt bei $N = \frac{K}{2}$ (maximale Wachstumsrate)
- Typisch: Populationsdynamik, Epidemien, Produktlebenszyklen

## Vergleich der Wachstumsmodelle

| Modell | Änderung | Langzeitverhalten | Graph |
|--------|----------|-------------------|-------|
| Linear | $\Delta N = m$ | unbegrenzt | Gerade |
| Exponentiell | $\Delta N = r \cdot N$ | unbegrenzt (oder → 0) | Exponentialkurve |
| Begrenzt | $\Delta N \sim (S - N)$ | → Sättigung $S$ | asymptotisch |
| Logistisch | $\Delta N \sim N(K-N)$ | → Kapazität $K$ | S-Kurve |

## Parameterbestimmung aus Daten

### Exponentielles Wachstum: Zwei Datenpunkte

Gegeben: $(t_1, N_1)$ und $(t_2, N_2)$

$$q = \sqrt[\Delta t]{\frac{N_2}{N_1}} \quad \text{mit } \Delta t = t_2 - t_1$$

$$N_0 = \frac{N_1}{q^{t_1}}$$

### Beispiel

Bevölkerung 2010: 80 Mio., Bevölkerung 2020: 84 Mio.

$$q = \sqrt[10]{\frac{84}{80}} = \sqrt[10]{1,05} \approx 1,00488$$

Jährliche Wachstumsrate: $r \approx 0,49\%$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Arithmetische-Folgen]] – Lineares Wachstum als Spezialfall
- → [[Geometrische-Folgen]] – Exponentielles Wachstum als Spezialfall
- → [[Exponentialfunktionen]] – Kontinuierliche Darstellung
- → [[Logarithmusfunktionen]] – Lösung nach der Zeit
- → [[Rekursive-Folgen]] – Rekursive Wachstumsmodelle

> [!warning] **Prüfungsrelevant**
> - Unterscheidung der Wachstumstypen anhand von Beschreibungen oder Daten
> - Aufstellen und Lösen von Wachstumsgleichungen
> - Berechnung von Verdopplungszeit und Halbwertszeit
> - Parameterbestimmung aus zwei gegebenen Werten
> - Textaufgaben zu Zinseszins, radioaktivem Zerfall, Populationen

> [!question] **Typische Prüfungsfragen**
> - Ein Kapital wächst jährlich um 4%. Nach wie vielen Jahren hat es sich verdoppelt?
> - Die Halbwertszeit eines Isotops beträgt 8 Tage. Welcher Anteil ist nach 20 Tagen noch vorhanden?
> - Eine Population wächst anfangs exponentiell mit 5% pro Jahr. Bei welcher Kapazitätsgrenze erreicht sie den Wendepunkt bei 10.000 Individuen?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Kuttler, C.: Mathematische Modelle in der Biologie. Springer Spektrum, 2015.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2019.

> [!tip] **Weiterführende Links**
> - [[Unendliche-geometrische-Reihen]] – Summen bei Wachstumsprozessen
> - [[Differentialrechnung-I-Index|Differentialrechnung]] – Kontinuierliche Wachstumsanalyse
