---
title: Arithmetisches Mittel
chapter: "13"
section: "13.8"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/statistik
  - mittelwert
  - lageparameter
---

# Arithmetisches Mittel

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Das arithmetische Mittel berechnen
> - Vor- und Nachteile kennen
> - Den Durchschnitt interpretieren

## Definition

> [!note] Formel
> $$\bar{x} = \frac{x_1 + x_2 + ... + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}$$
> 
> **Arithmetisches Mittel** = Summe aller Werte geteilt durch Anzahl

## Berechnung

> [!example] Beispiel: Klassenarbeitsnoten
> Noten: 2, 3, 1, 4, 2, 3, 2, 5, 3, 2
> 
> $$\bar{x} = \frac{2+3+1+4+2+3+2+5+3+2}{10} = \frac{27}{10} = 2{,}7$$

## Mit Häufigkeitstabelle

> [!note] Gewichtete Formel
> $$\bar{x} = \frac{\sum (x_i \cdot H_i)}{n}$$

> [!example] Beispiel
> | Note $x$ | Häufigkeit $H$ | $x \cdot H$ |
> |---------|---------------:|------------:|
> | 1 | 2 | 2 |
> | 2 | 5 | 10 |
> | 3 | 8 | 24 |
> | 4 | 3 | 12 |
> | 5 | 2 | 10 |
> | **Σ** | **20** | **58** |
> 
> $$\bar{x} = \frac{58}{20} = 2{,}9$$

## Vor- und Nachteile

| Vorteile | Nachteile |
|----------|-----------|
| Berücksichtigt alle Werte | Anfällig für Ausreißer |
| Leicht zu berechnen | Nicht immer sinnvoll |
| Gut für weitere Berechnungen | Kann unrealistisch sein |

> [!warning] Ausreißer
> Einkommen: 2000, 2200, 2100, 2300, 50000 €
> $$\bar{x} = \frac{58600}{5} = 11720 \text{ €}$$
> 
> Das Mittel ist nicht repräsentativ!

---

**Navigation:** [[07-Histogramme|← Histogramme]] | [[09-Median|Median →]]
