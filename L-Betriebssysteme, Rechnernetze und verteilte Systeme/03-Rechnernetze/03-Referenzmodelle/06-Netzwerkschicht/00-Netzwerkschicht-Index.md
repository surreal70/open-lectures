---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - network-layer
bereich: RN
---

# Netzwerkschicht (Layer 3)

> [!info] Einordnung im OSI-Modell
> Die Netzwerkschicht ist **Schicht 3** des OSI-Modells und entspricht der **Internetschicht** im TCP/IP-Modell. Sie ermöglicht die netzwerkübergreifende Kommunikation durch logische Adressierung und Routing.

## Lernziele

Nach diesem Kapitel sollten Sie:

- [ ] Die Aufgaben der Netzwerkschicht erklären können
- [ ] Den Aufbau von IPv4- und IPv6-Headern verstehen
- [ ] Subnetting und CIDR-Notation beherrschen
- [ ] Routing-Konzepte (statisch/dynamisch) unterscheiden können
- [ ] Die Unterschiede zwischen IPv4 und IPv6 kennen

## Kernaufgaben der Netzwerkschicht

```
┌─────────────────────────────────────────────────────────────────┐
│                    NETZWERKSCHICHT (Layer 3)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  ADRESSIERUNG    │    │    ROUTING       │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • IP-Adressen    │    │ • Wegfindung     │                  │
│   │ • Subnetting     │    │ • Forwarding     │                  │
│   │ • NAT            │    │ • Routing-Tab.   │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  FRAGMENTIERUNG  │    │  FEHLERMELDUNG   │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • MTU-Anpassung  │    │ • ICMP           │                  │
│   │ • Reassembly     │    │ • Ping/Tracert   │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│              PDU: IP-Paket (IP Datagram)                        │
└─────────────────────────────────────────────────────────────────┘
```

## Wichtige Protokolle

| Protokoll | Funktion | RFC |
|-----------|----------|-----|
| **IPv4** | Internet Protocol Version 4 | [[A-RFC-Index\|RFC 791]] |
| **IPv6** | Internet Protocol Version 6 | [[A-RFC-Index\|RFC 8200]] |
| **ICMP** | Fehlermeldungen, Ping | [[A-RFC-Index\|RFC 792]] |
| **ICMPv6** | ICMP für IPv6, inkl. NDP | [[A-RFC-Index\|RFC 4443]] |
| **ARP** | Address Resolution (L2/L3) | [[A-RFC-Index\|RFC 826]] |
| **OSPF** | Link-State Routing | [[A-RFC-Index\|RFC 2328]] |
| **BGP** | Border Gateway Protocol | [[A-RFC-Index\|RFC 4271]] |

## Inhaltsverzeichnis

1. [[01-IP-Protokoll]] - IPv4-Adressierung, Header, Subnetting
2. [[02-Routing]] - Statisches/dynamisches Routing, Protokolle
3. [[03-IPv6]] - Next Generation Internet Protocol

## Netzwerkgeräte auf Layer 3

```
              Internet
                 │
                 ▼
         ┌───────────────┐
         │    ROUTER     │  ← Verbindet Netzwerke
         │  (Layer 3)    │    Routing-Entscheidungen
         └───────┬───────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
   ┌─────────┐       ┌─────────┐
   │ Netz A  │       │ Netz B  │
   │10.0.1.0 │       │10.0.2.0 │
   └─────────┘       └─────────┘
```

> [!tip] Prüfungsrelevanz
> Die Netzwerkschicht ist ein **Kernthema** in der Prüfung. Besonders wichtig sind:
> - IP-Header-Aufbau (IPv4)
> - Subnetting-Berechnungen
> - Unterschied zwischen Routing und Switching
> - Private vs. öffentliche IP-Adressen

## Weiterführende Themen

- [[01-OSI-Modell]] - Einordnung im Schichtenmodell
- [[02-TCP-IP-Modell]] - Internetschicht
- [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] - Darunterliegende Schicht
- [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]] - Darüberliegende Schicht
