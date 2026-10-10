---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# CP/M (Control Program for Microcomputers)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 8-bit Betriebssystem |
| **Entwickler** | Gary Kildall / Digital Research |
| **Erstveröffentlichung** | 1974 |
| **Lizenz** | Proprietär |
| **Architektur** | Intel 8080, Zilog Z80 |

## Zusammenfassung

CP/M war das dominierende Betriebssystem für Mikrocomputer vor der IBM PC-Ära. Es etablierte Standards für Dateisysteme und Programm-APIs, die MS-DOS später übernahm.

### Historische Bedeutung

- Erstes standardisiertes Mikrocomputer-OS
- Ermöglichte Software-Portabilität zwischen Herstellern
- Etablierte das FCB (File Control Block)-Konzept
- Vorbild für MS-DOS

### Architektur

```
CP/M Speichermodell
┌────────────────────────────────────────┐
│           BIOS                         │ Oberste Adressen
│     (Hardware-spezifisch)              │
├────────────────────────────────────────┤
│           BDOS                         │
│   (Basic Disk Operating System)        │
├────────────────────────────────────────┤
│           CCP                          │
│   (Console Command Processor)          │
├────────────────────────────────────────┤
│                                        │
│      TPA (Transient Program Area)      │
│          Benutzer-Programme            │
│                                        │
├────────────────────────────────────────┤
│  Base Page (0000-00FF)                 │ Adresse 0
└────────────────────────────────────────┘
```

### Befehle

```
DIR      - Verzeichnis
ERA      - Datei löschen
REN      - Umbenennen
TYPE     - Datei anzeigen
STAT     - Statistik
PIP      - Kopieren
```

### CP/M-86 und die IBM-Geschichte

IBM wollte CP/M-86 für den PC lizenzieren, aber:
- Anekdote: Kildall verpasste das Meeting
- Digital Research lehnte IBMs Vertragsbedingungen ab
- IBM kaufte stattdessen QDOS → MS-DOS

### Varianten

| Variante | Beschreibung |
|----------|--------------|
| CP/M-80 | Original für 8080/Z80 |
| CP/M-86 | 16-bit Version für 8086 |
| MP/M | Multi-User-Version |
| CP/NET | Netzwerk-Version |
| DR-DOS | Späterer DOS-Konkurrent |

## Siehe auch

- [[MS-DOS]]
- [[Betriebssysteme-Index]]

## Quellen

- [CP/M Archive](http://www.cpm.z80.de/)
- [Digital Research Archive](https://www.computerhistory.org/collections/catalog/102707766)
- [Wikipedia: CP/M](https://en.wikipedia.org/wiki/CP/M)
