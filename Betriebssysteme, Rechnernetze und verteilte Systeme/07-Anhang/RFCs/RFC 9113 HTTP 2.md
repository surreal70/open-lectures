---
title: "RFC 9113 - HTTP/2"
rfc_number: 9113
version: "June 2022"
status: Proposed Standard
author: "M. Thomson, C. Benfield"
obsoletes: "RFC 7540, RFC 8740"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - http
  - http2
  - web
  - performance
---

# RFC 9113 - HTTP/2

## Überblick

RFC 9113 definiert HTTP/2, eine binäre, multiplexte Version von HTTP mit verbesserter Performance gegenüber HTTP/1.1.

## Zusammenfassung

HTTP/2-Eigenschaften:

- **Binäres Protokoll**: Effiziente Übertragung
- **Multiplexing**: Mehrere Streams pro Verbindung
- **Header-Kompression**: HPACK
- **Server Push**: Proaktives Senden
- **Stream-Priorisierung**: Wichtigkeit steuern

## Verbesserungen gegenüber HTTP/1.1

| HTTP/1.1 | HTTP/2 |
|----------|--------|
| Textbasiert | Binär |
| Head-of-Line Blocking | Multiplexing |
| Keine Kompression | HPACK Header-Kompression |
| Mehrere TCP-Verbindungen | Eine Verbindung |
| Kein Server Push | Server Push möglich |

## Frame-Typen

| Typ | Beschreibung |
|-----|--------------|
| DATA | Nutzdaten |
| HEADERS | HTTP-Header |
| PRIORITY | Stream-Priorität |
| RST_STREAM | Stream abbrechen |
| SETTINGS | Verbindungsparameter |
| PUSH_PROMISE | Server Push ankündigen |
| PING | Keep-Alive/RTT messen |
| GOAWAY | Verbindung schließen |

## Offizielles Dokument

**RFC 9113**: [https://www.rfc-editor.org/rfc/rfc9113](https://www.rfc-editor.org/rfc/rfc9113)

## Verwandte RFCs

- [[RFC 9110 HTTP Semantics]] - HTTP-Semantik
- [[RFC 9114 HTTP 3]] - HTTP/3 über QUIC
- [[RFC 8446 TLS 1.3]] - Verschlüsselung (ALPN)
