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

## Padding (Auffüllung)

### Warum Padding?

Ethernet erfordert eine **Mindestframegröße von 64 Bytes** (ohne Präambel/SFD). Dies hat technische Gründe:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PADDING BEI ETHERNET                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PROBLEM: Kollisionserkennung (CSMA/CD)                        │
│  ─────────────────────────────────────────────────────────────  │
│  Bei Ethernet muss der Sender während der gesamten Übertragung │
│  eine mögliche Kollision erkennen können. Das Frame muss       │
│  mindestens so lange sein, dass es die maximale Netzausdehnung │
│  (2× Laufzeit = Round-Trip-Time) überbrückt.                   │
│                                                                 │
│  Slot Time bei 10 Mbps:     51,2 µs = 512 Bit = 64 Bytes      │
│  Maximale Kabellänge:       2500 m (mit Repeatern)             │
│                                                                 │
│  BERECHNUNG der Mindestgröße:                                   │
│  ─────────────────────────────────────────────────────────────  │
│  Min. Frame = Dst MAC + Src MAC + Type + Payload + FCS         │
│             = 6 + 6 + 2 + Payload + 4 = 64 Bytes               │
│                                                                 │
│  → Payload muss mindestens 46 Bytes sein!                      │
│                                                                 │
│  Wenn Nutzdaten < 46 Bytes → Padding hinzufügen                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Wie funktioniert Padding?

```
┌─────────────────────────────────────────────────────────────────┐
│                    PADDING-BEISPIEL                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Beispiel: ARP-Paket (28 Bytes Nutzdaten)                      │
│                                                                 │
│  Ohne Padding (ungültig!):                                      │
│  │ Dst │ Src │ Type │ ARP-Paket │ FCS │                        │
│  │ 6 B │ 6 B │  2 B │   28 B    │ 4 B │ = 46 Bytes < 64!      │
│                                                                 │
│  Mit Padding (gültig):                                          │
│  │ Dst │ Src │ Type │ ARP-Paket │ Padding │ FCS │              │
│  │ 6 B │ 6 B │  2 B │   28 B    │  18 B   │ 4 B │ = 64 Bytes ✓│
│                                                                 │
│  Das Padding besteht aus Null-Bytes (0x00):                    │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │    │
│  └────────────────────────────────────────────────────────┘    │
│                        18 Bytes                                 │
│                                                                 │
│  WICHTIG:                                                       │
│  • Padding wird vom Sender hinzugefügt                         │
│  • Padding wird nicht als separates Feld im Header markiert    │
│  • Der Empfänger muss das echte Payload-Ende anhand des        │
│    übergeordneten Protokolls (z.B. IP Total Length) erkennen   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

> [!info] Padding bei Gigabit-Ethernet
> Bei Gigabit-Ethernet (1000 Mbps) wäre die Slot Time nur 0,512 µs – viel zu kurz für vernünftige Kabellängen. Daher wird **Carrier Extension** verwendet: Der Frame wird auf mindestens 512 Bytes erweitert (nicht die Nutzdaten, sondern spezielle Extension-Symbole nach dem FCS).

## MTU und Jumbo Frames

| Begriff | Größe | Beschreibung |
|---------|-------|--------------|
| **MTU** | 1500 Bytes | Standard Maximum Transmission Unit |
| **Jumbo Frame** | 9000 Bytes | Für Rechenzentren, reduziert Overhead |
| **Baby Giant** | 1504-1600 Bytes | Leicht vergrößert (für Tags) |

> [!warning] Jumbo Frames
> Jumbo Frames müssen auf **allen** Geräten im Pfad konfiguriert sein. Unterschiedliche MTU-Größen führen zu Fragmentierung oder Paketverlust.

## Leitungskodierung vs. Kanalkodierung

### Begriffsunterscheidung

```
┌─────────────────────────────────────────────────────────────────┐
│           LEITUNGSKODIERUNG VS. KANALKODIERUNG                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                                                          │  │
│  │   Daten (Bits)                                          │  │
│  │        │                                                 │  │
│  │        ▼                                                 │  │
│  │   ┌────────────────────┐                                │  │
│  │   │  KANALKODIERUNG    │  ← Layer 2 (Data Link)        │  │
│  │   │  (Redundanz für    │     Fehlererkennung/-korrektur│  │
│  │   │   Fehlerschutz)    │     z.B. CRC, FEC, Hamming    │  │
│  │   └─────────┬──────────┘                                │  │
│  │             │                                            │  │
│  │             ▼                                            │  │
│  │   ┌────────────────────┐                                │  │
│  │   │  LEITUNGSKODIERUNG │  ← Layer 1 (Physical)         │  │
│  │   │  (Bitdarstellung   │     Signalform auf Medium      │  │
│  │   │   auf dem Medium)  │     z.B. Manchester, 4B/5B    │  │
│  │   └─────────┬──────────┘                                │  │
│  │             │                                            │  │
│  │             ▼                                            │  │
│  │      Physisches Signal                                   │  │
│  │   (Spannung, Licht, Funk)                               │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Leitungskodierung (Physical Layer – Layer 1)

