---
title: Einführung in die Standardabweichung
chapter: "13"
section: "13.12"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/statistik
  - standardabweichung
  - streuung
---

# Einführung in die Standardabweichung

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Das Prinzip der Standardabweichung verstehen
> - Die Varianz berechnen
> - Die Standardabweichung interpretieren

## Idee

Die Standardabweichung misst, wie weit die Werte durchschnittlich vom Mittelwert entfernt sind.

## Berechnung

### Schritt 1: Mittelwert

$$\bar{x} = \frac{\sum x_i}{n}$$

### Schritt 2: Abweichungen quadrieren

$$(x_i - \bar{x})^2$$

### Schritt 3: Varianz

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n}$$

### Schritt 4: Standardabweichung

$$s = \sqrt{s^2}$$

## Beispiel

> [!example] Daten: 2, 4, 4, 4, 5, 5, 7, 9
> 
> 1. $\bar{x} = \frac{40}{8} = 5$
> 2. Abweichungen: -3, -1, -1, -1, 0, 0, 2, 4
> 3. Quadrate: 9, 1, 1, 1, 0, 0, 4, 16 → Summe = 32
> 4. $s^2 = \frac{32}{8} = 4$
> 5. $s = \sqrt{4} = 2$

## Interpretation

- $s = 0$: Alle Werte gleich
- Kleines $s$: Werte eng um Mittelwert
- Großes $s$: Werte weit gestreut

---

**Navigation:** [[11-Spannweite|← Spannweite]] | [[13-Interpretation|Interpretation →]]
