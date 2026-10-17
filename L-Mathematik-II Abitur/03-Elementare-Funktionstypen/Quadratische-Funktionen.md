---
author: Andreas Hümmer
title: Quadratische Funktionen
tags:
  - content
  - mathe
  - funktionen
  - quadratische-funktion
  - parabel
created: 2025-06-19
modified: 2025-06-19
---

# Quadratische Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Quadratische Funktionen in verschiedenen Darstellungsformen angeben und umwandeln können
> - Den Scheitelpunkt einer Parabel berechnen und die Scheitelpunktform aufstellen können
> - Nullstellen mit verschiedenen Verfahren bestimmen können
> - Quadratische Modelle zur Lösung von Extremwertproblemen einsetzen können

---

## Überblick

Quadratische Funktionen sind Polynomfunktionen zweiten Grades. Ihre Graphen sind Parabeln — symmetrische Kurven mit genau einem Extrempunkt, dem Scheitel. Quadratische Funktionen beschreiben viele natürliche und technische Phänomene wie den freien Fall, Wurfparabeln und Gewinnfunktionen in der Ökonomie. Sie bilden die Brücke zwischen linearen Funktionen und allgemeinen Polynomfunktionen.

## Darstellungsformen

### Allgemeine Form (Normalform)

$$f(x) = ax^2 + bx + c \quad \text{mit } a \neq 0$$

Die Parameter haben folgende Bedeutung:
- $a$ — **Öffnungsfaktor**: bestimmt Weite und Richtung der Öffnung
- $b$ — beeinflusst die Lage der Symmetrieachse
- $c$ — **y-Achsenabschnitt**: $f(0) = c$

### Scheitelpunktform

$$f(x) = a(x - x_S)^2 + y_S$$

Der Scheitelpunkt hat die Koordinaten $S(x_S|y_S)$.

**Umrechnung von Normalform zu Scheitelpunktform:**

$$x_S = -\frac{b}{2a}, \quad y_S = f(x_S) = c - \frac{b^2}{4a}$$

**Beispiel:**
$f(x) = 2x^2 - 8x + 5$

$$x_S = -\frac{-8}{2 \cdot 2} = 2, \quad y_S = 5 - \frac{64}{8} = 5 - 8 = -3$$

Scheitelpunktform: $f(x) = 2(x-2)^2 - 3$

### Linearfaktorform (Produktform)

Wenn Nullstellen $x_1$ und $x_2$ existieren:

$$f(x) = a(x - x_1)(x - x_2)$$

## Eigenschaften der Parabel

### Symmetrie

Jede Parabel ist **achsensymmetrisch** zur Geraden $x = x_S$ (Symmetrieachse durch den Scheitel).

$$f(x_S + t) = f(x_S - t) \quad \text{für alle } t \in \mathbb{R}$$

### Monotonie

- Für $a > 0$ (nach oben geöffnet):
  - streng monoton fallend auf $(-\infty, x_S]$
  - streng monoton steigend auf $[x_S, +\infty)$
- Für $a < 0$ (nach unten geöffnet): umgekehrt

### Krümmung und Öffnungsrichtung

| Bedingung | Öffnung | Scheitel |
|-----------|---------|----------|
| $a > 0$ | nach oben | Tiefpunkt (Minimum) |
| $a < 0$ | nach unten | Hochpunkt (Maximum) |
| $|a| > 1$ | schmal | — |
| $|a| < 1$ | weit | — |

### Wertebereich

- $a > 0$: $W_f = [y_S, +\infty)$
- $a < 0$: $W_f = (-\infty, y_S]$

## Nullstellen

Die Nullstellen ergeben sich aus $ax^2 + bx + c = 0$.

### Mitternachtsformel (p-q-Formel Alternative)

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Diskriminante

Die **Diskriminante** $D = b^2 - 4ac$ bestimmt die Anzahl der Nullstellen:

| Diskriminante | Nullstellen | Geometrie |
|---------------|-------------|-----------|
| $D > 0$ | 2 verschiedene | Parabel schneidet x-Achse |
| $D = 0$ | 1 (doppelte) | Parabel berührt x-Achse |
| $D < 0$ | keine (in $\mathbb{R}$) | Parabel liegt über/unter x-Achse |

### Satz von Vieta

Für eine quadratische Gleichung $x^2 + px + q = 0$ mit Lösungen $x_1$ und $x_2$ gilt:

$$x_1 + x_2 = -p \quad \text{und} \quad x_1 \cdot x_2 = q$$

**Anwendung:** Schnelles Erraten ganzzahliger Nullstellen.

