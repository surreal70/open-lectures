---
title: Der Würfel
chapter: "12"
section: "12.2"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - wuerfel
  - volumen
  - oberflaeche
---

# Der Würfel

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften des Würfels benennen
> - Volumen eines Würfels berechnen
> - Oberfläche eines Würfels berechnen
> - Raumdiagonale und Flächendiagonale bestimmen
> - Praktische Aufgaben zum Würfel lösen

## Definition und Eigenschaften

### Was ist ein Würfel?

> [!note] Definition
> Ein **Würfel** (auch Hexaeder) ist ein regelmäßiger Körper, bei dem alle sechs Begrenzungsflächen kongruente Quadrate sind.

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Flächen | 6 (alle Quadrate) |
| Kanten | 12 (alle gleich lang) |
| Ecken | 8 |
| Winkel | alle 90° |

**Der Würfel ist der einzige Körper, bei dem:**
- alle Kanten gleich lang sind
- alle Winkel rechte Winkel sind
- alle Flächen gleich groß sind

## Volumen des Würfels

### Formel

> [!note] Volumenformel
> $$V = a^3$$
> wobei $a$ die Kantenlänge ist.

Das Volumen ist die dritte Potenz der Kantenlänge – daher auch der Name "Kubikzahl" für $a^3$.

### Beispielrechnungen

> [!example] Beispiel 1: Volumen berechnen
> Ein Würfel hat die Kantenlänge $a = 5$ cm.
> 
> **Lösung:**
> $$V = a^3 = 5^3 = 5 \cdot 5 \cdot 5 = 125 \text{ cm}^3$$

> [!example] Beispiel 2: Kantenlänge berechnen
> Ein Würfel hat ein Volumen von 216 cm³. Wie lang ist eine Kante?
> 
> **Lösung:**
> $$V = a^3$$
> $$216 = a^3$$
> $$a = \sqrt[3]{216} = 6 \text{ cm}$$

### Umrechnung Volumeneinheiten

| Einheit | Umrechnung |
|---------|------------|
| 1 cm³ | = 1 ml |
| 1 dm³ | = 1 Liter = 1000 cm³ |
| 1 m³ | = 1000 Liter = 1.000.000 cm³ |

## Oberfläche des Würfels

### Formel

> [!note] Oberflächenformel
> $$O = 6a^2$$
> (6 Quadrate mit Fläche $a^2$)

### Beispielrechnungen

> [!example] Beispiel 3: Oberfläche berechnen
> Ein Würfel hat die Kantenlänge $a = 4$ cm.
> 
> **Lösung:**
> $$O = 6a^2 = 6 \cdot 4^2 = 6 \cdot 16 = 96 \text{ cm}^2$$

> [!example] Beispiel 4: Kantenlänge aus Oberfläche
> Ein Würfel hat eine Oberfläche von 150 cm². Wie lang ist eine Kante?
> 
> **Lösung:**
> $$O = 6a^2$$
> $$150 = 6a^2$$
> $$a^2 = 25$$
> $$a = 5 \text{ cm}$$

## Diagonalen

### Flächendiagonale

Die Diagonale einer Würfelfläche (eines Quadrats):

$$d_F = a\sqrt{2}$$

### Raumdiagonale

Die Diagonale durch den gesamten Würfel (von Ecke zu gegenüberliegender Ecke):

$$d_R = a\sqrt{3}$$

> [!example] Beispiel 5: Diagonalen berechnen
> Ein Würfel hat die Kantenlänge $a = 6$ cm.
> 
> **Flächendiagonale:**
> $$d_F = 6\sqrt{2} \approx 8,49 \text{ cm}$$
> 
> **Raumdiagonale:**
> $$d_R = 6\sqrt{3} \approx 10,39 \text{ cm}$$

### Herleitung der Raumdiagonale

Mit dem [[11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]]:

1. Flächendiagonale: $d_F^2 = a^2 + a^2 = 2a^2$
2. Raumdiagonale: $d_R^2 = d_F^2 + a^2 = 2a^2 + a^2 = 3a^2$
3. Also: $d_R = \sqrt{3a^2} = a\sqrt{3}$

## Würfelnetz

### Darstellung

Es gibt 11 verschiedene Würfelnetze. Das bekannteste:

```
    ▢
  ▢ ▢ ▢ ▢
    ▢
```

### Praktische Anwendung

> [!example] Beispiel 6: Kartonbedarf
> Für einen Würfel mit 10 cm Kantenlänge soll ein Netz aus Karton zugeschnitten werden. Wie viel Karton wird mindestens benötigt?
> 
> **Lösung:**
> Die Oberfläche beträgt:
> $$O = 6 \cdot 10^2 = 600 \text{ cm}^2$$
> 
> Mindestens 600 cm² Karton werden benötigt (ohne Klebelaschen).

## Praktische Anwendungen

### Verpackung und Lagerung

> [!example] Beispiel 7: Würfelzucker
> Ein Würfelzucker hat die Kantenlänge 1,2 cm.
> 
> a) Welches Volumen hat ein Stück?
> $$V = 1,2^3 = 1,728 \text{ cm}^3$$
> 
> b) Wie viele Stück passen in eine Dose von 500 cm³?
> $$n = \frac{500}{1,728} \approx 289 \text{ Stück}$$
> (theoretisch, praktisch weniger durch Lücken)

### Materialverbrauch

> [!example] Beispiel 8: Anstrich
> Ein Holzwürfel mit 15 cm Kantenlänge soll lackiert werden.
> 
> a) Welche Fläche muss lackiert werden?
> $$O = 6 \cdot 15^2 = 6 \cdot 225 = 1350 \text{ cm}^2 = 0,135 \text{ m}^2$$
> 
> b) Wie viel Lack wird bei 100 ml/m² benötigt?
> $$0,135 \cdot 100 = 13,5 \text{ ml}$$

## Verhältnis Volumen zu Oberfläche

### Größenabhängigkeit

Bei wachsender Kantenlänge wächst das Volumen schneller als die Oberfläche:

| Kantenlänge | Oberfläche | Volumen | O/V |
|-------------|------------|---------|-----|
| 1 cm | 6 cm² | 1 cm³ | 6 |
| 2 cm | 24 cm² | 8 cm³ | 3 |
| 3 cm | 54 cm² | 27 cm³ | 2 |
| 4 cm | 96 cm² | 64 cm³ | 1,5 |

> [!tip] Merke
> Je größer der Würfel, desto günstiger das Verhältnis von Volumen zu Oberfläche. Das erklärt, warum große Tiere relativ weniger Wärme verlieren als kleine.

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Volumen | $V = a^3$ |
> | Oberfläche | $O = 6a^2$ |
> | Flächendiagonale | $d_F = a\sqrt{2}$ |
> | Raumdiagonale | $d_R = a\sqrt{3}$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Ein Würfel hat die Kantenlänge 7 cm. Berechnen Sie:
> a) das Volumen
> b) die Oberfläche
> c) die Raumdiagonale

> [!question] Aufgabe 2
> Ein Aquarium in Würfelform fasst 125 Liter. Welche Kantenlänge hat es?

> [!question] Aufgabe 3
> Wie ändert sich das Volumen eines Würfels, wenn man die Kantenlänge verdoppelt?

> [!question] Aufgabe 4
> Ein Würfel hat eine Raumdiagonale von 12 cm. Wie lang ist eine Kante?

---

**Navigation:** [[01-Dreidimensionale-Koerper|← Dreidimensionale Körper]] | [[03-Quader|Quader →]]
