---
title: "RFC 9112 - HTTP/1.1"
rfc_number: 9112
version: "June 2022"
status: Internet Standard
author: "R. Fielding, M. Nottingham, J. Reschke"
obsoletes: "RFC 7230"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - http
  - http11
  - web
---

# RFC 9112 - HTTP/1.1

## Überblick

RFC 9112 definiert die Message-Syntax und Verbindungsverwaltung für HTTP/1.1, das am weitesten verbreitete HTTP-Protokoll.

## Zusammenfassung

HTTP/1.1-Eigenschaften:

- **Textbasiert**: Menschenlesbare Nachrichten
- **Persistent Connections**: Keep-Alive
- **Chunked Transfer**: Streaming von Daten
- **Pipelining**: Mehrere Requests ohne Warten
- **Host Header**: Virtuelles Hosting

## Message-Format

```
Request:
GET /path HTTP/1.1
Host: example.com
Connection: keep-alive

Response:
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
```

## Verbindungsmanagement

| Feature | Beschreibung |
|---------|--------------|
| Keep-Alive | Verbindung wiederverwendbar |
| Pipelining | Requests ohne Response-Warten |
| Head-of-Line Blocking | Problem bei Pipelining |
| Chunked Encoding | Streaming ohne Content-Length |

## Offizielles Dokument

**RFC 9112**: [https://www.rfc-editor.org/rfc/rfc9112](https://www.rfc-editor.org/rfc/rfc9112)

## Verwandte RFCs

- [[RFC 9110 HTTP Semantics]] - HTTP-Semantik
- [[RFC 9111 HTTP Caching]] - HTTP-Caching
- [[RFC 9113 HTTP 2]] - HTTP/2
- [[RFC 8446 TLS 1.3]] - HTTPS-Verschlüsselung
