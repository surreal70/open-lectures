---
title: "Flächenberechnungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "08"
status: "draft - review pending"
type: lecture
keywords:
  - Fläche
  - Flächeninhalt
  - Dreieck
  - Viereck
  - Kreis
---

# Flächenberechnungen

> [!info] Lernziele
> - Flächeninhalte grundlegender Figuren berechnen
> - Die richtigen Formeln anwenden
> - Zusammengesetzte Flächen berechnen
> - Einheiten korrekt verwenden

## Der Begriff Flächeninhalt

Der **Flächeninhalt** gibt an, wie viel „Platz" eine ebene Figur einnimmt.

### Flächeneinheiten

| Einheit | Abkürzung | Umrechnung |
|---|---|---|
| Quadratmillimeter | mm² | 1 mm² |
| Quadratzentimeter | cm² | 1 cm² = 100 mm² |
| Quadratdezimeter | dm² | 1 dm² = 100 cm² |
| Quadratmeter | m² | 1 m² = 100 dm² |
| Ar | a | 1 a = 100 m² |
| Hektar | ha | 1 ha = 100 a = 10.000 m² |
| Quadratkilometer | km² | 1 km² = 100 ha |

## Rechteck und Quadrat

### Rechteck

$$A = l \cdot b$$

wobei $l$ = Länge und $b$ = Breite

> [!example] Beispiel
> Rechteck mit $l = 8$ cm, $b = 5$ cm
> 
> $A = 8 \cdot 5 = 40$ cm²

### Quadrat

$$A = a^2$$

> [!example] Beispiel
> Quadrat mit $a = 6$ cm
> 
> $A = 6^2 = 36$ cm²

## Parallelogramm

$$A = g \cdot h$$

wobei $g$ = Grundseite und $h$ = Höhe (senkrecht zur Grundseite!)

```
        ┌─────────────┐
       ╱│            ╱
      ╱ │h          ╱
     ╱  │          ╱
    └───┴─────────┘
         g
```

> [!warning] Achtung
> Die Höhe $h$ ist **nicht** die Seitenlänge, sondern der senkrechte Abstand!

## Dreieck

$$A = \frac{1}{2} \cdot g \cdot h = \frac{g \cdot h}{2}$$

```
           C
          /|\
         / | \
        /  |h \
       /   |   \
      /___ |____\
     A     F     B
         g
```

> [!tip] Merkregel
> Das Dreieck ist das „halbe Parallelogramm".

> [!example] Beispiel
> Dreieck mit $g = 10$ cm, $h = 6$ cm
> 
> $A = \frac{10 \cdot 6}{2} = 30$ cm²

## Trapez

$$A = \frac{1}{2}(a + c) \cdot h = \frac{(a + c) \cdot h}{2}$$

wobei $a$ und $c$ die parallelen Seiten und $h$ die Höhe ist.

```
        ┌───c───┐
       ╱│       │╲
      ╱ │h      │ ╲
     ╱  │       │  ╲
    └───┴───────┴───┘
           a
```

> [!tip] Merkregel
> Mittelwert der parallelen Seiten mal Höhe.

> [!example] Beispiel
> Trapez mit $a = 12$ cm, $c = 6$ cm, $h = 4$ cm
> 
> $A = \frac{(12 + 6) \cdot 4}{2} = \frac{18 \cdot 4}{2} = 36$ cm²

## Raute und Drachen

$$A = \frac{e \cdot f}{2}$$

wobei $e$ und $f$ die Diagonalen sind.

> [!example] Beispiel
> Raute mit $e = 8$ cm, $f = 6$ cm
> 
> $A = \frac{8 \cdot 6}{2} = 24$ cm²

## Kreis

$$A = \pi \cdot r^2$$

> [!example] Beispiel
> Kreis mit $r = 5$ cm
> 
> $A = \pi \cdot 25 = 25\pi \approx 78{,}54$ cm²

### Kreissektor

$$A = \frac{\alpha}{360°} \cdot \pi r^2$$

### Kreisring

$$A = \pi(R^2 - r^2)$$

## Zusammengesetzte Flächen

### Strategie 1: Zerlegung

Die Figur in bekannte Teilfiguren zerlegen und die Flächen addieren.

### Strategie 2: Ergänzung

Die Figur zu einer einfacheren ergänzen und dann subtrahieren.

> [!example] Beispiel: L-Form
> ```
>     ┌───────────┐
>     │           │
>     │     ┌─────┘
>     │     │
>     │     │
>     └─────┘
> ```
> 
> Gesamtrechteck: $12 \times 8 = 96$ cm²
> Minus Ausschnitt: $6 \times 4 = 24$ cm²
> **Fläche: $96 - 24 = 72$ cm²**

## Formelübersicht

| Figur | Flächenformel |
|---|---|
| Rechteck | $A = l \cdot b$ |
| Quadrat | $A = a^2$ |
| Parallelogramm | $A = g \cdot h$ |
| Dreieck | $A = \frac{g \cdot h}{2}$ |
| Trapez | $A = \frac{(a+c) \cdot h}{2}$ |
| Raute/Drachen | $A = \frac{e \cdot f}{2}$ |
| Kreis | $A = \pi r^2$ |
| Kreissektor | $A = \frac{\alpha}{360°} \cdot \pi r^2$ |

## Rückwärtsrechnen

> [!example] Beispiel: Seite aus Fläche
> Ein Quadrat hat die Fläche 81 cm². Wie lang ist die Seite?
> 
> $$a = \sqrt{A} = \sqrt{81} = 9 \text{ cm}$$

> [!example] Beispiel: Höhe aus Fläche
> Ein Dreieck hat $A = 24$ cm² und $g = 8$ cm. Wie hoch ist es?
> 
> $$h = \frac{2A}{g} = \frac{2 \cdot 24}{8} = 6 \text{ cm}$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Flächeninhalt = „Platz" einer ebenen Figur
> - Grundformel Rechteck: Länge × Breite
> - Dreieck: halbes Rechteck (mit gleicher Grundseite und Höhe)
> - Trapez: Mittelwert der parallelen Seiten × Höhe
> - Kreis: $\pi r^2$
> - Zusammengesetzte Flächen: zerlegen oder ergänzen

## Übungsaufgaben

1. Berechne die Fläche:
   - Rechteck: $l = 15$ cm, $b = 8$ cm
   - Dreieck: $g = 12$ cm, $h = 9$ cm
   - Trapez: $a = 10$ cm, $c = 6$ cm, $h = 4$ cm
   - Kreis: $r = 7$ cm

2. Bestimme die fehlende Größe:
   - Quadrat mit $A = 144$ cm²
   - Rechteck mit $A = 60$ cm² und $l = 10$ cm
   - Dreieck mit $A = 35$ cm² und $h = 7$ cm

3. Eine L-förmige Fläche besteht aus zwei Rechtecken: $10 \times 4$ cm und $6 \times 3$ cm (überlappend). Berechne die Gesamtfläche.

4. Ein Grundstück hat die Form eines Rechtecks ($40 \times 30$ m) mit einem kreisförmigen Teich ($r = 5$ m). Wie groß ist die bepflanzbare Fläche?

5. Ein Fußballfeld ($100 \times 70$ m) soll mit Rollrasen belegt werden. Der Rasen kostet 8 € pro m². Was kostet der Rasen?

---

**Navigation**: [[07-Umfangsberechnungen|← Umfang]] | [[00-Geometrie-Index|Übersicht]] | [[09-Symmetrie|Symmetrie →]]
