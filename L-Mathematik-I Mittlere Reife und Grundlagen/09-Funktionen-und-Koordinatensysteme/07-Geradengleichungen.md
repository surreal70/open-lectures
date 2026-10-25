---
title: "Geradengleichungen aufstellen"
created: 2026-10-13
modified: 2026-10-25
chapter: "09"
section: "07"
status: final
type: lecture
keywords:
  - Geradengleichung
  - Punkt-Steigung-Form
  - Zwei-Punkte-Form
  - Normalform
---

# Geradengleichungen aufstellen

> [!info] Lernziele
> - Geradengleichungen aus verschiedenen Angaben aufstellen
> - Die Punkt-Steigung-Form anwenden können
> - Die Zwei-Punkte-Form beherrschen
> - Zwischen verschiedenen Darstellungsformen umwandeln

## Warum verschiedene Methoden?

In der Praxis haben wir oft unterschiedliche Informationen über eine Gerade:
- Manchmal kennen wir zwei Punkte, durch die sie verläuft
- Manchmal wissen wir, wo sie die y-Achse schneidet und wie steil sie ist
- Manchmal ist eine parallele Gerade bekannt und ein Punkt

Für jede Situation gibt es die passende Methode. Das Ziel ist immer dasselbe: die Gleichung $y = mx + b$ (oder eine andere Form) zu finden.

## Formen der Geradengleichung

Jede Gerade lässt sich auf verschiedene Weisen darstellen. Diese Formen sind äquivalent – sie beschreiben dieselbe Gerade, betonen aber unterschiedliche Aspekte.

### Normalform (Hauptform)

$$y = mx + b$$

oder als Funktion:

$$f(x) = mx + b$$

### Allgemeine Form (implizite Form)

$$ax + by + c = 0$$

### Punkt-Steigung-Form

$$y - y_1 = m(x - x_1)$$

wobei $P(x_1, y_1)$ ein Punkt auf der Geraden ist.

Diese Form ergibt sich direkt aus der Definition der Steigung: Für jeden weiteren Punkt $(x, y)$ auf der Geraden muss das Steigungsdreieck zum Punkt $P$ denselben Wert $m$ liefern, also $\frac{y - y_1}{x - x_1} = m$. Multipliziert man mit $(x - x_1)$, erhält man die Punkt-Steigung-Form. Ihr Vorteil: Man kann sie **sofort hinschreiben**, sobald ein Punkt und die Steigung bekannt sind – ohne erst $b$ auszurechnen.

## Methode 1: Aus Steigung und y-Achsenabschnitt

**Gegeben**: Steigung $m$ und y-Achsenabschnitt $b$

**Lösung**: Direkt einsetzen in $y = mx + b$

> [!example] Beispiel
> $m = 3$, $b = -2$
> 
> $$y = 3x - 2$$

## Methode 2: Aus Steigung und einem Punkt

**Gegeben**: Steigung $m$ und Punkt $P(x_1, y_1)$

**Vorgehen**:
1. In Punkt-Steigung-Form einsetzen
2. Nach $y$ auflösen

$$y - y_1 = m(x - x_1)$$
$$y = m(x - x_1) + y_1$$
$$y = mx - mx_1 + y_1$$
$$y = mx + (y_1 - mx_1)$$

> [!example] Beispiel
> $m = 2$ und $P(3, 5)$
> 
> $$y - 5 = 2(x - 3)$$
> $$y = 2x - 6 + 5$$
> $$y = 2x - 1$$

### Alternative: b direkt berechnen

$$b = y_1 - mx_1 = 5 - 2 \cdot 3 = -1$$

Also: $y = 2x - 1$

## Methode 3: Aus zwei Punkten

**Gegeben**: Zwei Punkte $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$

**Vorgehen**:
1. Steigung berechnen: $m = \frac{y_2 - y_1}{x_2 - x_1}$
2. Einen Punkt einsetzen und $b$ berechnen
3. Gleichung aufstellen

> [!example] Beispiel
> $P_1(1, 4)$ und $P_2(5, 12)$
> 
> **Schritt 1**: Steigung
> $$m = \frac{12 - 4}{5 - 1} = \frac{8}{4} = 2$$
> 
> **Schritt 2**: y-Achsenabschnitt (mit $P_1$)
> $$4 = 2 \cdot 1 + b$$
> $$b = 2$$
> 
> **Schritt 3**: Gleichung
> $$y = 2x + 2$$
> 
> **Probe** (mit $P_2$): $2 \cdot 5 + 2 = 12$ ✓

### Zwei-Punkte-Form (Formel)

$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$$

Diese Formel liefert direkt die Geradengleichung.

## Methode 4: Parallele Gerade durch einen Punkt

**Gegeben**: Gerade $g: y = mx + b_1$ und Punkt $P(x_1, y_1)$

**Gesucht**: Gerade $h$ durch $P$, parallel zu $g$

**Vorgehen**:
- Parallele Geraden haben **gleiche Steigung**: $m_h = m_g$
- Neue Gerade mit Methode 2 bestimmen

Anschaulich leuchtet das ein: Zwei Geraden verlaufen genau dann in dieselbe Richtung (sind parallel), wenn sie **gleich stark geneigt** sind. Nur der y-Achsenabschnitt $b$ unterscheidet sie – er verschiebt die Gerade nach oben oder unten, ohne ihre Richtung zu ändern.

