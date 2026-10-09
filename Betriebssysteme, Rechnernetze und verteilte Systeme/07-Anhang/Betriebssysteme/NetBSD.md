---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# NetBSD

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | NetBSD Foundation |
| **Erstveröffentlichung** | April 1993 |
| **Aktuelle Version** | 10.x |
| **Lizenz** | BSD-Lizenz |
| **Motto** | "Of course it runs NetBSD" |

## Zusammenfassung

NetBSD ist das portabelste BSD-Derivat und läuft auf über 60 verschiedenen Hardware-Architekturen. Das Projekt priorisiert sauberen, portablen Code und dient als Referenz für Betriebssystem-Architektur.

### Portabilität

NetBSD unterstützt eine außergewöhnliche Bandbreite an Plattformen:

| Kategorie | Beispiele |
|-----------|-----------|
| Modern | x86-64, ARM64, RISC-V |
| Klassisch | VAX, m68k, SPARC |
| Embedded | MIPS, SH3, PowerPC |
| Exotisch | Atari, Amiga, Dreamcast |

### Technische Merkmale

- **pkgsrc**: Plattformübergreifendes Paketsystem (auch für Linux, macOS)
- **rump kernels**: Kernel-Komponenten im Userspace
- **NPF**: Hochperformante Paketfilter-Firewall
- **Kernel ASLR**: Adress-Randomisierung im Kernel
- **Xen Dom0**: Hypervisor-Unterstützung

### Architektur-Abstraktionen

```
NetBSD Portabilitätsschichten
┌────────────────────────────────┐
│      Machine-Independent       │
│         Kernel Code            │
├────────────────────────────────┤
│        bus_space(9)            │
│       bus_dma(9) API           │
├────────────────────────────────┤
│   Machine-Dependent (MD)       │
│      pmap, interrupt           │
├────────────────────────────────┤
│    Hardware (60+ Archs)        │
└────────────────────────────────┘
```

### Einsatzgebiete

- Embedded Systems
- Forschung und Lehre
- Portierung auf neue Hardware
- Cross-Compilation-Host

## Siehe auch

- [[BSD]]
- [[FreeBSD]]
- [[OpenBSD]]
- [[DragonFly-BSD]]

## Quellen

- [NetBSD.org](https://www.netbsd.org/)
- [NetBSD Guide](https://www.netbsd.org/docs/guide/en/)
- [Wikipedia: NetBSD](https://en.wikipedia.org/wiki/NetBSD)
