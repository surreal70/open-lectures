---
title: "RFC 8737 - ACME TLS-ALPN-01 Challenge"
rfc_number: 8737
version: "February 2020"
status: Proposed Standard
author: "R. Shoemaker"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - acme
  - tls
  - alpn
  - certificate
---

# RFC 8737 - ACME TLS-ALPN-01

## Überblick

RFC 8737 definiert die TLS-ALPN-01 Challenge für ACME, eine Alternative zur HTTP-01 Challenge, die auf Port 443 arbeitet.

## Zusammenfassung

TLS-ALPN-01 Eigenschaften:

- **Port 443**: Funktioniert auch wenn Port 80 blockiert ist
- **TLS-basiert**: Validierung über TLS-Handshake
- **ALPN Protocol**: Spezielle ALPN-Kennung
- **Selbstsigniertes Zertifikat**: Mit Challenge-Token

## Challenge-Ablauf

```
1. ACME Server sendet Challenge mit Token
2. Client erstellt spezielles TLS-Zertifikat
3. Client konfiguriert Server für acme-tls/1 ALPN
4. ACME Server verbindet zu Port 443
5. ACME Server validiert Zertifikat
6. Bei Erfolg: Zertifikat wird ausgestellt
```

## TLS-Validierungszertifikat

| Feld | Wert |
|------|------|
| subjectAltName | Zu validierende Domain |
| acmeIdentifier Extension | SHA-256(Token \|\| Account Key) |
| ALPN Protocol | "acme-tls/1" |

## Vergleich Challenge-Typen

| Typ | Port | Protokoll |
|-----|------|-----------|
| HTTP-01 | 80 | HTTP |
| TLS-ALPN-01 | 443 | TLS |
| DNS-01 | - | DNS |

## Offizielles Dokument

**RFC 8737**: [https://www.rfc-editor.org/rfc/rfc8737](https://www.rfc-editor.org/rfc/rfc8737)

## Verwandte RFCs

- [[RFC 8555 ACME]] - ACME-Protokoll
- [[RFC 8738 ACME IP Validation]] - IP-Validierung
- [[RFC 8446 TLS 1.3]] - TLS-Protokoll
