---
author: Andreas Hümmer
title: IEEE 802.1Q - Virtual LANs (VLANs)
tags:
  - ieee
  - vlan
  - switching
  - 802.1Q
created: '2026-10-07'
---

# IEEE 802.1Q - Virtual LANs (VLANs)

## Kurzübersicht

**IEEE 802.1Q** definiert das Tagging-Verfahren für Virtual LANs (VLANs) in Ethernet-Netzwerken. Der Standard ermöglicht die logische Segmentierung von Netzwerken auf Layer 2.

| Eigenschaft | Wert |
|-------------|------|
| Erste Veröffentlichung | 1998 |
| Aktuelle Version | IEEE 802.1Q-2022 |
| VLAN-IDs | 0-4095 (4094 nutzbar) |
| Tag-Größe | 4 Byte |

## VLAN-Tag-Format

```
┌───────────────────────────────────────────────────────┐
│                   802.1Q VLAN Tag (4 Byte)            │
├─────────────────┬─────┬───────────────────────────────┤
│   TPID (16 Bit) │ PCP │ DEI │      VID (12 Bit)       │
│     0x8100      │ 3b  │ 1b  │        0-4095           │
└─────────────────┴─────┴─────┴─────────────────────────┘
```

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **TPID** | 16 | Tag Protocol Identifier (0x8100) |
| **PCP** | 3 | Priority Code Point (QoS) |
| **DEI** | 1 | Drop Eligible Indicator |
| **VID** | 12 | VLAN Identifier (0-4095) |

## Frame-Größe

- Standard Ethernet: max. 1518 Byte
- Mit 802.1Q-Tag: max. 1522 Byte
- Minimale Frame-Größe: 64 Byte (Bridge kann auf 68 erweitern)

## Reservierte VLANs

| VLAN-ID | Verwendung |
|---------|------------|
| 0 | Priority Tag only (kein VLAN) |
| 1 | Default VLAN |
| 4095 | Reserviert |

## Offizielle Quelle

> [!tip] IEEE-Referenz
> **IEEE 802.1Q-2022**: Bridges and Bridged Networks
> - URL: https://standards.ieee.org/ieee/802.1Q/10323/
> - Working Group: https://www.ieee802.org/1/

---

*Quelle: IEEE Standards Association*
