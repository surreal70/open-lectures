---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Solaris

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | Sun Microsystems, Oracle |
| **Erstveröffentlichung** | 1992 (Solaris 2.0) |
| **Aktuelle Version** | 11.4 |
| **Lizenz** | Proprietär (früher teilweise CDDL) |
| **Architektur** | SPARC, x86-64 |

## Zusammenfassung

Solaris entstand aus SunOS und wurde zum technologisch fortschrittlichsten kommerziellen Unix. Es führte bahnbrechende Technologien wie ZFS, DTrace und Zones ein, die später in andere Systeme übernommen wurden.

### Bahnbrechende Technologien

| Technologie | Eingeführt | Beschreibung |
|-------------|------------|--------------|
| **ZFS** | 2005 | Revolutionäres Dateisystem |
| **DTrace** | 2005 | Dynamisches Tracing |
| **Zones** | 2005 | Betriebssystem-Virtualisierung |
| **SMF** | 2005 | Service Management Facility |
| **Crossbow** | 2008 | Netzwerkvirtualisierung |

### Versionsgeschichte

| Version | Jahr | Name/Basis |
|---------|------|------------|
| SunOS 4.x | 1988 | BSD-basiert |
| Solaris 2.0 | 1992 | SVR4-basiert |
| Solaris 7 | 1998 | 64-bit UltraSPARC |
| Solaris 10 | 2005 | ZFS, DTrace, Zones |
| Solaris 11 | 2011 | Erstes Cloud-OS |
| Solaris 11.4 | 2018 | Aktuelle Version |

### ZFS-Features

```
ZFS Storage Stack
┌─────────────────────────────────────┐
│           ZFS File System           │
├─────────────────────────────────────┤
│  Snapshots │ Clones │ Compression   │
├─────────────────────────────────────┤
│      ZFS Intent Log (ZIL)           │
├─────────────────────────────────────┤
│          Storage Pool (zpool)       │
├─────────┬─────────┬─────────────────┤
│  Mirror │ RAID-Z  │  RAID-Z2/Z3    │
├─────────┴─────────┴─────────────────┤
│        Physical Disks (vdevs)       │
└─────────────────────────────────────┘
```

### OpenSolaris und Derivate

Nach der Oracle-Übernahme (2010) entstanden aus OpenSolaris:
- **illumos**: Open-Source-Kernel-Fork
- **OpenIndiana**: Desktop-Distribution
- **SmartOS**: Cloud-Plattform (Joyent)
- **OmniOS**: Server-Distribution

## Siehe auch

- [[System-V]]
- [[BSD]]
- [[Linux]]

## Quellen

- [Oracle Solaris](https://www.oracle.com/solaris/)
- [illumos Project](https://illumos.org/)
- [Wikipedia: Solaris](https://en.wikipedia.org/wiki/Solaris_(operating_system))
