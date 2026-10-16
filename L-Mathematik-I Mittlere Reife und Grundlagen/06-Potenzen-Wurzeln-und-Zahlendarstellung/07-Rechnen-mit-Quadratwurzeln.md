---
title: "Rechnen mit Quadratwurzeln"
chapter: "06"
section: "07"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Wurzeln addieren und subtrahieren (gleichartige)"
  - "Wurzeln multiplizieren und dividieren"
  - "Wurzeln teilweise ziehen (vereinfachen)"
  - "Den Nenner rational machen"
tags:
  - mathematik
  - wurzeln
  - rechnen
  - vereinfachen
created: 2026-10-13
modified: 2025-06-26
---

# Rechnen mit Quadratwurzeln

> [!info] Lernziele
> - Wurzeln addieren und subtrahieren (gleichartige)
> - Wurzeln multiplizieren und dividieren
> - Wurzeln teilweise ziehen (vereinfachen)
> - Den Nenner rational machen

## Überblick

Für das Rechnen mit Wurzeln gelten besondere Regeln, die sich aus den Wurzelgesetzen ergeben.

Das Rechnen mit Wurzeln ist eine wichtige Fertigkeit in der Mathematik, besonders in der Geometrie und Algebra. Anders als bei gewöhnlichen Zahlen können wir Wurzelausdrücke oft nicht einfach als Dezimalzahl ausrechnen – stattdessen arbeiten wir mit ihnen in **exakter Form**. Das ist präziser als gerundete Werte und verhindert Rundungsfehler.

Die Regeln für das Wurzelrechnen folgen direkt aus den [[03-Potenzgesetze|Potenzgesetzen]], da $\sqrt{a} = a^{1/2}$ gilt. Wer die Potenzgesetze beherrscht, kann die Wurzelgesetze jederzeit selbst herleiten.

## Multiplikation und Division

$$\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}$$
$$\frac{\sqrt{a}}{\sqrt{b}} = \sqrt{\frac{a}{b}}$$

**Beispiele:**
- $\sqrt{3} \cdot \sqrt{12} = \sqrt{36} = 6$
- $\frac{\sqrt{50}}{\sqrt{2}} = \sqrt{25} = 5$

## Addition und Subtraktion

> [!warning] **Häufiger Fehler: Wurzeln lassen sich NICHT einfach addieren!**
> Nur **gleichartige** Wurzeln können zusammengefasst werden!

$$3\sqrt{5} + 2\sqrt{5} = 5\sqrt{5}$$ ✓
$$\sqrt{2} + \sqrt{3} \neq \sqrt{5}$$ ✗

> [!tip] **Analogie zu Variablen**
> Denke an Wurzeln wie an Variablen:
> - $3x + 2x = 5x$ ✓ (gleichartig)
> - $x + y \neq xy$ ✗ (verschiedenartig)
>
> Genauso gilt:
> - $3\sqrt{5} + 2\sqrt{5} = 5\sqrt{5}$ ✓
> - $\sqrt{2} + \sqrt{3}$ bleibt $\sqrt{2} + \sqrt{3}$ (nicht vereinfachbar)

**Warum ist $\sqrt{2} + \sqrt{3} \neq \sqrt{5}$?**

Prüfe nach: $\sqrt{2} \approx 1,41$ und $\sqrt{3} \approx 1,73$, also $\sqrt{2} + \sqrt{3} \approx 3,14$. Aber $\sqrt{5} \approx 2,24$ – das ist etwas völlig anderes!

## Teilweises Wurzelziehen

**Methode:** Radikand in Faktoren zerlegen, Quadratzahlen herausziehen.

Das teilweise Wurzelziehen (auch „Teilradizieren" genannt) ist eine wichtige Technik, um Wurzelausdrücke zu **vereinfachen**. Die Idee: Wenn der Radikand einen quadratischen Faktor enthält, kann dieser „vor die Wurzel gezogen" werden.

**Beispiel:** $\sqrt{72}$
$$\sqrt{72} = \sqrt{36 \cdot 2} = \sqrt{36} \cdot \sqrt{2} = 6\sqrt{2}$$

**Beispiel:** $\sqrt{50}$
$$\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$$

> [!tip] **Strategie: Größten quadratischen Teiler finden**
> 1. Zerlege den Radikanden in Primfaktoren: $72 = 2^3 \cdot 3^2$
> 2. Finde Paare (quadratische Faktoren): $72 = 2^2 \cdot 3^2 \cdot 2 = 36 \cdot 2$
> 3. Ziehe die Wurzel aus den Paaren: $\sqrt{36 \cdot 2} = 6\sqrt{2}$

**Weiteres Beispiel:** $\sqrt{180}$
$$180 = 2^2 \cdot 3^2 \cdot 5 = 36 \cdot 5$$
$$\sqrt{180} = \sqrt{36 \cdot 5} = 6\sqrt{5}$$

## Nenner rational machen

$$\frac{1}{\sqrt{a}} = \frac{1}{\sqrt{a}} \cdot \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{a}$$

**Beispiel:**
$$\frac{3}{\sqrt{5}} = \frac{3\sqrt{5}}{5}$$

> [!note] **Warum den Nenner rational machen?**
> In der Mathematik gilt die Konvention, dass Wurzeln nicht im Nenner stehen sollten. Das hat historische Gründe: Vor Taschenrechnern war es einfacher, durch eine rationale Zahl zu dividieren als durch eine Wurzel. Außerdem erleichtert ein rationaler Nenner den Vergleich von Brüchen.

> [!tip] **Technik: Erweitern mit der Wurzel**
> Um eine Wurzel aus dem Nenner zu entfernen, erweitere den Bruch mit genau dieser Wurzel:
> $$\frac{a}{\sqrt{b}} = \frac{a}{\sqrt{b}} \cdot \frac{\sqrt{b}}{\sqrt{b}} = \frac{a\sqrt{b}}{b}$$
>
> Im Nenner steht dann $\sqrt{b} \cdot \sqrt{b} = b$ – eine rationale Zahl.

## Zusammenhänge

### Voraussetzungen

- [[06-Quadratwurzeln]]
- [[08-Wurzelgesetze]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Teilweises Wurzelziehen und Rationalmachen sind Standardaufgaben.

## Typische Prüfungsfragen

1. Vereinfache: $\sqrt{98}$
2. Berechne: $\sqrt{2} \cdot \sqrt{8}$
3. Mache den Nenner rational: $\frac{4}{\sqrt{2}}$

## Quellen

- Lambacher Schweizer Mathematik 9

## Weiterführende Links

- [[08-Wurzelgesetze]]
- [[06-Quadratwurzeln]]
