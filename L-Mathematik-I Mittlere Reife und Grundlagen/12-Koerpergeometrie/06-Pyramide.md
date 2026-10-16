---
title: Die Pyramide
chapter: "12"
section: "12.6"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - pyramide
  - volumen
  - oberflaeche
---

# Die Pyramide

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften verschiedener Pyramiden beschreiben
> - Das Volumen einer Pyramide berechnen
> - Die Oberfläche einer Pyramide berechnen
> - Körperhöhe und Seitenhöhe unterscheiden

## Definition und Eigenschaften

### Was ist eine Pyramide?

> [!note] Definition
> Eine **Pyramide** ist ein Körper mit:
> - Einer vieleckigen Grundfläche
> - Dreieckigen Seitenflächen, die in einem gemeinsamen Punkt (Spitze) zusammenlaufen

### Bezeichnungen

| Begriff | Bedeutung |
|---------|-----------|
| Grundfläche $G$ | Vieleck am Boden |
| Spitze $S$ | Oberer Endpunkt |
| Körperhöhe $h$ | Senkrechter Abstand Spitze – Grundfläche |
| Seitenhöhe $h_s$ | Höhe einer Seitenfläche (im Dreieck) |
| Seitenkante | Kante von Grundflächenecke zur Spitze |

### Arten von Pyramiden

**Nach der Grundfläche:**
- Dreieckige Pyramide (Tetraeder)
- Quadratische Pyramide (häufigste Form)
- Fünfeckige, sechseckige Pyramide, ...

**Nach der Ausrichtung:**
- **Gerade Pyramide:** Spitze liegt senkrecht über dem Mittelpunkt der Grundfläche
- **Schiefe Pyramide:** Spitze ist seitlich verschoben

## Volumen der Pyramide

### Formel

> [!note] Volumenformel
> $$V = \frac{1}{3} \cdot G \cdot h$$
> Das Volumen einer Pyramide ist **ein Drittel** des Volumens eines Prismas mit gleicher Grundfläche und Höhe.

### Herleitung

Drei kongruente Pyramiden mit quadratischer Grundfläche können zu einem Würfel zusammengesetzt werden. Daher:
$$V_{Pyramide} = \frac{1}{3} \cdot V_{Würfel} = \frac{1}{3} \cdot G \cdot h$$

### Beispielrechnungen

> [!example] Beispiel 1: Quadratische Pyramide
> Eine Pyramide hat eine quadratische Grundfläche mit Seitenlänge 6 cm und eine Höhe von 8 cm.
> 
> **Lösung:**
> $$G = 6^2 = 36 \text{ cm}^2$$
> $$V = \frac{1}{3} \cdot 36 \cdot 8 = 96 \text{ cm}^3$$

> [!example] Beispiel 2: Dreieckige Pyramide (Tetraeder)
> Ein regelmäßiges Tetraeder hat die Kantenlänge $a = 5$ cm.
> 
> **Lösung:**
> 1. Grundfläche (gleichseitiges Dreieck): $G = \frac{\sqrt{3}}{4} \cdot 5^2 = \frac{25\sqrt{3}}{4} \approx 10{,}83 \text{ cm}^2$
> 2. Höhe des Tetraeders: $h = a \cdot \sqrt{\frac{2}{3}} = 5 \cdot \sqrt{\frac{2}{3}} \approx 4{,}08 \text{ cm}$
> 3. Volumen: $V = \frac{1}{3} \cdot 10{,}83 \cdot 4{,}08 \approx 14{,}73 \text{ cm}^3$

## Oberfläche der Pyramide

### Bestandteile

Die Oberfläche besteht aus:
1. **Grundfläche** $G$
2. **Mantelfläche** $M$ (Summe der dreieckigen Seitenflächen)

### Formel

> [!note] Oberflächenformel
> $$O = G + M$$
> 
> Für eine gerade Pyramide mit regelmäßiger Grundfläche:
> $$M = \frac{1}{2} \cdot U \cdot h_s$$
> wobei $U$ = Umfang der Grundfläche, $h_s$ = Seitenhöhe

### Seitenhöhe berechnen

Mit dem [[11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]]:

> [!note] Seitenhöhe (quadratische Pyramide)
> $$h_s = \sqrt{h^2 + \left(\frac{a}{2}\right)^2}$$
> wobei $a$ = Seitenlänge der quadratischen Grundfläche

### Beispielrechnungen

> [!example] Beispiel 3: Oberfläche berechnen
> Eine quadratische Pyramide hat $a = 10$ cm Grundseitenlänge und $h = 12$ cm Körperhöhe.
> 
> **Lösung:**
> 1. Grundfläche: $G = 10^2 = 100 \text{ cm}^2$
> 2. Seitenhöhe: $h_s = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13 \text{ cm}$
> 3. Mantelfläche: $M = 4 \cdot \frac{1}{2} \cdot 10 \cdot 13 = 260 \text{ cm}^2$
> 4. Oberfläche: $O = 100 + 260 = 360 \text{ cm}^2$

