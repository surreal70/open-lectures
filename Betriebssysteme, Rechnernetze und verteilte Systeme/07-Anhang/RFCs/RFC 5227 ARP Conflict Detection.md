---
title: "RFC 5227 - IPv4 Address Conflict Detection"
rfc_number: 5227
version: "July 2008"
status: Proposed Standard
author: "S. Cheshire"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - arp
  - ipv4
  - conflict
  - networking
---

# RFC 5227 - ARP Conflict Detection

## Überblick

RFC 5227 definiert Verfahren zur Erkennung von IPv4-Adresskonflikten mittels ARP, um doppelte IP-Adressen im Netzwerk zu verhindern.

## Zusammenfassung

Konflikt-Erkennung:

- **ARP Probe**: Prüfung vor Adressnutzung
- **ARP Announcement**: Bekanntgabe der Adresse
- **Duplicate Detection**: Erkennung während Nutzung
- **Konflikt-Reaktion**: Verhalten bei Duplikaten

## ARP Probe

```
ARP Request:
  Sender IP: 0.0.0.0
  Sender MAC: eigene MAC
  Target IP: zu prüfende IP
  Target MAC: 00:00:00:00:00:00

Timeout: 1-2 Sekunden
Probes: 3 Versuche
```

## ARP Announcement

```
ARP Request (Gratuitous ARP):
  Sender IP: eigene IP
  Sender MAC: eigene MAC
  Target IP: eigene IP
  Target MAC: ff:ff:ff:ff:ff:ff
```

## Konflikt-Verhalten

| Situation | Aktion |
|-----------|--------|
| Konflikt während Probe | Andere Adresse wählen |
| Konflikt während Nutzung | Verteidigen oder aufgeben |
| Wiederholte Konflikte | Exponential Backoff |

## Offizielles Dokument

**RFC 5227**: [https://www.rfc-editor.org/rfc/rfc5227](https://www.rfc-editor.org/rfc/rfc5227)

## Verwandte RFCs

- [[RFC 826 ARP]] - Address Resolution Protocol
- [[RFC 3927 Link-Local]] - Link-Local-Adressen
- [[RFC 2131 DHCP]] - DHCP-Protokoll
