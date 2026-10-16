---
title: "Einführung in Funktionen"
created: 2026-10-13
modified: 2026-10-13
chapter: "09"
section: "03"
status: "draft - review pending"
type: lecture
keywords:
  - Funktion
  - Zuordnung
  - Definitions- und Wertebereich
  - Funktionswert
  - Funktionsterm
---

# Einführung in Funktionen

> [!info] Lernziele
> - Den Funktionsbegriff verstehen und erklären können
> - Funktionen von anderen Zuordnungen unterscheiden
> - Definitions- und Wertebereich bestimmen
> - Die verschiedenen Darstellungsformen kennen

## Was ist eine Funktion?

Eine **Funktion** ist eine eindeutige Zuordnung, die jedem Element einer Menge **genau ein** Element einer anderen Menge zuordnet.

### Formale Definition

$$f: D \to W, \quad x \mapsto f(x)$$

| Symbol | Bedeutung |
|---|---|
| $f$ | Name der Funktion |
| $D$ | Definitionsbereich (Input-Menge) |
| $W$ | Wertebereich (Output-Menge) |
| $x$ | Variable (Argument) |
| $f(x)$ | Funktionswert (Bild von $x$) |

### Das Prinzip der Eindeutigkeit

> [!warning] Wichtige Regel
> Zu jedem $x$-Wert gehört **genau ein** $y$-Wert.
> 
> - **Erlaubt**: Verschiedene $x$-Werte haben denselben $y$-Wert
> - **Nicht erlaubt**: Ein $x$-Wert hat mehrere $y$-Werte

```
Funktion:            Keine Funktion:
   x → y                x → y
   1 → 3                1 → 3
   2 → 5                1 → 4  ← Widerspruch!
   3 → 5                2 → 5
   ✓                    ✗
```

## Alltagsbeispiele für Funktionen

| Zuordnung | Funktion? | Begründung |
|---|---|---|
| Alter → Körpergröße | Ja | Jedes Alter hat eine Größe |
| Ort → Temperatur (zu einem Zeitpunkt) | Ja | Jeder Ort hat eine Temperatur |
| Person → Telefonnummer | Nein | Eine Person kann mehrere haben |
| Artikel → Preis | Ja | Jeder Artikel hat einen Preis |

## Schreibweisen

### Funktionsgleichung

$$f(x) = 2x + 3$$

- $f$ ist der Funktionsname
- $x$ ist die unabhängige Variable
- $2x + 3$ ist der Funktionsterm

### Alternative Schreibweise

$$y = 2x + 3$$

Hier wird $y$ als abhängige Variable verwendet.

### Funktionswerte berechnen

> [!example] Beispiel
> $f(x) = 2x + 3$
> 
> - $f(1) = 2 \cdot 1 + 3 = 5$
> - $f(4) = 2 \cdot 4 + 3 = 11$
> - $f(-2) = 2 \cdot (-2) + 3 = -1$
> - $f(0) = 2 \cdot 0 + 3 = 3$

## Definitionsbereich und Wertebereich

### Definitionsbereich $D$

Die Menge aller **erlaubten Eingabewerte** ($x$-Werte).

**Einschränkungen können entstehen durch**:
- Division durch Null (Nenner ≠ 0)
- Negative Werte unter der Wurzel
- Sachkontext (z.B. nur positive Längen)

> [!example] Beispiele
> - $f(x) = x^2$: $D = \mathbb{R}$
> - $f(x) = \frac{1}{x}$: $D = \mathbb{R} \setminus \{0\}$
> - $f(x) = \sqrt{x}$: $D = \mathbb{R}^+_0 = \{x \in \mathbb{R} \mid x \geq 0\}$

### Wertebereich $W$

Die Menge aller **möglichen Ausgabewerte** ($y$-Werte).

> [!example] Beispiele
> - $f(x) = x^2$: $W = \mathbb{R}^+_0$ (nur nicht-negative Werte)
> - $f(x) = 2x + 3$: $W = \mathbb{R}$ (alle reellen Zahlen)

## Darstellungsformen von Funktionen

### 1. Gleichung (algebraisch)

$$f(x) = x^2 - 4x + 3$$

### 2. Tabelle (Wertetabelle)

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $f(x)$ | $8$ | $3$ | $0$ | $-1$ | $0$ |

### 3. Graph (grafisch)

Der **Graph** einer Funktion ist die Menge aller Punkte $(x, f(x))$ im Koordinatensystem.

### 4. Verbal (in Worten)

„Die Funktion ordnet jeder Zahl ihr Quadrat zu."

## Grafischer Test auf Funktion

> [!tip] Vertikaler Linientest
> Wenn jede senkrechte Linie den Graphen **höchstens einmal** schneidet, liegt eine Funktion vor.

```
Funktion:              Keine Funktion:
    │  ╱                   │    ○
    │ ╱                    │   ╱ ╲
    │╱                     │  ╱   ╲
────┼──────                │ ○─────○
   ╱│                      │
  ╱ │                      │
 ✓                         ✗ (Kreis: mehrere y zu einem x)
```

## Zusammenfassung

> [!abstract] Kernpunkte
> - Eine Funktion ordnet jedem x-Wert genau einen y-Wert zu
> - Schreibweise: $f(x)$ oder $y = ...$
> - Der Definitionsbereich enthält alle erlaubten Eingabewerte
> - Der Wertebereich enthält alle möglichen Ausgabewerte
> - Darstellungsformen: Gleichung, Tabelle, Graph, verbal

## Übungsaufgaben

1. Prüfe, ob eine Funktion vorliegt:
   - Jedem Schüler wird seine Note zugeordnet
   - Jeder Note wird ein Schüler zugeordnet
   - Jeder Zahl wird ihr Betrag zugeordnet

2. Berechne für $f(x) = 3x - 5$:
   - $f(2)$, $f(0)$, $f(-3)$, $f(\frac{1}{3})$

3. Bestimme den Definitionsbereich:
   - $f(x) = \frac{2}{x-3}$
   - $g(x) = \sqrt{x-2}$
   - $h(x) = x^2 + 1$

4. Erstelle eine Wertetabelle für $f(x) = x^2 - 1$ mit $x \in \{-2, -1, 0, 1, 2\}$.

---

**Navigation**: [[02-Punkte-und-Koordinaten|← Punkte]] | [[00-Funktionen-Index|Übersicht]] | [[04-Funktionstabellen-und-Graphen|Funktionstabellen →]]
