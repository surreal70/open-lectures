---
author: Andreas Hümmer
title: Optimierungsprobleme
tags:
  - content
  - mathe
  - modellierung
  - optimierung
  - extremwert
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Optimierungsprobleme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Reale Optimierungsprobleme systematisch lösen können
> - Nebenbedingungen in die Zielfunktion einsetzen
> - Lokale und globale Extrema unterscheiden
> - Die Lösung im Sachzusammenhang interpretieren

---

## Überblick

Optimierungsprobleme sind Extremwertaufgaben mit praktischem Bezug: Es geht darum, eine Größe zu **maximieren** (Gewinn, Fläche, Volumen) oder zu **minimieren** (Kosten, Material, Zeit) unter bestimmten Einschränkungen. Diese Aufgaben verbinden Analysis mit mathematischer Modellierung und gehören zu den wichtigsten Abiturthemen.

## Systematische Vorgehensweise

### Der Fünf-Schritte-Algorithmus

**Schritt 1: Variablen und Zielfunktion**
- Welche Größe soll optimiert werden?
- Wovon hängt diese Größe ab?
- Zielfunktion $Z = f(x_1, x_2, \ldots)$ aufstellen

**Schritt 2: Nebenbedingungen**
- Welche Einschränkungen gibt es?
- Diese als Gleichungen formulieren

**Schritt 3: Elimination**
- Nebenbedingungen nutzen, um Variablen zu eliminieren
- Zielfunktion als Funktion einer Variablen schreiben: $Z = f(x)$

**Schritt 4: Extremwertberechnung**
- Ableitung bilden: $f'(x)$
- Nullstellen von $f'(x)$ bestimmen
- Extremstellen mit $f''(x)$ klassifizieren oder Randwerte prüfen

**Schritt 5: Interpretation**
- Ergebnis im Sachkontext angeben
- Definitionsbereich beachten (sinnvolle Werte!)
- Randextrema prüfen

## Klassische Optimierungsaufgaben

### Rechteck mit maximalem Flächeninhalt

**Problem**: Ein Zaun von $40\,\text{m}$ Länge soll ein rechteckiges Feld begrenzen. Welche Abmessungen maximieren den Flächeninhalt?

**Lösung**:

*Variablen*: Länge $l$, Breite $b$

*Zielfunktion*: $A = l \cdot b$ (maximieren)

*Nebenbedingung*: $U = 2l + 2b = 40 \quad \Rightarrow \quad b = 20 - l$

*Elimination*: 
$$A(l) = l \cdot (20 - l) = 20l - l^2$$

*Ableitung und Nullstelle*:
$$A'(l) = 20 - 2l = 0 \quad \Rightarrow \quad l = 10$$

*Nachweis Maximum*: $A''(l) = -2 < 0$ ✓

*Ergebnis*: $l = b = 10\,\text{m}$, also ein Quadrat mit $A_{\max} = 100\,\text{m}^2$

### Dose mit minimalem Materialverbrauch

**Problem**: Eine zylindrische Dose soll $V_0 = 1\,\text{L} = 1000\,\text{cm}^3$ fassen. Welche Abmessungen minimieren die Oberfläche?

**Lösung**:

*Variablen*: Radius $r$, Höhe $h$

*Zielfunktion*: $A = 2\pi r^2 + 2\pi r h$ (minimieren)

*Nebenbedingung*: $V = \pi r^2 h = 1000 \quad \Rightarrow \quad h = \frac{1000}{\pi r^2}$

*Elimination*:
$$A(r) = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}$$

*Definitionsbereich*: $r > 0$

*Ableitung und Nullstelle*:
$$A'(r) = 4\pi r - \frac{2000}{r^2} = 0$$
$$4\pi r^3 = 2000 \quad \Rightarrow \quad r = \sqrt[3]{\frac{500}{\pi}} \approx 5{,}42\,\text{cm}$$

*Nachweis Minimum*: $A''(r) = 4\pi + \frac{4000}{r^3} > 0$ ✓

*Ergebnis*: 
$$r \approx 5{,}42\,\text{cm}, \quad h = \frac{1000}{\pi \cdot 5{,}42^2} \approx 10{,}84\,\text{cm}$$

Die optimale Dose hat $h = 2r$, also Höhe gleich Durchmesser.

### Maximales Volumen eines offenen Kastens

**Problem**: Aus einem quadratischen Blech ($a = 30\,\text{cm}$) werden an den Ecken quadratische Stücke ausgeschnitten und die Seiten hochgebogen. Welche Seitenlänge $x$ der Ausschnitte maximiert das Volumen?

**Lösung**:

*Variable*: Seitenlänge $x$ der Ausschnitte

*Zielfunktion* (Volumen des Kastens):
$$V(x) = x \cdot (30 - 2x)^2$$

*Definitionsbereich*: $0 < x < 15$

*Ableitung*:
$$V(x) = x(30-2x)^2 = x(900 - 120x + 4x^2) = 4x^3 - 120x^2 + 900x$$
$$V'(x) = 12x^2 - 240x + 900 = 12(x^2 - 20x + 75)$$

*Nullstellen*:
$$x_{1,2} = 10 \pm \sqrt{100 - 75} = 10 \pm 5$$
$$x_1 = 5, \quad x_2 = 15$$

*Nur $x_1 = 5$ liegt im Definitionsbereich.*

*Ergebnis*: $x = 5\,\text{cm}$, $V_{\max} = 5 \cdot 20^2 = 2000\,\text{cm}^3$

