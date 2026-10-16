---
title: "Steigung und y-Achsenabschnitt"
created: 2026-10-13
modified: 2025-07-18
chapter: "09"
section: "06"
status: "draft - review pending"
type: lecture
keywords:
  - Steigung
  - Steigungsdreieck
  - y-Achsenabschnitt
  - Differenzenquotient
---

# Steigung und y-Achsenabschnitt

> [!info] Lernziele
> - Die Steigung grafisch und rechnerisch bestimmen
> - Das Steigungsdreieck anwenden können
> - Den y-Achsenabschnitt aus Graph und Gleichung ablesen
> - Zusammenhänge zwischen Steigung und Funktionsverlauf verstehen

## Die Steigung im Detail

### Definition

Die **Steigung** $m$ einer Geraden gibt an, wie stark die Gerade ansteigt oder fällt. Sie beschreibt das Verhältnis von vertikaler zu horizontaler Änderung.

$$m = \frac{\text{Änderung in } y}{\text{Änderung in } x} = \frac{\Delta y}{\Delta x}$$

> [!info] **Anschauliche Bedeutung**
> Die Steigung beantwortet die Frage: „Wenn ich eine Einheit nach rechts gehe, wie viele Einheiten gehe ich dann nach oben (oder unten)?"
>
> - Bei $m = 2$: Für jede Einheit nach rechts geht es 2 Einheiten nach oben
> - Bei $m = -3$: Für jede Einheit nach rechts geht es 3 Einheiten nach **unten**
> - Bei $m = 0{,}5$: Für jede Einheit nach rechts geht es nur eine halbe Einheit nach oben

### Das Steigungsdreieck

Das **Steigungsdreieck** ist ein rechtwinkliges Dreieck, das die Steigung veranschaulicht:

```
    y
    ↑
    │        ●P₂
    │       ╱│
    │     ╱  │ Δy (Höhe)
    │   ╱    │
    │ ●──────┘
    │ P₁  Δx (Breite)
────┼──────────→ x
```

$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

### Interpretation der Steigung

| Steigung | Bedeutung | Veranschaulichung |
|---|---|---|
| $m = 1$ | 45°-Winkel, pro 1 nach rechts auch 1 nach oben | „1:1 Anstieg" |
| $m = 2$ | steil, pro 1 nach rechts 2 nach oben | „2:1 Anstieg" |
| $m = 0{,}5$ | flach, pro 1 nach rechts nur 0,5 nach oben | „1:2 Anstieg" |
| $m = -1$ | fällt, pro 1 nach rechts 1 nach unten | „Gefälle 1:1" |

### Steigung in Prozent

In der Praxis (Straßenschilder) wird die Steigung oft in **Prozent** angegeben:

$$\text{Steigung in \%} = m \cdot 100\%$$

> [!example] Beispiel
> Ein Straßenschild zeigt 12% Gefälle.
> 
> Das bedeutet: $m = -0{,}12$
> 
> Pro 100 m horizontal fällt die Straße um 12 m.

> [!info] **Steigung im Alltag**
> Die Steigung begegnet uns überall:
>
> | Kontext | Typische Steigung |
> |---|---|
> | Rollstuhlrampe (barrierefrei) | max. 6% |
> | Normale Straße | bis 10% |
> | Passstraße in den Alpen | 10–15% |
> | Skipiste (leicht, blau) | ca. 25% |
> | Skipiste (schwer, schwarz) | über 40% |
> | Hausdach (flach) | ca. 20–30% |
> | Hausdach (steil) | 50–100% |
>
> Für Rollstuhlfahrer und Menschen mit Gehbehinderung ist die maximale Steigung von Rampen gesetzlich geregelt – hier hat Mathematik direkte Auswirkungen auf Barrierefreiheit!

## Steigung berechnen

### Aus zwei Punkten

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

> [!example] Beispiel
> $A(1, 3)$ und $B(5, 11)$
> 
> $$m = \frac{11 - 3}{5 - 1} = \frac{8}{4} = 2$$

> [!warning] Achtung
> Die Punkte können in beliebiger Reihenfolge eingesetzt werden, aber **konsistent**:
> $$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_1 - y_2}{x_1 - x_2}$$
> Nicht mischen!

> [!warning] **Häufiger Fehler**
> Ein klassischer Fehler ist das Vertauschen von Zähler und Nenner: $\frac{\Delta x}{\Delta y}$ statt $\frac{\Delta y}{\Delta x}$. Merke: Die Steigung beschreibt, wie stark die **y-Werte** (vertikal) sich ändern – also muss $\Delta y$ **oben** stehen!

### Aus der Funktionsgleichung

Bei $f(x) = mx + b$ ist $m$ direkt ablesbar.

> [!example] Beispiel
> $f(x) = -3x + 7$
> 
> Die Steigung ist $m = -3$.

### Aus dem Graphen

1. Zwei Punkte auf der Geraden wählen (mit ganzzahligen Koordinaten!)
2. Steigungsdreieck einzeichnen
3. $\Delta y$ und $\Delta x$ ablesen
4. $m = \frac{\Delta y}{\Delta x}$ berechnen

