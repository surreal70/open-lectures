---
author: Andreas Hümmer
title: Durchschnittliche Änderungsrate
tags:
  - content
  - mathe
  - differentialrechnung
  - aenderungsrate
  - sekante
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Durchschnittliche Änderungsrate

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die durchschnittliche Änderungsrate einer Funktion in einem Intervall berechnen können
> - Den Zusammenhang zwischen durchschnittlicher Änderungsrate und Sekantensteigung verstehen
> - Die durchschnittliche Änderungsrate in Sachkontexten interpretieren können
> - Die Notation mit dem Differenzenquotienten sicher anwenden können

---

## Überblick

Die durchschnittliche Änderungsrate beschreibt, wie sich die Funktionswerte einer Funktion *im Mittel* über ein bestimmtes Intervall ändern. Sie ist der Ausgangspunkt für das Verständnis der momentanen Änderungsrate und damit der Ableitung. Geometrisch entspricht sie der Steigung einer Sekante durch zwei Punkte des Funktionsgraphen.

## Definition

> [!note] **Definition: Durchschnittliche Änderungsrate**
> Die **durchschnittliche Änderungsrate** einer Funktion $f$ im Intervall $[x_1, x_2]$ ist definiert als:
> $$\bar{m} = \frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

Die durchschnittliche Änderungsrate gibt an, um wie viele Einheiten sich der Funktionswert *im Durchschnitt* ändert, wenn das Argument um eine Einheit zunimmt.

## Alternative Schreibweisen

Mit $h = x_2 - x_1$ als Intervalllänge und $x_1 = x_0$ als Startwert können wir schreiben:

$$\bar{m} = \frac{f(x_0 + h) - f(x_0)}{h}$$

Diese Schreibweise ist besonders nützlich für den späteren Grenzübergang zur [[Momentane-aenderungsrate|momentanen Änderungsrate]].

## Geometrische Interpretation

Die durchschnittliche Änderungsrate ist die **Steigung der Sekante** durch die Punkte $P(x_1 | f(x_1))$ und $Q(x_2 | f(x_2))$ auf dem Graphen von $f$.

```
       y
       |
       |        Q(x₂|f(x₂))
       |       /
       |      /  Δy = f(x₂) - f(x₁)
       |     / |
       | P  /  |
       |---/---|
       |       Δx = x₂ - x₁
       |
       +-----|-----|---------> x
            x₁    x₂
```

Die Steigung der Sekante berechnet sich wie bei jeder Geraden durch zwei Punkte als:

$$m_{\text{Sekante}} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

## Berechnungsbeispiele

### Beispiel 1: Polynomfunktion

Gegeben ist $f(x) = x^2 - 2x + 1$. Berechne die durchschnittliche Änderungsrate im Intervall $[1, 4]$.

**Lösung:**
$$\bar{m} = \frac{f(4) - f(1)}{4 - 1} = \frac{(16 - 8 + 1) - (1 - 2 + 1)}{3} = \frac{9 - 0}{3} = 3$$

Die Funktionswerte steigen im Intervall $[1, 4]$ im Durchschnitt um 3 Einheiten pro Einheit auf der $x$-Achse.

### Beispiel 2: Exponentialfunktion

Gegeben ist $f(x) = 2^x$. Berechne die durchschnittliche Änderungsrate im Intervall $[0, 3]$.

**Lösung:**
$$\bar{m} = \frac{f(3) - f(0)}{3 - 0} = \frac{2^3 - 2^0}{3} = \frac{8 - 1}{3} = \frac{7}{3} \approx 2{,}33$$

### Beispiel 3: Mit h-Schreibweise

Gegeben ist $f(x) = x^3$. Berechne die durchschnittliche Änderungsrate an der Stelle $x_0 = 2$ mit Schrittweite $h = 0{,}1$.

**Lösung:**
$$\bar{m} = \frac{f(2 + 0{,}1) - f(2)}{0{,}1} = \frac{f(2{,}1) - f(2)}{0{,}1} = \frac{9{,}261 - 8}{0{,}1} = \frac{1{,}261}{0{,}1} = 12{,}61$$

## Anwendung in Sachkontexten

### Beispiel: Bevölkerungswachstum

