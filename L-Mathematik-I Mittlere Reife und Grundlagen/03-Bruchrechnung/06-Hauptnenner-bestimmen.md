---
author: Open Lectures
title: Hauptnenner bestimmen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-13
---

# Hauptnenner bestimmen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das kgV zweier Zahlen bestimmen können
> - Brüche auf den Hauptnenner bringen können
> - Wissen, wann der Hauptnenner benötigt wird

---

## Überblick

Der **Hauptnenner** (auch: gemeinsamer Nenner) ist das kleinste gemeinsame Vielfache (kgV) der Nenner. Er wird benötigt, um Brüche zu addieren oder zu subtrahieren.

---

## Definition

Der **Hauptnenner** zweier Brüche $\frac{a}{b}$ und $\frac{c}{d}$ ist:

$$\text{Hauptnenner} = \text{kgV}(b, d)$$

---

## Das kgV finden

### Methode 1: Vielfache aufzählen

Vielfache von 4: 4, 8, 12, 16, 20, ...
Vielfache von 6: 6, 12, 18, 24, ...

kgV(4, 6) = 12 (kleinstes gemeinsames)

### Methode 2: Über ggT

$$\text{kgV}(a, b) = \frac{a \cdot b}{\text{ggT}(a, b)}$$

**Beispiel:** kgV(4, 6)
- ggT(4, 6) = 2
- kgV = $\frac{4 \cdot 6}{2} = 12$

---

## Brüche auf den Hauptnenner bringen

**Beispiel:** $\frac{2}{3}$ und $\frac{5}{4}$

1. Hauptnenner: kgV(3, 4) = 12
2. Erweitern:
   - $\frac{2}{3} = \frac{2 \cdot 4}{3 \cdot 4} = \frac{8}{12}$
   - $\frac{5}{4} = \frac{5 \cdot 3}{4 \cdot 3} = \frac{15}{12}$

---

## Beispiele

| Brüche | Nenner | Hauptnenner | Erweitert |
|--------|--------|-------------|-----------|
| $\frac{1}{2}, \frac{1}{3}$ | 2, 3 | 6 | $\frac{3}{6}, \frac{2}{6}$ |
| $\frac{3}{4}, \frac{5}{6}$ | 4, 6 | 12 | $\frac{9}{12}, \frac{10}{12}$ |
| $\frac{2}{5}, \frac{3}{10}$ | 5, 10 | 10 | $\frac{4}{10}, \frac{3}{10}$ |

---

## Sonderfall: Teilbarkeit

Wenn ein Nenner ein Vielfaches des anderen ist, ist der größere Nenner bereits der Hauptnenner:

$$\frac{1}{3} + \frac{5}{6}$$

6 ist Vielfaches von 3 → Hauptnenner = 6

$$= \frac{2}{6} + \frac{5}{6} = \frac{7}{6}$$

---

## Zusammenhänge

- → [[04-Brueche-erweitern|Brüche erweitern]]
- → [[07-Addition-von-Bruechen|Addition von Brüchen]]
- → [[08-Subtraktion-von-Bruechen|Subtraktion von Brüchen]]

> [!warning] **Prüfungsrelevant**
> - Hauptnenner = kgV der Nenner
> - Beide Brüche auf Hauptnenner erweitern
> - Notwendig für Addition und Subtraktion

> [!question] **Typische Prüfungsfragen**
> - Bestimme den Hauptnenner von $\frac{3}{8}$ und $\frac{5}{12}$.
> - Bringe $\frac{2}{5}$ und $\frac{3}{4}$ auf den Hauptnenner.

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
