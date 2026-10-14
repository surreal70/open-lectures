---
author: Andreas Hümmer
title: Spanning Tree Protocol (STP)
tags:
  - content
  - rn
  - protokolle
  - stp
  - rstp
  - layer2
  - switching
  - schleifenvermeidung
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Spanning Tree Protocol (STP)

## Definition

Das **Spanning Tree Protocol (STP)** verhindert Schleifen in geswitchten Layer-2-Netzwerken. Es erstellt einen schleifenfreien Spannbaum, indem es redundante Pfade blockiert und nur einen aktiven Pfad zwischen je zwei Netzwerkknoten zulässt.

> [!info] Schichtzuordnung
> STP ist ein **Layer-2-Protokoll** (Sicherungsschicht). Es arbeitet mit MAC-Adressen und Ethernet-Frames. Die BPDUs (Bridge Protocol Data Units) werden als Multicast an `01:80:C2:00:00:00` gesendet.

## Das Schleifenproblem

```
┌─────────────────────────────────────────────────────────────────┐
│              Warum sind Layer-2-Schleifen fatal?               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   OHNE STP (Schleife vorhanden):                               │
│                                                                  │
│        Switch A ◄─────────────────────► Switch B               │
│            │                                │                   │
│            └────────────► Switch C ◄────────┘                   │
│                              │                                  │
│                           Host X                                │
│                                                                  │
│   Problem 1: Broadcast-Sturm                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ Host X sendet einen Broadcast                           │  │
│   │ → Switch C flutet an A und B                            │  │
│   │ → A flutet an B, B flutet an A                          │  │
│   │ → Endlosschleife! Netzwerk kollabiert!                  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Problem 2: MAC-Flapping                                       │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ Switch sieht dieselbe MAC-Adresse an verschiedenen     │  │
│   │ Ports → MAC-Tabelle instabil → Pakete werden falsch    │  │
│   │ zugestellt                                              │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Problem 3: Mehrfachzustellung                                │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ Unicast-Frames erreichen Ziel mehrfach                  │  │
│   │ → Anwendungsprobleme, Duplikate                         │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## STP-Lösung: Der Spannbaum

> [!info] IEEE-Standard
> - **STP**: IEEE 802.1D (ursprünglich 1990, revidiert 2004)
> - **RSTP**: IEEE 802.1w (2001, in 802.1D-2004 integriert)
> - **MSTP**: IEEE 802.1s (2002, in 802.1Q integriert)

```
┌─────────────────────────────────────────────────────────────────┐
│              STP erstellt schleifenfreien Baum                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   VORHER (mit Schleife):        NACHHER (mit STP):             │
│                                                                  │
│        A ◄────────► B                A ◄────────► B             │
│        │            │                │    Root     │            │
│        │            │                │   Bridge    │            │
│        └─────► C ◄──┘                └─────► C ◄───┘            │
│             Schleife!                      │ X                  │
│                                       Blocked                   │
│                                                                  │
│   STP blockiert einen Port, um die Schleife zu unterbrechen.   │
│   Bei Ausfall wird der blockierte Port automatisch aktiviert.  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Root Bridge Election

Der erste Schritt in STP ist die Wahl der **Root Bridge** – der zentrale Punkt des Spannbaums.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Root Bridge Election                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Jeder Switch hat eine Bridge ID (8 Bytes):                   │
│                                                                  │
│   ┌──────────────────┬──────────────────────────────────────┐  │
│   │ Priority (2 Byte)│      MAC-Adresse (6 Byte)            │  │
│   │   0 - 65535      │      z.B. 00:1A:2B:3C:4D:5E          │  │
│   │   Default: 32768 │                                       │  │
│   └──────────────────┴──────────────────────────────────────┘  │
│                                                                  │
│   Regel: Die NIEDRIGSTE Bridge ID gewinnt!                     │
│                                                                  │
│   Beispiel:                                                     │
│   Switch A: Priority 32768, MAC 00:11:22:33:44:55              │
│   Switch B: Priority 32768, MAC 00:11:22:33:44:44  ← Root!     │
│   Switch C: Priority 32768, MAC 00:11:22:33:44:66              │
│                                                                  │
│   → Switch B wird Root Bridge (niedrigste MAC bei gleicher     │
│     Priority)                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!tip] Root Bridge gezielt setzen
> Um einen bestimmten Switch zur Root Bridge zu machen, setzt man dessen Priority niedriger:
> ```
> Switch(config)# spanning-tree vlan 1 priority 4096
> ```
> Priority muss ein Vielfaches von 4096 sein (0, 4096, 8192, ..., 61440).

