---
title: "Rundungsregeln"
chapter: "04"
section: "03"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Die Rundungsregeln korrekt anwenden können"
  - "Auf verschiedene Stellenwerte runden können"
  - "Die Bedeutung von Genauigkeit verstehen"
  - "Rundungsfehler einschätzen können"
tags:
  - mathematik
  - dezimalzahlen
  - runden
  - genauigkeit
created: 2026-10-13
modified: 2026-10-13
---

# Rundungsregeln

> [!info] Lernziele
> - Die Rundungsregeln korrekt anwenden können
> - Auf verschiedene Stellenwerte runden können
> - Die Bedeutung von Genauigkeit verstehen
> - Rundungsfehler einschätzen können

## Überblick

Runden ist das Ersetzen einer Zahl durch einen Näherungswert mit weniger Stellen. Es dient der Vereinfachung von Zahlen und der Darstellung sinnvoller Genauigkeit.

## Grundregeln des Rundens

### Die Rundungsregel

1. **Ziffer < 5:** Abrunden (Rundungsziffer bleibt)
2. **Ziffer ≥ 5:** Aufrunden (Rundungsziffer wird um 1 erhöht)

### Welche Ziffer entscheidet?

Die **erste wegfallende Ziffer** (rechts von der Rundungsstelle) bestimmt die Richtung.

### Schema

```
    Rundungsstelle
         ↓
    23,4 | 7 2
         ↑
    Entscheidungsziffer (7 ≥ 5 → aufrunden)
    
    Ergebnis: 23,5
```

## Runden auf verschiedene Stellenwerte

### Auf Einer runden

| Zahl | Entscheidungsziffer | Ergebnis |
|------|---------------------|----------|
| 3,2 | 2 < 5 | 3 |
| 7,8 | 8 ≥ 5 | 8 |
| 12,5 | 5 ≥ 5 | 13 |
| 99,6 | 6 ≥ 5 | 100 |

### Auf Zehntel runden

| Zahl | Entscheidungsziffer | Ergebnis |
|------|---------------------|----------|
| 2,34 | 4 < 5 | 2,3 |
| 5,67 | 7 ≥ 5 | 5,7 |
| 8,951 | 5 ≥ 5 | 9,0 |

### Auf Hundertstel runden

| Zahl | Entscheidungsziffer | Ergebnis |
|------|---------------------|----------|
| 3,142 | 2 < 5 | 3,14 |
| 2,718 | 8 ≥ 5 | 2,72 |
| 1,995 | 5 ≥ 5 | 2,00 |

### Auf Zehner runden

| Zahl | Entscheidungsziffer | Ergebnis |
|------|---------------------|----------|
| 123 | 3 < 5 | 120 |
| 567 | 7 ≥ 5 | 570 |
| 1495 | 5 ≥ 5 | 1500 |

## Besondere Fälle

### Die Ziffer 5

> [!note] Konvention
> Bei der Entscheidungsziffer 5 wird in der Schulmathematik immer **aufgerundet**.

**Beispiel:** 2,5 → 3 (nicht 2)

### Kettenrunden (schrittweises Runden)

> [!warning] Achtung
> Nicht in mehreren Schritten runden! Immer die Originalzahl betrachten.

**Beispiel:** 2,449 auf Zehntel runden

| Methode | Vorgehensweise | Ergebnis |
|---------|----------------|----------|
| **Falsch** | 2,449 → 2,45 → 2,5 | 2,5 |
| **Richtig** | 2,449 → direkt auf Zehntel | 2,4 |

Die Entscheidungsziffer ist 4 (< 5), also wird abgerundet.

### Überlauf beim Runden

Manchmal erhöht sich durch Aufrunden auch die nächsthöhere Stelle:

- 9,97 auf Zehntel: 9,9 + 0,1 = **10,0**
- 99,95 auf Zehntel: **100,0**

## Sinnvolles Runden

### Kontextabhängige Genauigkeit

| Kontext | Sinnvolle Genauigkeit |
|---------|----------------------|
| Geldbeträge | 2 Nachkommastellen (Cent) |
| Körpergröße | Ganze cm oder 0,5 cm |
| Temperatur | 1 Nachkommastelle |
| Prozente (Alltag) | Ganze Prozent |
| Wissenschaft | Je nach Messgenauigkeit |

### Scheingenauigkeit vermeiden

> [!warning] Scheingenauigkeit
> Eine Rechnung kann nicht genauer sein als die ungenaueste Eingangsgröße.

**Beispiel:**
- Strecke: ca. 12 km
- Zeit: 2,5 h
- Geschwindigkeit: 12 ÷ 2,5 = 4,8 km/h ✓
- **Nicht:** 4,800000 km/h ✗

## Rundungsfehler

### Absoluter Fehler

Der **absolute Rundungsfehler** ist die Differenz zwischen gerundeter und exakter Zahl.

**Beispiel:** 3,14 statt 3,14159...
- Absoluter Fehler: |3,14 - 3,14159| ≈ 0,00159

### Relativer Fehler

Der **relative Rundungsfehler** setzt den absoluten Fehler ins Verhältnis zum Wert.

**Formel:** Relativer Fehler = Absoluter Fehler / Exakter Wert

### Fehlerfortpflanzung

Bei mehreren Rundungen können sich Fehler aufaddieren:

```
1,4 × 2,3 × 1,7 = ?

Exakt: 1,4 × 2,3 × 1,7 = 5,474
Mit Zwischenrundung: 1,4 × 2,3 = 3,2 → 3,2 × 1,7 = 5,44
Differenz: 0,034
```

> [!tip] Empfehlung
> Bei Kettenrechnungen erst am Ende runden!

## Kaufmännisches Runden

Im kaufmännischen Bereich gelten dieselben Regeln, mit besonderer Bedeutung:

### Geldbeträge

- Immer auf 2 Nachkommastellen (Cent) runden
- 12,345 € → 12,35 €
- 12,344 € → 12,34 €

### Stückzahlen

- Auf ganze Zahlen runden
- Manchmal: immer aufrunden (z.B. benötigte Fliesen)

## Zusammenhänge

### Beziehung zu anderen Themen

- **Dezimalzahlen:** Runden reduziert Nachkommastellen
- **Prozentrechnung:** Ergebnisse werden oft gerundet
- **Überschlagsrechnung:** Extremes Runden zur Kontrolle

### Voraussetzungen

- [[01-Dezimalzahlen]] - Stellenwertsystem
- [[02-Rechnen-mit-Dezimalzahlen]] - Rechenoperationen

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Mittel
> Richtiges Runden wird in fast jeder Aufgabe erwartet, besonders bei Geldbeträgen und Prozentaufgaben.

## Typische Prüfungsfragen

1. **Runden:** Runde 12,7489 auf Zehntel / Hundertstel / Einer.
2. **Geldbeträge:** Der Preis beträgt 23,456 €. Wie viel muss bezahlt werden?
3. **Fehler:** Welchen maximalen Rundungsfehler hat eine auf Zehntel gerundete Zahl?
4. **Anwendung:** Ein Auto fährt 127,3 km in 1,8 h. Berechne die Durchschnittsgeschwindigkeit sinnvoll gerundet.

## Quellen

- Lambacher Schweizer Mathematik 6
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[04-Einfuehrung-in-die-Prozentrechnung]] - Anwendung beim Prozentrechnen
- [[02-Grundrechenarten-und-Rechengesetze/06-Schriftliche-Division|Schriftliche Division]] - Ergebnisse runden
