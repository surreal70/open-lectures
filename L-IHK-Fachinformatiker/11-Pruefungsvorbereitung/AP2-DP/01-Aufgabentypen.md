---
title: "AP2 Daten- und Prozessanalyse – Aufgabentypen"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - pruefung
  - ap2
  - daten-prozessanalyse
  - aufgabentypen
source: proTirone (CC-BY-4.0)
---

# AP2 Daten- und Prozessanalyse – Aufgabentypen

> [!info] Übersicht
> Typische Aufgabenformate in der schriftlichen AP2-Prüfung für die Fachrichtung Daten- und Prozessanalyse.

## Häufige Aufgabentypen

### 1. Prozessmodellierung

- **BPMN-Diagramme** lesen und erstellen
- **EPK-Diagramme** lesen und erstellen
- **Sequenzdiagramme** analysieren
- **Flussdiagramme** erstellen

→ Siehe [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/01-Prozessdokumentation/02-BPMN|BPMN]], [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/01-Prozessdokumentation/03-EPK|EPK]]

### 2. Algorithmen / Pseudocode

Typische Anforderungen:
- Funktion schreiben, die eine Liste verarbeitet
- Statistische Kennzahlen berechnen
- Datensätze filtern und aggregieren

> [!tip] Herangehensweise (Bottom-Up)
> 1. Funktionsheader oben hinschreiben
> 2. Return-Statement am Ende hinschreiben
> 3. Berechnung des Return-Werts davor schreiben
> 4. Variablen und Schleifen von oben auffüllen

### 3. Statistische Berechnungen

Häufig gefragt:
- Mittelwert, Median
- Varianz, Standardabweichung
- Verhältnisse / Anteile berechnen
- DPMO / Six Sigma

→ Siehe [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/05-Statistik/01-Grundlagen|Statistik-Grundlagen]]

### 4. Prozessanalyse-Methoden

- **FMEA**: RPZ berechnen (B × A × E)
- **ABC-Analyse**: Klassifizieren nach Pareto
- **Ishikawa**: Ursachen kategorisieren

→ Siehe [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/02-Prozessanalyse/01-FMEA|FMEA]]

### 5. Kapazitätsberechnungen

Typische Rechnung:
```
Gesamtmenge ÷ Anzahl Einheiten = Menge pro Einheit
Zeitraum ÷ Bearbeitungszeit = Kapazität pro Einheit
Menge pro Einheit ÷ Kapazität = Benötigte Einheiten
+ Reserve (z.B. 5%) = Gesamtbedarf
```

### 6. Datenqualität

- Qualitätskriterien benennen
- Plausibilitätsprüfungen beschreiben
- CRISP-DM Phasen kennen

→ Siehe [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/04-Datenqualitaet/01-Qualitaetskriterien|Qualitätskriterien]]

## Pseudocode-Konventionen

In der Prüfung wird oft eine Mischform akzeptiert:

```
FUNKTION Name(parameter: Typ) : RückgabeTyp
  // Kommentar
  variable = Wert
  
  FÜR element IN liste:
    WENN bedingung:
      // Aktion
    SONST:
      // Alternative
  
  RÜCKGABE ergebnis
```

> [!warning] Wichtig
> Der Pseudocode muss **nicht** kompilierbar sein, aber **logisch korrekt**!

## Punkte-Zeit-Verhältnis

| Punkte | ca. Minuten |
|--------|-------------|
| 5 | 5 |
| 10 | 10 |
| 15 | 15 |
| 20 | 20 |

> [!tip] Zeitmanagement
> Bei 90 Minuten Prüfungszeit ≈ 1 Punkt pro Minute. Nicht zu lange an einer Aufgabe hängen!

## Querverweise

- → [[02-Beispiel-2023SO|Beispiel 2023 Sommer]]
- → [[03-Beispiel-2024SO|Beispiel 2024 Sommer]]
- → [[../00-Pruefung-Index|Prüfungsübersicht]]

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
