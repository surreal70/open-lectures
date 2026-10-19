---
title: "Schnittpunkte berechnen"
created: 2026-10-13
modified: 2026-10-19
chapter: "09"
section: "10"
status: "draft - review pending"
type: lecture
keywords:
  - Schnittpunkt
  - Nullstelle
  - Gleichsetzen
  - Schnitt zweier Graphen
---

# Schnittpunkte berechnen

> [!info] Lernziele
> - Schnittpunkte mit den Koordinatenachsen berechnen
> - Schnittpunkte zweier Funktionen bestimmen
> - Das Gleichsetzungsverfahren sicher anwenden
> - Ergebnisse grafisch interpretieren

## Warum Schnittpunkte wichtig sind

Schnittpunkte beantworten praktische Fragen:
- **Wann sind die Kosten gedeckt?** (Schnittpunkt von Kosten- und Erlösfunktion = Break-Even)
- **Wann überholt Auto A das Auto B?** (Schnittpunkt der Weg-Zeit-Funktionen)
- **Wo trifft ein geworfener Ball den Boden?** (Schnittpunkt der Wurfparabel mit der x-Achse)
- **Bei welchem Preis sind Angebot und Nachfrage gleich?** (Marktgleichgewicht)

Die Berechnung von Schnittpunkten ist daher eine der wichtigsten praktischen Anwendungen von Funktionen.

## Schnittpunkt mit der y-Achse

Der Schnittpunkt mit der y-Achse liegt bei $x = 0$.

$$S_y = (0, f(0))$$

> [!example] Beispiel
> $f(x) = 2x^2 - 3x + 5$
> 
> $f(0) = 2 \cdot 0 - 3 \cdot 0 + 5 = 5$
> 
> Schnittpunkt: $S_y(0, 5)$

> [!tip] Merkregel
> Bei $f(x) = ax^2 + bx + c$ ist der y-Achsenabschnitt direkt $c$.
> Bei $f(x) = mx + b$ ist er $b$.

## Schnittpunkte mit der x-Achse (Nullstellen)

Die Schnittpunkte mit der x-Achse sind die **Nullstellen** der Funktion.

$$f(x) = 0$$

### Lineare Funktion

$$mx + b = 0$$
$$x = -\frac{b}{m}$$

> [!example] Beispiel
> $f(x) = 3x - 6$
> 
> $3x - 6 = 0$
> $x = 2$
> 
> Nullstelle: $N(2, 0)$

### Quadratische Funktion

$$ax^2 + bx + c = 0$$

Lösung mit p-q-Formel oder Mitternachtsformel.

> [!example] Beispiel
> $f(x) = x^2 - 5x + 6$
> 
> $x^2 - 5x + 6 = 0$
> 
> $x_{1,2} = \frac{5}{2} \pm \sqrt{\frac{25}{4} - 6} = \frac{5}{2} \pm \frac{1}{2}$
> 
> $x_1 = 3$, $x_2 = 2$
> 
> Nullstellen: $N_1(2, 0)$ und $N_2(3, 0)$

## Schnittpunkt zweier Funktionen

### Prinzip: Gleichsetzen

Am Schnittpunkt haben beide Funktionen denselben y-Wert:

$$f(x) = g(x)$$

Die Lösung $x$ wird in eine der Funktionen eingesetzt, um $y$ zu berechnen.

Warum funktioniert das? Ein Schnittpunkt ist genau der Ort, an dem **beide Graphen durch denselben Punkt** laufen – dort stimmen also sowohl die x- als auch die y-Koordinate überein. Setzt man $f(x) = g(x)$, sucht man genau die x-Werte, bei denen beide Funktionen denselben Funktionswert liefern. Die Gleichsetzung übersetzt die geometrische Frage „Wo treffen sich die Graphen?" in eine lösbare Gleichung.

> [!tip] **In welche Funktion einsetzen?**
> Für die y-Koordinate darfst du den gefundenen x-Wert in $f$ **oder** $g$ einsetzen – beide liefern denselben Wert (das ist ja gerade die Bedingung am Schnittpunkt). Wähle einfach die Funktion, mit der sich leichter rechnen lässt. Setzt du in beide ein und erhältst verschiedene Werte, war die Rechnung fehlerhaft.

### Schnittpunkt zweier Geraden

> [!example] Beispiel
> $f(x) = 2x + 1$ und $g(x) = -x + 7$
> 
> **Gleichsetzen**:
> $$2x + 1 = -x + 7$$
> $$3x = 6$$
> $$x = 2$$
> 
> **y-Koordinate**:
> $$y = f(2) = 2 \cdot 2 + 1 = 5$$
> 
> **Schnittpunkt**: $S(2, 5)$

### Schnittpunkt Gerade und Parabel

> [!example] Beispiel
> $f(x) = x^2$ und $g(x) = x + 2$
> 
> **Gleichsetzen**:
> $$x^2 = x + 2$$
> $$x^2 - x - 2 = 0$$
> 
> **p-q-Formel**:
> $$x_{1,2} = \frac{1}{2} \pm \sqrt{\frac{1}{4} + 2} = \frac{1}{2} \pm \frac{3}{2}$$
> 
> $x_1 = 2$, $x_2 = -1$
> 
> **y-Koordinaten**:
> - $y_1 = f(2) = 4$ → $S_1(2, 4)$
> - $y_2 = f(-1) = 1$ → $S_2(-1, 1)$

