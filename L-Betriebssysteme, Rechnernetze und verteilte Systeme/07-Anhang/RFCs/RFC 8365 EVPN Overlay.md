---
title: "RFC 8365 - A Network Virtualization Overlay Solution Using EVPN"
rfc_number: 8365
version: "March 2018"
status: Proposed Standard
author: "A. Sajassi, J. Drake, N. Bitar, R. Shekhar, J. Uttaro, W. Henderickx"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - evpn
  - overlay
  - vxlan
  - datacenter
---

# RFC 8365 - EVPN Overlay

## Überblick

RFC 8365 beschreibt, wie EVPN als Control Plane für Overlay-Netzwerke wie VXLAN, NVGRE und MPLSoGRE verwendet wird.

## Zusammenfassung

EVPN Overlay-Lösung:

- **Unified Control Plane**: EVPN für verschiedene Encapsulations
- **VXLAN Integration**: EVPN + VXLAN
- **Distributed Gateway**: Anycast Gateway
- **Seamless Mobility**: VM-Migration

## Unterstützte Encapsulations

| Encapsulation | Beschreibung |
|---------------|--------------|
| VXLAN | UDP-basiert, Port 4789 |
| NVGRE | GRE-basiert |
| MPLSoGRE | MPLS über GRE |
| MPLSoUDP | MPLS über UDP |

## EVPN + VXLAN Architektur

```
+--------+                              +--------+
| VM 1   |                              | VM 2   |
+--------+                              +--------+
     |                                       |
+--------+     VXLAN Tunnel (VNI)      +--------+
| VTEP 1 |<===========================>| VTEP 2 |
+--------+         BGP EVPN            +--------+
     |                                       |
[========= Underlay Network (IP/MPLS) =========]
```

## Offizielles Dokument

**RFC 8365**: [https://www.rfc-editor.org/rfc/rfc8365](https://www.rfc-editor.org/rfc/rfc8365)

## Verwandte RFCs

- [[RFC 7432 BGP EVPN]] - EVPN-Grundlagen
- [[RFC 7348 VXLAN]] - VXLAN-Spezifikation
- [[RFC 791 IPv4]] - IP-Transport
