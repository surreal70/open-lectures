---
title: "RFC 6890 - Special-Purpose IP Address Registries"
rfc_number: 6890
version: "April 2013"
status: Best Current Practice
author: "M. Cotton, L. Vegoda, R. Bonica, B. Haberman"
obsoletes: "RFC 5735, RFC 5156"
obsoleted_by: ""
updated_by: "RFC 8190"
language: DE
tags:
  - rfc
  - networking
  - ipv4
  - ipv6
  - special-use
---

# RFC 6890 - Register für Sonderzweck-IP-Adressen

## Überblick

RFC 6890 konsolidiert die IANA IPv4- und IPv6-Register für Sonderzweck-Adressen und dokumentiert Adressblöcke, die für spezielle Zwecke zugewiesen wurden, wie private Netzwerke, Loopback, Dokumentation und mehr.

## Zusammenfassung

Sonderzweck-Adressen dienen spezifischen Funktionen:

- **Loopback**: Lokaler Host-Test
- **Private Nutzung**: Interne Netzwerke (RFC 1918)
- **Link-Local**: Autokonfiguration
- **Dokumentation**: Beispiele in Dokumentationen
- **Multicast**: One-to-Many-Zustellung
- **Broadcast**: Legacy One-to-All-Zustellung

## IPv4-Sonderzweck-Adressen

| Block | Name | RFC | Verwendung |
|-------|------|-----|------------|
| 0.0.0.0/8 | "This host" | RFC 1122 | Nur Quelle, lokales Netzwerk |
| 10.0.0.0/8 | Private-Use | RFC 1918 | Interne Netzwerke |
| 100.64.0.0/10 | Shared Address | RFC 6598 | Carrier-Grade NAT |
| 127.0.0.0/8 | Loopback | RFC 1122 | Host-Loopback |
| 169.254.0.0/16 | Link-Local | RFC 3927 | Autokonfiguration |
| 172.16.0.0/12 | Private-Use | RFC 1918 | Interne Netzwerke |
| 192.0.0.0/24 | IETF Protocol | RFC 6890 | IETF-Protokollzuweisungen |
| 192.0.2.0/24 | Documentation | RFC 5737 | TEST-NET-1 |
| 192.88.99.0/24 | 6to4 Relay | RFC 3068 | Anycast (veraltet) |
| 192.168.0.0/16 | Private-Use | RFC 1918 | Interne Netzwerke |
| 198.18.0.0/15 | Benchmarking | RFC 2544 | Netzwerkgeräte-Tests |
| 198.51.100.0/24 | Documentation | RFC 5737 | TEST-NET-2 |
| 203.0.113.0/24 | Documentation | RFC 5737 | TEST-NET-3 |
| 224.0.0.0/4 | Multicast | RFC 5771 | One-to-Many-Zustellung |
| 240.0.0.0/4 | Reserved | RFC 1112 | Zukünftige Nutzung |
| 255.255.255.255/32 | Limited Broadcast | RFC 919 | Lokaler Broadcast |

## Link-Local-Adressen (169.254.0.0/16)

Automatisch zugewiesen, wenn kein DHCP-Server verfügbar ist:
- Bereich: 169.254.1.0 – 169.254.254.255
- Nicht über die lokale Verbindung hinaus routbar
- Verwendet von APIPA (Windows), avahi/zeroconf (Linux)
Sonderadressen werden in der gesamten Infrastruktur verwendet:
- Loopback (127.0.0.1) für lokale Dienste

## Offizielles Dokument

**RFC 6890**: [https://www.rfc-editor.org/rfc/rfc6890](https://www.rfc-editor.org/rfc/rfc6890)

## Verwandte RFCs

- [[RFC 791 IPv4]] - Internet Protocol
- [[RFC 1918 Private Networks]] - Private Adresszuweisung
- [[RFC 5771 Multicast]] - Multicast-Adresszuweisung
- [[RFC 3927 Link-Local]] - IPv4 Link-Local-Adressen
