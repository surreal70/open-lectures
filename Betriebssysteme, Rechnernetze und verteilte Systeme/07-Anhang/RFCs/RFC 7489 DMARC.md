---
title: "RFC 7489 - Domain-based Message Authentication, Reporting, and Conformance (DMARC)"
rfc_number: 7489
version: "March 2015"
status: Informational
author: "M. Kucherawy, E. Zwicky"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - email
  - dmarc
  - authentication
  - security
---

# RFC 7489 - DMARC

## Überblick

RFC 7489 definiert Domain-based Message Authentication, Reporting, and Conformance (DMARC), ein Protokoll, das auf SPF und DKIM aufbaut, um Domain-Inhabern Kontrolle über E-Mail-Authentifizierung und Berichterstattung zu geben.

## Zusammenfassung

DMARC bietet E-Mail-Richtlinien und Berichterstattung:

- **Richtliniendefinition**: Festlegung der Behandlung von Authentifizierungsfehlern
- **Alignment**: Erfordert Übereinstimmung von SPF/DKIM-Domains mit From-Header
- **Berichterstattung**: Aggregierte und forensische Berichte an Domain-Inhaber
- **Richtlinien**: none, quarantine, reject

## DMARC-Record-Format

```
_dmarc.example.com TXT "v=DMARC1; p=reject; rua=mailto:dmarc@example.com"
```

## Wichtige Parameter

| Parameter | Beschreibung | Werte |
|-----------|--------------|-------|
| v | Version | DMARC1 |
| p | Richtlinie | none, quarantine, reject |
| sp | Subdomain-Richtlinie | none, quarantine, reject |
| rua | Aggregatbericht-URI | mailto:-Adresse |
| ruf | Forensischer Bericht-URI | mailto:-Adresse |
| pct | Prozentsatz für Richtlinienanwendung | 0-100 |
| adkim | DKIM-Alignment | r (relaxed), s (strict) |
| aspf | SPF-Alignment | r (relaxed), s (strict) |

## DMARC-Richtlinien

| Richtlinie | Aktion |
|------------|--------|
| none | Nur überwachen, keine Aktion |
| quarantine | Als Spam/verdächtig markieren |
| reject | Nachricht ablehnen |

## Offizielles Dokument

**RFC 7489**: [https://www.rfc-editor.org/rfc/rfc7489](https://www.rfc-editor.org/rfc/rfc7489)

## Verwandte RFCs

- [[RFC 5321 SMTP]] - SMTP-Protokoll
- [[RFC 7208 SPF]] - SPF-Authentifizierung
- [[RFC 6376 DKIM]] - DKIM-Signierung
