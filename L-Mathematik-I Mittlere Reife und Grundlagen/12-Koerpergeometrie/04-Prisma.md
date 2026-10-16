---
title: Das Prisma
chapter: "12"
section: "12.4"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - prisma
  - volumen
  - oberflaeche
---

# Das Prisma

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Prismen erkennen und beschreiben
> - Das Volumen eines Prismas berechnen
> - Die Oberfläche eines Prismas bestimmen
> - Verschiedene Prismenarten unterscheiden

## Definition und Eigenschaften

### Was ist ein Prisma?

> [!note] Definition
> Ein **Prisma** ist ein Körper mit:
> - Zwei kongruenten, parallelen Grundflächen (Vielecke)
> - Seitenflächen, die Parallelogramme sind (bei geraden Prismen: Rechtecke)

### Arten von Prismen

**Nach der Grundfläche:**
- Dreiecksprisma (Grundfläche: Dreieck)
- Quadratisches Prisma = [[03-Quader|Quader]] (Grundfläche: Quadrat)
- Fünfecksprisma, Sechsecksprisma, ...

**Nach der Ausrichtung:**
- **Gerades Prisma:** Seitenflächen stehen senkrecht zur Grundfläche
- **Schiefes Prisma:** Seitenflächen sind geneigt

> [!tip] Der Quader als Prisma
> Der [[03-Quader|Quader]] ist ein gerades Prisma mit rechteckiger Grundfläche.

## Volumen des Prismas

### Formel

> [!note] Volumenformel
> $$V = G \cdot h$$
> wobei:
> - $G$ = Flächeninhalt der Grundfläche
> - $h$ = Höhe des Prismas (senkrechter Abstand der Grundflächen)

Diese Formel gilt für **alle** Prismen, unabhängig von der Form der Grundfläche!

### Beispielrechnungen

> [!example] Beispiel 1: Dreiecksprisma
> Ein Dreiecksprisma hat eine dreieckige Grundfläche mit Basis 6 cm und Höhe 4 cm. Das Prisma ist 10 cm hoch.
> 
> **Lösung:**
> 1. Grundfläche: $G = \frac{1}{2} \cdot 6 \cdot 4 = 12 \text{ cm}^2$
> 2. Volumen: $V = G \cdot h = 12 \cdot 10 = 120 \text{ cm}^3$

> [!example] Beispiel 2: Sechsecksprisma
> Ein regelmäßiges Sechsecksprisma hat einen Umkreisradius der Grundfläche von 4 cm und eine Höhe von 8 cm.
> 
> **Lösung:**
> 1. Regelmäßiges Sechseck: $G = \frac{3\sqrt{3}}{2} \cdot a^2$
>    Bei Umkreisradius $r = a$: $a = 4$ cm
> 2. $G = \frac{3\sqrt{3}}{2} \cdot 4^2 = \frac{3\sqrt{3}}{2} \cdot 16 = 24\sqrt{3} \approx 41{,}57 \text{ cm}^2$
> 3. $V = 41{,}57 \cdot 8 \approx 332{,}6 \text{ cm}^3$

## Oberfläche des Prismas

### Formel

> [!note] Oberflächenformel
> $$O = 2G + M$$
> wobei:
> - $G$ = Grundfläche
> - $M$ = Mantelfläche (Summe aller Seitenflächen)
> 
> Für ein gerades Prisma:
> $$M = U \cdot h$$
> wobei $U$ = Umfang der Grundfläche

### Beispielrechnungen

> [!example] Beispiel 3: Oberfläche Dreiecksprisma
> Ein gleichseitiges Dreiecksprisma hat die Seitenlänge des Dreiecks $a = 5$ cm und die Prismenhöhe $h = 12$ cm.
> 
> **Lösung:**
> 1. Grundfläche: $G = \frac{\sqrt{3}}{4} \cdot 5^2 = \frac{25\sqrt{3}}{4} \approx 10{,}83 \text{ cm}^2$
> 2. Umfang: $U = 3 \cdot 5 = 15$ cm
> 3. Mantelfläche: $M = 15 \cdot 12 = 180 \text{ cm}^2$
> 4. Oberfläche: $O = 2 \cdot 10{,}83 + 180 = 201{,}66 \text{ cm}^2$

## Spezielle Prismen

### Dreiecksprisma (Dreiseitiges Prisma)

**Grundfläche:** Dreieck
- Allgemein: $G = \frac{1}{2} \cdot \text{Basis} \cdot \text{Höhe}_{Dreieck}$
- Gleichseitig: $G = \frac{\sqrt{3}}{4} \cdot a^2$

