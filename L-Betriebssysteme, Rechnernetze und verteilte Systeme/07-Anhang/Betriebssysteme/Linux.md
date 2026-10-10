---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Linux

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-ähnlicher Betriebssystem-Kernel |
| **Entwickler** | Linus Torvalds + Community |
| **Erstveröffentlichung** | 17. September 1991 |
| **Aktuelle Version** | 6.x (laufend) |
| **Lizenz** | GPL v2 |
| **Architektur** | x86, x86-64, ARM, RISC-V, u.v.m. |

## Zusammenfassung

Linux ist ein freier, Unix-ähnlicher Kernel, der zusammen mit GNU-Tools ein vollständiges Betriebssystem bildet. Als Open-Source-Projekt ist es heute das meistverbreitete Server-Betriebssystem, die Basis für Android und dominiert Cloud, Container und eingebettete Systeme.

### Die Geburtsnachricht

Linus Torvalds am 25. August 1991 in comp.os.minix:
> "I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones."

### Kernel-Architektur

Linux ist ein **monolithischer Kernel** mit ladbaren Modulen:

```
Linux Kernel-Architektur
┌─────────────────────────────────────┐
│          User Space                 │
│   (glibc, Apps, Daemons)           │
├─────────────────────────────────────┤
│        System Call Interface        │
├──────┬──────┬───────┬──────┬───────┤
│ VFS  │ Net  │Sched. │ MM   │ IPC   │
├──────┴──────┴───────┴──────┴───────┤
│           Device Drivers            │
│         (ladbare Module)            │
├─────────────────────────────────────┤
│    Architecture-Dependent Code      │
├─────────────────────────────────────┤
│            Hardware                 │
└─────────────────────────────────────┘
```

### Wichtige Distributionen

| Distribution | Fokus |
|--------------|-------|
| **Debian** | Stabilität, Freie Software |
| **Ubuntu** | Desktop, Benutzerfreundlichkeit |
| **Red Hat / Fedora** | Enterprise |
| **SUSE** | Enterprise, Europa |
| **Arch** | Minimalismus, Rolling Release |
| **Alpine** | Container, minimaler Footprint |

### Einsatzgebiete

| Bereich | Marktanteil |
|---------|-------------|
| Server | ~80% |
| Supercomputer | ~100% (Top 500) |
| Smartphones | ~85% (Android) |
| Cloud/Container | Dominant |
| Desktop | ~4% |

### Schlüsselinnovationen

- **Cgroups**: Ressourcen-Isolation (Basis für Container)
- **Namespaces**: Prozess-Isolation
- **eBPF**: Programmierbare Kernel-Erweiterungen
- **KVM**: Kernel-basierte Virtualisierung
- **btrfs/XFS/ext4**: Moderne Dateisysteme

### Versionsgeschichte (Auswahl)

| Version | Jahr | Milestone |
|---------|------|-----------|
| 0.01 | 1991 | Erste Version (10.000 LoC) |
| 1.0 | 1994 | Erste stabile Version |
| 2.0 | 1996 | SMP-Support |
| 2.4 | 2001 | USB, Enterprise-Features |
| 2.6 | 2003 | O(1)-Scheduler, NPTL |
| 3.0 | 2011 | 20-Jahr-Jubiläum |
| 4.0 | 2015 | Live Patching |
| 5.0 | 2019 | AMD GPU, btrfs RAID1 |
| 6.0 | 2022 | Rust im Kernel |

## Siehe auch

- [[UNIX]]
- [[Minix]]
- [[Android]]
- [[FreeBSD]]

## Quellen

- [kernel.org](https://www.kernel.org/)
- [Linux Foundation](https://www.linuxfoundation.org/)
- [Linux History (Kernel.org)](https://www.kernel.org/doc/html/latest/process/1.Intro.html)
- [Wikipedia: Linux](https://en.wikipedia.org/wiki/Linux)
