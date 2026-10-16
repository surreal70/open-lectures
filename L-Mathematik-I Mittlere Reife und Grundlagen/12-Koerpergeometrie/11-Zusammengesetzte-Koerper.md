---
title: Zusammengesetzte Körper
chapter: "12"
section: "12.11"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
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

## Strategien

### Addition

Körper besteht aus mehreren Grundkörpern:
$$V_{gesamt} = V_1 + V_2 + ...$$

### Subtraktion

Hohlräume oder Bohrungen:
$$V_{gesamt} = V_{außen} - V_{innen}$$

## Beispiele

> [!example] Beispiel 1: Silo (Zylinder + Kegel)
> Zylinder: $r = 3$ m, $h = 8$ m  
> Kegel (Dach): $r = 3$ m, $h = 2$ m
> 
> $$V = \pi \cdot 3^2 \cdot 8 + \frac{1}{3}\pi \cdot 3^2 \cdot 2 = 72\pi + 6\pi = 78\pi \approx 245 \text{ m}^3$$

> [!example] Beispiel 2: Würfel mit Bohrung
> Würfel: $a = 10$ cm  
> Zylindrische Bohrung: $r = 2$ cm
> 
> $$V = 10^3 - \pi \cdot 2^2 \cdot 10 = 1000 - 40\pi \approx 874 \text{ cm}^3$$

## Oberflächenberechnung

Bei Oberflächen: **Berührungsflächen abziehen!**

$$O_{gesamt} = O_1 + O_2 - 2 \cdot A_{Kontakt}$$

---

**Navigation:** [[10-Oberflaechenberechnung|← Oberflächenberechnung]] | [[12-Praktische-Berechnungen|Praktische Berechnungen →]]