**Beispiel:** $x^2 - 5x + 6 = 0$
Gesucht: Zwei Zahlen mit Summe 5 und Produkt 6 → $x_1 = 2$, $x_2 = 3$

## Quadratische Ergänzung

Die quadratische Ergänzung transformiert die Normalform in die Scheitelpunktform:

$$ax^2 + bx + c = a\left(x^2 + \frac{b}{a}x\right) + c$$
$$= a\left(x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} - \frac{b^2}{4a^2}\right) + c$$
$$= a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a} + c$$

**Beispiel:** $f(x) = x^2 + 6x + 5$

$$= (x^2 + 6x + 9) - 9 + 5 = (x+3)^2 - 4$$

Scheitel: $S(-3|-4)$

## Bestimmung quadratischer Funktionen

### Aus drei Punkten

Drei Punkte $P_1(x_1|y_1)$, $P_2(x_2|y_2)$, $P_3(x_3|y_3)$ ergeben ein lineares Gleichungssystem:

$$\begin{cases}
ax_1^2 + bx_1 + c = y_1 \\
ax_2^2 + bx_2 + c = y_2 \\
ax_3^2 + bx_3 + c = y_3
\end{cases}$$

### Aus Scheitel und weiterem Punkt

Mit $S(x_S|y_S)$ und Punkt $P(x_P|y_P)$:

$$a = \frac{y_P - y_S}{(x_P - x_S)^2}$$

### Aus Nullstellen und weiterem Punkt

Mit Nullstellen $x_1$, $x_2$ und Punkt $P(x_P|y_P)$:

$$a = \frac{y_P}{(x_P - x_1)(x_P - x_2)}$$

## Anwendungen

### Wurfparabel

Der schiefe Wurf wird durch eine quadratische Funktion beschrieben:

$$y(x) = -\frac{g}{2v_0^2 \cos^2(\alpha)} x^2 + \tan(\alpha) \cdot x + h_0$$

wobei $v_0$ die Anfangsgeschwindigkeit, $\alpha$ der Abwurfwinkel und $h_0$ die Anfangshöhe ist.

### Extremwertaufgaben

**Beispiel:** Ein Rechteck mit Umfang 20 m soll maximalen Flächeninhalt haben.

Mit Seitenlängen $x$ und $y$ gilt: $2x + 2y = 20 \Rightarrow y = 10 - x$

Flächenfunktion: $A(x) = x \cdot (10-x) = -x^2 + 10x$

Scheitel: $x_S = \frac{10}{2} = 5$, also $y_S = 5$

Maximale Fläche: $A(5) = 25$ m² (Quadrat)

### Gewinnmaximierung

Bei linearer Preis-Absatz-Funktion $p(x) = a - bx$ und linearen Kosten $K(x) = kx + K_f$:

$$G(x) = p(x) \cdot x - K(x) = -bx^2 + (a-k)x - K_f$$

Die gewinnmaximale Menge liegt beim Scheitelpunkt der nach unten geöffneten Parabel.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Lineare-Funktionen]] — Spezialfall für $a = 0$
- → [[Polynomfunktionen]] — Verallgemeinerung auf höhere Grade
- → [[Nullstellen]] — Allgemeine Nullstellentheorie
- → [[Symmetrie]] — Achsensymmetrie bei Funktionen
- → [[Gleichungen-hoeheren-Grades]] — Biquadratische Gleichungen
- → [[Transformationen]] — Verschiebung und Streckung von Parabeln

> [!warning] **Prüfungsrelevant**
> - Sichere Beherrschung der quadratischen Ergänzung zur Scheitelpunktbestimmung
> - Mitternachtsformel und Interpretation der Diskriminante
> - Aufstellen quadratischer Funktionen aus verschiedenen Bedingungen
> - Lösung von Extremwertproblemen durch Scheitelbestimmung
> - Anwendungsaufgaben zur Wurfparabel und Gewinnmaximierung

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie den Scheitelpunkt der Parabel $f(x) = 2x^2 - 12x + 13$ mittels quadratischer Ergänzung.
> - Für welche Werte von $k$ hat die Gleichung $x^2 + 4x + k = 0$ genau eine Lösung?
> - Ein Ball wird von einem 2 m hohen Podest mit 15 m/s unter 45° abgeworfen. Bestimmen Sie die maximale Höhe und die Wurfweite.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Abiturprüfungsaufgaben Mathematik*, verschiedene Jahrgänge

> [!tip] **Weiterführende Links**
> - [[05-Differentialrechnung-I|Differentialrechnung I]] — Extremwertbestimmung mit Ableitungen
> - [[Einfuehrung-in-komplexe-Zahlen]] — Nullstellen bei negativer Diskriminante

