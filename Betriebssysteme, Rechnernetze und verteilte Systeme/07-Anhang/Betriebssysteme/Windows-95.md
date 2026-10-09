---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows 95

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 32-bit Hybrid-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 24. August 1995 |
| **Support-Ende** | 31. Dezember 2001 |
| **Lizenz** | Proprietär |
| **Codename** | Chicago |

## Zusammenfassung

Windows 95 war ein Meilenstein in der PC-Geschichte: Es führte die bis heute bekannte Benutzeroberfläche mit Startmenü, Taskleiste und Desktop ein. Obwohl es noch auf MS-DOS basierte, bot es 32-bit-Unterstützung und präventives Multitasking.

### Revolutionäre Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Startmenü** | Zentrale Programmverwaltung |
| **Taskleiste** | Fenster-Übersicht |
| **Explorer** | Neuer Dateimanager |
| **Plug and Play** | Automatische Hardware-Erkennung |
| **Lange Dateinamen** | Bis 255 Zeichen (statt 8.3) |
| **Internet Explorer** | Ab OSR2 integriert |

### Architektur

```
Windows 95 Hybrid-Architektur
┌─────────────────────────────────────┐
│     32-bit Windows-Anwendungen     │
│         (Win32-API)                 │
├─────────────────────────────────────┤
│     16-bit Windows-Anwendungen     │
│         (Win16-API)                 │
├──────────────────┬──────────────────┤
│   Windows 95     │   MS-DOS 7.0     │
│   Kernel/GDI/USER│   (Real-Mode)    │
├──────────────────┴──────────────────┤
│           Hardware                  │
└─────────────────────────────────────┘
```

### Systemanforderungen

| Komponente | Minimum | Empfohlen |
|------------|---------|-----------|
| CPU | 386 DX | 486 |
| RAM | 4 MB | 8 MB |
| Festplatte | 55 MB | 120 MB |

### Marketing-Phänomen

Der Launch am 24. August 1995 war ein Medienereignis:
- Lizenzierung von "Start Me Up" (Rolling Stones)
- Mitternachtsverkäufe weltweit
- Empire State Building in Windows-Farben
- 1 Million verkaufte Kopien in 4 Tagen

### DOS-Basis

Trotz 32-bit-Oberfläche basierte Windows 95 auf MS-DOS:
- DOS 7.0 bootete zuerst
- `WIN.COM` startete GUI
- Kritische Komponenten teilweise noch 16-bit
- FAT32 erst ab OSR2 (1996)

## Siehe auch

- [[MS-DOS]]
- [[Windows-98]]
- [[Windows-NT]]

## Quellen

- [Windows 95 Resource Kit](https://archive.org/details/windows95resourcekit)
- [Raymond Chen: The Old New Thing](https://devblogs.microsoft.com/oldnewthing/)
- [Wikipedia: Windows 95](https://en.wikipedia.org/wiki/Windows_95)
