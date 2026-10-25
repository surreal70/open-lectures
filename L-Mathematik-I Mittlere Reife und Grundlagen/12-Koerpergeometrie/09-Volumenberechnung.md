---
title: Volumenberechnung - Übersicht und Vergleich
chapter: "12"
section: "12.9"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - volumen
  - zusammenfassung
---

# Volumenberechnung

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Volumenformeln aller Grundkörper anwenden
> - Die richtige Formel für verschiedene Aufgaben auswählen
> - Volumen in verschiedenen Einheiten umrechnen
> - Volumenberechnungen für praktische Probleme durchführen

## Übersicht aller Volumenformeln

Die Volumenberechnung ist eines der zentralen Themen der Körpergeometrie. Schon in der Antike war es wichtig, Volumina zu berechnen – etwa um Getreide in Silos zu messen, Bausteine für Pyramiden zu planen oder Schiffe zu konstruieren. Heute begegnen uns Volumenberechnungen beim Tanken, Kochen, Bauen und in zahllosen technischen Anwendungen.

### Säulenförmige Körper (Prismen)

> [!note] Grundprinzip
> $$V = \text{Grundfläche} \times \text{Höhe} = G \cdot h$$

Dieses Prinzip gilt für alle Körper, bei denen die Grundfläche „nach oben gestapelt" wird – also für alle Prismen und den Zylinder. Die Idee geht auf Bonaventura Cavalieri (1598–1647) zurück und wird als **Prinzip von Cavalieri** bezeichnet.

| Körper | Formel | Grundfläche |
|--------|--------|-------------|
| [[02-Wuerfel\|Würfel]] | $V = a^3$ | $G = a^2$ |
| [[03-Quader\|Quader]] | $V = a \cdot b \cdot c$ | $G = a \cdot b$ |
| [[04-Prisma\|Prisma]] | $V = G \cdot h$ | beliebiges Vieleck |
| [[05-Zylinder\|Zylinder]] | $V = \pi r^2 h$ | $G = \pi r^2$ |

### Spitze Körper (Pyramiden/Kegel)

> [!note] Grundprinzip
> $$V = \frac{1}{3} \cdot \text{Grundfläche} \times \text{Höhe} = \frac{1}{3} G \cdot h$$

Der Faktor $\frac{1}{3}$ ist charakteristisch für alle spitzen Körper. Er ergibt sich daraus, dass der Körper zur Spitze hin „immer weniger Platz" hat.

| Körper | Formel |
|--------|--------|
| [[06-Pyramide\|Pyramide]] | $V = \frac{1}{3} G \cdot h$ |
| [[07-Kegel\|Kegel]] | $V = \frac{1}{3} \pi r^2 h$ |

> [!warning] **Häufiger Fehler: Faktor $\frac{1}{3}$ vergessen**
> Bei Pyramiden und Kegeln wird oft der Faktor $\frac{1}{3}$ vergessen. Ohne diesen Faktor berechnet man das Volumen eines Prismas bzw. Zylinders – das wäre dreimal zu viel!

### Kugel

| Körper | Formel |
|--------|--------|
| [[08-Kugel\|Kugel]] | $V = \frac{4}{3} \pi r^3$ |
| Halbkugel | $V = \frac{2}{3} \pi r^3$ |

Die Kugelformel steht für sich allein – sie folgt weder dem Prisma- noch dem Pyramidenprinzip. Archimedes entdeckte sie durch einen genialen geometrischen Vergleich mit Zylinder und Kegel.

## Volumeneinheiten

### Umrechnungstabelle

| Einheit | Umrechnung |
|---------|------------|
| 1 cm³ | = 1 ml (Milliliter) |
| 1 dm³ | = 1 Liter = 1000 cm³ |
| 1 m³ | = 1000 dm³ = 1000 Liter |
| 1 m³ | = 1.000.000 cm³ |

### Umrechnungsfaktoren

![[volumen-einheiten.png]]
*<span class="fig-id">12-09-volumen-einheiten</span>: Umrechnung der Volumeneinheiten – jeder Schritt entspricht dem Faktor 1000.*

> [!tip] Merkhilfe
> Bei Volumeneinheiten verschiebt man das Komma immer um **drei** Stellen (weil Volumen = Länge³).

## Vergleich der Körper

### Prisma vs. Pyramide

Bei gleicher Grundfläche und Höhe:
$$V_{\text{Pyramide}} = \frac{1}{3} V_{\text{Prisma}}$$

> [!example] Beispiel
> Prisma und Pyramide haben beide $G = 30$ cm² und $h = 12$ cm.
> - Prisma: $V = 30 \cdot 12 = 360$ cm³
> - Pyramide: $V = \frac{1}{3} \cdot 30 \cdot 12 = 120$ cm³

### Zylinder vs. Kegel

Bei gleichem Radius und gleicher Höhe:
$$V_{\text{Kegel}} = \frac{1}{3} V_{\text{Zylinder}}$$

### Kugel vs. Zylinder (umschrieben)

Ein Zylinder, der eine Kugel genau umschließt ($r = r$, $h = 2r$):
$$V_{\text{Kugel}} = \frac{2}{3} V_{\text{Zylinder}}$$

## Strategien zur Volumenberechnung

### Schritt-für-Schritt-Vorgehen

1. **Körper identifizieren:** Welche Form hat der Körper?
2. **Formel auswählen:** Passende Volumenformel
3. **Maße zuordnen:** Welche Werte sind gegeben?
4. **Einheiten prüfen:** Alle Maße in derselben Einheit?
5. **Berechnung durchführen**
6. **Ergebnis prüfen:** Ist das Ergebnis plausibel?

