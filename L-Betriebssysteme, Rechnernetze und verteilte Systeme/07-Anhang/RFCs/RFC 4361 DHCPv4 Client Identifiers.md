---
title: "RFC 4361 - Node-specific Client Identifiers for DHCPv4"
rfc_number: 4361
version: "February 2006"
status: Proposed Standard
author: "T. Lemon, B. Sommerfeld"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dhcp
  - client-id
  - networking
---

# RFC 4361 - DHCPv4 Client Identifiers

## Überblick

RFC 4361 definiert verbesserte Client-Identifikatoren für DHCPv4, die eine konsistente Identifikation über verschiedene Netzwerkschnittstellen ermöglichen.

## Zusammenfassung

Verbesserte Client-Identifikation:

- **DUID**: DHCP Unique Identifier (aus DHCPv6)
- **IAID**: Interface Association Identifier
- **Konsistenz**: Gleiche ID über Schnittstellen hinweg
- **Dual-Stack**: Kompatibilität mit DHCPv6

## DUID-Typen

| Typ | Beschreibung |
|-----|--------------|
| DUID-LLT | Link-Layer + Zeit |
| DUID-EN | Enterprise Number + ID |
| DUID-LL | Nur Link-Layer-Adresse |

## Format

```
Client Identifier Option (61):
+------+--------+------+--------+------+
| 61   | Length | Type | IAID   | DUID |
+------+--------+------+--------+------+
```

## Offizielles Dokument

**RFC 4361**: [https://www.rfc-editor.org/rfc/rfc4361](https://www.rfc-editor.org/rfc/rfc4361)

## Verwandte RFCs

- [[RFC 2131 DHCP]] - DHCP-Protokoll
- [[RFC 2132 DHCP Options]] - DHCP-Optionen
- [[RFC 8415 DHCPv6]] - DHCP für IPv6
