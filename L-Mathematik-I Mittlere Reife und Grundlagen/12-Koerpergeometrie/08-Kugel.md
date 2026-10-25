---
title: Die Kugel
chapter: "12"
section: "12.8"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - kugel
  - volumen
  - oberflaeche
---

# Die Kugel

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften der Kugel beschreiben
> - Das Volumen einer Kugel berechnen
> - Die Oberfläche einer Kugel berechnen
> - Praktische Aufgaben mit Kugeln lösen

## Definition und Eigenschaften

### Was ist eine Kugel?

> [!note] Definition
> Eine **Kugel** ist die Menge aller Punkte im Raum, die von einem festen Punkt (Mittelpunkt) den gleichen Abstand (Radius) haben.

![[kugel-3d.png]]
*<span class="fig-id">12-08-kugel-3d</span>: Schrägbild einer Kugel mit Radius $r$ vom Mittelpunkt zur Oberfläche. Der hintere Teil des Äquators ist gestrichelt dargestellt.*

Die Kugel ist der perfekteste aller Körper – sie hat keine Ecken, keine Kanten, keine ausgezeichnete Richtung. In der Natur entstehen Kugeln überall dort, wo Kräfte gleichmäßig aus allen Richtungen wirken: Seifenblasen, Wassertropfen im freien Fall, Planeten und Sterne. 

Der griechische Mathematiker Archimedes (287–212 v. Chr.) war so stolz auf seine Entdeckung des Zusammenhangs zwischen Kugel und Zylinder, dass er wünschte, eine Kugel in einem Zylinder auf seinem Grabstein abgebildet zu bekommen. Er hatte bewiesen, dass eine Kugel genau zwei Drittel des Volumens eines umschriebenen Zylinders einnimmt.

### Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Mittelpunkt | Zentrum der Kugel |
| Radius $r$ | Abstand vom Mittelpunkt zur Oberfläche |
| Durchmesser $d$ | $d = 2r$ |
| Symmetrie | Unendlich viele Symmetrieachsen |

> [!tip] Die Kugel ist besonders
> Die Kugel ist der Körper mit dem kleinsten Oberflächen-zu-Volumen-Verhältnis. Bei gleichem Volumen hat die Kugel die kleinste Oberfläche.

> [!info] **Warum ist die Kugel so effizient?**
> Die Kugel minimiert die Oberfläche bei gegebenem Volumen – das ist ein mathematisches Optimum! Deshalb sind Seifenblasen kugelförmig (minimale Oberflächenspannung), Planeten kugelförmig (Gravitation wirkt gleichmäßig) und Wassertropfen im Weltraum kugelförmig (keine Schwerkraft, nur Oberflächenspannung).

## Volumen der Kugel

### Formel

> [!note] Volumenformel
> $$V = \frac{4}{3} \pi r^3$$
> 
> Mit Durchmesser:
> $$V = \frac{\pi d^3}{6}$$

Diese Formel wurde von Archimedes entdeckt. Er bewies, dass das Volumen einer Kugel genau zwei Drittel des Volumens eines umschriebenen Zylinders (gleicher Radius, Höhe = Durchmesser) beträgt. Dieser Zusammenhang war ihm so wichtig, dass er ihn auf seinem Grabstein verewigen ließ.

> [!tip] **Merkregel für die Kugelformel**
> Die Kugelformel enthält drei „magische" Elemente: $\frac{4}{3}$, $\pi$ und $r^3$. 
> - Der Faktor $\frac{4}{3}$ kommt aus der Integration (höhere Mathematik)
> - $\pi$ erscheint, weil Kreise beteiligt sind
> - $r^3$ zeigt, dass es ein Volumen ist (dritte Potenz)

### Beispielrechnungen

> [!example] Beispiel 1: Volumen berechnen
> Eine Kugel hat den Radius $r = 6$ cm.
> 
> **Lösung:**
> $$V = \frac{4}{3} \pi \cdot 6^3 = \frac{4}{3} \pi \cdot 216 = 288\pi \approx 904{,}8 \text{ cm}^3$$

