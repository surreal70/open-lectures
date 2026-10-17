---
author: Andreas Hümmer
title: Wachstumsmodelle
tags:
  - content
  - mathe
  - modellierung
  - wachstum
  - exponentialfunktion
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Wachstumsmodelle

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Wachstumstypen unterscheiden und anwenden können
> - Wachstumsmodelle aus Daten oder Beschreibungen aufstellen
> - Die Halbwertszeit und Verdopplungszeit berechnen
> - Logistisches Wachstum als realistischere Alternative kennen

---

## Überblick

Wachstumsmodelle beschreiben, wie sich Größen im Laufe der Zeit verändern. Sie sind fundamental für das Verständnis von Naturvorgängen (Populationsdynamik, radioaktiver Zerfall), wirtschaftlichen Prozessen (Zinsen, Inflation) und technischen Anwendungen (Signalverarbeitung, Regelungstechnik).

Die Wahl des richtigen Modells hängt von der Situation ab: Unbeschränktes exponentielles Wachstum ist theoretisch, beschränktes und logistisches Wachstum bilden die Realität besser ab.

## Lineares Wachstum

### Definition

Beim linearen Wachstum ist die **absolute Änderung** pro Zeiteinheit konstant:

$$f(t) = f_0 + k \cdot t$$

wobei:
- $f_0$: Anfangswert
- $k$: Wachstumsrate (konstante Steigung)
- $t$: Zeit

### Differentialgleichung

$$\frac{df}{dt} = k = \text{const}$$

### Beispiele

- **Sparbuch mit einfachen Zinsen**: $K(t) = K_0 + K_0 \cdot p \cdot t$
- **Gleichförmige Bewegung**: $s(t) = s_0 + v \cdot t$
- **Lineare Abschreibung**: $W(t) = W_0 - a \cdot t$

**Konkretes Beispiel**: Ein Wasserbecken füllt sich mit konstanter Zuflussrate von $50\,\text{L/min}$. Nach $t$ Minuten enthält es:
$$V(t) = V_0 + 50t$$

## Exponentielles Wachstum

### Definition

Beim exponentiellen Wachstum ist die **relative Änderung** pro Zeiteinheit konstant:

$$f(t) = f_0 \cdot e^{kt}$$

oder in der Basis-Form:

$$f(t) = f_0 \cdot a^t \quad \text{mit } a = e^k$$

### Differentialgleichung

$$\frac{df}{dt} = k \cdot f(t)$$

Das bedeutet: Je größer der Bestand, desto schneller das Wachstum.

### Charakteristische Größen

**Verdopplungszeit** $T_2$ (bei $k > 0$):

$$f(T_2) = 2f_0 \quad \Rightarrow \quad T_2 = \frac{\ln 2}{k} \approx \frac{0{,}693}{k}$$

**Halbwertszeit** $T_{1/2}$ (bei $k < 0$):

$$f(T_{1/2}) = \frac{1}{2}f_0 \quad \Rightarrow \quad T_{1/2} = \frac{\ln 2}{|k|}$$

### Beispiele

**Bakterienwachstum**: Eine Bakterienkultur verdoppelt sich alle $20$ Minuten.

$$N(t) = N_0 \cdot 2^{t/20} = N_0 \cdot e^{(\ln 2/20) \cdot t}$$

Mit $k = \frac{\ln 2}{20} \approx 0{,}0347\,\text{min}^{-1}$.

**Radioaktiver Zerfall**: Kohlenstoff-14 hat eine Halbwertszeit von $5730$ Jahren.

$$N(t) = N_0 \cdot e^{-\lambda t} \quad \text{mit } \lambda = \frac{\ln 2}{5730} \approx 1{,}21 \cdot 10^{-4}\,\text{a}^{-1}$$

**Zinseszins**: Kapital $K_0$ wird mit Zinssatz $p\%$ angelegt:

$$K(n) = K_0 \cdot \left(1 + \frac{p}{100}\right)^n$$

Bei kontinuierlicher Verzinsung:

$$K(t) = K_0 \cdot e^{(p/100) \cdot t}$$

## Beschränktes Wachstum

### Definition

Beim beschränkten Wachstum nähert sich $f(t)$ einem Grenzwert $S$ (Sättigungsgrenze):

$$f(t) = S - (S - f_0) \cdot e^{-kt}$$

oder äquivalent:

$$f(t) = S \cdot (1 - e^{-kt}) + f_0 \cdot e^{-kt}$$

### Differentialgleichung

$$\frac{df}{dt} = k \cdot (S - f(t))$$

Die Wachstumsrate ist proportional zum **Sättigungsdefizit** $(S - f)$.

### Beispiele

**Aufheizen eines Körpers**: Ein kalter Körper ($20°C$) wird in einen Ofen ($200°C$) gelegt:

$$T(t) = 200 - 180 \cdot e^{-kt}$$

**Lernkurve**: Die Anzahl gelernter Vokabeln nähert sich einer Maximalzahl:

$$V(t) = V_{\max} \cdot (1 - e^{-kt})$$

**Medikamentenkonzentration**: Bei konstanter Infusion:

