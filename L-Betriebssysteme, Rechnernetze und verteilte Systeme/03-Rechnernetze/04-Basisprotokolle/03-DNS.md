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

Bei der rekursiven Auflösung fragt der Client einen Resolver, der die gesamte Auflösung übernimmt:

1. Client fragt lokalen DNS-Resolver
2. Resolver prüft lokalen Cache
3. Bei Cache Miss: Resolver fragt nacheinander Root → TLD → Authoritative
4. Resolver speichert Ergebnis im Cache und antwortet dem Client

> [!info] Caching
> Sowohl positive als auch **negative Antworten** werden gecacht (Negative Caching). Die TTL bestimmt die Cache-Dauer.

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

| Typ | IPv4 | IPv6 | Beschreibung | Beispiel |
|-----|------|------|--------------|----------|
| **A** | ✓ | - | Name zu IPv4-Adresse | `foo.example.org. IN A 192.168.1.2` |
| **AAAA** | - | ✓ | Name zu IPv6-Adresse | `foo.example.org. IN AAAA 2001:db8::1` |
| **PTR** | ✓ | ✓ | Adresse zu Name (Reverse) | `2.1.168.192.in-addr.arpa. IN PTR foo.example.org.` |
| **CNAME** | ✓ | ✓ | Alias für einen Namen | `www IN CNAME foo.example.org.` |
| **NS** | ✓ | ✓ | Nameserver für Domain | `example.org. IN NS ns1.example.org.` |
| **MX** | ✓ | ✓ | Mailserver für Domain | `example.org. 10 IN MX mail.example.org.` |
| **TXT** | ✓ | ✓ | Textinformation | SPF, DKIM, DMARC |
| **SOA** | ✓ | ✓ | Zone-Autorität | Seriennummer, Refresh, Expire |

## Paketformat

TODO: DNS-Header und -Sections (Question, Answer, Authority, Additional)

## DNS-Zonen

### Zonentypen

| Zonentyp | Beschreibung |
|----------|--------------|
| **Primary** | Autoritativer Server mit Original-Zonendaten. Hier werden Änderungen durchgeführt. |
| **Secondary** | Autoritativer DNS Server mit Kopie der Zonendaten vom Primary. Zonendaten müssen nur an einer Stelle gepflegt werden. |
| **Stub Zone** | Enthält nur Verweise auf die autoritativen Nameserver für eine DNS Zone (keine vollständige Kopie) |
| **Delegate** | Benennt einen autoritativen Nameserver für eine DNS Zone |
| **Hidden Primary** | Die Zonendaten zeigen auf "andere" autoritative DNS Server für diese Zone |

### Zone Transfers

- **AXFR**: Vollständiger Zonentransfer
- **IXFR**: Inkrementeller Zonentransfer (nur Änderungen)

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
