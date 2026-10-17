---
author: Andreas Hümmer
title: Logarithmusfunktionen
tags:
  - content
  - mathe
  - funktionen
  - logarithmus
  - umkehrfunktion
created: 2025-06-19
modified: 2025-06-19
---

# Logarithmusfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Logarithmus als Umkehroperation des Potenzierens verstehen
> - Die verschiedenen Logarithmenbasen (natürlich, dekadisch) unterscheiden können
> - Die Logarithmengesetze sicher anwenden können
> - Logarithmische Gleichungen und Funktionen analysieren können

---

## Überblick

Der Logarithmus beantwortet die Frage: „Mit welchem Exponenten muss ich die Basis potenzieren, um einen bestimmten Wert zu erhalten?" Die Logarithmusfunktion ist die Umkehrfunktion der Exponentialfunktion und spielt eine zentrale Rolle bei der Lösung von Exponentialgleichungen. Sie findet Anwendung in der Akustik (Dezibel), der Chemie (pH-Wert) und der Informatik (Komplexitätsanalyse).

## Definition des Logarithmus

### Grunddefinition

Für $a > 0$, $a \neq 1$ und $x > 0$ ist der **Logarithmus zur Basis $a$**:

$$y = \log_a(x) \quad \Leftrightarrow \quad a^y = x$$

Der Logarithmus ist der Exponent, mit dem man die Basis potenzieren muss, um das Argument zu erhalten.

### Beispiele

- $\log_2(8) = 3$, denn $2^3 = 8$
- $\log_{10}(1000) = 3$, denn $10^3 = 1000$
- $\log_5(1) = 0$, denn $5^0 = 1$
- $\log_3\left(\frac{1}{9}\right) = -2$, denn $3^{-2} = \frac{1}{9}$

## Spezielle Logarithmen

### Natürlicher Logarithmus

$$\ln(x) = \log_e(x)$$

Der natürliche Logarithmus hat die Eulersche Zahl $e \approx 2{,}718$ als Basis. Er ist in der Analysis der wichtigste Logarithmus.

### Dekadischer (Zehner-)Logarithmus

$$\lg(x) = \log_{10}(x)$$

Der dekadische Logarithmus wird in Technik und Naturwissenschaften häufig verwendet.

### Binärer Logarithmus

$$\text{lb}(x) = \log_2(x)$$

Der binäre Logarithmus ist in der Informatik von besonderer Bedeutung (Bits, Komplexitätsanalyse).

## Die Logarithmusfunktion

### Eigenschaften von $f(x) = \log_a(x)$

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $D_f = (0, +\infty)$ |
| Wertebereich | $W_f = \mathbb{R}$ |
| Nullstelle | $x = 1$ (denn $\log_a(1) = 0$) |
| Asymptote | $x = 0$ (vertikale Asymptote) |
| Monotonie | streng monoton steigend für $a > 1$ |
| | streng monoton fallend für $0 < a < 1$ |

### Graph von $f(x) = \ln(x)$

```
     y
     │
   1 ┼       ╱
     │     ╱
     │   ╱
─────┼──•─────────── x
     │╱  1
  -1 ┼
     │
```

Der Graph schneidet die x-Achse bei $x = 1$ und nähert sich für $x \to 0^+$ der vertikalen Asymptote.

### Charakteristische Werte

| $x$ | $\ln(x)$ |
|-----|----------|
| $e^{-1} \approx 0{,}368$ | $-1$ |
| $1$ | $0$ |
| $e \approx 2{,}718$ | $1$ |
| $e^2 \approx 7{,}389$ | $2$ |

## Logarithmengesetze

### Fundamentale Regeln

Für $a > 0$, $a \neq 1$ und $x, y > 0$:

| Regel | Formel |
|-------|--------|
| Produktregel | $\log_a(x \cdot y) = \log_a(x) + \log_a(y)$ |
| Quotientenregel | $\log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)$ |
| Potenzregel | $\log_a(x^n) = n \cdot \log_a(x)$ |
| Wurzelregel | $\log_a\left(\sqrt[n]{x}\right) = \frac{1}{n} \cdot \log_a(x)$ |
| Basiswert | $\log_a(a) = 1$ |
| Eins-Regel | $\log_a(1) = 0$ |

### Basiswechsel

$$\log_a(x) = \frac{\log_b(x)}{\log_b(a)} = \frac{\ln(x)}{\ln(a)}$$

**Beispiel:** $\log_2(5) = \frac{\ln 5}{\ln 2} \approx \frac{1{,}609}{0{,}693} \approx 2{,}322$

### Umkehrbeziehungen

$$a^{\log_a(x)} = x \quad \text{für } x > 0$$
$$\log_a(a^x) = x \quad \text{für } x \in \mathbb{R}$$

Insbesondere:
$$e^{\ln x} = x \quad \text{und} \quad \ln(e^x) = x$$

