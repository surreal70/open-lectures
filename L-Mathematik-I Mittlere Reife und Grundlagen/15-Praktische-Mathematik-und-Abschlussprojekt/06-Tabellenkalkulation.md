---
title: Statistik mit Tabellenkalkulation
chapter: "15"
section: "15.6"
type: lecture
created: 2026-10-13
modified: 2025-07-18
status: draft - review pending
tags:
  - mathematik/statistik
  - tabellenkalkulation
  - excel
---

# Statistik mit Tabellenkalkulation

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Statistische Funktionen in Excel/Calc nutzen
> - Diagramme erstellen
> - Daten analysieren

Tabellenkalkulationsprogramme wie Microsoft Excel, Google Sheets oder LibreOffice Calc sind unverzichtbare Werkzeuge für die moderne Datenanalyse. Sie verbinden mathematische Berechnungen mit visueller Darstellung und ermöglichen es, große Datenmengen effizient zu verarbeiten.

### Warum Tabellenkalkulation lernen?

Die Beherrschung von Tabellenkalkulationen ist heute eine Schlüsselkompetenz:

| Bereich | Anwendung |
|---------|-----------|
| **Beruf** | Buchhaltung, Projektplanung, Controlling |
| **Studium** | Versuchsauswertung, statistische Analysen |
| **Privat** | Haushaltsbuch, Kostenvergleiche, Planung |

> [!note] **Geschichte der Tabellenkalkulation**
> Das erste erfolgreiche Tabellenkalkulationsprogramm war **VisiCalc** (1979), entwickelt für den Apple II. Es revolutionierte die Geschäftswelt und gilt als „Killer-App", die den Erfolg des Personal Computers begründete. Excel erschien erstmals 1985 für den Macintosh.

---

## Wichtige Funktionen

| Berechnung | Formel (Excel) |
|------------|----------------|
| Summe | =SUMME(A1:A10) |
| Mittelwert | =MITTELWERT(A1:A10) |
| Median | =MEDIAN(A1:A10) |
| Maximum | =MAX(A1:A10) |
| Minimum | =MIN(A1:A10) |
| Anzahl | =ANZAHL(A1:A10) |

### Syntax verstehen

Alle Formeln beginnen mit einem Gleichheitszeichen `=`. Der Bereich `A1:A10` bezeichnet alle Zellen von A1 bis A10 (insgesamt 10 Zellen).

> [!example] Beispiel: Notenberechnung
> In Spalte A stehen Prüfungsnoten: 2, 3, 1, 4, 2, 3, 2, 1
> 
> | Berechnung | Formel | Ergebnis |
> |------------|--------|----------|
> | Durchschnitt | =MITTELWERT(A1:A8) | 2,25 |
> | Beste Note | =MIN(A1:A8) | 1 |
> | Schlechteste | =MAX(A1:A8) | 4 |
> | Anzahl | =ANZAHL(A1:A8) | 8 |

### Weitere nützliche Funktionen

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| =RUNDEN(Zahl;Stellen) | Rundet auf Nachkommastellen | =RUNDEN(3,14159;2) → 3,14 |
| =WENN(Bedingung;Dann;Sonst) | Bedingte Berechnung | =WENN(A1>50;"Bestanden";"Nicht bestanden") |
| =ZÄHLENWENN(Bereich;Kriterium) | Zählt mit Bedingung | =ZÄHLENWENN(A1:A10;">5") |
| =WURZEL(Zahl) | Quadratwurzel | =WURZEL(16) → 4 |
| =POTENZ(Basis;Exponent) | Potenz berechnen | =POTENZ(2;10) → 1024 |

> [!tip] **Formelassistent nutzen**
> Tippen Sie `=` und den Funktionsnamen, dann drücken Sie **Tab** oder klicken auf die Funktion. Excel zeigt eine Hilfe mit den benötigten Argumenten an.

---

## Diagramme erstellen

1. Daten markieren
2. Einfügen → Diagramm
3. Diagrammtyp wählen
4. Beschriftungen hinzufügen

