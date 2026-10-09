---
title: "RFC 7432 - BGP MPLS-Based Ethernet VPN"
rfc_number: 7432
version: "February 2015"
status: Proposed Standard
author: "A. Sajassi, R. Aggarwal, N. Bitar, A. Isaac, J. Uttaro, J. Drake, W. Henderickx"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - bgp
  - evpn
  - mpls
  - datacenter
---

# RFC 7432 - BGP EVPN

## Überblick

RFC 7432 definiert Ethernet VPN (EVPN), ein BGP-basiertes Layer-2-VPN-Verfahren für moderne Datacenter-Netzwerke.

## Zusammenfassung

EVPN-Eigenschaften:

- **BGP Control Plane**: MAC-Lernen via BGP
- **Active-Active**: Multi-Homing ohne STP
- **MAC Mobility**: Schnelle VM-Migration
- **Integrated Routing**: L2 und L3 kombiniert

## EVPN Route Types

| Typ | Beschreibung |
|-----|--------------|
| 1 | Ethernet Auto-Discovery |
| 2 | MAC/IP Advertisement |
| 3 | Inclusive Multicast Ethernet Tag |
| 4 | Ethernet Segment |
| 5 | IP Prefix Advertisement |

## Vorteile gegenüber VPLS

| VPLS | EVPN |
|------|------|
| Flood & Learn | BGP-basiertes Lernen |
| Active-Standby | Active-Active |
| Kein ARP Suppression | ARP Proxy möglich |
| Skalierungsprobleme | Bessere Skalierung |

## Offizielles Dokument

**RFC 7432**: [https://www.rfc-editor.org/rfc/rfc7432](https://www.rfc-editor.org/rfc/rfc7432)

## Verwandte RFCs

- [[RFC 8365 EVPN Overlay]] - EVPN als Overlay
- [[RFC 7348 VXLAN]] - VXLAN-Encapsulation
- [[RFC 8200 IPv6]] - IPv6-Unterstützung
