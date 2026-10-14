---
author: Andreas Hümmer
title: MAC-Protokolle und Medienzugriff
tags:
  - vorlesung
  - rn
  - layer2
  - csma-cd
  - spanning-tree
  - mac
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# MAC-Protokolle und Medienzugriff

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Das Problem des Medienzugriffs erklären
> - CSMA/CD und CSMA/CA unterscheiden
> - Das Spanning Tree Protocol verstehen
> - Die Funktion von Switches und Bridges erläutern
> - Kollisions- und Broadcast-Domänen unterscheiden

## Das Medienzugriffsproblem

Bei geteilten Medien (Shared Media) müssen Regeln festlegen, **wer wann senden darf**:

```
┌─────────────────────────────────────────────────────────────────┐
│              MEDIENZUGRIFFSVERFAHREN                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   DETERMINISTISCH                 PROBABILISTISCH               │
│   ──────────────                  ───────────────               │
│                                                                 │
│   Token Passing                   CSMA/CD (Ethernet)            │
│   • Token Ring                    • Carrier Sense              │
│   • Token Bus                     • Kollisionserkennung        │
│   • FDDI                          • Backoff bei Kollision      │
│                                                                 │
│   Polling                         CSMA/CA (WLAN)                │
│   • Master fragt Slaves           • Carrier Sense              │
│                                   • Kollisionsvermeidung       │
│   TDMA (Zeitmultiplex)            • RTS/CTS optional           │
│   • Feste Zeitschlitze                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## CSMA/CD – Carrier Sense Multiple Access / Collision Detection

### Funktionsweise

```
┌─────────────────────────────────────────────────────────────────┐
│                    CSMA/CD ABLAUF                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. CARRIER SENSE (Träger abhören)                            │
│      • Station prüft, ob Medium frei ist                       │
│      • Wenn belegt → warten                                    │
│                                                                 │
│   2. MULTIPLE ACCESS (Mehrfachzugriff)                         │
│      • Wenn frei → senden beginnen                             │
│      • Mehrere Stationen können gleichzeitig starten           │
│                                                                 │
│   3. COLLISION DETECTION (Kollisionserkennung)                 │
│      • Während des Sendens: Medium weiter abhören              │
│      • Kollision erkannt → Jam-Signal senden (32 Bit)         │
│      • Senden abbrechen                                        │
│                                                                 │
│   4. BACKOFF (Wartezeit)                                       │
│      • Zufällige Wartezeit nach Kollision                      │
│      • Binary Exponential Backoff:                             │
│        Wartezeit = random(0, 2^n - 1) × Slot-Time             │
│        n = Anzahl der Kollisionen (max. 10)                   │
│      • Nach 16 Kollisionen: Übertragung aufgeben              │
│                                                                 │
│   ┌─────┐     ┌─────┐                                          │
│   │  A  │═════│  B  │  A und B senden gleichzeitig            │
│   └─────┘     └─────┘                                          │
│        ╲     ╱                                                  │
│         ╲   ╱   KOLLISION!                                     │
│          ╲ ╱                                                    │
│           ╳                                                     │
│          ╱ ╲                                                    │
│         ╱   ╲   Jam → Backoff → Retry                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Slot-Time und Kollisionsdomäne

> [!wichtig] Kollisionserkennung
> Ein Sender muss eine Kollision erkennen können, **bevor** er das Senden beendet. Daher gilt:
> 
> **Minimale Frame-Größe** = 2 × Signallaufzeit × Datenrate
> 
> Bei Ethernet: 64 Bytes Minimum → max. Segmentlänge 100m bei 100 Mbit/s

| Geschwindigkeit | Slot-Time | Max. Segmentlänge |
|-----------------|-----------|-------------------|
| 10 Mbit/s | 51,2 µs | 2500 m (mit Repeatern) |
| 100 Mbit/s | 5,12 µs | 100 m |
| 1000 Mbit/s | 4,096 µs | Carrier Extension |

> [!info] Heute: Full-Duplex
> Moderne Ethernet-Netze mit Switches arbeiten im **Full-Duplex**-Modus. Jede Verbindung ist **Punkt-zu-Punkt**, daher gibt es **keine Kollisionen** mehr. CSMA/CD ist dann deaktiviert.

## CSMA/CA – Collision Avoidance (WLAN)

WLAN kann Kollisionen nicht erkennen (Sender übertönt schwache Signale), daher **Vermeidung** statt Erkennung:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CSMA/CA ABLAUF                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. Carrier Sense                                              │
│      • Prüfen, ob Medium frei                                  │
│                                                                 │
│   2. Wenn frei: DIFS warten                                    │
│      • Distributed Inter-Frame Space                           │
│      • Sicherstellen, dass wirklich frei                       │
│                                                                 │
│   3. Backoff-Counter                                            │
│      • Zufällige Wartezeit herunterzählen                      │
│      • Nur wenn Medium frei                                    │
│                                                                 │
│   4. Senden                                                     │
│      • Wenn Counter = 0 → senden                               │
│                                                                 │
│   5. ACK erwarten                                               │
│      • Empfänger bestätigt nach SIFS                           │
│      • Keine ACK → Kollision vermutet → Retry                  │
│                                                                 │
│   Optional: RTS/CTS (Request to Send / Clear to Send)          │
│   • Löst Hidden-Node-Problem                                   │
│   • Overhead für kurze Frames                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Spanning Tree Protocol (STP)

### Problem: Broadcast-Stürme

