---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows 11

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 64-bit NT-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 5. Oktober 2021 |
| **Lizenz** | Proprietär |
| **Codename** | Sun Valley |
| **Kernel** | NT 10.0 (Build 22000+) |

## Zusammenfassung

Windows 11 bringt eine überarbeitete Benutzeroberfläche mit zentrierter Taskleiste, abgerundeten Ecken und neuen Produktivitätsfeatures. Die erhöhten Hardware-Anforderungen (TPM 2.0, Secure Boot) sorgten für Kontroversen.

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Zentrierte Taskleiste** | macOS-ähnliches Layout |
| **Snap Layouts** | Fensteranordnung |
| **Widgets** | Personalisierte Feeds |
| **Teams Integration** | Chat in Taskleiste |
| **Android Apps** | Amazon Appstore (WSA) |
| **DirectStorage** | Schnelles Laden für Spiele |

### Hardware-Anforderungen

| Komponente | Minimum |
|------------|---------|
| CPU | 1 GHz, 2 Kerne, 64-bit |
| RAM | 4 GB |
| Speicher | 64 GB |
| TPM | Version 2.0 |
| Secure Boot | UEFI |
| Grafik | DirectX 12, WDDM 2.0 |

### Neue UI-Elemente

```
Windows 11 Taskleiste
┌─────────────────────────────────────────┐
│                                         │
│      [🔍][□][📁][Edge][▶]               │
│                                         │
│  Zentrierte Icons mit Animation         │
│                                         │
└─────────┬───────────────────────┬───────┘
          │                       │
    Start/Suche              System Tray
    (abgerundet)             (neu gruppiert)
```

### Entfernte Features

- Live Tiles
- Internet Explorer
- Timeline
- Cortana (aus Standard-Erfahrung)
- Taskleiste: Drag & Drop, Kontextmenü-Anpassung (teilweise wiederhergestellt)

### Snap Layouts

```
Windows 11 Snap Layouts
┌─────────┬─────────┐  ┌─────────┬───┬───┐
│         │         │  │         │   │   │
│   50%   │   50%   │  │   50%   │25%│25%│
│         │         │  │         │   │   │
└─────────┴─────────┘  └─────────┴───┴───┘

┌─────────────────────┐  ┌───┬───┬───┬───┐
│         75%         │  │   │   │   │   │
├───────┬─────────────┤  │25%│25%│25%│25%│
│  25%  │     25%     │  │   │   │   │   │
└───────┴─────────────┘  └───┴───┴───┴───┘
```

### Copilot-Integration

2023 wurde Copilot (KI-Assistent) in Windows 11 integriert:
- Seitenleiste mit ChatGPT-ähnlicher Funktion
- Integration in Einstellungen und Apps
- Microsoft 365 Copilot-Anbindung

## Siehe auch

- [[Windows-10]]
- [[macOS]]
- [[Linux]]

## Quellen

- [Microsoft Windows 11 Documentation](https://learn.microsoft.com/en-us/windows/whats-new/windows-11-overview)
- [Windows 11 Specs](https://www.microsoft.com/en-us/windows/windows-11-specifications)
- [Wikipedia: Windows 11](https://en.wikipedia.org/wiki/Windows_11)
