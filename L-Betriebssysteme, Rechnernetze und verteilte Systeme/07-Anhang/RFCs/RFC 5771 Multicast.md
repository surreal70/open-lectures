---
title: "RFC 5771 - IANA Guidelines for IPv4 Multicast Address Assignments"
rfc_number: 5771
version: "March 2010"
status: Best Current Practice
author: "M. Cotton, L. Vegoda, D. Meyer"
obsoletes: "RFC 3171"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - ipv4
  - multicast
  - igmp
---

# RFC 5771 - IPv4-Multicast-Adresszuweisungen

## Überblick

RFC 5771 definiert die Richtlinien für die IANA-Verwaltung des IPv4-Multicast-Adressraums (224.0.0.0/4). Multicast ermöglicht eine effiziente One-to-Many-Zustellung von Daten, bei der ein einzelnes Paket gleichzeitig an mehrere Empfänger zugestellt werden kann.

## Zusammenfassung

IP-Multicast bietet effiziente Gruppenkommunikation:

- **One-to-Many**: Einzelne Übertragung erreicht mehrere Empfänger
- **Bandbreiten-effizient**: Reduziert Netzwerklast im Vergleich zu mehreren Unicasts
- **Gruppenmitgliedschaft**: Hosts treten Multicast-Gruppen dynamisch bei/aus
- **IGMP**: Internet Group Management Protocol für Gruppenverwaltung

## Multicast-Adressbereiche

| Bereich | Beschreibung | Geltungsbereich |
|---------|--------------|-----------------|
| 224.0.0.0/24 | Local Network Control | Link-lokal, nicht weitergeleitet |
| 224.0.1.0/24 | Internetwork Control | Global routbar |
| 224.0.2.0 – 224.0.255.255 | AD-HOC Block I | Verschiedene Verwendungen |
| 224.1.0.0 – 224.1.255.255 | ST Multicast Groups | Experimentell |
| 224.2.0.0 – 224.2.255.255 | SDP/SAP Block | Sitzungsankündigungen |
| 224.3.0.0 – 224.4.255.255 | AD-HOC Block II | Verschiedene Verwendungen |
| 232.0.0.0/8 | Source-Specific Multicast | SSM |
| 233.0.0.0/8 | GLOP Block | AS-basierte Zuweisung |
| 234.0.0.0/8 | Unicast-Prefix-based | Organisations-lokal |
| 239.0.0.0/8 | Administratively Scoped | Privat/intern |

## Bekannte Multicast-Adressen

| Adresse | Name | Protokoll |
|---------|------|-----------|
| 224.0.0.1 | All Hosts | IGMP |
| 224.0.0.2 | All Routers | IGMP |
| 224.0.0.5 | OSPF All Routers | OSPF |
| 224.0.0.6 | OSPF DR Routers | OSPF |
| 224.0.0.9 | RIPv2 Routers | RIP |
| 224.0.0.18 | VRRP | VRRP |
| 224.0.0.22 | IGMPv3 | IGMP |
| 224.0.0.251 | mDNS | DNS-SD |
| 224.0.0.252 | LLMNR | Link-Local Multicast |

## IGMP (Internet Group Management Protocol)

| Version | RFC | Funktionen |
|---------|-----|------------|
| IGMPv1 | RFC 1112 | Grundlegendes Join/Leave |
| IGMPv2 | RFC 2236 | Leave-Group-Nachrichten |
| IGMPv3 | RFC 3376 | Quellfilterung (SSM) |
Multicast wird für verschiedene Infrastrukturprotokolle verwendet:
- OSPF-Routing (falls eingesetzt)
- mDNS/Bonjour für Service-Discovery

## Offizielles Dokument

**RFC 5771**: [https://www.rfc-editor.org/rfc/rfc5771](https://www.rfc-editor.org/rfc/rfc5771)

## Verwandte RFCs

- [[RFC 791 IPv4]] - Internet Protocol
- [[RFC 1112 IGMP]] - Host Extensions for IP Multicasting (IGMPv1)
- [[RFC 3376 IGMPv3]] - IGMPv3
- [[RFC 4604 SSM]] - Source-Specific Multicast
