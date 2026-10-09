---
title: "RFC 7348 - Virtual eXtensible Local Area Network (VXLAN)"
rfc_number: 7348
version: "August 2014"
status: Informational
author: "M. Mahalingam, et al."
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - vxlan
  - overlay
  - sdn
---

# RFC 7348 - Virtual eXtensible LAN (VXLAN)

## Überblick

RFC 7348 definiert VXLAN (Virtual eXtensible Local Area Network), eine Netzwerkvirtualisierungstechnologie, die die Skalierungsprobleme von VLAN-basierten Netzwerken in hochvirtualisierten Rechenzentren adressiert.

## Zusammenfassung

VXLAN bietet ein Framework für das Überlagern virtualisierter Layer-2-Netzwerke über Layer-3-Infrastruktur:

- **24-Bit VXLAN Network Identifier (VNI)**: Unterstützt bis zu 16 Millionen logische Netzwerke (vs. 4.094 VLANs)
- **MAC-in-UDP-Kapselung**: Layer-2-Frames in UDP-Paketen gekapselt
- **VTEP (VXLAN Tunnel Endpoint)**: Kapselungs-/Entkapselungspunkte
- **Multicast oder Unicast**: BUM-Verkehrsbehandlung (Broadcast, Unknown unicast, Multicast)

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| VNI-Bereich | 1 bis 16.777.215 (24-Bit) |
| UDP-Port | 4789 (IANA-zugewiesen) |
| Overhead | 50 Bytes (Ethernet + IP + UDP + VXLAN) |
| Innerer Frame | Standard-Ethernet-Frame |

## VXLAN-Paketformat

```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   Outer Ethernet Header                       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   Outer IP Header                             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   Outer UDP Header (Dst Port 4789)            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   VXLAN Header (8 bytes, includes VNI)        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   Inner Ethernet Frame                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Offizielles Dokument

**RFC 7348**: [https://www.rfc-editor.org/rfc/rfc7348](https://www.rfc-editor.org/rfc/rfc7348)

## Verwandte RFCs

- [[RFC 7432 BGP EVPN]] - BGP MPLS-Based Ethernet VPN
- [[RFC 8365 EVPN Overlay]] - EVPN Network Virtualization Overlay
- [[RFC 791 IPv4]] - IP-Transportschicht
