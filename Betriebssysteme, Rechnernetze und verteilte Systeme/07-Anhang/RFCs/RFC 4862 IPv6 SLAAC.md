---
title: "RFC 4862 - IPv6 Stateless Address Autoconfiguration"
rfc_number: 4862
version: "September 2007"
status: Draft Standard
author: "S. Thomson, T. Narten, T. Jinmei"
obsoletes: "RFC 2462"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ipv6
  - slaac
  - autoconfiguration
---

# RFC 4862 - IPv6 SLAAC

## Überblick

RFC 4862 definiert Stateless Address Autoconfiguration (SLAAC), ein Verfahren zur automatischen IPv6-Adresskonfiguration ohne DHCP-Server.

## Zusammenfassung

SLAAC-Funktionen:

- **Stateless**: Keine Statusverwaltung auf dem Router
- **Präfix-Discovery**: Router Advertisement (RA)
- **Interface ID**: Aus MAC-Adresse oder Privacy Extensions
- **DAD**: Duplicate Address Detection
- **Lifetime**: Gültigkeitsdauern für Adressen

## SLAAC-Prozess

```
1. Host generiert Link-Local-Adresse (fe80::)
2. Host führt DAD durch
3. Router sendet Router Advertisement mit Präfix
4. Host bildet globale Adresse: Präfix + Interface ID
5. Host führt DAD für globale Adresse durch
6. Adresse wird verwendet
```

## Router Advertisement Flags

| Flag | Beschreibung |
|------|--------------|
| M (Managed) | DHCPv6 für Adressen verwenden |
| O (Other) | DHCPv6 für andere Konfiguration |
| A (Autonomous) | SLAAC erlaubt |
| L (On-Link) | Präfix ist on-link |

## Offizielles Dokument

**RFC 4862**: [https://www.rfc-editor.org/rfc/rfc4862](https://www.rfc-editor.org/rfc/rfc4862)

## Verwandte RFCs

- [[RFC 8200 IPv6]] - IPv6-Spezifikation
- [[RFC 4291 IPv6 Addressing]] - IPv6-Adressierungsarchitektur
- [[RFC 4941 Privacy Extensions]] - Temporäre Adressen
