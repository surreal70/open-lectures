---
author: Andreas Hümmer
title: Broadcast- und Kollisionsdomäne
tags:
  - content
  - rn
  - network-layer
  - broadcast
  - kollision
  - switch
  - router
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Broadcast- und Kollisionsdomäne

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Begriffe Broadcast- und Kollisionsdomäne definieren
> - Die Unterschiede zwischen beiden Konzepten erklären
> - Erkennen, welche Geräte Domänen trennen oder verbinden
> - Netzwerke hinsichtlich ihrer Domänenstruktur analysieren

## Definitionen

### Kollisionsdomäne (Collision Domain)

Eine **Kollisionsdomäne** ist der Netzwerkbereich, in dem Datenpakete miteinander kollidieren können, wenn zwei oder mehr Geräte gleichzeitig senden.

```
┌─────────────────────────────────────────────────────────────────┐
│                    KOLLISIONSDOMÄNE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Eigenschaften:                                                 │
│  • Layer 1 / Layer 2 Konzept (Physisch/Sicherung)             │
│  • Betrifft das gemeinsam genutzte Übertragungsmedium          │
│  • Nur relevant bei Half-Duplex und Shared Media              │
│  • Alle Geräte "hören" die gleichen Signale                   │
│  • CSMA/CD regelt den Zugriff                                  │
│                                                                 │
│  Beispiel: Koaxial-Ethernet (10BASE2, 10BASE5)                 │
│                                                                 │
│       ══════════════════════════════════════════               │
│          │         │         │         │                        │
│        ┌─┴─┐     ┌─┴─┐     ┌─┴─┐     ┌─┴─┐                    │
│        │PC1│     │PC2│     │PC3│     │PC4│                    │
│        └───┘     └───┘     └───┘     └───┘                    │
│                                                                 │
│        └─────────────────────────────────────┘                 │
│                 EINE Kollisionsdomäne                          │
│                                                                 │
│  → Wenn PC1 und PC3 gleichzeitig senden: KOLLISION!           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Broadcast-Domäne (Broadcast Domain)

Eine **Broadcast-Domäne** ist der Netzwerkbereich, in dem ein Broadcast-Frame (Ziel: FF:FF:FF:FF:FF:FF) alle Geräte erreicht.

```
┌─────────────────────────────────────────────────────────────────┐
│                    BROADCAST-DOMÄNE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Eigenschaften:                                                 │
│  • Layer 2 / Layer 3 Konzept (Sicherung/Vermittlung)          │
│  • Betrifft die logische Netzwerkstruktur                      │
│  • Alle Geräte empfangen Broadcast-Frames                      │
│  • Entspricht typischerweise einem IP-Subnetz                  │
│  • Begrenzt durch Router (Layer 3 Geräte)                      │
│                                                                 │
│  Beispiel: Geswitchtes Ethernet                                │
│                                                                 │
│                    ┌────────┐                                  │
│                    │ Switch │                                  │
│                    └───┬────┘                                  │
│           ┌────────┬───┴───┬────────┐                          │
│           │        │       │        │                          │
│        ┌──┴──┐  ┌──┴──┐ ┌──┴──┐  ┌──┴──┐                      │
│        │ PC1 │  │ PC2 │ │ PC3 │  │ PC4 │                      │
│        └─────┘  └─────┘ └─────┘  └─────┘                      │
│                                                                 │
│        └─────────────────────────────────────┘                 │
│                 EINE Broadcast-Domäne                          │
│                                                                 │
│  → Broadcast von PC1 erreicht PC2, PC3 und PC4                │
│  → Aber: KEINE Kollisionen mehr (Switch trennt!)              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Gegenüberstellung

### Vergleichstabelle

| Aspekt | Kollisionsdomäne | Broadcast-Domäne |
|--------|------------------|------------------|
| **OSI-Schicht** | Layer 1 (physisch) | Layer 2 (logisch) |
| **Trennung durch** | Switch, Bridge | Router, Layer-3-Switch |
| **Relevanz** | Shared Media, Half-Duplex | Immer (auch Full-Duplex) |
| **Betrifft** | Signalübertragung | Frame-Verteilung |
| **Problem** | Kollisionen, Durchsatz | Broadcast-Stürme, Skalierung |
| **Adressierung** | - | MAC FF:FF:FF:FF:FF:FF |

