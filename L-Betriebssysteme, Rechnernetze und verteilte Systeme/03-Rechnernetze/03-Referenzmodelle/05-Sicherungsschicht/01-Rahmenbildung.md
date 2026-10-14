---
author: Andreas Hümmer
title: Rahmenbildung und Ethernet-Frame
tags:
  - vorlesung
  - rn
  - layer2
  - ethernet
  - frame
  - mac
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Rahmenbildung und Ethernet-Frame

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Aufbau eines Ethernet-Frames erklären
> - MAC-Adressen lesen und interpretieren
> - Den Unterschied zwischen Ethernet II und 802.3 erklären
> - VLAN-Tagging (802.1Q) verstehen
> - Die Bedeutung von MTU und Jumbo Frames erläutern

## Ethernet-Frame-Formate

### Ethernet II (DIX) vs. IEEE 802.3

```
┌─────────────────────────────────────────────────────────────────┐
│                    ETHERNET-FRAME-FORMATE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ETHERNET II (DIX) – heute Standard                           │
│   ──────────────────────────────────────────────────────────   │
│   │Präambel│SFD│ Dst MAC │ Src MAC │Type │  Payload  │ FCS │   │
│   │  7 B   │1B │   6 B   │   6 B   │ 2B  │ 46-1500 B │ 4B  │   │
│   └────────┴───┴─────────┴─────────┴─────┴───────────┴─────┘   │
│                                                                 │
│   IEEE 802.3 (mit LLC)                                          │
│   ──────────────────────────────────────────────────────────   │
│   │Präambel│SFD│ Dst MAC │ Src MAC │Len │LLC│  Payload │FCS │  │
│   │  7 B   │1B │   6 B   │   6 B   │ 2B │3B │ 43-1497B │4B  │  │
│   └────────┴───┴─────────┴─────────┴────┴───┴──────────┴────┘  │
│                                                                 │
│   Unterscheidung: Type/Length Feld                              │
│   • Wert ≤ 1500 (0x05DC) → Length (IEEE 802.3)                 │
│   • Wert ≥ 1536 (0x0600) → EtherType (Ethernet II)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Ethernet-Frame im Detail

```
┌─────────────────────────────────────────────────────────────────┐
│                ETHERNET II FRAME AUFBAU                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   PRÄAMBEL (7 Bytes)                                           │
│   • Bitfolge: 10101010 10101010 10101010 ... (7×)              │
│   • Zweck: Taktsynchronisation des Empfängers                  │
│                                                                 │
│   SFD – Start Frame Delimiter (1 Byte)                         │
│   • Bitfolge: 10101011                                         │
│   • Markiert Beginn des eigentlichen Frames                    │
│                                                                 │
│   DESTINATION MAC (6 Bytes)                                     │
│   • MAC-Adresse des Empfängers                                 │
│   • Kann Unicast, Multicast oder Broadcast sein                │
│                                                                 │
│   SOURCE MAC (6 Bytes)                                          │
│   • MAC-Adresse des Senders                                    │
│   • Immer Unicast                                              │
│                                                                 │
│   ETHERTYPE (2 Bytes)                                           │
│   • Identifiziert Protokoll der Nutzlast                       │
│   • 0x0800 = IPv4                                              │
│   • 0x0806 = ARP                                               │
│   • 0x86DD = IPv6                                              │
│   • 0x8100 = 802.1Q VLAN Tag                                   │
│                                                                 │
│   PAYLOAD (46-1500 Bytes)                                       │
│   • Nutzdaten (z.B. IP-Paket)                                  │
│   • Minimum 46 Bytes (sonst Padding)                           │
│   • Maximum 1500 Bytes (MTU)                                   │
│                                                                 │
│   FCS – Frame Check Sequence (4 Bytes)                         │
│   • CRC-32 Prüfsumme                                           │
│   • Berechnet über Dst MAC bis Payload                         │
│                                                                 │
│   Gesamtgröße: 64 - 1518 Bytes (ohne Präambel/SFD)            │
│   Mit Präambel/SFD: 72 - 1526 Bytes                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Wichtige EtherTypes

| EtherType | Protokoll |
|-----------|-----------|
| 0x0800 | IPv4 |
| 0x0806 | ARP |
| 0x8035 | RARP |
| 0x8100 | 802.1Q VLAN Tag |
| 0x86DD | IPv6 |
| 0x8847 | MPLS Unicast |
| 0x8848 | MPLS Multicast |
| 0x88A8 | 802.1ad (QinQ) |
| 0x88CC | LLDP |

## MAC-Adressen

### Aufbau

