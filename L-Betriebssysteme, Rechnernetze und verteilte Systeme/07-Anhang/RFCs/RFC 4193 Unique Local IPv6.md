---
title: "RFC 4193 - Unique Local IPv6 Unicast Addresses"
rfc_number: 4193
version: "October 2005"
status: Proposed Standard
author: "R. Hinden, B. Haberman"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ipv6
  - ula
  - private
---

# RFC 4193 - Unique Local IPv6

## Überblick

RFC 4193 definiert Unique Local Addresses (ULA) für IPv6, das Äquivalent zu privaten IPv4-Adressen (RFC 1918).

## Zusammenfassung

ULA-Eigenschaften:

- **Präfix**: fc00::/7 (praktisch fd00::/8)
- **Global eindeutig**: Zufällig generierte 40-Bit-ID
- **Nicht routbar**: Nicht im globalen Internet
- **Stabil**: Für interne Dienste geeignet
- **Kollisionsarm**: Geringe Wahrscheinlichkeit bei Zusammenlegung

## Adressformat

```
| 7 Bit |  1  |    40 Bit     |  16 Bit  |     64 Bit     |
+-------+-----+---------------+----------+----------------+
| fc00  |  L  |   Global ID   | Subnet   |  Interface ID  |
+-------+-----+---------------+----------+----------------+

L=1: Lokal zugewiesen (fd00::/8)
L=0: Reserviert für zukünftige Nutzung
```

## Vergleich mit RFC 1918

| IPv4 (RFC 1918) | IPv6 (ULA) |
|-----------------|------------|
| 10.0.0.0/8 | fd00::/8 |
| 172.16.0.0/12 | fd00::/8 |
| 192.168.0.0/16 | fd00::/8 |
| Kollisionsgefahr | Eindeutige Global ID |

## Offizielles Dokument

**RFC 4193**: [https://www.rfc-editor.org/rfc/rfc4193](https://www.rfc-editor.org/rfc/rfc4193)

## Verwandte RFCs

- [[RFC 8200 IPv6]] - IPv6-Spezifikation
- [[RFC 4291 IPv6 Addressing]] - IPv6-Adressierungsarchitektur
- [[RFC 1918 Private Networks]] - IPv4 Private Adressen
