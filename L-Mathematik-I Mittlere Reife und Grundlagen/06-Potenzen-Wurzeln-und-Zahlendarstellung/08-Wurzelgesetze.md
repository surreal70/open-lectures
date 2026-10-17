---
title: "Wurzelgesetze"
chapter: "06"
section: "08"
type: topic
status: final
learning_objectives:
  - "Die Wurzelgesetze kennen und anwenden"
  - "Den Zusammenhang zwischen Wurzeln und Potenzen verstehen"
  - "Wurzelausdrücke systematisch vereinfachen"
  - "Wurzelgesetze bei Umformungen nutzen"
tags:
  - mathematik
  - wurzeln
  - wurzelgesetze
  - rechenregeln
created: 2026-10-13
modified: 2026-10-16
---

# Wurzelgesetze

> [!info] Lernziele
> - Die Wurzelgesetze kennen und anwenden
> - Den Zusammenhang zwischen Wurzeln und Potenzen verstehen
> - Wurzelausdrücke systematisch vereinfachen
> - Wurzelgesetze bei Umformungen nutzen

## Überblick

Die **Wurzelgesetze** sind die Entsprechung der Potenzgesetze für Wurzeln.

Da Wurzeln nichts anderes als Potenzen mit gebrochenen Exponenten sind ($\sqrt{a} = a^{1/2}$), leiten sich die Wurzelgesetze direkt aus den [[03-Potenzgesetze|Potenzgesetzen]] ab. Diese Verbindung ist fundamental: Wer die Potenzgesetze versteht, kann die Wurzelgesetze jederzeit selbst herleiten.

Die systematische Behandlung der Wurzelgesetze geht auf die Arbeiten von **Leonhard Euler** (1707–1783) zurück, der als Erster eine vollständige Theorie der Potenzen und Wurzeln mit beliebigen Exponenten entwickelte. Seine Erkenntnisse bilden noch heute die Grundlage für das Rechnen mit Wurzeln.

In der Praxis helfen uns die Wurzelgesetze, komplizierte Wurzelausdrücke zu **vereinfachen**, Gleichungen zu lösen und Terme umzuformen – unverzichtbare Fähigkeiten für Algebra und Geometrie.

## Die Wurzelgesetze

### 1. Produktregel

$$\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}$$

### 2. Quotientenregel

$$\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$$

### 3. Potenzregel

$$\sqrt{a^n} = a^{n/2} = (\sqrt{a})^n$$

### 4. Wurzel aus Wurzel

$$\sqrt{\sqrt{a}} = \sqrt[4]{a} = a^{1/4}$$

## Zusammenhang mit Potenzen

$$\sqrt{a} = a^{1/2}$$
$$\sqrt[n]{a} = a^{1/n}$$

## Übersicht

| Gesetz | Formel | Beispiel |
|--------|--------|----------|
| Produkt | $\sqrt{ab} = \sqrt{a} \cdot \sqrt{b}$ | $\sqrt{4 \cdot 9} = 2 \cdot 3 = 6$ |
| Quotient | $\sqrt{a/b} = \sqrt{a}/\sqrt{b}$ | $\sqrt{16/4} = 4/2 = 2$ |
| Potenz | $\sqrt{a^2} = |a|$ | $\sqrt{(-3)^2} = 3$ |

## Häufige Fehler

> [!warning] **Häufiger Fehler: Die gefährlichste Verwechslung**

| Falsch | Richtig | Erklärung |
|--------|---------|-----------|
| $\sqrt{a+b} = \sqrt{a} + \sqrt{b}$ | Gilt nicht! | Die Wurzel einer Summe ist NICHT die Summe der Wurzeln |
| $\sqrt{a^2} = a$ | $\sqrt{a^2} = |a|$ | Der Betrag ist nötig, falls $a$ negativ sein könnte |

> [!tip] **Gegenbeispiel zum Merken**
> $\sqrt{9 + 16} = \sqrt{25} = 5$
> 
> Aber: $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$
> 
> $5 \neq 7$ → Die Wurzel einer Summe ist **nicht** die Summe der Wurzeln!

> [!note] **Warum $\sqrt{a^2} = |a|$?**
> Betrachte $a = -3$: Dann ist $a^2 = 9$ und $\sqrt{9} = 3$ (nicht $-3$!).
> 
> Da die Quadratwurzel per Definition **immer nicht-negativ** ist, brauchen wir den Betrag:
> - $\sqrt{(-3)^2} = \sqrt{9} = 3 = |-3|$
> - $\sqrt{3^2} = \sqrt{9} = 3 = |3|$

## Zusammenhänge

### Voraussetzungen

- [[06-Quadratwurzeln]]
- [[03-Potenzgesetze]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Grundlage für Termumformungen und Gleichungen.

## Typische Prüfungsfragen

1. Vereinfache mit Wurzelgesetzen: $\sqrt{16 \cdot 25}$
2. Berechne: $\sqrt{\frac{49}{9}}$
3. Warum ist $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$?

## Quellen

- Lambacher Schweizer Mathematik 9

## Weiterführende Links

- [[03-Potenzgesetze]]
- [[07-Rechnen-mit-Quadratwurzeln]]
