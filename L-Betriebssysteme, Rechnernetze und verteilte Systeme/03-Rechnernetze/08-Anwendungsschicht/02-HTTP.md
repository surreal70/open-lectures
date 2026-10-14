---
author: Andreas Hümmer
title: HTTP
tags:
  - content
  - rn
  - application-layer
  - http
  - web
  - protokoll
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---

# HTTP

## Definition

HTTP (Hypertext Transfer Protocol) ist das Protokoll für die Übertragung von Webinhalten.

## Erklärung

HTTP ist ein zustandsloses Request-Response-Protokoll. Ein Client sendet eine Anfrage (GET, POST, etc.) an einen Server, der mit einer Antwort und Statuscode antwortet. HTTPS ist die verschlüsselte Variante über TLS.

## Eigenschaften

- Zustandsloses Request-Response-Modell
- Methoden: GET, POST, PUT, DELETE, etc.
- Statuscodes: 2xx (Erfolg), 4xx (Client-Fehler), 5xx (Server-Fehler)
- HTTP/2 und HTTP/3 für bessere Performance

## Beispiele

- GET /index.html HTTP/1.1
- Status 200 OK - Erfolgreiche Anfrage
- Status 404 Not Found - Ressource nicht gefunden

## Zusammenhänge

- [[DNS]]
- [[TCP]]
- [[TLS]]
- [[Ports]]

## Prüfungstipps

- HTTP-Methoden und ihre Bedeutung
- Wichtige Statuscodes
- Unterschied HTTP/1.1, HTTP/2, HTTP/3

## Quellen

- *Quelle 1*
