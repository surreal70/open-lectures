---
title: "Quadratische Funktionen"
created: 2026-10-13
modified: 2026-10-19
chapter: "09"
section: "08"
status: "draft - review pending"
type: lecture
keywords:
  - Quadratische Funktion
  - Parabel
  - Scheitelpunkt
  - Normalform
  - Öffnung
---

# Quadratische Funktionen

> [!info] Lernziele
> - Quadratische Funktionen erkennen und beschreiben
> - Die verschiedenen Darstellungsformen kennen
> - Den Graphen (Parabel) skizzieren können
> - Den Einfluss der Parameter auf den Graphen verstehen

## Definition

Eine **quadratische Funktion** hat die allgemeine Form:

$$f(x) = ax^2 + bx + c \quad \text{mit } a \neq 0$$

| Parameter | Bedeutung |
|---|---|
| $a$ | Öffnungsfaktor (bestimmt Weite und Richtung) |
| $b$ | Beeinflusst die Lage der Parabel |
| $c$ | y-Achsenabschnitt |

> [!note] Merkmal
> Der Graph einer quadratischen Funktion ist eine **Parabel**. Der Name kommt vom griechischen *parabole* (Nebeneinanderwerfen, Gleichnis).

> [!info] **Warum sind quadratische Funktionen wichtig?**
> Quadratische Funktionen beschreiben viele Phänomene in Natur und Technik:
> - **Wurfbewegung**: Die Flugbahn eines geworfenen Balls ist eine Parabel
> - **Bremsweg**: Der Bremsweg eines Autos wächst quadratisch mit der Geschwindigkeit
> - **Flächen**: Die Fläche eines Quadrats mit Seitenlänge $x$ ist $x^2$
> - **Fallbewegung**: Die Höhe eines fallenden Objekts folgt einer quadratischen Funktion
> - **Parabolspiegel**: Satellitenschüsseln und Autoscheinwerfer nutzen die Parabelform
>
> Galileo Galilei entdeckte im 17. Jahrhundert, dass Kanonenkugeln Parabelbahnen fliegen – ein Durchbruch für die Ballistik!

## Die Normalparabel

Die einfachste quadratische Funktion ist:

$$f(x) = x^2$$

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $9$ | $4$ | $1$ | $0$ | $1$ | $4$ | $9$ |

![[normalparabel.png]]
*<span class="fig-id">01-09-08-normalparabel</span>: Die Normalparabel $f(x)=x^2$ – die Punkte aus der Wertetabelle bilden eine nach oben geöffnete, zur y-Achse symmetrische Kurve mit dem Scheitel im Ursprung.*

**Eigenschaften der Normalparabel**:
- Scheitelpunkt bei $(0, 0)$
- Achsensymmetrisch zur y-Achse
- Öffnung nach oben

> [!note] **Die Normalparabel als Bauplan**
> Die Normalparabel $f(x) = x^2$ ist die „Mutter" aller Parabeln: Jede andere quadratische Funktion entsteht aus ihr durch **Strecken/Stauchen** (Faktor $a$) und **Verschieben** (Scheitelpunktform). Wer die Normalparabel im Kopf hat, kann jede Parabel schnell skizzieren. Beachte auch die Werte in der Tabelle: Von einem ganzzahligen $x$ zum nächsten wachsen die Funktionswerte in den Sprüngen $1, 3, 5, 7, \dots$ – den ungeraden Zahlen. Dieses Muster ist typisch für quadratisches Wachstum.

## Der Öffnungsfaktor $a$

### Einfluss auf die Öffnungsrichtung

| Wert von $a$ | Öffnungsrichtung | Graph |
|---|---|---|
| $a > 0$ | Nach **oben** (Minimum) | ⌣ |
| $a < 0$ | Nach **unten** (Maximum) | ⌢ |

### Einfluss auf die Weite

| Wert von $\lvert a\rvert$ | Erscheinung |
|---|---|
| $\lvert a\rvert > 1$ | Schmaler als Normalparabel |
| $\lvert a\rvert = 1$ | Wie Normalparabel |
| $0 < \lvert a\rvert < 1$ | Weiter als Normalparabel |

![[oeffnungsfaktor.png]]
*<span class="fig-id">01-09-08-oeffnungsfaktor</span>: Einfluss des Öffnungsfaktors $a$ bei gleichem Scheitel – $a = 2$ ergibt eine schmale, $a = 1$ die Normalparabel und $a = 0{,}5$ eine weite Parabel. Je größer $|a|$, desto steiler steigen die Äste.*

Anschaulich **streckt** der Faktor $a$ die Parabel in y-Richtung: Jeder Funktionswert der Normalparabel wird mit $a$ multipliziert. Bei $a = 2$ erreicht die Parabel doppelt so schnell große Werte, wirkt also schmaler; bei $a = 0{,}5$ nur halb so schnell, wirkt also weiter. Ein **negatives** $a$ spiegelt die Parabel zusätzlich an der x-Achse – die Öffnung zeigt dann nach unten, und der Scheitel wird zum Hochpunkt (Maximum) statt zum Tiefpunkt.

## Formen der quadratischen Funktion

### 1. Allgemeine Form (Normalform)

$$f(x) = ax^2 + bx + c$$

- Leicht erkennbar: ist es eine quadratische Funktion?
- y-Achsenabschnitt direkt ablesbar: $c = f(0)$

### 2. Scheitelpunktform

$$f(x) = a(x - d)^2 + e$$

Scheitelpunkt: $S(d, e)$

Diese Form ist besonders praktisch, weil man an ihr den **Scheitelpunkt direkt ablesen** kann – ohne zu rechnen. $d$ verschiebt die Parabel waagerecht, $e$ senkrecht. Zum schnellen Skizzieren ist sie deshalb oft die beste Wahl: Scheitel einzeichnen, Öffnungsrichtung aus $a$ bestimmen, fertig.

