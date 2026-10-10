---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# iOS

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Mobiles Unix-Betriebssystem |
| **Entwickler** | Apple Inc. |
| **Erstveröffentlichung** | 29. Juni 2007 (iPhone OS 1.0) |
| **Aktuelle Version** | iOS 18.x (2024) |
| **Lizenz** | Proprietär |
| **Basis** | Darwin (XNU Kernel) |

## Zusammenfassung

iOS ist Apples mobiles Betriebssystem für iPhone und iPod touch (iPad nutzt iPadOS). Es teilt den Darwin-Kern mit macOS, verwendet aber eine Touch-optimierte Oberfläche und strikte App-Sandboxing.

### Architektur

```
iOS Schichtenmodell
┌─────────────────────────────────────┐
│    Cocoa Touch (UIKit/SwiftUI)      │
├─────────────────────────────────────┤
│          Media Layer               │
│   (Core Audio, Core Graphics)       │
├─────────────────────────────────────┤
│       Core Services Layer           │
│  (Foundation, Core Data, CloudKit)  │
├─────────────────────────────────────┤
│         Core OS Layer               │
│    (Darwin/XNU, POSIX, Security)    │
├─────────────────────────────────────┤
│        ARM64 Hardware               │
└─────────────────────────────────────┘
```

### Sicherheitskonzept

| Feature | Beschreibung |
|---------|--------------|
| **Secure Enclave** | Hardware-Sicherheitsmodul |
| **App Sandbox** | Isolierte App-Container |
| **Code Signing** | Nur signierte Apps |
| **ASLR** | Address Space Randomization |
| **Face ID / Touch ID** | Biometrische Authentifizierung |
| **Datenschutz-Labels** | App Store Transparenz |

### Versionsgeschichte (Auswahl)

| Version | Jahr | Highlights |
|---------|------|------------|
| 1.0 | 2007 | Erstes iPhone |
| 2.0 | 2008 | App Store |
| 4.0 | 2010 | Multitasking |
| 7.0 | 2013 | Flat Design |
| 8.0 | 2014 | Extensions, HealthKit |
| 13.0 | 2019 | Dark Mode |
| 14.0 | 2020 | Widgets, App Clips |
| 16.0 | 2022 | Sperrbildschirm |
| 18.0 | 2024 | Apple Intelligence |

### App-Ökosystem

- **App Store**: Einzige offizielle Installationsquelle
- **Swift/Objective-C**: Native Entwicklung
- **TestFlight**: Beta-Tests
- **Enterprise Deployment**: Firmen-Apps ohne Store

### Unterschiede zu macOS

| Aspekt | iOS | macOS |
|--------|-----|-------|
| Multi-Window | Eingeschränkt | Vollständig |
| Dateisystem | Sandboxed | Voller Zugriff |
| Shell-Zugang | Nein | Terminal.app |
| App-Installation | Nur App Store | Überall |

## Siehe auch

- [[macOS]]
- [[Android]]
- [[Darwin]]

## Quellen

- [Apple iOS](https://www.apple.com/ios/)
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Wikipedia: iOS](https://en.wikipedia.org/wiki/IOS)
