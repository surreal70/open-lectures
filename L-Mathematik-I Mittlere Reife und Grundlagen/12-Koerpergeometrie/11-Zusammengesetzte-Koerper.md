---
title: Zusammengesetzte Körper
chapter: "12"
section: "12.11"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/geometrie/koerper
  - zusammengesetzte-koerper
  - volumen
  - oberflaeche
---

# Zusammengesetzte Körper

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Zusammengesetzte Körper in Grundkörper zerlegen
> - Volumen durch Addition/Subtraktion berechnen
> - Oberflächen komplexer Körper bestimmen

In der Praxis begegnen uns selten perfekte Würfel, Zylinder oder Kugeln. Die meisten realen Objekte sind Kombinationen aus mehreren Grundkörpern: Ein Silo besteht aus einem Zylinder mit aufgesetztem Kegel, ein Bleistift aus einem Sechseckprisma mit Kegelspitze, ein Haus aus einem Quader mit Dreiecksprisma-Dach. Das Berechnen solcher zusammengesetzter Körper ist eine wichtige praktische Fähigkeit.

## Strategien

### Addition

Wenn ein Körper aus mehreren Grundkörpern zusammengesetzt ist:
$$V_{gesamt} = V_1 + V_2 + ...$$

Diese Strategie verwendet man bei Silos (Zylinder + Kegel), Bleistiften (Prisma + Kegel) oder Häusern (Quader + Prisma als Dach).

### Subtraktion

Wenn ein Körper Hohlräume, Bohrungen oder Aussparungen hat:
$$V_{gesamt} = V_{außen} - V_{innen}$$

Diese Strategie verwendet man bei durchbohrten Objekten, ausgehöhlten Körpern oder Rohren (Zylinder minus Zylinder).

> [!tip] **Systematisches Vorgehen**
> 1. Skizziere den Körper und markiere die einzelnen Teilkörper
> 2. Identifiziere jeden Teilkörper (Würfel? Zylinder? Kegel?)
> 3. Notiere die Maße für jeden Teilkörper
> 4. Berechne das Volumen jedes Teilkörpers einzeln
> 5. Addiere oder subtrahiere je nach Situation

## Beispiele

> [!example] Beispiel 1: Silo (Zylinder + Kegel)
> Ein Getreidesilo besteht aus einem zylindrischen Hauptteil und einem kegelförmigen Dach.
> Zylinder: $r = 3$ m, $h = 8$ m  
> Kegel (Dach): $r = 3$ m, $h = 2$ m
> 
> **Volumen:**
> $$V_{Zylinder} = \pi \cdot 3^2 \cdot 8 = 72\pi \text{ m}^3$$
> $$V_{Kegel} = \frac{1}{3}\pi \cdot 3^2 \cdot 2 = 6\pi \text{ m}^3$$
> $$V_{gesamt} = 72\pi + 6\pi = 78\pi \approx 245 \text{ m}^3$$

> [!example] Beispiel 2: Würfel mit Bohrung
> Aus einem Würfel wird eine zylindrische Bohrung durch die Mitte geführt.
> Würfel: $a = 10$ cm  
> Zylindrische Bohrung: $r = 2$ cm, durchgehend
> 
> **Restvolumen:**
> $$V_{Würfel} = 10^3 = 1000 \text{ cm}^3$$
> $$V_{Bohrung} = \pi \cdot 2^2 \cdot 10 = 40\pi \approx 125{,}7 \text{ cm}^3$$
> $$V_{Rest} = 1000 - 40\pi \approx 874 \text{ cm}^3$$

> [!example] Beispiel 3: Eiscreme-Waffel mit Kugel
> Eine Eistüte (Kegel) mit einer aufgesetzten Halbkugel Eis.
> Kegel: $r = 3$ cm, $h = 12$ cm  
> Halbkugel: $r = 3$ cm
> 
> **Gesamtvolumen:**
> $$V_{Kegel} = \frac{1}{3}\pi \cdot 3^2 \cdot 12 = 36\pi \text{ cm}^3$$
> $$V_{Halbkugel} = \frac{2}{3}\pi \cdot 3^3 = 18\pi \text{ cm}^3$$
> $$V_{gesamt} = 36\pi + 18\pi = 54\pi \approx 170 \text{ cm}^3$$

## Oberflächenberechnung

Bei Oberflächen zusammengesetzter Körper gilt eine wichtige Regel:

> [!warning] **Berührungsflächen abziehen!**
> Wo zwei Körper aneinanderstoßen, ist die Berührungsfläche von außen nicht mehr sichtbar. Diese Flächen müssen von der Summe der Einzeloberflächen abgezogen werden.

$$O_{gesamt} = O_1 + O_2 - 2 \cdot A_{Kontakt}$$

Der Faktor 2 entsteht, weil die Kontaktfläche bei beiden Körpern wegfällt.

> [!example] Beispiel 4: Oberfläche eines Silos
> Zylinder ($r = 3$ m, $h = 8$ m) mit Kegeldach ($r = 3$ m, $h = 2$ m)
> 
> **Berechnung:**
> - Zylinder: Mantelfläche + Boden (Deckel entfällt!) 
>   $= 2\pi \cdot 3 \cdot 8 + \pi \cdot 3^2 = 48\pi + 9\pi = 57\pi$ m²
> - Kegel: Nur Mantelfläche (Grundfläche ist der „Deckel" des Zylinders)
>   $s = \sqrt{3^2 + 2^2} = \sqrt{13}$ m
>   $M = \pi \cdot 3 \cdot \sqrt{13} \approx 34$ m²
> - Gesamtoberfläche: $57\pi + 34 \approx 213$ m²

## Zusammenfassung

> [!abstract] Kernpunkte
> - **Addition:** Wenn Körper zusammengesetzt sind → Volumina addieren
> - **Subtraktion:** Wenn Körper Hohlräume haben → Volumina subtrahieren
> - **Oberflächen:** Berührungsflächen müssen abgezogen werden (Faktor 2!)
> - Immer erst skizzieren und Teilkörper identifizieren

---

**Navigation:** [[10-Oberflaechenberechnung|← Oberflächenberechnung]] | [[12-Praktische-Berechnungen|Praktische Berechnungen →]]