### Visuelle Gegenüberstellung

```
┌─────────────────────────────────────────────────────────────────┐
│           KOLLISIONSDOMÄNE VS. BROADCAST-DOMÄNE                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SZENARIO 1: Hub (Repeater)                                    │
│  ───────────────────────────                                   │
│                                                                 │
│                    ┌───────┐                                   │
│                    │  HUB  │                                   │
│                    └───┬───┘                                   │
│           ┌────────┬───┴───┬────────┐                          │
│        ┌──┴──┐  ┌──┴──┐ ┌──┴──┐  ┌──┴──┐                      │
│        │ PC1 │  │ PC2 │ │ PC3 │  │ PC4 │                      │
│        └─────┘  └─────┘ └─────┘  └─────┘                      │
│                                                                 │
│        Kollisionsdomänen:  1 (alle Geräte)                     │
│        Broadcast-Domänen:  1 (alle Geräte)                     │
│                                                                 │
│  ═══════════════════════════════════════════════════════════   │
│                                                                 │
│  SZENARIO 2: Switch                                            │
│  ──────────────────────                                        │
│                                                                 │
│                    ┌────────┐                                  │
│                    │ SWITCH │                                  │
│                    └───┬────┘                                  │
│           ┌────────┬───┴───┬────────┐                          │
│        ┌──┴──┐  ┌──┴──┐ ┌──┴──┐  ┌──┴──┐                      │
│        │ PC1 │  │ PC2 │ │ PC3 │  │ PC4 │                      │
│        └─────┘  └─────┘ └─────┘  └─────┘                      │
│           │        │       │        │                          │
│           ▼        ▼       ▼        ▼                          │
│          KD1      KD2     KD3      KD4                         │
│                                                                 │
│        Kollisionsdomänen:  4 (eine pro Port)                   │
│        Broadcast-Domänen:  1 (alle Geräte)                     │
│                                                                 │
│  ═══════════════════════════════════════════════════════════   │
│                                                                 │
│  SZENARIO 3: Router (oder Layer-3-Switch)                      │
│  ────────────────────────────────────────                      │
│                                                                 │
│      ┌────────┐           ┌────────┐                          │
│      │Switch A│           │Switch B│                          │
│      └───┬────┘           └───┬────┘                          │
│     ┌────┴────┐          ┌────┴────┐                          │
│  ┌──┴──┐  ┌──┴──┐    ┌──┴──┐  ┌──┴──┐                        │
│  │ PC1 │  │ PC2 │    │ PC3 │  │ PC4 │                        │
│  └─────┘  └─────┘    └─────┘  └─────┘                        │
│     │        │          │        │                             │
│    KD1      KD2        KD3      KD4                            │
│     └────────┘          └────────┘                             │
│        BD1      ┌────────┐  BD2                                │
│                 │ ROUTER │                                     │
│                 └────────┘                                     │
│                                                                 │
│        Kollisionsdomänen:  4 (eine pro Switch-Port)            │
│        Broadcast-Domänen:  2 (eine pro Router-Interface)       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Geräte und ihre Wirkung auf Domänen

### Übersicht

```
┌─────────────────────────────────────────────────────────────────┐
│              GERÄTE UND DOMÄNENTRENNUNG                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Gerät              │ Kollisions-D. │ Broadcast-D. │ OSI-Layer │
│  ───────────────────┼───────────────┼──────────────┼───────────│
│  Repeater/Hub       │ Verbindet     │ Verbindet    │ Layer 1   │
│  Bridge             │ TRENNT        │ Verbindet    │ Layer 2   │
│  Switch             │ TRENNT        │ Verbindet    │ Layer 2   │
│  Router             │ TRENNT        │ TRENNT       │ Layer 3   │
│  Layer-3-Switch     │ TRENNT        │ TRENNT*      │ Layer 3   │
│                                                                 │
│  * Bei Routing zwischen VLANs                                  │
│                                                                 │
│  Merksatz:                                                      │
│  ─────────                                                      │
│  "Router trennen BEIDE Domänen"                                │
│  "Switches trennen NUR Kollisionsdomänen"                      │
│  "Hubs trennen NICHTS"                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Detailbetrachtung: Switch

