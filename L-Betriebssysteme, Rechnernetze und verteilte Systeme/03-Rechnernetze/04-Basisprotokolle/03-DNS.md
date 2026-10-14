---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - dns
  - layer7
bereich: RN
---

# DNS – Domain Name System

## Lernziele

- [ ] DNS-Hierarchie verstehen
- [ ] Auflösungsprozess (iterativ/rekursiv) erklären können
- [ ] Wichtige Record-Typen kennen
- [ ] DNS-Caching verstehen

## Überblick

Das **Domain Name System (DNS)** ist ein hierarchisches, verteiltes System zur Namensauflösung. Es übersetzt menschenlesbare Domainnamen in IP-Adressen.

```
┌─────────────────────────────────────────────────────────────┐
│                    DNS-Hierarchie                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                         . (Root)                            │
│                            │                                │
│          ┌─────────────────┼─────────────────┐              │
│          │                 │                 │              │
│         com               de                org             │
│          │                 │                 │              │
│    ┌─────┴─────┐     ┌─────┴─────┐          │              │
│    │           │     │           │          │              │
│  google    amazon   example    bund      wikipedia          │
│    │                   │                                    │
│   www               mail                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] RFC-Referenz
> - DNS Concepts: [[A-RFC-Index#RFC 1034|RFC 1034]]
> - DNS Implementation: [[A-RFC-Index#RFC 1035|RFC 1035]]

### Rekursive Auflösung

TODO: Client fragt Resolver, Resolver erledigt alles

### Iterative Auflösung

TODO: Resolver fragt nacheinander Root → TLD → Authoritative

```
┌────────┐  ┌──────────┐  ┌──────┐  ┌─────┐  ┌─────────────┐
│ Client │──│ Resolver │──│ Root │──│ TLD │──│Authoritative│
└────────┘  └──────────┘  └──────┘  └─────┘  └─────────────┘
     1.          2.           3.       4.          5.
   Anfrage    Rekursion    Verweis  Verweis     Antwort
```

### DNS-Caching

TODO: TTL, Negative Caching

## Record-Typen

| Typ | Beschreibung | Beispiel |
|-----|--------------|----------|
| A | IPv4-Adresse | `www.example.de → 93.184.216.34` |
| AAAA | IPv6-Adresse | `www.example.de → 2606:2800:...` |
| CNAME | Alias | `www → webserver.example.de` |
| MX | Mailserver | `example.de → mail.example.de` |
| NS | Nameserver | `example.de → ns1.example.de` |
| TXT | Textinformation | SPF, DKIM, DMARC |
| PTR | Reverse DNS | `34.216.184.93 → www.example.de` |
| SOA | Zone-Autorität | Seriennummer, Refresh, Expire |

TODO: Detaillierte Erklärung jedes Typs

## Paketformat

TODO: DNS-Header und -Sections (Question, Answer, Authority, Additional)

## DNS-Zonen

TODO: Primary/Secondary, Zone Transfers (AXFR, IXFR)

## Sicherheit

### DNS-Spoofing/Cache Poisoning

TODO: Gefälschte Antworten einspeisen

### DNSSEC

TODO: Kryptographische Signierung von DNS-Records

### DoH/DoT

TODO: DNS over HTTPS, DNS over TLS

## Praxisbeispiele

TODO: nslookup, dig, host

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - DNS-Hierarchie (Root, TLD, SLD)
> - Rekursive vs. iterative Auflösung
> - Wichtige Record-Typen (A, AAAA, MX, CNAME, NS)
> - TTL und Caching

## Zusammenfassung

TODO: Kernpunkte zusammenfassen

## Querverweise

- [[02-DHCP|DHCP]] – liefert DNS-Server-Adressen
- [[../05-Sicherheit/03-TLS|TLS]] – Zertifikate benötigen DNS
- [[../03-Referenzmodelle/08-Anwendungsschicht/02-HTTP|HTTP]] – nutzt DNS für Hostname-Auflösung
