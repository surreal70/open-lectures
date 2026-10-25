---
title: Der Zylinder
chapter: "12"
section: "12.5"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - zylinder
  - volumen
  - oberflaeche
  - kreiszylinder
---

# Der Zylinder

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften des Zylinders beschreiben
> - Volumen eines Zylinders berechnen
> - Oberfläche (Mantelfläche und Gesamtfläche) berechnen
> - Praktische Aufgaben mit Zylindern lösen

## Definition und Eigenschaften

### Was ist ein Zylinder?

> [!note] Definition
> Ein **Kreiszylinder** (oder kurz Zylinder) ist ein Körper mit:
> - Zwei kongruenten, parallelen kreisförmigen Grundflächen
> - Einer gekrümmten Mantelfläche, die beide Grundflächen verbindet

![[zylinder-3d.png]]
*<span class="fig-id">12-05-zylinder-3d</span>: Schrägbild eines Zylinders mit Radius $r$ und Höhe $h$. Die verdeckte Grundkante ist gestrichelt dargestellt.*

Der Begriff „Zylinder" stammt vom griechischen Wort „kylindros" (= Rolle, Walze). Zylinder sind in der Technik und im Alltag allgegenwärtig: Getränkedosen, Rohre, Säulen, Baumstämme, Kerzen – die zylindrische Form verbindet praktische Vorteile wie gute Stapelbarkeit, gleichmäßige Materialverteilung und einfache Herstellung.

### Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Grundfläche | Kreis mit Radius $r$ |
| Deckfläche | Kreis mit Radius $r$ |
| Mantelfläche | Rechteck (abgewickelt) |
| Höhe | Senkrechter Abstand der Grundflächen |

> [!tip] Der Zylinder als "rundes Prisma"
> Der Zylinder verhält sich zum [[04-Prisma|Prisma]] wie der Kreis zum Vieleck – man kann ihn als Prisma mit unendlich vielen Seitenflächen betrachten.

> [!info] **Warum sind Dosen zylindrisch?**
> Die Zylinderform hat handfeste Vorteile: Sie ist stabil (der Druck verteilt sich gleichmäßig), leicht herzustellen (Blech wird gerollt), transportfreundlich (rollt auf Förderbändern) und bietet ein günstiges Verhältnis von Volumen zu Material. Bei gleichem Umfang fasst ein Kreis mehr Fläche als jede andere Form – und damit auch mehr Volumen bei gleicher Blechmenge.

## Volumen des Zylinders

### Formel

> [!note] Volumenformel
> $$V = \pi r^2 \cdot h = G \cdot h$$
> wobei:
> - $r$ = Radius der Grundfläche
> - $h$ = Höhe des Zylinders
> - $G = \pi r^2$ = Grundfläche (Kreisfläche)

### Beispielrechnungen

> [!example] Beispiel 1: Volumen berechnen
> Ein Zylinder hat den Radius $r = 5$ cm und die Höhe $h = 12$ cm.
> 
> **Lösung:**
> $$V = \pi \cdot 5^2 \cdot 12 = \pi \cdot 25 \cdot 12 = 300\pi \approx 942{,}5 \text{ cm}^3$$

> [!example] Beispiel 2: Mit Durchmesser rechnen
> Eine zylindrische Dose hat 8 cm Durchmesser und 15 cm Höhe.
> 
> **Lösung:**
> $$r = \frac{d}{2} = \frac{8}{2} = 4 \text{ cm}$$
> $$V = \pi \cdot 4^2 \cdot 15 = 240\pi \approx 754 \text{ cm}^3 = 0{,}754 \text{ Liter}$$

### Fehlende Größen berechnen

> [!example] Beispiel 3: Radius berechnen
> Ein Zylinder hat das Volumen 500 cm³ und die Höhe 10 cm. Wie groß ist der Radius?
> 
> **Lösung:**
> $$V = \pi r^2 h$$
> $$500 = \pi r^2 \cdot 10$$
> $$r^2 = \frac{500}{10\pi} = \frac{50}{\pi} \approx 15{,}92$$
> $$r = \sqrt{15{,}92} \approx 3{,}99 \text{ cm}$$

> [!example] Beispiel 4: Höhe berechnen
> Ein Zylinder hat das Volumen 1 Liter und den Durchmesser 10 cm. Wie hoch ist er?
> 
> **Lösung:**
> $$V = \pi r^2 h$$
> $$1000 = \pi \cdot 5^2 \cdot h$$
> $$h = \frac{1000}{25\pi} \approx 12{,}73 \text{ cm}$$

## Oberfläche des Zylinders

### Bestandteile

Die Oberfläche besteht aus:
1. **Grundfläche:** $G = \pi r^2$
2. **Deckfläche:** $G = \pi r^2$
3. **Mantelfläche:** $M = 2\pi r \cdot h$ (abgewickelt ein Rechteck)

### Formeln

> [!note] Oberflächenformeln
> **Mantelfläche:**
> $$M = 2\pi r \cdot h = U \cdot h$$
> (Umfang × Höhe)
> 
> **Gesamtoberfläche:**
> $$O = 2\pi r^2 + 2\pi rh = 2\pi r(r + h)$$

### Beispielrechnungen

> [!example] Beispiel 5: Oberfläche berechnen
> Ein Zylinder hat $r = 4$ cm und $h = 10$ cm.
> 
> **Lösung:**
> $$M = 2\pi \cdot 4 \cdot 10 = 80\pi \approx 251{,}3 \text{ cm}^2$$
> $$O = 2\pi \cdot 4 \cdot (4 + 10) = 8\pi \cdot 14 = 112\pi \approx 351{,}9 \text{ cm}^2$$

