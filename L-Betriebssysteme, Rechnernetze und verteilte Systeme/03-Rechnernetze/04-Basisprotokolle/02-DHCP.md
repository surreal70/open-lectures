---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - dhcp
  - layer3
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

Der DHCP-Prozess besteht aus vier Schritten (DORA):

1. **DHCPDISCOVER**: Ein Client ohne IP-Adresse sendet eine Broadcast-Anfrage nach Adress-Angeboten an alle DHCP-Server im lokalen Netz.

2. **DHCPOFFER**: Die DHCP-Server antworten mit entsprechenden Werten auf eine DHCPDISCOVER-Anfrage.

3. **DHCPREQUEST**: Der Client fordert eine der angebotenen IP-Adressen, weitere Daten sowie Verlängerung der Lease-Zeit von einem der antwortenden DHCP-Server.

4. **DHCPACK**: Bestätigung des DHCP-Servers zu einer DHCPREQUEST-Anforderung.

### Weitere DHCP-Nachrichten

| Nachricht | Beschreibung |
|-----------|--------------|
| **DHCPNAK** | Ablehnung einer DHCPREQUEST-Anforderung durch den DHCP-Server |
| **DHCPDECLINE** | Ablehnung durch den Client, da die IP-Adresse schon verwendet wird |
| **DHCPRELEASE** | Der Client gibt die eigene Konfiguration frei, damit die Parameter wieder für andere Clients zur Verfügung stehen |
| **DHCPINFORM** | Anfrage eines Clients nach weiteren Konfigurationsparametern, z.B. weil der Client eine statische IP-Adresse besitzt |

### Lease-Verwaltung

TODO: Lease-Zeit, Renewal (T1), Rebinding (T2)

### Portnummern

| Protokoll | Port | Verwendung |
|-----------|------|------------|
| UDP | 67 | IPv4 Server oder Relay Agent |
| UDP | 68 | IPv4 Client |
| UDP | 547 | IPv6 Server oder Relay Agent |
| UDP | 546 | IPv6 Client |

### DHCP-Optionen

Wichtige Server-Optionen (Auszug):
- **Time Server** (RFC 868) und NTP-Server
- **Name Server** (DNS)
- **Router** (Default Gateway)
- **Subnet Mask**
- **Domain Name**
- **Lease Time**

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
