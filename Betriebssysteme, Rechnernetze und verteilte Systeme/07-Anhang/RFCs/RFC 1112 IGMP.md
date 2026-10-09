---
title: "RFC 1112 - Host Extensions for IP Multicasting"
rfc_number: 1112
version: "August 1989"
status: Internet Standard
author: "S. Deering"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - multicast
  - igmp
  - ipv4
---

# RFC 1112 - IGMP (v1)

## Überblick

RFC 1112 definiert die grundlegenden Erweiterungen für IP-Multicasting, einschließlich IGMP Version 1.

## Zusammenfassung

IP-Multicast-Grundlagen:

- **Multicast-Adressen**: 224.0.0.0 - 239.255.255.255 (Class D)
- **IGMP**: Internet Group Management Protocol
- **Host-Gruppen**: Dynamische Mitgliedschaft
- **Local Multicast**: 224.0.0.x (TTL=1)

## IGMP Version 1

| Nachricht | Beschreibung |
|-----------|--------------|
| Membership Query | Router fragt nach Mitgliedern |
| Membership Report | Host meldet Gruppenmitgliedschaft |

## Multicast-Adressen

| Bereich | Verwendung |
|---------|------------|
| 224.0.0.0/24 | Local Network Control |
| 224.0.0.1 | All Hosts |
| 224.0.0.2 | All Routers |
| 224.0.1.0/24 | Internetwork Control |
| 239.0.0.0/8 | Administratively Scoped |

## Funktionsweise

```
1. Host will Multicast-Gruppe beitreten
2. Host sendet IGMP Report
3. Router notiert Gruppenmitgliedschaft
4. Router leitet Multicast-Traffic weiter
5. Periodische Queries prüfen Mitgliedschaft
6. Ohne Reports: Gruppe wird entfernt
```

## Offizielles Dokument

**RFC 1112**: [https://www.rfc-editor.org/rfc/rfc1112](https://www.rfc-editor.org/rfc/rfc1112)

## Verwandte RFCs

- [[RFC 3376 IGMPv3]] - IGMP Version 3
- [[RFC 5771 Multicast]] - Multicast-Adressverwaltung
- [[RFC 791 IPv4]] - Internet Protocol
