---
author: Andreas Hümmer
title: IEEE 802.1D - Spanning Tree Protocol (STP)
tags:
  - ieee
  - stp
  - switching
  - 802.1D
created: '2026-10-07'
---

# IEEE 802.1D - Spanning Tree Protocol (STP)

## Kurzübersicht

**IEEE 802.1D** definiert das **Spanning Tree Protocol (STP)**, das Schleifen in Ethernet-Netzwerken verhindert, indem es eine schleifenfreie Baumtopologie erstellt. Der ursprüngliche Standard wurde in 802.1Q integriert.

| Eigenschaft | Wert |
|-------------|------|
| Erste Veröffentlichung | 1990 |
| Erfinder | Radia Perlman (1985) |
| Konvergenzzeit | 30-50 Sekunden |
| Status | In 802.1Q integriert |

## Funktionsweise

STP wählt eine **Root Bridge** und blockiert redundante Pfade, um Broadcast-Stürme zu verhindern:

```
        [Root Bridge]
           /    \
          /      \
    [Bridge A]  [Bridge B]
         \        /
          \      /    ← Ein Link wird BLOCKIERT
         [Bridge C]
```

## Port-Zustände

| Zustand | Dauer | Datenverkehr | Lernt MACs |
|---------|-------|--------------|------------|
| **Blocking** | - | ❌ | ❌ |
| **Listening** | 15 s | ❌ | ❌ |
| **Learning** | 15 s | ❌ | ✓ |
| **Forwarding** | - | ✓ | ✓ |
| **Disabled** | - | ❌ | ❌ |

## Timer

| Timer | Standardwert | Beschreibung |
|-------|--------------|--------------|
| Hello Time | 2 s | BPDU-Intervall |
| Forward Delay | 15 s | Listening/Learning-Dauer |
| Max Age | 20 s | BPDU-Timeout |

## Weiterentwicklungen

| Standard | Name | Verbesserung |
|----------|------|--------------|
| 802.1w | RSTP | Schnelle Konvergenz (<1 s) |
| 802.1s | MSTP | Multiple Spanning Trees |

## Offizielle Quelle

> [!tip] IEEE-Referenz
> Der ursprüngliche 802.1D wurde in **IEEE 802.1Q** integriert.
> - URL: https://standards.ieee.org/ieee/802.1Q/10323/
> - Working Group: https://www.ieee802.org/1/

---

*Quelle: IEEE Standards Association*
