---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# macOS (früher Mac OS X, OS X)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-basiertes Betriebssystem |
| **Entwickler** | Apple Inc. |
| **Erstveröffentlichung** | 24. März 2001 (Mac OS X 10.0) |
| **Aktuelle Version** | macOS 15.x (Sequoia, 2024) |
| **Lizenz** | Proprietär (Teile Open Source) |
| **Basis** | Darwin (XNU Kernel, BSD Userland) |

## Zusammenfassung

macOS ist Apples Desktop-Betriebssystem mit Unix-Kern (Darwin/XNU). Es kombiniert BSD-Userland mit einem Mach-Mikrokernel und der proprietären Aqua-Oberfläche. Seit 2020 läuft es auch auf Apple Silicon (ARM).

### Architektur

```
macOS Schichtenmodell
┌─────────────────────────────────────┐
│        Cocoa / AppKit / SwiftUI     │
├─────────────────────────────────────┤
│    Core Services (Foundation, CF)   │
├─────────────────────────────────────┤
│   Core OS (POSIX, BSD, IOKit)       │
├─────────────────────────────────────┤
│           Darwin                    │
│  ┌────────────────────────────────┐ │
│  │   XNU Kernel (Mach + BSD)      │ │
│  └────────────────────────────────┘ │
├─────────────────────────────────────┤
│     Hardware (x86-64 / ARM64)       │
└─────────────────────────────────────┘
```

### Geschichte

| Version | Codename | Jahr | Highlights |
|---------|----------|------|------------|
| 10.0 | Cheetah | 2001 | Aqua UI, Unix-Basis |
| 10.4 | Tiger | 2005 | Spotlight, Dashboard |
| 10.5 | Leopard | 2007 | Time Machine |
| 10.6 | Snow Leopard | 2009 | Intel-only, Grand Central |
| 10.7 | Lion | 2011 | iOS-Features |
| 10.9 | Mavericks | 2013 | Kostenlos |
| 10.11 | El Capitan | 2015 | SIP |
| 10.14 | Mojave | 2018 | Dark Mode |
| 11 | Big Sur | 2020 | Apple Silicon, neues Design |
| 14 | Sonoma | 2023 | Widgets, Game Mode |

### Schlüsselfeatures

| Feature | Beschreibung |
|---------|--------------|
| **Time Machine** | Automatische Backups |
| **Spotlight** | Systemweite Suche |
| **Mission Control** | Fenster-/Desktop-Übersicht |
| **AirDrop** | Drahtloser Datenaustausch |
| **Continuity** | iPhone/iPad-Integration |
| **SIP** | System Integrity Protection |

### Darwin und Open Source

Der Kernel Darwin ist Open Source:
- XNU: Hybrid aus Mach-Mikrokernel und BSD
- Userland-Tools aus FreeBSD/NetBSD
- Treiber-Framework: IOKit

Auf Darwin basiert auch das PureDarwin-Projekt.

### Apple Silicon

Seit 2020 wechselt Apple von Intel zu eigenen ARM-Chips:
- M1, M2, M3 (Desktop/Laptop)
- Rosetta 2 für x86-Emulation
- Unified Memory Architecture

## Siehe auch

- [[iOS]]
- [[BSD]]
- [[UNIX]]

## Quellen

- [Apple macOS](https://www.apple.com/macos/)
- [Darwin Open Source](https://opensource.apple.com/)
- [Wikipedia: macOS](https://en.wikipedia.org/wiki/MacOS)