### Komplexe Körper zerlegen

> [!example] Beispiel: Zusammengesetzter Körper
> Ein Behälter besteht aus einem Zylinder ($r = 5$ cm, $h = 10$ cm) mit aufgesetzter Halbkugel.
> 
> **Lösung:**
> $$V_{\text{Zylinder}} = \pi \cdot 5^2 \cdot 10 = 250\pi$$
> $$V_{\text{Halbkugel}} = \frac{2}{3}\pi \cdot 5^3 = \frac{250}{3}\pi$$
> $$V_{\text{gesamt}} = 250\pi + \frac{250}{3}\pi = \frac{1000}{3}\pi \approx 1047 \text{ cm}^3$$

## Typische Aufgabentypen

### Typ 1: Volumen direkt berechnen

> [!example] Aufgabe
> Ein Quader hat die Maße 8 cm × 5 cm × 3 cm. Berechne das Volumen.
> 
> **Lösung:** $V = 8 \cdot 5 \cdot 3 = 120$ cm³

### Typ 2: Fehlende Maße berechnen

> [!example] Aufgabe
> Ein Zylinder hat das Volumen 500 cm³ und den Radius 4 cm. Wie hoch ist er?
> 
> **Lösung:**
> $$500 = \pi \cdot 4^2 \cdot h$$
> $$h = \frac{500}{16\pi} \approx 9{,}95 \text{ cm}$$

### Typ 3: Volumenvergleich

> [!example] Aufgabe
> Welcher Körper hat mehr Volumen: Ein Würfel mit 5 cm Kantenlänge oder eine Kugel mit 5 cm Durchmesser?
> 
> **Lösung:**
> - Würfel: $V = 5^3 = 125$ cm³
> - Kugel: $V = \frac{4}{3}\pi \cdot 2{,}5^3 \approx 65{,}4$ cm³
> 
> Der Würfel hat mehr Volumen.

### Typ 4: Füllmengen und Flüssigkeiten

> [!example] Aufgabe
> Wie viele Liter Wasser passen in ein zylindrisches Fass mit 40 cm Durchmesser und 60 cm Höhe?
> 
> **Lösung:**
> $$V = \pi \cdot 20^2 \cdot 60 = 24.000\pi \approx 75.398 \text{ cm}^3 \approx 75{,}4 \text{ Liter}$$

### Typ 5: Umfüllen

> [!example] Aufgabe
> Wasser aus einem vollen Würfelbehälter (20 cm Kantenlänge) wird in einen Zylinder (Radius 10 cm) umgefüllt. Wie hoch steht das Wasser?
> 
> **Lösung:**
> $$V_{\text{Würfel}} = 20^3 = 8000 \text{ cm}^3$$
> $$8000 = \pi \cdot 10^2 \cdot h$$
> $$h = \frac{8000}{100\pi} \approx 25{,}5 \text{ cm}$$

## Praktische Anwendungen

### Materialbedarf

> [!example] Betonmenge
> Ein Fundament ist ein Quader: 4 m × 3 m × 0,3 m.
> $$V = 4 \cdot 3 \cdot 0{,}3 = 3{,}6 \text{ m}^3$$
> Bei 10% Zugabe für Verlust: $3{,}6 \cdot 1{,}1 = 3{,}96$ m³ ≈ 4 m³ Beton

### Verpackungsoptimierung

> [!example] Optimale Dose
> Welche Zylinderform bei festem Volumen braucht am wenigsten Material?
> 
> **Antwort:** Wenn Höhe = Durchmesser ($h = 2r$), ist die Oberfläche minimal.

### Dichte und Masse

> [!note] Formel
> $$m = \varrho \cdot V$$
> Masse = Dichte × Volumen

> [!example] Goldbarren
> Ein Goldbarren (Quader) hat die Maße 10 cm × 5 cm × 2 cm. Gold hat die Dichte 19,3 g/cm³.
> $$V = 10 \cdot 5 \cdot 2 = 100 \text{ cm}^3$$
> $$m = 19{,}3 \cdot 100 = 1930 \text{ g} = 1{,}93 \text{ kg}$$

## Zusammenfassung

> [!abstract] Formelübersicht
> | Körpertyp | Formel |
> |-----------|--------|
> | Säulen | $V = G \cdot h$ |
> | Spitzen | $V = \frac{1}{3} G \cdot h$ |
> | Kugel | $V = \frac{4}{3} \pi r^3$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Ordnen Sie die Körper nach Volumen (kleinster zuerst):
> - Würfel mit $a = 6$ cm
> - Kugel mit $r = 4$ cm
> - Zylinder mit $r = 3$ cm, $h = 10$ cm
> - Kegel mit $r = 5$ cm, $h = 12$ cm

> [!question] Aufgabe 2
> Ein Silo besteht aus einem Zylinder (Durchmesser 4 m, Höhe 8 m) mit aufgesetztem Kegel (Höhe 2 m). Wie viel m³ fasst es?

> [!question] Aufgabe 3
> Aus einem Würfel ($a = 10$ cm) wird eine zylindrische Bohrung ($r = 3$ cm) durch die Mitte geführt. Wie viel Restvolumen bleibt?

> [!question] Aufgabe 4
> Eine Pralinenschachtel enthält 9 Pralinen (Kugeln, $d = 2$ cm) in einem Quader (9 cm × 6 cm × 3 cm). Wie viel Prozent des Kartons sind mit Luft gefüllt?

---

**Navigation:** [[08-Kugel|← Kugel]] | [[10-Oberflaechenberechnung|Oberflächenberechnung →]]
