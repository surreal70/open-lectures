---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# AIX (Advanced Interactive eXecutive)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | IBM |
| **Erstveröffentlichung** | 1986 |
| **Aktuelle Version** | 7.3 |
| **Lizenz** | Proprietär |
| **Architektur** | POWER (früher: ROMP, RS/6000) |

## Zusammenfassung

AIX ist IBMs Unix-Implementierung für POWER-Prozessoren. Das System bietet fortschrittliche Virtualisierung, Workload-Partitionierung und Enterprise-Features für geschäftskritische Anwendungen.

### Hauptmerkmale

| Feature | Beschreibung |
|---------|--------------|
| **LPAR** | Logical Partitioning der Hardware |
| **WPAR** | Workload Partitions (Container) |
| **PowerVM** | Hypervisor-Virtualisierung |
| **JFS2** | Journaling File System 2 |
| **Live Partition Mobility** | VM-Migration ohne Downtime |

### Technische Innovationen

AIX führte mehrere Technologien ein, die später Standard wurden:

- **Journaling File System (JFS)**: Erstes kommerzielles JFS (1990)
- **Logical Volume Manager**: Frühe LVM-Implementierung
- **SMIT**: System Management Interface Tool
- **ODM**: Object Data Manager für Konfiguration

### Versionsgeschichte

| Version | Jahr | Neuerungen |
|---------|------|------------|
| AIX 1.0 | 1986 | PS/2 und RT PC |
| AIX 3.1 | 1990 | RS/6000, JFS |
| AIX 4.x | 1994 | 64-bit, SMP |
| AIX 5L | 2001 | Linux-Affinität |
| AIX 6.1 | 2007 | WPAR |
| AIX 7.x | 2010+ | Cloud, Live Update |

### Virtualisierung

```
AIX PowerVM Architektur
┌──────────────────────────────────────┐
│            POWER Hardware            │
├──────────────────────────────────────┤
│      PowerVM Hypervisor (PHYP)       │
├─────────┬─────────┬─────────┬────────┤
│  LPAR 1 │  LPAR 2 │  LPAR 3 │ VIOS   │
│  AIX    │  AIX    │  Linux  │(I/O)   │
├─────────┼─────────┼─────────┼────────┤
│  WPAR   │  WPAR   │         │        │
│  WPAR   │         │         │        │
└─────────┴─────────┴─────────┴────────┘
```

## Siehe auch

- [[System-V]]
- [[HP-UX]]
- [[Solaris]]

## Quellen

- [IBM AIX](https://www.ibm.com/products/aix)
- [AIX Documentation](https://www.ibm.com/docs/en/aix)
- [Wikipedia: AIX](https://en.wikipedia.org/wiki/AIX)
