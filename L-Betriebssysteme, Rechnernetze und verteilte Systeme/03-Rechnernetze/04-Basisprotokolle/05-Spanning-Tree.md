---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - stp
  - layer2
bereich: RN
---

# Spanning Tree Protocol (STP)

## Lernziele

- [ ] Problem der Layer-2-Schleifen verstehen
- [ ] STP-Algorithmus erklären können
- [ ] Port-Zustände und -Rollen kennen
- [ ] Varianten (RSTP, MSTP) unterscheiden können

## Überblick

Das **Spanning Tree Protocol (STP)** verhindert Schleifen in geswitchten Netzwerken. Ohne STP führen redundante Verbindungen zu Broadcast-Stürmen und MAC-Tabellen-Instabilität.

```
┌─────────────────────────────────────────────────────────────┐
│              Das Schleifenproblem                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   OHNE STP:                     MIT STP:                    │
│                                                              │
│   ┌────────┐                    ┌────────┐                  │
│   │Switch A│                    │Switch A│  ← Root Bridge  │
│   └───┬┬───┘                    └───┬────┘                  │
│       ││ ← Schleife!                │                       │
│   ┌───┴┴───┐                    ┌───┴────┐                  │
│   │Switch B│                    │Switch B│                  │
│   └────────┘                    └───┬────┘                  │
│                                     │                       │
│   → Broadcast-Sturm!            ┌───┴────┐                  │
│   → MAC-Flapping!               │Switch C│  X = Blocked    │
│                                 └────────┘                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] IEEE-Standard
> - STP: IEEE 802.1D (ursprünglich 1990, revidiert 2004)
> - RSTP: IEEE 802.1w (2001, in 802.1D-2004 integriert)
> - MSTP: IEEE 802.1s (2002, in 802.1Q integriert)

### Root Bridge Election

Im ersten Schritt wird eine **Root Bridge** ausgewählt, die als Ausgangspunkt für den Spannbaum fungiert:

- Jeder Switch hat eine **Bridge ID** (Priorität + MAC-Adresse)
- Die **niedrigste Bridge ID** gewinnt
- Standardpriorität: 32768
- Von der Root Bridge aus werden die Pfade ausgebaut

> [!warning] Sicherheitsrisiko
> Die vergleichsweise lange Ausfallzeit bei Neustrukturierung macht STP anfällig für Angriffe. Nur über die Root Bridge können Einstellungen verändert und Timer neu justiert werden.

### Pfadkostenberechnung

TODO: Kosten basierend auf Bandbreite

| Bandbreite | STP-Kosten (802.1D-1998) | RSTP-Kosten |
|------------|--------------------------|-------------|
| 10 Mbps | 100 | 2.000.000 |
| 100 Mbps | 19 | 200.000 |
| 1 Gbps | 4 | 20.000 |
| 10 Gbps | 2 | 2.000 |

## Port-Zustände

| Zustand | Frames | Adressen lernen | BPDUs empfangen | BPDUs senden |
|---------|--------|-----------------|-----------------|--------------|
| **Forwarding** | Weiterleiten | ✓ | ✓ | ✓ |
| **Blocking** | Verwerfen | ✗ | ✓ | ✗ |
| **Listening** | Verwerfen | ✗ | ✓ | ✓ |
| **Learning** | Verwerfen | ✓ | ✓ | ✓ |
| **Disabled** | Verwerfen | ✗ | ✗ | ✗ |

> [!info] BPDU
> **Bridge Protocol Data Units (BPDUs)** sind die Kontrollnachrichten, die Switches untereinander austauschen, um die Topologie zu ermitteln.

### Port-Rollen

- **Root Port**: Der Port mit dem kürzesten Pfad zur Root Bridge
- **Designated Port**: Der Port, der Frames an ein Segment weiterleitet
- **Blocked/Alternate Port**: Deaktivierter Port zur Schleifenvermeidung

## BPDU-Format

TODO: Bridge Protocol Data Unit

## Konvergenz

TODO: Konvergenzzeit (30-50 Sekunden bei STP)

## Varianten

### RSTP (Rapid Spanning Tree)

TODO: Schnellere Konvergenz, Proposal/Agreement

### MSTP (Multiple Spanning Tree)

TODO: Multiple Instanzen für VLANs

### PVST+ (Per-VLAN Spanning Tree)

TODO: Cisco-proprietär

## Sicherheit

### BPDU Guard

TODO: Schutz vor unautorisierten Switches

### Root Guard

TODO: Schutz der Root Bridge

## Praxisbeispiele

TODO: Switch-Konfiguration, show spanning-tree

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - Warum Schleifen problematisch sind
> - Root Bridge Election
> - Port-Rollen und -Zustände
> - Unterschied STP vs. RSTP

## Zusammenfassung

TODO: Kernpunkte zusammenfassen

## Querverweise

- [[../03-Referenzmodelle/05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – STP arbeitet auf Layer 2
- [[../03-Referenzmodelle/05-Sicherungsschicht/04-Broadcast-Kollisionsdomaene|Broadcast-Domäne]] – STP beeinflusst Broadcast-Verhalten
