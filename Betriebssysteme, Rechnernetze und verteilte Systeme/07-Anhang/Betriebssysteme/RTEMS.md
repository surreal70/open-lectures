---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# RTEMS (Real-Time Executive for Multiprocessor Systems)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Echtzeit-Betriebssystem |
| **Entwickler** | OAR Corporation, Community |
| **Erstveröffentlichung** | 1988 |
| **Lizenz** | Modifizierte GPL (ohne Linking-Einschränkung) |
| **Architektur** | ARM, SPARC, PowerPC, RISC-V, x86 |

## Zusammenfassung

RTEMS ist ein Open-Source-Echtzeitbetriebssystem, das ursprünglich für militärische und raumfahrttechnische Anwendungen entwickelt wurde. Es wird von der ESA, NASA und in kritischen Embedded-Systemen weltweit eingesetzt.

### Prominente Einsätze

| Projekt | Organisation |
|---------|--------------|
| Herschel-Weltraumteleskop | ESA |
| Mars Reconnaissance Orbiter | NASA |
| Gaia-Mission | ESA |
| Large Hadron Collider | CERN |
| GPS-Satelliten | US Air Force |

### Architektur

```
RTEMS Schichtenmodell
┌─────────────────────────────────────────┐
│         Anwendungen                     │
├─────────────────────────────────────────┤
│    POSIX / Classic / RTEMS APIs         │
├─────────────────────────────────────────┤
│           SuperCore                     │
│  ┌────────────────────────────────────┐ │
│  │ Threads │ Heaps │ Timer │ Mutex  │ │
│  └────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│      Board Support Package (BSP)        │
├─────────────────────────────────────────┤
│            Hardware                     │
└─────────────────────────────────────────┘
```

### APIs

RTEMS bietet mehrere API-Sets:

| API | Beschreibung |
|-----|--------------|
| **Classic** | Originale RTEMS-API |
| **POSIX** | IEEE Std 1003.1 |
| **ITRON** | µITRON-kompatibel |

### Eigenschaften

| Feature | Beschreibung |
|---------|--------------|
| **Präemptiv** | 256 Prioritätsebenen |
| **SMP** | Multi-Core-Unterstützung |
| **POSIX** | PSE51/52/53/54 Profile |
| **Networking** | lwIP, FreeBSD-Stack |
| **Filesystems** | IMFS, JFFS2, FAT, NFS |

### Entwicklung

- Waf/CMake Build-System
- RSB (RTEMS Source Builder)
- GDB-Debugging
- QEMU-Emulation
- CI/CD-Integration

### SPARC/LEON-Prozessoren

RTEMS ist die Referenzplattform für:
- ESA LEON SPARC-Prozessoren
- Raumfahrt-qualifizierte Hardware
- Strahlengehärtete Systeme

## Siehe auch

- [[FreeRTOS]]
- [[VxWorks]]
- [[Zephyr]]

## Quellen

- [RTEMS.org](https://www.rtems.org/)
- [RTEMS Documentation](https://docs.rtems.org/)
- [Wikipedia: RTEMS](https://en.wikipedia.org/wiki/RTEMS)
