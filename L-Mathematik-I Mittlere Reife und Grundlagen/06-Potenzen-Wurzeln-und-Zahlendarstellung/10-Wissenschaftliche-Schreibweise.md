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
modified: 2025-06-26
---

# Wissenschaftliche Schreibweise

> [!info] Lernziele
> - Zahlen in wissenschaftlicher Schreibweise darstellen
> - Von wissenschaftlicher in Dezimalschreibweise umwandeln
> - Mit Zahlen in wissenschaftlicher Schreibweise rechnen
> - Größenordnungen abschätzen

## Überblick

Die **wissenschaftliche Schreibweise** (Exponentialschreibweise) stellt Zahlen als Produkt einer Zahl zwischen 1 und 10 und einer Zehnerpotenz dar.

Diese Notation ist unverzichtbar in Wissenschaft und Technik, wo man regelmäßig mit extrem großen oder kleinen Zahlen arbeitet. Statt 299.792.458 m/s (Lichtgeschwindigkeit) schreibt man kompakt $2{,}998 \times 10^8$ m/s. Statt 0,000000000001 m (Durchmesser eines Wasserstoffatoms) schreibt man $1 \times 10^{-12}$ m.

Die wissenschaftliche Schreibweise wurde im 20. Jahrhundert mit dem Aufkommen der modernen Physik populär, als Wissenschaftler wie **Albert Einstein** und **Niels Bohr** mit atomaren und kosmischen Größenordnungen arbeiteten. Heute ist sie Standard in allen Naturwissenschaften und auf jedem wissenschaftlichen Taschenrechner zu finden (oft als „SCI" oder „EXP" Modus).

> [!note] **Vorteile der wissenschaftlichen Schreibweise**
> - **Kompaktheit**: Sehr große/kleine Zahlen werden übersichtlich
> - **Genauigkeit**: Die Anzahl signifikanter Stellen ist sofort erkennbar
> - **Rechenfreundlichkeit**: Multiplikation/Division wird einfacher
> - **Vergleichbarkeit**: Größenordnungen lassen sich schnell einschätzen

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

> [!note] **Größenordnungen im Universum**
> Die wissenschaftliche Schreibweise macht die unvorstellbaren Dimensionen des Universums handhabbar:
>
> | Objekt/Entfernung | Größe |
> |-------------------|-------|
> | Durchmesser eines Protons | $\approx 10^{-15}$ m |
> | Durchmesser eines Atoms | $\approx 10^{-10}$ m |
> | Durchmesser eines Haares | $\approx 10^{-4}$ m |
> | Höhe eines Menschen | $\approx 10^{0}$ m = 1 m |
> | Höhe des Mt. Everest | $\approx 10^{4}$ m |
> | Entfernung zum Mond | $\approx 10^{8}$ m |
> | Entfernung zur Sonne | $\approx 10^{11}$ m |
> | Durchmesser der Milchstraße | $\approx 10^{21}$ m |
>
> Vom Proton bis zur Galaxis – 36 Größenordnungen Unterschied!

> [!tip] **Taschenrechner-Eingabe**
> Auf Taschenrechnern wird die wissenschaftliche Schreibweise oft verkürzt dargestellt:
> - $3{,}2 \times 10^5$ erscheint als `3.2E5` oder `3.2×10⁵`
> - $4{,}5 \times 10^{-3}$ erscheint als `4.5E-3`
>
> Die Taste heißt oft „EXP", „EE" oder „×10ˣ".

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