> [!example] Beispiel 2: Mit Durchmesser
> Ein Fußball hat 22 cm Durchmesser.
> 
> **Lösung:**
> $$r = 11 \text{ cm}$$
> $$V = \frac{4}{3} \pi \cdot 11^3 = \frac{4}{3} \pi \cdot 1331 \approx 5575{,}3 \text{ cm}^3 \approx 5{,}6 \text{ Liter}$$

### Radius aus Volumen

> [!example] Beispiel 3: Radius berechnen
> Eine Kugel hat das Volumen 500 cm³. Wie groß ist der Radius?
> 
> **Lösung:**
> $$V = \frac{4}{3} \pi r^3$$
> $$500 = \frac{4}{3} \pi r^3$$
> $$r^3 = \frac{500 \cdot 3}{4\pi} = \frac{1500}{4\pi} \approx 119{,}4$$
> $$r = \sqrt[3]{119{,}4} \approx 4{,}92 \text{ cm}$$

## Oberfläche der Kugel

### Formel

> [!note] Oberflächenformel
> $$O = 4\pi r^2$$
> 
> Mit Durchmesser:
> $$O = \pi d^2$$

> [!tip] Zusammenhang
> Die Oberfläche einer Kugel ist genau **viermal** so groß wie die Fläche eines Kreises mit gleichem Radius (Großkreis).

### Beispielrechnungen

> [!example] Beispiel 4: Oberfläche berechnen
> Eine Kugel hat den Radius $r = 5$ cm.
> 
> **Lösung:**
> $$O = 4\pi \cdot 5^2 = 100\pi \approx 314{,}2 \text{ cm}^2$$

> [!example] Beispiel 5: Radius aus Oberfläche
> Eine Kugel hat die Oberfläche 200 cm². Wie groß ist der Radius?
> 
> **Lösung:**
> $$O = 4\pi r^2$$
> $$200 = 4\pi r^2$$
> $$r^2 = \frac{200}{4\pi} = \frac{50}{\pi} \approx 15{,}92$$
> $$r \approx 3{,}99 \text{ cm}$$

## Zusammenhang Volumen und Oberfläche

### Verhältnis

$$\frac{V}{O} = \frac{\frac{4}{3}\pi r^3}{4\pi r^2} = \frac{r}{3}$$

> [!tip] Bedeutung
> Je größer die Kugel, desto günstiger das Verhältnis. Das erklärt, warum:
> - Große Tiere weniger Wärme verlieren
> - Wassertropfen kugelförmig sind (minimale Oberfläche)
> - Planeten und Sterne kugelförmig sind

### Vergleich mit anderen Körpern

Bei gleichem Volumen von 1000 cm³:

| Körper | Oberfläche |
|--------|------------|
| Kugel | ca. 483 cm² |
| Würfel | 600 cm² |
| Quader (2:1:0,5) | ca. 848 cm² |

## Kugelteile

### Halbkugel

> [!note] Halbkugel
> **Volumen:** $V = \frac{2}{3}\pi r^3$
> 
> **Oberfläche:** $O = 3\pi r^2$ (Mantelfläche + Schnittfläche)

### Kugelkappe (Kugelabschnitt)

Eine Kugelkappe entsteht, wenn man eine Kugel mit einer Ebene schneidet.

> [!note] Kugelkappe
> **Volumen:** $V = \frac{\pi h^2}{3}(3r - h)$
> 
> wobei $h$ = Höhe der Kappe, $r$ = Kugelradius

### Kugelschicht (Kugelzone)

Der Teil einer Kugel zwischen zwei parallelen Schnitten.

## Praktische Anwendungen

### Sport

> [!example] Beispiel 6: Bälle
> | Ball | Durchmesser | Volumen |
> |------|-------------|---------|
> | Tischtennisball | 4 cm | ≈ 33,5 cm³ |
> | Tennisball | 6,7 cm | ≈ 157 cm³ |
> | Fußball | 22 cm | ≈ 5575 cm³ |
> | Basketball | 24 cm | ≈ 7238 cm³ |

### Erde und Planeten

