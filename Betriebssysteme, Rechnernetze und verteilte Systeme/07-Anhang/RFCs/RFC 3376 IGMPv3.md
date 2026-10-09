---
title: "RFC 3376 - Internet Group Management Protocol, Version 3"
rfc_number: 3376
version: "October 2002"
status: Proposed Standard
author: "B. Cain, S. Deering, I. Kouvelas, B. Fenner, A. Thyagarajan"
obsoletes: "RFC 2236"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - multicast
  - igmp
  - igmpv3
---

# RFC 3376 - IGMPv3

## Überblick

RFC 3376 definiert IGMP Version 3, das Source-Specific Multicast (SSM) unterstützt und erweiterte Filterung ermöglicht.

## Zusammenfassung

IGMPv3-Erweiterungen:

- **Source Filtering**: Include/Exclude Listen
- **SSM Support**: Source-Specific Multicast
- **Abwärtskompatibel**: Mit IGMPv1/v2
- **Robustheit**: Verbesserte Zuverlässigkeit

## Vergleich IGMP-Versionen

| Feature | v1 | v2 | v3 |
|---------|----|----|-----|
| Leave Group | Nein | Ja | Ja |
| Group-Specific Query | Nein | Ja | Ja |
| Source Filtering | Nein | Nein | Ja |
| SSM Support | Nein | Nein | Ja |

## Source Filtering Modes

| Modus | Beschreibung |
|-------|--------------|
| INCLUDE | Nur von bestimmten Quellen empfangen |
| EXCLUDE | Von allen außer bestimmten Quellen empfangen |

## Membership Report

```
IGMPv3 Report enthält:
- Group Records (mehrere pro Nachricht)
  - Record Type (INCLUDE/EXCLUDE/Change)
  - Multicast Address
  - Source Addresses (Liste)
```

## Offizielles Dokument

**RFC 3376**: [https://www.rfc-editor.org/rfc/rfc3376](https://www.rfc-editor.org/rfc/rfc3376)

## Verwandte RFCs

- [[RFC 1112 IGMP]] - IGMP Version 1
- [[RFC 4604 SSM]] - Source-Specific Multicast
- [[RFC 5771 Multicast]] - Multicast-Adressverwaltung