## Körperhöhe vs. Seitenhöhe

### Unterschied

- **Körperhöhe $h$:** Senkrecht von der Spitze zur Grundfläche
- **Seitenhöhe $h_s$:** Höhe einer Seitenfläche (schräg)
- **Seitenkante $s$:** Kante von Grundflächenecke zur Spitze

### Zusammenhang (quadratische Pyramide)

```
      Spitze
        /|\
       / | \
      /  |h \
     /   |   \
    /____|____\
    |    |    |
    a/2      a/2
    
    h_s² = h² + (a/2)²
```

> [!example] Beispiel 4: Alle Maße berechnen
> Eine quadratische Pyramide hat $a = 8$ cm und $s = 10$ cm (Seitenkante).
> 
> **Lösung:**
> 1. Halbe Grundflächendiagonale: $d/2 = \frac{8\sqrt{2}}{2} = 4\sqrt{2} \approx 5{,}66$ cm
> 2. Körperhöhe: $h = \sqrt{s^2 - (d/2)^2} = \sqrt{100 - 32} = \sqrt{68} \approx 8{,}25$ cm
> 3. Seitenhöhe: $h_s = \sqrt{h^2 + (a/2)^2} = \sqrt{68 + 16} = \sqrt{84} \approx 9{,}17$ cm

## Praktische Anwendungen

### Ägyptische Pyramiden

> [!example] Beispiel 5: Cheops-Pyramide
> Die Cheops-Pyramide hat eine quadratische Grundfläche mit ca. 230 m Seitenlänge und eine Höhe von ca. 147 m (ursprünglich).
> 
> **Volumen:**
> $$V = \frac{1}{3} \cdot 230^2 \cdot 147 = \frac{1}{3} \cdot 52.900 \cdot 147 \approx 2{,}59 \text{ Millionen m}^3$$

### Dächer

> [!example] Beispiel 6: Pyramidendach
> Ein Turm hat ein quadratisches Pyramidendach mit 4 m Seitenlänge und 3 m Höhe.
> 
> a) **Seitenhöhe:**
> $$h_s = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3{,}61 \text{ m}$$
> 
> b) **Dachfläche (Mantelfläche):**
> $$M = 4 \cdot \frac{1}{2} \cdot 4 \cdot 3{,}61 \approx 28{,}84 \text{ m}^2$$

### Hohlpyramiden

> [!example] Beispiel 7: Pyramiden-Verpackung
> Eine dekorative Verpackung ist eine hohle quadratische Pyramide mit $a = 12$ cm und $h = 16$ cm.
> 
> **Innenvolumen:**
> $$V = \frac{1}{3} \cdot 12^2 \cdot 16 = \frac{1}{3} \cdot 144 \cdot 16 = 768 \text{ cm}^3$$
> 
> **Materialbedarf (Oberfläche):**
> $$h_s = \sqrt{16^2 + 6^2} = \sqrt{292} \approx 17{,}09 \text{ cm}$$
> $$O = 144 + 4 \cdot \frac{1}{2} \cdot 12 \cdot 17{,}09 = 144 + 410{,}2 \approx 554 \text{ cm}^2$$

## Pyramidenstumpf

### Definition

Ein Pyramidenstumpf entsteht, wenn man eine Pyramide parallel zur Grundfläche schneidet und die Spitze entfernt.

### Volumenformel

> [!note] Pyramidenstumpf
> $$V = \frac{h}{3} \cdot (G_1 + G_2 + \sqrt{G_1 \cdot G_2})$$
> wobei $G_1$ = Grundfläche unten, $G_2$ = Grundfläche oben

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Volumen | $V = \frac{1}{3} \cdot G \cdot h$ |
> | Mantelfläche | $M = \frac{1}{2} \cdot U \cdot h_s$ |
> | Oberfläche | $O = G + M$ |
> | Seitenhöhe (quadr.) | $h_s = \sqrt{h^2 + (a/2)^2}$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Eine quadratische Pyramide hat die Grundseitenlänge 9 cm und die Höhe 12 cm. Berechnen Sie:
> a) das Volumen
> b) die Seitenhöhe
> c) die Oberfläche

> [!question] Aufgabe 2
> Eine Pyramide hat eine rechteckige Grundfläche (6 cm × 8 cm) und das Volumen 160 cm³. Wie hoch ist sie?

> [!question] Aufgabe 3
> Ein Zelt hat die Form einer quadratischen Pyramide mit 3 m Seitenlänge und 2,5 m Höhe. Wie viel Stoff wird für die Zeltplane (nur Mantelfläche) benötigt?

> [!question] Aufgabe 4
> Eine Pyramide mit quadratischer Grundfläche hat die Seitenkante 13 cm und die Körperhöhe 12 cm. Wie lang ist die Grundseitenlänge?

---

**Navigation:** [[05-Zylinder|← Zylinder]] | [[07-Kegel|Kegel →]]