## Logarithmische Gleichungen

### Typ 1: Logarithmus isolieren

**Beispiel:** $\ln(x) = 3$

$$x = e^3 \approx 20{,}09$$

### Typ 2: Gleichung auf gleiche Basis bringen

**Beispiel:** $\log_2(x+1) = \log_2(5)$

Da der Logarithmus injektiv ist: $x + 1 = 5 \Rightarrow x = 4$

### Typ 3: Logarithmengesetze anwenden

**Beispiel:** $\ln(x) + \ln(x-2) = \ln(15)$

$$\ln(x(x-2)) = \ln(15)$$
$$x^2 - 2x = 15$$
$$x^2 - 2x - 15 = 0$$
$$(x-5)(x+3) = 0$$

Lösungskandidaten: $x_1 = 5$, $x_2 = -3$

**Definitionsbereich beachten:** $x > 0$ und $x - 2 > 0$, also $x > 2$

**Lösung:** $x = 5$ (da $x = -3$ nicht im Definitionsbereich)

### Typ 4: Exponentialgleichungen lösen

**Beispiel:** $3^x = 20$

Logarithmieren: $x \cdot \ln(3) = \ln(20)$

$$x = \frac{\ln(20)}{\ln(3)} \approx \frac{3{,}00}{1{,}10} \approx 2{,}73$$

## Transformationen

### Allgemeine Form

$$f(x) = a \cdot \log_b(c(x - d)) + e$$

| Parameter | Wirkung |
|-----------|---------|
| $a$ | Streckung/Stauchung in y-Richtung |
| $b$ | Basis des Logarithmus |
| $c$ | Streckung/Stauchung in x-Richtung |
| $d$ | Verschiebung in x-Richtung (Asymptote: $x = d$) |
| $e$ | Verschiebung in y-Richtung |

### Beispiel

$f(x) = 2\ln(x-1) + 3$

- Verschiebung um 1 nach rechts
- Streckung mit Faktor 2 in y-Richtung
- Verschiebung um 3 nach oben
- Definitionsbereich: $D_f = (1, +\infty)$
- Asymptote: $x = 1$
- Nullstelle: $2\ln(x-1) + 3 = 0 \Rightarrow \ln(x-1) = -\frac{3}{2} \Rightarrow x = 1 + e^{-1{,}5} \approx 1{,}22$

## Anwendungen

### pH-Wert in der Chemie

$$\text{pH} = -\lg(c_{H^+})$$

wobei $c_{H^+}$ die Wasserstoffionenkonzentration in mol/l ist.

**Beispiel:** $c_{H^+} = 10^{-4}$ mol/l → pH = 4

### Dezibel in der Akustik

$$L = 10 \cdot \lg\left(\frac{I}{I_0}\right) \text{ dB}$$

wobei $I_0 = 10^{-12}$ W/m² die Hörschwelle ist.

### Informationsgehalt

$$H = -\sum p_i \cdot \log_2(p_i)$$

Die Shannon-Entropie misst den Informationsgehalt in Bits.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentialfunktionen]] — Umkehrfunktion
- → [[Umkehrfunktionen]] — Allgemeine Theorie
- → [[Potenzfunktionen]] — Potenzregel des Logarithmus
- → [[Grenzwerte-von-Funktionen]] — Verhalten für $x \to 0^+$ und $x \to \infty$
- → [[05-Differentialrechnung-I|Differentialrechnung]] — $\frac{d}{dx}\ln x = \frac{1}{x}$
- → [[07-Integralrechnung-I|Integralrechnung]] — $\int \frac{1}{x} dx = \ln|x| + C$

> [!warning] **Prüfungsrelevant**
> - Definition: $\log_a(x) = y \Leftrightarrow a^y = x$
> - Sichere Beherrschung der Logarithmengesetze
> - Basiswechselformel für Taschenrechnerberechnungen
> - Definitionsbereich: Argument muss positiv sein!
> - Logarithmieren zur Lösung von Exponentialgleichungen
> - Graph: vertikale Asymptote bei $x = 0$, Nullstelle bei $x = 1$

> [!question] **Typische Prüfungsfragen**
> - Lösen Sie die Gleichung $\log_3(x) + \log_3(x-6) = 3$.
> - Vereinfachen Sie $\ln(e^2 \cdot \sqrt{e})$ ohne Verwendung eines Taschenrechners.
> - Bestimmen Sie Definitions- und Wertebereich sowie die Nullstelle von $f(x) = \ln(2x-4) - 1$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Abiturprüfungsaufgaben Mathematik*, verschiedene Jahrgänge

> [!tip] **Weiterführende Links**
> - [[Exponentialfunktionen]] — Die Umkehrfunktion
> - [[07-Integralrechnung-I|Integralrechnung]] — Stammfunktion $\ln|x|$

