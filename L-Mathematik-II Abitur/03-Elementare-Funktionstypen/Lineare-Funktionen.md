---
author: Andreas Hümmer
title: Lineare Funktionen
tags:
  - content
  - mathe
  - funktionen
  - lineare-funktion
  - gerade
created: 2025-06-19
modified: 2025-06-19
---

# Lineare Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Darstellungsformen linearer Funktionen beherrschen und ineinander umwandeln können
> - Geradengleichungen aus gegebenen Bedingungen aufstellen können
> - Die Lagebeziehungen zweier Geraden analysieren und Schnittpunkte berechnen können
> - Lineare Modelle auf Anwendungsprobleme anwenden können

---

## Überblick

Lineare Funktionen sind Funktionen ersten Grades und bilden die einfachste Klasse der Polynomfunktionen. Sie beschreiben proportionale Zusammenhänge mit konstantem Änderungsverhalten und werden durch Geraden im Koordinatensystem dargestellt. Als fundamentaler Funktionstyp bilden sie die Grundlage für das Verständnis komplexerer Funktionen und spielen in der linearen Algebra sowie bei Näherungsverfahren (Linearisierung) eine zentrale Rolle.

## Definition und Darstellungsformen

### Normalform (Explizite Form)

Eine lineare Funktion hat die allgemeine Form:

$$f(x) = mx + n$$

Dabei bedeuten:
- $m$ — **Steigung** (Anstieg): gibt an, um wie viele Einheiten sich $y$ ändert, wenn $x$ um eine Einheit zunimmt
- $n$ — **y-Achsenabschnitt**: der Schnittpunkt der Geraden mit der y-Achse, also $f(0) = n$

**Beispiel:**
Die Funktion $f(x) = 2x - 3$ hat die Steigung $m = 2$ und den y-Achsenabschnitt $n = -3$.

### Punkt-Steigungs-Form

Ist ein Punkt $P(x_0|y_0)$ und die Steigung $m$ gegeben:

$$y - y_0 = m(x - x_0)$$

**Beispiel:**
Eine Gerade durch $P(2|5)$ mit Steigung $m = 3$:
$$y - 5 = 3(x - 2) \quad \Rightarrow \quad y = 3x - 1$$

### Zwei-Punkte-Form

Sind zwei Punkte $P_1(x_1|y_1)$ und $P_2(x_2|y_2)$ gegeben, berechnet sich die Steigung:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

**Beispiel:**
Für $P_1(1|2)$ und $P_2(4|8)$:
$$m = \frac{8-2}{4-1} = \frac{6}{3} = 2$$

### Achsenabschnittsform

Mit x-Achsenabschnitt $a$ und y-Achsenabschnitt $b$ (beide $\neq 0$):

$$\frac{x}{a} + \frac{y}{b} = 1$$

### Allgemeine Form (Implizite Form)

$$Ax + By + C = 0 \quad \text{mit } A, B \in \mathbb{R}, \, B \neq 0$$

Die Umrechnung zur Normalform ergibt: $y = -\frac{A}{B}x - \frac{C}{B}$

## Eigenschaften linearer Funktionen

### Monotonie

Lineare Funktionen sind auf ganz $\mathbb{R}$ streng monoton:
- $m > 0$: streng monoton **steigend**
- $m < 0$: streng monoton **fallend**
- $m = 0$: **konstant** (Sonderfall: horizontale Gerade)

### Nullstelle

Die Nullstelle einer linearen Funktion (für $m \neq 0$):

$$f(x_0) = 0 \quad \Rightarrow \quad x_0 = -\frac{n}{m}$$

### Definitionsbereich und Wertebereich

- **Definitionsbereich**: $D_f = \mathbb{R}$
- **Wertebereich**: $W_f = \mathbb{R}$ (für $m \neq 0$) bzw. $W_f = \{n\}$ (für $m = 0$)

### Steigungsdreieck

Die Steigung kann geometrisch als Verhältnis interpretiert werden:

```
        ╱
       ╱│ Δy
      ╱ │
     ╱──┘
      Δx

m = Δy/Δx = tan(α)
```

Der Winkel $\alpha$ zwischen Gerade und positiver x-Achse erfüllt: $m = \tan(\alpha)$

## Lagebeziehungen zweier Geraden

Gegeben seien zwei Geraden $g_1: y = m_1 x + n_1$ und $g_2: y = m_2 x + n_2$.

