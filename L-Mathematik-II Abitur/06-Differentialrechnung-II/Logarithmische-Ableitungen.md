---
author: Andreas Hümmer
title: Logarithmische Ableitungen
tags:
  - content
  - mathe
  - differentialrechnung
  - logarithmus
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Logarithmische Ableitungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Ableitung der natürlichen Logarithmusfunktion kennen und anwenden können
> - Ableitungen von Logarithmusfunktionen mit beliebiger Basis berechnen können
> - Die Technik des logarithmischen Differenzierens beherrschen
> - Verkettete Logarithmusfunktionen ableiten können

---

## Überblick

Die **Logarithmusfunktion** ist die Umkehrfunktion der Exponentialfunktion. Ihre Ableitung $\frac{1}{x}$ ist bemerkenswert einfach und führt zu wichtigen Anwendungen in der Analysis. Darüber hinaus ermöglicht das **logarithmische Differenzieren** die elegante Berechnung von Ableitungen bei komplexen Produkten und Potenzen mit variablen Exponenten.

## Ableitung der natürlichen Logarithmusfunktion

> [!note] **Satz: Ableitung von $\ln x$**
> Für $f(x) = \ln x$ mit $x > 0$ gilt:
> $$\frac{d}{dx} \ln x = \frac{1}{x}$$

### Herleitung

Da $\ln x$ die Umkehrfunktion von $e^x$ ist, gilt $e^{\ln x} = x$.

Ableiten beider Seiten nach $x$ (Kettenregel links):
$$e^{\ln x} \cdot (\ln x)' = 1$$
$$x \cdot (\ln x)' = 1$$
$$(\ln x)' = \frac{1}{x}$$

### Ableitung mit Kettenregel

Für $f(x) = \ln(g(x))$ mit $g(x) > 0$ gilt:

