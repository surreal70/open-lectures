---
title: "RFC 4291 - IP Version 6 Addressing Architecture"
rfc_number: 4291
version: "February 2006"
status: Draft Standard
author: "R. Hinden, S. Deering"
obsoletes: "RFC 3513"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ipv6
  - addressing
  - networking
---

# RFC 4291 - IPv6 Addressing

## Überblick

RFC 4291 definiert die Adressierungsarchitektur für IPv6, einschließlich Adresstypen, Formate und Zuweisungsregeln.

## Zusammenfassung

IPv6-Adressierung:

- **128-Bit-Adressen**: Massiv erweiterter Adressraum
- **Unicast**: Einzeladresse für ein Interface
- **Multicast**: Adresse für eine Gruppe von Interfaces
- **Anycast**: Nächstes Interface einer Gruppe
- **Kein Broadcast**: Ersetzt durch Multicast

## Adressformate

| Typ | Präfix | Beschreibung |
|-----|--------|--------------|
| Loopback | ::1/128 | Lokale Schleife |
| Link-Local | fe80::/10 | Nur lokales Netzwerk |
| Unique Local | fc00::/7 | Private Adressen |
| Global Unicast | 2000::/3 | Öffentliche Adressen |
| Multicast | ff00::/8 | Gruppenadressierung |

## Notation

```
Vollständig: 2001:0db8:0000:0000:0000:0000:0000:0001
Komprimiert: 2001:db8::1

Interface ID: typisch /64 für Hosts
Präfix: typisch /48 oder /64 für Netzwerke
```

## Offizielles Dokument

**RFC 4291**: [https://www.rfc-editor.org/rfc/rfc4291](https://www.rfc-editor.org/rfc/rfc4291)

## Verwandte RFCs

- [[RFC 8200 IPv6]] - IPv6-Spezifikation
- [[RFC 4862 IPv6 SLAAC]] - Stateless Address Autoconfiguration
- [[RFC 4193 Unique Local IPv6]] - Unique Local Adressen
