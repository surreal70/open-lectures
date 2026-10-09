---
title: "RFC 9110 - HTTP Semantics"
rfc_number: 9110
version: "June 2022"
status: Internet Standard
author: "R. Fielding, M. Nottingham, J. Reschke"
obsoletes: "RFC 2818, RFC 7230, RFC 7231, RFC 7232, RFC 7233, RFC 7235, RFC 7538, RFC 7615, RFC 7694"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - http
  - web
  - api
  - semantics
---

# RFC 9110 - HTTP Semantics

## Überblick

RFC 9110 definiert die Semantik des HTTP-Protokolls, einschließlich Methoden, Statuscodes und Header-Felder. Dieser RFC konsolidiert und aktualisiert frühere HTTP-Spezifikationen zu einem modernen, einheitlichen Dokument.

## Zusammenfassung

HTTP-Semantik definiert, wie HTTP funktioniert:

- **Methoden**: GET, POST, PUT, DELETE, PATCH, etc.
- **Statuscodes**: 1xx-5xx Antwortkategorien
- **Header**: Request- und Response-Metadaten
- **Content Negotiation**: Client-Präferenzen für Content-Type
- **Caching**: Cache-Control-Mechanismen
- **Authentifizierung**: Authorization-Header-Framework

## HTTP-Methoden

| Methode | Beschreibung | Safe | Idempotent |
|---------|--------------|------|------------|
| GET | Ressource abrufen | Ja | Ja |
| HEAD | Nur Header abrufen | Ja | Ja |
| POST | Daten übermitteln | Nein | Nein |
| PUT | Ressource ersetzen | Nein | Ja |
| DELETE | Ressource entfernen | Nein | Ja |
| PATCH | Teilaktualisierung | Nein | Nein |
| OPTIONS | Erlaubte Methoden abrufen | Ja | Ja |

## Statuscode-Kategorien

| Bereich | Kategorie | Beispiele |
|---------|-----------|-----------|
| 1xx | Informational | 100 Continue |
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved, 304 Not Modified |
| 4xx | Client Error | 400 Bad Request, 404 Not Found |
| 5xx | Server Error | 500 Internal Error, 503 Unavailable |

## Offizielles Dokument

**RFC 9110**: [https://www.rfc-editor.org/rfc/rfc9110](https://www.rfc-editor.org/rfc/rfc9110)

## Verwandte RFCs

- [[RFC 9111 HTTP Caching]] - HTTP Caching
- [[RFC 9112 HTTP 1.1]] - HTTP/1.1
- [[RFC 9113 HTTP 2]] - HTTP/2
- [[RFC 9114 HTTP 3]] - HTTP/3
- [[RFC 8446 TLS 1.3]] - HTTPS-Transport-Sicherheit
