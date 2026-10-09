---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# SCO Unix / SCO OpenServer

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | Santa Cruz Operation (SCO) |
| **Erstveröffentlichung** | 1989 |
| **Letzte Version** | OpenServer 6 (2005) |
| **Lizenz** | Proprietär |
| **Architektur** | x86 |

## Zusammenfassung

SCO Unix (später SCO OpenServer und UnixWare) war in den 1990ern die dominierende Unix-Plattform für x86-Server. Nach der Übernahme von Xenix von Microsoft wurde SCO zum größten Unix-Anbieter für PC-Hardware.

### Produkte

| Produkt | Beschreibung |
|---------|--------------|
| **SCO Xenix** | Microsoft-Unix-Nachfolger |
| **SCO Unix** | System V für 386 |
| **OpenServer** | Enterprise-Server-Unix |
| **UnixWare** | SVR4.2-basiert (von Novell gekauft) |

### Zeitlinie

| Jahr | Ereignis |
|------|----------|
| 1979 | SCO gegründet (Santa Cruz Operation) |
| 1987 | Xenix von Microsoft übernommen |
| 1989 | SCO Unix 3.2 |
| 1992 | OpenServer |
| 1995 | UnixWare von Novell gekauft |
| 2000 | Verkauf an Caldera |
| 2003-2007 | SCO vs. IBM Rechtsstreit |
| 2007 | Konkurs |

### Der SCO-Linux-Rechtsstreit

SCO (unter Caldera/The SCO Group) verklagte IBM 2003 wegen angeblicher Verwendung von Unix-Code in Linux. Der langwierige Rechtsstreit endete mit:
- SCO verliert Urheberrechtsansprüche
- Novell hält Unix-Copyrights
- SCO meldet Insolvenz an (2007)

### Technische Merkmale

- Unix System V Release 3.2 / 4.2 Basis
- Läuft auf Standard-PC-Hardware
- Gute Hardware-Unterstützung für seine Zeit
- Volle POSIX-Kompatibilität
- Multiuser-fähig mit Terminals

```
SCO-Produktlinie
┌──────────────────────────────────────┐
│           Microsoft Xenix            │
│              (1980-1987)             │
└──────────────────┬───────────────────┘
                   │
         ┌─────────▼─────────┐
         │    SCO Unix       │
         │    (1989)         │
         └─────────┬─────────┘
        ┌──────────┴──────────┐
        │                     │
┌───────▼───────┐     ┌───────▼───────┐
│  OpenServer   │     │   UnixWare    │
│  (SCO Unix)   │     │   (Novell)    │
└───────────────┘     └───────────────┘
```

## Siehe auch

- [[Xenix]]
- [[System-V]]
- [[Linux]]

## Quellen

- [SCO History Archive](https://archive.org/search.php?query=SCO%20Unix)
- [Groklaw SCO Litigation Archive](https://www.groklaw.net/)
- [Wikipedia: SCO Group](https://en.wikipedia.org/wiki/SCO_Group)
