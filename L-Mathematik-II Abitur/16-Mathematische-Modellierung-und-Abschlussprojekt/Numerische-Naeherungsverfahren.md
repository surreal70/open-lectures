---
author: Andreas Hümmer
title: Numerische Näherungsverfahren
tags:
  - content
  - mathe
  - modellierung
  - numerik
  - newton
  - integration
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Numerische Näherungsverfahren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Newton-Verfahren zur Nullstellenberechnung anwenden können
> - Numerische Integrationsmethoden kennen und durchführen
> - Die Konvergenz und Genauigkeit von Verfahren einschätzen
> - Grenzen und Fehlerquellen numerischer Methoden verstehen

---

## Überblick

Viele mathematische Probleme haben keine geschlossene analytische Lösung — oder die Lösung ist so kompliziert, dass numerische Näherungen praktischer sind. **Numerische Verfahren** liefern Näherungswerte mit kontrollierbarer Genauigkeit.

Die wichtigsten Anwendungsgebiete sind:
- Nullstellenberechnung bei komplizierten Funktionen
- Integration von Funktionen ohne elementare Stammfunktion
- Lösung von Differentialgleichungen

## Das Newton-Verfahren (Newton-Raphson)

### Grundidee

Das Newton-Verfahren nähert sich iterativ einer Nullstelle von $f(x)$:
1. Starte mit einem Schätzwert $x_0$
2. Lege die Tangente an den Graphen bei $(x_0, f(x_0))$
3. Der Schnittpunkt der Tangente mit der $x$-Achse gibt den nächsten Näherungswert

### Iterationsformel

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Herleitung

Die Tangente an $f$ im Punkt $(x_n, f(x_n))$ hat die Gleichung:
$$y = f(x_n) + f'(x_n)(x - x_n)$$

Nullstelle der Tangente (setze $y = 0$):
$$0 = f(x_n) + f'(x_n)(x_{n+1} - x_n)$$
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Beispiel: $\sqrt{2}$ berechnen

Gesucht ist die positive Nullstelle von $f(x) = x^2 - 2$.

$f'(x) = 2x$

**Iteration**: $x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{x_n}{2} + \frac{1}{x_n}$

| $n$ | $x_n$ | $f(x_n) = x_n^2 - 2$ |
|-----|-------|----------------------|
| 0 | 1,0000 | -1,0000 |
| 1 | 1,5000 | 0,2500 |
| 2 | 1,4167 | 0,0069 |
| 3 | 1,4142 | 0,00002 |
| 4 | 1,41421356 | $< 10^{-8}$ |

Nach nur 4 Iterationen ist die Genauigkeit besser als $10^{-8}$!

### Konvergenz

Das Newton-Verfahren konvergiert **quadratisch** (die Anzahl korrekter Stellen verdoppelt sich pro Schritt), wenn:
- Der Startwert $x_0$ nahe genug an der Nullstelle liegt
- $f'(x^*) \neq 0$ an der Nullstelle $x^*$

### Probleme und Grenzen

**Divergenz**: Bei ungünstigem Startwert oder $f'(x_n) \approx 0$ kann das Verfahren:
- Oszillieren
- Divergieren
- Zu einer anderen Nullstelle konvergieren

**Beispiel für Divergenz**: $f(x) = x^3 - 2x + 2$ mit $x_0 = 0$ führt zu Oszillation zwischen $0$ und $1$.

> [!warning] **Praktischer Hinweis**
> Immer zuerst den Graphen skizzieren und einen sinnvollen Startwert wählen!

## Numerische Integration

### Warum numerisch integrieren?

Viele wichtige Integrale haben keine elementare Stammfunktion:
$$\int e^{-x^2}\,dx, \quad \int \frac{\sin x}{x}\,dx, \quad \int \sqrt{1 + x^4}\,dx$$

Numerische Verfahren liefern Näherungen für $\int_a^b f(x)\,dx$.

### Rechteckregel (Mittelpunktregel)

Die Fläche wird durch Rechtecke angenähert:

$$\int_a^b f(x)\,dx \approx \sum_{i=1}^{n} f(m_i) \cdot \Delta x$$

wobei $\Delta x = \frac{b-a}{n}$ und $m_i$ der Mittelpunkt des $i$-ten Teilintervalls ist.

### Trapezregel

Die Fläche wird durch Trapeze angenähert:

$$\int_a^b f(x)\,dx \approx \frac{\Delta x}{2}\left[f(a) + 2\sum_{i=1}^{n-1}f(x_i) + f(b)\right]$$

oder kompakt:

$$\int_a^b f(x)\,dx \approx \Delta x \left[\frac{f(a) + f(b)}{2} + \sum_{i=1}^{n-1}f(x_i)\right]$$

### Simpson-Regel

Die Funktion wird stückweise durch Parabeln angenähert (benötigt gerade Anzahl $n$ von Teilintervallen):

$$\int_a^b f(x)\,dx \approx \frac{\Delta x}{3}\left[f(a) + 4\sum_{\text{ungerade }i}f(x_i) + 2\sum_{\text{gerade }i}f(x_i) + f(b)\right]$$

### Vergleich der Verfahren

