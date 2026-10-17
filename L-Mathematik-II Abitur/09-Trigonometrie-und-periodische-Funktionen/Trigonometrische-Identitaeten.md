---
author: Andreas Hümmer
title: Trigonometrische Identitäten
tags:
  - content
  - mathe
  - trigonometrie
  - identitaeten
  - formeln
created: 2025-06-20
modified: 2025-06-20
---

# Trigonometrische Identitäten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die fundamentalen trigonometrischen Identitäten kennen und anwenden können
> - Ausdrücke mit trigonometrischen Funktionen vereinfachen können
> - Die Beziehungen zwischen Sinus, Kosinus und Tangens verstehen
> - Identitäten für Umformungen und Beweise nutzen können

---

## Überblick

**Trigonometrische Identitäten** sind Gleichungen, die für alle zulässigen Werte der Variablen gelten. Sie sind fundamentale Werkzeuge zum Vereinfachen von Ausdrücken, Lösen von Gleichungen und Beweisen mathematischer Aussagen. Das Beherrschen dieser Identitäten ist essentiell für die gesamte Oberstufenmathematik.

## Die Pythagoräische Identität

### Hauptform

Die wichtigste trigonometrische Identität leitet sich direkt aus dem Einheitskreis ab:

$$\boxed{\sin^2(\alpha) + \cos^2(\alpha) = 1}$$

Sie gilt für **alle** $\alpha \in \mathbb{R}$.

### Umgestellte Formen

$$\sin^2(\alpha) = 1 - \cos^2(\alpha)$$
$$\cos^2(\alpha) = 1 - \sin^2(\alpha)$$

### Weitere Pythagoräische Identitäten

Durch Division der Hauptform durch $\cos^2(\alpha)$ bzw. $\sin^2(\alpha)$:

$$1 + \tan^2(\alpha) = \frac{1}{\cos^2(\alpha)} = \sec^2(\alpha)$$

$$1 + \cot^2(\alpha) = \frac{1}{\sin^2(\alpha)} = \csc^2(\alpha)$$

## Quotientenbeziehungen

### Definition des Tangens

$$\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$$

### Definition des Kotangens

$$\cot(\alpha) = \frac{\cos(\alpha)}{\sin(\alpha)} = \frac{1}{\tan(\alpha)}$$

### Produkt von Tangens und Kotangens

$$\tan(\alpha) \cdot \cot(\alpha) = 1$$

## Symmetriebeziehungen

### Negative Argumente

$$\sin(-\alpha) = -\sin(\alpha) \quad \text{(ungerade)}$$
$$\cos(-\alpha) = \cos(\alpha) \quad \text{(gerade)}$$
$$\tan(-\alpha) = -\tan(\alpha) \quad \text{(ungerade)}$$

### Komplementärwinkel ($90° - \alpha$)

$$\sin\left(\frac{\pi}{2} - \alpha\right) = \cos(\alpha)$$
$$\cos\left(\frac{\pi}{2} - \alpha\right) = \sin(\alpha)$$
$$\tan\left(\frac{\pi}{2} - \alpha\right) = \cot(\alpha)$$

Diese Beziehungen erklären die Namen „Cosinus" (= „Complement-Sinus") und „Cotangens".

### Supplementärwinkel ($180° - \alpha$)

$$\sin(\pi - \alpha) = \sin(\alpha)$$
$$\cos(\pi - \alpha) = -\cos(\alpha)$$
$$\tan(\pi - \alpha) = -\tan(\alpha)$$

### Verschiebung um $90°$

$$\sin\left(\alpha + \frac{\pi}{2}\right) = \cos(\alpha)$$
$$\cos\left(\alpha + \frac{\pi}{2}\right) = -\sin(\alpha)$$

### Verschiebung um $180°$

$$\sin(\alpha + \pi) = -\sin(\alpha)$$
$$\cos(\alpha + \pi) = -\cos(\alpha)$$
$$\tan(\alpha + \pi) = \tan(\alpha)$$

## Doppelwinkelformeln

### Sinus des doppelten Winkels

$$\sin(2\alpha) = 2\sin(\alpha)\cos(\alpha)$$

### Kosinus des doppelten Winkels

$$\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha)$$

Äquivalente Formen (durch Anwendung von $\sin^2 + \cos^2 = 1$):

$$\cos(2\alpha) = 2\cos^2(\alpha) - 1$$
$$\cos(2\alpha) = 1 - 2\sin^2(\alpha)$$

### Tangens des doppelten Winkels

