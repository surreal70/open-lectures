---
title: "RFC 9114 - HTTP/3"
rfc_number: 9114
version: "June 2022"
status: Proposed Standard
author: "M. Bishop"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - http
  - http3
  - quic
  - web
---

# RFC 9114 - HTTP/3

## Überblick

RFC 9114 definiert HTTP/3, das HTTP über QUIC (UDP) implementiert und Latenz sowie Verbindungsmigration verbessert.

## Zusammenfassung

HTTP/3-Eigenschaften:

- **QUIC-basiert**: UDP statt TCP
- **0-RTT**: Schneller Verbindungsaufbau
- **Kein Head-of-Line Blocking**: Stream-unabhängig
- **Verbindungsmigration**: IP-Wechsel ohne Unterbrechung
- **Integrierte Verschlüsselung**: TLS 1.3 in QUIC

## Vergleich HTTP-Versionen

| Aspekt | HTTP/1.1 | HTTP/2 | HTTP/3 |
|--------|----------|--------|--------|
| Transport | TCP | TCP | QUIC/UDP |
| TLS | Optional | Üblich | Integriert |
| Multiplexing | Nein | Ja | Ja |
| HoL Blocking | Ja | TCP-Level | Nein |
| 0-RTT | Nein | Nein | Ja |

## QUIC-Vorteile

| Vorteil | Beschreibung |
|---------|--------------|
| Schneller Handshake | 1-RTT oder 0-RTT |
| Unabhängige Streams | Paketverlust betrifft nur einen Stream |
| Connection Migration | Mobil: IP-Wechsel ohne Reconnect |
| Always Encrypted | TLS 1.3 fest integriert |

## Offizielles Dokument

**RFC 9114**: [https://www.rfc-editor.org/rfc/rfc9114](https://www.rfc-editor.org/rfc/rfc9114)

## Verwandte RFCs

- [[RFC 9110 HTTP Semantics]] - HTTP-Semantik
- [[RFC 9113 HTTP 2]] - HTTP/2
- [[RFC 9000 QUIC]] - QUIC Transport Protocol
