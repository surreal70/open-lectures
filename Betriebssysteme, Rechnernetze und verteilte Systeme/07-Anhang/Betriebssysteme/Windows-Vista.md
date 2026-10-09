---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows Vista

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 32/64-bit NT-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 30. Januar 2007 |
| **Support-Ende** | 11. April 2017 |
| **Lizenz** | Proprietär |
| **Codename** | Longhorn |
| **Kernel** | NT 6.0 |

## Zusammenfassung

Windows Vista war ein umfangreicher Umbau des Windows-Kernels mit Fokus auf Sicherheit und visuelle Effekte. Trotz technischer Innovationen litt es unter hohen Hardware-Anforderungen und Kompatibilitätsproblemen.

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Aero Glass** | Transparente 3D-Oberfläche |
| **UAC** | User Account Control |
| **BitLocker** | Festplattenverschlüsselung |
| **SuperFetch** | Intelligentes Prefetching |
| **ReadyBoost** | Flash-Speicher als Cache |
| **IPv6** | Native Unterstützung |

### Architektur-Verbesserungen

```
Vista Sicherheitsarchitektur
┌─────────────────────────────────────────┐
│         User Mode                       │
│  ┌─────────────────────────────────┐   │
│  │      UAC (User Account Control) │   │
│  │      Alle Nutzer eingeschränkt  │   │
│  └─────────────────────────────────┘   │
├─────────────────────────────────────────┤
│         Kernel Mode                     │
│  ┌─────────────────────────────────┐   │
│  │  ASLR (Address Space Layout     │   │
│  │        Randomization)           │   │
│  ├─────────────────────────────────┤   │
│  │  Kernel Patch Protection        │   │
│  │  (PatchGuard, 64-bit)          │   │
│  ├─────────────────────────────────┤   │
│  │  Driver Signing (mandatory)     │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Kritik

| Problem | Beschreibung |
|---------|--------------|
| **Performance** | Hohe RAM-Anforderungen (1-2 GB) |
| **Kompatibilität** | Viele XP-Treiber/-Software inkompatibel |
| **UAC** | Ständige Sicherheitsabfragen |
| **DRM** | Einschränkungen bei HD-Inhalten |

### Editionen

- Starter (für Schwellenländer)
- Home Basic
- Home Premium
- Business
- Enterprise
- Ultimate

### Vermächtnis

Viele Vista-Innovationen wurden erst mit Windows 7 akzeptiert:
- Verfeinertes UAC
- Optimierte Ressourcennutzung
- Bessere Treiberunterstützung

## Siehe auch

- [[Windows-XP]]
- [[Windows-7]]
- [[Windows-NT]]

## Quellen

- [Microsoft Vista Documentation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-vista)
- [Windows Internals 5th Ed. (Vista/Server 2008)](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals)
- [Wikipedia: Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista)
