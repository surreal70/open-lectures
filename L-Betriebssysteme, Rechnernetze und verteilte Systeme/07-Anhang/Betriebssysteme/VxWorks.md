---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# VxWorks

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Echtzeit-Betriebssystem |
| **Entwickler** | Wind River Systems |
| **Erstveröffentlichung** | 1987 |
| **Lizenz** | Proprietär |
| **Architektur** | ARM, x86, MIPS, PowerPC, RISC-V |

## Zusammenfassung

VxWorks ist ein kommerzielles Echtzeit-Betriebssystem für sicherheitskritische Embedded-Systeme. Es wird in der Luft- und Raumfahrt, Automobil- und Medizintechnik eingesetzt und läuft auf Mars-Rovern.

### Prominente Einsätze

| Projekt | Bereich |
|---------|---------|
| Mars Pathfinder | NASA |
| Mars Rovers | NASA |
| Boeing 787 | Avionik |
| BMW iDrive | Automotive |
| Cisco Router | Netzwerk |

### Kernel-Architektur

```
VxWorks Architektur
┌─────────────────────────────────────────┐
│    User Applications                    │
├─────────────────────────────────────────┤
│    POSIX / VxWorks API                  │
├─────────────────────────────────────────┤
│    VxWorks Kernel                       │
│  ┌────────────────────────────────────┐ │
│  │  Scheduler │ IPC │ Memory │ Timer │ │
│  └────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│    Board Support Package (BSP)          │
├─────────────────────────────────────────┤
│    Hardware                             │
└─────────────────────────────────────────┘
```

### Hauptmerkmale

| Feature | Beschreibung |
|---------|--------------|
| **Determinismus** | Garantierte Interrupt-Latenz |
| **POSIX-konform** | PSE52/PSE54 Profile |
| **Skalierbar** | Von MCU bis Multi-Core |
| **Sicherheitszertifizierungen** | DO-178B/C, IEC 61508, ISO 26262 |
| **Virtualisierung** | VxWorks Hypervisor |

### VxWorks 7

Die aktuelle Generation bietet:
- Modulare Architektur (VSB/VIP)
- Container-Unterstützung
- Cloud-Konnektivität
- Machine Learning Runtime
- Erweiterte Sicherheitsfeatures

### Echtzeit-Eigenschaften

```
VxWorks Echtzeit-Garantien
┌─────────────────────────────────────────┐
│  Interrupt-Latenz:    < 1 µs            │
│  Context-Switch:      < 2 µs            │
│  Determinismus:       Garantiert        │
│  Priority Levels:     256               │
│  Preemption:          Ja                │
└─────────────────────────────────────────┘
```

## Siehe auch

- [[FreeRTOS]]
- [[QNX]]
- [[RTEMS]]

## Quellen

- [Wind River VxWorks](https://www.windriver.com/products/vxworks)
- [VxWorks Documentation](https://docs.windriver.com/)
- [Wikipedia: VxWorks](https://en.wikipedia.org/wiki/VxWorks)
