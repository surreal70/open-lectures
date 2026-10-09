---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# z/OS

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Mainframe-Betriebssystem |
| **Entwickler** | IBM |
| **Erstveröffentlichung** | 2001 (als z/OS) |
| **Vorgänger** | OS/390, MVS |
| **Lizenz** | Proprietär |
| **Architektur** | IBM Z (z/Architecture) |

## Zusammenfassung

z/OS ist IBMs Flaggschiff-Betriebssystem für Mainframe-Computer. Es verarbeitet den Großteil der weltweiten Finanztransaktionen und bietet extreme Zuverlässigkeit, Sicherheit und Skalierbarkeit.

### Evolution

```
IBM Mainframe-OS Evolution
┌────────────────────────────────────────┐
│  OS/360 (1966)                         │
│     └─► MVS (1974)                     │
│          └─► MVS/ESA (1988)            │
│               └─► OS/390 (1995)        │
│                    └─► z/OS (2001)     │
└────────────────────────────────────────┘
```

### Hauptmerkmale

| Feature | Beschreibung |
|---------|--------------|
| **WLM** | Workload Manager |
| **Parallel Sysplex** | Cluster mit bis zu 32 Systemen |
| **RACF** | Sicherheitssystem |
| **CICS** | Transaktionsserver |
| **DB2** | Relationale Datenbank |
| **USS** | Unix System Services (POSIX) |

### Zuverlässigkeit

- **99.999%** Uptime ("Five Nines")
- Rolling Upgrades ohne Downtime
- Hardware-Fehlerkorrektur
- Automatische Failover

### Einsatzgebiete

| Branche | Anwendung |
|---------|-----------|
| Banken | Kernbanken-Systeme |
| Versicherungen | Policy-Verwaltung |
| Fluggesellschaften | Reservierungssysteme |
| Einzelhandel | Kreditkartenabwicklung |

### Dateisysteme

- **VSAM**: Virtual Storage Access Method
- **HFS**: Hierarchical File System (Unix)
- **zFS**: High-Performance Unix FS
- **Datasets**: Klassische MVS-Dateien

### Programmiersprachen

- COBOL (Milliarden Codezeilen weltweit)
- PL/I
- Assembler
- Java (z.B. Liberty auf z/OS)
- Python, Go (moderne Erweiterungen)

## Siehe auch

- [[OS-360]]
- [[BS2000]]
- [[Linux]]

## Quellen

- [IBM z/OS](https://www.ibm.com/products/zos)
- [IBM z/OS Documentation](https://www.ibm.com/docs/en/zos)
- [Wikipedia: z/OS](https://en.wikipedia.org/wiki/Z/OS)
