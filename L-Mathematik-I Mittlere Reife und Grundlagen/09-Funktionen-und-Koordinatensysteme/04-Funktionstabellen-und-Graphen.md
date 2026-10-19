---
title: "Funktionstabellen und graphische Darstellung"
created: 2026-10-13
modified: 2026-10-19
chapter: "09"
section: "04"
status: "draft - review pending"
type: lecture
keywords:
  - Wertetabelle
  - Graph
  - Zeichnen
  - Ablesen
  - Kurvendiskussion
---

# Funktionstabellen und graphische Darstellung

> [!info] Lernziele
> - Wertetabellen systematisch erstellen können
> - Funktionsgraphen aus Wertetabellen zeichnen
> - Eigenschaften aus Graphen ablesen können
> - Den Zusammenhang zwischen Gleichung und Graph verstehen

## Wertetabellen erstellen

### Grundprinzip

Eine **Wertetabelle** zeigt Paare von Eingabe- und Ausgabewerten. Sie ist wie ein „Fahrplan" für die Funktion: Für jeden gewählten x-Wert wird der zugehörige Funktionswert berechnet.

| $x$ | Berechnung | $f(x)$ |
|---|---|---|
| gewählt | Formel anwenden | Ergebnis |

> [!info] **Historischer Hintergrund**
> Vor der Erfindung des Taschenrechners waren Wertetabellen von enormer praktischer Bedeutung. Wissenschaftler wie Johannes Kepler verbrachten Jahre damit, umfangreiche Logarithmentafeln zu berechnen. Diese Tabellen waren so wertvoll, dass sie in speziellen Büchern veröffentlicht wurden, die Generationen von Ingenieuren und Wissenschaftlern dienten.

### Schritt-für-Schritt

**Beispiel**: $f(x) = 2x - 1$

1. **x-Werte wählen**: sinnvoller Bereich, oft symmetrisch um 0
2. **Funktionswerte berechnen**: $f(x)$ für jeden x-Wert
3. **Tabelle ausfüllen**

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|
| $f(x)$ | $-5$ | $-3$ | $-1$ | $1$ | $3$ | $5$ |

**Rechenweg für $x = -2$**:
$$f(-2) = 2 \cdot (-2) - 1 = -4 - 1 = -5$$

## Graphen zeichnen

### Vorgehensweise

```mermaid
graph TD
    A[Wertetabelle erstellen] --> B[Koordinatensystem zeichnen<br/>passende Skalierung wählen]
    B --> C[Punkte einzeichnen]
    C --> D[Punkte verbinden<br/>Gerade bei linearen Funktionen,<br/>Kurve bei anderen]
    D --> E[Graph beschriften]
```

### Beispiel: Linearer Graph

$f(x) = \frac{1}{2}x + 1$

| $x$ | $-4$ | $-2$ | $0$ | $2$ | $4$ |
|---|---|---|---|---|---|
| $f(x)$ | $-1$ | $0$ | $1$ | $2$ | $3$ |

![[graph-linear.png]]
*<span class="fig-id">01-09-04-graph-linear</span>: Graph der linearen Funktion $f(x)=\frac{1}{2}x+1$ – die Punkte aus der Wertetabelle liegen auf einer Geraden, die mit dem Lineal verbunden wird.*

### Beispiel: Quadratischer Graph (Parabel)

$f(x) = x^2 - 2$

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|---|
| $f(x)$ | $2$ | $-1$ | $-2$ | $-1$ | $2$ |

![[graph-parabel.png]]
*<span class="fig-id">01-09-04-graph-parabel</span>: Graph der quadratischen Funktion $f(x)=x^2-2$ – die Punkte aus der Wertetabelle werden zu einer nach oben geöffneten Parabel mit Scheitel bei $(0, -2)$ verbunden.*

## Eigenschaften aus Graphen ablesen

### Nullstellen

**Nullstellen** sind die x-Werte, an denen der Graph die **x-Achse schneidet**.

$$f(x) = 0$$

### Schnittpunkt mit der y-Achse

Der **y-Achsenabschnitt** ist der Punkt, an dem der Graph die **y-Achse schneidet**.

$$f(0) = ?$$

### Steigungsverhalten

| Verlauf | Bedeutung |
|---|---|
| Graph steigt (von links nach rechts) | $f$ ist monoton steigend |
| Graph fällt | $f$ ist monoton fallend |
| Graph hat Maximum/Minimum | Lokale Extremstelle |

### Symmetrie

