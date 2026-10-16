---
title: "Entscheidungsmatrix und Nutzwertanalyse"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - entscheidungsmatrix
  - nutzwertanalyse
  - bewertung
source: proTirone (CC-BY-4.0)
---

# Entscheidungsmatrix und Nutzwertanalyse

> [!info] Lernziele
> - Nutzwertanalyse durchführen können
> - Entscheidungsmatrix erstellen und auswerten
> - Kriteriengewichtung verstehen und anwenden

## Nutzwertanalyse

### Definition

Die **Nutzwertanalyse** ist eine systematische Methode zur Bewertung von Alternativen, die:

- Qualitative **und** quantitative Kriterien einbezieht
- Eine geordnete Entscheidungsfindung ermöglicht
- Subjektive Bewertungen transparent macht

### Vorgehensweise

1. **Alternativen auflisten**: Alle zu bewertenden Optionen
2. **Kriterien definieren**: Relevante Bewertungsmaßstäbe
3. **Gewichtung festlegen**: Relative Wichtigkeit der Kriterien (Summe = 1)
4. **Werte ermitteln**: Für jede Alternative pro Kriterium
5. **Gewichtete Werte berechnen**: Kriteriumswert × Gewicht
6. **Gesamtnutzen summieren**: Alle gewichteten Werte addieren

### Beispiel: Prozessalternativen vergleichen

**Randbedingungen:**
- Drei Prozessschritte Ps1, Ps2, Ps3 mit gleicher Funktion
- Kriterien: Kosten (€/Durchlauf), Zeit (h/Durchlauf)
- Gewichtung: Zeit 70%, Kosten 30%

| PS | €/DL | h/DL | gew. Kosten | gew. Zeit | Nutzwert |
|----|------|------|-------------|-----------|----------|
| Ps1 | 100 | 5 | 100 × 0,3 = 30 | 5 × 0,7 = 3,5 | **33,5** |
| Ps2 | 200 | 2 | 200 × 0,3 = 60 | 2 × 0,7 = 1,4 | 61,4 |
| Ps3 | 50 | 6 | 50 × 0,3 = 15 | 6 × 0,7 = 4,2 | 19,2 |

> [!tip] Interpretation
> Je **niedriger** der Nutzwert (bei Kosten/Zeit), desto **besser** die Alternative.
> **Gewinner: Ps3** mit dem niedrigsten Gesamtnutzwert.

### Bewertung der Methode

| Vorteile | Nachteile |
|----------|-----------|
| Mathematisch nachvollziehbar | Kriterienwahl beeinflusst Ergebnis |
| Transparente Entscheidung | Gewichtung ist subjektiv |
| Vergleichbarkeit | Aufwendige mathematische Absicherung |

## Entscheidungsmatrix

### Definition

Die **Entscheidungsmatrix** ist eine vereinfachte tabellarische Form zur Alternativenbewertung mit Punktevergabe.

### Vorgehensweise

1. **Punkteskala** konzipieren (z.B. 1–10)
2. **Kriteriumsgewichtung** festlegen
3. **Punkte vergeben** pro Kriterium und Alternative
4. **Gewichtete Punkte** berechnen
5. **Summe** der gewichteten Punkte bilden

### Beispiel mit Punkteskala

**Bewertungsskala:** 1 (schlecht) bis 10 (sehr gut)

| Kriterium | Gewicht | Software A | Software B | Software C |
|-----------|---------|------------|------------|------------|
| Funktionsumfang | 0,4 | 8 × 0,4 = 3,2 | 6 × 0,4 = 2,4 | 9 × 0,4 = 3,6 |
| Benutzerfreundlichkeit | 0,3 | 7 × 0,3 = 2,1 | 9 × 0,3 = 2,7 | 5 × 0,3 = 1,5 |
| Preis | 0,2 | 5 × 0,2 = 1,0 | 8 × 0,2 = 1,6 | 4 × 0,2 = 0,8 |
| Support | 0,1 | 6 × 0,1 = 0,6 | 7 × 0,1 = 0,7 | 8 × 0,1 = 0,8 |
| **Gesamt** | **1,0** | **6,9** | **7,4** | **6,7** |

> [!success] Ergebnis
> **Software B** gewinnt mit 7,4 Punkten.

## Prozessanalysekennzahlen

Für die Bewertung von Prozessen sind folgende Kennzahlen relevant:

| Kennzahl | Definition |
|----------|------------|
| **Wirtschaftlichkeit** | Wirkung(Prozess) > Aufwand(Prozess) |
| **Rentabilität** | val(Output) > val(Input) |
| **Produktivität** | val(Output) / val(Input) |
| **Amortisation** | Zeitpunkt, ab dem Gewinn > Investition |
| **Break-Even** | Zeitpunkt der Amortisation |

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Führen Sie für gegebene Alternativen eine Nutzwertanalyse durch
> - Was ist bei der Kriteriengewichtung zu beachten?
> - Unterschied zwischen Nutzwertanalyse und Entscheidungsmatrix?

## Querverweise

- → [[01-FMEA|FMEA]] – Risikobewertung von Fehlern
- → [[02-ABC-Analyse|ABC-Analyse]] – Priorisierung nach Bedeutung
- → [[06-Six-Sigma|Six Sigma]] – Prozessqualitätskennzahlen

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