**Zweck:** Umsetzung von Bits in physikalische Signale

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEITUNGSKODIERUNG                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Anforderungen:                                                 │
│  • Taktrückgewinnung (Synchronisation)                         │
│  • Gleichstromfreiheit (DC-Balance)                            │
│  • Geringe Bandbreite                                          │
│  • Fehlererkennung auf Symbolebene                             │
│                                                                 │
│  BEISPIEL: Manchester-Kodierung (10BASE-T)                     │
│  ─────────────────────────────────────────                     │
│  • Jedes Bit wird durch einen Pegelwechsel kodiert             │
│  • 0 = Wechsel von High nach Low (fallende Flanke)             │
│  • 1 = Wechsel von Low nach High (steigende Flanke)            │
│                                                                 │
│      Daten:    0       1       1       0       1               │
│                │       │       │       │       │               │
│           ┌────┘   ┌───┘   ┌───┘   ┌───┘   ┌───┘              │
│      ─────┤    ├───┤   ├───┤   ├───┤   ├───┤   ├───           │
│           └────    └───    └───    └───    └───                │
│                ↓       ↑       ↑       ↓       ↑               │
│               High→Low Low→High                                 │
│                                                                 │
│  Vorteil:  Takt ist im Signal enthalten                        │
│  Nachteil: Doppelte Bandbreite nötig (10 Mbps → 20 MHz)       │
│                                                                 │
│                                                                 │
│  BEISPIEL: 4B/5B + MLT-3 (100BASE-TX)                         │
│  ─────────────────────────────────────                         │
│  • 4 Datenbits werden auf 5 Symbole abgebildet                 │
│  • Garantiert maximal 3 aufeinanderfolgende gleiche Bits       │
│  • MLT-3: Drei Pegel (-V, 0, +V) für Signalübertragung        │
│                                                                 │
│  Effizienz: 4/5 = 80% (besser als Manchester mit 50%)         │
│                                                                 │
│                                                                 │
│  BEISPIEL: 8B/10B (1000BASE-X, Gigabit Ethernet)              │
│  ───────────────────────────────────────────────               │
│  • 8 Datenbits → 10 Symbole                                    │
│  • DC-Balance durch Running Disparity                          │
│  • Spezielle Kontrollsymbole (K-Codes) für Framing            │
│                                                                 │
│  Effizienz: 8/10 = 80%                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Kanalkodierung (Data Link Layer – Layer 2)