```
┌─────────────────────────────────────────────────────────────────┐
│                    SWITCH – MIKROSEGMENTIERUNG                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Ein Switch mit 24 Ports erzeugt:                              │
│  • 24 Kollisionsdomänen (eine pro Port)                        │
│  • 1 Broadcast-Domäne (alle Ports)                             │
│                                                                 │
│                    ┌─────────────────────────────────┐         │
│                    │           SWITCH                │         │
│                    │  ┌─────────────────────────┐   │         │
│                    │  │    MAC-Adresstabelle    │   │         │
│                    │  │   Port │ MAC-Adresse    │   │         │
│                    │  │   ─────┼──────────────  │   │         │
│                    │  │    1   │ AA:AA:...:01   │   │         │
│                    │  │    2   │ AA:AA:...:02   │   │         │
│                    │  │   ...  │ ...            │   │         │
│                    │  └─────────────────────────┘   │         │
│                    └──┬────┬────┬────┬────┬────┬────┘         │
│                       │    │    │    │    │    │              │
│  Kollisionsdomänen:  KD1  KD2  KD3  KD4  KD5  KD6  ...       │
│                       │    │    │    │    │    │              │
│                      PC1  PC2  PC3  PC4  PC5  PC6             │
│                                                                 │
│  Unicast: Switch leitet gezielt an den richtigen Port          │
│  Broadcast: Switch flutet an ALLE Ports (außer Quell-Port)    │
│                                                                 │
│  → Keine Kollisionen bei Unicast (Full-Duplex)                │
│  → Aber: Broadcast erreicht alle Geräte                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Detailbetrachtung: Router

```
┌─────────────────────────────────────────────────────────────────┐
│                    ROUTER – BROADCAST-GRENZE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Ein Router mit 3 Interfaces erzeugt:                          │
│  • 3 Kollisionsdomänen (eine pro Interface)                    │
│  • 3 Broadcast-Domänen (eine pro Interface/Subnetz)            │
│                                                                 │
│                       ┌────────────┐                           │
│                       │   ROUTER   │                           │
│                       │            │                           │
│                       │ eth0  eth1 │ eth2                      │
│                       └──┬─────┬───┘──┬                        │
│                          │     │      │                        │
│        ┌─────────────────┘     │      └─────────────────┐     │
│        │                       │                        │     │
│        ▼                       ▼                        ▼     │
│   ┌─────────┐            ┌─────────┐            ┌─────────┐   │
│   │ Switch  │            │ Switch  │            │ Switch  │   │
│   └────┬────┘            └────┬────┘            └────┬────┘   │
│   ┌────┴────┐            ┌────┴────┐            ┌────┴────┐   │
│   │    │    │            │    │    │            │    │    │   │
│  PC1  PC2  PC3          PC4  PC5  PC6          PC7  PC8  PC9  │
│                                                                 │
│  Subnetz A              Subnetz B              Subnetz C       │
│  192.168.1.0/24         192.168.2.0/24         192.168.3.0/24 │
│                                                                 │
│  Broadcast-Domäne 1     Broadcast-Domäne 2     Broadcast-D. 3 │
│                                                                 │
│  Broadcast von PC1:                                            │
│  → Erreicht PC2, PC3 (gleiches Subnetz)                       │
│  → Erreicht NICHT PC4-PC9 (Router blockiert!)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Überlappung und Zusammenhang

### Wann sind beide Domänen identisch?

