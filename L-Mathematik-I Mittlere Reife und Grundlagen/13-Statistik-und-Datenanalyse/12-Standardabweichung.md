---
title: Einführung in die Standardabweichung
chapter: "13"
section: "13.12"
type: lecture
created: 2026-10-13
modified: 2026-10-25
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

Die Standardabweichung ist das wichtigste und am häufigsten verwendete Streuungsmaß in der Statistik. Anders als die Spannweite berücksichtigt sie **alle** Datenwerte und gibt an, wie weit die Werte **im Durchschnitt** vom Mittelwert entfernt sind.

### Historischer Hintergrund

Die Standardabweichung wurde um 1893 vom britischen Statistiker Karl Pearson eingeführt. Der Begriff stammt vom englischen *standard deviation*. Pearson entwickelte sie, um die Streuung von Messreihen präzise zu quantifizieren – ein entscheidender Fortschritt für die Wissenschaft, da nun Messunsicherheiten vergleichbar wurden.

> [!tip] **Warum nicht einfach der Durchschnitt der Abweichungen?**
> Man könnte meinen, die „durchschnittliche Abweichung vom Mittelwert" sei ein gutes Streuungsmaß. Das Problem: Positive und negative Abweichungen heben sich gegenseitig auf – die Summe der Abweichungen ist immer null!
> 
> Lösung: Man **quadriert** die Abweichungen. Dadurch werden alle Werte positiv, und größere Abweichungen werden stärker gewichtet.

## Idee

Die Standardabweichung misst, wie weit die einzelnen Werte **durchschnittlich** vom arithmetischen Mittel $\bar{x}$ entfernt sind.

**Anschaulich:** Stell dir den Mittelwert als „Zentrum" der Daten vor. Die Standardabweichung gibt an, wie weit die Datenpunkte im Durchschnitt von diesem Zentrum entfernt liegen.

## Berechnung

Die Berechnung erfolgt in vier Schritten:

### Schritt 1: Mittelwert berechnen

$$\bar{x} = \frac{\sum x_i}{n}$$

### Schritt 2: Abweichungen vom Mittelwert berechnen und quadrieren

Für jeden Wert: $(x_i - \bar{x})^2$

> [!note] **Warum quadrieren?**
> 1. Negative Abweichungen werden positiv (sonst würden sie sich aufheben)
> 2. Größere Abweichungen werden stärker gewichtet (Ausreißer fallen mehr ins Gewicht)

### Schritt 3: Varianz berechnen

Die **Varianz** $s^2$ ist der Durchschnitt der quadrierten Abweichungen:

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n}$$

### Schritt 4: Standardabweichung berechnen

Die **Standardabweichung** $s$ ist die Wurzel aus der Varianz:

$$s = \sqrt{s^2} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$$

> [!note] **Warum die Wurzel ziehen?**
> Durch das Quadrieren in Schritt 2 hat die Varianz eine „falsche" Einheit (z.B. cm² statt cm). Die Wurzel bringt uns zurück zur ursprünglichen Einheit, sodass die Standardabweichung direkt mit den Daten vergleichbar ist.

## Beispiel

> [!example] **Daten:** 2, 4, 4, 4, 5, 5, 7, 9
> 
> **Schritt 1: Mittelwert**
> $$\bar{x} = \frac{2 + 4 + 4 + 4 + 5 + 5 + 7 + 9}{8} = \frac{40}{8} = 5$$
> 
> **Schritt 2: Abweichungen und Quadrate**
> | Wert $x_i$ | Abweichung $x_i - \bar{x}$ | Quadrat $(x_i - \bar{x})^2$ |
> |------------|----------------------------|----------------------------|
> | 2 | 2 − 5 = −3 | 9 |
> | 4 | 4 − 5 = −1 | 1 |
> | 4 | 4 − 5 = −1 | 1 |
> | 4 | 4 − 5 = −1 | 1 |
> | 5 | 5 − 5 = 0 | 0 |
> | 5 | 5 − 5 = 0 | 0 |
> | 7 | 7 − 5 = 2 | 4 |
> | 9 | 9 − 5 = 4 | 16 |
> | **Summe** | **0** | **32** |
> 
> **Schritt 3: Varianz**
> $$s^2 = \frac{32}{8} = 4$$
> 
> **Schritt 4: Standardabweichung**
> $$s = \sqrt{4} = 2$$
> 
> Die Werte weichen im Durchschnitt um etwa 2 Einheiten vom Mittelwert ab.

## Interpretation

Die Standardabweichung gibt die „typische" Streuung um den Mittelwert an:

- **$s = 0$**: Alle Werte sind gleich (keine Streuung)
- **Kleines $s$**: Die Werte liegen eng um den Mittelwert
- **Großes $s$**: Die Werte sind weit um den Mittelwert gestreut

> [!tip] **Faustregel für normalverteilte Daten**
> Bei vielen natürlichen Phänomenen (Körpergröße, IQ, Messfehler) gilt näherungsweise:
> - Ca. **68%** der Werte liegen innerhalb von $\bar{x} \pm s$
> - Ca. **95%** der Werte liegen innerhalb von $\bar{x} \pm 2s$
> - Ca. **99,7%** der Werte liegen innerhalb von $\bar{x} \pm 3s$

> [!warning] **Häufiger Fehler: Einheit vergessen**
> Die Standardabweichung hat dieselbe Einheit wie die Daten!
> 
> Wenn die Daten in cm gemessen sind, ist auch $s$ in cm. Die Varianz $s^2$ hingegen ist in cm² – deshalb ist sie schwerer zu interpretieren.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Basis für die Standardabweichung
- → [[11-Spannweite|Spannweite]] – Einfacheres (aber gröberes) Streuungsmaß
- → [[07-Histogramme|Histogramme]] – Verteilungsformen visualisieren
- → [[13-Interpretation|Interpretation]] – Statistische Kennwerte deuten

> [!warning] **Prüfungsrelevant**
> - Die vier Berechnungsschritte kennen
> - Unterschied Varianz (quadriert) und Standardabweichung (Wurzel)
> - Interpretation: Was bedeutet ein kleines/großes $s$?
> - Summe der Abweichungen ist immer 0 (deshalb wird quadriert)

---

**Navigation:** [[11-Spannweite|← Spannweite]] | [[13-Interpretation|Interpretation →]]