> [!example] Beispiel
> $g: y = 3x - 1$, Punkt $P(2, 4)$
> 
> Steigung: $m = 3$
> 
> $b = 4 - 3 \cdot 2 = -2$
> 
> $h: y = 3x - 2$

## Methode 5: Senkrechte Gerade durch einen Punkt

**Gegeben**: Gerade $g: y = mx + b_1$ und Punkt $P(x_1, y_1)$

**Gesucht**: Gerade $h$ durch $P$, senkrecht zu $g$

**Vorgehen**:
- Senkrechte Geraden: $m_h = -\frac{1}{m_g}$ (negative Kehrwert)
- Neue Gerade mit Methode 2 bestimmen

> [!info] **Warum der negative Kehrwert?**
> Wenn zwei Geraden senkrecht aufeinander stehen, gilt für ihre Steigungen: $m_1 \cdot m_2 = -1$. Das bedeutet: Die Steigung der senkrechten Geraden ist der **negative Kehrwert** der Originalsteigung. Bei $m_g = 2$ ist also $m_h = -\frac{1}{2}$.

> [!example] Beispiel
> $g: y = 2x + 1$, Punkt $P(4, 3)$
> 
> Steigung von $g$: $m_g = 2$
> 
> Steigung der Senkrechten: $m_h = -\frac{1}{2}$
> 
> $b = 3 - (-\frac{1}{2}) \cdot 4 = 3 + 2 = 5$
> 
> $h: y = -\frac{1}{2}x + 5$

> [!warning] **Häufiger Fehler**
> Beim negativen Kehrwert wird oft nur der Kehrwert gebildet und das Minuszeichen vergessen. Bei $m = 3$ ist der negative Kehrwert $-\frac{1}{3}$, nicht $\frac{1}{3}$!

![[parallel-senkrecht.png]]
*<span class="fig-id">01-09-07-parallel-senkrecht</span>: Links verlaufen zwei parallele Geraden mit gleicher Steigung ($m_1 = m_2$), nur ihr y-Achsenabschnitt unterscheidet sich. Rechts stehen zwei Geraden senkrecht aufeinander – ihre Steigungen sind negative Kehrwerte ($m_2 = -\frac{1}{m_1}$), erkennbar am rechten Winkel im Schnittpunkt.*

## Übersicht: Was ist gegeben?

| Gegeben | Methode |
|---|---|
| $m$ und $b$ | Direkt einsetzen |
| $m$ und ein Punkt | Punkt-Steigung-Form |
| Zwei Punkte | Erst $m$, dann $b$ berechnen |
| Parallele + Punkt | $m$ übernehmen, $b$ berechnen |
| Senkrechte + Punkt | $m = -\frac{1}{m_g}$, dann $b$ berechnen |

## Umwandlung zwischen Formen

### Von allgemeiner Form zu Normalform

$$ax + by + c = 0 \quad \Rightarrow \quad y = -\frac{a}{b}x - \frac{c}{b}$$

> [!example] Beispiel
> $3x - 2y + 4 = 0$
> 
> $-2y = -3x - 4$
> $y = \frac{3}{2}x + 2$

### Von Normalform zu allgemeiner Form

$$y = mx + b \quad \Rightarrow \quad mx - y + b = 0$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Normalform: $y = mx + b$
> - Punkt-Steigung-Form: $y - y_1 = m(x - x_1)$
> - Aus zwei Punkten: erst Steigung, dann y-Achsenabschnitt
> - Parallele Geraden: gleiche Steigung
> - Senkrechte Geraden: Steigungen sind negative Kehrwerte

## Zusammenhänge

- → [[05-Lineare-Funktionen|Lineare Funktionen]] – Die Grundlagen
- → [[06-Steigung-und-Achsenabschnitt|Steigung und Achsenabschnitt]] – Die Parameter im Detail
- → [[10-Schnittpunkte|Schnittpunkte]] – Wo sich Geraden treffen
- → [[../10-Grundlagen-der-Geometrie/01-Punkte-Strecken-Geraden|Geometrie: Geraden]] – Geometrische Perspektive

> [!tip] **Praxis-Tipp: Probe machen**
> Setze nach dem Aufstellen der Gleichung die gegebenen Punkte ein. Wenn die Gleichung stimmt, müssen beide Punkte sie erfüllen. Das ist eine schnelle Kontrolle gegen Rechenfehler!

## Übungsaufgaben

1. Stelle die Geradengleichung auf:
   - Durch $(0, -3)$ mit $m = 4$
   - Durch $(2, 5)$ mit $m = -1$
   - Durch $(-1, 2)$ und $(3, 10)$
   - Durch $(4, 1)$ und $(4, 7)$ – was ist hier anders?

2. Bestimme die Gleichung der Geraden parallel zu $y = -2x + 3$ durch $(1, 4)$.

3. Bestimme die Gleichung der Geraden senkrecht zu $y = \frac{1}{3}x - 2$ durch $(6, 1)$.

4. Wandle in Normalform um: $4x - 2y - 6 = 0$

5. Eine Gerade geht durch $A(1, 2)$ und $B(4, 8)$. Wo schneidet sie die y-Achse? Wo die x-Achse?

---

**Navigation**: [[06-Steigung-und-Achsenabschnitt|← Steigung]] | [[00-Funktionen-Index|Übersicht]] | [[08-Quadratische-Funktionen|Quadratische Funktionen →]]
