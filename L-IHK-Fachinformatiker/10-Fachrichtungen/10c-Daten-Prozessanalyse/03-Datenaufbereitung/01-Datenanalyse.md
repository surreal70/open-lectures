---
title: "Datenaufbereitung – Syntaktische und semantische Analyse"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - daten
  - datenanalyse
  - konverter
source: proTirone (CC-BY-4.0)
---

# Datenaufbereitung – Syntaktische und semantische Analyse

> [!info] Lernziele
> - Phasen der Datenanalyse anwenden
> - Syntaktische Datenprobleme erkennen und lösen
> - Konverter nach MVP-Strategie entwickeln
> - Zeichencodierungen verstehen (ASCII, UTF-8)

## Zweck von Daten

Daten sollen:
- **Weltbeschreibungen** liefern
- Zur **Weltverbesserung** anregen

**Aber:** Elektronische RAW-Daten sind nur Bits = Bytes = Zahlen. Sie müssen **syntaktisch** und **semantisch** interpretiert werden.

## Datenarten

### Nach Herkunft

| Art | Beschreibung |
|-----|--------------|
| **Interne Daten** | Entstehen bei firmeneigenen Prozessen, mit firmeneigenen Systemen |
| **Externe Daten** | Entstehen durch Fremdfirmenprozesse (offene Statistiken, Web-Crawler, gekaufte Daten) |

### Nach Strukturierungsgrad

| Grad | Beschreibung | Formate |
|------|--------------|---------|
| **Strukturiert** | Festes, bedeutungsgemäßes Format | JSON, XML, CSV, YAML, INI |
| **Semi-strukturiert** | Format repräsentiert Bedeutung nicht vollständig | Bilder, Logs |
| **Unstrukturiert** | Verschiedene Formate und Bedeutungen | Dokumentsammlungen |

## Phasen der Datenanalyse

> [!warning] Grundregel
> Nicht auf Originaldaten arbeiten! Immer erst **Datensicherung** anlegen.

### Syntaktische Datenaufbereitung

| Phase | Kürzel | Beschreibung |
|-------|--------|--------------|
| **Byte-Analyse** | SYDA.A | Was steht tatsächlich auf der "Platte"? (HEX-Editor) |
| **Byte-Interpretation** | SYDA.I | Welche Bytes gehören zusammen? Welche Datentypen? |
| **Formatanalyse** | SYDA.E | Datensätze und deren innere Struktur ermitteln |
| **Reparatur** | SYDA.R | Abweichende Datensätze syntaktisch angleichen oder löschen |
| **Konverter** | SYDA.K | Konverter mit wiederverwendbarer Zwischenrepräsentation |

### Semantische Auswertung

| Phase | Kürzel | Beschreibung |
|-------|--------|--------------|
| **Laden** | SEDA.L | Daten programmintern zum Auswerten laden |
| **Korrektur** | SEDA.K | Datensätze plausibilisieren und korrigieren |
| **Evaluation** | SEDA.E | Durchschnitt, Mittelwert, Varianz berechnen |
| **Aggregation** | SEDA.A | Trends und Aussagen zusammenfassen |
| **Visualisierung** | SEDA.V | Präsentables Format entwickeln |
| **Präsentation** | SEDA.P | Tendenzen präsentabel darstellen |

```
┌─────────────────────────────────────────────────────────────┐
│                  SYNTAKTISCHE AUFBEREITUNG                  │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ SYDA.A   │ SYDA.I   │ SYDA.E   │ SYDA.R   │    SYDA.K       │
│ Byte-    │ Byte-    │ Format-  │ Syntax-  │   Konverter     │
│ Analyse  │ Interpret│ Analyse  │ Reparatur│   bauen         │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  SEMANTISCHE AUSWERTUNG                     │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ SEDA.L   │ SEDA.K   │ SEDA.E   │ SEDA.A   │ SEDA.V/P        │
│ Laden    │ Semantik │ Evaluate │ Aggre-   │ Visualisieren   │
│          │ Korrektur│          │ gieren   │ Präsentieren    │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

## Zeichencodierungen

### Das Problem

> [!important] Merksatz
> Ein Byte repräsentiert **entweder** eine Zahl **oder** ein Zeichen!
> Was davon – das ist Interpretationssache.

### ASCII (7-Bit)

**American Standard Code for Information Interchange**

| Bereich | Hex | Inhalt |
|---------|-----|--------|
| Steuerzeichen | 0x00-0x1F | Nicht druckbar (Drucker-Befehle) |
| Satzzeichen | 0x20-0x2F | Space, !, ", #, $, ... |
| Ziffern | 0x30-0x3F | 0-9, :, ;, <, =, >, ? |
| Großbuchstaben | 0x40-0x5F | @, A-Z, [, \, ], ^, _ |
| Kleinbuchstaben | 0x60-0x7F | `, a-z, {, |, }, ~ |

### ANSI/Latin-1 (8-Bit)

