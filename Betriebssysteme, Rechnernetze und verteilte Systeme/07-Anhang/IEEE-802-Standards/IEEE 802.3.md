---
author: Andreas Hümmer
title: IEEE 802.3 - Ethernet
tags:
- ieee
- ethernet
- lan
- 802.3
created: '2026-10-07'
---
author: Andreas Hümmer

# IEEE 802.3 - Ethernet

## Kurzübersicht

**IEEE 802.3** definiert die Physical Layer und Data Link Layer (MAC) Spezifikationen für kabelgebundenes Ethernet. Erstmals 1983 veröffentlicht, unterstützt der Standard heute Datenraten von 10 Mbit/s bis 400 Gbit/s.

| Eigenschaft | Wert |
|-------------|------|
| Erste Veröffentlichung | 1983 |
| Arbeitsgruppe | IEEE 802.3 Working Group |
| Datenraten | 10 Mbit/s - 400 Gbit/s |
| Medien | Koaxial, Twisted Pair, Glasfaser |

## Wichtige Amendments

| Standard | Jahr | Name | Geschwindigkeit | Medium |
|----------|------|------|-----------------|--------|
| 802.3 | 1983 | 10BASE5 | 10 Mbit/s | Thick Coax |
| 802.3a | 1985 | 10BASE2 | 10 Mbit/s | Thin Coax |
| 802.3i | 1990 | 10BASE-T | 10 Mbit/s | Twisted Pair |
| 802.3u | 1995 | 100BASE-TX | 100 Mbit/s | Cat5 |
| 802.3ab | 1999 | 1000BASE-T | 1 Gbit/s | Cat5e/6 |
| 802.3ae | 2002 | 10GBASE | 10 Gbit/s | Fiber |
| 802.3ba | 2010 | 40G/100G | 40/100 Gbit/s | Fiber |
| 802.3bs | 2017 | 200G/400G | 200/400 Gbit/s | Fiber |

## Ethernet-Frame-Format

```
┌─────────┬─────────┬─────────┬──────────┬─────────┬─────┐
│Preamble │  Dest   │ Source  │Type/Len  │  Data   │ FCS │
│  8 Byte │MAC 6 B  │MAC 6 B  │  2 Byte  │46-1500 B│4 B  │
└─────────┴─────────┴─────────┴──────────┴─────────┴─────┘
```

## Offizielle Quelle

> [!tip] IEEE-Referenz
> **IEEE 802.3-2022**: IEEE Standard for Ethernet
> - URL: https://standards.ieee.org/ieee/802.3/10422/
> - Working Group: https://www.ieee802.org/3/

---
author: Andreas Hümmer

*Quelle: IEEE Standards Association*
