---
title: "RFC 8738 - ACME IP Identifier Validation Extension"
rfc_number: 8738
version: "February 2020"
status: Proposed Standard
author: "R. Shoemaker"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - acme
  - ip
  - certificate
  - validation
---

# RFC 8738 - ACME IP Validation

## Überblick

RFC 8738 erweitert ACME um die Validierung von IP-Adressen für Zertifikate, nicht nur Domainnamen.

## Zusammenfassung

IP-Validierung in ACME:

- **IP-Zertifikate**: Zertifikate für IP-Adressen
- **HTTP-01**: Challenge auf IP-Adresse
- **TLS-ALPN-01**: TLS-Challenge auf IP
- **Keine DNS-01**: Nicht für IPs anwendbar

## Anwendungsfälle

| Szenario | Beschreibung |
|----------|--------------|
| Interne Server | Server ohne DNS-Namen |
| IoT Geräte | Geräte mit statischer IP |
| API Endpoints | Direkte IP-Verbindungen |
| Entwicklung | Testumgebungen |

## Identifier-Format

```json
{
  "identifier": {
    "type": "ip",
    "value": "192.0.2.1"
  }
}
```

## Challenges für IPs

| Challenge | Verfügbar für IP |
|-----------|-----------------|
| HTTP-01 | Ja |
| TLS-ALPN-01 | Ja |
| DNS-01 | Nein |

## Offizielles Dokument

**RFC 8738**: [https://www.rfc-editor.org/rfc/rfc8738](https://www.rfc-editor.org/rfc/rfc8738)

## Verwandte RFCs

- [[RFC 8555 ACME]] - ACME-Protokoll
- [[RFC 8737 ACME ALPN Challenge]] - TLS-ALPN-01
- [[RFC 8446 TLS 1.3]] - TLS-Protokoll
