---
author: Andreas Hümmer
title: IP-Protokoll
tags:
  - content
  - rn
  - network-layer
  - ip
  - ipv4
  - adressierung
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---

# IP-Protokoll

## Definition

Das Internet Protocol (IP) ist das zentrale Protokoll der Netzwerkschicht für die Adressierung und Weiterleitung von Paketen.

## Erklärung

IP ermöglicht die netzwerkübergreifende Kommunikation durch eindeutige Adressen und Routing. IPv4 verwendet 32-Bit-Adressen, während IPv6 128-Bit-Adressen nutzt. IP ist verbindungslos und unzuverlässig (Best-Effort).

## Eigenschaften

- IPv4: 32-Bit-Adressen (ca. 4,3 Milliarden)
- Verbindungslos und paketorientiert
- Best-Effort-Zustellung
- TTL zur Vermeidung von Endlosschleifen

## Beispiele

- IPv4-Adresse: 192.168.1.1
- Subnetzmaske: 255.255.255.0 (/24)
- Private Adressbereiche: 10.x.x.x, 172.16-31.x.x, 192.168.x.x

## Zusammenhänge

- [[Routing]]
- [[IPv6]]
- [[TCP]]
- [[UDP]]

## Prüfungstipps

- IP-Header-Aufbau verstehen
- Subnetting und CIDR-Notation
- Unterschied öffentliche vs. private Adressen

## Quellen

- *Quelle 1*
