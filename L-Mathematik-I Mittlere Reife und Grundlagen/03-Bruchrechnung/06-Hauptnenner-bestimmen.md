---
author: Andreas Hümmer
title: Hauptnenner bestimmen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
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

Warum brauchen wir einen gemeinsamen Nenner? Stell dir vor, du möchtest $\frac{1}{3}$ und $\frac{1}{4}$ addieren. Das ist wie der Versuch, Äpfel und Birnen zu addieren – verschiedene „Sorten". Erst wenn wir beide Brüche auf denselben Nenner bringen (dieselbe „Sorte" Bruchteil), können wir sie sinnvoll zusammenzählen.

Der **Hauptnenner** ist dabei der **kleinste** gemeinsame Nenner. Theoretisch könnten wir auch einen größeren gemeinsamen Nenner wählen, aber der Hauptnenner hält die Zahlen klein und die Rechnung übersichtlich.

---

## Definition

Der **Hauptnenner** zweier Brüche $\frac{a}{b}$ und $\frac{c}{d}$ ist:

$$\text{Hauptnenner} = \text{kgV}(b, d)$$

Das **kgV** (kleinstes gemeinsames Vielfaches) ist die kleinste Zahl, die von beiden Nennern geteilt werden kann.

> [!note] **Warum das kgV?**
> Jeder gemeinsame Nenner muss ein Vielfaches beider ursprünglichen Nenner sein – sonst könnten wir nicht auf ihn erweitern. Das **kleinste** dieser Vielfachen zu nehmen, macht die Rechnung am einfachsten.

---

## Das kgV finden

### Methode 1: Vielfache aufzählen

Liste die Vielfachen beider Zahlen auf und finde das kleinste gemeinsame:

Vielfache von 4: 4, 8, **12**, 16, 20, 24, ...
Vielfache von 6: 6, **12**, 18, 24, 30, ...

kgV(4, 6) = 12 (kleinstes gemeinsames)

> [!tip] **Praktischer Tipp**
> Schreibe die Vielfachen der größeren Zahl auf und prüfe, welches davon auch durch die kleinere Zahl teilbar ist.
>
> Für kgV(4, 6): Vielfache von 6 sind 6, 12, 18...
> - 6 : 4 = 1,5 ✗
> - 12 : 4 = 3 ✓ → kgV = 12

### Methode 2: Über ggT

Es gibt einen eleganten Zusammenhang zwischen kgV und ggT (größter gemeinsamer Teiler):

$$\text{kgV}(a, b) = \frac{a \cdot b}{\text{ggT}(a, b)}$$

**Beispiel:** kgV(4, 6)
- ggT(4, 6) = 2
- kgV = $\frac{4 \cdot 6}{2} = \frac{24}{2} = 12$

> [!note] **Warum funktioniert diese Formel?**
> Das Produkt $a \cdot b$ enthält alle Primfaktoren von beiden Zahlen – aber manche doppelt. Durch Division mit dem ggT (der die gemeinsamen Faktoren enthält) eliminieren wir diese Dopplung.

### Methode 3: Primfaktorzerlegung (für Fortgeschrittene)

Zerlege beide Zahlen in Primfaktoren und nimm jeden Primfaktor in der höchsten vorkommenden Potenz:

- $12 = 2^2 \cdot 3$
- $18 = 2 \cdot 3^2$
- kgV$(12, 18) = 2^2 \cdot 3^2 = 4 \cdot 9 = 36$

---

## Brüche auf den Hauptnenner bringen

**Beispiel:** $\frac{2}{3}$ und $\frac{5}{4}$

1. Hauptnenner: kgV(3, 4) = 12
2. Erweitern:
   - $\frac{2}{3} = \frac{2 \cdot 4}{3 \cdot 4} = \frac{8}{12}$ (Erweiterungsfaktor: $12 : 3 = 4$)
   - $\frac{5}{4} = \frac{5 \cdot 3}{4 \cdot 3} = \frac{15}{12}$ (Erweiterungsfaktor: $12 : 4 = 3$)

> [!tip] **So findest du den Erweiterungsfaktor**
> Der Erweiterungsfaktor für jeden Bruch ist:
> $$\text{Erweiterungsfaktor} = \frac{\text{Hauptnenner}}{\text{alter Nenner}}$$
>
> Bei $\frac{2}{3}$ auf Nenner 12: Faktor = $12 : 3 = 4$

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

> [!note] **Warum ist das so?**
> Wenn $b$ ein Vielfaches von $a$ ist (z.B. 6 ist Vielfaches von 3), dann ist kgV$(a, b) = b$.
> Der Bruch mit dem größeren Nenner muss gar nicht erweitert werden!

### Weitere Sonderfälle

| Situation | Hauptnenner | Beispiel |
|-----------|-------------|----------|
| Nenner sind gleich | Der gemeinsame Nenner | $\frac{1}{5} + \frac{3}{5}$: HN = 5 |
| Ein Nenner teilt den anderen | Der größere Nenner | $\frac{1}{4} + \frac{3}{8}$: HN = 8 |
| Nenner sind teilerfremd | Produkt der Nenner | $\frac{1}{3} + \frac{1}{7}$: HN = 21 |

> [!warning] **Häufiger Fehler**
> Manche Schüler nehmen immer das Produkt der Nenner als gemeinsamen Nenner. Das funktioniert zwar, führt aber oft zu unnötig großen Zahlen:
>
> **Umständlich:** $\frac{1}{4} + \frac{1}{6}$ mit Nenner $4 \cdot 6 = 24$
> **Besser:** $\frac{1}{4} + \frac{1}{6}$ mit Hauptnenner kgV$(4,6) = 12$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[04-Brueche-erweitern|Brüche erweitern]] – Wie wir auf den Hauptnenner kommen
- → [[07-Addition-von-Bruechen|Addition von Brüchen]] – Hauptanwendung des Hauptnenners
- → [[08-Subtraktion-von-Bruechen|Subtraktion von Brüchen]] – Ebenfalls Hauptnenner nötig

> [!warning] **Prüfungsrelevant**
> - Hauptnenner = kgV der Nenner
> - Beide Brüche auf Hauptnenner erweitern
> - Notwendig für Addition und Subtraktion

> [!question] **Typische Prüfungsfragen**
> - Bestimme den Hauptnenner von $\frac{3}{8}$ und $\frac{5}{12}$.
> - Bringe $\frac{2}{5}$ und $\frac{3}{4}$ auf den Hauptnenner.

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
