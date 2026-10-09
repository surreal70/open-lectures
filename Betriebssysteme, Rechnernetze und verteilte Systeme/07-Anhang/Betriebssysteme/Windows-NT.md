---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows NT

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 32-bit/64-bit Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 27. Juli 1993 (NT 3.1) |
| **Designer** | David Cutler (ex DEC VMS) |
| **Lizenz** | Proprietär |
| **Einfluss** | Alle modernen Windows-Versionen |

## Zusammenfassung

Windows NT war Microsofts komplett neu geschriebenes Enterprise-Betriebssystem. Anders als die DOS-basierte Consumer-Linie bot NT echten Speicherschutz, präventives Multitasking und eine portable Architektur. NT ist die Basis aller modernen Windows-Versionen.

### Design-Prinzipien

| Prinzip | Beschreibung |
|---------|--------------|
| **Portabilität** | HAL abstrahiert Hardware |
| **Sicherheit** | C2-Zertifizierung (DoD) |
| **POSIX** | Unix-Kompatibilitätsschicht |
| **Multiprocessing** | Symmetrisches SMP |
| **Internationalisierung** | Unicode von Anfang an |

### NT-Architektur

```
Windows NT Kernel-Architektur
┌─────────────────────────────────────────┐
│        User Mode Subsystems             │
│   (Win32, POSIX, OS/2, Security)        │
├─────────────────────────────────────────┤
│             NT Executive                │
│  ┌───────┬───────┬───────┬───────────┐  │
│  │ I/O   │ Obj.  │ Mem.  │ Process   │  │
│  │ Mgr   │ Mgr   │ Mgr   │ Mgr       │  │
│  └───────┴───────┴───────┴───────────┘  │
├─────────────────────────────────────────┤
│          NT Kernel (Microkernel)        │
├─────────────────────────────────────────┤
│    HAL (Hardware Abstraction Layer)     │
├─────────────────────────────────────────┤
│               Hardware                  │
└─────────────────────────────────────────┘
```

### Versionsgeschichte

| Version | Jahr | Codename | Kernel |
|---------|------|----------|--------|
| NT 3.1 | 1993 | - | 3.1 |
| NT 3.5 | 1994 | Daytona | 3.5 |
| NT 4.0 | 1996 | Cairo (Teil) | 4.0 |
| Windows 2000 | 2000 | - | 5.0 |
| Windows XP | 2001 | Whistler | 5.1 |
| Windows Vista | 2006 | Longhorn | 6.0 |
| Windows 7 | 2009 | Vienna | 6.1 |
| Windows 10 | 2015 | Threshold | 10.0 |
| Windows 11 | 2021 | Sun Valley | 10.0 |

### David Cutler

Der Chefarchitekt von Windows NT kam von DEC, wo er VMS entwickelt hatte. Viele NT-Konzepte stammen aus VMS:
- HAL-Konzept
- Object Manager
- Layered I/O
- Symmetrisches Multiprocessing

### NTFS

NT führte das NT File System ein:
- Journaling für Crash-Recovery
- ACLs für Sicherheit
- Kompression und Verschlüsselung
- Große Volumes (bis 256 TB)

## Siehe auch

- [[Windows-2000]]
- [[Windows-XP]]
- [[Windows-95]]

## Quellen

- [Windows Internals (Russinovich, Solomon)](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals)
- [The Old New Thing (Raymond Chen)](https://devblogs.microsoft.com/oldnewthing/)
- [Wikipedia: Windows NT](https://en.wikipedia.org/wiki/Windows_NT)
