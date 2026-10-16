---
title: "Datenvisualisierung"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - statistik
  - datenvisualisierung
  - diagramme
  - excel
source: proTirone (CC-BY-4.0)
---

# Datenvisualisierung

> [!info] Lernziele
> - Geeignete Diagrammtypen auswählen können
> - Diagramme in Excel/LibreOffice erstellen
> - Aussagen aus Visualisierungen ableiten

## Definition

**Datenvisualisierung** = Grafische Aufbereitung von Daten zwecks Ableitung von Aussagen anhand visueller Auffälligkeiten.

## Diagrammtypen

### Linien- und Flächendiagramme

**Einsatz:** Darstellung des Werteverlaufs über die Zeit

```
Wert
  │
  │    ╭─╮
  │   ╱  ╲    ╭──
  │  ╱    ╲  ╱
  │ ╱      ╲╱
  └─────────────────▶ Zeit
```

**Geeignet für:**
- Zeitreihen (Temperaturverlauf, Aktienkurse)
- Trends erkennen
- Vergleich mehrerer Zeitreihen

### Balkendiagramme

**Einsatz:** Konfrontativer Vergleich von erreichten Werten pro Werteträger

```
        ████████████  42%
        ████████      31%
        █████         19%
        ██             8%
```

**Geeignet für:**
- Wahlergebnisse
- Umsatz pro Produkt
- Vergleich diskreter Kategorien

### Tortendiagramme (Kreisdiagramme)

**Einsatz:** Darstellung von Anteilen an einer Gesamtanzahl

```
         ╭───────╮
       ╱    42%    ╲
      │             │
      │    31%   19%│
       ╲    8%    ╱
         ╰───────╯
```

**Geeignet für:**
- Marktanteile
- Budgetverteilung
- Zusammensetzung eines Ganzen

> [!warning] Einschränkung
> Tortendiagramme funktionieren nur bei wenigen Kategorien gut. Bei mehr als 5–6 Segmenten wird die Darstellung unübersichtlich.

### Streudiagramm (Scatter Plot)

**Einsatz:** Verteilung von zweidimensionalen Messungen zwecks Einteilung in Gruppen

```
Y │
  │      ·  ·
  │    · ·  · ·
  │  ·  ··    ·
  │    ·
  └─────────────▶ X
```

**Geeignet für:**
- Korrelationen erkennen
- Cluster identifizieren
- Ausreißer finden

### Blasendiagramm

**Einsatz:** Verteilung von dreidimensionalen Messungen

Die dritte Dimension wird durch die Größe der Blasen dargestellt.

**Geeignet für:**
- Drei Variablen gleichzeitig darstellen
- Marktpositionierung (Größe = Umsatz)

### Wortwolken (Word Cloud)

**Einsatz:** Assoziative Begriffsdarstellung mit Gewichtung per Größe

```
      Qualität
   Prozess    DATEN
     Analyse
  Statistik   FMEA
```

**Geeignet für:**
- Häufigkeitsverteilung von Begriffen
- Textanalysen
- Übersichtliche Darstellung von Keywords

## Praxisanleitung: Diagramme in Excel/Calc

### Schritte zur Erstellung

1. **CSV-Daten laden** in LibreOffice Calc (oder Excel)
2. **Datentypen konvertieren**: Text in intendierte Typen (Datum, Zeit, Zahlen)
3. **Diagrammtyp auswählen** (Einfügen → Diagramm)
4. **Datenranges zusammenstellen** (Spalten markieren)
5. **Achsenbeschriftungen** hinzufügen
6. **Titel und Legende** einfügen

### Wahl des richtigen Diagrammtyps

| Fragestellung | Diagrammtyp |
|---------------|-------------|
| Wie entwickelt sich X über die Zeit? | Liniendiagramm |
| Wie verteilt sich X auf Kategorien? | Balkendiagramm |
| Welchen Anteil hat X am Ganzen? | Tortendiagramm |
| Gibt es einen Zusammenhang zwischen X und Y? | Streudiagramm |
| Wie verteilen sich drei Variablen? | Blasendiagramm |

> [!warning] Achtung
> Nicht alle Diagrammtypen sind für alle Daten visuell angemessen:
> - Zeitverläufe: Liniendiagramm ✓, Tortendiagramm ✗
> - Anteile: Tortendiagramm ✓, Liniendiagramm ✗
> - Aggregierte Balkendarstellungen: Oft schwer verständlich

## Auswertungsstrategie

### Intuitives Verfahren

1. **Normalität ermitteln**: Mittelwert, Median, Trends identifizieren
2. **Ausreißer finden**: Peaks, ungewöhnliche Abweichungen markieren
3. **Gründe suchen**: Warum gibt es diese Abweichungen?

### Beispiel: Blutdruckmessung

- **Trend:** Abfallende Systole-Werte deuten auf Medikamentenwirkung
- **Ausreißer:** Plötzliche Peaks können auf vergessene Einnahme hinweisen
- **Korrelation:** Negativer Zusammenhang zwischen Systole und Puls

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welcher Diagrammtyp eignet sich für welche Daten?
> - Interpretieren Sie das gezeigte Diagramm
> - Welche Erkenntnisse lassen sich aus der Visualisierung ableiten?

## Querverweise

- → [[01-Grundlagen|Statistische Grundlagen]] – Kennzahlen für Analyse
- → [[../02-Datenaufbereitung/01-Datenanalyse|Datenanalyse]] – Datenbereinigung vor Visualisierung
- → [[../03-Datenqualitaet/01-Qualitaetskriterien|Datenqualität]] – Qualität der Ausgangsdaten

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
