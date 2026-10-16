---
title: "Dezimalzahlen"
chapter: "04"
section: "01"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Das Stellenwertsystem der Dezimalzahlen verstehen"
  - "Dezimalzahlen lesen und schreiben können"
  - "Dezimalzahlen am Zahlenstrahl einordnen"
  - "Zwischen Brüchen und Dezimalzahlen umwandeln"
tags:
  - mathematik
  - dezimalzahlen
  - stellenwert
  - zahlensysteme
created: 2026-10-13
modified: 2026-10-13
---

# Dezimalzahlen

> [!info] Lernziele
> - Das Stellenwertsystem der Dezimalzahlen verstehen
> - Dezimalzahlen lesen und schreiben können
> - Dezimalzahlen am Zahlenstrahl einordnen
> - Zwischen Brüchen und Dezimalzahlen umwandeln

## Überblick

Dezimalzahlen sind eine alternative Schreibweise für Brüche, die auf dem Stellenwertsystem mit der Basis 10 aufbaut. Sie ermöglichen eine einheitliche Darstellung von Zahlen und vereinfachen viele Rechenoperationen.

## Das Stellenwertsystem

### Aufbau einer Dezimalzahl

Eine Dezimalzahl besteht aus einem **Vorkommateil** (ganzer Teil) und einem **Nachkommateil** (dezimaler Teil), getrennt durch ein Komma:

```
    123,456
    ↑↑↑ ↑↑↑
    │││ │││
    │││ ││└── Tausendstel (1/1000)
    │││ │└─── Hundertstel (1/100)
    │││ └──── Zehntel (1/10)
    ││└────── Einer (1)
    │└─────── Zehner (10)
    └──────── Hunderter (100)
```

### Stellenwerttabelle

| Position | Name | Wert als Bruch | Wert als Potenz |
|----------|------|----------------|-----------------|
| 3 links vom Komma | Hunderter | 100 | 10² |
| 2 links vom Komma | Zehner | 10 | 10¹ |
| 1 links vom Komma | Einer | 1 | 10⁰ |
| 1 rechts vom Komma | Zehntel | 1/10 | 10⁻¹ |
| 2 rechts vom Komma | Hundertstel | 1/100 | 10⁻² |
| 3 rechts vom Komma | Tausendstel | 1/1000 | 10⁻³ |

### Beispiel: Stellenwertzerlegung

Die Zahl 45,372 bedeutet:
- 4 Zehner = 40
- 5 Einer = 5
- 3 Zehntel = 3/10 = 0,3
- 7 Hundertstel = 7/100 = 0,07
- 2 Tausendstel = 2/1000 = 0,002

**Summe:** 40 + 5 + 0,3 + 0,07 + 0,002 = 45,372

## Lesen und Schreiben von Dezimalzahlen

### Sprechweisen

| Dezimalzahl | Sprechweise |
|-------------|-------------|
| 0,5 | "null Komma fünf" oder "fünf Zehntel" |
| 3,14 | "drei Komma eins vier" oder "drei Komma vierzehn" |
| 0,007 | "null Komma null null sieben" oder "sieben Tausendstel" |
| 12,345 | "zwölf Komma drei vier fünf" |

> [!tip] Merkhilfe
> Nach dem Komma werden die Ziffern einzeln gelesen: 2,45 = "zwei Komma vier fünf" (nicht "zwei Komma fünfundvierzig")

### Führende und endständige Nullen

- **Führende Nullen** nach dem Komma sind bedeutsam: 0,07 ≠ 0,7
- **Endständige Nullen** ändern den Wert nicht: 3,50 = 3,5

## Umwandlung zwischen Brüchen und Dezimalzahlen

### Bruch → Dezimalzahl

**Methode:** Zähler durch Nenner dividieren

**Beispiele:**
- $\frac{1}{2} = 1 ÷ 2 = 0,5$
- $\frac{3}{4} = 3 ÷ 4 = 0,75$
- $\frac{1}{8} = 1 ÷ 8 = 0,125$

### Dezimalzahl → Bruch

**Methode:** Dezimalzahl als Bruch mit Zehnerpotenz im Nenner schreiben

