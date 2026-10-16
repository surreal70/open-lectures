---
title: Der Kegel
chapter: "12"
section: "12.7"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - kegel
  - volumen
  - oberflaeche
---

# Der Kegel

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften des Kegels beschreiben
> - Das Volumen eines Kegels berechnen
> - Mantelfläche und Oberfläche berechnen
> - Mantellinie (Seitenlinie) bestimmen
> - Praktische Aufgaben mit Kegeln lösen

## Definition und Eigenschaften

### Was ist ein Kegel?

> [!note] Definition
> Ein **Kreiskegel** (oder kurz Kegel) ist ein Körper mit:
> - Einer kreisförmigen Grundfläche
> - Einer gekrümmten Mantelfläche, die in einem Punkt (Spitze) zusammenläuft

### Bezeichnungen

| Symbol | Bedeutung |
|--------|-----------|
| $r$ | Radius der Grundfläche |
| $h$ | Körperhöhe (senkrecht) |
| $s$ | Mantellinie (Seitenlinie) |
| $G$ | Grundfläche |
| $M$ | Mantelfläche |

> [!tip] Kegel als "runde Pyramide"
> Der Kegel verhält sich zur [[06-Pyramide|Pyramide]] wie der Kreis zum Vieleck. Die Volumenformel ist identisch aufgebaut.

### Zusammenhang der Maße

Mit dem [[11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]]:

> [!note] Mantellinie
> $$s = \sqrt{r^2 + h^2}$$

```
      Spitze
        /|\
       / | \
      /  |h \ s
     /   |   \
    /____|____\
         r
```

## Volumen des Kegels

### Formel

> [!note] Volumenformel
> $$V = \frac{1}{3} \cdot \pi r^2 \cdot h = \frac{1}{3} \cdot G \cdot h$$
> Das Volumen eines Kegels ist **ein Drittel** des Volumens eines Zylinders mit gleicher Grundfläche und Höhe.

### Beispielrechnungen

> [!example] Beispiel 1: Volumen berechnen
> Ein Kegel hat den Radius $r = 5$ cm und die Höhe $h = 12$ cm.
> 
> **Lösung:**
> $$V = \frac{1}{3} \cdot \pi \cdot 5^2 \cdot 12 = \frac{1}{3} \cdot 25\pi \cdot 12 = 100\pi \approx 314{,}2 \text{ cm}^3$$

> [!example] Beispiel 2: Mit Durchmesser
> Eine Eistüte hat 4 cm Durchmesser und 12 cm Höhe.
> 
> **Lösung:**
> $$r = 2 \text{ cm}$$
> $$V = \frac{1}{3} \cdot \pi \cdot 2^2 \cdot 12 = 16\pi \approx 50{,}3 \text{ cm}^3 = 50{,}3 \text{ ml}$$

### Fehlende Größen berechnen

> [!example] Beispiel 3: Höhe berechnen
> Ein Kegel hat das Volumen 500 cm³ und den Radius 6 cm. Wie hoch ist er?
> 
> **Lösung:**
> $$V = \frac{1}{3} \pi r^2 h$$
> $$500 = \frac{1}{3} \pi \cdot 36 \cdot h$$
> $$h = \frac{500 \cdot 3}{36\pi} = \frac{1500}{36\pi} \approx 13{,}26 \text{ cm}$$

> [!example] Beispiel 4: Radius berechnen
> Ein Kegel hat das Volumen 200 cm³ und die Höhe 8 cm. Wie groß ist der Radius?
> 
> **Lösung:**
> $$200 = \frac{1}{3} \pi r^2 \cdot 8$$
> $$r^2 = \frac{200 \cdot 3}{8\pi} = \frac{75}{\pi} \approx 23{,}87$$
> $$r \approx 4{,}89 \text{ cm}$$

## Oberfläche des Kegels

### Mantelfläche

Die abgewickelte Mantelfläche ist ein Kreissektor:

> [!note] Mantelflächenformel
> $$M = \pi \cdot r \cdot s$$
> wobei $s = \sqrt{r^2 + h^2}$ die Mantellinie ist.

### Gesamtoberfläche

> [!note] Oberflächenformel
> $$O = \pi r^2 + \pi rs = \pi r(r + s)$$

### Beispielrechnungen

> [!example] Beispiel 5: Oberfläche berechnen
> Ein Kegel hat $r = 3$ cm und $h = 4$ cm.
> 
> **Lösung:**
> 1. Mantellinie: $s = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$ cm
> 2. Mantelfläche: $M = \pi \cdot 3 \cdot 5 = 15\pi \approx 47{,}1 \text{ cm}^2$
> 3. Oberfläche: $O = \pi \cdot 3 \cdot (3 + 5) = 24\pi \approx 75{,}4 \text{ cm}^2$

