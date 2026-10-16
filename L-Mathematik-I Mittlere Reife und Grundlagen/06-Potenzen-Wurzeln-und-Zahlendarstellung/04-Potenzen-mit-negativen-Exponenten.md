---
title: "Potenzen mit negativen Exponenten"
chapter: "06"
section: "04"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Negative Exponenten als Kehrwert verstehen"
  - "Potenzen mit negativen Exponenten berechnen"
  - "Zwischen positiven und negativen Exponenten umformen"
  - "Die Potenzgesetze auf negative Exponenten anwenden"
tags:
  - mathematik
  - potenzen
  - negative-exponenten
  - kehrwert
created: 2026-10-13
modified: 2025-06-26
---

# Potenzen mit negativen Exponenten

> [!info] Lernziele
> - Negative Exponenten als Kehrwert verstehen
> - Potenzen mit negativen Exponenten berechnen
> - Zwischen positiven und negativen Exponenten umformen
> - Die Potenzgesetze auf negative Exponenten anwenden

## Überblick

Ein **negativer Exponent** bedeutet, dass man den Kehrwert der Potenz mit positivem Exponenten bildet.

Diese Erweiterung der Potenzschreibweise auf negative Exponenten ist keine willkürliche Definition, sondern eine logische Konsequenz der Potenzgesetze. Sie ermöglicht es, Brüche elegant als Potenzen zu schreiben und macht die Rechenregeln konsistenter.

Historisch entwickelte sich das Konzept im 17. Jahrhundert. **John Wallis** und **Isaac Newton** erkannten, dass die Potenzgesetze auch für negative (und sogar gebrochene) Exponenten gelten sollten. Die Definition $a^{-n} = \frac{1}{a^n}$ ist die einzige, die alle Potenzgesetze erhält.

> [!tip] **Warum ist $a^{-n} = \frac{1}{a^n}$?**
> Betrachte die Potenzreihe: $a^3, a^2, a^1, a^0, a^{-1}, a^{-2}, ...$
> 
> Wenn wir den Exponenten um 1 verringern, **dividieren wir durch a**:
> - $a^3 : a = a^2$
> - $a^2 : a = a^1$  
> - $a^1 : a = a^0 = 1$
> - $a^0 : a = a^{-1} = \frac{1}{a}$
> - $a^{-1} : a = a^{-2} = \frac{1}{a^2}$
> 
> Das Muster setzt sich logisch fort!

## Definition

> [!tip] Definition
> $$a^{-n} = \frac{1}{a^n}$$ (für a ≠ 0)

## Beispiele

| Potenz | Umformung | Ergebnis |
|--------|-----------|----------|
| $2^{-1}$ | $\frac{1}{2^1}$ | $\frac{1}{2} = 0,5$ |
| $3^{-2}$ | $\frac{1}{3^2}$ | $\frac{1}{9}$ |
| $10^{-3}$ | $\frac{1}{10^3}$ | $\frac{1}{1000} = 0,001$ |
| $5^{-1}$ | $\frac{1}{5}$ | $0,2$ |

## Umformungsregeln

### Vom Nenner in den Zähler

$$\frac{1}{a^n} = a^{-n}$$

### Vom Zähler in den Nenner

$$a^{-n} = \frac{1}{a^n}$$

### Im Bruch

$$\frac{a^m}{a^n} = a^{m-n}$$

Wenn m < n: Ergebnis hat negativen Exponenten.

## Zehnerpotenzen mit negativem Exponenten

| Potenz | Wert |
|--------|------|
| $10^{-1}$ | 0,1 |
| $10^{-2}$ | 0,01 |
| $10^{-3}$ | 0,001 |
| $10^{-6}$ | 0,000001 |

> [!note] **Anschauliche Deutung**
> Der negative Exponent zeigt an, wie viele Stellen das Komma **nach links** verschoben wird:
> - $10^{-1}$: eine Stelle nach links → $0,1$
> - $10^{-3}$: drei Stellen nach links → $0,001$
>
> Umgekehrt bedeutet ein positiver Exponent eine Verschiebung nach rechts.

> [!warning] **Häufiger Fehler**
> Verwechsle nicht:
> - $10^{-2} = 0,01$ (positiv, sehr klein)
> - $-10^2 = -100$ (negativ, groß)
>
> Der negative Exponent macht die Zahl **klein**, nicht negativ!

## Potenzgesetze gelten weiterhin

$$a^3 \cdot a^{-5} = a^{3+(-5)} = a^{-2} = \frac{1}{a^2}$$

$$\frac{a^2}{a^5} = a^{2-5} = a^{-3}$$

## Zusammenhänge

### Voraussetzungen

- [[03-Potenzgesetze]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Wichtig für wissenschaftliche Schreibweise und Bruchrechnung mit Potenzen.

## Typische Prüfungsfragen

1. Schreibe als Bruch: $4^{-2}$, $10^{-4}$
2. Schreibe mit positivem Exponenten: $\frac{1}{x^3}$
3. Vereinfache: $a^5 \cdot a^{-3}$

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[05-Zehnerpotenzen]]
- [[10-Wissenschaftliche-Schreibweise]]
