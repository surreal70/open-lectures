---
title: "RFC 2132 - DHCP Options and BOOTP Vendor Extensions"
rfc_number: 2132
version: "March 1997"
status: Draft Standard
author: "S. Alexander, R. Droms"
obsoletes: "RFC 1533"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dhcp
  - bootp
  - options
---

# RFC 2132 - DHCP Options

## Überblick

RFC 2132 definiert die DHCP-Optionen, die zusammen mit [[RFC 2131 DHCP]] die vollständige DHCP-Konfiguration ermöglichen.

## Zusammenfassung

DHCP-Optionen ermöglichen:

- **Netzwerkkonfiguration**: Gateway, DNS, NTP
- **Host-Konfiguration**: Hostname, Domain
- **Vendor-spezifisch**: Herstelleroptionen
- **Lease-Management**: Zeiten, Erneuerung

## Wichtige Optionen

| Option | Code | Beschreibung |
|--------|------|--------------|
| Subnet Mask | 1 | Subnetzmaske |
| Router | 3 | Default Gateway |
| DNS Server | 6 | DNS-Server-Adressen |
| Domain Name | 15 | DNS-Domainname |
| NTP Server | 42 | Zeitserver |
| Lease Time | 51 | Gültigkeitsdauer |
| DHCP Server | 54 | Server-Identifikation |
| Renewal Time | 58 | T1 - Erneuerungszeit |
| Rebinding Time | 59 | T2 - Rebinding-Zeit |

## Option-Format

```
+------+--------+------+------+------+
| Code | Length | Data | Data | ...  |
+------+--------+------+------+------+
  1B      1B       Length Bytes
```

## Offizielles Dokument

**RFC 2132**: [https://www.rfc-editor.org/rfc/rfc2132](https://www.rfc-editor.org/rfc/rfc2132)

## Verwandte RFCs

- [[RFC 2131 DHCP]] - DHCP-Protokoll
- [[RFC 4361 DHCPv4 Client Identifiers]] - Client-Identifikation
- [[RFC 3927 Link-Local]] - DHCP-Fallback