**Zweck:** Hinzufügen von Redundanz zur Fehlererkennung/-korrektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    KANALKODIERUNG                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Ziel: Schutz der Datenintegrität bei der Übertragung          │
│                                                                 │
│  FEHLERERKENNUNG (Detection):                                   │
│  ────────────────────────────                                   │
│  • Parität (einfach, erkennt 1-Bit-Fehler)                     │
│  • Prüfsummen (Checksums)                                      │
│  • CRC (Cyclic Redundancy Check) ← bei Ethernet!              │
│                                                                 │
│  Ethernet verwendet CRC-32:                                     │
│  • 32-Bit Prüfsumme im FCS-Feld                               │
│  • Erkennt alle 1-Bit, 2-Bit und ungerade Bitfehler           │
│  • Erkennt alle Burst-Fehler ≤ 32 Bit                         │
│  • Fehlerhafte Frames werden verworfen (kein ARQ bei Ethernet)│
│                                                                 │
│  FEHLERKORREKTUR (Correction) – FEC:                           │
│  ────────────────────────────────────                          │
│  • Hamming-Code (korrigiert 1-Bit-Fehler)                      │
│  • Reed-Solomon (Block-Codes, z.B. bei CDs, DVDs)              │
│  • Convolutional Codes (Faltungscodes, z.B. bei WLAN)         │
│  • LDPC (Low-Density Parity Check, z.B. bei 10GBASE-T)        │
│                                                                 │
│  Bei Ethernet:                                                  │
│  • Klassisches Ethernet: Nur Fehlererkennung (CRC)            │
│  • 10GBASE-T: FEC (LDPC) wegen schlechterer Kanalqualität     │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                                                          │  │
│  │  Daten (46-1500 Bytes)                                   │  │
│  │  ┌───────────────────────────────────────────────────┐  │  │
│  │  │ Nutzdaten                                          │  │  │
│  │  └───────────────────────────────────────────────────┘  │  │
│  │                          │                               │  │
│  │                          ▼ CRC-32 Berechnung            │  │
│  │  ┌───────────────────────────────────────────────┬────┐ │  │
│  │  │ Nutzdaten                                     │FCS │ │  │
│  │  └───────────────────────────────────────────────┴────┘ │  │
│  │                                                  4 Bytes │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Vergleich: Leitungs- vs. Kanalkodierung

| Aspekt | Leitungskodierung | Kanalkodierung |
|--------|-------------------|----------------|
| **Schicht** | Layer 1 (Physical) | Layer 2 (Data Link) |
| **Zweck** | Bitdarstellung auf Medium | Fehlerschutz |
| **Redundanz** | Für Synchronisation | Für Integrität |
| **Beispiele** | Manchester, 4B/5B, 8B/10B | CRC, Hamming, LDPC |
| **Bei Ethernet** | 4B/5B (100M), 8B/10B (1G) | CRC-32 (FCS) |

## Übergang Layer 1 ↔ Layer 2: Die Netzwerkkarte (NIC)

### Aufbau einer Netzwerkkarte