## Wirtschaftliche Optimierung

### Gewinnmaximierung

**Problem**: Ein Unternehmen hat die Kostenfunktion $K(x) = 0{,}1x^2 + 10x + 500$ und die Erlösfunktion $E(x) = 50x - 0{,}05x^2$ (in Euro). Bei welcher Stückzahl wird der Gewinn maximal?

**Lösung**:

*Gewinnfunktion*:
$$G(x) = E(x) - K(x) = 50x - 0{,}05x^2 - 0{,}1x^2 - 10x - 500$$
$$G(x) = -0{,}15x^2 + 40x - 500$$

*Ableitung*:
$$G'(x) = -0{,}3x + 40 = 0 \quad \Rightarrow \quad x = \frac{40}{0{,}3} \approx 133{,}3$$

*Ergebnis*: Bei etwa $133$ Stück ist der Gewinn maximal:
$$G(133) = -0{,}15 \cdot 133^2 + 40 \cdot 133 - 500 \approx 2166{,}67\,\text{€}$$

### Stückkosten-Minimum

Die **durchschnittlichen Stückkosten** sind:
$$k(x) = \frac{K(x)}{x} = \frac{K_f}{x} + k_v(x)$$

Das Minimum der Stückkosten liegt dort, wo Stückkosten gleich Grenzkosten sind:
$$k(x) = K'(x)$$

**Beweis**: 
$$k'(x) = \frac{K'(x) \cdot x - K(x)}{x^2} = 0 \quad \Rightarrow \quad K'(x) = \frac{K(x)}{x} = k(x)$$

## Geometrische Optimierung

### Punkt auf einer Kurve mit minimalem Abstand

**Problem**: Welcher Punkt auf der Parabel $y = x^2$ hat den kleinsten Abstand zum Punkt $P(0|4)$?

**Lösung**:

*Abstandsfunktion*: Für einen Punkt $(x, x^2)$ auf der Parabel:
$$d(x) = \sqrt{x^2 + (x^2 - 4)^2}$$

*Tipp*: Man minimiert $d^2(x)$ statt $d(x)$:
$$f(x) = x^2 + (x^2 - 4)^2 = x^2 + x^4 - 8x^2 + 16 = x^4 - 7x^2 + 16$$

*Ableitung*:
$$f'(x) = 4x^3 - 14x = 2x(2x^2 - 7) = 0$$
$$x = 0 \quad \text{oder} \quad x = \pm\sqrt{\frac{7}{2}} \approx \pm 1{,}87$$

*Vergleich*:
- $f(0) = 16 \quad \Rightarrow \quad d = 4$
- $f(\pm 1{,}87) = 3{,}5^2 - 7 \cdot 3{,}5 + 16 = 3{,}75 \quad \Rightarrow \quad d \approx 1{,}94$

*Ergebnis*: Die Punkte $(\pm\sqrt{3{,}5}, \, 3{,}5)$ haben den minimalen Abstand $\approx 1{,}94$.

### Eingeschriebenes Rechteck maximaler Fläche

**Problem**: In eine Parabel $y = 4 - x^2$ wird ein achsenparalleles Rechteck eingeschrieben (Grundseite auf der $x$-Achse). Welches Rechteck hat die größte Fläche?

**Lösung**:

*Variablen*: Die rechte obere Ecke liegt bei $(x, 4-x^2)$ mit $0 < x < 2$.

*Zielfunktion*:
$$A(x) = 2x \cdot (4 - x^2) = 8x - 2x^3$$

*Ableitung*:
$$A'(x) = 8 - 6x^2 = 0 \quad \Rightarrow \quad x = \sqrt{\frac{4}{3}} = \frac{2}{\sqrt{3}} \approx 1{,}15$$

*Ergebnis*:
- Breite: $2x = \frac{4}{\sqrt{3}} \approx 2{,}31$
- Höhe: $y = 4 - \frac{4}{3} = \frac{8}{3} \approx 2{,}67$
- Fläche: $A_{\max} = \frac{32}{3\sqrt{3}} \approx 6{,}16$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Extremwertprobleme]] — Theoretische Grundlagen
- → [[Extremstellen]] — Berechnung von Maxima und Minima
- → [[Vollstaendige-Kurvendiskussion]] — Analyse von Funktionen
- → [[Mathematische-Modellbildung]] — Der Modellierungsprozess
- → [[Optimierungsaufgaben]] — Weitere Anwendungen

> [!warning] **Prüfungsrelevant**
> - Systematisches Aufstellen von Zielfunktion und Nebenbedingung
> - Korrekte Elimination auf eine Variable
> - Definitionsbereich der Zielfunktion bestimmen
> - Randwerte und Extremstellen vergleichen
> - Ergebnis mit Einheiten im Sachkontext angeben

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Abmessungen, für die das Volumen maximal wird.
> - Bei welcher Produktionsmenge ist der Gewinn am größten?
> - Weisen Sie nach, dass ein Maximum (kein Minimum) vorliegt.
> - Begründen Sie, warum Randwerte nicht in Frage kommen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2014
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett, 2019
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Bewegungsmodelle]] — Optimierung von Bewegungsabläufen
> - [[Numerische-Naeherungsverfahren]] — Wenn analytische Lösungen schwierig sind
> - [[Vorbereitung-auf-Hochschulmathematik]] — Mehrdimensionale Optimierung
