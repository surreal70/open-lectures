---
author: Andreas Hümmer
title: Exponentielles Wachstum und die e-Funktion
tags:
  - content
  - mathe
  - differentialrechnung
  - exponentialfunktion
  - wachstum
created: 2025-06-20
modified: 2025-06-20
---

# Exponentielles Wachstum und die e-Funktion

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Ableitung der e-Funktion und allgemeiner Exponentialfunktionen beherrschen
> - Den Zusammenhang zwischen Wachstumsrate und Ableitung verstehen
> - Exponentielles Wachstum und Zerfall modellieren können
> - Die Bedeutung der Euler'schen Zahl e für Analysis und Anwendungen verstehen

---

## Überblick

Die **Exponentialfunktion** $f(x) = e^x$ nimmt in der Analysis eine Sonderstellung ein: Sie ist die einzige Funktion (bis auf Vielfache), die mit ihrer Ableitung identisch ist. Diese Eigenschaft macht sie zum idealen Werkzeug für die Beschreibung von Wachstums- und Zerfallsprozessen, bei denen die Änderungsrate proportional zum aktuellen Bestand ist.

## Die Euler'sche Zahl e

Die **Euler'sche Zahl** ist definiert als:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2{,}71828$$

Alternative Definition über die Reihe:

$$e = \sum_{k=0}^{\infty} \frac{1}{k!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \ldots$$

## Ableitung der e-Funktion

> [!note] **Satz: Ableitung von $e^x$**
> Die natürliche Exponentialfunktion $f(x) = e^x$ hat die besondere Eigenschaft:
> $$\frac{d}{dx} e^x = e^x$$

Die e-Funktion ist ihre eigene Ableitung. Dies gilt für alle höheren Ableitungen:

$$f(x) = e^x \implies f'(x) = f''(x) = f'''(x) = \ldots = e^x$$

### Ableitung mit Kettenregel

Für $f(x) = e^{g(x)}$ gilt nach der Kettenregel:

$$\frac{d}{dx} e^{g(x)} = e^{g(x)} \cdot g'(x)$$

**Beispiele:**

| Funktion | Ableitung |
|----------|-----------|
| $e^{2x}$ | $2e^{2x}$ |
| $e^{-x}$ | $-e^{-x}$ |
| $e^{x^2}$ | $2x \cdot e^{x^2}$ |
| $e^{\sin x}$ | $\cos x \cdot e^{\sin x}$ |

### Allgemeine Exponentialfunktion

Für $f(x) = a^x$ mit $a > 0$, $a \neq 1$ gilt:

$$\frac{d}{dx} a^x = a^x \cdot \ln a$$

**Herleitung:** $a^x = e^{x \ln a}$, also mit Kettenregel:
$$\frac{d}{dx} a^x = e^{x \ln a} \cdot \ln a = a^x \cdot \ln a$$

## Exponentielles Wachstum

### Das Grundmodell

Viele natürliche Prozesse folgen dem Gesetz:

> Die momentane Änderungsrate ist proportional zum aktuellen Bestand.

Mathematisch: $f'(t) = k \cdot f(t)$ mit $k \in \mathbb{R}$

**Lösung dieser Differentialgleichung:**

$$f(t) = f(0) \cdot e^{kt}$$

wobei $f(0)$ der Anfangswert zur Zeit $t = 0$ ist.

### Interpretation des Parameters k

- $k > 0$: **Exponentielles Wachstum** (Verdopplung, Vermehrung)
- $k < 0$: **Exponentieller Zerfall** (Halbierung, Abnahme)
- $|k|$ groß: schnelles Wachstum/Zerfall
- $|k|$ klein: langsames Wachstum/Zerfall

### Verdopplungs- und Halbwertszeit

**Verdopplungszeit** (für $k > 0$):
$$T_2: \quad f(t + T_2) = 2 \cdot f(t)$$
$$e^{k \cdot T_2} = 2 \implies T_2 = \frac{\ln 2}{k}$$

**Halbwertszeit** (für $k < 0$):
$$T_{1/2}: \quad f(t + T_{1/2}) = \frac{1}{2} \cdot f(t)$$
$$e^{k \cdot T_{1/2}} = \frac{1}{2} \implies T_{1/2} = \frac{\ln 2}{|k|}$$

## Anwendungsbeispiele

### Beispiel 1: Bakterienwachstum

Eine Bakterienkultur verdoppelt sich alle 20 Minuten. Anfangs sind 1000 Bakterien vorhanden.

**Modell:** $N(t) = N_0 \cdot e^{kt}$ mit $N_0 = 1000$

**Bestimmung von k:**
$$T_2 = 20 \text{ min} \implies k = \frac{\ln 2}{20} \approx 0{,}0347 \text{ min}^{-1}$$

**Funktion:**
$$N(t) = 1000 \cdot e^{0{,}0347t}$$

**Nach 1 Stunde:**
$$N(60) = 1000 \cdot e^{0{,}0347 \cdot 60} = 1000 \cdot e^{2{,}08} \approx 8000$$

### Beispiel 2: Radioaktiver Zerfall

Kohlenstoff-14 hat eine Halbwertszeit von etwa 5730 Jahren.

**Modell:** $N(t) = N_0 \cdot e^{kt}$

**Bestimmung von k:**
$$k = -\frac{\ln 2}{5730} \approx -1{,}21 \cdot 10^{-4} \text{ a}^{-1}$$

**Altersbestimmung:** Wenn noch 70% des ursprünglichen C-14 vorhanden sind:

$$0{,}7 = e^{kt} \implies t = \frac{\ln 0{,}7}{k} \approx 2950 \text{ Jahre}$$

### Beispiel 3: Abkühlung (Newton'sches Abkühlungsgesetz)

Die Temperatur eines Körpers nähert sich exponentiell der Umgebungstemperatur:

$$T(t) = T_U + (T_0 - T_U) \cdot e^{-kt}$$

wobei $T_U$ die Umgebungstemperatur und $T_0$ die Anfangstemperatur ist.

## Kurvendiskussion der e-Funktion

Für $f(x) = e^x$:

| Eigenschaft | Ergebnis |
|-------------|----------|
| Definitionsbereich | $\mathbb{R}$ |
| Wertebereich | $(0, \infty)$ |
| Nullstellen | keine |
| y-Achsenabschnitt | $(0|1)$ |
| Monotonie | streng monoton steigend |
| Krümmung | linksgekrümmt (konvex) |
| Asymptote | $y = 0$ (für $x \to -\infty$) |
| Grenzwerte | $\lim_{x \to -\infty} e^x = 0$, $\lim_{x \to \infty} e^x = \infty$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentialfunktionen]] – Grundlegende Eigenschaften
- → [[Logarithmusfunktionen]] – Umkehrfunktion
- → [[Kettenregel]] – Ableitung zusammengesetzter e-Funktionen
- → [[Logarithmische-Ableitungen]] – Verwandte Ableitungstechniken
- → [[Anwendungen-in-Physik-und-Technik]] – Praktische Anwendungen

> [!warning] **Prüfungsrelevant**
> - $(e^x)' = e^x$ – die fundamentale Ableitungsregel
> - $(e^{g(x)})' = e^{g(x)} \cdot g'(x)$ – Kettenregel
> - $(a^x)' = a^x \cdot \ln a$ – allgemeine Exponentialfunktion
> - Verdopplungszeit: $T_2 = \frac{\ln 2}{k}$
> - Halbwertszeit: $T_{1/2} = \frac{\ln 2}{|k|}$

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Ableitung von $f(x) = x^2 \cdot e^{-x}$
> - Ermitteln Sie die Wachstumskonstante k aus gegebenen Daten
> - Nach welcher Zeit ist der Bestand auf 10% gesunken?
> - Führen Sie eine Kurvendiskussion für $f(x) = x \cdot e^{-x}$ durch

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Logarithmische-Ableitungen]] – Ableitung von Logarithmusfunktionen
> - [[Anwendungen-in-Physik-und-Technik]] – Weitere Anwendungsbeispiele
