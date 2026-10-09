---
title: "RFC 4604 - Using IGMPv3 and MLDv2 for Source-Specific Multicast"
rfc_number: 4604
version: "August 2006"
status: Proposed Standard
author: "H. Holbrook, B. Cain, B. Haberman"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - multicast
  - ssm
  - igmp
---

# RFC 4604 - Source-Specific Multicast

## Überblick

RFC 4604 definiert, wie IGMPv3 und MLDv2 für Source-Specific Multicast (SSM) verwendet werden.

## Zusammenfassung

SSM-Eigenschaften:

- **Quelle spezifiziert**: Empfang nur von bestimmter Quelle
- **Kein RP erforderlich**: Vereinfachtes Routing
- **Sicherheit**: Keine ungewollten Quellen
- **Effizienz**: Direkter Source-to-Group Tree

## SSM vs ASM

| ASM (Any-Source) | SSM (Source-Specific) |
|------------------|----------------------|
| (*,G) - Alle Quellen | (S,G) - Bestimmte Quelle |
| Rendezvous Point | Kein RP nötig |
| Komplexes Routing | Einfaches Routing |
| 224.0.0.0/4 | 232.0.0.0/8 |

## SSM-Adressbereich

| IP-Version | SSM Range |
|------------|-----------|
| IPv4 | 232.0.0.0/8 |
| IPv6 | ff3x::/32 |

## SSM-Ablauf

```
1. Empfänger kennt Quelle (S) und Gruppe (G)
2. Empfänger sendet IGMPv3 INCLUDE(G,{S})
3. Router baut Shortest Path Tree zu S
4. Daten fließen direkt von S zu Empfängern
```

## Offizielles Dokument

**RFC 4604**: [https://www.rfc-editor.org/rfc/rfc4604](https://www.rfc-editor.org/rfc/rfc4604)

## Verwandte RFCs

- [[RFC 3376 IGMPv3]] - IGMP Version 3
- [[RFC 1112 IGMP]] - IP-Multicasting-Grundlagen
- [[RFC 5771 Multicast]] - Multicast-Adressverwaltung
