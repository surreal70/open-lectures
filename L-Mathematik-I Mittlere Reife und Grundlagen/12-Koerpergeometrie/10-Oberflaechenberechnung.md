---
title: Oberflächenberechnung - Übersicht und Vergleich
chapter: "12"
section: "12.10"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - oberflaeche
  - zusammenfassung
---

# Oberflächenberechnung

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Oberflächenformeln aller Grundkörper anwenden
> - Mantelfläche und Gesamtoberfläche unterscheiden
> - Die richtige Formel für verschiedene Aufgaben auswählen
> - Praktische Berechnungen für Materialverbrauch durchführen

## Übersicht aller Oberflächenformeln

### Grundkörper

| Körper | Oberfläche | Mantelfläche |
|--------|------------|--------------|
| [[02-Wuerfel\|Würfel]] | $O = 6a^2$ | — |
| [[03-Quader\|Quader]] | $O = 2(ab + ac + bc)$ | — |
| [[05-Zylinder\|Zylinder]] | $O = 2\pi r(r + h)$ | $M = 2\pi rh$ |
| [[07-Kegel\|Kegel]] | $O = \pi r(r + s)$ | $M = \pi rs$ |
| [[08-Kugel\|Kugel]] | $O = 4\pi r^2$ | — |

### Prismen und Pyramiden

| Körper | Oberfläche |
|--------|------------|
| [[04-Prisma\|Prisma]] | $O = 2G + M = 2G + U \cdot h$ |
| [[06-Pyramide\|Pyramide]] | $O = G + M = G + \frac{1}{2}U \cdot h_s$ |

## Mantelfläche vs. Gesamtoberfläche

### Definition

- **Mantelfläche (M):** Nur die Seitenfläche(n)
- **Gesamtoberfläche (O):** Mantelfläche + Grund-/Deckflächen

> [!tip] Wann welche Formel?
> - **Etikett, Anstrich außen:** Mantelfläche
> - **Verpackungsmaterial, kompletter Anstrich:** Gesamtoberfläche
> - **Offene Behälter:** Ohne Deckel berechnen

## Praktische Anwendungen

### Materialverbrauch

> [!example] Beispiel 1: Blechdose
> Eine zylindrische Dose ($r = 4$ cm, $h = 12$ cm) wird aus Blech gefertigt.
> 
> **Blechbedarf:**
> $$O = 2\pi \cdot 4 \cdot (4 + 12) = 128\pi \approx 402 \text{ cm}^2$$

### Anstrich und Lackierung

> [!example] Beispiel 2: Kugeltank
> Ein kugelförmiger Tank ($r = 1{,}5$ m) wird lackiert.
> 
> **Lackfläche:**
> $$O = 4\pi \cdot 1{,}5^2 = 9\pi \approx 28{,}3 \text{ m}^2$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - **Säulen:** $O = 2G + M$
> - **Spitzen:** $O = G + M$
> - **Kugel:** $O = 4\pi r^2$
> - Mantelfläche für Seitenflächen, Gesamtoberfläche für komplette Hülle

---

**Navigation:** [[09-Volumenberechnung|← Volumenberechnung]] | [[11-Zusammengesetzte-Koerper|Zusammengesetzte Körper →]]
