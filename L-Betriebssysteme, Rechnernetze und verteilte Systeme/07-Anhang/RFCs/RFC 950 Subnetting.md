---
title: "RFC 950 - Internet Standard Subnetting Procedure"
rfc_number: 950
version: "August 1985"
status: Internet Standard
author: "J. Mogul, J. Postel"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ip
  - subnetting
  - networking
---

# RFC 950 - Subnetting

## Überblick

RFC 950 definiert das Verfahren zur Unterteilung von IP-Netzwerken in kleinere Subnetze. Dies ermöglicht eine effizientere Nutzung des IP-Adressraums und bessere Netzwerksegmentierung.

## Zusammenfassung

Subnetting-Grundlagen:

- **Subnetzmaske**: Trennung von Netz- und Host-Anteil
- **Netzwerkadresse**: Erste Adresse eines Subnetzes
- **Broadcast-Adresse**: Letzte Adresse eines Subnetzes
- **Host-Bereich**: Nutzbare Adressen im Subnetz
- **CIDR-Notation**: Kompakte Schreibweise (/24, /16, etc.)

## Subnetzmasken

| CIDR | Dezimal | Hosts |
|------|---------|-------|
| /8 | 255.0.0.0 | 16.777.214 |
| /16 | 255.255.0.0 | 65.534 |
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

## Berechnung

```
Netzwerkadresse = IP AND Subnetzmaske
Broadcast = Netzwerk OR (NOT Subnetzmaske)
Hosts = 2^(32-CIDR) - 2
```

## Offizielles Dokument

**RFC 950**: [https://www.rfc-editor.org/rfc/rfc950](https://www.rfc-editor.org/rfc/rfc950)

## Verwandte RFCs

- [[RFC 791 IPv4]] - Internet Protocol
- [[RFC 1918 Private Networks]] - Private Adressbereiche
- [[RFC 4632 CIDR]] - Classless Inter-Domain Routing