## Pfadkosten

Nach der Root Bridge Election berechnet jeder Switch den kürzesten Pfad zur Root Bridge basierend auf **Pfadkosten**.

| Bandbreite | STP-Kosten (802.1D-1998) | RSTP-Kosten (802.1D-2004) |
|------------|--------------------------|---------------------------|
| 10 Mbps | 100 | 2.000.000 |
| 100 Mbps | 19 | 200.000 |
| 1 Gbps | 4 | 20.000 |
| 10 Gbps | 2 | 2.000 |
| 100 Gbps | — | 200 |

```
┌─────────────────────────────────────────────────────────────────┐
│              Pfadkostenberechnung                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    Root Bridge (A)                              │
│                    Priority: 4096                               │
│                         │                                       │
│              ┌──────────┴──────────┐                            │
│              │ 1 Gbps              │ 1 Gbps                     │
│              │ Kosten: 4           │ Kosten: 4                  │
│              ▼                     ▼                            │
│          Switch B              Switch C                         │
│          Root Path Cost: 4     Root Path Cost: 4               │
│              │                     │                            │
│              │ 100 Mbps            │                            │
│              │ Kosten: 19          │                            │
│              ▼                     │                            │
│          Switch D ◄────────────────┘                            │
│          Root Path Cost: 23   oder   4                         │
│                                                                  │
│   Switch D wählt den Pfad über C (Kosten 4) statt über B (23)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Port-Rollen

| Rolle | Beschreibung | Zustand |
|-------|--------------|---------|
| **Root Port (RP)** | Port mit kürzestem Pfad zur Root Bridge | Forwarding |
| **Designated Port (DP)** | Bester Port für ein Segment zur Root Bridge | Forwarding |
| **Blocked/Alternate Port** | Redundanter Port, deaktiviert | Blocking |
| **Backup Port** | Redundanter Port zum gleichen Segment (RSTP) | Blocking |

```
┌─────────────────────────────────────────────────────────────────┐
│                    Port-Rollen Beispiel                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                     Root Bridge (A)                             │
│                    ┌──────────────┐                             │
│                    │   DP    DP   │                             │
│                    └───┬──────┬───┘                             │
│                        │      │                                 │
│              ┌─────────┘      └─────────┐                       │
│              │                          │                       │
│         ┌────┴────┐                ┌────┴────┐                  │
│         │RP    DP │                │ RP   DP │                  │
│         │ Switch B│                │Switch C │                  │
│         └────┬────┘                └────┬────┘                  │
│              │                          │                       │
│              │         ┌────────────────┘                       │
│              │         │                                        │
│         ┌────┴─────────┴────┐                                   │
│         │RP      Blocked    │                                   │
│         │     Switch D      │                                   │
│         └───────────────────┘                                   │
│                                                                  │
│   RP = Root Port, DP = Designated Port                         │
│   Switch D: Port zu B ist Root Port (besserer Pfad)            │
│            Port zu C ist Blocked (Schleifenvermeidung)         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Port-Zustände (STP)

| Zustand | Frames | MAC lernen | BPDUs RX | BPDUs TX | Dauer |
|---------|--------|------------|----------|----------|-------|
| **Disabled** | ✗ | ✗ | ✗ | ✗ | — |
| **Blocking** | ✗ | ✗ | ✓ | ✗ | 20s (max age) |
| **Listening** | ✗ | ✗ | ✓ | ✓ | 15s (forward delay) |
| **Learning** | ✗ | ✓ | ✓ | ✓ | 15s (forward delay) |
| **Forwarding** | ✓ | ✓ | ✓ | ✓ | — |

