---
author: Andreas Hümmer
title: Mathematische Simulationen
tags:
  - content
  - mathe
  - modellierung
  - simulation
  - numerik
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Mathematische Simulationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen analytischer Lösung und Simulation verstehen
> - Grundprinzipien numerischer Zeitschrittverfahren kennen
> - Einfache Simulationen mit Tabellenkalkulationen durchführen können
> - Grenzen und Fehlerquellen von Simulationen einschätzen

---

## Überblick

Eine **mathematische Simulation** ist die numerische Nachahmung eines realen oder theoretischen Systems mithilfe von Computern. Während die analytische Mathematik exakte Lösungen sucht (z.B. $y(t) = e^{-kt}$), berechnet eine Simulation Näherungswerte schrittweise.

Simulationen sind unverzichtbar, wenn:
- Keine geschlossene analytische Lösung existiert
- Das System zu komplex für exakte Lösungen ist
- Man das Verhalten unter variierenden Bedingungen studieren will

## Grundprinzip der Zeitschrittsimulation

### Die Euler-Methode

Das einfachste Verfahren zur Lösung von Differentialgleichungen ist das **Euler-Verfahren**:

Gegeben sei die Differentialgleichung $\frac{dy}{dt} = f(t, y)$ mit Anfangswert $y(0) = y_0$.

**Euler-Iteration**:
$$y_{n+1} = y_n + \Delta t \cdot f(t_n, y_n)$$

wobei $\Delta t$ die Schrittweite (Zeitschritt) ist.

### Geometrische Interpretation

Die Ableitung gibt die Tangentensteigung an. Das Euler-Verfahren folgt dieser Tangente für einen kleinen Zeitschritt und wiederholt den Prozess:

```
y
│         /
│       •
│     /   (wahrer Verlauf)
│   •
│ / 
•─────────────────── t
  Δt  Δt  Δt
```

### Fehleranalyse

- **Lokaler Fehler**: Fehler in einem Schritt, proportional zu $(\Delta t)^2$
- **Globaler Fehler**: Gesamtfehler, proportional zu $\Delta t$
- **Kleinere Schrittweite** → genauere Lösung, aber mehr Rechenaufwand

## Simulation von Wachstumsprozessen

### Exponentielles Wachstum simulieren

**Differentialgleichung**: $\frac{dN}{dt} = kN$

**Euler-Iteration**:
$$N_{n+1} = N_n + \Delta t \cdot k \cdot N_n = N_n (1 + k \cdot \Delta t)$$

**Beispiel**: Bakterienwachstum mit $N_0 = 1000$, $k = 0{,}5\,\text{h}^{-1}$, $\Delta t = 0{,}1\,\text{h}$

| $t$ (h) | $N$ (Simulation) | $N$ (exakt: $1000 \cdot e^{0{,}5t}$) |
|---------|------------------|--------------------------------------|
| 0 | 1000 | 1000 |
| 0,1 | 1050 | 1051,3 |
| 0,2 | 1102,5 | 1105,2 |
| 0,5 | 1276,3 | 1284,0 |
| 1,0 | 1628,9 | 1648,7 |

Der Fehler beträgt etwa $1{-}2\%$ bei $\Delta t = 0{,}1$.

### Logistisches Wachstum simulieren

**Differentialgleichung**: $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$

**Euler-Iteration**:
$$N_{n+1} = N_n + \Delta t \cdot r \cdot N_n \cdot \left(1 - \frac{N_n}{K}\right)$$

**Beispiel**: Population mit $N_0 = 100$, $K = 1000$, $r = 0{,}5$, $\Delta t = 0{,}5$

| $t$ | $N$ |
|-----|-----|
| 0 | 100 |
| 0,5 | 122,5 |
| 1,0 | 149,0 |
| 2,0 | 217,8 |
| 5,0 | 505,1 |
| 10,0 | 878,3 |
| 20,0 | 993,5 |

Die Population nähert sich der Kapazitätsgrenze $K = 1000$.

## Simulation von Bewegungen

### Fallbewegung mit Luftwiderstand

**Modell**: $\frac{dv}{dt} = g - \frac{c}{m}v^2$

wobei $c$ der Luftwiderstandskoeffizient ist.

**Euler-Iteration**:
$$v_{n+1} = v_n + \Delta t \cdot \left(g - \frac{c}{m}v_n^2\right)$$
$$h_{n+1} = h_n - \Delta t \cdot v_n$$

**Beispiel**: Fallschirmspringer ($m = 80\,\text{kg}$, $c = 0{,}25\,\frac{\text{kg}}{\text{m}}$)

Grenzgeschwindigkeit: $v_{\infty} = \sqrt{\frac{mg}{c}} = \sqrt{\frac{80 \cdot 9{,}81}{0{,}25}} \approx 56\,\frac{\text{m}}{\text{s}}$

### Projektilbewegung in 2D

**Gleichungen**:
$$\frac{dv_x}{dt} = -\frac{c}{m}v_x\sqrt{v_x^2 + v_y^2}$$
$$\frac{dv_y}{dt} = -g - \frac{c}{m}v_y\sqrt{v_x^2 + v_y^2}$$

**Iteration** (für jede Komponente):
$$v_{x,n+1} = v_{x,n} + \Delta t \cdot a_{x,n}$$
$$x_{n+1} = x_n + \Delta t \cdot v_{x,n}$$

(analog für $y$-Komponente)

## Simulation von Schwingungen