```
┌─────────────────────────────────────────────────────────────────┐
│               NETZWERKKARTE (NIC) – Layer 1 & 2                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────────────────────────────────────────────────┐│
│  │                       HOST (CPU)                           ││
│  │                          │                                 ││
│  │                     ┌────┴────┐                            ││
│  │                     │   Bus   │ (PCIe)                     ││
│  │                     └────┬────┘                            ││
│  └──────────────────────────┼─────────────────────────────────┘│
│                             │                                   │
│  ┌──────────────────────────┼─────────────────────────────────┐│
│  │                    NETZWERKKARTE                           ││
│  │                          │                                 ││
│  │  ┌───────────────────────┼───────────────────────────────┐ ││
│  │  │              MAC-Controller (Layer 2)                 │ ││
│  │  │                       │                               │ ││
│  │  │  ┌────────────────────┼──────────────────────────┐   │ ││
│  │  │  │  • Frame-Aufbau/-Abbau                        │   │ ││
│  │  │  │  • MAC-Adressfilterung                        │   │ ││
│  │  │  │  • FCS-Berechnung/-Prüfung (CRC-32)          │   │ ││
│  │  │  │  • CSMA/CD-Logik (Half-Duplex)               │   │ ││
│  │  │  │  • Flow Control (Pause Frames)               │   │ ││
│  │  │  │  • VLAN-Tagging                               │   │ ││
│  │  │  └────────────────────┼──────────────────────────┘   │ ││
│  │  │                       │                               │ ││
│  │  └───────────────────────┼───────────────────────────────┘ ││
│  │                          │                                 ││
│  │  ┌───────────────────────┼───────────────────────────────┐ ││
│  │  │               PHY-Chip (Layer 1)                      │ ││
│  │  │                       │                               │ ││
│  │  │  ┌────────────────────┼──────────────────────────┐   │ ││
│  │  │  │  • Leitungskodierung (4B/5B, 8B/10B, ...)     │   │ ││
│  │  │  │  • Scrambling/Descrambling                    │   │ ││
│  │  │  │  • Taktrückgewinnung (Clock Recovery)         │   │ ││
│  │  │  │  • Signalverstärkung                          │   │ ││
│  │  │  │  • Auto-Negotiation                           │   │ ││
│  │  │  │  • Link-Detection                             │   │ ││
│  │  │  └────────────────────┼──────────────────────────┘   │ ││
│  │  │                       │                               │ ││
│  │  └───────────────────────┼───────────────────────────────┘ ││
│  │                          │                                 ││
│  │                    ┌─────┴─────┐                           ││
│  │                    │Transformer│ (galvanische Trennung)    ││
│  │                    └─────┬─────┘                           ││
│  │                          │                                 ││
│  │                    ┌─────┴─────┐                           ││
│  │                    │ RJ45-Port │                           ││
│  │                    └───────────┘                           ││
│  │                                                            ││
│  └────────────────────────────────────────────────────────────┘│
│                             │                                   │
│                      ═══════╧═══════                           │
│                        Kabel (UTP)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Zusammenspiel MAC-Controller und PHY

```
┌─────────────────────────────────────────────────────────────────┐
│              MAC-PHY-SCHNITTSTELLE (MII/GMII/RGMII)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SENDEN (Host → Medium):                                       │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  1. Host übergibt Daten an MAC-Controller                      │
│       │                                                        │
│       ▼                                                        │
│  2. MAC-Controller:                                            │
│     • Baut Ethernet-Frame auf (Header + FCS)                  │
│     • Prüft ob Medium frei (CSMA/CD bei Half-Duplex)          │
│     • Wartet ggf. auf IFG (Inter-Frame Gap, 96 Bit-Zeiten)    │
│       │                                                        │
│       ▼                                                        │
│  3. MAC übergibt Frame bitweise an PHY                        │
│     (über MII: 4 Bit parallel @ 25 MHz bei 100 Mbps)          │
│       │                                                        │
│       ▼                                                        │
│  4. PHY-Chip:                                                  │
│     • Kodiert Bits (z.B. 4B/5B-Kodierung)                     │
│     • Wandelt in Signale um (MLT-3 Pegel)                     │
│     • Sendet über Transformer auf das Kabel                   │
│                                                                 │
│  EMPFANGEN (Medium → Host):                                    │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  1. PHY-Chip empfängt Signale vom Kabel                       │
│     • Taktrückgewinnung aus Präambel                          │
│     • Dekodierung (z.B. 5B/4B)                                │
│     • Übergabe an MAC                                          │
│       │                                                        │
│       ▼                                                        │
│  2. MAC-Controller:                                            │
│     • Erkennt SFD (Start Frame Delimiter)                     │
│     • Prüft Destination MAC (für mich? Broadcast? Multicast?) │
│     • Prüft FCS (CRC-32)                                      │
│     • Verwirft bei Fehler oder gibt an Host weiter            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### CSMA/CD im Detail (Übergang L1/L2)

