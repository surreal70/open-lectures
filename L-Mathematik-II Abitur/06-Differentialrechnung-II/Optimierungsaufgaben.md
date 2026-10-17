---
author: Andreas Hümmer
title: Optimierungsaufgaben
tags:
  - content
  - mathe
  - differentialrechnung
  - optimierung
  - anwendungen
created: 2025-06-20
modified: 2025-06-20
---

# Optimierungsaufgaben

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verschiedene Typen von Optimierungsaufgaben erkennen und lösen können
> - Geometrische Optimierungsprobleme systematisch bearbeiten können
> - Ökonomische Optimierungsaufgaben verstehen und lösen können
> - Optimierung mit Randbedingungen durchführen können

---

## Überblick

**Optimierungsaufgaben** sind praktische Anwendungen der Extremwertrechnung aus verschiedenen Bereichen wie Geometrie, Wirtschaft, Physik und Technik. In diesem Kapitel werden verschiedene Aufgabentypen systematisch vorgestellt und gelöst. Der Schwerpunkt liegt auf der Übertragung der mathematischen Methoden auf konkrete Problemstellungen.

## Geometrische Optimierung

### Beispiel 1: Einbeschriebenes Rechteck

**Aufgabe:** In ein rechtwinkliges Dreieck mit Katheten $a = 6$ und $b = 4$ soll ein Rechteck mit maximaler Fläche einbeschrieben werden, wobei eine Seite auf der Hypotenuse liegt.

**Lösung:**

Wir legen das Koordinatensystem so, dass die Katheten auf den Achsen liegen:
- Eckpunkte des Dreiecks: $O(0|0)$, $A(6|0)$, $B(0|4)$
- Hypotenuse: Gerade durch $A$ und $B$ mit Gleichung $\frac{x}{6} + \frac{y}{4} = 1$, also $y = 4 - \frac{2x}{3}$

Sei $P(x|0)$ ein Punkt auf der $x$-Achse mit $0 < x < 6$.
Die Höhe des Rechtecks ist dann $h = 4 - \frac{2x}{3}$.

**Zielfunktion:**
$$A(x) = x \cdot \left(4 - \frac{2x}{3}\right) = 4x - \frac{2x^2}{3}$$

**Extremum:**
$$A'(x) = 4 - \frac{4x}{3} = 0 \implies x = 3$$

$$A''(x) = -\frac{4}{3} < 0 \implies \text{Maximum}$$

**Ergebnis:**
- Breite: $x = 3$
- Höhe: $h = 4 - 2 = 2$
- Maximale Fläche: $A = 3 \cdot 2 = 6$

### Beispiel 2: Zylinder in einer Kugel

**Aufgabe:** In eine Kugel mit Radius $R$ ist ein Zylinder mit maximalem Volumen einzubeschreiben.

**Lösung:**

Sei $r$ der Radius und $h$ die Höhe des Zylinders.

Aus der Geometrie (Pythagoras im Achsenschnitt):
$$r^2 + \left(\frac{h}{2}\right)^2 = R^2$$
$$\implies r^2 = R^2 - \frac{h^2}{4}$$

**Zielfunktion:**
$$V(h) = \pi r^2 h = \pi \left(R^2 - \frac{h^2}{4}\right) h = \pi R^2 h - \frac{\pi h^3}{4}$$

**Extremum:**
$$V'(h) = \pi R^2 - \frac{3\pi h^2}{4} = 0$$
$$h^2 = \frac{4R^2}{3} \implies h = \frac{2R}{\sqrt{3}} = \frac{2R\sqrt{3}}{3}$$

**Radius:**
$$r^2 = R^2 - \frac{1}{4} \cdot \frac{4R^2}{3} = R^2 - \frac{R^2}{3} = \frac{2R^2}{3}$$
$$r = R\sqrt{\frac{2}{3}}$$

**Maximales Volumen:**
$$V_{\max} = \frac{4\pi R^3}{3\sqrt{3}} = \frac{4\pi R^3 \sqrt{3}}{9}$$

## Ökonomische Optimierung

### Gewinnmaximierung

Ein Unternehmen produziert ein Gut mit:
- **Erlösfunktion:** $E(x) = p \cdot x$ (Preis mal Menge)
- **Kostenfunktion:** $K(x) = K_f + K_v(x)$ (Fixkosten plus variable Kosten)
- **Gewinnfunktion:** $G(x) = E(x) - K(x)$

