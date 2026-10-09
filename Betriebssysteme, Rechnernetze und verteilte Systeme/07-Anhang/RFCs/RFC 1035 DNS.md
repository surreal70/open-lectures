---
title: "RFC 1035 - Domain Name System"
rfc_number: 1035
version: "November 1987"
status: Internet Standard
author: "P. Mockapetris"
obsoletes: "RFC 882, RFC 883"
obsoleted_by: ""
updated_by: "Many (RFC 8499 for terminology)"
language: DE
tags:
  - rfc
  - dns
  - domain-names
  - foundation
---

# RFC 1035 - Domain Name System

## Überblick

RFC 1035 definiert zusammen mit RFC 1034 das Domain Name System (DNS), ein hierarchisches und dezentralisiertes Namenssystem für Ressourcen, die mit dem Internet oder privaten Netzwerken verbunden sind. DNS übersetzt menschenlesbare Domainnamen in IP-Adressen.

## Zusammenfassung

Das Domain Name System bietet:

- **Hierarchischer Namensraum**: Baumstrukturierte Domainnamen (z.B. www.example.com)
- **Verteilte Datenbank**: Nameserver weltweit verteilt
- **Resource Records**: Verschiedene Record-Typen (A, AAAA, MX, CNAME, TXT, etc.)
- **Anfrage/Antwort-Protokoll**: UDP Port 53 (TCP für Zonentransfers)
- **Caching**: TTL-basiertes Caching zur Reduzierung der Anfragelast
- **Rekursion**: Resolver können iterative Lookups durchführen

## Wichtige Record-Typen

| Typ | Zweck | Beispiel |
|-----|-------|----------|
| A | IPv4-Adresse | 192.0.2.1 |
| AAAA | IPv6-Adresse | 2001:db8::1 |
| CNAME | Kanonischer Name (Alias) | www → host.example.com |
| MX | Mail Exchanger | Priorität + Mailserver |
| TXT | Text-Records | SPF, DKIM, Verifizierung |
| NS | Nameserver | Autoritative Server |
| SOA | Start of Authority | Zonen-Metadaten |
| PTR | Reverse DNS | IP → Hostname |
DNS ist ein kritischer Foundation-Service:

- Upstream: Quad9 (9.9.9.9) mit DNSSEC-Validierung
- Lokaler Resolver: OPNsense Unbound
- Interne Zonen: Bereitgestellt durch internen DNS-Server

## Offizielles Dokument

**RFC 1035**: [https://www.rfc-editor.org/rfc/rfc1035](https://www.rfc-editor.org/rfc/rfc1035)

## Verwandte RFCs

- [[RFC 1034 DNS Concepts]] - Domain Names - Concepts and Facilities
- [[RFC 4033-4035 DNSSEC]] - DNS Security Extensions
- [[RFC 8484 DoH]] - DNS over HTTPS
- [[RFC 7858 DoT]] - DNS over TLS