> [!example] Beispiel 6: Mantellinie gegeben
> Ein Kegel hat $r = 7$ cm und $s = 25$ cm.
> 
> **Lösung:**
> 1. Höhe: $h = \sqrt{s^2 - r^2} = \sqrt{625 - 49} = \sqrt{576} = 24$ cm
> 2. Volumen: $V = \frac{1}{3} \pi \cdot 49 \cdot 24 = 392\pi \approx 1231{,}5 \text{ cm}^3$
> 3. Oberfläche: $O = \pi \cdot 7 \cdot (7 + 25) = 224\pi \approx 703{,}7 \text{ cm}^2$

## Kegelnetz

### Aufbau

Ein Kegelnetz besteht aus:
- 1 Kreis (Grundfläche) mit Radius $r$
- 1 Kreissektor (abgewickelte Mantelfläche) mit Radius $s$ und Bogenlänge $2\pi r$

### Öffnungswinkel des Sektors

$$\alpha = \frac{r}{s} \cdot 360° = \frac{2\pi r}{s} \cdot \frac{180°}{\pi} = \frac{360° \cdot r}{s}$$

> [!example] Beispiel 7: Kegelnetz konstruieren
> Ein Kegel hat $r = 4$ cm und $s = 10$ cm.
> 
> **Öffnungswinkel des Kreissektors:**
> $$\alpha = \frac{360° \cdot 4}{10} = 144°$$

## Praktische Anwendungen

### Eistüten

> [!example] Beispiel 8: Waffeleis
> Eine Eiswaffel hat 5 cm Durchmesser am oberen Rand und ist 14 cm tief.
> 
> a) **Fassungsvermögen:**
> $$V = \frac{1}{3} \pi \cdot 2{,}5^2 \cdot 14 = \frac{1}{3} \cdot 6{,}25\pi \cdot 14 \approx 91{,}6 \text{ cm}^3$$
> 
> b) **Waffelfläche (Mantelfläche):**
> $$s = \sqrt{2{,}5^2 + 14^2} = \sqrt{202{,}25} \approx 14{,}22 \text{ cm}$$
> $$M = \pi \cdot 2{,}5 \cdot 14{,}22 \approx 111{,}7 \text{ cm}^2$$

### Sandhaufen und Schüttgut

> [!example] Beispiel 9: Sandhaufen
> Ein kegelförmiger Sandhaufen hat einen Durchmesser von 6 m und eine Höhe von 2 m.
> 
> **Sandvolumen:**
> $$V = \frac{1}{3} \pi \cdot 3^2 \cdot 2 = 6\pi \approx 18{,}85 \text{ m}^3$$
> 
> Bei 1,5 t/m³ Schüttdichte:
> $$m = 18{,}85 \cdot 1{,}5 \approx 28{,}3 \text{ Tonnen}$$

### Trichter

> [!example] Beispiel 10: Öltrichter
> Ein Trichter hat oben 12 cm Durchmesser, unten 2 cm Durchmesser und ist 15 cm tief (Kegelstumpf).
> 
> **Näherung als Kegel (ohne untere Öffnung):**
> $$V \approx \frac{1}{3} \pi \cdot 6^2 \cdot 15 = 180\pi \approx 565 \text{ cm}^3$$

## Kegelstumpf

### Definition

Ein Kegelstumpf entsteht, wenn man einen Kegel parallel zur Grundfläche schneidet und die Spitze entfernt.

### Volumenformel

> [!note] Kegelstumpf
> $$V = \frac{\pi h}{3} \cdot (r_1^2 + r_1 r_2 + r_2^2)$$
> wobei $r_1$ = Radius unten, $r_2$ = Radius oben

> [!example] Beispiel 11: Blumentopf
> Ein Blumentopf (Kegelstumpf) hat unten 8 cm, oben 12 cm Durchmesser und ist 15 cm hoch.
> 
> **Fassungsvermögen:**
> $$V = \frac{\pi \cdot 15}{3} \cdot (4^2 + 4 \cdot 6 + 6^2)$$
> $$V = 5\pi \cdot (16 + 24 + 36) = 5\pi \cdot 76 = 380\pi \approx 1194 \text{ cm}^3 \approx 1{,}2 \text{ Liter}$$

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Mantellinie | $s = \sqrt{r^2 + h^2}$ |
> | Volumen | $V = \frac{1}{3} \pi r^2 h$ |
> | Mantelfläche | $M = \pi r s$ |
> | Oberfläche | $O = \pi r(r + s)$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Ein Kegel hat den Radius 6 cm und die Höhe 8 cm. Berechnen Sie:
> a) die Mantellinie
> b) das Volumen
> c) die Oberfläche

> [!question] Aufgabe 2
> Eine kegelförmige Sanduhr enthält 150 cm³ Sand. Der Radius beträgt 3 cm. Wie hoch steht der Sand?

> [!question] Aufgabe 3
> Ein Partyhut (Kegel) soll aus Pappe hergestellt werden. Der Radius soll 8 cm und die Höhe 20 cm betragen. Wie viel cm² Pappe werden benötigt?

> [!question] Aufgabe 4
> Ein Kegelstumpf hat die Radien 5 cm (unten) und 3 cm (oben) bei einer Höhe von 10 cm. Berechnen Sie das Volumen.

---

**Navigation:** [[06-Pyramide|← Pyramide]] | [[08-Kugel|Kugel →]]
