---
title: "Parabeln und ihre Eigenschaften"
created: 2026-10-13
modified: 2026-10-25
chapter: "09"
section: "09"
status: final
type: lecture
keywords:
  - Parabel
  - Scheitelpunkt
  - Symmetrieachse
  - Verschiebung
  - Streckung
---

# Parabeln und ihre Eigenschaften

> [!info] Lernziele
> - Parabeln systematisch analysieren können
> - Verschiebungen und Streckungen verstehen
> - Aus dem Graphen die Funktionsgleichung ableiten
> - Parabeln skizzieren können

## Die Parabel in Alltag und Technik

Die Parabelform begegnet uns überall – oft ohne dass wir es bemerken:

- **Satellitenschüsseln**: Die Parabelform bündelt eintreffende Signale im Brennpunkt
- **Autoscheinwerfer**: Eine Lampe im Brennpunkt erzeugt parallele Lichtstrahlen
- **Hängebrücken**: Die Kabel hängen in einer Form, die der Parabel sehr ähnelt
- **Springbrunnen**: Wasserstrahlen beschreiben Parabelbahnen
- **Basketball-Wurf**: Der Ball fliegt auf einer Parabelbahn zum Korb

> [!info] **Die Physik dahinter**
> Die Parabel hat eine besondere physikalische Eigenschaft: Alle parallel zur Achse eintreffenden Strahlen werden im **Brennpunkt** (Fokus) gebündelt. Diese Eigenschaft nutzen Parabolantennen, Spiegel in Teleskopen und Solaröfen. Umgekehrt gilt dasselbe: Eine Lichtquelle im Brennpunkt erzeugt ein paralleles Strahlenbündel – genau so funktionieren Autoscheinwerfer und Taschenlampen. Diese Bündelung funktioniert *nur* bei der Parabelform exakt, nicht bei einer beliebig gekrümmten Schale.

> [!tip] **Eine Transformation genügt zum Skizzieren**
> Alle Parabeln dieses Kapitels entstehen aus derselben Normalparabel $x^2$ durch Verschieben (Parameter $d$, $e$) und Strecken/Spiegeln (Parameter $a$). Wenn du diese drei Bausteine beherrschst, kannst du jede Parabel skizzieren, ohne eine einzige Wertetabelle zu rechnen – Scheitel setzen, Öffnung und Weite aus $a$ ablesen, fertig.

## Verschiebungen der Normalparabel

### Vertikale Verschiebung

$$f(x) = x^2 + e$$

Die Parabel wird um $e$ Einheiten **nach oben** (wenn $e > 0$) oder **nach unten** (wenn $e < 0$) verschoben.

![[parabel-vertikal.png]]
*<span class="fig-id">01-09-09-parabel-vertikal</span>: Vertikale Verschiebung der Normalparabel – $x^2+2$ liegt um 2 Einheiten höher, $x^2-2$ um 2 Einheiten tiefer. Form und Öffnung bleiben gleich, nur der Scheitel wandert auf der y-Achse.*

Der Parameter $e$ verschiebt also einfach die **gesamte** Parabel senkrecht, ohne ihre Form zu verändern. Das leuchtet ein, denn zu jedem Funktionswert wird derselbe Betrag $e$ addiert – jeder Punkt des Graphen wandert um $e$ nach oben oder unten. Der Scheitel liegt dann bei $(0, e)$.

### Horizontale Verschiebung

$$f(x) = (x - d)^2$$

Die Parabel wird um $d$ Einheiten **nach rechts** (wenn $d > 0$) oder **nach links** (wenn $d < 0$) verschoben.

> [!warning] Achtung: Vorzeichen!
> $(x - 3)^2$ verschiebt nach **rechts** (zu $x = 3$)
> $(x + 2)^2 = (x - (-2))^2$ verschiebt nach **links** (zu $x = -2$)
>
> Das Vorzeichen in der Klammer ist „umgekehrt" zur Verschiebungsrichtung – ein häufiger Stolperstein!

> [!tip] **Merkregel für Verschiebungen**
> Denke an die Klammer als „Verzögerung": Bei $(x - 3)^2$ erreicht die Funktion den Wert, den $x^2$ bei $x = 0$ hatte, erst bei $x = 3$ – also 3 Einheiten später/weiter rechts.

![[parabel-horizontal.png]]
*<span class="fig-id">01-09-09-parabel-horizontal</span>: Horizontale Verschiebung der Normalparabel – $(x+2)^2$ hat den Scheitel bei $x=-2$ (nach links), $(x-3)^2$ bei $x=3$ (nach rechts). Das Vorzeichen in der Klammer ist jeweils umgekehrt zur Verschiebungsrichtung.*

### Kombinierte Verschiebung

$$f(x) = (x - d)^2 + e$$

Scheitelpunkt: $S(d, e)$

> [!example] Beispiel
> $f(x) = (x - 2)^2 + 3$
> 
> - Verschiebung: 2 nach rechts, 3 nach oben
> - Scheitelpunkt: $S(2, 3)$

## Streckung und Stauchung

### Vertikale Streckung/Stauchung

$$f(x) = a \cdot x^2$$

| $\lvert a\rvert$ | Wirkung |
|---|---|
| $\lvert a\rvert > 1$ | Parabel wird **schmaler** (gestreckt in y-Richtung) |
| $\lvert a\rvert = 1$ | Normalparabel |
| $0 < \lvert a\rvert < 1$ | Parabel wird **weiter** (gestaucht in y-Richtung) |

### Spiegelung an der x-Achse