```
┌─────────────────────────────────────────────────────────────────┐
│                    ÜBERLAPPUNG DER DOMÄNEN                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FALL 1: Shared Medium (Hub/Koaxial)                           │
│  ─────────────────────────────────────                         │
│                                                                 │
│       ══════════════════════════════                           │
│          │         │         │                                  │
│        ┌─┴─┐     ┌─┴─┐     ┌─┴─┐                              │
│        │PC1│     │PC2│     │PC3│                              │
│        └───┘     └───┘     └───┘                              │
│                                                                 │
│        Kollisionsdomäne = Broadcast-Domäne                     │
│        (identisch, da keine Trennung)                          │
│                                                                 │
│  ═══════════════════════════════════════════════════════════   │
│                                                                 │
│  FALL 2: Switched Network (ohne Router)                        │
│  ──────────────────────────────────────                        │
│                                                                 │
│                    ┌────────┐                                  │
│                    │ SWITCH │                                  │
│                    └───┬────┘                                  │
│           ┌────────┬───┴───┬────────┐                          │
│        ┌──┴──┐  ┌──┴──┐ ┌──┴──┐  ┌──┴──┐                      │
│        │ PC1 │  │ PC2 │ │ PC3 │  │ PC4 │                      │
│        └─────┘  └─────┘ └─────┘  └─────┘                      │
│                                                                 │
│        4 Kollisionsdomänen ⊂ 1 Broadcast-Domäne               │
│        (Kollisionsdomänen sind Teilmengen)                     │
│                                                                 │
│  ═══════════════════════════════════════════════════════════   │
│                                                                 │
│  FALL 3: Routed Network                                        │
│  ──────────────────────                                        │
│                                                                 │
│        ┌────────┐           ┌────────┐                        │
│        │Switch A│           │Switch B│                        │
│        └───┬────┘           └───┬────┘                        │
│       ┌────┴────┐          ┌────┴────┐                        │
│    ┌──┴──┐  ┌──┴──┐    ┌──┴──┐  ┌──┴──┐                      │
│    │ PC1 │  │ PC2 │    │ PC3 │  │ PC4 │                      │
│    └─────┘  └─────┘    └─────┘  └─────┘                      │
│       └────────┘  ┌────────┐  └────────┘                      │
│          BD1      │ ROUTER │     BD2                          │
│                   └────────┘                                   │
│                                                                 │
│        4 Kollisionsdomänen, 2 Broadcast-Domänen               │
│        (unabhängig voneinander)                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Mathematische Beziehung

```
┌─────────────────────────────────────────────────────────────────┐
│                    MENGENDARSTELLUNG                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Bei reinen Switches (ohne VLANs/Router):                      │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    Broadcast-Domäne                       │ │
│  │                                                           │ │
│  │   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐      │ │
│  │   │ KD1 │   │ KD2 │   │ KD3 │   │ KD4 │   │ KD5 │ ... │ │
│  │   └─────┘   └─────┘   └─────┘   └─────┘   └─────┘      │ │
│  │                                                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Kollisionsdomänen ⊆ Broadcast-Domäne                         │
│  (Kollisionsdomänen sind echte Teilmengen)                     │
│                                                                 │
│  Bei Routern:                                                   │
│                                                                 │
│  ┌─────────────────────┐      ┌─────────────────────┐         │
│  │   Broadcast-D. 1    │      │   Broadcast-D. 2    │         │
│  │                     │      │                     │         │
│  │  ┌────┐   ┌────┐   │      │  ┌────┐   ┌────┐   │         │
│  │  │KD1 │   │KD2 │   │      │  │KD3 │   │KD4 │   │         │
│  │  └────┘   └────┘   │      │  └────┘   └────┘   │         │
│  │                     │      │                     │         │
│  └─────────────────────┘      └─────────────────────┘         │
│                                                                 │
│  BD1 ∩ BD2 = ∅  (Broadcast-Domänen sind disjunkt)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Praktische Auswirkungen

### Probleme großer Domänen

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROBLEME UND LÖSUNGEN                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GROSSE KOLLISIONSDOMÄNE (z.B. Hub-Netzwerk):                  │
│  ─────────────────────────────────────────────                 │
│  Probleme:                                                      │
│  • Häufige Kollisionen                                         │
│  • Geringe effektive Bandbreite                                │
│  • Wartezeiten (Backoff)                                       │
│  • Maximale Ausdehnung begrenzt                                │
│                                                                 │
│  Lösung: → Switches einsetzen (Mikrosegmentierung)            │
│                                                                 │
│  ───────────────────────────────────────────────────────────   │
│                                                                 │
│  GROSSE BROADCAST-DOMÄNE (z.B. flaches L2-Netzwerk):          │
│  ─────────────────────────────────────────────────             │
│  Probleme:                                                      │
│  • Broadcast-Stürme möglich                                    │
│  • Jedes Gerät verarbeitet jeden Broadcast                     │
│  • ARP-Tabellen werden groß                                    │
│  • Sicherheitsrisiko (alle sehen Broadcasts)                   │
│  • Skalierungsprobleme (>500 Hosts problematisch)             │
│                                                                 │
│  Lösungen:                                                      │
│  → Router einsetzen (L3-Segmentierung)                        │
│  → VLANs konfigurieren (virtuelle Trennung)                   │
│  → Layer-3-Switches mit Inter-VLAN-Routing                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Empfehlungen für das Netzwerkdesign

