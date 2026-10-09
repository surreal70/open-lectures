---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows 3.x

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Grafische Oberfläche für MS-DOS |
| **Entwickler** | Microsoft |
| **Windows 3.0** | 22. Mai 1990 |
| **Windows 3.1** | 6. April 1992 |
| **Windows 3.11** | November 1993 |
| **Lizenz** | Proprietär |

## Zusammenfassung

Windows 3.x war der Durchbruch für Microsoft im GUI-Markt. Mit verbesserter Speichernutzung, Multimedia-Fähigkeiten und dem Program Manager erreichte Windows erstmals Massenmarkt-Akzeptanz.

### Neuerungen gegenüber Windows 2.x

| Feature | Beschreibung |
|---------|--------------|
| **Protected Mode** | 80286/386 Speichererweiterung |
| **TrueType** | Skalierbare Schriften |
| **OLE** | Object Linking and Embedding |
| **Multimedia** | CD-Audio, MIDI, Video (MPC) |
| **Program Manager** | Neue Shell mit Gruppen |

### Speichermodi

```
Windows 3.x Speichermodi
┌─────────────────────────────────────────┐
│  Real Mode (nur 3.0)                    │
│  └─ 8086/88: 640 KB + EMS              │
├─────────────────────────────────────────┤
│  Standard Mode (286+)                   │
│  └─ 1-16 MB, kein Multitasking         │
├─────────────────────────────────────────┤
│  386 Enhanced Mode                      │
│  └─ Virtueller Speicher                │
│  └─ DOS-Boxen mit Multitasking         │
│  └─ Bis 4 GB adressierbar              │
└─────────────────────────────────────────┘
```

### Windows for Workgroups

Windows 3.11 for Workgroups (WfW) fügte Netzwerk-Features hinzu:
- Peer-to-Peer Networking
- TCP/IP-Unterstützung
- Mail und Schedule+
- 32-bit Datei-/Festplatten-Zugriff

### Benutzeroberfläche

```
Windows 3.1 Program Manager
┌─────────────────────────────────────────┐
│ Program Manager                    [─]  │
├─────────────────────────────────────────┤
│ ┌─Main────────────┐ ┌─Accessories──────┐│
│ │ [File] [Word]   │ │ [Calc] [Write]  ││
│ │ [Excel][Control]│ │ [Paint][Notepad]││
│ └─────────────────┘ └─────────────────┘│
│ ┌─Games───────────┐                    │
│ │ [Sol] [Mine]    │                    │
│ └─────────────────┘                    │
└─────────────────────────────────────────┘
```

### Verkaufszahlen

- 10 Millionen Lizenzen in 2 Jahren
- Erste Windows-Version mit Massenmarkt-Erfolg
- Legte Grundstein für Windows-Dominanz

## Siehe auch

- [[MS-DOS]]
- [[Windows-95]]
- [[Windows-NT]]

## Quellen

- [Microsoft Windows 3.1 Resource Kit](https://archive.org/details/microsoft-windows-3.1-resource-kit)
- [WinWorld: Windows 3.x](https://winworldpc.com/product/windows-3)
- [Wikipedia: Windows 3.1x](https://en.wikipedia.org/wiki/Windows_3.1x)
