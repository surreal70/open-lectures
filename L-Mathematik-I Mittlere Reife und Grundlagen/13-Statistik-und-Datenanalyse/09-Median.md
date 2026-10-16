---
title: Median (Zentralwert)
chapter: "13"
section: "13.9"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/statistik
  - median
  - lageparameter
---

# Median (Zentralwert)

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Den Median bestimmen
> - Median und Mittelwert vergleichen
> - Den geeigneten Lageparameter wählen

## Definition

> [!note] Definition
> Der **Median** ist der mittlere Wert einer geordneten Datenreihe. Er teilt die Daten in zwei gleich große Hälften.

## Berechnung

### Ungerade Anzahl

Bei $n$ Werten (ungerade): Median = $\left(\frac{n+1}{2}\right)$-ter Wert

> [!example] Beispiel
> Daten: 3, 7, 2, 9, 5
> Geordnet: 2, 3, **5**, 7, 9
> Median = 5

### Gerade Anzahl

Bei $n$ Werten (gerade): Median = Mittel der beiden mittleren Werte

> [!example] Beispiel
> Daten: 4, 8, 2, 6, 1, 9
> Geordnet: 1, 2, **4**, **6**, 8, 9
> Median = $\frac{4 + 6}{2} = 5$

## Vergleich mit Mittelwert

> [!example] Einkommensbeispiel
> Einkommen: 2000, 2100, 2200, 2300, 50000 €
> 
> - **Mittelwert:** 11.720 €
> - **Median:** 2.200 €
> 
> Der Median ist robuster gegen Ausreißer!

## Wann welchen Wert?

| Situation | Empfehlung |
|-----------|------------|
| Symmetrische Verteilung | Mittelwert |
| Ausreißer vorhanden | Median |
| Ordinale Daten | Median |

---

**Navigation:** [[08-Arithmetisches-Mittel|← Arithmetisches Mittel]] | [[10-Modalwert|Modalwert →]]
