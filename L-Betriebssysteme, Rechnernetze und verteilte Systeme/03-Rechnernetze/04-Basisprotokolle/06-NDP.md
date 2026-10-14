---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - ndp
  - ipv6
  - layer3
bereich: RN
---

# NDP – Neighbor Discovery Protocol

## Lernziele

- [ ] NDP als IPv6-Ersatz für ARP verstehen
- [ ] NDP-Nachrichtentypen kennen
- [ ] SLAAC-Prozess erklären können
- [ ] Unterschiede zu ARP verstehen

## Überblick

Das **Neighbor Discovery Protocol (NDP)** ist der IPv6-Ersatz für ARP. Es nutzt ICMPv6 und bietet deutlich mehr Funktionalität als das klassische ARP.

```
┌─────────────────────────────────────────────────────────────┐
│                    NDP vs. ARP                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   IPv4 + ARP                      IPv6 + NDP                │
│   ──────────                      ──────────                │
│   • Nur Adressauflösung           • Adressauflösung         │
│   • Broadcast-basiert             • Router Discovery        │
│   • Einfach                       • Prefix Discovery        │
│   • Unsicher                      • SLAAC                   │
│                                   • DAD                     │
│                                   • Redirect                │
│                                   • Multicast-basiert       │
│                                   • Sicherer (SEND)         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] RFC-Referenz
> - NDP: [[A-RFC-Index#RFC 4861|RFC 4861]]
> - SLAAC: [[A-RFC-Index#RFC 4862|RFC 4862]]
> - SEND: [[A-RFC-Index#RFC 3971|RFC 3971]]

### ICMPv6-Nachrichtentypen

NDP verwendet folgende ICMPv6-Nachrichtentypen:

| Typ | Name | Beschreibung |
|-----|------|--------------|
| 133 | **Router Solicitation (RS)** | Host fragt nach Routern |
| 134 | **Router Advertisement (RA)** | Router kündigt sich an, liefert Prefix |
| 135 | **Neighbor Solicitation (NS)** | Entspricht ARP Request |
| 136 | **Neighbor Advertisement (NA)** | Entspricht ARP Reply |
| 137 | **Redirect** | Router leitet Host zu besserem Next-Hop um |

### Neighbor Discovery (Adressauflösung)

```
┌─────────────────────────────────────────────────────────────┐
│              NDP Neighbor Discovery                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Host A                                    Host B          │
│   fe80::1                                   fe80::2         │
│   MAC: AA:AA:...                           MAC: BB:BB:...   │
│                                                              │
│      │                                         │            │
│      │  Neighbor Solicitation (Multicast)      │            │
│      │  "Wer hat fe80::2?"                     │            │
│      │  Ziel: ff02::1:ff00:0002               │            │
│      │─────────────────────────────────────────>│            │
│      │                                         │            │
│      │  Neighbor Advertisement (Unicast)       │            │
│      │  "Ich (BB:BB:...) habe fe80::2"         │            │
│      │<─────────────────────────────────────────│            │
│      │                                         │            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> [!tip] Multicast statt Broadcast
> NDP nutzt **Solicited-Node Multicast** (`ff02::1:ffXX:XXXX`) statt Broadcast. Dadurch werden nur relevante Hosts angesprochen.

### Router Discovery

TODO: RS/RA-Austausch, Prefix-Information

### SLAAC (Stateless Address Autoconfiguration)

TODO: Automatische IPv6-Adresskonfiguration ohne DHCP

### Duplicate Address Detection (DAD)

TODO: Prüfung auf doppelte Adressen

## Neighbor Cache

TODO: Entspricht ARP-Cache, Zustände (REACHABLE, STALE, DELAY, PROBE)

## Sicherheit

### NDP-Spoofing

TODO: Ähnlich wie ARP-Spoofing

### SEND (Secure Neighbor Discovery)

TODO: Kryptographisch gesichertes NDP (RFC 3971)

### RA Guard

TODO: Schutz vor gefälschten Router Advertisements

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - NDP als IPv6-Ersatz für ARP
> - ICMPv6-Nachrichtentypen (RS, RA, NS, NA)
> - Multicast statt Broadcast
> - SLAAC-Grundprinzip

## Zusammenfassung

NDP ist ein mächtiger Ersatz für ARP in IPv6-Netzen. Es kombiniert Adressauflösung, Router Discovery und automatische Adresskonfiguration in einem Protokoll.

## Querverweise

- [[01-ARP|ARP]] – IPv4-Pendant
- [[../03-Referenzmodelle/06-Netzwerkschicht/03-IPv6|IPv6]] – Netzwerkschicht
- [[../03-Referenzmodelle/06-Netzwerkschicht/05-ICMP|ICMP]] – ICMPv6 ist die Basis für NDP
- [[02-DHCP|DHCP]] – Alternative zu SLAAC (DHCPv6)
