---
title: "RFC 5905 - Network Time Protocol Version 4 (NTPv4)"
rfc_number: 5905
version: "June 2010"
status: Proposed Standard
author: "D. Mills, J. Martin, J. Burbank, W. Kasch"
obsoletes: "RFC 1305, RFC 4330"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ntp
  - time
  - synchronization
  - foundation
---

# RFC 5905 - Network Time Protocol Version 4 (NTPv4)

## Überblick

RFC 5905 definiert das Network Time Protocol Version 4 (NTPv4), das Protokoll zur Synchronisation von Computeruhren über paketvermittelte Netzwerke. NTP ist eines der ältesten noch verwendeten Internetprotokolle.

## Zusammenfassung

NTP bietet präzise Zeitsynchronisation:

- **Stratum-Hierarchie**: Stratum 0 (Atomuhren) → Stratum 15
- **Taktfilterung**: Algorithmen zur Auswahl der besten Zeitquelle
- **Authentifizierung**: Optionale symmetrische Schlüssel und Autokey
- **Genauigkeit**: Typischerweise Millisekunden über das Internet, Mikrosekunden im LAN
- **Modi**: Client/Server, Symmetrisch, Broadcast

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | UDP |
| Port | 123 |
| Paketgröße | Minimum 48 Bytes |
| Stratum-Bereich | 0-15 (16 = nicht synchronisiert) |
| Poll-Intervall | 64s bis 1024s (adaptiv) |

## Stratum-Ebenen

| Stratum | Beschreibung |
|---------|--------------|
| 0 | Referenzuhr (Atom, GPS) |
| 1 | Primärer Server (direkt mit Stratum 0 verbunden) |
| 2 | Sekundärer Server (mit Stratum 1 synchronisiert) |
| 3+ | Tertiäre Server |
| 16 | Nicht synchronisiert |
NTP wird für die Zeitsynchronisation aller Systeme verwendet:

- Upstream: PTB (ptbtime1/2/3.ptb.de) - Stratum 1
- Firewalls: Direkte Synchronisation mit PTB (Stratum 2)
- Clients: Synchronisation über Firewalls oder DHCP-bereitgestelltes NTP

## Offizielles Dokument

**RFC 5905**: [https://www.rfc-editor.org/rfc/rfc5905](https://www.rfc-editor.org/rfc/rfc5905)

## Verwandte RFCs

- RFC 8915 - Network Time Security for NTP
- RFC 7822 - NTP Extension Field
- RFC 5906 - NTP Autokey Protocol (veraltet)
