---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# MS-DOS (Microsoft Disk Operating System)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 16-bit Einzelbenutzer-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | August 1981 |
| **Letzte Version** | 8.0 (in Windows ME, 2000) |
| **Lizenz** | Proprietär |
| **Basis** | 86-DOS (Seattle Computer Products) |

## Zusammenfassung

MS-DOS war das dominierende Betriebssystem der PC-Ära in den 1980ern und frühen 1990ern. Microsoft lizenzierte 86-DOS (QDOS) von Seattle Computer Products und lieferte es als PC-DOS für IBM, parallel als MS-DOS für andere Hersteller.

### Merkmale

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Single-Tasking** | Nur ein Programm gleichzeitig |
| **Kein Speicherschutz** | Alle Programme im Real Mode |
| **640 KB Limit** | "640K ought to be enough" |
| **FAT-Dateisystem** | FAT12, FAT16 |
| **Command-Line** | COMMAND.COM als Shell |

### Versionsgeschichte

| Version | Jahr | Neuerungen |
|---------|------|------------|
| 1.0 | 1981 | IBM PC, 160 KB Disketten |
| 2.0 | 1983 | Festplatten, Verzeichnisse |
| 3.0 | 1984 | 1.2 MB Disketten, Networks |
| 4.0 | 1988 | >32 MB Partitionen |
| 5.0 | 1991 | EDIT, QBASIC, High Memory |
| 6.0 | 1993 | DoubleSpace, Defrag |
| 6.22 | 1994 | Letzte Standalone-Version |

### Speichermodell

```
MS-DOS Speicheraufteilung (Real Mode)
┌────────────────────┐ 1 MB
│  High Memory Area  │ 64 KB (A20-Gate)
├────────────────────┤ 1024 KB
│                    │
│   Upper Memory     │ 384 KB
│   (UMBs, ROMs)     │
│                    │
├────────────────────┤ 640 KB
│                    │
│  Conventional      │
│    Memory          │ 640 KB
│  (Programme)       │
│                    │
├────────────────────┤
│  DOS + Treiber     │
└────────────────────┘ 0 KB
```

### Wichtige Befehle

```
DIR      - Verzeichnis anzeigen
CD       - Verzeichnis wechseln
COPY     - Dateien kopieren
DEL      - Dateien löschen
FORMAT   - Datenträger formatieren
EDIT     - Texteditor
MEM      - Speicher anzeigen
```

### Vermächtnis

MS-DOS-Kompatibilität blieb bis Windows XP/Vista erhalten. Die Eingabeaufforderung (CMD.EXE) führt das Erbe fort, PowerShell löst es modern ab.

## Siehe auch

- [[Windows-95]]
- [[CP-M]]
- [[Xenix]]

## Quellen

- [MS-DOS Source Code (GitHub)](https://github.com/microsoft/MS-DOS)
- [PCjs MS-DOS History](https://www.pcjs.org/software/pcx86/sys/dos/microsoft/)
- [Wikipedia: MS-DOS](https://en.wikipedia.org/wiki/MS-DOS)