```
┌─────────────────────────────────────────────────────────────────┐
│              STP Port-Zustandsübergänge                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Port aktiviert                                                │
│        │                                                        │
│        ▼                                                        │
│   ┌─────────┐                                                   │
│   │Blocking │ ←──── Port wird blockiert                        │
│   └────┬────┘                                                   │
│        │ Port soll aktiv werden (20s Max Age)                  │
│        ▼                                                        │
│   ┌─────────┐                                                   │
│   │Listening│  ←── Sendet/empfängt BPDUs                       │
│   └────┬────┘       (15s Forward Delay)                        │
│        │                                                        │
│        ▼                                                        │
│   ┌─────────┐                                                   │
│   │Learning │  ←── Lernt MAC-Adressen                          │
│   └────┬────┘       (15s Forward Delay)                        │
│        │                                                        │
│        ▼                                                        │
│   ┌──────────┐                                                  │
│   │Forwarding│ ←── Leitet Frames weiter                        │
│   └──────────┘                                                  │
│                                                                  │
│   Gesamte Konvergenzzeit: 30-50 Sekunden!                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## BPDU-Format

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│      Protocol ID (0x0000)     │    Version    │   BPDU Type   │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                              Flags                            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                         Root Bridge ID                        │
│                           (8 Bytes)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                        Root Path Cost                         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                        Bridge ID                              │
│                           (8 Bytes)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│           Port ID             │         Message Age           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│           Max Age             │         Hello Time            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│        Forward Delay          │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### STP-Timer

| Timer | Default | Beschreibung |
|-------|---------|--------------|
| **Hello Time** | 2s | Intervall für BPDU-Versand |
| **Max Age** | 20s | Zeit bis BPDU als veraltet gilt |
| **Forward Delay** | 15s | Zeit in Listening/Learning |

## RSTP (Rapid Spanning Tree)

RSTP (IEEE 802.1w) verbessert die Konvergenzzeit drastisch:

```
┌─────────────────────────────────────────────────────────────────┐
│              STP vs. RSTP Konvergenz                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   STP:  Blocking → Listening → Learning → Forwarding           │
│         (20s)       (15s)       (15s)                          │
│         Gesamt: 30-50 Sekunden                                 │
│                                                                  │
│   RSTP: Discarding ────────────────────► Forwarding            │
│         Proposal/Agreement-Mechanismus                         │
│         Gesamt: < 1 Sekunde (oft Millisekunden!)               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### RSTP Port-Zustände

| STP | RSTP | Aktiv |
|-----|------|-------|
| Disabled | Discarding | Nein |
| Blocking | Discarding | Nein |
| Listening | Discarding | Nein |
| Learning | Learning | Nein |
| Forwarding | Forwarding | Ja |

### RSTP Proposal/Agreement

```
┌─────────────────────────────────────────────────────────────────┐
│              RSTP Proposal/Agreement                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Switch A (Root)                    Switch B                   │
│       │                                  │                      │
│       │  BPDU mit Proposal-Flag         │                      │
│       │────────────────────────────────►│                      │
│       │                                  │                      │
│       │                        B blockiert alle                 │
│       │                        anderen Ports                    │
│       │                                  │                      │
│       │  BPDU mit Agreement-Flag        │                      │
│       │◄────────────────────────────────│                      │
│       │                                  │                      │
│       │  Port geht sofort auf           │                      │
│       │  Forwarding!                    │                      │
│       │                                  │                      │
│                                                                  │
│   → Kein Warten auf Timer, sofortige Konvergenz!               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## MSTP (Multiple Spanning Tree)

MSTP (IEEE 802.1s) ermöglicht mehrere STP-Instanzen für verschiedene VLANs:

```
┌─────────────────────────────────────────────────────────────────┐
│              MSTP - Multiple Instances                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Problem mit klassischem STP:                                 │
│   → Eine Root Bridge für alle VLANs                            │
│   → Suboptimale Pfade für manche VLANs                        │
│   → Keine Lastverteilung                                       │
│                                                                  │
│   MSTP-Lösung:                                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ Instance 1 (VLAN 10, 20):    Root = Switch A            │  │
│   │ Instance 2 (VLAN 30, 40):    Root = Switch B            │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   → Lastverteilung über verschiedene Pfade                     │
│   → Optimale Pfade pro VLAN-Gruppe                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Sicherheit

### BPDU Guard

```
┌─────────────────────────────────────────────────────────────────┐
│                    BPDU Guard                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Problem: Angreifer schließt Switch mit niedriger Priority an │
│           → Wird zur Root Bridge → MITM möglich!               │
│                                                                  │
│   Lösung: BPDU Guard auf Access-Ports                          │
│                                                                  │
│   ┌──────────────────────────────────────────┐                 │
│   │ Wenn BPDU empfangen wird:                │                 │
│   │ → Port wird sofort disabled (err-disabled)│                 │
│   │ → Admin-Eingriff nötig zur Reaktivierung │                 │
│   └──────────────────────────────────────────┘                 │
│                                                                  │
│   Cisco-Konfiguration:                                         │
│   Switch(config-if)# spanning-tree bpduguard enable           │
│   oder global:                                                  │
│   Switch(config)# spanning-tree portfast bpduguard default    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Root Guard

```
┌─────────────────────────────────────────────────────────────────┐
│                    Root Guard                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Problem: Upstream-Switch wird durch bessere BPDU             │
│           zur Root Bridge degradiert                           │
│                                                                  │
│   Lösung: Root Guard auf Ports zu Downstream-Switches          │
│                                                                  │
│   ┌──────────────────────────────────────────┐                 │
│   │ Wenn Superior BPDU empfangen wird:       │                 │
│   │ → Port geht in "root-inconsistent" State │                 │
│   │ → Keine Frames werden weitergeleitet     │                 │
│   │ → Automatische Erholung wenn BPDU stoppt │                 │
│   └──────────────────────────────────────────┘                 │
│                                                                  │
│   Cisco-Konfiguration:                                         │
│   Switch(config-if)# spanning-tree guard root                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Praxisbeispiele

