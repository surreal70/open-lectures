---
title: "Anwendungen des Satzes des Pythagoras"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "04"
status: "draft - review pending"
type: lecture
keywords:
  - Anwendung
  - Raumdiagonale
  - Flächen
  - Koordinaten
---

# Anwendungen des Satzes des Pythagoras

> [!info] Lernziele
> - Den Satz des Pythagoras auf praktische Probleme anwenden
> - Räumliche Probleme auf ebene Dreiecke zurückführen
> - Die Raumdiagonale berechnen können
> - Sachaufgaben systematisch lösen

## Diagonalen

### Diagonale im Rechteck

$$d = \sqrt{l^2 + b^2}$$

### Diagonale im Quadrat

$$d = a\sqrt{2}$$

### Raumdiagonale im Quader

```
        ┌─────────────────┐
       ╱│                ╱│
      ╱ │               ╱ │
     ╱  │       d      ╱  │
    ┌───│─────────────┐   │ c
    │   │             │   │
    │   └─────────────│───┘
    │  ╱              │  ╱
    │ ╱               │ ╱  b
    │╱                │╱
    └─────────────────┘
            a
```

$$d = \sqrt{a^2 + b^2 + c^2}$$

> [!example] Beispiel
> Quader mit $a = 3$ cm, $b = 4$ cm, $c = 12$ cm
> 
> $d = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$ cm

### Raumdiagonale im Würfel

$$d = a\sqrt{3}$$

## Höhenberechnung im gleichschenkligen Dreieck

```
           A
          ╱╲
         ╱  ╲
        ╱    ╲   a
       ╱  h   ╲
      ╱   │    ╲
     ╱____|____╲
    B     M     C
        c/2
```

Die Höhe $h$ im gleichschenkligen Dreieck:

$$h = \sqrt{a^2 - \left(\frac{c}{2}\right)^2}$$

> [!example] Beispiel
> Gleichschenkliges Dreieck mit $a = 5$ cm, $c = 6$ cm
> 
> $h = \sqrt{25 - 9} = \sqrt{16} = 4$ cm

## Höhe im gleichseitigen Dreieck

Im gleichseitigen Dreieck mit Seitenlänge $a$:

$$h = \frac{a\sqrt{3}}{2}$$

## Praktische Anwendungen

### Baugerüste und Leitern

> [!example] Beispiel
> Eine Leiter soll bis zu einem 4 m hohen Fenster reichen. Der Neigungswinkel erfordert einen Fußabstand von 1,5 m. Wie lang muss die Leiter sein?
> 
> $$l = \sqrt{4^2 + 1{,}5^2} = \sqrt{16 + 2{,}25} = \sqrt{18{,}25} \approx 4{,}27 \text{ m}$$

### Dachkonstruktionen

> [!example] Beispiel
> Ein Satteldach hat eine Spannweite von 10 m und eine Firsthöhe von 3 m. Wie lang ist eine Dachseite?
> 
> Halbe Spannweite: $5$ m
> 
> $$d = \sqrt{5^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34} \approx 5{,}83 \text{ m}$$

### Abstände im Koordinatensystem

Abstand zweier Punkte $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Im dreidimensionalen Raum mit $P_1(x_1, y_1, z_1)$ und $P_2(x_2, y_2, z_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

### Flächenberechnung mit Pythagoras

Wenn die Höhe nicht gegeben ist, kann sie oft mit Pythagoras berechnet werden.

> [!example] Beispiel: Fläche eines gleichschenkligen Dreiecks
> Seiten: $a = b = 10$ cm, $c = 12$ cm
> 
> **Höhe berechnen**:
> $h = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8$ cm
> 
> **Fläche**:
> $A = \frac{1}{2} \cdot 12 \cdot 8 = 48$ cm²

## Mehrfache Anwendung

Manchmal muss der Satz mehrfach angewendet werden.

> [!example] Beispiel: Höhe einer Pyramide
> Eine quadratische Pyramide hat eine Grundkante von 6 cm und eine Seitenkante von 5 cm.
> 
> **Schritt 1**: Halbe Diagonale der Grundfläche
> $d_{halb} = \frac{6\sqrt{2}}{2} = 3\sqrt{2} \approx 4{,}24$ cm
> 
> **Schritt 2**: Höhe berechnen
> $h = \sqrt{5^2 - (3\sqrt{2})^2} = \sqrt{25 - 18} = \sqrt{7} \approx 2{,}65$ cm

## Zusammenfassung

> [!abstract] Kernpunkte
> - Rechteckdiagonale: $d = \sqrt{l^2 + b^2}$
> - Raumdiagonale Quader: $d = \sqrt{a^2 + b^2 + c^2}$
> - Höhe im gleichschenkligen Dreieck durch Pythagoras berechenbar
> - Koordinatenabstand: Differenzen quadrieren und Wurzel ziehen
> - Bei komplexen Aufgaben: Problem in Teilprobleme zerlegen

## Übungsaufgaben

1. Berechne die Raumdiagonale eines Quaders mit den Maßen 8 cm × 6 cm × 24 cm.

2. Ein gleichseitiges Dreieck hat die Seitenlänge 12 cm. Berechne die Höhe.

3. Wie weit sind die Punkte $A(3, 1)$ und $B(7, 4)$ voneinander entfernt?

4. Ein Fernseher hat die Maße 80 cm × 60 cm. Wie groß ist die Bildschirmdiagonale?

5. Ein Schrank (80 × 50 × 200 cm) soll durch eine Tür (90 × 210 cm) getragen werden. Passt der Schrank diagonal durch die Tür?

---

**Navigation**: [[03-Berechnung-unbekannter-Seiten|← Berechnung]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[05-Einfuehrung-Trigonometrie|Trigonometrie →]]