| Größe | Kollisionsdomänen | Broadcast-Domänen | Empfehlung |
|-------|-------------------|-------------------|------------|
| Klein (<50 Hosts) | Via Switch segmentiert | 1 reicht oft | Flaches L2-Netz OK |
| Mittel (50-200) | Via Switch segmentiert | 1-5 VLANs | VLANs empfohlen |
| Groß (>200 Hosts) | Via Switch segmentiert | Viele VLANs/Subnetze | L3-Design Pflicht |

## VLANs und Broadcast-Domänen

```
┌─────────────────────────────────────────────────────────────────┐
│              VLAN – VIRTUELLE BROADCAST-DOMÄNEN                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  VLANs teilen einen Switch in mehrere logische Switches:       │
│                                                                 │
│                    ┌─────────────────────────┐                 │
│                    │     SWITCH (physisch)   │                 │
│                    │  ┌───────┐  ┌───────┐  │                 │
│                    │  │VLAN 10│  │VLAN 20│  │                 │
│                    │  │ (rot) │  │(blau) │  │                 │
│                    │  └───┬───┘  └───┬───┘  │                 │
│                    └──────┼──────────┼──────┘                  │
│                     ┌─────┼────┐  ┌──┼─────┐                   │
│                     │     │    │  │  │     │                   │
│                   ┌─┴─┐ ┌─┴─┐┌─┴─┐┌─┴─┐ ┌─┴─┐                 │
│                   │PC1│ │PC2││PC3││PC4│ │PC5│                 │
│                   └───┘ └───┘└───┘└───┘ └───┘                 │
│                   VLAN10 VLAN10 VLAN20 VLAN20 VLAN20          │
│                                                                 │
│  Broadcast-Domäne 1:  PC1, PC2 (VLAN 10)                      │
│  Broadcast-Domäne 2:  PC3, PC4, PC5 (VLAN 20)                 │
│                                                                 │
│  → Broadcast von PC1 erreicht NUR PC2                         │
│  → Kommunikation VLAN 10 ↔ VLAN 20 nur über Router/L3-Switch │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> 
> **Kollisionsdomäne:**
> - Layer 1 Konzept
> - Bereich, wo Signale kollidieren können
> - Getrennt durch: Switch, Bridge
> - Bei Full-Duplex/Switches: Pro Port eine Domäne
> 
> **Broadcast-Domäne:**
> - Layer 2/3 Konzept
> - Bereich, den ein Broadcast erreicht
> - Getrennt durch: Router, Layer-3-Switch, VLAN
> - Entspricht typischerweise einem IP-Subnetz
> 
> **Beziehung:**
> - Kollisionsdomänen ⊆ Broadcast-Domäne
> - Bei Hubs: Beide identisch
> - Bei Switches: Viele Kollisions-D., eine Broadcast-D.
> - Bei Routern: Beide getrennt

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Verstehen Sie den Unterschied zwischen beiden Domänen
> - Wissen Sie, welches Gerät was trennt
> - Können Sie die Anzahl der Domänen in einem Netzwerkdiagramm zählen
> - Kennen Sie die Probleme großer Broadcast-Domänen

### Typische Prüfungsaufgabe

> [!example] Beispiel
> **Frage:** Ein Netzwerk besteht aus 2 Switches, verbunden durch einen Router. An jedem Switch hängen 10 PCs. Wie viele Kollisions- und Broadcast-Domänen gibt es?
> 
> **Antwort:**
> - Kollisionsdomänen: 20 + 2 = 22 (10 pro Switch + je 1 für Router-Port)
> - Broadcast-Domänen: 2 (eine pro Switch/Subnetz, Router trennt)

## Verwandte Themen

- [[../05-Sicherungsschicht/03-MAC-Protokolle|CSMA/CD]] – Kollisionserkennung
- [[01-IP-Protokoll]] – Subnetting und Broadcast-Adressen
- [[02-Routing]] – Router als Broadcast-Grenze
- [[../05-Sicherungsschicht/01-Rahmenbildung|Ethernet-Frame]] – Broadcast-MAC-Adresse

## Quellen

- Tanenbaum, A. S.: Computernetzwerke, Kap. 4
- Kurose, J., Ross, K.: Computernetze, Kap. 6
