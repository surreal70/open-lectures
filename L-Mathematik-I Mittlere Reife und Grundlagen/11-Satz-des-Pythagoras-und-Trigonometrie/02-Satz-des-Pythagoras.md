---
title: "Der Satz des Pythagoras"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "02"
status: "draft - review pending"
type: lecture
keywords:
  - Pythagoras
  - Kathetensatz
  - Hypotenusenquadrat
  - Beweis
---

# Der Satz des Pythagoras

> [!info] Lernziele
> - Den Satz des Pythagoras formulieren und verstehen
> - Die Formel korrekt anwenden
> - Die Bedeutung geometrisch interpretieren
> - Einen anschaulichen Beweis nachvollziehen

## Der Satz

> [!warning] Satz des Pythagoras
> In einem **rechtwinkligen Dreieck** gilt:
> 
> $$a^2 + b^2 = c^2$$
> 
> Das Quadrat über der Hypotenuse ist gleich der Summe der Quadrate über den Katheten.

### Formulierung in Worten

> „In jedem rechtwinkligen Dreieck ist die Summe der Flächeninhalte der Quadrate über den Katheten gleich dem Flächeninhalt des Quadrates über der Hypotenuse."

## Geometrische Interpretation

```
           ┌─────┐
           │  c² │
           │     │
       ┌───┼─────┼───┐
       │   │╲    │   │
       │ a²│ ╲   │   │
       │   │  ╲  │   │
       │   │   ╲ │   │
       └───┼────╲┼───┘
           │     ╲
           └──────┘
              b²
```

Fläche des Quadrats über $c$ = Fläche des Quadrats über $a$ + Fläche des Quadrats über $b$

## Historischer Hintergrund

- Benannt nach dem griechischen Mathematiker **Pythagoras** (~570–510 v. Chr.)
- War aber schon den Babyloniern bekannt (~1800 v. Chr.)
- Über 400 verschiedene Beweise sind dokumentiert

## Anschaulicher Beweis

### Beweis durch Flächenvergleich

Zwei gleich große Quadrate mit Seitenlänge $(a + b)$:

**Anordnung 1**:
```
┌────┬────────┐
│    │        │
│ a² │        │
│    │        │
├────┼────────┤
│    │   b²   │
└────┴────────┘
```
Plus zwei Rechtecke der Fläche $a \cdot b$

**Anordnung 2**:
```
    ╱╲
   ╱  ╲
  ╱ c² ╲
 ╱      ╲
╱────────╲
```
Ein Quadrat $c^2$ plus vier Dreiecke mit je Fläche $\frac{1}{2}ab$

Da beide Anordnungen dieselbe Gesamtfläche haben:

$$a^2 + b^2 + 2ab = c^2 + 4 \cdot \frac{1}{2}ab$$
$$a^2 + b^2 + 2ab = c^2 + 2ab$$
$$a^2 + b^2 = c^2$$

## Anwendung der Formel

### Hypotenuse berechnen

Gegeben: Katheten $a$ und $b$, gesucht: Hypotenuse $c$

$$c = \sqrt{a^2 + b^2}$$

> [!example] Beispiel
> $a = 3$ cm, $b = 4$ cm
> 
> $c = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$ cm

### Kathete berechnen

Gegeben: Hypotenuse $c$ und eine Kathete $a$, gesucht: Kathete $b$

$$b = \sqrt{c^2 - a^2}$$

> [!example] Beispiel
> $c = 13$ cm, $a = 5$ cm
> 
> $b = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$ cm

## Formelübersicht

| Gesucht | Formel |
|---|---|
| Hypotenuse $c$ | $c = \sqrt{a^2 + b^2}$ |
| Kathete $a$ | $a = \sqrt{c^2 - b^2}$ |
| Kathete $b$ | $b = \sqrt{c^2 - a^2}$ |

## Wichtige Hinweise

> [!warning] Voraussetzung
> Der Satz des Pythagoras gilt **nur für rechtwinklige Dreiecke**!

> [!tip] Rechenschritte
> 1. Prüfen: Ist das Dreieck rechtwinklig?
> 2. Identifizieren: Welche Seite ist die Hypotenuse?
> 3. Einsetzen: Werte in die richtige Formel einsetzen
> 4. Ausrechnen: Quadrieren, Addieren/Subtrahieren, Wurzel ziehen

## Die Umkehrung des Satzes

> [!note] Umkehrung
> Wenn in einem Dreieck $a^2 + b^2 = c^2$ gilt (wobei $c$ die längste Seite ist), dann ist das Dreieck **rechtwinklig**.

Dies ermöglicht die **Prüfung auf Rechtwinkligkeit**.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Im rechtwinkligen Dreieck: $a^2 + b^2 = c^2$
> - Die Hypotenuse $c$ liegt dem rechten Winkel gegenüber
> - Die Formel kann nach jeder Seite umgestellt werden
> - Der Satz gilt nur für rechtwinklige Dreiecke
> - Mit der Umkehrung kann man prüfen, ob ein Dreieck rechtwinklig ist

## Übungsaufgaben

1. Berechne die fehlende Seite:
   - $a = 6$ cm, $b = 8$ cm, $c = ?$
   - $a = 5$ cm, $c = 13$ cm, $b = ?$
   - $b = 15$ cm, $c = 17$ cm, $a = ?$

2. Prüfe, ob die Dreiecke rechtwinklig sind:
   - $a = 9$, $b = 12$, $c = 15$
   - $a = 4$, $b = 5$, $c = 6$

3. Ein rechtwinkliges Dreieck hat die Katheten 7 cm und 24 cm. Wie lang ist die Hypotenuse?

4. Die Hypotenuse eines rechtwinkligen Dreiecks ist 25 cm lang. Eine Kathete misst 7 cm. Wie lang ist die andere Kathete?

---

**Navigation**: [[01-Rechtwinklige-Dreiecke|← Rechtwinklige Dreiecke]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[03-Berechnung-unbekannter-Seiten|Anwendungen →]]
