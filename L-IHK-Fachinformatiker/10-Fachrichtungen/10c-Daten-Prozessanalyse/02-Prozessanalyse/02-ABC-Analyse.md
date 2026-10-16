---
title: "ABC-Analyse"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - abc-analyse
  - priorisierung
  - pareto
source: proTirone (CC-BY-4.0)
---

# ABC-Analyse

> [!info] Lernziele
> - ABC-Analyse durchführen können
> - Klassen A, B, C korrekt zuordnen
> - Pareto-Prinzip verstehen und anwenden

## Definition

Die **ABC-Analyse** ist ein betriebswirtschaftliches Analyseverfahren zur Klassifizierung von Ereignissen in:

- **A**: Wichtige Fehler/Ereignisse
- **B**: Mittlere Fehler/Ereignisse  
- **C**: Unwichtige Fehler/Ereignisse

## Vorgehensweise

1. **Fehler ermitteln**: Alle relevanten Fehler auflisten
2. **Absoluten Schadenswert** pro Fehlertyp bestimmen
3. **Häufigkeit** pro Fehlertyp ermitteln
4. **Relativen Schadenswert** berechnen: `Häufigkeit × absoluter Schadenswert`
5. **Gesamtschaden** addieren: Summe aller relativen Schadenswerte
6. **Anteil** am Gesamtschaden pro Fehler berechnen
7. **Liste sortieren**: Absteigend nach Anteil
8. **Cluster bilden** (Klassifizierung):

| Klasse | Anteil am Gesamtschaden | Priorität |
|--------|-------------------------|-----------|
| **A** | Die ersten ~80% | Höchste |
| **B** | Die nächsten ~15% | Mittel |
| **C** | Die letzten ~5% | Niedrig |

## Pareto-Prinzip (80/20-Regel)

> [!tip] Kernaussage
> Kümmere dich zuerst um das, was 80% deiner Probleme verursacht. Oft verursachen 20% der Fehlerursachen 80% der Probleme.

## Berechnungsbeispiel: Füllernutzung

### Ausgangsdaten

| Prozessschritt | Fehler | Häufigkeit | Fehlerwert | Schaden |
|----------------|--------|------------|------------|---------|
| Füllerkauf | Haarriss im Kolben | 1 × 0,1 | 300 € | 30 € |
| Füllerkauf | Feder verbogen | 1 × 0,5 | 30 € | 15 € |
| Tintenkauf | Tinte vertrocknet | 50 × 0,2 | 10 € | 100 € |
| Befüllung | Kolbenüberlauf | 1000 × 0,2 | 1 € | 200 € |
| | | | **Summe:** | **345 €** |

### ABC-Klassifizierung

| Fehler | Anteil | Kumuliert | Klasse |
|--------|--------|-----------|--------|
| Kolbenüberlauf | 58% | 58% | **A** |
| Tinte vertrocknet | 29% | 87% | **A** |
| Haarriss im Kolben | 9% | 96% | **B** |
| Feder verbogen | 4% | 100% | **C** |

### Ergebnis

> [!success] Handlungsempfehlung
> Um den Füllerprozess um 80% zu verbessern:
> 1. Befüllungstechnik verbessern (Überlauf vermeiden)
> 2. Neuen Tintenlieferanten suchen (Qualitätsproblem)

## Visualisierung

```
Anteil am Gesamtschaden
│
│ ████████████████████████████████  58% ─┐
│ ████████████████                  29%  ├─ Klasse A (87%)
│ █████                              9%  ─── Klasse B
│ ██                                 4%  ─── Klasse C
└─────────────────────────────────────────
  Kolben-   Tinte    Haar-    Feder
  überlauf  trocken  riss     verbogen
```

## Anwendungsgebiete

- **Lagerhaltung**: Welche Artikel sind am wertvollsten?
- **Kundensegmentierung**: Welche Kunden bringen den meisten Umsatz?
- **Fehlermanagement**: Welche Fehler verursachen die meisten Kosten?
- **Zeitmanagement**: Welche Aufgaben haben die größte Wirkung?

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Wie werden die Klassen A, B, C definiert?
> - Welches Prinzip liegt der ABC-Analyse zugrunde?
> - Berechnen Sie für gegebene Daten eine ABC-Klassifizierung

## Querverweise

- → [[01-FMEA|FMEA]] – Alternative Priorisierungsmethode
- → [[03-Ishikawa|Ishikawa-Diagramm]] – Ursachenanalyse
- → [[04-Entscheidungsmatrix|Entscheidungsmatrix]] – Alternativenbewertung

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
