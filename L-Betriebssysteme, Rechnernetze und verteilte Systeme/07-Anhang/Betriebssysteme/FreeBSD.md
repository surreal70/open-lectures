---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# FreeBSD

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | FreeBSD Project |
| **Erstveröffentlichung** | November 1993 |
| **Aktuelle Version** | 14.x (2023+) |
| **Lizenz** | BSD-Lizenz |
| **Architektur** | x86, x86-64, ARM, RISC-V |

## Zusammenfassung

FreeBSD ist das am weitesten verbreitete BSD-Derivat mit Fokus auf Performance, Stabilität und fortschrittliche Netzwerkfunktionen. Es bildet die Basis für PlayStation-Firmware und Teile von macOS/iOS.

### Hauptmerkmale

- **ZFS-Dateisystem**: Enterprise-Features wie Snapshots, RAID-Z
- **Jails**: Leichtgewichtige Container-Virtualisierung (seit 2000)
- **bhyve**: Moderner Hypervisor
- **DTrace**: Systemweites Tracing
- **Ports Collection**: Über 30.000 Softwarepakete

### Einsatzgebiete

| Bereich | Beispiele |
|---------|-----------|
| Server | Netflix CDN, WhatsApp |
| Embedded | PlayStation 3/4/5 |
| Storage | FreeNAS/TrueNAS |
| Netzwerk | pfSense, OPNsense Firewalls |

### Technische Besonderheiten

```
FreeBSD Kernel-Architektur
┌─────────────────────────────────────┐
│         Userspace (Apps)            │
├─────────────────────────────────────┤
│    libc / System Libraries          │
├─────────────────────────────────────┤
│  Syscall Interface                  │
├─────────────────────────────────────┤
│  VFS │ Network │ VM │ Scheduler     │
├─────────────────────────────────────┤
│        Device Drivers               │
├─────────────────────────────────────┤
│           Hardware                  │
└─────────────────────────────────────┘
```

## Siehe auch

- [[BSD]]
- [[OpenBSD]]
- [[NetBSD]]

## Quellen

- [FreeBSD.org](https://www.freebsd.org/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)
- [Wikipedia: FreeBSD](https://en.wikipedia.org/wiki/FreeBSD)