Redundante Verbindungen zwischen Switches können zu **Endlosschleifen** führen:

```
┌─────────────────────────────────────────────────────────────────┐
│              PROBLEM: LAYER-2-SCHLEIFE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│        ┌──────────┐          ┌──────────┐                      │
│        │ Switch A │══════════│ Switch B │                      │
│        └────┬─────┘          └─────┬────┘                      │
│             │                      │                            │
│             │    ┌──────────┐      │                            │
│             └────│ Switch C │──────┘                            │
│                  └──────────┘                                   │
│                                                                 │
│   Ein Broadcast-Frame kreist endlos!                           │
│   → Broadcast-Sturm → Netzwerk kollabiert                      │
│                                                                 │
│   Lösung: Spanning Tree Protocol (STP)                         │
│   • Erkennt Schleifen                                          │
│   • Blockiert redundante Ports                                 │
│   • Behält Redundanz für Failover                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### STP-Funktionsweise

```
┌─────────────────────────────────────────────────────────────────┐
│              SPANNING TREE PROTOCOL                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. ROOT BRIDGE WAHL                                           │
│      • Switch mit niedrigster Bridge-ID wird Root              │
│      • Bridge-ID = Priorität (2 Byte) + MAC (6 Byte)          │
│      • Default-Priorität: 32768                                │
│                                                                 │
│   2. PFADKOSTEN BERECHNEN                                       │
│      • Kosten basieren auf Linkgeschwindigkeit                 │
│      • Jeder Switch ermittelt besten Pfad zur Root             │
│                                                                 │
│   3. PORT-ROLLEN ZUWEISEN                                       │
│      • Root Port: Bester Weg zur Root Bridge                   │
│      • Designated Port: Bester Weg vom Segment zur Root        │
│      • Blocked Port: Redundante Ports werden blockiert         │
│                                                                 │
│   Port-Zustände:                                                │
│   ┌────────────┬─────────────────────────────────────────────┐ │
│   │ Disabled   │ Administrativ deaktiviert                   │ │
│   │ Blocking   │ Empfängt BPDUs, leitet keine Frames         │ │
│   │ Listening  │ Verarbeitet BPDUs, lernt keine MACs         │ │
│   │ Learning   │ Lernt MACs, leitet noch keine Frames        │ │
│   │ Forwarding │ Normaler Betrieb                            │ │
│   └────────────┴─────────────────────────────────────────────┘ │
│                                                                 │
│   Konvergenzzeit bei Topologieänderung: 30-50 Sekunden!       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### STP-Varianten

| Protokoll | Standard | Konvergenz | Besonderheit |
|-----------|----------|------------|--------------|
| STP | 802.1D | 30-50 s | Original |
| RSTP | 802.1w | 1-2 s | Rapid Spanning Tree |
| MSTP | 802.1s | 1-2 s | Multiple Spanning Tree |
| PVST+ | Cisco | 30-50 s | Per-VLAN STP |
| Rapid PVST+ | Cisco | 1-2 s | RSTP pro VLAN |

## Kollisions- und Broadcast-Domänen

```
┌─────────────────────────────────────────────────────────────────┐
│         KOLLISIONS- vs. BROADCAST-DOMÄNE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   KOLLISIONSDOMÄNE                                              │
│   • Bereich, in dem Kollisionen auftreten können               │
│   • Getrennt durch: Switch, Bridge, Router                     │
│   • NICHT getrennt durch: Hub, Repeater                        │
│                                                                 │
│   BROADCAST-DOMÄNE                                              │
│   • Bereich, den ein Broadcast erreicht                        │
│   • Getrennt durch: Router, VLAN                               │
│   • NICHT getrennt durch: Hub, Switch, Bridge                  │
│                                                                 │
│        ┌─────┐     ┌─────┐     ┌─────┐                        │
│        │ PC1 │─────│ Hub │─────│ PC2 │                        │
│        └─────┘     └──┬──┘     └─────┘                        │
│                       │                                         │
│              ┌────────┴────────┐                               │
│              │     Switch      │                               │
│              └────────┬────────┘                               │
│                       │                                         │
│        ┌─────┐     ┌──┴──┐     ┌─────┐                        │
│        │ PC3 │─────│     │─────│ PC4 │                        │
│        └─────┘     └─────┘     └─────┘                        │
│                                                                 │
│   Kollisionsdomänen: 3 (Hub-Segment, PC3-Port, PC4-Port)      │
│   Broadcast-Domäne: 1 (alle PCs)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **CSMA/CD**: Kollisionserkennung bei Ethernet (Half-Duplex)
> - **CSMA/CA**: Kollisionsvermeidung bei WLAN
> - Moderne Switches: **Full-Duplex**, keine Kollisionen
> - **STP** verhindert Schleifen bei redundanten Links
> - **RSTP** konvergiert schneller (1-2s statt 30-50s)
> - **Switch** trennt Kollisionsdomänen, **Router** trennt Broadcast-Domänen

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Verstehen Sie CSMA/CD und warum es heute selten relevant ist
> - Kennen Sie den Unterschied CSMA/CD vs. CSMA/CA
> - Wissen Sie, warum STP notwendig ist (Schleifen verhindern)
> - Können Sie Kollisions-/Broadcast-Domänen bestimmen

## Verwandte Themen

- [[01-Rahmenbildung]] – Ethernet-Frame
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE 802.3]] – Ethernet-Standard
- [[07-Anhang/IEEE-802-Standards/IEEE 802.1D|IEEE 802.1D]] – Spanning Tree

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
