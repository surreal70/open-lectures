---
title: "Wissenschaftliche Schreibweise"
chapter: "06"
section: "10"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Zahlen in wissenschaftlicher Schreibweise darstellen"
  - "Von wissenschaftlicher in Dezimalschreibweise umwandeln"
  - "Mit Zahlen in wissenschaftlicher Schreibweise rechnen"
  - "Größenordnungen abschätzen"
tags:
  - mathematik
  - wissenschaftlich
  - notation
  - zehnerpotenzen
created: 2026-10-13
modified: 2026-10-13
---

# Wissenschaftliche Schreibweise

> [!info] Lernziele
> - Zahlen in wissenschaftlicher Schreibweise darstellen
> - Von wissenschaftlicher in Dezimalschreibweise umwandeln
> - Mit Zahlen in wissenschaftlicher Schreibweise rechnen
> - Größenordnungen abschätzen

## Überblick

Die **wissenschaftliche Schreibweise** (Exponentialschreibweise) stellt Zahlen als Produkt einer Zahl zwischen 1 und 10 und einer Zehnerpotenz dar.

## Definition

> [!tip] Standardform
> $$a \times 10^n$$ mit $1 \leq a < 10$

## Umwandlung

### Große Zahlen → Wissenschaftliche Schreibweise

**Beispiel:** 4.500.000

1. Komma nach erste Ziffer: 4,5
2. Nullen zählen: 6 Stellen
3. **Ergebnis:** $4,5 \times 10^6$

### Kleine Zahlen → Wissenschaftliche Schreibweise

**Beispiel:** 0,00032

1. Komma nach erste Ziffer (≠0): 3,2
2. Stellen zählen: 4 nach links
3. **Ergebnis:** $3,2 \times 10^{-4}$

## Beispiele

| Dezimal | Wissenschaftlich |
|---------|------------------|
| 300.000.000 | $3 \times 10^8$ |
| 6.700.000 | $6,7 \times 10^6$ |
| 0,00045 | $4,5 \times 10^{-4}$ |
| 0,000000012 | $1,2 \times 10^{-8}$ |

## Rechnen

### Multiplikation

$$(a \times 10^m) \cdot (b \times 10^n) = (a \cdot b) \times 10^{m+n}$$

### Division

$$\frac{a \times 10^m}{b \times 10^n} = \frac{a}{b} \times 10^{m-n}$$

## Anwendungen

| Größe | Wert |
|-------|------|
| Lichtgeschwindigkeit | $3 \times 10^8$ m/s |
| Erdumfang | $4 \times 10^7$ m |
| Wasserstoffatom | $1 \times 10^{-10}$ m |

## Zusammenhänge

### Voraussetzungen

- [[05-Zehnerpotenzen]]
- [[04-Potenzen-mit-negativen-Exponenten]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Standard in Physik und Technik.

## Typische Prüfungsfragen

1. Schreibe wissenschaftlich: 45.000.000
2. Schreibe als Dezimalzahl: $2,5 \times 10^{-3}$
3. Berechne: $(3 \times 10^4) \cdot (2 \times 10^5)$

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[05-Zehnerpotenzen]]
- [[12-Anwendungen-in-Wissenschaft-und-Technik]]
