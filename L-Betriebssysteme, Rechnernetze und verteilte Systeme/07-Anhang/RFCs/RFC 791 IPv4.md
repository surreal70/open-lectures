---
title: "RFC 791 - Internet Protocol (IPv4)"
rfc_number: 791
version: "September 1981"
status: Internet Standard
author: "J. Postel"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - ipv4
  - internet-protocol
---

# RFC 791 - Internet Protocol (IPv4)

## Überblick

RFC 791 definiert das Internet Protocol (IP), das grundlegende Kommunikationsprotokoll zur Weiterleitung von Datagrammen über Netzwerkgrenzen hinweg. IPv4 ist die vierte Version des Internet Protocols und bleibt das vorherrschende Protokoll für den Internetverkehr.

## Zusammenfassung

Das Internet Protocol stellt den grundlegenden Mechanismus für die Übertragung von Datagrammen von einem Quell- zu einem Zielhost bereit. Das Protokoll umfasst Vorkehrungen für:

- **Adressierung**: 32-Bit-Adressen zur Identifizierung von Quelle und Ziel
- **Fragmentierung**: Aufteilung von Datagrammen in kleinere Teile zur Übertragung
- **Diensttyp**: Parameter für Quality of Service
- **Time to Live (TTL)**: Begrenzung der Lebensdauer von Datagrammen zur Vermeidung von Schleifen
- **Optionen**: Erweiterte Funktionalität (Routing, Zeitstempel, Sicherheit)

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Adresslänge | 32 Bit (4 Oktette) |
| Header-Länge | 20-60 Bytes |
| Maximale Datagrammgröße | 65.535 Bytes |
| Standard-TTL | Implementierungsabhängig (typisch 64 oder 128) |

## Offizielles Dokument

**RFC 791**: [https://www.rfc-editor.org/rfc/rfc791](https://www.rfc-editor.org/rfc/rfc791)

## Verwandte RFCs

- [[RFC 8200 IPv6]] - Internet Protocol Version 6
- [[RFC 950 Subnetting]] - Internet Standard Subnetting Procedure
- [[RFC 1918 Private Networks]] - Address Allocation for Private Internets