> [!example] Beispiel 6: Etikett einer Dose
> Wie groß muss ein Etikett sein, das eine Dose (Durchmesser 7 cm, Höhe 12 cm) vollständig umschließt?
> 
> **Lösung:**
> Das Etikett entspricht der Mantelfläche:
> $$M = 2\pi r h = 2\pi \cdot 3{,}5 \cdot 12 = 84\pi \approx 263{,}9 \text{ cm}^2$$
> 
> Abgewickelt: Rechteck mit Breite $U = 2\pi \cdot 3{,}5 \approx 22$ cm und Höhe 12 cm.

## Zylindernetz

### Aufbau

Ein Zylindernetz besteht aus:
- 2 Kreisen (Grund- und Deckfläche)
- 1 Rechteck (abgewickelte Mantelfläche)

Das Rechteck hat:
- **Breite:** Umfang des Kreises $= 2\pi r$
- **Höhe:** Zylinderhöhe $= h$

> [!tip] **Anschauliche Vorstellung**
> Wenn du das Etikett einer Dose ablöst und flach hinlegst, erhältst du ein Rechteck – das ist die abgewickelte Mantelfläche. Die Breite des Rechtecks entspricht genau dem Umfang der Dose.

> [!warning] **Häufiger Fehler: Mantelfläche und Oberfläche verwechseln**
> - **Mantelfläche $M$:** Nur die „Rundseite" (das abgewickelte Rechteck) → $M = 2\pi r h$
> - **Oberfläche $O$:** Mantelfläche PLUS beide Kreisflächen → $O = 2\pi r(r + h)$
> 
> Bei einem Etikett (nur die Seite) brauchst du die Mantelfläche. Bei einer kompletten Dose (rundum einpacken) brauchst du die Oberfläche.

## Praktische Anwendungen

### Getränkedosen und Behälter

> [!example] Beispiel 7: Getränkedose
> Eine Standard-Getränkedose hat 6,6 cm Durchmesser und 11,5 cm Höhe.
> 
> a) **Fassungsvermögen:**
> $$V = \pi \cdot 3{,}3^2 \cdot 11{,}5 = \pi \cdot 10{,}89 \cdot 11{,}5 \approx 393{,}4 \text{ cm}^3$$
> Das sind etwa 0,4 Liter (330 ml + Kopfraum).
> 
> b) **Materialbedarf für das Blech:**
> $$O = 2\pi \cdot 3{,}3 \cdot (3{,}3 + 11{,}5) = 2\pi \cdot 3{,}3 \cdot 14{,}8 \approx 307 \text{ cm}^2$$

### Rohre und Hohlzylinder

> [!example] Beispiel 8: Wasserrohr
> Ein Wasserrohr hat den Außendurchmesser 5 cm und den Innendurchmesser 4,6 cm. Es ist 2 m lang.
> 
> **Volumen des Materials:**
> $$V = \pi h (r_a^2 - r_i^2) = \pi \cdot 200 \cdot (2{,}5^2 - 2{,}3^2)$$
> $$V = 200\pi \cdot (6{,}25 - 5{,}29) = 200\pi \cdot 0{,}96 \approx 603 \text{ cm}^3$$

### Tanks und Silos

> [!example] Beispiel 9: Öltank
> Ein zylindrischer Öltank hat 1,2 m Durchmesser und 2 m Höhe.
> 
> a) **Fassungsvermögen:**
> $$V = \pi \cdot 0{,}6^2 \cdot 2 = 0{,}72\pi \approx 2{,}26 \text{ m}^3 = 2260 \text{ Liter}$$
> 
> b) **Lackbedarf für Außenanstrich (ohne Boden):**
> $$O = \pi r^2 + 2\pi rh = \pi \cdot 0{,}6^2 + 2\pi \cdot 0{,}6 \cdot 2$$
> $$O = 0{,}36\pi + 2{,}4\pi = 2{,}76\pi \approx 8{,}67 \text{ m}^2$$

### Füllstandsprobleme

> [!example] Beispiel 10: Wassertank füllen
> Ein zylindrischer Tank (Radius 50 cm, Höhe 120 cm) wird mit 50 Liter pro Minute befüllt.
> 
> a) **Fassungsvermögen:**
> $$V = \pi \cdot 50^2 \cdot 120 = 300.000\pi \approx 942.478 \text{ cm}^3 \approx 942 \text{ Liter}$$
> 
> b) **Füllzeit:**
> $$t = \frac{942}{50} \approx 18{,}8 \text{ Minuten}$$

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Grundfläche | $G = \pi r^2$ |
> | Volumen | $V = \pi r^2 h$ |
> | Mantelfläche | $M = 2\pi r h$ |
> | Oberfläche | $O = 2\pi r(r + h)$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Ein Zylinder hat den Radius 6 cm und die Höhe 14 cm. Berechnen Sie:
> a) das Volumen
> b) die Mantelfläche
> c) die Gesamtoberfläche

> [!question] Aufgabe 2
> Eine zylindrische Kerze hat 4 cm Durchmesser. Wie hoch muss sie sein, damit sie 200 cm³ Wachs enthält?

> [!question] Aufgabe 3
> Ein Regenfass (Durchmesser 60 cm, Höhe 90 cm) ist zu 75% gefüllt. Wie viele Liter Wasser sind drin?

> [!question] Aufgabe 4
> Vergleichen Sie zwei Dosen mit gleichem Volumen von 500 ml:
> a) Dose A: Durchmesser 8 cm
> b) Dose B: Durchmesser 6 cm
> Welche braucht weniger Material (kleinere Oberfläche)?

---

**Navigation:** [[04-Prisma|← Prisma]] | [[06-Pyramide|Pyramide →]]
