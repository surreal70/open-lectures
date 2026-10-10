---
title: "RFC 8200 - Internet Protocol Version 6 (IPv6)"
rfc_number: 8200
version: "July 2017"
status: Internet Standard
author: "S. Deering, R. Hinden"
obsoletes: "RFC 2460"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - ipv6
  - internet-protocol
---

# RFC 8200 - Internet Protocol Version 6 (IPv6)

## Überblick

RFC 8200 spezifiziert Version 6 des Internet Protocols (IPv6), das als Nachfolger von IPv4 entwickelt wurde. IPv6 bietet einen deutlich größeren Adressraum und enthält Verbesserungen für Routing-Effizienz, Sicherheit und Autokonfiguration.

## Zusammenfassung

IPv6 wurde entwickelt, um die IPv4-Adresserschöpfung zu adressieren und enthält mehrere Verbesserungen:

- **Erweiterte Adressierung**: 128-Bit-Adressen (vs. 32-Bit bei IPv4)
- **Vereinfachter Header**: Fester 40-Byte-Header für schnellere Verarbeitung
- **Erweiterungsheader**: Modularer Ansatz für optionale Funktionen
- **Flow-Kennzeichnung**: Unterstützung für QoS und Echtzeit-Anwendungen
- **Integrierte Sicherheit**: IPsec-Unterstützung in der Originalspezifikation obligatorisch
- **Autokonfiguration**: Stateless Address Autoconfiguration (SLAAC)

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Adresslänge | 128 Bit (16 Oktette) |
| Header-Länge | Fest 40 Bytes |
| Adressnotation | Acht Gruppen von vier hexadezimalen Ziffern |
| Loopback | ::1 |
| Link-Local Präfix | fe80::/10 |
IPv6-Bereitschaft wird für zukünftige Netzwerkerweiterung berücksichtigt:

## Offizielles Dokument

**RFC 8200**: [https://www.rfc-editor.org/rfc/rfc8200](https://www.rfc-editor.org/rfc/rfc8200)

## Verwandte RFCs

- [[RFC 791 IPv4]] - Internet Protocol Version 4
- [[RFC 4291 IPv6 Addressing]] - IP Version 6 Addressing Architecture
- [[RFC 4862 IPv6 SLAAC]] - IPv6 Stateless Address Autoconfiguration