> [!example] Switch-Befehle (Cisco IOS)
> 
> ```
> ! STP-Status anzeigen
> Switch# show spanning-tree
> 
> VLAN0001
>   Spanning tree enabled protocol rstp
>   Root ID    Priority    4096
>              Address     0011.2233.4455
>              This bridge is the root
> 
> Interface        Role Sts Cost      Prio.Nbr Type
> ---------------- ---- --- --------- -------- ----
> Gi0/1            Desg FWD 4         128.1    P2p
> Gi0/2            Desg FWD 4         128.2    P2p
> 
> ! Priority setzen (Root Bridge werden)
> Switch(config)# spanning-tree vlan 1 priority 4096
> 
> ! PortFast aktivieren (Access-Ports)
> Switch(config-if)# spanning-tree portfast
> ```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. Warum sind Layer-2-Schleifen problematisch?
> 2. Root Bridge Election (Bridge ID = Priority + MAC)
> 3. Port-Rollen (Root, Designated, Blocked)
> 4. Port-Zustände (Blocking, Listening, Learning, Forwarding)
> 5. STP vs. RSTP Konvergenzzeit
> 6. BPDU Guard / Root Guard

### Typische Prüfungsfragen

> [!question] Übungsfragen
> 1. Was passiert ohne STP bei redundanten Verbindungen?
> 2. Wie wird die Root Bridge gewählt?
> 3. Was ist der Unterschied zwischen Root Port und Designated Port?
> 4. Warum ist RSTP schneller als STP?
> 5. Wie schützt BPDU Guard vor Angriffen?

### Merkhilfen

> [!tip] Merkregeln
> - **Root Bridge** = Niedrigste Bridge ID gewinnt
> - **Root Port** = Bester Weg ZUR Root
> - **Designated Port** = Bester Weg VON der Root (pro Segment)
> - **STP-Konvergenz** = 30-50 Sekunden
> - **RSTP-Konvergenz** = < 1 Sekunde

## Zusammenfassung

```
┌─────────────────────────────────────────────────────────────────┐
│              Spanning Tree auf einen Blick                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zweck:      Schleifenvermeidung in Layer-2-Netzen            │
│   Schicht:    Layer 2 (Sicherungsschicht)                      │
│   Standard:   IEEE 802.1D (STP), 802.1w (RSTP), 802.1s (MSTP) │
│   Multicast:  01:80:C2:00:00:00                                │
│                                                                  │
│   Ablauf:                                                       │
│   1. Root Bridge Election (niedrigste Bridge ID)               │
│   2. Root Ports bestimmen (kürzester Pfad zur Root)           │
│   3. Designated Ports bestimmen (bester Port pro Segment)     │
│   4. Übrige Ports blockieren                                   │
│                                                                  │
│   Bridge ID: Priority (2 Byte) + MAC-Adresse (6 Byte)         │
│   Pfadkosten: Bandbreitenabhängig (1 Gbps = 4, 100 Mbps = 19) │
│                                                                  │
│   Konvergenz: STP 30-50s, RSTP < 1s                           │
│   Sicherheit: BPDU Guard, Root Guard                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Querverweise

- [[../03-Referenzmodelle/05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – STP arbeitet auf Layer 2
- [[../03-Referenzmodelle/05-Sicherungsschicht/04-Broadcast-Kollisionsdomaene|Broadcast-Domäne]] – STP verhindert Broadcast-Stürme
- [[01-ARP|ARP]] – Broadcasts, die ohne STP zu Stürmen führen würden

## Quellen

- IEEE 802.1D-2004 - MAC Bridges and Bridged Networks
- IEEE 802.1w - Rapid Spanning Tree Protocol
- IEEE 802.1Q - VLAN und MSTP