```
┌─────────────────────────────────────────────────────────────────┐
│                    MAC-ADRESSE (48 Bit)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Beispiel: AA:BB:CC:DD:EE:FF                                  │
│             ─────────  ─────────                                │
│               OUI       NIC                                     │
│                                                                 │
│   ┌─────────────────────┬─────────────────────┐                │
│   │    OUI (24 Bit)     │    NIC (24 Bit)     │                │
│   │  Hersteller-ID      │  Geräte-ID          │                │
│   │  (von IEEE vergeben)│  (vom Hersteller)   │                │
│   └─────────────────────┴─────────────────────┘                │
│                                                                 │
│   Bit 0 des ersten Bytes (I/G-Bit):                            │
│   • 0 = Unicast (Einzeladresse)                                │
│   • 1 = Multicast/Broadcast (Gruppenadresse)                   │
│                                                                 │
│   Bit 1 des ersten Bytes (U/L-Bit):                            │
│   • 0 = Universally Administered (OUI von IEEE)                │
│   • 1 = Locally Administered (lokal zugewiesen)                │
│                                                                 │
│   Erstes Byte: XX:__:__:__:__:__                               │
│                                                                 │
│   Bit 7 6 5 4 3 2 1 0                                          │
│                   │ └─ I/G: 0=Unicast, 1=Multicast             │
│                   └─── U/L: 0=Universal, 1=Local               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Spezielle MAC-Adressen

| Adresse | Bedeutung |
|---------|-----------|
| FF:FF:FF:FF:FF:FF | Broadcast (an alle) |
| 01:00:5E:xx:xx:xx | IPv4 Multicast |
| 33:33:xx:xx:xx:xx | IPv6 Multicast |
| 01:80:C2:00:00:00 | STP (Spanning Tree) |
| 01:80:C2:00:00:0E | LLDP |

### OUI-Beispiele (Hersteller)

| OUI | Hersteller |
|-----|------------|
| 00:00:0C | Cisco |
| 00:1A:A0 | Dell |
| 3C:D9:2B | HP |
| FC:AA:14 | Giga-Byte |
| 00:50:56 | VMware |
| 08:00:27 | VirtualBox |

## VLAN-Tagging (IEEE 802.1Q)

```
┌─────────────────────────────────────────────────────────────────┐
│                    802.1Q VLAN TAG                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Frame ohne Tag:                                               │
│   │ Dst MAC │ Src MAC │ Type │   Payload   │ FCS │             │
│   │   6 B   │   6 B   │  2B  │  46-1500 B  │ 4B  │             │
│                                                                 │
│   Frame mit 802.1Q Tag:                                         │
│   │ Dst MAC │ Src MAC │ 802.1Q │ Type │  Payload  │ FCS │      │
│   │   6 B   │   6 B   │   4B   │  2B  │ 46-1500 B │ 4B  │      │
│                                                                 │
│   802.1Q Tag (4 Bytes):                                         │
│   ┌─────────────┬─────┬─────┬────────────────┐                 │
│   │    TPID     │ PCP │ DEI │      VID       │                 │
│   │   0x8100    │ 3b  │ 1b  │    12 Bit      │                 │
│   │  (2 Bytes)  │     │     │   (0-4095)     │                 │
│   └─────────────┴─────┴─────┴────────────────┘                 │
│                                                                 │
│   TPID = Tag Protocol Identifier (0x8100)                      │
│   PCP  = Priority Code Point (0-7, für QoS)                    │
│   DEI  = Drop Eligible Indicator                               │
│   VID  = VLAN Identifier (1-4094 nutzbar)                      │
│                                                                 │
│   Reservierte VLANs:                                            │
│   • VID 0: Priority Tagged (nur QoS, kein VLAN)                │
│   • VID 1: Default VLAN                                        │
│   • VID 4095: Reserviert                                       │
│                                                                 │
│   Max. Frame-Größe mit Tag: 1522 Bytes (statt 1518)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## MTU und Jumbo Frames

| Begriff | Größe | Beschreibung |
|---------|-------|--------------|
| **MTU** | 1500 Bytes | Standard Maximum Transmission Unit |
| **Jumbo Frame** | 9000 Bytes | Für Rechenzentren, reduziert Overhead |
| **Baby Giant** | 1504-1600 Bytes | Leicht vergrößert (für Tags) |

> [!warning] Jumbo Frames
> Jumbo Frames müssen auf **allen** Geräten im Pfad konfiguriert sein. Unterschiedliche MTU-Größen führen zu Fragmentierung oder Paketverlust.

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Ethernet II ist das heute übliche Frame-Format
> - **MAC-Adressen** sind 48 Bit lang (OUI + NIC)
> - **Broadcast**: FF:FF:FF:FF:FF:FF
> - **EtherType** identifiziert das Nutzlast-Protokoll (0x0800 = IPv4)
> - **802.1Q** fügt 4 Bytes VLAN-Tag hinzu
> - **FCS** enthält CRC-32 zur Fehlererkennung
> - Standard-MTU: **1500 Bytes**

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Felder eines Ethernet-Frames
> - Verstehen Sie MAC-Adressen (48 Bit, OUI + NIC)
> - Wissen Sie, was Broadcast und Multicast bedeuten
> - Können Sie 802.1Q VLAN-Tagging erklären

## Verwandte Themen

- [[02-Fehlererkennung]] – CRC und FCS
- [[03-MAC-Protokolle]] – Medienzugriffssteuerung
- [[../06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]] – Die Nutzlast des Frames

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- [[07-Anhang/IEEE-802-Standards/IEEE 802.3|IEEE 802.3]] – Ethernet-Standard
