---
title: "RFC 7858 - DNS over TLS (DoT)"
rfc_number: 7858
version: "May 2016"
status: Proposed Standard
author: "Z. Hu, L. Zhu, J. Heidemann, A. Mankin, D. Wessels, P. Hoffman"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - dot
  - tls
  - privacy
  - encryption
---

# RFC 7858 - DNS over TLS (DoT)

## Überblick

RFC 7858 definiert DNS over TLS (DoT), ein Protokoll zur Verschlüsselung von DNS-Anfragen und -Antworten mittels Transport Layer Security (TLS). DoT bietet Datenschutz und Integrität für DNS-Kommunikation.

## Zusammenfassung

DNS over TLS bietet:

- **Verschlüsselung**: DNS-Verkehr mit TLS verschlüsselt
- **Dedizierter Port**: Port 853 für DoT-Verkehr
- **Server-Authentifizierung**: TLS-Zertifikatsverifizierung
- **Datenschutz**: Verhindert Abhören von DNS-Anfragen
- **Integrität**: Schutz vor DNS-Manipulation

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | TCP mit TLS |
| Port | 853 |
| TLS-Version | Minimum 1.2 (1.3 empfohlen) |
| Verbindung | Persistente TCP-Verbindung empfohlen |

## DoT vs DoH

| Aspekt | DoT (RFC 7858) | DoH (RFC 8484) |
|--------|----------------|----------------|
| Port | 853 | 443 |
| Protokoll | TLS-Stream | HTTPS |
| Blockierbar | Leicht zu blockieren | Schwer zu blockieren |
| Performance | Geringerer Overhead | Höherer Overhead |
DoT wird von Quad9, dem Upstream-DNS-Anbieter, unterstützt:

**Quad9 DoT:**
- Server: dns.quad9.net
- Port: 853

## Offizielles Dokument

**RFC 7858**: [https://www.rfc-editor.org/rfc/rfc7858](https://www.rfc-editor.org/rfc/rfc7858)

## Verwandte RFCs

- [[RFC 1035 DNS]] - Basis-DNS-Spezifikation
- [[RFC 8484 DoH]] - DNS over HTTPS
- [[RFC 8446 TLS 1.3]] - Transport-Sicherheit