$$\tan(2\alpha) = \frac{2\tan(\alpha)}{1 - \tan^2(\alpha)}$$

## Halbwinkelformeln

Aus den Doppelwinkelformeln ergeben sich:

$$\sin^2\left(\frac{\alpha}{2}\right) = \frac{1 - \cos(\alpha)}{2}$$

$$\cos^2\left(\frac{\alpha}{2}\right) = \frac{1 + \cos(\alpha)}{2}$$

$$\tan\left(\frac{\alpha}{2}\right) = \frac{\sin(\alpha)}{1 + \cos(\alpha)} = \frac{1 - \cos(\alpha)}{\sin(\alpha)}$$

## Potenzformeln

Diese Formeln sind wichtig für die Integration:

$$\sin^2(\alpha) = \frac{1 - \cos(2\alpha)}{2}$$

$$\cos^2(\alpha) = \frac{1 + \cos(2\alpha)}{2}$$

### Anwendungsbeispiel

Berechne $\int \sin^2(x) \, dx$:

$$\int \sin^2(x) \, dx = \int \frac{1 - \cos(2x)}{2} \, dx = \frac{x}{2} - \frac{\sin(2x)}{4} + C$$

## Produkt-zu-Summe-Formeln

$$\sin(\alpha)\cos(\beta) = \frac{1}{2}\left[\sin(\alpha + \beta) + \sin(\alpha - \beta)\right]$$

$$\cos(\alpha)\cos(\beta) = \frac{1}{2}\left[\cos(\alpha + \beta) + \cos(\alpha - \beta)\right]$$

$$\sin(\alpha)\sin(\beta) = \frac{1}{2}\left[\cos(\alpha - \beta) - \cos(\alpha + \beta)\right]$$

## Summe-zu-Produkt-Formeln

$$\sin(\alpha) + \sin(\beta) = 2\sin\left(\frac{\alpha + \beta}{2}\right)\cos\left(\frac{\alpha - \beta}{2}\right)$$

$$\sin(\alpha) - \sin(\beta) = 2\cos\left(\frac{\alpha + \beta}{2}\right)\sin\left(\frac{\alpha - \beta}{2}\right)$$

$$\cos(\alpha) + \cos(\beta) = 2\cos\left(\frac{\alpha + \beta}{2}\right)\cos\left(\frac{\alpha - \beta}{2}\right)$$

$$\cos(\alpha) - \cos(\beta) = -2\sin\left(\frac{\alpha + \beta}{2}\right)\sin\left(\frac{\alpha - \beta}{2}\right)$$

## Zusammenfassung: Die wichtigsten Identitäten

| Identität | Formel |
|-----------|--------|
| Pythagoras | $\sin^2(\alpha) + \cos^2(\alpha) = 1$ |
| Tangens | $\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$ |
| Negativer Winkel | $\sin(-\alpha) = -\sin(\alpha)$, $\cos(-\alpha) = \cos(\alpha)$ |
| Doppelwinkel (sin) | $\sin(2\alpha) = 2\sin(\alpha)\cos(\alpha)$ |
| Doppelwinkel (cos) | $\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha)$ |
| Potenz (sin²) | $\sin^2(\alpha) = \frac{1 - \cos(2\alpha)}{2}$ |
| Potenz (cos²) | $\cos^2(\alpha) = \frac{1 + \cos(2\alpha)}{2}$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Einheitskreis]] – Geometrische Herleitung der Identitäten
- → [[Additionstheoreme]] – Erweiterung auf Summen von Winkeln
- → [[Trigonometrische-Gleichungen]] – Anwendung der Identitäten
- → [[07-Integralrechnung-I-Index]] – Integration mit Potenzformeln

> [!warning] **Prüfungsrelevant**
> - Die Pythagoräische Identität $\sin^2 + \cos^2 = 1$ ist **absolut fundamental**
> - Die Doppelwinkelformeln werden häufig in Kurvendiskussionen benötigt
> - Die Potenzformeln sind für Integrale unverzichtbar
> - Symmetriebeziehungen helfen beim Vereinfachen

> [!question] **Typische Prüfungsfragen**
> - Vereinfachen Sie $\frac{1 - \cos^2(x)}{\sin(x)}$.
> - Zeigen Sie, dass $\sin(2x) = 2\sin(x)\cos(x)$ gilt.
> - Berechnen Sie $\int_0^{\pi} \cos^2(x) \, dx$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Additionstheoreme]] – Formeln für Summen und Differenzen von Winkeln
> - [[Trigonometrische-Gleichungen]] – Praktische Anwendung der Identitäten