### Harmonischer Oszillator

**Differentialgleichung**: $\frac{d^2y}{dt^2} = -\omega^2 y$

Umschreiben als System erster Ordnung:
$$\frac{dy}{dt} = v, \quad \frac{dv}{dt} = -\omega^2 y$$

**Euler-Iteration**:
$$y_{n+1} = y_n + \Delta t \cdot v_n$$
$$v_{n+1} = v_n + \Delta t \cdot (-\omega^2 y_n)$$

> [!warning] **Problem des Euler-Verfahrens**
> Bei Schwingungen addiert das Euler-Verfahren systematisch Energie hinzu — die simulierte Amplitude wächst langsam. Bessere Verfahren (Runge-Kutta, symplektische Integratoren) vermeiden dieses Problem.

### Gedämpfter Oszillator

**System**:
$$\frac{dy}{dt} = v, \quad \frac{dv}{dt} = -\omega^2 y - 2\gamma v$$

Die Dämpfung sorgt hier für Energieverlust, was den numerischen Energiezuwachs teilweise kompensiert.

## Simulation mit Tabellenkalkulation

### Aufbau einer Simulationstabelle

| Spalte A | Spalte B | Spalte C | Spalte D |
|----------|----------|----------|----------|
| $t$ | $y$ | $y'$ | (Hilfsgrößen) |
| 0 | $y_0$ | =f(A2,B2) | ... |
| =A2+Δt | =B2+Δt*C2 | =f(A3,B3) | ... |

**Vorgehensweise**:
1. Parameter ($\Delta t$, $k$, etc.) in separaten Zellen definieren
2. Anfangswerte in erste Zeile eintragen
3. Formeln für nächsten Zeitschritt aufstellen
4. Formeln nach unten kopieren
5. Diagramm erstellen

### Beispiel: Exponentieller Zerfall in Excel/Calc

```
A1: "t"      B1: "N"       C1: "dN/dt"    D1: "N_exakt"
A2: 0        B2: 1000      C2: =-0.1*B2   D2: =1000*EXP(-0.1*A2)
A3: =A2+0.1  B3: =B2+0.1*C2  C3: =-0.1*B3   D3: =1000*EXP(-0.1*A3)
```

## Monte-Carlo-Simulationen

### Prinzip

Bei Monte-Carlo-Methoden werden Zufallszahlen genutzt, um Probleme zu lösen:
- Schätzung von Wahrscheinlichkeiten
- Approximation von Integralen
- Simulation stochastischer Prozesse

### Beispiel: $\pi$ durch Simulation

Ein Quadrat der Seitenlänge $2$ enthält einen Kreis mit Radius $1$. Durch zufälliges Werfen von Punkten kann $\pi$ geschätzt werden:

$$\frac{\text{Treffer im Kreis}}{\text{Gesamtanzahl}} \approx \frac{\pi}{4}$$

**Algorithmus**:
1. Erzeuge zufällige Punkte $(x, y)$ mit $-1 \leq x, y \leq 1$
2. Prüfe: $x^2 + y^2 \leq 1$? → Treffer!
3. Schätze: $\pi \approx 4 \cdot \frac{\text{Treffer}}{N}$

Mit $N = 10000$ Punkten erhält man typischerweise $\pi \approx 3{,}14 \pm 0{,}02$.

## Fehlerquellen und Grenzen

### Systematische Fehler

- **Diskretisierungsfehler**: Durch endliche Schrittweite
- **Modellfehler**: Das Modell vereinfacht die Realität
- **Rundungsfehler**: Begrenzte Rechengenauigkeit

### Stabilitätsprobleme

Bei zu großer Schrittweite können Simulationen instabil werden:
- Oszillationen statt Konvergenz
- Exponentielles Anwachsen der Lösung
- Negative Werte bei eigentlich positiven Größen

**Faustregel**: $\Delta t$ sollte viel kleiner als die charakteristische Zeitskala des Systems sein.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Numerische-Naeherungsverfahren]] — Theoretische Grundlagen
- → [[Wachstumsmodelle]] — Analytische Lösungen zum Vergleich
- → [[Schwingungsmodelle]] — Oszillatorsimulation
- → [[Funktionendarstellung-mit-Python]] — Programmierung von Simulationen
- → [[Wahrscheinlichkeitsmodelle-implementieren]] — Monte-Carlo-Methoden

> [!warning] **Prüfungsrelevant**
> - Euler-Verfahren verstehen und anwenden
> - Simulationstabelle aufstellen können
> - Einfluss der Schrittweite auf die Genauigkeit
> - Vergleich zwischen Simulation und analytischer Lösung
> - Grenzen von Simulationen benennen

> [!question] **Typische Prüfungsfragen**
> - Führen Sie drei Schritte des Euler-Verfahrens für die gegebene DGL durch.
> - Wie verändert sich die Genauigkeit, wenn Sie die Schrittweite halbieren?
> - Vergleichen Sie Ihr Simulationsergebnis mit der exakten Lösung.
> - Welche Fehlerquellen können bei dieser Simulation auftreten?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2. Springer Vieweg, 2015
- Press, W.H. et al.: Numerical Recipes. Cambridge University Press, 2007
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Funktionendarstellung-mit-Python]] — Simulationen programmieren
> - [[Numerische-Naeherungsverfahren]] — Verbesserte Verfahren (Runge-Kutta)
> - [[Vorbereitung-auf-Hochschulmathematik]] — Numerik an der Hochschule