$$f(x) = -x^2$$

Bei $a < 0$ wird die Parabel an der x-Achse **gespiegelt** und öffnet nach unten.

## Vollständige Analyse einer Parabel

### Gegebene Gleichung analysieren

$f(x) = -2(x + 1)^2 + 4$

**Schritt 1**: Parameter identifizieren
- $a = -2$ (negativ → Öffnung nach unten, Betrag > 1 → schmaler)
- $d = -1$ (Verschiebung 1 nach links)
- $e = 4$ (Verschiebung 4 nach oben)

**Schritt 2**: Eigenschaften bestimmen

| Eigenschaft | Wert |
|---|---|
| Scheitelpunkt | $S(-1, 4)$ |
| Symmetrieachse | $x = -1$ |
| Öffnungsrichtung | nach unten |
| Weite | schmaler als Normalparabel |
| Maximum/Minimum | Maximum bei $y = 4$ |

**Schritt 3**: Weitere Punkte berechnen

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
|---|---|---|---|---|---|
| $f(x)$ | $-4$ | $2$ | $4$ | $2$ | $-4$ |

## Parabel aus Graph bestimmen

### Methode 1: Scheitelpunkt und weiterer Punkt

1. Scheitelpunkt $S(d, e)$ ablesen
2. Weiteren Punkt $P(x_1, y_1)$ ablesen
3. In Scheitelpunktform einsetzen und $a$ berechnen

> [!example] Beispiel
> Scheitelpunkt $S(2, -1)$, weiterer Punkt $P(4, 3)$
> 
> Ansatz: $f(x) = a(x - 2)^2 - 1$
> 
> Mit $P(4, 3)$: $3 = a(4 - 2)^2 - 1$
> $3 = 4a - 1$
> $a = 1$
> 
> Gleichung: $f(x) = (x - 2)^2 - 1$

### Methode 2: Drei Punkte

Drei Punkte in $f(x) = ax^2 + bx + c$ einsetzen und das Gleichungssystem lösen.

## Transformationen zusammenfassen

Die allgemeine Form mit allen Transformationen:

$$f(x) = a(x - d)^2 + e$$

| Parameter | Wirkung |
|---|---|
| $a > 0$ | Öffnung nach oben |
| $a < 0$ | Öffnung nach unten |
| $|a| > 1$ | Parabel schmaler |
| $|a| < 1$ | Parabel weiter |
| $d > 0$ | Verschiebung nach rechts |
| $d < 0$ | Verschiebung nach links |
| $e > 0$ | Verschiebung nach oben |
| $e < 0$ | Verschiebung nach unten |

## Parabeln zeichnen

### Schnelle Skizze

1. Scheitelpunkt einzeichnen
2. Symmetrieachse markieren
3. Weitere Punkte symmetrisch berechnen
4. Parabel durch die Punkte zeichnen

### Standardpunkte

Für $f(x) = a(x - d)^2 + e$:
- $x = d$: $y = e$ (Scheitelpunkt)
- $x = d \pm 1$: $y = e + a$
- $x = d \pm 2$: $y = e + 4a$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Scheitelpunktform: $f(x) = a(x - d)^2 + e$
> - $d$ bestimmt die horizontale, $e$ die vertikale Verschiebung
> - $|a|$ bestimmt die Weite, Vorzeichen von $a$ die Öffnungsrichtung
> - Scheitelpunkt: $S(d, e)$
> - Symmetrieachse: $x = d$
> - Zur Bestimmung der Gleichung: Scheitelpunkt + 1 weiterer Punkt genügen

## Zusammenhänge

- → [[08-Quadratische-Funktionen|Quadratische Funktionen]] – Allgemeine Form und Grundlagen
- → [[10-Schnittpunkte|Schnittpunkte]] – Wo Parabeln Geraden oder andere Parabeln schneiden
- → [[11-Anwendungen-Funktionen|Anwendungen]] – Wurfparabeln und Optimierung
- → [[../08-Gleichungen-und-Ungleichungen/09-Loesungsformel-quadratische-Gleichungen|Lösungsformel]] – Nullstellen von Parabeln berechnen

> [!tip] **Praxis-Tipp**
> Bei Prüfungsaufgaben lohnt es sich, die Parabel schnell zu skizzieren. Der Scheitelpunkt und die Öffnungsrichtung geben bereits einen guten Überblick, ob die berechneten Werte plausibel sind.

## Übungsaufgaben

1. Beschreibe die Transformation ausgehend von der Normalparabel:
   - $f(x) = (x - 4)^2$
   - $g(x) = x^2 + 5$
   - $h(x) = 3x^2$
   - $k(x) = -(x + 2)^2 - 1$

2. Bestimme den Scheitelpunkt und skizziere:
   - $f(x) = (x - 1)^2 - 4$
   - $g(x) = -0{,}5(x + 3)^2 + 2$

3. Bestimme die Funktionsgleichung:
   - Scheitelpunkt $S(3, 2)$, durch $P(5, 6)$
   - Scheitelpunkt $S(-1, 4)$, Öffnung nach unten, durch $P(1, 0)$

4. Ordne die Parabeln nach Weite (schmalste zuerst):
   $f(x) = 2x^2$, $g(x) = \frac{1}{3}x^2$, $h(x) = x^2$, $k(x) = 0{,}5x^2$

---

**Navigation**: [[08-Quadratische-Funktionen|← Quadratische Funktionen]] | [[00-Funktionen-Index|Übersicht]] | [[10-Schnittpunkte|Schnittpunkte →]]