## Der y-Achsenabschnitt

### Definition

Der **y-Achsenabschnitt** $b$ ist der y-Wert des Schnittpunkts der Geraden mit der y-Achse.

$$b = f(0)$$

### Aus der Gleichung ablesen

Bei $f(x) = mx + b$ ist $b$ direkt ablesbar.

> [!example] Beispiele
> - $f(x) = 2x + 5$ → $b = 5$
> - $g(x) = -x - 3$ → $b = -3$
> - $h(x) = 4x$ → $b = 0$

### Aus dem Graphen ablesen

Der y-Achsenabschnitt ist dort, wo die Gerade die **y-Achse schneidet** (bei $x = 0$).

```
    y
    ↑
  5 ┤───●────── Schnittpunkt bei b = 5
    │  ╱
  3 ┤╱
    │
────┼──────→ x
    │
```

### Aus einem Punkt und der Steigung berechnen

Gegeben: Punkt $P(x_1, y_1)$ und Steigung $m$.

$$b = y_1 - m \cdot x_1$$

> [!example] Beispiel
> $P(3, 7)$ und $m = 2$
> 
> $b = 7 - 2 \cdot 3 = 7 - 6 = 1$
> 
> Also: $f(x) = 2x + 1$

## Besondere Geraden

### Horizontale Geraden

$$f(x) = b \quad (m = 0)$$

- Steigung ist Null
- Parallel zur x-Achse
- Alle Punkte haben denselben y-Wert

```
    y
    ↑
  3 ├────────────── f(x) = 3
    │
────┼──────────→ x
```

### Die x-Achse

$$f(x) = 0$$

Ist ein Sonderfall einer horizontalen Geraden mit $b = 0$.

### Vertikale Geraden

$$x = c$$

> [!warning] Keine Funktion!
> Vertikale Geraden sind **keine Funktionen**, da jedem x-Wert unendlich viele y-Werte zugeordnet wären.

## Geraden skizzieren

### Schnelle Methode

1. y-Achsenabschnitt $b$ auf der y-Achse einzeichnen
2. Von dort mit dem Steigungsdreieck weitergehen
3. Gerade durch beide Punkte zeichnen

> [!example] Beispiel: $f(x) = \frac{2}{3}x - 1$
> 1. $b = -1$ einzeichnen: Punkt $(0, -1)$
> 2. Steigung $m = \frac{2}{3}$: 3 nach rechts, 2 nach oben → Punkt $(3, 1)$
> 3. Gerade durch $(0, -1)$ und $(3, 1)$ zeichnen

## Zusammenfassung

> [!abstract] Kernpunkte
> - Steigung $m = \frac{\Delta y}{\Delta x}$ = Höhe durch Breite des Steigungsdreiecks
> - y-Achsenabschnitt $b$ = Schnittpunkt mit der y-Achse
> - Aus der Gleichung $f(x) = mx + b$ sind beide direkt ablesbar
> - Steigung aus zwei Punkten: $m = \frac{y_2 - y_1}{x_2 - x_1}$
> - y-Achsenabschnitt aus Punkt und Steigung: $b = y - mx$

## Zusammenhänge

- → [[05-Lineare-Funktionen|Lineare Funktionen]] – Die Grundlagen linearer Funktionen
- → [[07-Geradengleichungen|Geradengleichungen]] – Gleichungen aufstellen
- → [[../05-Verhaeltnisse-und-Proportionalitaet/04-Direkte-Proportionalitaet|Direkte Proportionalität]] – Steigung als Proportionalitätsfaktor
- → [[../11-Satz-des-Pythagoras-und-Trigonometrie/11-Steigungen-Neigungswinkel|Steigungen und Neigungswinkel]] – Zusammenhang mit Trigonometrie

## Übungsaufgaben

1. Bestimme die Steigung der Geraden durch:
   - $A(2, 4)$ und $B(6, 12)$
   - $C(-1, 5)$ und $D(3, -3)$
   - $E(0, 2)$ und $F(4, 2)$

2. Lies Steigung und y-Achsenabschnitt ab:
   - $f(x) = -2x + 4$
   - $g(x) = \frac{3}{4}x - 2$
   - $h(x) = 5$

3. Bestimme die Geradengleichung:
   - Durch $(0, 3)$ mit $m = -2$
   - Durch $(4, 5)$ mit $m = \frac{1}{2}$

4. Skizziere die Geraden:
   - $f(x) = 2x - 3$
   - $g(x) = -\frac{1}{2}x + 2$
   - $h(x) = 4$

5. Ein Straßenschild zeigt 15% Steigung. Wie hoch liegt das Ende einer 200 m langen Strecke über dem Anfang?

---

**Navigation**: [[05-Lineare-Funktionen|← Lineare Funktionen]] | [[00-Funktionen-Index|Übersicht]] | [[07-Geradengleichungen|Geradengleichungen →]]
