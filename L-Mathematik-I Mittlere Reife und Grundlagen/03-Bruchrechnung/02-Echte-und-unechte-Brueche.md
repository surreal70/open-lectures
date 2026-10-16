---
author: Open Lectures
title: Echte und unechte Brüche
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-13
---

# Echte und unechte Brüche

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Echte und unechte Brüche unterscheiden können
> - Unechte Brüche in gemischte Zahlen umwandeln können
> - Wissen, wann ein Bruch größer, kleiner oder gleich 1 ist

---

## Überblick

Brüche lassen sich in zwei Kategorien einteilen: **echte Brüche** (kleiner als 1) und **unechte Brüche** (größer oder gleich 1). Diese Unterscheidung ist wichtig für das Verständnis und die Umwandlung in gemischte Zahlen.

---

## Definition

### Echter Bruch

Ein **echter Bruch** hat einen Zähler, der **kleiner** ist als der Nenner:

$$\text{Zähler} < \text{Nenner} \quad \Rightarrow \quad \frac{a}{b} < 1$$

**Beispiele:** $\frac{1}{2}$, $\frac{3}{4}$, $\frac{7}{10}$

### Unechter Bruch

Ein **unechter Bruch** hat einen Zähler, der **größer oder gleich** dem Nenner ist:

$$\text{Zähler} \geq \text{Nenner} \quad \Rightarrow \quad \frac{a}{b} \geq 1$$

**Beispiele:** $\frac{5}{3}$, $\frac{7}{4}$, $\frac{8}{8} = 1$

---

## Visualisierung

### Echter Bruch: $\frac{3}{4}$

```
┌───┬───┬───┬───┐
│ ▓ │ ▓ │ ▓ │   │   weniger als ein Ganzes
└───┴───┴───┴───┘
```

### Unechter Bruch: $\frac{5}{4}$

```
┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐
│ ▓ │ ▓ │ ▓ │ ▓ │   │ ▓ │   │   │   │   mehr als ein Ganzes
└───┴───┴───┴───┘   └───┴───┴───┴───┘
      1 Ganzes    +    ¼ = 1¼
```

---

## Umwandlung: Unechter Bruch → Gemischte Zahl

Division mit Rest:

$$\frac{7}{4} = 7 : 4 = 1 \text{ Rest } 3 = 1\frac{3}{4}$$

**Schritte:**
1. Zähler durch Nenner teilen (ganzzahlig)
2. Rest als Zähler des Bruchteils
3. Nenner bleibt gleich

**Beispiele:**

| Unechter Bruch | Rechnung | Gemischte Zahl |
|----------------|----------|----------------|
| $\frac{7}{3}$ | $7 : 3 = 2$ Rest $1$ | $2\frac{1}{3}$ |
| $\frac{11}{4}$ | $11 : 4 = 2$ Rest $3$ | $2\frac{3}{4}$ |
| $\frac{10}{5}$ | $10 : 5 = 2$ Rest $0$ | $2$ |

---

## Auf dem Zahlenstrahl

```
    echte Brüche          unechte Brüche
         ↓                      ↓
    ←──┬────┬────┬────┬────┬────┬────┬────┬──→
       0   ¼   ½   ¾    1   5/4  3/2  7/4   2
                        ↑
              Grenze: Zähler = Nenner
```

---

## Zusammenhänge

- → [[01-Grundlagen-der-Brueche|Grundlagen der Brüche]]
- → [[03-Gemischte-Zahlen|Gemischte Zahlen]]

> [!warning] **Prüfungsrelevant**
> - Echter Bruch: Zähler < Nenner, Wert < 1
> - Unechter Bruch: Zähler ≥ Nenner, Wert ≥ 1
> - Umwandlung durch Division mit Rest

> [!question] **Typische Prüfungsfragen**
> - Ist $\frac{9}{7}$ ein echter oder unechter Bruch?
> - Wandle $\frac{17}{5}$ in eine gemischte Zahl um.

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
