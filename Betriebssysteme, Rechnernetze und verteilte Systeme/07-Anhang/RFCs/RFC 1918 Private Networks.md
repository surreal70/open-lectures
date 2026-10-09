---
title: "RFC 1918 - Address Allocation for Private Internets"
rfc_number: 1918
version: "February 1996"
status: Best Current Practice
author: "Y. Rekhter, B. Moskowitz, D. Karrenberg, G. J. de Groot, E. Lear"
obsoletes: "RFC 1627, RFC 1597"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - ipv4
  - private-networks
  - nat
---

# RFC 1918 - Adresszuweisung für private Internets

## Überblick

RFC 1918 definiert drei Blöcke von IPv4-Adressraum, die für private Internets reserviert sind. Diese Adressen sind im öffentlichen Internet nicht routbar und können von jeder Organisation ohne Koordination mit der IANA verwendet werden.

## Zusammenfassung

Privater Adressraum ermöglicht Organisationen die interne Verwendung von IP-Adressen ohne Verbrauch global eindeutiger Adressen:

- **Adresskonservierung**: Reduziert den Bedarf an öffentlichen IPv4-Adressen
- **Keine Registrierung erforderlich**: Freie Nutzung ohne Koordination
- **Nicht routbar**: Erfordert NAT für Internetzugang
- **Wiederverwendbar**: Gleiche Adressen können von mehreren Organisationen verwendet werden

## Private Adressbereiche

| Bereich | CIDR | Adressanzahl | Klasse |
|---------|------|--------------|--------|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | 16.777.216 | Klasse A |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 1.048.576 | Klasse B |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 65.536 | Klasse C |

- Hetzner-Zuweisung: 10.10.96.0/19
- Grossheide-Zuweisung: 10.10.64.0/19
- VPN-Transfer: 172.16.100.0/22

| Netzwerk | Verwendung |
|----------|------------|
| 10.10.0.0/16 | Primäres internes Netzwerk |
| 10.11.0.0/16 | Hetzner Private Cloud |
| 172.16.100.0/22 | VPN-Transfernetzwerk |

## Offizielles Dokument

**RFC 1918**: [https://www.rfc-editor.org/rfc/rfc1918](https://www.rfc-editor.org/rfc/rfc1918)

## Verwandte RFCs

- [[RFC 791 IPv4]] - Internet Protocol
- [[RFC 6890 Special-Purpose Addresses]] - Sonderzweck-Adressregister
- [[RFC 4193 Unique Local IPv6]] - Unique Local IPv6 Unicast Addresses (IPv6-Äquivalent)
