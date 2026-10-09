---
title: "RFC 6750 - OAuth 2.0 Bearer Token Usage"
rfc_number: 6750
version: "October 2012"
status: Proposed Standard
author: "M. Jones, D. Hardt"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - oauth
  - bearer
  - token
  - authentication
---

# RFC 6750 - OAuth Bearer Token

## Überblick

RFC 6750 definiert, wie OAuth 2.0 Bearer Tokens zur Authentifizierung bei geschützten Ressourcen verwendet werden.

## Zusammenfassung

Bearer Token-Eigenschaften:

- **Träger-basiert**: Besitz des Tokens gewährt Zugang
- **Einfach**: Keine kryptografische Berechnung
- **TLS-pflichtig**: Muss über HTTPS übertragen werden
- **Zeitbegrenzt**: Expiration zur Schadensbegrenzung

## Token-Übertragung

### Authorization Header (empfohlen)
```
GET /resource HTTP/1.1
Authorization: Bearer mF_9.B5f-4.1JqM
```

### Form-Encoded Body
```
POST /resource HTTP/1.1
Content-Type: application/x-www-form-urlencoded

access_token=mF_9.B5f-4.1JqM
```

### URI Query Parameter (nicht empfohlen)
```
GET /resource?access_token=mF_9.B5f-4.1JqM HTTP/1.1
```

## Fehler-Responses

| Error | Beschreibung |
|-------|--------------|
| invalid_request | Fehlerhafter Request |
| invalid_token | Token abgelaufen/ungültig |
| insufficient_scope | Unzureichende Berechtigungen |

## Offizielles Dokument

**RFC 6750**: [https://www.rfc-editor.org/rfc/rfc6750](https://www.rfc-editor.org/rfc/rfc6750)

## Verwandte RFCs

- [[RFC 6749 OAuth 2.0]] - OAuth 2.0 Framework
- [[RFC 7519 JWT]] - JSON Web Tokens
- [[RFC 8446 TLS 1.3]] - Transport-Sicherheit