$$\frac{d}{dx} \ln(g(x)) = \frac{g'(x)}{g(x)}$$

**Beispiele:**

| Funktion | Ableitung |
|----------|-----------|
| $\ln(2x)$ | $\frac{2}{2x} = \frac{1}{x}$ |
| $\ln(x^2)$ | $\frac{2x}{x^2} = \frac{2}{x}$ |
| $\ln(\sin x)$ | $\frac{\cos x}{\sin x} = \cot x$ |
| $\ln(e^x + 1)$ | $\frac{e^x}{e^x + 1}$ |

### Ableitung des Betrags

Für $f(x) = \ln|x|$ mit $x \neq 0$ gilt:

$$\frac{d}{dx} \ln|x| = \frac{1}{x}$$

Diese Formel gilt sowohl für $x > 0$ als auch für $x < 0$.

## Logarithmus mit beliebiger Basis

Für $f(x) = \log_a x$ mit $a > 0$, $a \neq 1$ und $x > 0$ gilt:

$$\frac{d}{dx} \log_a x = \frac{1}{x \cdot \ln a}$$

**Herleitung:** Mit der Basisumrechnung $\log_a x = \frac{\ln x}{\ln a}$:
$$\frac{d}{dx} \log_a x = \frac{1}{\ln a} \cdot \frac{d}{dx} \ln x = \frac{1}{\ln a} \cdot \frac{1}{x} = \frac{1}{x \ln a}$$

**Wichtige Spezialfälle:**

| Basis | $\ln a$ | Ableitung von $\log_a x$ |
|-------|---------|--------------------------|
| $e$ | $1$ | $\frac{1}{x}$ |
| $10$ | $\approx 2{,}303$ | $\frac{1}{x \cdot 2{,}303}$ |
| $2$ | $\approx 0{,}693$ | $\frac{1}{x \cdot 0{,}693}$ |

## Logarithmisches Differenzieren

Das **logarithmische Differenzieren** ist eine Technik zur Ableitung von Funktionen der Form:
- Produkte mit vielen Faktoren
- Quotienten mit vielen Faktoren
- Potenzen mit variablem Exponenten: $f(x) = g(x)^{h(x)}$

### Vorgehensweise

1. Logarithmiere beide Seiten: $\ln y = \ln f(x)$
2. Vereinfache mit Logarithmenregeln
3. Leite implizit ab
4. Löse nach $y'$ auf

### Beispiel 1: Produkt mit vielen Faktoren

Gegeben: $f(x) = x^2 \cdot \sqrt{x+1} \cdot (x-2)^3$

**Schritt 1:** Logarithmieren
$$\ln f = \ln(x^2) + \ln\sqrt{x+1} + \ln(x-2)^3$$
$$\ln f = 2\ln x + \frac{1}{2}\ln(x+1) + 3\ln(x-2)$$

**Schritt 2:** Ableiten (links mit Kettenregel)
$$\frac{f'}{f} = \frac{2}{x} + \frac{1}{2(x+1)} + \frac{3}{x-2}$$

**Schritt 3:** Auflösen
$$f' = f \cdot \left(\frac{2}{x} + \frac{1}{2(x+1)} + \frac{3}{x-2}\right)$$
$$f' = x^2 \sqrt{x+1} (x-2)^3 \cdot \left(\frac{2}{x} + \frac{1}{2(x+1)} + \frac{3}{x-2}\right)$$

### Beispiel 2: Potenz mit variablem Exponenten

Gegeben: $f(x) = x^x$ für $x > 0$

**Schritt 1:** Logarithmieren
$$\ln f = x \cdot \ln x$$

**Schritt 2:** Ableiten (Produktregel rechts)
$$\frac{f'}{f} = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$$

**Schritt 3:** Auflösen
$$f' = x^x \cdot (\ln x + 1)$$

### Beispiel 3: Allgemeine Potenz $g(x)^{h(x)}$

Für $f(x) = g(x)^{h(x)}$ mit $g(x) > 0$:

$$f' = g(x)^{h(x)} \cdot \left(h'(x) \cdot \ln g(x) + h(x) \cdot \frac{g'(x)}{g(x)}\right)$$

## Kombinierte Beispiele

### Beispiel: Kurvendiskussion

Gegeben: $f(x) = x \cdot \ln x$ für $x > 0$

**Ableitungen:**
$$f'(x) = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
$$f''(x) = \frac{1}{x}$$

**Nullstelle von f:**
$$x \cdot \ln x = 0 \implies x = 1$$ (da $x > 0$)

**Extremum:**
$$f'(x) = 0 \implies \ln x = -1 \implies x = e^{-1} = \frac{1}{e}$$
$$f''(1/e) = e > 0 \implies \text{Minimum}$$

Minimum bei $\left(\frac{1}{e} \,\middle|\, -\frac{1}{e}\right)$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Logarithmusfunktionen]] – Grundlegende Eigenschaften
- → [[Exponentialfunktionen]] – Umkehrfunktion
- → [[Exponentielles-Wachstum]] – Anwendung der e-Funktion
- → [[Kettenregel]] – Verkettete Ableitungen
- → [[Produktregel]] – Kombinierte Anwendung

> [!warning] **Prüfungsrelevant**
> - $(\ln x)' = \frac{1}{x}$ – Grundformel
> - $(\ln g(x))' = \frac{g'(x)}{g(x)}$ – mit Kettenregel
> - $(\log_a x)' = \frac{1}{x \ln a}$ – beliebige Basis
> - Logarithmisches Differenzieren für $f(x) = g(x)^{h(x)}$
> - Definitionsbereich beachten: $\ln x$ nur für $x > 0$

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Ableitung von $f(x) = \ln(x^2 + 1)$
> - Leiten Sie $f(x) = x^{\sin x}$ mithilfe logarithmischen Differenzierens ab
> - Führen Sie eine Kurvendiskussion für $f(x) = \frac{\ln x}{x}$ durch
> - Für welche $x$ ist $f'(x) = 0$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Exponentielles-Wachstum]] – Zusammenhang mit e-Funktion
> - [[Vollstaendige-Kurvendiskussion]] – Anwendung auf ln-Funktionen