Die Bevölkerung einer Stadt wird durch $B(t) = 50000 \cdot 1{,}02^t$ modelliert, wobei $t$ die Zeit in Jahren seit 2020 ist.

**Durchschnittliche Wachstumsrate von 2020 bis 2025:**

$$\bar{m} = \frac{B(5) - B(0)}{5 - 0} = \frac{50000 \cdot 1{,}02^5 - 50000}{5}$$
$$= \frac{55204 - 50000}{5} = \frac{5204}{5} = 1040{,}8$$

**Interpretation:** Die Bevölkerung wächst zwischen 2020 und 2025 im Durchschnitt um etwa 1041 Personen pro Jahr.

### Beispiel: Kostenrechnung

Die Gesamtkosten für die Produktion von $x$ Einheiten betragen $K(x) = 0{,}01x^2 + 5x + 200$ (in Euro).

**Durchschnittliche Stückkosten bei Erhöhung der Produktion von 100 auf 150 Stück:**

$$\bar{m} = \frac{K(150) - K(100)}{150 - 100} = \frac{(225 + 750 + 200) - (100 + 500 + 200)}{50}$$
$$= \frac{1175 - 800}{50} = \frac{375}{50} = 7{,}50\,\frac{\text{€}}{\text{Stück}}$$

**Interpretation:** Jede zusätzliche Einheit kostet im Durchschnitt 7,50 € in diesem Produktionsbereich.

## Eigenschaften der durchschnittlichen Änderungsrate

### Vorzeichen

- $\bar{m} > 0$: Funktion ist im Intervall im Mittel **steigend**
- $\bar{m} < 0$: Funktion ist im Intervall im Mittel **fallend**
- $\bar{m} = 0$: Funktion hat an den Intervallenden **gleiche Werte** (sagt nichts über den Verlauf dazwischen)

### Spezialfall: Lineare Funktionen

Bei [[Lineare-Funktionen|linearen Funktionen]] $f(x) = mx + b$ ist die durchschnittliche Änderungsrate in jedem Intervall gleich der Steigung $m$:

$$\bar{m} = \frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{(mx_2 + b) - (mx_1 + b)}{x_2 - x_1} = \frac{m(x_2 - x_1)}{x_2 - x_1} = m$$

## Grenzen der durchschnittlichen Änderungsrate

Die durchschnittliche Änderungsrate kann das lokale Verhalten einer Funktion nicht erfassen:

- Sie sagt nichts über den Verlauf der Funktion *zwischen* den beiden Punkten aus
- Sie kann lokale Extrema oder Wendepunkte nicht erkennen
- Verschiedene Funktionen können dieselbe durchschnittliche Änderungsrate haben

Um das Verhalten an einem *bestimmten Punkt* zu beschreiben, benötigen wir die [[Momentane-aenderungsrate|momentane Änderungsrate]].

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[aenderungsraten|Änderungsraten]] – Einführung und Motivation
- → [[Momentane-aenderungsrate|Momentane Änderungsrate]] – Der Grenzübergang
- → [[Differenzenquotient|Differenzenquotient]] – Formale Bezeichnung
- → [[Lineare-Funktionen|Lineare Funktionen]] – Konstante Änderungsrate
- → [[Monotonie|Monotonie]] – Zusammenhang mit dem Vorzeichen

> [!warning] **Prüfungsrelevant**
> - Die Formel $\bar{m} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$ muss sicher angewendet werden können
> - Die geometrische Deutung als Sekantensteigung wird häufig abgefragt
> - Interpretation im Sachkontext ist essentiell (Einheiten angeben!)
> - Die alternative Schreibweise mit $h$ ist Grundlage für die Definition der Ableitung

> [!question] **Typische Prüfungsfragen**
> - "Berechnen Sie die durchschnittliche Änderungsrate von $f$ im Intervall $[a, b]$."
> - "Interpretieren Sie die durchschnittliche Änderungsrate im gegebenen Sachzusammenhang."
> - "Welche geometrische Bedeutung hat die durchschnittliche Änderungsrate?"

## Quellen

- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Differentialquotient|Differentialquotient]] – Der Grenzwert des Differenzenquotienten
> - [[Geometrische-Bedeutung-der-Ableitung|Geometrische Bedeutung der Ableitung]] – Von der Sekante zur Tangente
