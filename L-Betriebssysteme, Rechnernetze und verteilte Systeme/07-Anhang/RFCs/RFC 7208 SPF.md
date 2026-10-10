---
title: "RFC 7208 - Sender Policy Framework (SPF)"
rfc_number: 7208
version: "April 2014"
status: Proposed Standard
author: "S. Kitterman"
obsoletes: "RFC 4408"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - email
  - spf
  - authentication
  - security
---

# RFC 7208 - Sender Policy Framework (SPF)

## Überblick

RFC 7208 definiert das Sender Policy Framework (SPF), eine E-Mail-Authentifizierungsmethode zur Erkennung gefälschter Absenderadressen während der E-Mail-Zustellung. SPF ermöglicht Domain-Inhabern anzugeben, welche Mailserver berechtigt sind, E-Mails in ihrem Namen zu senden.

## Zusammenfassung

SPF bietet E-Mail-Absendervalidierung:

- **DNS TXT Record**: In der DNS-Zone der Domain veröffentlicht
- **IP-Autorisierung**: Listet autorisierte Sende-IPs/Hosts
- **Mechanismen**: ALL, INCLUDE, A, MX, PTR, IP4, IP6, EXISTS
- **Qualifizierer**: + (Pass), - (Fail), ~ (SoftFail), ? (Neutral)
- **Modifikatoren**: redirect=, exp=

## SPF-Syntax

```
v=spf1 [mechanisms] [modifiers]
```

**Beispiel:**
```
v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all
```

## Wichtige Mechanismen

| Mechanismus | Beschreibung |
|-------------|--------------|
| ip4/ip6 | Übereinstimmung mit IP-Adresse/-Bereich |
| include | Einbinden des SPF einer anderen Domain |
| a | Übereinstimmung mit A-Record der Domain |
| mx | Übereinstimmung mit MX-Records der Domain |
| all | Übereinstimmung mit allem (üblicherweise zuletzt, mit Qualifizierer) |
SPF ist für die E-Mail-Authentifizierung konfiguriert:

**Typischer SPF-Record:**
```
v=spf1 include:spf.protection.outlook.com -all
```

## Offizielles Dokument

**RFC 7208**: [https://www.rfc-editor.org/rfc/rfc7208](https://www.rfc-editor.org/rfc/rfc7208)

## Verwandte RFCs

- [[RFC 5321 SMTP]] - SMTP-Protokoll
- [[RFC 6376 DKIM]] - DKIM-Signierung
- [[RFC 7489 DMARC]] - DMARC-Richtlinie