| Verfahren | Fehlerordnung | Genauigkeit |
|-----------|---------------|-------------|
| Rechteck | $O(\Delta x^2)$ | niedrig |
| Trapez | $O(\Delta x^2)$ | mittel |
| Simpson | $O(\Delta x^4)$ | hoch |

### Beispiel: $\int_0^1 e^{-x^2}\,dx$

Mit $n = 4$ Teilintervallen ($\Delta x = 0{,}25$):

**Trapezregel**:

| $x$ | $f(x) = e^{-x^2}$ | Gewicht |
|-----|-------------------|---------|
| 0 | 1,0000 | 0,5 |
| 0,25 | 0,9394 | 1 |
| 0,5 | 0,7788 | 1 |
| 0,75 | 0,5698 | 1 |
| 1,0 | 0,3679 | 0,5 |

$$I \approx 0{,}25 \cdot (0{,}5 + 0{,}9394 + 0{,}7788 + 0{,}5698 + 0{,}1840) = 0{,}7430$$

(Exakter Wert: $\approx 0{,}7468$, Fehler: $\approx 0{,}5\%$)

## Fixpunktiteration

### Prinzip

Umschreiben einer Gleichung $f(x) = 0$ in die Form $x = g(x)$.

**Iteration**: $x_{n+1} = g(x_n)$

### Konvergenzbedingung

Die Iteration konvergiert, wenn $|g'(x)| < 1$ in der Nähe des Fixpunkts.

### Beispiel

Löse $x = \cos(x)$.

**Iteration**: $x_{n+1} = \cos(x_n)$

| $n$ | $x_n$ |
|-----|-------|
| 0 | 0,5 |
| 1 | 0,8776 |
| 2 | 0,6390 |
| 3 | 0,8027 |
| ... | ... |
| 50 | 0,7391 |

Der Fixpunkt ist $x^* \approx 0{,}739085$.

## Bisektionsverfahren (Intervallhalbierung)

### Prinzip

Wenn $f(a) \cdot f(b) < 0$, liegt eine Nullstelle zwischen $a$ und $b$ (Zwischenwertsatz).

**Algorithmus**:
1. Berechne $m = \frac{a+b}{2}$
2. Falls $f(a) \cdot f(m) < 0$: Nullstelle in $[a, m]$, setze $b = m$
3. Sonst: Nullstelle in $[m, b]$, setze $a = m$
4. Wiederhole bis gewünschte Genauigkeit erreicht

### Eigenschaften

- **Immer konvergent** (wenn Nullstelle im Startintervall)
- **Lineare Konvergenz**: Ein korrektes Bit pro Schritt
- Langsamer als Newton, aber robuster

### Beispiel

Nullstelle von $f(x) = x^3 - x - 1$ in $[1, 2]$.

| Schritt | $a$ | $b$ | $m$ | $f(m)$ |
|---------|-----|-----|-----|--------|
| 1 | 1,0 | 2,0 | 1,5 | 0,875 |
| 2 | 1,0 | 1,5 | 1,25 | -0,297 |
| 3 | 1,25 | 1,5 | 1,375 | 0,224 |
| 4 | 1,25 | 1,375 | 1,3125 | -0,051 |

Nach 10 Schritten: $x^* \approx 1{,}3247$ mit Fehler $< 10^{-3}$.

## Fehlerabschätzung

### Absoluter und relativer Fehler

**Absoluter Fehler**: $|x_{\text{approx}} - x_{\text{exakt}}|$

**Relativer Fehler**: $\frac{|x_{\text{approx}} - x_{\text{exakt}}|}{|x_{\text{exakt}}|}$

### Abbruchkriterien

Ein iteratives Verfahren wird beendet, wenn:
- $|x_{n+1} - x_n| < \varepsilon$ (Schrittweite klein genug)
- $|f(x_n)| < \varepsilon$ (Funktionswert nahe Null)
- Maximale Iterationszahl erreicht

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Nullstellen]] — Analytische Methoden
- → [[Bestimmte-Integrale]] — Grundlagen der Integration
- → [[Stammfunktionen]] — Elementare Integration
- → [[Mathematische-Simulationen]] — Anwendung in Simulationen
- → [[Numerische-Integration-Grundlagen]] — Einführung in der Integralrechnung

> [!warning] **Prüfungsrelevant**
> - Newton-Verfahren: Formel anwenden, erste Iterationen durchrechnen
> - Trapezregel: Integral numerisch berechnen
> - Konvergenzverhalten erklären
> - Fehler bei numerischen Verfahren einschätzen
> - Geeigneten Startwert wählen und begründen

> [!question] **Typische Prüfungsfragen**
> - Führen Sie zwei Schritte des Newton-Verfahrens zur Bestimmung von $\sqrt{5}$ durch.
> - Berechnen Sie $\int_0^2 f(x)\,dx$ mit der Trapezregel und $n = 4$.
> - Warum kann das Newton-Verfahren bei diesem Startwert divergieren?
> - Wie viele Iterationen sind nötig, um die Genauigkeit $10^{-6}$ zu erreichen?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2. Springer Vieweg, 2015
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Mathematische-Simulationen]] — Anwendung in der Praxis
> - [[Funktionendarstellung-mit-Python]] — Numerische Verfahren programmieren
> - [[Vorbereitung-auf-Hochschulmathematik]] — Numerische Analysis an der Hochschule
