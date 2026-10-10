---
title: "RFC 5321 - Simple Mail Transfer Protocol (SMTP)"
rfc_number: 5321
version: "October 2008"
status: Draft Standard
author: "J. Klensin"
obsoletes: "RFC 2821, RFC 821"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - smtp
  - email
  - mail
  - foundation
---

# RFC 5321 - Simple Mail Transfer Protocol (SMTP)

## Überblick

RFC 5321 definiert das Simple Mail Transfer Protocol (SMTP), das Standardprotokoll zum Senden von E-Mail-Nachrichten zwischen Servern. SMTP ist die Grundlage der E-Mail-Zustellung im Internet.

## Zusammenfassung

SMTP stellt E-Mail-Transport bereit:

- **Store-and-Forward**: Nachrichten zwischen MTAs weitergeleitet
- **Befehle**: HELO/EHLO, MAIL FROM, RCPT TO, DATA, QUIT
- **Erweiterungen**: ESMTP fügt Funktionen hinzu (STARTTLS, AUTH, SIZE)
- **Antwortcodes**: 2xx Erfolg, 4xx temporärer Fehler, 5xx permanenter Fehler
- **Port 25**: Standard-SMTP, oft für Einreichung blockiert
- **Port 587**: Nachrichteneinreichung (empfohlen)

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | TCP |
| Port 25 | Server-zu-Server-Relay |
| Port 587 | Client-Einreichung (STARTTLS) |
| Port 465 | Implizites TLS (veraltet, wiederbelebt) |
| Max. Zeilenlänge | 998 Zeichen |

## SMTP-Befehle

| Befehl | Zweck |
|--------|-------|
| EHLO | Erweiterte Begrüßung (identifiziert Client) |
| MAIL FROM | Absenderadresse |
| RCPT TO | Empfängeradresse |
| DATA | Nachrichteninhalt folgt |
| QUIT | Sitzung beenden |
| STARTTLS | Upgrade auf TLS |
| AUTH | Authentifizierung |

## Offizielles Dokument

**RFC 5321**: [https://www.rfc-editor.org/rfc/rfc5321](https://www.rfc-editor.org/rfc/rfc5321)

## Verwandte RFCs

- [[RFC 5321 SMTP]] - SMTP-Protokoll
- [[RFC 6376 DKIM]] - DomainKeys Identified Mail
- [[RFC 7489 DMARC]] - Domain-based Message Authentication
- [[RFC 3207 SMTP STARTTLS]] - SMTP Service Extension for Secure SMTP over TLS
