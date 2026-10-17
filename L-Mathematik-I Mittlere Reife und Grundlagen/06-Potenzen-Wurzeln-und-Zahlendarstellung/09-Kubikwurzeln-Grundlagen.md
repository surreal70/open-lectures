---
title: "Kubikwurzeln Grundlagen"
chapter: "06"
section: "09"
type: topic
status: final
learning_objectives:
  - "Den Begriff Kubikwurzel verstehen"
  - "Einfache Kubikwurzeln berechnen"
  - "Den Unterschied zur Quadratwurzel erkennen"
  - "Kubikwurzeln in der Anwendung nutzen"
tags:
  - mathematik
  - wurzeln
  - kubikwurzel
  - dritte-wurzel
created: 2026-10-13
modified: 2026-10-16
---

# Kubikwurzeln Grundlagen

> [!info] Lernziele
> - Den Begriff Kubikwurzel verstehen
> - Einfache Kubikwurzeln berechnen
> - Den Unterschied zur Quadratwurzel erkennen
> - Kubikwurzeln in der Anwendung nutzen

## Überblick

Die **Kubikwurzel** (dritte Wurzel) ist die Umkehroperation des Kubierens (hoch 3).

Während die Quadratwurzel fragt „Welche Zahl ergibt quadriert den Radikanden?", fragt die Kubikwurzel: „Welche Zahl ergibt **dreimal mit sich selbst multipliziert** den Radikanden?" Die Kubikwurzel von 8 ist also 2, weil $2 \cdot 2 \cdot 2 = 8$.

Historisch spielten Kubikwurzeln eine wichtige Rolle bei einem der berühmtesten Probleme der Antike: der **Würfelverdopplung** (auch „Delisches Problem" genannt). Die Aufgabe war, einen Würfel zu konstruieren, dessen Volumen doppelt so groß ist wie ein gegebener Würfel. Dafür muss die Kantenlänge mit $\sqrt[3]{2}$ multipliziert werden – doch die Griechen konnten zeigen, dass dies mit Zirkel und Lineal **unmöglich** ist.

In der Praxis begegnen uns Kubikwurzeln bei **Volumenberechnungen**: Wenn ein Würfel ein bestimmtes Volumen haben soll, berechnet man die Kantenlänge mit der Kubikwurzel. Beispielsweise hat ein Würfel mit 1 Liter Volumen (= 1000 cm³) die Kantenlänge $\sqrt[3]{1000} = 10$ cm.

## Definition

> [!tip] Definition
> $\sqrt[3]{a} = b$ bedeutet: $b^3 = a$

## Wichtige Kubikwurzeln

| $\sqrt[3]{a}$ | Wert |
|---------------|------|
| $\sqrt[3]{1}$ | 1 |
| $\sqrt[3]{8}$ | 2 |
| $\sqrt[3]{27}$ | 3 |
| $\sqrt[3]{64}$ | 4 |
| $\sqrt[3]{125}$ | 5 |
| $\sqrt[3]{216}$ | 6 |
| $\sqrt[3]{1000}$ | 10 |

## Unterschied zur Quadratwurzel

| Quadratwurzel | Kubikwurzel |
|---------------|-------------|
| Nur für a ≥ 0 definiert | Für alle reellen Zahlen definiert |
| $\sqrt{-4}$ existiert nicht | $\sqrt[3]{-8} = -2$ ✓ |
| Ergebnis ≥ 0 | Ergebnis kann negativ sein |

> [!note] **Warum kann die Kubikwurzel negativ sein?**
> Der entscheidende Unterschied: Eine **negative Zahl hoch 3** ergibt wieder eine **negative Zahl**:
> - $(-2)^3 = (-2) \cdot (-2) \cdot (-2) = 4 \cdot (-2) = -8$
>
> Daher existiert zu jeder negativen Zahl eine (negative) Kubikwurzel.
>
> Bei Quadraten ist das anders: $(-2)^2 = 4$ und $2^2 = 4$ – beide Ergebnisse sind positiv. Daher gibt es keine reelle Quadratwurzel aus negativen Zahlen.

> [!tip] **Merkregel: Ungerade Exponenten erhalten das Vorzeichen**
> - Quadratwurzel ($\sqrt{\phantom{x}}$): nur für $a \geq 0$, Ergebnis immer $\geq 0$
> - Kubikwurzel ($\sqrt[3]{\phantom{x}}$): für alle reellen Zahlen, Vorzeichen bleibt erhalten
> - Allgemein: Wurzeln mit **ungeradem** Index ($\sqrt[3]{\phantom{x}}, \sqrt[5]{\phantom{x}}, ...$) erlauben negative Radikanden

## Negative Radikanden

$$\sqrt[3]{-27} = -3$$ weil $(-3)^3 = -27$

## Zusammenhang mit Potenzen

$$\sqrt[3]{a} = a^{1/3}$$

## Zusammenhänge

### Voraussetzungen

- [[06-Quadratwurzeln]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Mittel
> Weniger häufig als Quadratwurzeln, aber für Volumenberechnungen wichtig.

## Typische Prüfungsfragen

1. Berechne: $\sqrt[3]{64}$, $\sqrt[3]{-125}$
2. Ein Würfel hat das Volumen 343 cm³. Kantenlänge?

## Quellen

- Lambacher Schweizer Mathematik 9

## Weiterführende Links

- [[06-Quadratwurzeln]]
- [[08-Wurzelgesetze]]
