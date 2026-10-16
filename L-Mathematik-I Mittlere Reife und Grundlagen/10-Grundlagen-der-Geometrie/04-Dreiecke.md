---
title: "Dreiecke"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "04"
status: "draft - review pending"
type: lecture
keywords:
  - Dreieck
  - Innenwinkelsumme
  - Dreieckarten
  - Höhe
  - Seitenhalbierende
---

# Dreiecke

> [!info] Lernziele
> - Die verschiedenen Dreieckarten kennen und unterscheiden
> - Die Innenwinkelsumme anwenden können
> - Besondere Linien im Dreieck kennen
> - Dreiecke konstruieren können

## Definition und Bezeichnung

Ein **Dreieck** ist eine geschlossene Figur aus drei Seiten und drei Ecken.

### Standardbezeichnung

```
           C
          /\
         /  \
      a /    \ b
       /      \
      /________\
     B    c     A
```

| Element | Bezeichnung |
|---|---|
| Eckpunkte | $A$, $B$, $C$ (gegen den Uhrzeigersinn) |
| Seiten | $a = \overline{BC}$, $b = \overline{CA}$, $c = \overline{AB}$ |
| Winkel | $\alpha$ bei $A$, $\beta$ bei $B$, $\gamma$ bei $C$ |

> [!tip] Merkregel
> Jede Seite liegt dem gleichnamigen Winkel/Eckpunkt **gegenüber**:
> - Seite $a$ liegt gegenüber von Ecke $A$ (und Winkel $\alpha$)

## Die Innenwinkelsumme

> [!warning] Fundamentaler Satz
> Die Summe der Innenwinkel eines Dreiecks beträgt immer **180°**:
> $$\alpha + \beta + \gamma = 180°$$

### Anwendung

> [!example] Beispiel
> Gegeben: $\alpha = 45°$, $\beta = 70°$
> 
> $\gamma = 180° - 45° - 70° = 65°$

## Dreieckarten nach Seiten

### Gleichseitiges Dreieck

Alle drei Seiten gleich lang: $a = b = c$

Alle Winkel gleich: $\alpha = \beta = \gamma = 60°$

```
         △
        ╱ ╲
       ╱   ╲
      ╱─────╲
```

### Gleichschenkliges Dreieck

Zwei Seiten gleich lang (z.B. $a = b$)

Die Basiswinkel sind gleich: $\alpha = \beta$

```
         △
        ╱|╲
       ╱ | ╲
      ╱──┴──╲
```

### Ungleichseitiges Dreieck

Alle Seiten verschieden lang: $a \neq b \neq c$

Alle Winkel verschieden.

## Dreieckarten nach Winkeln

### Spitzwinkliges Dreieck

Alle Winkel kleiner als 90°.

### Rechtwinkliges Dreieck

Ein Winkel ist genau 90°.

```
       C
       │╲
       │ ╲
       │  ╲
       │   ╲
       │____╲
       A     B
```

Die Seite gegenüber dem rechten Winkel heißt **Hypotenuse**.
Die anderen beiden Seiten heißen **Katheten**.

### Stumpfwinkliges Dreieck

Ein Winkel ist größer als 90°.

## Besondere Linien im Dreieck

### Höhe

Die **Höhe** $h_a$ ist das Lot von der Ecke $A$ auf die Gegenseite $a$.

```
           C
          /|\
         / | \
        /  |h \
       /   |   \
      /____|____\
     B     F     A
```

- Jedes Dreieck hat drei Höhen
- Die Höhen schneiden sich im **Höhenschnittpunkt** $H$

### Seitenhalbierende (Median)

Die **Seitenhalbierende** $s_a$ verbindet Ecke $A$ mit dem Mittelpunkt von Seite $a$.

- Die drei Seitenhalbierenden schneiden sich im **Schwerpunkt** $S$
- Der Schwerpunkt teilt jede Seitenhalbierende im Verhältnis 2:1

### Mittelsenkrechte

Die **Mittelsenkrechte** einer Seite steht senkrecht auf dieser und geht durch ihren Mittelpunkt.

- Die drei Mittelsenkrechten schneiden sich im **Umkreismittelpunkt** $U$

### Winkelhalbierende

Die **Winkelhalbierende** teilt einen Winkel in zwei gleich große Teile.

- Die drei Winkelhalbierenden schneiden sich im **Inkreismittelpunkt** $I$

## Übersicht: Besondere Punkte

| Punkt | Schnittpunkt von | Symbol |
|---|---|---|
| Höhenschnittpunkt | Höhen | $H$ |
| Schwerpunkt | Seitenhalbierenden | $S$ |
| Umkreismittelpunkt | Mittelsenkrechten | $U$ |
| Inkreismittelpunkt | Winkelhalbierenden | $I$ |

## Dreiecksungleichung

> [!warning] Existenzbedingung
> Ein Dreieck existiert nur, wenn jede Seite **kleiner** ist als die Summe der anderen beiden:
> 
> $$a < b + c$$
> $$b < a + c$$
> $$c < a + b$$

> [!example] Beispiel
> Können die Seiten $a = 3$, $b = 4$, $c = 8$ ein Dreieck bilden?
> 
> Prüfung: $3 + 4 = 7 < 8$ ✗
> 
> Nein, kein Dreieck möglich!

## Zusammenfassung

> [!abstract] Kernpunkte
> - Dreiecke haben drei Seiten, drei Ecken und drei Winkel
> - Die Innenwinkelsumme beträgt immer 180°
> - Einteilung nach Seiten: gleichseitig, gleichschenklig, ungleichseitig
> - Einteilung nach Winkeln: spitz-, recht-, stumpfwinklig
> - Besondere Linien: Höhen, Seitenhalbierende, Mittelsenkrechte, Winkelhalbierende
> - Die Dreiecksungleichung muss erfüllt sein

## Übungsaufgaben

1. Berechne den fehlenden Winkel:
   - $\alpha = 55°$, $\beta = 75°$
   - $\alpha = 90°$, $\gamma = 38°$
   - $\beta = \gamma = 50°$

2. Klassifiziere die Dreiecke nach Seiten und Winkeln:
   - $a = 5$, $b = 5$, $c = 8$, $\gamma = 106°$
   - $a = b = c = 6$
   - $a = 3$, $b = 4$, $c = 5$, $\gamma = 90°$

3. Prüfe, ob ein Dreieck mit den Seitenlängen existieren kann:
   - $a = 4$, $b = 5$, $c = 6$
   - $a = 2$, $b = 3$, $c = 7$
   - $a = 5$, $b = 5$, $c = 10$

4. Ein gleichschenkliges Dreieck hat den Basiswinkel $\alpha = 70°$. Berechne alle Winkel.

---

**Navigation**: [[03-Winkelberechnungen|← Winkelberechnungen]] | [[00-Geometrie-Index|Übersicht]] | [[05-Vierecke|Vierecke →]]