### Schnittpunkt zweier Parabeln

> [!example] Beispiel
> $f(x) = x^2 + 2x$ und $g(x) = -x^2 + 4$
> 
> **Gleichsetzen**:
> $$x^2 + 2x = -x^2 + 4$$
> $$2x^2 + 2x - 4 = 0$$
> $$x^2 + x - 2 = 0$$
> 
> **Lösung**: $x_1 = 1$, $x_2 = -2$
> 
> **Schnittpunkte**: $S_1(1, 3)$ und $S_2(-2, 0)$

## Anzahl der Schnittpunkte

### Gerade und Gerade

| Situation | Anzahl Schnittpunkte |
|---|---|
| Verschiedene Steigungen | genau 1 |
| Gleiche Steigung, verschiedene y-Achsenabschnitte | 0 (parallel) |
| Gleiche Steigung und y-Achsenabschnitt | unendlich (identisch) |

### Gerade und Parabel

| Diskriminante | Anzahl Schnittpunkte |
|---|---|
| $D > 0$ | 2 (Sekante) |
| $D = 0$ | 1 (Tangente) |
| $D < 0$ | 0 (Passante) |

> [!info] **Geometrische Bedeutung**
> - Eine **Sekante** schneidet die Parabel in zwei Punkten – wie ein Messer durch einen Apfel
> - Eine **Tangente** berührt die Parabel in genau einem Punkt – sie „streift" die Kurve
> - Eine **Passante** verfehlt die Parabel komplett – sie „geht vorbei"
>
> Diese Begriffe stammen aus dem Lateinischen: *secare* (schneiden), *tangere* (berühren), *passare* (vorbeigehen).

![[sekante-tangente-passante.png]]
*<span class="fig-id">01-09-10-sekante-tangente-passante</span>: Eine Gerade kann eine Parabel in zwei Punkten schneiden (Sekante), in einem Punkt berühren (Tangente) oder ganz verfehlen (Passante). Welcher Fall vorliegt, entscheidet die Diskriminante der Gleichsetzung.*

> [!warning] **Häufiger Fehler**
> Beim Berechnen von Schnittpunkten vergessen viele, die gefundenen x-Werte auch noch in eine der Funktionen einzusetzen, um die y-Koordinate zu erhalten. Ein Schnittpunkt besteht aus **zwei** Koordinaten!

## Grafische Interpretation

### Schnittpunkte ablesen

1. Beide Graphen in dasselbe Koordinatensystem zeichnen
2. Schnittpunkte identifizieren
3. Koordinaten ablesen

### Prüfung durch Einsetzen

Berechnete Schnittpunkte in **beide** Funktionen einsetzen – die y-Werte müssen übereinstimmen.

## Zusammenfassung

> [!abstract] Kernpunkte
> - y-Achse: $f(0)$ berechnen
> - x-Achse: $f(x) = 0$ lösen (Nullstellen)
> - Zwei Funktionen: $f(x) = g(x)$ lösen (Gleichsetzen)
> - x-Wert in eine Funktion einsetzen für y-Wert
> - Anzahl der Schnittpunkte hängt vom Funktionstyp und der Diskriminante ab

## Zusammenhänge

- → [[05-Lineare-Funktionen|Lineare Funktionen]] – Schnittpunkte von Geraden
- → [[08-Quadratische-Funktionen|Quadratische Funktionen]] – Schnittpunkte mit Parabeln
- → [[../08-Gleichungen-und-Ungleichungen/04-Lineare-Gleichungen|Lineare Gleichungen]] – Lösen der Gleichsetzung
- → [[../08-Gleichungen-und-Ungleichungen/08-Quadratische-Gleichungen|Quadratische Gleichungen]] – Nullstellen von Parabeln
- → [[11-Anwendungen-Funktionen|Anwendungen]] – Break-Even-Analysen und mehr

> [!tip] **Praxis-Tipp: Grafische Kontrolle**
> Skizziere die Funktionen grob, bevor du rechnest. So siehst du sofort, wie viele Schnittpunkte zu erwarten sind – und ob deine berechneten Werte plausibel sind.

## Übungsaufgaben

1. Bestimme die Schnittpunkte mit den Koordinatenachsen:
   - $f(x) = 4x - 8$
   - $g(x) = x^2 - 9$
   - $h(x) = x^2 - 4x + 4$

2. Berechne den Schnittpunkt der Geraden:
   - $f(x) = 3x - 2$ und $g(x) = x + 4$

3. Berechne die Schnittpunkte:
   - $f(x) = x^2$ und $g(x) = 2x + 3$
   - $f(x) = x^2 - 2$ und $g(x) = x$

4. Zeige, dass die Gerade $g(x) = 2x + 5$ eine Tangente an die Parabel $f(x) = x^2 + 4x + 4$ ist.

5. Für welchen Wert von $c$ berührt die Gerade $g(x) = 2x + c$ die Parabel $f(x) = x^2$?

---

**Navigation**: [[09-Parabeln|← Parabeln]] | [[00-Funktionen-Index|Übersicht]] | [[11-Anwendungen-Funktionen|Anwendungen →]]