Erweiterung für europäische Zeichen:
- 0x00-0x7F: Wie ASCII
- 0x80-0xFF: Umlaute, Sonderzeichen (iso-latin-1 bis iso-latin-15)

### Unicode

- Ordnet **allen weltweit genutzten Zeichen** einen eindeutigen Wert zu
- Präfix: `U+` gefolgt von 4-6 Hex-Zahlen
- Beispiel: `U+00C4` = 'Ä'
- Aktuell: 154.998 Zeichen in 17 Ebenen

### UTF-8

**Unicode Transformation Format – 8 Bit**

Jede Unicode-Zahl wird in 1-4 Bytes transformiert:

| Bytes | Höchstes Byte | Folgebytes | Codepoint-Bereich |
|-------|---------------|------------|-------------------|
| 1 | `0xxxxxxx` | - | U+0000 – U+007F (ASCII) |
| 2 | `110xxxxx` | `10xxxxxx` | U+0080 – U+07FF |
| 3 | `1110xxxx` | 2× `10xxxxxx` | U+0800 – U+FFFF |
| 4 | `11110xxx` | 3× `10xxxxxx` | U+10000 – U+10FFFF |

**Beispiel: Ä**
| Codierung | Wert |
|-----------|------|
| Unicode | U+00C4 |
| UTF-8 | 0xC3 0x84 |
| ISO-Latin-1 | 196 (0xC4) |
| HTML Entity | `&Auml;` |

## Konverterentwicklung

### Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                      KONVERTER                              │
├─────────────────┬─────────────────┬─────────────────────────┤
│  Input-Adapter  │  Zwischen-      │  Output-Adapter         │
│                 │  repräsentation │                         │
│  ┌───────────┐  │  (ZRP)          │  ┌───────────┐          │
│  │   CSV     │──│──┐              │──│   JSON    │          │
│  └───────────┘  │  │  ┌────────┐  │  └───────────┘          │
│  ┌───────────┐  │  ├─▶│ Python │──│  ┌───────────┐          │
│  │   XML     │──│──┤  │  Dict  │  │──│   INI     │          │
│  └───────────┘  │  │  └────────┘  │  └───────────┘          │
│  ┌───────────┐  │  │              │  ┌───────────┐          │
│  │   ...     │──│──┘              │──│   ...     │          │
│  └───────────┘  │                 │  └───────────┘          │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### MVP-Strategie

> [!quote] Definition
> Ein **MVP** (Minimal Viable Product) ist die erste minimal funktionsfähige Iteration eines Produkts.

**Entwicklungsschritte:**

1. **MVP**: Leerer Konverter mit hart-codierter ZRP und Methodenhülsen
2. **VP-0.1**: + Output-Adapter (ZRP → **Input**-Format)
3. **VP-0.2**: + Input-Adapter (Testdaten → ZRP)
4. **VP-0.3**: + Output-Adapter (ZRP → **Ziel**-Format)
5. **VP-1.0**: + User-Handling, Kommandozeilenparameter

### Beispiel: Python-Konverter

```python
# MVP: Grundstruktur mit hart-codierten Testdaten
test_data = [
    {"date": "2024-01-15", "value": 120},
    {"date": "2024-01-16", "value": 118}
]

def read_csv(filepath):
    """Input-Adapter: CSV → ZRP"""
    records = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            records.append({
                "date": parts[0],
                "value": int(parts[1])
            })
    return records

def write_json(records, filepath):
    """Output-Adapter: ZRP → JSON"""
    import json
    with open(filepath, 'w') as f:
        json.dump(records, f, indent=2)

def write_ini(records, filepath):
    """Output-Adapter: ZRP → INI"""
    with open(filepath, 'w') as f:
        for i, rec in enumerate(records):
            f.write(f"[record_{i}]\n")
            for key, value in rec.items():
                f.write(f"{key} = {value}\n")
            f.write("\n")

# Main
if __name__ == "__main__":
    data = read_csv("input.csv")
    write_json(data, "output.json")
```

---

> [!tip] Regeln für die Datenanalyse
> 1. Gehen Sie davon aus, dass Ihre Daten **verrauscht** sind
> 2. Verlassen Sie sich nicht auf zugesagte Formatstabilität
> 3. Trennen Sie syntaktische Bereinigung vom Konverter
> 4. Nutzen Sie eine wiederverwendbare Zwischenrepräsentation

---

> [!tip] Übungen
> 1. Analysieren Sie eine unbekannte Binärdatei mit einem HEX-Editor
> 2. Entwickeln Sie einen CSV→JSON-Konverter nach MVP-Strategie
> 3. Identifizieren Sie die Codierung einer Textdatei anhand der Byte-Sequenzen

## Weiterführende Links

- [UTF-8 bei Wikipedia](https://de.wikipedia.org/wiki/UTF-8)
- [ASCII-Code Tabelle](https://www.ascii-code.com/)
- [SELFHTML: Zeichencodierung](https://wiki.selfhtml.org/wiki/Zeichencodierung/Bytes_und_Buchstaben)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