**Mantelfläche:** 3 Rechtecke
$$M = (a + b + c) \cdot h$$

> [!example] Alltagsbeispiel
> Toblerone-Verpackung, Zeltdach, Rampenprisma

### Fünfecksprisma

**Grundfläche:** Regelmäßiges Fünfeck
$$G = \frac{5a^2}{4} \cdot \sqrt{1 + \frac{2}{\sqrt{5}}} \approx 1{,}72 \cdot a^2$$

### Sechsecksprisma (Bleistift)

**Grundfläche:** Regelmäßiges Sechseck
$$G = \frac{3\sqrt{3}}{2} \cdot a^2 \approx 2{,}598 \cdot a^2$$

> [!example] Alltagsbeispiel
> Bleistifte, Schraubenmuttern, Bienenwaben

## Praktische Anwendungen

### Bauwerke

> [!example] Beispiel 4: Dachkonstruktion
> Ein Satteldach hat eine dreieckige Giebelseite mit 8 m Basis und 3 m Höhe. Die Dachlänge beträgt 12 m.
> 
> **Dachraum-Volumen:**
> $$G = \frac{1}{2} \cdot 8 \cdot 3 = 12 \text{ m}^2$$
> $$V = 12 \cdot 12 = 144 \text{ m}^3$$

### Verpackungen

> [!example] Beispiel 5: Toblerone-Verpackung
> Eine Toblerone-Verpackung ist ein Dreiecksprisma. Das gleichseitige Dreieck hat 4 cm Seitenlänge, die Verpackung ist 30 cm lang.
> 
> a) **Volumen:**
> $$G = \frac{\sqrt{3}}{4} \cdot 4^2 = 4\sqrt{3} \approx 6{,}93 \text{ cm}^2$$
> $$V = 6{,}93 \cdot 30 \approx 207{,}8 \text{ cm}^3$$
> 
> b) **Kartonbedarf (Oberfläche):**
> $$U = 3 \cdot 4 = 12 \text{ cm}$$
> $$M = 12 \cdot 30 = 360 \text{ cm}^2$$
> $$O = 2 \cdot 6{,}93 + 360 \approx 373{,}9 \text{ cm}^2$$

### Rampen und Keile

> [!example] Beispiel 6: Laderampe
> Eine Laderampe hat einen dreieckigen Querschnitt: rechtwinkliges Dreieck mit Katheten 80 cm und 15 cm. Die Rampe ist 2 m lang.
> 
> **Volumen:**
> $$G = \frac{1}{2} \cdot 80 \cdot 15 = 600 \text{ cm}^2$$
> $$V = 600 \cdot 200 = 120.000 \text{ cm}^3 = 0{,}12 \text{ m}^3$$

## Prisma mit beliebiger Grundfläche

### Zusammengesetzte Grundflächen

> [!example] Beispiel 7: L-förmiges Prisma
> Ein Prisma hat eine L-förmige Grundfläche (zwei verbundene Rechtecke: 6 cm × 3 cm und 2 cm × 4 cm). Die Höhe ist 5 cm.
> 
> **Lösung:**
> $$G = 6 \cdot 3 + 2 \cdot 4 = 18 + 8 = 26 \text{ cm}^2$$
> $$V = 26 \cdot 5 = 130 \text{ cm}^3$$

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Volumen | $V = G \cdot h$ |
> | Oberfläche | $O = 2G + M$ |
> | Mantelfläche (gerade) | $M = U \cdot h$ |

> [!tip] Universelle Volumenformel
> Die Formel $V = G \cdot h$ gilt für alle Prismen – man muss nur die Grundfläche entsprechend der Form berechnen können.

## Übungsaufgaben

> [!question] Aufgabe 1
> Ein Dreiecksprisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Katheten 5 cm und 12 cm. Die Prismenhöhe beträgt 20 cm. Berechnen Sie Volumen und Oberfläche.

> [!question] Aufgabe 2
> Ein Bleistift (Sechsecksprisma) hat 7 mm Kantenlänge des Sechsecks und ist 17,5 cm lang. Wie viel Holz wurde für den Bleistift verwendet?

> [!question] Aufgabe 3
> Wie viel Liter Luft enthält ein Zelt mit dreieckiger Grundform (Basis 2,5 m, Höhe 2 m) und einer Länge von 3 m?

> [!question] Aufgabe 4
> Ein Prisma hat ein regelmäßiges Fünfeck als Grundfläche mit Seitenlänge 4 cm. Die Höhe beträgt 10 cm. Berechnen Sie das Volumen.

---

**Navigation:** [[03-Quader|← Quader]] | [[05-Zylinder|Zylinder →]]
