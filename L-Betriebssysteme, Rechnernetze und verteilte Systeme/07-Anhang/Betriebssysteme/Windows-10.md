---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows 10

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 32/64-bit NT-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 29. Juli 2015 |
| **Support-Ende** | 14. Oktober 2025 |
| **Lizenz** | Proprietär |
| **Codename** | Threshold, Redstone, u.a. |
| **Kernel** | NT 10.0 |

## Zusammenfassung

Windows 10 markierte Microsofts Wechsel zu "Windows as a Service" mit kontinuierlichen Updates. Es vereinte Desktop, Tablet und Xbox unter einer Plattform und führte viele moderne Features ein.

### Windows as a Service

Microsoft liefert halbjährliche Feature-Updates:
- Kein Windows 11 geplant (später revidiert)
- Kontinuierliche Weiterentwicklung
- LTSC-Versionen für Stabilität

### Wichtige Features

| Feature | Beschreibung |
|---------|--------------|
| **Startmenü** | Rückkehr + Live Tiles |
| **Cortana** | Digitaler Assistent |
| **Edge** | Neuer Browser (später Chromium) |
| **Virtual Desktops** | Native Arbeitsflächen |
| **Windows Hello** | Biometrische Anmeldung |
| **WSL** | Windows Subsystem for Linux |
| **Sandbox** | Isolierte Testumgebung |

### WSL (Windows Subsystem for Linux)

```
WSL2 Architektur
┌─────────────────────────────────────────┐
│           Windows 10/11                 │
├─────────────────────────────────────────┤
│       Hyper-V Hypervisor                │
├──────────────────┬──────────────────────┤
│   Windows NT     │   WSL2 VM           │
│   Kernel         │   (echter Linux-    │
│                  │    Kernel)          │
├──────────────────┴──────────────────────┤
│              Hardware                    │
└─────────────────────────────────────────┘
```

### Editionen

| Edition | Zielgruppe |
|---------|------------|
| Home | Consumer |
| Pro | Prosumer, KMU |
| Enterprise | Großunternehmen |
| Education | Bildungseinrichtungen |
| IoT | Internet of Things |
| LTSC | Long-Term Servicing |

### Feature-Updates (Auswahl)

| Version | Codename | Neuerungen |
|---------|----------|------------|
| 1507 | Threshold 1 | Erstrelease |
| 1607 | Redstone 1 | Anniversary, WSL1 |
| 1903 | 19H1 | Windows Sandbox |
| 2004 | 20H1 | WSL2 |
| 21H2 | 21H2 | Letztes Feature-Update |

## Siehe auch

- [[Windows-7]]
- [[Windows-11]]
- [[Linux]]

## Quellen

- [Microsoft Windows 10 Documentation](https://learn.microsoft.com/en-us/windows/windows-10/)
- [Windows 10 IT Pro Blog](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/bg-p/Windows10Blog)
- [Wikipedia: Windows 10](https://en.wikipedia.org/wiki/Windows_10)
