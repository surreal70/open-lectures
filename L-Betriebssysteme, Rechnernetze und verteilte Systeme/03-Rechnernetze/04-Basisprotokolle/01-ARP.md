---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - arp
  - layer2
bereich: RN
---

# ARP – Address Resolution Protocol

## Lernziele

- [ ] Zweck von ARP verstehen
- [ ] ARP-Request und ARP-Reply erklären können
- [ ] ARP-Cache und dessen Bedeutung kennen
- [ ] ARP-Spoofing als Sicherheitsrisiko verstehen

## Überblick

Das **Address Resolution Protocol (ARP)** löst IP-Adressen in MAC-Adressen auf. Es ist die Brücke zwischen Layer 3 (IP) und Layer 2 (Ethernet).

```
┌─────────────────────────────────────────────────────────────┐
│                    ARP-Funktionsprinzip                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Host A                                    Host B          │
│   IP: 192.168.1.10                         IP: 192.168.1.20 │
│   MAC: AA:AA:AA:AA:AA:AA                   MAC: BB:BB:BB:..│
│                                                              │
│      │                                         │            │
│      │  ARP Request (Broadcast)                │            │
│      │  "Wer hat 192.168.1.20?"                │            │
│      │─────────────────────────────────────────>│            │
│      │                                         │            │
│      │  ARP Reply (Unicast)                    │            │
│      │  "Ich (BB:BB:...) habe 192.168.1.20"    │            │
│      │<─────────────────────────────────────────│            │
│      │                                         │            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] RFC-Referenz
> ARP ist definiert in [[A-RFC-Index#RFC 826|RFC 826]] (1982).

### ARP-Request

TODO: Detaillierte Beschreibung des ARP-Request-Prozesses

### ARP-Reply

TODO: Detaillierte Beschreibung des ARP-Reply-Prozesses

### ARP-Cache

TODO: ARP-Cache-Verwaltung, Timeouts, Befehle (arp -a, ip neigh)

## ARP-Paketformat

TODO: ASCII-Darstellung des ARP-Paketformats

## Varianten

### Gratuitous ARP

TODO: Unsolicited ARP, Duplicate Address Detection

### Proxy ARP

TODO: Router antwortet im Namen anderer Hosts

### RARP (Reverse ARP)

TODO: Historisch – MAC zu IP (ersetzt durch BOOTP/DHCP)

## Sicherheit

### ARP-Spoofing

TODO: Angriffsszenario, Man-in-the-Middle

### Gegenmaßnahmen

TODO: Dynamic ARP Inspection (DAI), Static ARP Entries

## Praxisbeispiele

TODO: Kommandozeilen-Beispiele für Linux/Windows

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - ARP-Ablauf (Request/Reply)
> - Broadcast vs. Unicast
> - ARP-Cache
> - Sicherheitsrisiken

## Zusammenfassung

TODO: Kernpunkte zusammenfassen

## Querverweise

- [[../03-Referenzmodelle/05-Sicherungsschicht/02-MAC-Adressen|MAC-Adressen]]
- [[../03-Referenzmodelle/06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]]
- [[02-DHCP|DHCP]] – nutzt ARP für Duplicate Detection
