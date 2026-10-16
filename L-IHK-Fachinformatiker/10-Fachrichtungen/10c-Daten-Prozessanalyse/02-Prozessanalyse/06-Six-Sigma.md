---
title: "Six Sigma und DMAIC"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - six-sigma
  - dmaic
  - dpmo
  - qualitaetsmanagement
source: proTirone (CC-BY-4.0)
---

# Six Sigma und DMAIC

> [!info] Lernziele
> - DMAIC-Zyklus verstehen und anwenden
> - DPMO berechnen können
> - Six-Sigma-Levels interpretieren

## DMAIC-Prozess

**DMAIC** ist der Kernprozess des Six-Sigma-Qualitätsmanagements:

| Phase | Englisch | Deutsch | Aktivität |
|-------|----------|---------|-----------|
| **D** | Define | Definieren | Sollzustand und Fehlerdefinition |
| **M** | Measure | Messen | Daten über IST-Zustand sammeln |
| **A** | Analyse | Analysieren | Ursachen für Abweichungen finden |
| **I** | Improve | Verbessern | Lösungen entwickeln und umsetzen |
| **C** | Control | Steuern | Verbesserungen im Alltag verankern |

```
    ┌─────────┐
    │ DEFINE  │ ──▶ Was ist der Fehler? Was ist das Ziel?
    └────┬────┘
         │
    ┌────▼────┐
    │ MEASURE │ ──▶ Wie messen wir den aktuellen Zustand?
    └────┬────┘
         │
    ┌────▼────┐
    │ ANALYSE │ ──▶ Warum weichen wir vom Ziel ab?
    └────┬────┘
         │
    ┌────▼────┐
    │ IMPROVE │ ──▶ Wie beheben wir die Ursachen?
    └────┬────┘
         │
    ┌────▼────┐
    │ CONTROL │ ──▶ Wie sichern wir die Verbesserung?
    └─────────┘
```

## DPMO – Defects Per Million Opportunities

### Definition

**DPMO** gibt an, wie viele Fehler pro eine Million Möglichkeiten auftreten.

### Berechnung

$$DPMO = \frac{D}{N \times O} \times 1.000.000$$

| Variable | Bedeutung |
|----------|-----------|
| **D** | Anzahl der gemessenen Fehler |
| **N** | Anzahl der produzierten/geprüften Einheiten |
| **O** | Anzahl möglicher Fehler pro Einheit (Opportunities) |

### Beispiel: Blutdruckmessung

> 1. 163 Messungen zwischen 05/2024 und 03/2025: **N = 163**
> 2. Zwei Fehlerarten möglich (Datum falsch, Werte vertauscht): **O = 2**
> 3. 10× nur Datum falsch, 24× beide Fehler: **D = 10 + 24×2 = 58**
> 4. Berechnung:

$$DPMO = \frac{58}{163 \times 2} \times 1.000.000 = 177.914$$

> [!note] Interpretation
> Mit DPMO ≈ 178.000 liegt der Prozess zwischen Sigma-Level 2 und 3.

## Six Sigma Levels

| Sigma | DPMO | Fehlerquote | Fehlerfreiheit |
|-------|------|-------------|----------------|
| 1σ | 691.462 | 69,15% | 30,85% |
| 2σ | 308.538 | 30,85% | 69,15% |
| 3σ | 66.807 | 6,68% | 93,32% |
| 4σ | 6.210 | 0,62% | 99,38% |
| 5σ | 233 | 0,023% | 99,977% |
| **6σ** | **3,4** | **0,00034%** | **99,99966%** |
| 7σ | 0,019 | 0,0000019% | 99,9999981% |

> [!tip] Six-Sigma-Ziel
> Das Ziel von Six Sigma ist ein DPMO-Wert von maximal **3,4** – praktisch nahezu fehlerfreie Prozesse.

## Normalverteilung und Six Sigma

Die Six-Sigma-Methodik basiert auf der **Normalverteilung** (Gauß'sche Glockenkurve):

- Prozessergebnisse schwanken um einen Erwartungswert
- Kleinere Abweichungen treten häufiger auf als große
- σ (Sigma) = Standardabweichung = Maß für die Streuung

```
Häufigkeit
    │
    │           ╭───╮
    │         ╭─╯   ╰─╮
    │       ╭─╯       ╰─╮
    │     ╭─╯           ╰─╮
    │   ╭─╯               ╰─╮
    └───┴───┬───┬───┬───┬───┴───▶ Wert
          -3σ -1σ  μ  +1σ +3σ
                  
    μ = Mittelwert (Erwartungswert)
    σ = Standardabweichung
```

**Verteilung der Werte:**
- ±1σ: ~68% aller Werte
- ±2σ: ~95% aller Werte
- ±3σ: ~99,7% aller Werte
- ±6σ: ~99,99966% aller Werte

## Verwandte Managementmethoden

### Kaizen / KVP

- **Kaizen** (japanisch: „Veränderung zum Besseren")
- **KVP** = Kontinuierlicher Verbesserungsprozess
- **CIP** = Continual Improvement Process

Leitfragen (PDCA-Zyklus):
| Phase | Frage |
|-------|-------|
| **Plan** | Wie soll es sein? |
| **Do** | Was tun wir aktuell wie? |
| **Check** | Was wurde erreicht? |
| **Act** | Was ist noch zu tun? |

### Lean Management

Fünf Prinzipien:
1. **Wert definieren** aus Kundensicht
2. **Wertstrom analysieren**
3. **Wertfluss sicherstellen** (keine Unterbrechungen)
4. **Pull-Prinzip** (Produktion auf Anfrage)
5. **Perfektion anstreben** (kontinuierliche Verbesserung)

### TQM – Total Quality Management

> „Optimierung der Qualität von Produkten und Dienstleistungen in allen Funktionsbereichen durch Mitwirkung aller Mitarbeiter."

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Wofür steht DMAIC?
> - Berechnen Sie den DPMO-Wert für gegebene Daten
> - Welchem Sigma-Level entspricht ein bestimmter DPMO-Wert?
> - Was ist der Unterschied zwischen Kaizen und Six Sigma?

## Querverweise

- → [[01-FMEA|FMEA]] – Fehlerbewertung
- → [[../04-Statistik/01-Grundlagen|Statistik-Grundlagen]] – Standardabweichung, Varianz
- → [[../03-Datenqualitaet/01-Qualitaetskriterien|Datenqualität]] – Qualitätsmerkmale

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
