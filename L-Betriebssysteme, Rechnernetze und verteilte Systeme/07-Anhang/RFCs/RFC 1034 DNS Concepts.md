---
title: "RFC 1034 - Domain Names - Concepts and Facilities"
rfc_number: 1034
version: "November 1987"
status: Internet Standard
author: "P. Mockapetris"
obsoletes: "RFC 882, RFC 883"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - naming
  - concepts
---

# RFC 1034 - DNS Concepts

## Überblick

RFC 1034 definiert die grundlegenden Konzepte und Architektur des Domain Name Systems (DNS). Zusammen mit [[RFC 1035 DNS]] bildet dieser RFC die Basis für das gesamte DNS-System.

## Zusammenfassung

DNS-Konzepte und Architektur:

- **Domain-Namensraum**: Hierarchische Baumstruktur
- **Resource Records**: Datenformat für DNS-Einträge
- **Name Server**: Autoritative und rekursive Server
- **Resolver**: Client-seitige DNS-Auflösung
- **Caching**: Performanceoptimierung durch Zwischenspeicherung
- **Delegation**: Verteilung der Verantwortung

## DNS-Hierarchie

```
                    . (Root)
                    |
    +-------+-------+-------+-------+
    |       |       |       |       |
   com     org     net     de      edu
    |       |
  example  ietf
    |
   www
```

## Konzepte

| Konzept | Beschreibung |
|---------|--------------|
| Domain | Teilbaum des Namensraums |
| Zone | Administrativ verwalteter Bereich |
| Delegation | Übertragung der Autorität |
| FQDN | Fully Qualified Domain Name |
| Label | Einzelner Namensbestandteil |

## Offizielles Dokument

**RFC 1034**: [https://www.rfc-editor.org/rfc/rfc1034](https://www.rfc-editor.org/rfc/rfc1034)

## Verwandte RFCs

- [[RFC 1035 DNS]] - DNS Implementation and Specification
- [[RFC 4033-4035 DNSSEC]] - DNS Security Extensions
- [[RFC 8484 DoH]] - DNS over HTTPS
- [[RFC 7858 DoT]] - DNS over TLS
