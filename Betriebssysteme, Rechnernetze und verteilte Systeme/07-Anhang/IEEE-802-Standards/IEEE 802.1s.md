---
author: Andreas Hümmer
title: IEEE 802.1s - Multiple Spanning Tree Protocol (MSTP)
tags:
  - ieee
  - mstp
  - stp
  - vlan
  - 802.1s
created: '2026-10-07'
---

# IEEE 802.1s - Multiple Spanning Tree Protocol (MSTP)

## Kurzübersicht

**IEEE 802.1s** definiert das **Multiple Spanning Tree Protocol (MSTP)**, das mehrere VLANs auf eine begrenzte Anzahl von Spanning-Tree-Instanzen abbildet. Dies ermöglicht Load Balancing über redundante Links.

| Eigenschaft | Wert |
|-------------|------|
| Veröffentlichung | 2002 |
| Basiert auf | RSTP (802.1w) |
| Max. Instanzen | 65 (typisch 16) |
| Status | In 802.1Q integriert |

## Konzept

```
VLAN 10, 20, 30 ──┐
                  ├──→ MST Instance 1 ──→ Root A
VLAN 40, 50    ───┘

VLAN 60, 70, 80 ──┐
                  ├──→ MST Instance 2 ──→ Root B
VLAN 90        ───┘
```

## Vorteile gegenüber PVST+

| Aspekt | PVST+ | MSTP |
|--------|-------|------|
| Instanzen | 1 pro VLAN | Konfigurierbar |
| CPU-Last | Hoch (viele VLANs) | Niedrig |
| Skalierbarkeit | Begrenzt | Gut |
| Load Balancing | Ja | Ja |

## MST-Region

Switches gehören zur selben MST-Region, wenn sie identische Konfiguration haben:
- **Configuration Name** (32 Zeichen)
- **Revision Number** (0-65535)
- **VLAN-to-Instance Mapping**

## Offizielle Quelle

> [!tip] IEEE-Referenz
> MSTP ist in **IEEE 802.1Q** integriert.
> - URL: https://standards.ieee.org/ieee/802.1Q/10323/
> - Working Group: https://www.ieee802.org/1/

---

*Quelle: IEEE Standards Association*