| Symmetrieart | Eigenschaft | Beispiel |
|---|---|---|
| Achsensymmetrisch zur y-Achse | $f(-x) = f(x)$ | $f(x) = x^2$ |
| Punktsymmetrisch zum Ursprung | $f(-x) = -f(x)$ | $f(x) = x^3$ |

## Werte aus Graphen ablesen

### Funktionswert ablesen

**Aufgabe**: Bestimme $f(2)$ aus dem Graphen.

1. Auf der x-Achse den Wert 2 suchen
2. Senkrecht nach oben/unten zum Graphen gehen
3. Waagerecht zur y-Achse gehen
4. y-Wert ablesen

### x-Wert zu gegebenem y-Wert finden

**Aufgabe**: Für welche x gilt $f(x) = 3$?

1. Auf der y-Achse den Wert 3 suchen
2. Waagerecht zum Graphen gehen
3. Senkrecht zur x-Achse gehen
4. x-Wert(e) ablesen

> [!note] Mehrere Lösungen möglich
> Bei nicht-linearen Funktionen kann ein y-Wert zu mehreren x-Werten gehören.

## Skalierung und Darstellung

### Tipps für gute Zeichnungen

> [!tip] Praktische Hinweise
> - **Ausreichend Punkte**: Bei Geraden reichen 2-3, bei Kurven mehr
> - **Charakteristische Punkte**: Nullstellen, Extrema, Wendepunkte einbeziehen
> - **Passende Skalierung**: Alle wichtigen Punkte sollen sichtbar sein
> - **Gleichmäßige Abstände**: x-Werte mit gleichen Abständen wählen

### Häufige Fehler

> [!warning] **Zu vermeiden**
> - Punkte mit Lineal bei Kurven verbinden (nur bei Geraden!)
> - Zu wenige Punkte berechnen
> - Punkte falsch einzeichnen (x und y vertauscht)
> - Graph über den sinnvollen Bereich hinaus zeichnen
> - Bei negativen x-Werten die Vorzeichen beim Einsetzen vergessen

> [!tip] **Kontrolle durch Probe**
> Prüfe nach dem Zeichnen: Liegt ein einfach zu berechnender Punkt (z.B. $x = 0$ oder $x = 1$) tatsächlich auf deinem Graphen? Das hilft, Flüchtigkeitsfehler zu entdecken.

## Graphen im Alltag

Funktionsgraphen begegnen uns überall:

| Kontext | x-Achse | y-Achse |
|---|---|---|
| Aktienkurs | Zeit | Preis in € |
| Fieberkurve | Zeit | Temperatur in °C |
| Tacho im Auto | Zeit | Geschwindigkeit in km/h |
| Klimadiagramm | Monat | Temperatur / Niederschlag |
| Fitness-Tracker | Tag | Schritte |

Die Fähigkeit, Graphen zu lesen und zu interpretieren, ist eine wichtige Kompetenz in vielen Lebensbereichen – von der Zeitung bis zum Arztbesuch.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Wertetabellen: x-Werte wählen, f(x) berechnen, Tabelle füllen
> - Graphen zeichnen: Punkte einzeichnen, sinnvoll verbinden
> - Aus Graphen ablesen: Nullstellen, y-Abschnitt, Steigung
> - Lineare Funktionen: Gerade; quadratische: Parabel
> - Die Skalierung dem Problem anpassen

## Zusammenhänge

- → [[03-Einfuehrung-Funktionen|Einführung Funktionen]] – Grundbegriffe des Funktionsbegriffs
- → [[05-Lineare-Funktionen|Lineare Funktionen]] – Graphen als Geraden
- → [[08-Quadratische-Funktionen|Quadratische Funktionen]] – Graphen als Parabeln
- → [[10-Schnittpunkte|Schnittpunkte]] – Ablesen und Berechnen von Schnittpunkten

## Übungsaufgaben

1. Erstelle eine Wertetabelle und zeichne den Graphen:
   - $f(x) = -x + 3$ für $x \in \{-2, -1, 0, 1, 2, 3, 4\}$
   - $g(x) = x^2 - 4$ für $x \in \{-3, -2, -1, 0, 1, 2, 3\}$

2. Lies aus dem Graphen von $f(x) = x^2 - 1$ ab:
   - Die Nullstellen
   - Den y-Achsenabschnitt
   - $f(1{,}5)$
   - Alle $x$ mit $f(x) = 3$

3. Skizziere ohne Rechnung den Graphen von:
   - $f(x) = 2x$
   - $g(x) = -x^2$
   - $h(x) = |x|$

---

**Navigation**: [[03-Einfuehrung-Funktionen|← Einführung]] | [[00-Funktionen-Index|Übersicht]] | [[05-Lineare-Funktionen|Lineare Funktionen →]]