**Beispiele:**
- $0,3 = \frac{3}{10}$
- $0,25 = \frac{25}{100} = \frac{1}{4}$
- $0,125 = \frac{125}{1000} = \frac{1}{8}$

### Wichtige Entsprechungen

| Bruch | Dezimalzahl | Bruch | Dezimalzahl |
|-------|-------------|-------|-------------|
| 1/2 | 0,5 | 1/5 | 0,2 |
| 1/4 | 0,25 | 2/5 | 0,4 |
| 3/4 | 0,75 | 3/5 | 0,6 |
| 1/8 | 0,125 | 4/5 | 0,8 |
| 1/10 | 0,1 | 1/3 | 0,333... |

## Abbrechende und periodische Dezimalzahlen

### Abbrechende Dezimalzahlen

Brüche, deren Nenner nur die Primfaktoren 2 und 5 enthält, ergeben **abbrechende** Dezimalzahlen:

- $\frac{1}{4} = \frac{1}{2^2} = 0,25$ ✓
- $\frac{3}{8} = \frac{3}{2^3} = 0,375$ ✓
- $\frac{7}{20} = \frac{7}{2^2 \cdot 5} = 0,35$ ✓

### Periodische Dezimalzahlen

Enthält der Nenner andere Primfaktoren, entsteht eine **periodische** Dezimalzahl:

- $\frac{1}{3} = 0,\overline{3} = 0,333...$
- $\frac{1}{6} = 0,1\overline{6} = 0,1666...$
- $\frac{1}{7} = 0,\overline{142857}$

> [!note] Notation
> Der sich wiederholende Teil (Periode) wird mit einem Überstrich gekennzeichnet: $0,\overline{3}$

## Dezimalzahlen am Zahlenstrahl

### Einordnung

```
    0    0,5    1    1,5    2    2,5    3
    |-----|-----|-----|-----|-----|-----|
              ↑
            1,25
```

### Zwischen zwei Dezimalzahlen

Zwischen je zwei Dezimalzahlen liegen unendlich viele weitere:
- Zwischen 0,1 und 0,2 liegt z.B.: 0,15, 0,12, 0,178, ...
- Zwischen 1,5 und 1,6 liegt z.B.: 1,55, 1,52, 1,599, ...

## Vergleichen von Dezimalzahlen

### Methode

1. Gleiche Anzahl an Nachkommastellen herstellen (durch Anhängen von Nullen)
2. Stellenweise von links nach rechts vergleichen

### Beispiel

Vergleiche 0,8 und 0,75:
1. Angleichen: 0,80 und 0,75
2. Vergleichen: 80 Hundertstel > 75 Hundertstel
3. **Ergebnis:** 0,8 > 0,75

## Zusammenhänge

### Beziehung zu anderen Themen

- **Bruchrechnung:** Dezimalzahlen sind eine alternative Darstellung von Brüchen
- **Stellenwertsystem:** Erweiterung des Systems für natürliche Zahlen
- **Prozentrechnung:** Prozente werden oft als Dezimalzahlen dargestellt (50% = 0,5)

### Voraussetzungen

- [[02-Grundrechenarten-und-Rechengesetze/00-Grundrechenarten-Index|Grundrechenarten]] - Division
- [[03-Bruchrechnung/00-Bruchrechnung-Index|Bruchrechnung]] - Grundverständnis

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Dezimalzahlen sind Grundlage für die Prozentrechnung und alle weiteren kaufmännischen Berechnungen.

## Typische Prüfungsfragen

1. **Umwandlung:** Wandle 3/8 in eine Dezimalzahl um.
2. **Stellenwert:** Welchen Wert hat die Ziffer 7 in der Zahl 24,375?
3. **Vergleichen:** Ordne die Zahlen 0,45; 0,405; 0,5 der Größe nach.
4. **Bruchdarstellung:** Schreibe 0,625 als vollständig gekürzten Bruch.

## Quellen

- Lambacher Schweizer Mathematik 6
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[02-Rechnen-mit-Dezimalzahlen]] - Rechenoperationen
- [[03-Rundungsregeln]] - Runden von Dezimalzahlen
- [[03-Bruchrechnung/11-Umwandlung-Brueche-Dezimalzahlen|Umwandlung Brüche-Dezimalzahlen]]
