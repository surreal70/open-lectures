---
author: Andreas Hümmer
title: IEEE 802.1w - Rapid Spanning Tree Protocol (RSTP)
tags:
- ieee
- rstp
- stp
- switching
- 802.1w
created: '2026-10-07'
---
author: Andreas Hümmer

# IEEE 802.1w - Rapid Spanning Tree Protocol (RSTP)

## Kurzübersicht

**IEEE 802.1w** definiert das **Rapid Spanning Tree Protocol (RSTP)**, eine Weiterentwicklung von STP mit deutlich schnellerer Konvergenz. RSTP wurde in 802.1D-2004 integriert.

| Eigenschaft | Wert |
|-------------|------|
| Veröffentlichung | 2001 |
| Konvergenzzeit | < 1 Sekunde |
| Rückwärtskompatibel | Ja (zu STP) |
| Status | In 802.1Q integriert |

## Verbesserungen gegenüber STP

| Aspekt | STP (802.1D) | RSTP (802.1w) |
|--------|--------------|---------------|
| Konvergenz | 30-50 s | < 1 s |
| Port-Zustände | 5 | 3 |
| Edge Ports | Nein | Ja (PortFast) |
| Proposal/Agreement | Nein | Ja |

## Port-Zustände (vereinfacht)

| RSTP-Zustand | STP-Entsprechung |
|--------------|------------------|
| **Discarding** | Blocking, Listening, Disabled |
| **Learning** | Learning |
| **Forwarding** | Forwarding |

## Port-Rollen

| Rolle | Beschreibung |
|-------|--------------|
| **Root Port** | Bester Pfad zur Root Bridge |
| **Designated Port** | Bester Pfad vom Segment zur Root |
| **Alternate Port** | Backup für Root Port |
| **Backup Port** | Backup für Designated Port |
| **Edge Port** | Direkt zu Endgeräten (kein BPDU) |

## Offizielle Quelle

> [!tip] IEEE-Referenz
> RSTP wurde in **IEEE 802.1D-2004** und später in **IEEE 802.1Q** integriert.
> - URL: https://standards.ieee.org/ieee/802.1Q/10323/
> - Working Group: https://www.ieee802.org/1/

---
author: Andreas Hümmer

*Quelle: IEEE Standards Association*