$$c(t) = c_{\max} \cdot (1 - e^{-kt})$$

## Logistisches Wachstum

### Definition

Das logistische Wachstum kombiniert exponentielles Wachstum bei kleinen Beständen mit Sättigung bei großen Beständen:

$$f(t) = \frac{S}{1 + \left(\frac{S}{f_0} - 1\right) \cdot e^{-kSt}}$$

oder in vereinfachter Form:

$$f(t) = \frac{S}{1 + c \cdot e^{-rt}}$$

### Differentialgleichung

$$\frac{df}{dt} = k \cdot f(t) \cdot (S - f(t))$$

Die Wachstumsrate hängt sowohl vom aktuellen Bestand als auch vom verbleibenden Wachstumspotential ab.

### Eigenschaften

- **Wendepunkt** bei $f = \frac{S}{2}$: Hier ist das Wachstum maximal
- **S-förmiger Verlauf** (Sigmoidkurve)
- **Anfangs**: annähernd exponentielles Wachstum
- **Später**: Annäherung an die Kapazitätsgrenze $S$

### Beispiele

**Ausbreitung einer Nachricht**: In einer Gruppe von $1000$ Personen kennt anfangs $1$ Person eine Neuigkeit. Mit $k = 0{,}001$ pro Tag:

$$N(t) = \frac{1000}{1 + 999 \cdot e^{-t}}$$

**Populationsdynamik**: Eine Tierpopulation in einem begrenzten Lebensraum mit Kapazität $K$:

$$P(t) = \frac{K}{1 + \left(\frac{K}{P_0} - 1\right) \cdot e^{-rt}}$$

## Vergleich der Wachstumstypen

| Modell | Differentialgleichung | Lösung | Grenzwert |
|--------|----------------------|--------|-----------|
| Linear | $f' = k$ | $f_0 + kt$ | $\pm\infty$ |
| Exponentiell | $f' = kf$ | $f_0 \cdot e^{kt}$ | $\pm\infty$ oder $0$ |
| Beschränkt | $f' = k(S-f)$ | $S - (S-f_0)e^{-kt}$ | $S$ |
| Logistisch | $f' = kf(S-f)$ | $\frac{S}{1+ce^{-rt}}$ | $S$ |

## Modellwahl und Parameterbestimmung

### Wann welches Modell?

**Lineares Wachstum**: Konstante Zufuhr/Abnahme, keine Rückkopplung
- Gleichförmige Bewegung, konstante Abschreibung

**Exponentielles Wachstum**: Prozentuale Änderung, unbegrenzte Ressourcen
- Zinsen, radioaktiver Zerfall, frühe Epidemiephase

**Beschränktes Wachstum**: Annäherung an einen Gleichgewichtswert
- Temperaturausgleich, Medikamentenkonzentration

**Logistisches Wachstum**: Anfangs exponentiell, dann Sättigung
- Populationen, Technologieadoption, Epidemieausbreitung

### Parameterbestimmung aus Daten

**Aus zwei Messpunkten** $(t_1, f_1)$ und $(t_2, f_2)$:

Für exponentielles Wachstum $f(t) = f_0 \cdot e^{kt}$:

$$k = \frac{\ln(f_2) - \ln(f_1)}{t_2 - t_1} = \frac{1}{t_2 - t_1} \ln\left(\frac{f_2}{f_1}\right)$$

$$f_0 = f_1 \cdot e^{-kt_1}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentialfunktionen]] — Mathematische Grundlagen
- → [[Logarithmusfunktionen]] — Umkehrung und Linearisierung
- → [[Exponentielles-Wachstum]] — Vertiefung in der Differentialrechnung
- → [[Mathematische-Modellbildung]] — Der Modellierungsprozess
- → [[Einfache-Wachstumsmodelle]] — Grundlagen der Integralrechnung

> [!warning] **Prüfungsrelevant**
> - Unterscheidung der Wachstumstypen anhand von Beschreibungen
> - Aufstellen der Wachstumsfunktion aus Textaufgaben
> - Berechnung von Verdopplungszeit und Halbwertszeit
> - Interpretation der Parameter im Sachkontext
> - Langzeitverhalten und Grenzwerte bestimmen

> [!question] **Typische Prüfungsfragen**
> - Ein Bestand verdoppelt sich alle $x$ Jahre. Geben Sie die Wachstumsfunktion an.
> - Nach welcher Zeit ist nur noch $10\%$ des radioaktiven Stoffes vorhanden?
> - Bestimmen Sie die Kapazitätsgrenze und den Wendepunkt des logistischen Wachstums.
> - Begründen Sie, warum exponentielles Wachstum langfristig nicht realistisch ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2. Springer Vieweg, 2015
- Tietze, U.-P. et al.: Mathematikunterricht in der Sekundarstufe II. Vieweg, 2000
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Bewegungsmodelle]] — Wachstum in der Kinematik
> - [[Numerische-Naeherungsverfahren]] — Numerische Lösung von Wachstumsgleichungen
> - [[Mathematische-Simulationen]] — Wachstumsmodelle simulieren