```
┌─────────────────────────────────────────────────────────────────┐
│                CSMA/CD – LAYER 1 & 2 KOOPERATION                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CSMA/CD = Carrier Sense Multiple Access / Collision Detection │
│                                                                 │
│  ┌────────────────────────────────────────────────────────────┐│
│  │                                                            ││
│  │   LAYER 2 (MAC-Controller):          LAYER 1 (PHY):       ││
│  │                                                            ││
│  │   ┌─────────────────────┐           ┌──────────────────┐  ││
│  │   │ 1. Frame bereit     │           │                  │  ││
│  │   │    zum Senden       │           │                  │  ││
│  │   └──────────┬──────────┘           │                  │  ││
│  │              │                       │                  │  ││
│  │              ▼                       │                  │  ││
│  │   ┌─────────────────────┐           │                  │  ││
│  │   │ 2. Carrier Sense?   │◄──────────│ Signalpegel      │  ││
│  │   │    (Medium frei?)   │  Carrier  │ messen           │  ││
│  │   └──────────┬──────────┘  Detect   │                  │  ││
│  │          Ja  │  Nein                 │                  │  ││
│  │              │    └──► Warten        │                  │  ││
│  │              ▼                       │                  │  ││
│  │   ┌─────────────────────┐           │                  │  ││
│  │   │ 3. Senden starten   │──────────►│ Signal auf       │  ││
│  │   │    + weiter prüfen  │  Daten    │ Medium senden    │  ││
│  │   └──────────┬──────────┘           │                  │  ││
│  │              │                       │                  │  ││
│  │              ▼                       │                  │  ││
│  │   ┌─────────────────────┐           │                  │  ││
│  │   │ 4. Collision        │◄──────────│ Signalpegel      │  ││
│  │   │    Detection?       │ Collision │ zu hoch?         │  ││
│  │   └──────────┬──────────┘  Signal   │ (Überlagerung)   │  ││
│  │         Nein │  Ja                   │                  │  ││
│  │              │    │                  │                  │  ││
│  │              │    ▼                  │                  │  ││
│  │              │ ┌─────────────────┐   │                  │  ││
│  │              │ │ 5. JAM-Signal   │──►│ 32-Bit JAM      │  ││
│  │              │ │    senden       │   │ übertragen      │  ││
│  │              │ └────────┬────────┘   │                  │  ││
│  │              │          │            │                  │  ││
│  │              │          ▼            │                  │  ││
│  │              │ ┌─────────────────┐   │                  │  ││
│  │              │ │ 6. Backoff      │   │                  │  ││
│  │              │ │ (exponentiell)  │   │                  │  ││
│  │              │ └────────┬────────┘   │                  │  ││
│  │              │          │            │                  │  ││
│  │              │          └──► zurück zu 2.               │  ││
│  │              │                       │                  │  ││
│  │              ▼                       │                  │  ││
│  │   ┌─────────────────────┐           │                  │  ││
│  │   │ 7. Frame komplett   │           │                  │  ││
│  │   │    gesendet         │           │                  │  ││
│  │   └─────────────────────┘           └──────────────────┘  ││
│  │                                                            ││
│  └────────────────────────────────────────────────────────────┘│
│                                                                 │
│  Layer 1 (PHY) liefert:                                        │
│  • Carrier Sense Signal (CRS) – "Medium belegt"               │
│  • Collision Detect Signal (COL) – "Kollision erkannt"        │
│                                                                 │
│  Layer 2 (MAC) steuert:                                        │
│  • Entscheidung wann senden                                    │
│  • JAM-Signal bei Kollision                                    │
│  • Exponentieller Backoff-Algorithmus                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Exponentieller Backoff (Binary Exponential Backoff)

```
┌─────────────────────────────────────────────────────────────────┐
│              BACKOFF-ALGORITHMUS BEI KOLLISION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Nach Kollision Nr. n:                                         │
│                                                                 │
│  Wartezeit = zufällig(0 bis 2^n - 1) × Slot Time              │
│              ────────────────────────                          │
│                Slot Time = 51,2 µs (bei 10 Mbps)              │
│                                                                 │
│  ┌────────────┬─────────────────┬─────────────────────────┐    │
│  │ Kollision  │ Bereich k       │ Max. Wartezeit          │    │
│  ├────────────┼─────────────────┼─────────────────────────┤    │
│  │     1      │ 0 oder 1        │ 1 × 51,2 µs = 51,2 µs  │    │
│  │     2      │ 0 bis 3         │ 3 × 51,2 µs = 153,6 µs │    │
│  │     3      │ 0 bis 7         │ 7 × 51,2 µs = 358,4 µs │    │
│  │     4      │ 0 bis 15        │ 15 × 51,2 µs           │    │
│  │    ...     │ ...             │ ...                     │    │
│  │    10      │ 0 bis 1023      │ 1023 × 51,2 µs ≈ 52 ms │    │
│  │  11-15     │ 0 bis 1023      │ (gedeckelt)            │    │
│  │    16      │ ABBRUCH         │ Frame wird verworfen   │    │
│  └────────────┴─────────────────┴─────────────────────────┘    │
│                                                                 │
│  Nach 16 Kollisionen: Übertragung fehlgeschlagen!             │
│  → Frame wird an höhere Schicht mit Fehler gemeldet           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

> [!info] Full-Duplex und Switches
> Bei modernem Switched Ethernet im **Full-Duplex-Modus** ist CSMA/CD **deaktiviert**, da jeder Port eine dedizierte, kollisionsfreie Verbindung hat. Stattdessen wird **Flow Control** (Pause Frames nach IEEE 802.3x) verwendet.

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