> [!example] Beispiel 7: Erdkugel
> Die Erde hat einen mittleren Radius von etwa 6371 km.
> 
> **Volumen:**
> $$V = \frac{4}{3}\pi \cdot 6371^3 \approx 1{,}083 \cdot 10^{12} \text{ km}^3$$
> 
> **Oberfläche:**
> $$O = 4\pi \cdot 6371^2 \approx 510 \text{ Millionen km}^2$$

### Kugeltanks

> [!example] Beispiel 8: Gastank
> Ein kugelförmiger Gastank hat 3 m Durchmesser.
> 
> a) **Fassungsvermögen:**
> $$V = \frac{4}{3}\pi \cdot 1{,}5^3 = \frac{4}{3}\pi \cdot 3{,}375 = 4{,}5\pi \approx 14{,}14 \text{ m}^3$$
> 
> b) **Materialbedarf (Oberfläche):**
> $$O = 4\pi \cdot 1{,}5^2 = 9\pi \approx 28{,}27 \text{ m}^2$$

### Eiskugeln

> [!example] Beispiel 9: Eiskugel
> Eine Eiskugel hat 5 cm Durchmesser.
> 
> **Volumen:**
> $$V = \frac{4}{3}\pi \cdot 2{,}5^3 = \frac{4}{3}\pi \cdot 15{,}625 \approx 65{,}4 \text{ cm}^3$$
> 
> Wie viele Eiskugeln passen in einen Liter?
> $$n = \frac{1000}{65{,}4} \approx 15 \text{ Kugeln}$$

### Verpackung von Kugeln

> [!example] Beispiel 10: Kugeln im Karton
> Wie viele Tischtennisbälle (4 cm Durchmesser) passen in einen Karton von 40 cm × 32 cm × 24 cm?
> 
> **Lösung (kubische Packung):**
> - In der Länge: $40 \div 4 = 10$ Bälle
> - In der Breite: $32 \div 4 = 8$ Bälle
> - In der Höhe: $24 \div 4 = 6$ Bälle
> - Gesamt: $10 \cdot 8 \cdot 6 = 480$ Bälle
> 
> (Mit optimaler Kugelpackung wären es ca. 550 Bälle)

## Hohlkugeln

### Volumen

> [!note] Hohlkugel
> $$V = \frac{4}{3}\pi(r_a^3 - r_i^3)$$
> wobei $r_a$ = Außenradius, $r_i$ = Innenradius

> [!example] Beispiel 11: Christbaumkugel
> Eine Christbaumkugel hat 8 cm Außendurchmesser und 0,2 cm Wandstärke.
> 
> **Materialvolumen:**
> $$r_a = 4 \text{ cm}, \quad r_i = 3{,}8 \text{ cm}$$
> $$V = \frac{4}{3}\pi(4^3 - 3{,}8^3) = \frac{4}{3}\pi(64 - 54{,}872) \approx 38{,}3 \text{ cm}^3$$

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Volumen | $V = \frac{4}{3}\pi r^3$ |
> | Oberfläche | $O = 4\pi r^2$ |
> | Halbkugel-Volumen | $V = \frac{2}{3}\pi r^3$ |
> | Hohlkugel-Volumen | $V = \frac{4}{3}\pi(r_a^3 - r_i^3)$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Eine Kugel hat den Radius 8 cm. Berechnen Sie:
> a) das Volumen
> b) die Oberfläche

> [!question] Aufgabe 2
> Eine Bowlingkugel hat die Masse 7 kg und eine Dichte von 2,7 g/cm³. Wie groß ist ihr Durchmesser?

> [!question] Aufgabe 3
> Wie viel Farbe braucht man, um 100 Weihnachtskugeln (je 6 cm Durchmesser) zu bemalen? (Farbbedarf: 0,1 ml/cm²)

> [!question] Aufgabe 4
> Eine Halbkugel-Schüssel hat 15 cm Durchmesser. Wie viel ml fasst sie?

> [!question] Aufgabe 5
> Um wie viel Prozent nimmt das Volumen einer Kugel zu, wenn der Radius um 10% vergrößert wird?

---

**Navigation:** [[07-Kegel|← Kegel]] | [[09-Volumenberechnung|Volumenberechnung →]]
