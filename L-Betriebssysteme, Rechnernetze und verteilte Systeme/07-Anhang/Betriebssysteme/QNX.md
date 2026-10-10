---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# QNX

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Echtzeit-Mikrokernel-Betriebssystem |
| **Entwickler** | BlackBerry (früher QNX Software Systems) |
| **Erstveröffentlichung** | 1982 |
| **Lizenz** | Proprietär (Non-Commercial-Lizenz verfügbar) |
| **Architektur** | x86, ARM, PowerPC |

## Zusammenfassung

QNX ist ein echtes Mikrokernel-Betriebssystem mit POSIX-Kompatibilität. Es ist führend in der Automobil-Industrie (Infotainment, ADAS) und bekannt für seine Robustheit und Echtzeitfähigkeiten.

### Mikrokernel-Architektur

```
QNX Neutrino Mikrokernel
┌─────────────────────────────────────────┐
│    Anwendungen (User Space)             │
├────────┬────────┬────────┬──────────────┤
│ File   │Network │ Device │ Process      │
│ System │ Stack  │ Driver │ Manager      │
├────────┴────────┴────────┴──────────────┤
│         Message Passing IPC             │
├─────────────────────────────────────────┤
│         Neutrino Microkernel            │
│    (nur ~64 KB, Threads, Scheduling,    │
│     IPC, Interrupts)                    │
├─────────────────────────────────────────┤
│              Hardware                   │
└─────────────────────────────────────────┘
```

### Vorteile der Mikrokernel-Architektur

| Vorteil | Beschreibung |
|---------|--------------|
| **Isolation** | Treiber-Crash betrifft nicht Kernel |
| **Wartbarkeit** | Komponenten separat aktualisierbar |
| **Sicherheit** | Kleinere TCB (Trusted Computing Base) |
| **Determinismus** | Vorhersagbares Timing |

### Einsatzgebiete

| Branche | Anwendung |
|---------|-----------|
| Automotive | Infotainment (Audi, BMW, Mercedes) |
| Medizin | Chirurgie-Roboter |
| Industrie | Fabrikautomation |
| Bahn | Zugsteuerung |
| Nuklear | Kraftwerkssteuerung |

### QNX CAR/IVI

Die Automotive-Plattform bietet:
- Schneller Boot (<2 Sekunden bis GUI)
- Apple CarPlay / Android Auto
- Digital Cluster Support
- Hypervisor für Isolation

### Sicherheitszertifizierungen

- ISO 26262 (Automotive)
- IEC 61508 (Industrie)
- IEC 62304 (Medizin)
- EN 50128 (Bahn)

## Siehe auch

- [[VxWorks]]
- [[AUTOSAR]]
- [[Linux]]

## Quellen

- [BlackBerry QNX](https://blackberry.qnx.com/)
- [QNX Developer Network](https://www.qnx.com/developers/)
- [Wikipedia: QNX](https://en.wikipedia.org/wiki/QNX)
