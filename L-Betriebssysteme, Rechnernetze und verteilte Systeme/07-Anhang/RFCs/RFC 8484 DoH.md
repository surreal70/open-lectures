---
title: "RFC 8484 - DNS Queries over HTTPS (DoH)"
rfc_number: 8484
version: "October 2018"
status: Proposed Standard
author: "P. Hoffman, P. McManus"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - doh
  - https
  - privacy
  - encryption
---

# RFC 8484 - DNS-Anfragen über HTTPS (DoH)

## Überblick

RFC 8484 definiert DNS over HTTPS (DoH), ein Protokoll zum Senden von DNS-Anfragen und Empfangen von DNS-Antworten über HTTPS. DoH bietet Datenschutz durch Verschlüsselung des DNS-Verkehrs und verhindert Abhören und Manipulation.

## Zusammenfassung

DNS over HTTPS bietet:

- **Verschlüsselung**: DNS-Anfragen/Antworten via TLS verschlüsselt
- **Datenschutz**: Verhindert, dass ISP und Netzwerkbeobachter DNS-Anfragen sehen
- **Integrität**: Schutz vor DNS-Manipulation
- **HTTP-Integration**: Nutzt Standard-HTTPS-Infrastruktur
- **Port 443**: Vermischt sich mit regulärem HTTPS-Verkehr

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | HTTPS |
| Port | 443 |
| Media Type | application/dns-message |
| Methoden | GET und POST |
| URI-Template | Anbieter-spezifisch (z.B. /dns-query) |

## DoH-Anbieter

| Anbieter | DoH-Endpoint |
|----------|--------------|
| Quad9 | https://dns.quad9.net/dns-query |
| Cloudflare | https://cloudflare-dns.com/dns-query |
| Google | https://dns.google/dns-query |
DoH wird von Quad9, dem Upstream-DNS-Anbieter, unterstützt:
- Potenzielle zukünftige Implementierung für Client-Geräte

## Offizielles Dokument

**RFC 8484**: [https://www.rfc-editor.org/rfc/rfc8484](https://www.rfc-editor.org/rfc/rfc8484)

## Verwandte RFCs

- [[RFC 1035 DNS]] - Basis-DNS-Spezifikation
- [[RFC 7858 DoT]] - DNS over TLS
- [[RFC 8446 TLS 1.3]] - Transport-Sicherheit
