---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# DragonFly BSD

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | DragonFly BSD Project |
| **Gründer** | Matthew Dillon |
| **Erstveröffentlichung** | Juli 2004 |
| **Basis** | FreeBSD 4.8 Fork |
| **Lizenz** | BSD-Lizenz |

## Zusammenfassung

DragonFly BSD entstand als Fork von FreeBSD 4.8 mit dem Ziel, innovative Konzepte für Multiprocessing und Clustering zu implementieren. Das Projekt entwickelte das HAMMER-Dateisystem und einen einzigartigen Ansatz für SMP-Skalierung.

### Designziele

- Leichtgewichtige Kernel-Threads (LWKT)
- Message-Passing statt Locking
- Bessere SMP-Skalierung
- Clusterweite Single-System-Image (langfristig)

### HAMMER/HAMMER2 Dateisystem

| Feature | Beschreibung |
|---------|--------------|
| **History** | Automatische Versionierung aller Dateien |
| **Snapshots** | Effiziente Momentaufnahmen |
| **Checksums** | Datenintegritätsprüfung |
| **Clustering** | Multi-Node-Unterstützung (HAMMER2) |
| **Dedup** | Deduplizierung (HAMMER2) |

### Kernel-Architektur

```
DragonFly BSD Message Passing
┌─────────────────────────────────┐
│          User Threads           │
├─────────────────────────────────┤
│  LWKT (Light Weight Kernel      │
│        Threads)                 │
├─────────────────────────────────┤
│   Message Ports & IPI           │
│  (keine globalen Locks)         │
├─────────────────────────────────┤
│     Per-CPU Run Queues          │
└─────────────────────────────────┘
```

### Unterschiede zu FreeBSD

- Kein Giant Lock, minimales Locking
- Tokenbasierte Serialisierung
- Virtuelles Kernel (vkernel) für User-Mode-Kernel
- HAMMER statt UFS/ZFS als primäres FS

## Siehe auch

- [[BSD]]
- [[FreeBSD]]

## Quellen

- [DragonFlyBSD.org](https://www.dragonflybsd.org/)
- [HAMMER2 Design Document](https://www.dragonflybsd.org/hammer/)
- [Wikipedia: DragonFly BSD](https://en.wikipedia.org/wiki/DragonFly_BSD)