| Lagebeziehung | Bedingung | Schnittpunkte |
|---------------|-----------|---------------|
| **Parallel** | $m_1 = m_2$ und $n_1 \neq n_2$ | 0 |
| **Identisch** | $m_1 = m_2$ und $n_1 = n_2$ | unendlich viele |
| **Schneidend** | $m_1 \neq m_2$ | genau 1 |
| **Orthogonal** | $m_1 \cdot m_2 = -1$ | genau 1 |

### Schnittpunktberechnung

Für $m_1 \neq m_2$ ergibt sich der Schnittpunkt durch Gleichsetzen:

$$m_1 x + n_1 = m_2 x + n_2$$
$$x_S = \frac{n_2 - n_1}{m_1 - m_2}$$
$$y_S = m_1 \cdot x_S + n_1$$

**Beispiel:**
$g_1: y = 2x + 1$ und $g_2: y = -x + 7$
$$2x + 1 = -x + 7 \quad \Rightarrow \quad 3x = 6 \quad \Rightarrow \quad x_S = 2$$
$$y_S = 2 \cdot 2 + 1 = 5$$
Schnittpunkt: $S(2|5)$

## Lineare Funktionen aus Bedingungen aufstellen

### Typische Aufgabenstellungen

1. **Gerade durch zwei Punkte**: Steigung berechnen, dann Punkt-Steigungs-Form
2. **Punkt und Steigung gegeben**: Direkt Punkt-Steigungs-Form anwenden
3. **Parallele zu einer Geraden durch einen Punkt**: Steigung übernehmen
4. **Senkrechte zu einer Geraden durch einen Punkt**: Negative Kehrwert der Steigung

**Beispiel — Senkrechte:**
Gesucht ist die Senkrechte zu $g: y = 3x - 2$ durch $P(6|1)$.
$$m_g = 3 \quad \Rightarrow \quad m_{\perp} = -\frac{1}{3}$$
$$y - 1 = -\frac{1}{3}(x - 6) \quad \Rightarrow \quad y = -\frac{1}{3}x + 3$$

## Anwendungen

### Lineare Modellierung

Lineare Funktionen modellieren Zusammenhänge mit konstanter Änderungsrate:

- **Gleichförmige Bewegung**: $s(t) = v \cdot t + s_0$ (Weg-Zeit-Gesetz)
- **Lineare Kostenfunktion**: $K(x) = k \cdot x + K_f$ (variable + fixe Kosten)
- **Temperaturumrechnung**: $F = \frac{9}{5}C + 32$ (Celsius zu Fahrenheit)

### Lineare Regression (Ausblick)

Bei Messdaten mit annähernd linearem Zusammenhang bestimmt man eine Ausgleichsgerade nach der Methode der kleinsten Quadrate. Dies wird in [[15-Statistik-und-Hypothesentests|Modul 15]] vertieft.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-des-Funktionsbegriffs]] — Grundlegende Begriffe
- → [[Monotonie]] — Allgemeine Theorie der Monotonie
- → [[Nullstellen]] — Nullstellenberechnung bei verschiedenen Funktionstypen
- → [[Quadratische-Funktionen]] — Erweiterung auf Polynome zweiten Grades
- → [[Gleichungssysteme]] — Schnittprobleme mehrerer Geraden
- → [[Transformationen]] — Verschiebung und Streckung linearer Funktionen

> [!warning] **Prüfungsrelevant**
> - Die Umrechnung zwischen den verschiedenen Darstellungsformen muss sicher beherrscht werden
> - Orthogonalitätsbedingung $m_1 \cdot m_2 = -1$ für senkrechte Geraden
> - Aufstellen von Geradengleichungen aus zwei Punkten oder Punkt und Steigung
> - Schnittpunktberechnung durch Gleichsetzen der Funktionsgleichungen
> - Interpretation der Steigung als Änderungsrate in Anwendungskontexten

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Gleichung der Geraden durch die Punkte $A$ und $B$.
> - Zeigen Sie, dass die Geraden $g$ und $h$ orthogonal zueinander sind.
> - Eine Firma hat Fixkosten von 500€ und variable Kosten von 12€ pro Stück. Stellen Sie die Kostenfunktion auf und interpretieren Sie die Parameter.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2020
- ISB Bayern: *Lehrplan Mathematik Gymnasium*, 2023

> [!tip] **Weiterführende Links**
> - [[Polynomfunktionen]] — Verallgemeinerung auf höhere Grade
> - [[11-Analytische-Geometrie|Analytische Geometrie]] — Geraden im Raum

