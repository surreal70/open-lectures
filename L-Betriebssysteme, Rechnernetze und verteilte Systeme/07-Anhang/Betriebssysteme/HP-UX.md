---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# HP-UX

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | Hewlett-Packard / HPE |
| **Erstveröffentlichung** | 1984 |
| **Aktuelle Version** | 11i v3 (11.31) |
| **Lizenz** | Proprietär |
| **Architektur** | PA-RISC, Itanium |

## Zusammenfassung

HP-UX ist Hewlett-Packards Unix-Implementierung für Mission-Critical Enterprise-Systeme. Das System ist bekannt für extreme Stabilität, Hochverfügbarkeit und wird weiterhin auf Itanium-Servern unterstützt.

### Hauptmerkmale

| Feature | Beschreibung |
|---------|--------------|
| **ServiceGuard** | HA-Clustering mit automatischem Failover |
| **VxFS** | Veritas File System (JFS) |
| **LVM** | Logical Volume Manager (HP-Erfindung) |
| **vPars/nPars** | Hardware-Partitionierung |
| **Integrity VM** | Virtualisierung auf Itanium |

### Versionsgeschichte

| Version | Jahr | Plattform |
|---------|------|-----------|
| HP-UX 1.0 | 1984 | HP 9000 (Motorola 68k) |
| HP-UX 8.0 | 1991 | PA-RISC |
| HP-UX 10.x | 1995 | PA-RISC |
| HP-UX 11.0 | 1997 | 64-bit PA-RISC |
| HP-UX 11i v1 | 2000 | PA-RISC & Itanium |
| HP-UX 11i v3 | 2007 | Itanium |

### Hochverfügbarkeits-Architektur

```
HP-UX ServiceGuard Cluster
┌────────────────┐   ┌────────────────┐
│   Node 1       │   │   Node 2       │
│   (Primary)    │   │   (Standby)    │
├────────────────┤   ├────────────────┤
│   HP-UX 11i    │   │   HP-UX 11i    │
│   ServiceGuard │◄─►│   ServiceGuard │
└───────┬────────┘   └───────┬────────┘
        │    Heartbeat       │
        │◄──────────────────►│
        │                    │
   ┌────┴────────────────────┴────┐
   │      Shared Storage          │
   │        (SAN/FC)              │
   └──────────────────────────────┘
```

### Einsatzgebiete

- SAP-Systeme
- Oracle-Datenbanken
- Telekommunikation
- Finanzsektor

## Siehe auch

- [[System-V]]
- [[AIX]]
- [[Solaris]]

## Quellen

- [HPE HP-UX](https://www.hpe.com/us/en/servers/hp-ux.html)
- [HP-UX Documentation](https://support.hpe.com/hpesc/public/home)
- [Wikipedia: HP-UX](https://en.wikipedia.org/wiki/HP-UX)
