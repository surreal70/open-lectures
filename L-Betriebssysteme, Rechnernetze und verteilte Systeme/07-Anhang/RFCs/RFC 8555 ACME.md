---
title: "RFC 8555 - Automatic Certificate Management Environment (ACME)"
rfc_number: 8555
version: "March 2019"
status: Proposed Standard
author: "R. Barnes, J. Hoffman-Andrews, D. McCarney, J. Kasten"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - acme
  - certificates
  - tls
  - automation
  - lets-encrypt
---

# RFC 8555 - Automatic Certificate Management Environment (ACME)

## Überblick

RFC 8555 definiert das ACME-Protokoll (Automatic Certificate Management Environment), das den Prozess der Zertifikatsausstellung und -verwaltung automatisiert. ACME ist das Protokoll hinter Let's Encrypt und anderen automatisierten Zertifizierungsstellen.

## Zusammenfassung

ACME automatisiert die TLS-Zertifikatsverwaltung:

- **Kontoregistrierung**: Konto bei CA erstellen
- **Zertifikate bestellen**: Zertifikate für Domains anfordern
- **Autorisierungs-Challenges**: Domain-Kontrolle nachweisen
- **Zertifikatsausstellung**: Signierte Zertifikate erhalten
- **Zertifikatswiderruf**: Kompromittierte Zertifikate widerrufen

## Challenge-Typen

| Challenge | Beschreibung | Port |
|-----------|--------------|------|
| HTTP-01 | Datei bei /.well-known/acme-challenge/ platzieren | 80 |
| DNS-01 | TXT-Record bei _acme-challenge erstellen | 53 |
| TLS-ALPN-01 | TLS-Handshake mit spezieller ALPN-Erweiterung | 443 |

## ACME-Workflow

```
1. Client → CA: Neues Konto
2. Client → CA: Neue Bestellung (für Domain)
3. CA → Client: Autorisierungs-Challenges
4. Client: Erfüllt Challenge (HTTP/DNS/TLS-ALPN)
5. Client → CA: Challenge abgeschlossen melden
6. CA: Validiert Challenge
7. Client → CA: Bestellung finalisieren (CSR einreichen)
8. CA → Client: Zertifikat
```

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | HTTPS (JSON) |
| Kontoschlüssel | RSA oder ECDSA |
| Zertifikatsformat | PEM |
| Gültigkeit (Let's Encrypt) | 90 Tage |
ACME wird für die automatisierte Zertifikatsverwaltung verwendet:

- Client: Certbot
- Challenge: DNS-01 via TSIG an BIND
- Validierung: Automatisiert über _acme-challenge TXT-Records
- Erneuerung: Automatisch 30 Tage vor Ablauf

## Offizielles Dokument

**RFC 8555**: [https://www.rfc-editor.org/rfc/rfc8555](https://www.rfc-editor.org/rfc/rfc8555)

## Verwandte RFCs

- [[RFC 8446 TLS 1.3]] - Transport Layer Security
- [[RFC 8737 ACME ALPN Challenge]] - ACME TLS-ALPN-01 Challenge
- [[RFC 8738 ACME IP Validation]] - ACME IP Identifier Validation