### Das richtige Diagramm wählen

| Diagrammtyp | Verwendung | Beispiel |
|-------------|------------|----------|
| **Säulen/Balken** | Kategorien vergleichen | Umsatz nach Monaten |
| **Linien** | Entwicklung über Zeit | Temperaturverlauf |
| **Kreis** | Anteile am Ganzen | Marktanteile |
| **Punkt (XY)** | Zusammenhänge zwischen Variablen | Korrelation Lernzeit/Note |

> [!warning] **Häufiger Fehler: Falscher Diagrammtyp**
> - Kreisdiagramme nur für Anteile eines Ganzen (Summe = 100%)
> - Keine 3D-Effekte verwenden – sie verzerren die Wahrnehmung
> - Achsen immer bei 0 beginnen lassen (sonst irreführend!)

### Diagrammgestaltung

Ein gutes Diagramm braucht:
- **Titel**: Was zeigt das Diagramm?
- **Achsenbeschriftung**: Was ist auf den Achsen?
- **Einheiten**: € , kg, Stück, ...
- **Legende**: Bei mehreren Datenreihen

> [!example] Professionelles Diagramm
> ```
> Monatlicher Stromverbrauch 2024 (kWh)
> 
> 400 ┤                      ╭──╮
>     │         ╭──╮        │  │
> 300 ┤    ╭──╮ │  │ ╭──╮   │  │
>     │╭──╮│  │ │  │ │  │╭──╮  │
> 200 ┤│  ││  │ │  │ │  ││  │  │
>     ││  ││  │ │  │ │  ││  │  │
> 100 ┤│  ││  │ │  │ │  ││  │  │
>     └┴──┴┴──┴─┴──┴─┴──┴┴──┴──┴─
>      Jan Feb Mär Apr Mai Jun
> ```

---

## Tipps

- Absolute Bezüge mit $ (z.B. $A$1)
- Bedingte Formatierung für Visualisierung
- Sortieren und Filtern für große Datenmengen

### Absolute vs. relative Bezüge

Das Dollarzeichen `$` fixiert Zeilen- oder Spaltenbezüge beim Kopieren:

| Bezug | Bedeutung | Beim Kopieren nach rechts/unten |
|-------|-----------|--------------------------------|
| A1 | Relativ | Ändert sich mit (B2, C3, ...) |
| $A$1 | Absolut | Bleibt immer A1 |
| $A1 | Spalte fixiert | A2, A3, A4, ... |
| A$1 | Zeile fixiert | B1, C1, D1, ... |

> [!tip] **F4-Taste**
> Drücken Sie **F4** nach dem Eingeben eines Zellbezugs, um zwischen den verschiedenen Bezugsarten zu wechseln.

### Bedingte Formatierung

Mit bedingter Formatierung können Sie Zellen automatisch farblich hervorheben:
- Alle Werte > 100 grün markieren
- Negative Zahlen rot darstellen
- Duplikate hervorheben
- Farbskala für Wertebereiche

> [!example] Praktische Anwendung
> In einer Notenliste alle Noten ≥ 4 rot markieren:
> 1. Zellen markieren
> 2. Start → Bedingte Formatierung → Regeln hervorheben
> 3. „Größer als" → 3 → Format: Rot

---

## Zusammenhänge

Tabellenkalkulation verbindet mathematische Konzepte mit digitaler Praxis:

- → [[../13-Statistik-und-Datenanalyse/08-Arithmetisches-Mittel|Arithmetisches Mittel]] – mathematische Grundlage
- → [[../13-Statistik-und-Datenanalyse/05-Balkendiagramme|Balkendiagramme]] – Diagrammtypen verstehen
- → [[05-Funktionen-graphisch|Funktionen graphisch]] – manuelle vs. digitale Darstellung
- → [[07-Python-Mathematik|Python für Mathematik]] – alternative digitale Werkzeuge

---

**Navigation:** [[05-Funktionen-graphisch|← Funktionen]] | [[07-Python-Mathematik|Python →]]
