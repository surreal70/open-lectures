---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - protokolle
bereich: RN
---

# Basis-Netzwerkprotokolle und Dienste

## Übersicht

Dieses Kapitel behandelt fundamentale Netzwerkprotokolle und Dienste, die für den Betrieb von IP-Netzwerken unerlässlich sind.

```
┌─────────────────────────────────────────────────────────────────┐
│           Basis-Netzwerkprotokolle und Dienste                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │      ARP         │    │      DHCP        │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ IP → MAC         │    │ Automatische     │                  │
│   │ Adressauflösung  │    │ IP-Konfiguration │                  │
│   │ Layer 2/3        │    │ Layer 3/7        │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │      DNS         │    │      NTP         │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ Namensauflösung  │    │ Zeitsynchroni-   │                  │
│   │ Hierarchisch     │    │ sation           │                  │
│   │ Layer 7          │    │ Layer 7          │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐                                          │
│   │  SPANNING TREE   │                                          │
│   ├──────────────────┤                                          │
│   │ Schleifenver-    │                                          │
│   │ meidung          │                                          │
│   │ Layer 2          │                                          │
│   └──────────────────┘                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Inhaltsverzeichnis

| Nr. | Protokoll | Beschreibung | Schicht |
|-----|-----------|--------------|---------|
| 01 | [[01-ARP\|ARP]] | Address Resolution Protocol – IP zu MAC | 2/3 |
| 02 | [[02-DHCP\|DHCP]] | Dynamic Host Configuration Protocol | 3/7 |
| 03 | [[03-DNS\|DNS]] | Domain Name System | 7 |
| 04 | [[04-NTP\|NTP]] | Network Time Protocol | 7 |
| 05 | [[05-Spanning-Tree\|Spanning Tree]] | Schleifenvermeidung in L2-Netzen | 2 |

## Einordnung

Diese Protokolle bilden das **Fundament** für den praktischen Betrieb von Netzwerken:

- **ARP**: Ermöglicht die Kommunikation zwischen IP-Schicht und Ethernet
- **DHCP**: Automatisiert die Netzwerkkonfiguration von Endgeräten
- **DNS**: Übersetzt menschenlesbare Namen in IP-Adressen
- **NTP**: Synchronisiert Systemuhren – kritisch für Logs, Zertifikate, Authentifizierung
- **Spanning Tree**: Verhindert Broadcast-Stürme in geswitchten Netzen

## Zusammenhänge

- [[../03-Referenzmodelle/05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – ARP und STP arbeiten hier
- [[../03-Referenzmodelle/06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] – IP-Adressen, die ARP auflöst
- [[../03-Referenzmodelle/08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] – DNS, DHCP, NTP
