---
title: "Ausklammern"
chapter: "07"
section: "06"
type: topic
status: final
learning_objectives:
  - "Den größten gemeinsamen Faktor erkennen"
  - "Terme ausklammern können"
  - "Die Probe durch Ausmultiplizieren machen"
  - "Ausklammern als Umkehrung des Ausmultiplizierens verstehen"
tags:
  - mathematik
  - terme
  - ausklammern
  - faktor
created: 2026-10-13
modified: 2026-10-16
---

# Ausklammern

> [!info] Lernziele
> - Den größten gemeinsamen Faktor erkennen
> - Terme ausklammern können
> - Die Probe durch Ausmultiplizieren machen
> - Ausklammern als Umkehrung des Ausmultiplizierens verstehen

## Überblick

**Ausklammern** ist die Umkehrung des Ausmultiplizierens: Ein gemeinsamer Faktor wird vor eine Klammer geschrieben.

Das Ausklammern ist wie das „Rückwärts-Lesen" des Distributivgesetzes. Wenn Ausmultiplizieren bedeutet $a(b + c) \rightarrow ab + ac$, dann bedeutet Ausklammern $ab + ac \rightarrow a(b + c)$. Diese Technik ist besonders wichtig beim Vereinfachen von Brüchen und beim Lösen von Gleichungen.

> [!info] **Warum Ausklammern nützlich ist**
> - Terme werden oft kürzer und übersichtlicher
> - Brüche lassen sich leichter kürzen
> - Gleichungen werden einfacher zu lösen
> - Es ist der erste Schritt zur Faktorisierung (→ [[09-Faktorisierung]])

## Prinzip

$$ab + ac = a(b + c)$$

## Methode

1. Größten gemeinsamen Faktor (ggF) aller Summanden finden
2. Jeden Summanden durch ggF teilen
3. ggF vor die Klammer, Rest in die Klammer
4. **Probe:** Ausmultiplizieren muss Ausgangsterme ergeben

> [!tip] **Systematisches Vorgehen beim Finden des ggF**
> 1. Zuerst die **Zahlen** betrachten: Was ist der größte gemeinsame Teiler?
> 2. Dann die **Variablen**: Welche kommen in **allen** Summanden vor?
> 3. Bei Variablen: Die **kleinste** vorkommende Potenz wählen
>
> Beispiel: Bei $6x^3 + 9x^2$ ist der ggF = $3x^2$ (3 ist ggT von 6 und 9; $x^2$ ist die kleinste Potenz von $x$)

## Beispiele

### Zahlen ausklammern

$$6x + 9 = 3(2x + 3)$$
$$15a - 10 = 5(3a - 2)$$

### Variablen ausklammern

$$x^2 + 3x = x(x + 3)$$
$$2a^2 - 4a = 2a(a - 2)$$

### Kombiniert

$$6x^2 + 9x = 3x(2x + 3)$$
$$10ab - 15a = 5a(2b - 3)$$

## Übersicht

| Ausdruck | Ausgeklammert |
|----------|---------------|
| $4x + 8$ | $4(x + 2)$ |
| $x^2 - x$ | $x(x - 1)$ |
| $3a^2 + 6a$ | $3a(a + 2)$ |
| $12xy - 8x$ | $4x(3y - 2)$ |

## Probe

$$3x(2x + 3) = 6x^2 + 9x \checkmark$$

Die Probe ist unverzichtbar! Durch Ausmultiplizieren kann man sofort überprüfen, ob man richtig ausgeklammert hat.

> [!warning] **Häufiger Fehler: Nicht vollständig ausklammern**
> Manchmal wird nicht der größtmögliche Faktor ausgeklammert:
> 
> **Nicht optimal:** $12x^2 + 6x = 2(6x^2 + 3x)$
> **Besser:** $12x^2 + 6x = 6x(2x + 1)$
> 
> Prüfe immer, ob in der Klammer noch ein gemeinsamer Faktor steckt!

## Zusammenhänge

### Voraussetzungen

- [[05-Ausmultiplizieren]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Wichtig für Faktorisierung und Bruchrechnung mit Termen.

## Typische Prüfungsfragen

1. Klammere aus: 8x + 12
2. Klammere aus: x³ − 2x²
3. Klammere vollständig aus: 6a²b − 9ab²

## Quellen

- Lambacher Schweizer Mathematik 7

## Weiterführende Links

- [[09-Faktorisierung]]
- [[07-Vereinfachen-von-Termen]]
