---
author: Andreas Hümmer
title: MPLS - Multiprotocol Label Switching
tags:
  - content
  - rn
  - wan
  - mpls
  - carrier
  - label-switching
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# MPLS - Multiprotocol Label Switching

## Definition

**MPLS (Multiprotocol Label Switching)** ist eine Technologie zur effizienten Weiterleitung von Paketen in Provider-Netzwerken. Statt IP-basiertem Routing werden kurze Labels für schnelles Forwarding verwendet.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | Zwischen 2 und 3 ("Layer 2.5") |
| **Label-Größe** | 32 Bit (4 Bytes) |
| **Forwarding** | Label-basiert (nicht IP-basiert) |
| **Protokoll** | LDP (Label Distribution Protocol) |
| **Anwendung** | Provider-Backbones, VPNs |

## MPLS-Header (Shim Header)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                Label                  │ TC  │S│      TTL      │
│               (20 Bit)                │(3 B)│ │    (8 Bit)    │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Label: Forwarding-Entscheidung
TC:    Traffic Class (QoS)
S:     Bottom of Stack (1 = letztes Label)
TTL:   Time to Live
```

## Funktionsprinzip

```
┌─────────────────────────────────────────────────────────────────┐
│                    MPLS Label Switching                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Kunde A            MPLS-Backbone              Kunde B         │
│   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   │
│   │ CE  │───│ PE  │───│  P  │───│  P  │───│ PE  │───│ CE  │   │
│   │     │   │     │   │     │   │     │   │     │   │     │   │
│   └─────┘   └─────┘   └─────┘   └─────┘   └─────┘   └─────┘   │
│      │         │         │         │         │         │        │
│   [IP-Pkt]  [Label]   [Label]   [Label]   [Label]   [IP-Pkt]   │
│             Push       Swap      Swap      Pop                  │
│                                                                  │
│   CE = Customer Edge Router                                     │
│   PE = Provider Edge Router (Label Push/Pop)                   │
│   P  = Provider Router (Label Swap)                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Label-Operationen

<!-- TODO: Push, Pop, Swap erklären -->
<!-- TODO: PHP (Penultimate Hop Popping) -->

## MPLS VPN (L3VPN)

<!-- TODO: VRF (Virtual Routing and Forwarding) -->
<!-- TODO: Route Distinguisher, Route Target -->
<!-- TODO: MP-BGP für VPN-Routen -->

## Vor- und Nachteile

<!-- TODO: Vorteile: QoS, Traffic Engineering, Zuverlässigkeit -->
<!-- TODO: Nachteile: Kosten, Komplexität, Inflexibilität -->

## Prüfungsrelevante Themen

> [!tip] Prüfungshinweis
> - "Layer 2.5" – warum?
> - Label-Operationen (Push, Swap, Pop)
> - Unterschied CE/PE/P-Router
> - Warum wird MPLS durch SD-WAN ersetzt?

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[02-SD-WAN]] - Nachfolger/Ergänzung
- [[../03-Referenzmodelle/06-Netzwerkschicht/02-Routing|Routing]] - IP-Routing vs. Label-Switching

## Quellen

- [[A-RFC-Index#RFC 3031|RFC 3031]] - MPLS Architecture
- [[A-RFC-Index#RFC 3032|RFC 3032]] - MPLS Label Stack Encoding

