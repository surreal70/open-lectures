---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# AUTOSAR (Automotive Open System Architecture)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Automotive-Software-Architektur |
| **Entwickler** | AUTOSAR-Konsortium |
| **Erstveröffentlichung** | 2003 |
| **Aktuelle Version** | Classic: R23-11, Adaptive: R23-11 |
| **Lizenz** | Konsortium-Mitgliedschaft |

## Zusammenfassung

AUTOSAR ist keine einzelne Software, sondern eine standardisierte Software-Architektur für Automobil-Steuergeräte (ECUs). Sie ermöglicht die Wiederverwendung von Software-Komponenten zwischen verschiedenen Fahrzeugherstellern und Zulieferern.

### Zwei Plattformen

```
AUTOSAR Plattformen
┌────────────────────────────────────────────────────────┐
│                                                        │
│  AUTOSAR Classic              AUTOSAR Adaptive         │
│  ─────────────────           ─────────────────────     │
│  Für: Echzeit-kritische      Für: Hochleistungs-       │
│       Steuergeräte                Systeme              │
│                                                        │
│  Beispiele:                  Beispiele:                │
│  - Motorsteuerung            - ADAS/Autonomes Fahren   │
│  - ABS/ESP                   - Infotainment            │
│  - Airbag                    - Vehicle-to-X            │
│                                                        │
│  Basis: OSEK/VDX             Basis: POSIX (Linux-like) │
│  Sprache: C                  Sprache: C++14/17         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### AUTOSAR Classic Architektur

```
AUTOSAR Classic Layered Architecture
┌─────────────────────────────────────────┐
│      Application Layer (SWC)            │
├─────────────────────────────────────────┤
│      Runtime Environment (RTE)          │
├──────────────┬──────────────────────────┤
│  Services    │   ECU Abstraction        │
│  Layer       │        Layer             │
├──────────────┼──────────────────────────┤
│    Complex   │  Microcontroller         │
│    Drivers   │  Abstraction Layer       │
├──────────────┴──────────────────────────┤
│              Microcontroller            │
└─────────────────────────────────────────┘
```

### Konsortium-Mitglieder

| Kategorie | Beispiele |
|-----------|-----------|
| OEMs | BMW, Daimler, Toyota, VW |
| Tier 1 | Bosch, Continental, ZF |
| Semiconductor | Infineon, NXP, Renesas |
| Tool-Anbieter | Vector, ETAS, dSPACE |

### Schlüsselkonzepte

| Konzept | Beschreibung |
|---------|--------------|
| **SWC** | Software Component |
| **RTE** | Runtime Environment |
| **BSW** | Basic Software |
| **VFB** | Virtual Functional Bus |
| **ARXML** | Konfigurationsformat |

### AUTOSAR Adaptive

Für moderne Fahrzeugfunktionen:
- Service-orientierte Architektur (SOA)
- POSIX-basiertes OS (meist Linux)
- C++14/17 statt C
- Dynamisches Laden von Anwendungen
- Kommunikation über SOME/IP

## Siehe auch

- [[QNX]]
- [[VxWorks]]
- [[Linux]]

## Quellen

- [AUTOSAR.org](https://www.autosar.org/)
- [AUTOSAR Specifications](https://www.autosar.org/standards/)
- [Wikipedia: AUTOSAR](https://en.wikipedia.org/wiki/AUTOSAR)
