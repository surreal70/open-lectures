---
title: "RFC 9111 - HTTP Caching"
rfc_number: 9111
version: "June 2022"
status: Internet Standard
author: "R. Fielding, M. Nottingham, J. Reschke"
obsoletes: "RFC 7234"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - http
  - caching
  - web
---

# RFC 9111 - HTTP Caching

## Überblick

RFC 9111 definiert HTTP-Caching-Mechanismen, die Webseiten und APIs effizienter machen, indem Antworten zwischengespeichert werden.

## Zusammenfassung

HTTP-Caching-Konzepte:

- **Freshness**: Wie lange eine Antwort gültig ist
- **Validation**: Prüfung ob Cache noch aktuell
- **Invalidation**: Wann Cache gelöscht wird
- **Cache-Control**: Header zur Steuerung

## Cache-Control Direktiven

| Direktive | Beschreibung |
|-----------|--------------|
| max-age=N | Cache gültig für N Sekunden |
| no-cache | Revalidierung vor Nutzung |
| no-store | Nicht cachen |
| private | Nur privater Cache |
| public | Auch shared Cache |
| must-revalidate | Nach Ablauf revalidieren |
| immutable | Nie revalidieren |

## Validation Headers

| Header | Zweck |
|--------|-------|
| ETag | Entity Tag für Ressource |
| Last-Modified | Letzter Änderungszeitpunkt |
| If-None-Match | Conditional mit ETag |
| If-Modified-Since | Conditional mit Datum |

## Offizielles Dokument

**RFC 9111**: [https://www.rfc-editor.org/rfc/rfc9111](https://www.rfc-editor.org/rfc/rfc9111)

## Verwandte RFCs

- [[RFC 9110 HTTP Semantics]] - HTTP-Grundlagen
- [[RFC 9112 HTTP 1.1]] - HTTP/1.1 Syntax
- [[RFC 9113 HTTP 2]] - HTTP/2
