---
title: "Rechtwinklige Dreiecke"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "01"
status: "draft - review pending"
type: lecture
keywords:
  - Rechtwinkliges Dreieck
  - Hypotenuse
  - Kathete
  - rechter Winkel
---

# Rechtwinklige Dreiecke

> [!info] Lernziele
> - Rechtwinklige Dreiecke erkennen und charakterisieren
> - Die Bezeichnungen Kathete und Hypotenuse sicher verwenden
> - Eigenschaften rechtwinkliger Dreiecke kennen
> - Die Bedeutung für Berechnungen verstehen

## Definition

Ein **rechtwinkliges Dreieck** ist ein Dreieck, bei dem ein Winkel genau **90°** (ein rechter Winkel) beträgt.

```
       C
       │╲
       │ ╲
       │  ╲
    a  │   ╲  c (Hypotenuse)
       │    ╲
       │     ╲
       │______╲
       A   b   B
```

## Bezeichnungen

### Hypotenuse

Die **Hypotenuse** ist die Seite, die dem rechten Winkel **gegenüberliegt**.

> [!tip] Merkregel
> Die Hypotenuse ist immer die **längste Seite** des rechtwinkligen Dreiecks.

In der Standardbezeichnung: Seite $c$ (gegenüber dem rechten Winkel bei $C$... aber Vorsicht: der rechte Winkel kann bei jeder Ecke sein!)

### Katheten

Die **Katheten** sind die beiden Seiten, die den rechten Winkel **einschließen**.

Man unterscheidet:
- **Ankathete** (zu einem spitzen Winkel): die Kathete, die am Winkel anliegt
- **Gegenkathete** (zu einem spitzen Winkel): die Kathete, die dem Winkel gegenüberliegt

```
       C
       │╲
       │ ╲
       │  ╲   Gegenkathete zu α
    a  │   ╲
       │  α ╲
       │______╲
       A   b   B
       
       b = Ankathete zu α
       a = Gegenkathete zu α
```

## Eigenschaften

### Winkelsumme

Da ein Winkel 90° beträgt, gilt für die beiden anderen Winkel:

$$\alpha + \beta = 90°$$

Die spitzen Winkel sind also **komplementär**.

> [!example] Beispiel
> Wenn $\alpha = 35°$, dann $\beta = 90° - 35° = 55°$.

### Seitenverhältnisse

- Die Hypotenuse ist **immer länger** als jede Kathete
- Es gilt: $c > a$ und $c > b$
- Aber auch: $c < a + b$ (Dreiecksungleichung)

### Spezielle rechtwinklige Dreiecke

| Name | Winkel | Seitenverhältnis |
|---|---|---|
| Gleichschenklig-rechtwinklig | 45°-45°-90° | $1 : 1 : \sqrt{2}$ |
| Ägyptisches Dreieck | 37°-53°-90° | $3 : 4 : 5$ |
| Halbes gleichseitiges | 30°-60°-90° | $1 : \sqrt{3} : 2$ |

### Das 3-4-5-Dreieck

Das älteste bekannte rechtwinklige Dreieck mit ganzzahligen Seiten:

$$3^2 + 4^2 = 9 + 16 = 25 = 5^2$$

> [!note] Pythagoreische Tripel
> Ganzzahlige Kombinationen wie (3, 4, 5), (5, 12, 13), (8, 15, 17) heißen **pythagoreische Tripel**.

## Erkennen rechtwinkliger Dreiecke

### Aus gegebenen Winkeln

Wenn einer der Winkel 90° beträgt → rechtwinklig.

### Aus gegebenen Seiten

Prüfung mit dem Satz des Pythagoras:

$$a^2 + b^2 = c^2$$

Wenn diese Gleichung erfüllt ist (mit $c$ als längster Seite), ist das Dreieck rechtwinklig.

> [!example] Beispiel
> Seiten: 6, 8, 10
> 
> Prüfung: $6^2 + 8^2 = 36 + 64 = 100 = 10^2$ ✓
> 
> Das Dreieck ist rechtwinklig.

## Der Thaleskreis

> [!note] Satz des Thales
> Jeder Punkt auf einem Halbkreis über dem Durchmesser bildet mit den Endpunkten des Durchmessers ein **rechtwinkliges Dreieck**.

```
           C
          ╱╲
         ╱  ╲
        ╱    ╲
       ╱      ╲
    A ●────────● B
        Durchmesser
```

Der Winkel bei $C$ ist immer 90°.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ein rechtwinkliges Dreieck hat einen Winkel von genau 90°
> - Die Hypotenuse liegt dem rechten Winkel gegenüber und ist die längste Seite
> - Die Katheten bilden den rechten Winkel
> - Die beiden spitzen Winkel ergeben zusammen 90°
> - Prüfung auf Rechtwinkligkeit: Pythagoras anwenden

## Übungsaufgaben

1. Bestimme den dritten Winkel:
   - $\alpha = 42°$, $\gamma = 90°$
   - $\beta = 28°$, rechter Winkel bei A

2. Welche der folgenden Tripel bilden rechtwinklige Dreiecke?
   - (5, 12, 13)
   - (7, 8, 11)
   - (9, 40, 41)

3. Zeichne ein rechtwinkliges Dreieck mit den Katheten 3 cm und 4 cm. Miss die Hypotenuse.

4. Beschrifte in einem rechtwinkligen Dreieck mit rechtem Winkel bei B die Hypotenuse und die Katheten.

---

**Navigation**: [[00-Pythagoras-Trigonometrie-Index|← Übersicht]] | [[02-Satz-des-Pythagoras|Satz des Pythagoras →]]
