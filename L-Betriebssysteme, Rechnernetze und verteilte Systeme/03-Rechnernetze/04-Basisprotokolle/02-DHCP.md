---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - dhcp
  - layer7
bereich: RN
---

# DHCP – Dynamic Host Configuration Protocol

## Lernziele

- [ ] DHCP-Prozess (DORA) erklären können
- [ ] DHCP-Optionen kennen
- [ ] DHCP-Relay verstehen
- [ ] Lease-Konzept erklären können

## Überblick

Das **Dynamic Host Configuration Protocol (DHCP)** automatisiert die Netzwerkkonfiguration von Endgeräten. Es vergibt IP-Adressen, Subnetzmasken, Gateways und weitere Parameter.

```
┌─────────────────────────────────────────────────────────────┐
│                    DHCP-DORA-Prozess                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Client                                    DHCP-Server     │
│      │                                         │            │
│      │  1. DISCOVER (Broadcast)                │            │
│      │  "Gibt es einen DHCP-Server?"           │            │
│      │─────────────────────────────────────────>│            │
│      │                                         │            │
│      │  2. OFFER (Unicast/Broadcast)           │            │
│      │  "Hier ist IP 192.168.1.100"            │            │
│      │<─────────────────────────────────────────│            │
│      │                                         │            │
│      │  3. REQUEST (Broadcast)                 │            │
│      │  "Ich nehme 192.168.1.100"              │            │
│      │─────────────────────────────────────────>│            │
│      │                                         │            │
│      │  4. ACK (Unicast/Broadcast)             │            │
│      │  "Bestätigt, Lease: 24h"                │            │
│      │<─────────────────────────────────────────│            │
│      │                                         │            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] RFC-Referenz
> - DHCPv4: [[A-RFC-Index#RFC 2131|RFC 2131]]
> - DHCPv6: [[A-RFC-Index#RFC 8415|RFC 8415]]

### DORA-Prozess

TODO: Detaillierte Beschreibung der vier Schritte

### Lease-Verwaltung

TODO: Lease-Zeit, Renewal (T1), Rebinding (T2)

### DHCP-Optionen

TODO: Option 1 (Subnet Mask), Option 3 (Router), Option 6 (DNS), etc.

## Paketformat

TODO: DHCP-Paketstruktur (basiert auf BOOTP)

## DHCP-Relay

TODO: Relay-Agent für Netzwerke ohne lokalen DHCP-Server

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Client  │────>│  Relay   │────>│  DHCP    │
│          │     │  Agent   │     │  Server  │
└──────────┘     └──────────┘     └──────────┘
   Netz A           Router           Netz B
```

## DHCPv6

TODO: Unterschiede zu DHCPv4, Stateful vs. Stateless (SLAAC)

## Sicherheit

### DHCP-Starvation

TODO: Erschöpfung des Adresspools

### Rogue DHCP Server

TODO: Gefälschte DHCP-Server

### DHCP Snooping

TODO: Switch-basierte Absicherung

## Praxisbeispiele

TODO: Konfiguration Windows Server, ISC DHCP, dnsmasq

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - DORA-Prozess
> - Lease-Konzept (T1, T2)
> - DHCP-Relay
> - Wichtige DHCP-Optionen

## Zusammenfassung

TODO: Kernpunkte zusammenfassen

## Querverweise

- [[01-ARP|ARP]] – DHCP nutzt ARP für Duplicate Detection
- [[03-DNS|DNS]] – DHCP liefert DNS-Server-Adressen
- [[../03-Referenzmodelle/06-Netzwerkschicht/03-IPv6|IPv6]] – DHCPv6 vs. SLAAC
