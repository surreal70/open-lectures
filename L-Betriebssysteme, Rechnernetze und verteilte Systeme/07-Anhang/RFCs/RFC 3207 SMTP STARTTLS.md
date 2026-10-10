---
title: "RFC 3207 - SMTP Service Extension for Secure SMTP over TLS"
rfc_number: 3207
version: "February 2002"
status: Proposed Standard
author: "P. Hoffman"
obsoletes: "RFC 2487"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - smtp
  - tls
  - email
  - security
---

# RFC 3207 - SMTP STARTTLS

## Überblick

RFC 3207 definiert die STARTTLS-Erweiterung für SMTP, die eine Verschlüsselung der E-Mail-Übertragung zwischen Mailservern ermöglicht.

## Zusammenfassung

STARTTLS-Funktionen:

- **Opportunistische Verschlüsselung**: TLS wenn verfügbar
- **ESMTP-Erweiterung**: Angekündigt via EHLO
- **In-Band-Upgrade**: Verschlüsselung nach Verbindungsaufbau
- **Zertifikatsvalidierung**: Server-Authentifizierung

## STARTTLS-Ablauf

```
Client                          Server
   |                               |
   |------ EHLO example.com ------>|
   |<----- 250-STARTTLS -----------|
   |------ STARTTLS -------------->|
   |<----- 220 Ready for TLS ------|
   |                               |
   |       [TLS Handshake]         |
   |                               |
   |------ EHLO example.com ------>|
   |<----- 250 OK -----------------|
   |                               |
   |       [Encrypted SMTP]        |
```

## Wichtige Hinweise

| Aspekt | Beschreibung |
|--------|--------------|
| Port 25 | STARTTLS für Server-zu-Server |
| Port 587 | Submission mit STARTTLS |
| Port 465 | Implicit TLS (SMTPS) |
| MTA-STS | Erzwungenes TLS via DNS |

## Offizielles Dokument

**RFC 3207**: [https://www.rfc-editor.org/rfc/rfc3207](https://www.rfc-editor.org/rfc/rfc3207)

## Verwandte RFCs

- [[RFC 5321 SMTP]] - SMTP-Protokoll
- [[RFC 8446 TLS 1.3]] - TLS-Verschlüsselung
- [[RFC 8461 MTA-STS]] - SMTP MTA Strict Transport Security