> [!tip] Merkhilfe
> In der Klammer steht $(x - d)$, der Scheitelpunkt hat aber $x = d$ (nicht $-d$!).
>
> **Eselsbrücke**: Das Vorzeichen in der Klammer ist „umgedreht" – bei $(x - 3)^2$ liegt der Scheitelpunkt bei $x = +3$, bei $(x + 2)^2$ bei $x = -2$.

> [!warning] **Häufiger Fehler**
> Bei der Scheitelpunktform wird oft das Vorzeichen verwechselt. Merke: $(x - d)^2$ bedeutet, der Scheitelpunkt liegt bei $x = d$. Das Minus in der Klammer „dreht" das Vorzeichen um!

### 3. Faktorisierte Form (Nullstellenform)

$$f(x) = a(x - x_1)(x - x_2)$$

Nullstellen: $x_1$ und $x_2$

## Umrechnung zwischen den Formen

### Von Scheitelpunktform zu Normalform

$$f(x) = a(x - d)^2 + e$$

Ausmultiplizieren:
$$f(x) = a(x^2 - 2dx + d^2) + e$$
$$f(x) = ax^2 - 2adx + ad^2 + e$$

> [!example] Beispiel
> $f(x) = 2(x - 3)^2 + 1$
> 
> $= 2(x^2 - 6x + 9) + 1$
> $= 2x^2 - 12x + 18 + 1$
> $= 2x^2 - 12x + 19$

### Von Normalform zu Scheitelpunktform

Die Koordinaten des Scheitelpunkts:

$$x_S = -\frac{b}{2a}$$
$$y_S = f(x_S) = c - \frac{b^2}{4a}$$

> [!example] Beispiel
> $f(x) = x^2 - 4x + 7$
> 
> $x_S = -\frac{-4}{2 \cdot 1} = 2$
> 
> $y_S = 7 - \frac{(-4)^2}{4 \cdot 1} = 7 - 4 = 3$
> 
> Scheitelpunkt: $S(2, 3)$
> 
> Scheitelpunktform: $f(x) = (x - 2)^2 + 3$

## Wichtige Eigenschaften einer Parabel

| Eigenschaft | Berechnung/Ablesen |
|---|---|
| Scheitelpunkt | $S\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)$ |
| Symmetrieachse | $x = -\frac{b}{2a}$ |
| y-Achsenabschnitt | $f(0) = c$ |
| Nullstellen | $f(x) = 0$ lösen (p-q-Formel) |
| Öffnungsrichtung | Vorzeichen von $a$ |

## Nullstellen

Die **Nullstellen** einer quadratischen Funktion $f(x) = ax^2 + bx + c$ sind die Lösungen von $f(x) = 0$.

Mit der p-q-Formel (nach Division durch $a$):

$$x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}$$

| Diskriminante $D$ | Anzahl Nullstellen |
|---|---|
| $D > 0$ | 2 verschiedene |
| $D = 0$ | 1 (Doppelnullstelle = Scheitelpunkt auf x-Achse) |
| $D < 0$ | keine reellen |

Grafisch bedeutet das einfach, **wie oft die Parabel die x-Achse trifft**: Bei zwei Nullstellen durchstößt sie die Achse an zwei Stellen, bei einer Doppelnullstelle berührt sie die Achse nur im Scheitel, und bei keiner reellen Nullstelle liegt die ganze Parabel vollständig über oder unter der x-Achse. Du kannst die Anzahl der Nullstellen also schon an einer Skizze abschätzen, bevor du rechnest.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Quadratische Funktion: $f(x) = ax^2 + bx + c$ mit $a \neq 0$
> - Der Graph ist eine Parabel
> - $a > 0$: Öffnung nach oben; $a < 0$: nach unten
> - $|a|$ bestimmt die Weite der Parabel
> - Scheitelpunktform: $f(x) = a(x - d)^2 + e$ mit $S(d, e)$
> - Scheitelpunkt: $x_S = -\frac{b}{2a}$

## Zusammenhänge

Quadratische Funktionen sind eng verbunden mit:

- → [[09-Parabeln|Parabeln]] – Detaillierte Analyse von Parabeleigenschaften
- → [[10-Schnittpunkte|Schnittpunkte]] – Schnittpunkte quadratischer Funktionen
- → [[../08-Gleichungen-und-Ungleichungen/08-Quadratische-Gleichungen|Quadratische Gleichungen]] – Nullstellen berechnen
- → [[11-Anwendungen-Funktionen|Anwendungen]] – Wurfparabeln und Optimierung
- → [[../07-Terme-und-algebraische-Ausdruecke/08-Binomische-Formeln|Binomische Formeln]] – Wichtig für die Scheitelpunktform

## Übungsaufgaben

1. Bestimme die Öffnungsrichtung und vergleiche mit der Normalparabel:
   - $f(x) = 3x^2$
   - $g(x) = -x^2$
   - $h(x) = \frac{1}{4}x^2$

2. Forme in Normalform um:
   - $f(x) = (x - 2)^2 + 5$
   - $g(x) = -2(x + 1)^2 - 3$

3. Bestimme den Scheitelpunkt:
   - $f(x) = x^2 - 6x + 5$
   - $g(x) = 2x^2 + 8x + 10$

4. Bestimme die Nullstellen:
   - $f(x) = x^2 - 4$
   - $g(x) = x^2 - 6x + 9$
   - $h(x) = x^2 + 4$

---

**Navigation**: [[07-Geradengleichungen|← Geradengleichungen]] | [[00-Funktionen-Index|Übersicht]] | [[09-Parabeln|Parabeln →]]
