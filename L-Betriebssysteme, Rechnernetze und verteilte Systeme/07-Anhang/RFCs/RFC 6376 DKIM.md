---
title: "RFC 6376 - DomainKeys Identified Mail (DKIM)"
rfc_number: 6376
version: "September 2011"
status: Internet Standard
author: "D. Crocker, T. Hansen, M. Kucherawy"
obsoletes: "RFC 4871, RFC 5672"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - email
  - dkim
  - authentication
  - cryptography
---

# RFC 6376 - DomainKeys Identified Mail (DKIM)

## Überblick

RFC 6376 definiert DomainKeys Identified Mail (DKIM), eine E-Mail-Authentifizierungsmethode, die es einer Organisation ermöglicht, Verantwortung für eine Nachricht zu übernehmen, indem sie diese mit einer digitalen Signatur versieht. Empfänger können die Signatur mithilfe des in DNS veröffentlichten öffentlichen Schlüssels verifizieren.

## Zusammenfassung

DKIM bietet kryptografische E-Mail-Authentifizierung:

- **Digitale Signatur**: RSA- oder Ed25519-Signierung
- **Header-Kanonisierung**: Normalisiert Header vor dem Signieren
- **Body-Kanonisierung**: Normalisiert Body vor dem Signieren
- **DNS Public Key**: Als TXT-Record veröffentlicht
- **Selektor**: Ermöglicht mehrere Schlüssel pro Domain

## DKIM-Signatur-Header

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
  d=example.com; s=selector1;
  h=from:to:subject:date;
  bh=<body hash>;
  b=<signature>
```

## Wichtige Parameter

| Parameter | Beschreibung |
|-----------|--------------|
| v | Version (immer "1") |
| a | Algorithmus (rsa-sha256, ed25519-sha256) |
| d | Signierende Domain |
| s | Selektor (Schlüsselkennung) |
| h | Signierte Header |
| bh | Body-Hash |
| b | Signatur |

## DNS-Record-Format

```
selector._domainkey.example.com TXT "v=DKIM1; k=rsa; p=<public key>"
```
DKIM wird von Microsoft 365 gehandhabt:

## Offizielles Dokument

**RFC 6376**: [https://www.rfc-editor.org/rfc/rfc6376](https://www.rfc-editor.org/rfc/rfc6376)

## Verwandte RFCs

- [[RFC 5321 SMTP]] - SMTP-Protokoll
- [[RFC 7208 SPF]] - SPF-Authentifizierung
- [[RFC 7489 DMARC]] - DMARC-Richtlinie
- [[RFC 8463 Ed25519 DKIM]] - Ed25519 for DKIM
