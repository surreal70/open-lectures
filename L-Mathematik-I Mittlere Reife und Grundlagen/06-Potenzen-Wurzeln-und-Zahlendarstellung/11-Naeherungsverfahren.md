---
title: "Näherungsverfahren"
chapter: "06"
section: "11"
type: topic
status: final
learning_objectives:
  - "Wurzeln durch Intervallschachtelung approximieren"
  - "Das Heron-Verfahren anwenden können"
  - "Näherungswerte abschätzen"
  - "Die Genauigkeit von Näherungen beurteilen"
tags:
  - mathematik
  - naeherung
  - approximation
  - heron
created: 2026-10-13
modified: 2026-10-16
---

# Näherungsverfahren

> [!info] Lernziele
> - Wurzeln durch Intervallschachtelung approximieren
> - Das Heron-Verfahren anwenden können
> - Näherungswerte abschätzen
> - Die Genauigkeit von Näherungen beurteilen

## Überblick

**Näherungsverfahren** erlauben die Berechnung von Wurzeln ohne Taschenrechner.

Vor der Erfindung elektronischer Rechengeräte waren Näherungsverfahren unverzichtbar. Wie berechnet man $\sqrt{20}$, wenn man weder Taschenrechner noch Wurzeltabelle hat? Mathematiker entwickelten clevere Algorithmen, die sich Schritt für Schritt dem exakten Wert annähern.

Das berühmteste dieser Verfahren ist das **Heron-Verfahren**, benannt nach **Heron von Alexandria** (ca. 10–70 n. Chr.), einem griechischen Mathematiker und Ingenieur. Tatsächlich war das Verfahren schon den **Babyloniern** (ca. 1800 v. Chr.) bekannt – es ist also fast 4000 Jahre alt! Auf antiken Tontafeln finden sich Berechnungen von $\sqrt{2}$, die auf 6 Dezimalstellen genau sind.

Heute sind diese Verfahren nicht nur historisch interessant: Sie zeigen, wie Computer intern Wurzeln berechnen, und vermitteln ein tiefes Verständnis für **iterative Algorithmen** – Verfahren, die sich schrittweise einem Ergebnis nähern.

## Intervallschachtelung

**Beispiel:** $\sqrt{20}$ bestimmen

| Schritt | Intervall | Mitte | Mitte² |
|---------|-----------|-------|--------|
| 1 | [4; 5] | 4,5 | 20,25 (zu groß) |
| 2 | [4; 4,5] | 4,25 | 18,06 (zu klein) |
| 3 | [4,25; 4,5] | 4,375 | 19,14 (zu klein) |
| 4 | [4,375; 4,5] | 4,4375 | 19,69 |

**Ergebnis:** $\sqrt{20} \approx 4,47$

## Heron-Verfahren

**Formel:**
$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$$

> [!note] **Die Idee hinter dem Heron-Verfahren**
> Wenn $x$ eine Näherung für $\sqrt{a}$ ist, dann ist $\frac{a}{x}$ ebenfalls eine Näherung – aber auf der „anderen Seite" des wahren Werts. Ist $x$ zu groß, ist $\frac{a}{x}$ zu klein, und umgekehrt.
>
> Der **Mittelwert** $\frac{1}{2}(x + \frac{a}{x})$ liegt dazwischen und ist eine **bessere Näherung** als beide Ausgangswerte. Dieser Prozess wird wiederholt, bis die gewünschte Genauigkeit erreicht ist.

**Beispiel:** $\sqrt{10}$, Startwert $x_0 = 3$

| n | $x_n$ | $10/x_n$ | $x_{n+1}$ |
|---|-------|----------|-----------|
| 0 | 3 | 3,333 | 3,1667 |
| 1 | 3,1667 | 3,158 | 3,1623 |
| 2 | 3,1623 | 3,1623 | 3,1623 |

**Ergebnis:** $\sqrt{10} \approx 3,162$

> [!tip] **Schnelle Konvergenz**
> Das Heron-Verfahren konvergiert **quadratisch**: Mit jedem Schritt verdoppelt sich ungefähr die Anzahl korrekter Dezimalstellen! Schon nach 5-6 Schritten hat man typischerweise 10+ korrekte Stellen – ausreichend für fast alle praktischen Zwecke.

## Zusammenhänge

### Voraussetzungen

- [[06-Quadratwurzeln]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Niedrig-Mittel
> Mathematisches Verständnis, selten in Prüfungen.

## Typische Prüfungsfragen

1. Bestimme $\sqrt{30}$ durch Intervallschachtelung (2 Schritte).
2. Führe einen Schritt des Heron-Verfahrens für $\sqrt{5}$ durch.

## Quellen

- Lambacher Schweizer Mathematik 9

## Weiterführende Links

- [[06-Quadratwurzeln]]