**Beispiel:** 
$$K(x) = 0{,}01x^3 - 0{,}9x^2 + 30x + 100$$
$$E(x) = 50x$$

**Gewinnfunktion:**
$$G(x) = 50x - (0{,}01x^3 - 0{,}9x^2 + 30x + 100)$$
$$G(x) = -0{,}01x^3 + 0{,}9x^2 + 20x - 100$$

**Gewinnmaximum:**
$$G'(x) = -0{,}03x^2 + 1{,}8x + 20 = 0$$
$$x^2 - 60x - \frac{2000}{3} = 0$$

Mit der Mitternachtsformel: $x \approx 70$ Einheiten

### Kostenminimierung: Stückkosten

Die **Stückkosten** (Durchschnittskosten) sind:
$$k(x) = \frac{K(x)}{x}$$

Das Minimum der Stückkosten liegt dort, wo Stückkosten gleich Grenzkosten sind:
$$k(x) = K'(x)$$

**Herleitung:**
$$k'(x) = \frac{K'(x) \cdot x - K(x)}{x^2} = 0$$
$$\implies K'(x) \cdot x = K(x) \implies K'(x) = \frac{K(x)}{x} = k(x)$$

## Optimierung unter Randbedingungen

### Abgeschlossene Intervalle

Bei Optimierung auf einem abgeschlossenen Intervall $[a, b]$ können Extrema auch an den Rändern liegen.

**Vorgehen:**
1. Finde kritische Stellen im Inneren $(a, b)$
2. Berechne Funktionswerte an kritischen Stellen und Randpunkten
3. Vergleiche alle Werte

**Beispiel:** $f(x) = x^3 - 3x + 1$ auf $[-2, 2]$

$$f'(x) = 3x^2 - 3 = 0 \implies x = \pm 1$$

| $x$ | $-2$ | $-1$ | $1$ | $2$ |
|-----|------|------|-----|-----|
| $f(x)$ | $-1$ | $3$ | $-1$ | $3$ |

Globales Maximum: $f(-1) = f(2) = 3$
Globales Minimum: $f(-2) = f(1) = -1$

### Natürliche Einschränkungen

Oft ergeben sich Definitionsbereiche aus dem Sachkontext:
- Längen, Flächen, Volumen: positiv
- Mengen: nicht-negativ, oft ganzzahlig
- Prozentsätze: zwischen 0 und 100

## Zusammenfassung der Lösungsstrategie

| Schritt | Aktion |
|---------|--------|
| 1 | Skizze anfertigen, Größen benennen |
| 2 | Zielfunktion $f(x)$ aufstellen |
| 3 | Nebenbedingung nutzen, um auf eine Variable zu reduzieren |
| 4 | Definitionsbereich festlegen |
| 5 | $f'(x) = 0$ lösen |
| 6 | Art des Extremums prüfen |
| 7 | Randwerte prüfen (falls abgeschlossen) |
| 8 | Ergebnis berechnen und interpretieren |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Extremwertprobleme]] – Grundlegende Methodik
- → [[Extremstellen]] – Mathematische Grundlagen
- → [[Vollstaendige-Kurvendiskussion]] – Analyse der Zielfunktion
- → [[Anwendungen-in-Physik-und-Technik]] – Physikalische Optimierung
- → [[Exponentielles-Wachstum]] – Wachstumsoptimierung

> [!warning] **Prüfungsrelevant**
> - Bei geometrischen Aufgaben: Skizze mit eingezeichneten Variablen
> - Ökonomische Aufgaben: Unterscheide Gewinn-, Erlös- und Kostenfunktion
> - Abgeschlossene Intervalle: Randwerte nie vergessen
> - Definitionsbereich aus Sachkontext ableiten
> - Ergebnis im Kontext interpretieren und Einheiten angeben

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Abmessungen des Körpers mit maximalem Volumen
> - Bei welcher Produktionsmenge wird der Gewinn maximal?
> - Zeigen Sie, dass das Optimum die Beziehung ... erfüllt
> - Wie ändert sich das Ergebnis bei Variation eines Parameters?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Extremwertprobleme]] – Weitere Grundlagen
> - [[Anwendungen-in-Physik-und-Technik]] – Technische Anwendungen
