---
author: Andreas Hümmer
title: SASE - Secure Access Service Edge
tags:
  - content
  - rn
  - wan
  - sase
  - zero-trust
  - cloud
  - ztna
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# SASE - Secure Access Service Edge

> [!info] Lernziele
> - Verstehen des SASE-Konzepts als Kombination von Netzwerk und Sicherheit
> - Kennenlernen der SASE-Komponenten (ZTNA, SWG, CASB, FWaaS)
> - Unterscheiden zwischen SSE (Security Service Edge) und SD-WAN als SASE-Bausteine
> - Verstehen des Zero-Trust-Prinzips bei SASE
> - Kennen der Vorteile Cloud-nativer Sicherheitsarchitekturen

## Definition

> [!quote] Definition
> **SASE (Secure Access Service Edge)**, ausgesprochen "sassy", ist ein von Gartner 2019 definiertes Cloud-Architekturmodell, das Netzwerk- und Sicherheitsfunktionen in einem einheitlichen, Cloud-nativen Service kombiniert.
## Komponenten

```
┌─────────────────────────────────────────────────────────────────┐
│                    SASE-Komponenten                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Netzwerk (WAN Edge)          Sicherheit (SSE)                │
│   ┌─────────────────────┐      ┌─────────────────────┐         │
│   │                     │      │                     │         │
│   │  • SD-WAN           │      │  • ZTNA             │         │
│   │  • WAN Optimization │      │  • SWG              │         │
│   │  • QoS              │      │  • CASB             │         │
│   │  • Routing          │      │  • FWaaS            │         │
│   │                     │      │  • DLP              │         │
│   │                     │      │  • Threat Protection│         │
│   │                     │      │                     │         │
│   └──────────┬──────────┘      └──────────┬──────────┘         │
│              │                            │                     │
│              └────────────┬───────────────┘                     │
│                           │                                     │
│              ┌────────────▼────────────┐                       │
│              │     SASE Platform       │                       │
│              │   (Cloud-Native)        │                       │
│              └─────────────────────────┘                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Komponenten erklärt

| Abkürzung | Name | Funktion |
|-----------|------|----------|
| **ZTNA** | Zero Trust Network Access | Identity-basierter Zugriff, ersetzt VPN |
| **SWG** | Secure Web Gateway | Web-Filterung, Malware-Schutz |
| **CASB** | Cloud Access Security Broker | Sicherheit für Cloud-Apps (SaaS) |
| **FWaaS** | Firewall as a Service | Cloud-basierte Firewall |
| **DLP** | Data Loss Prevention | Schutz vor Datenverlust |

## ZTNA - Zero Trust Network Access

```
┌─────────────────────────────────────────────────────────────────┐
│               ZTNA vs. Traditional VPN                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Traditional VPN                                               │
│   ┌────────┐        ┌────────────────────────────────┐         │
│   │ User   │───VPN──│        Netzwerk                │         │
│   │        │Tunnel  │   (Vollständiger Zugriff)      │         │
│   └────────┘        └────────────────────────────────┘         │
│   Problem: Einmal drin = Zugriff auf alles                     │
│                                                                  │
│   ─────────────────────────────────────────────────────────    │
│                                                                  │
│   ZTNA (Zero Trust)                                             │
│   ┌────────┐        ┌─────────────────┐    ┌─────────┐         │
│   │ User   │───────►│  ZTNA Broker    │───►│ App A   │         │
│   │        │Identity│  • Wer?         │    └─────────┘         │
│   │        │Context │  • Was?         │                        │
│   └────────┘        │  • Wie?         │    ┌─────────┐         │
│                     │  • Woher?       │───►│ App B   │         │
│                     └─────────────────┘    └─────────┘         │
│   Prinzip: "Never trust, always verify"                        │
│   Zugriff nur auf autorisierte Anwendungen                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Architekturprinzipien

<!-- TODO: Identity-Centric -->
<!-- TODO: Cloud-Native -->
<!-- TODO: Globale Edge-Präsenz -->
<!-- TODO: Single-Pass Architecture -->

## Anbieter

<!-- TODO: Zscaler (ZIA, ZPA) -->
<!-- TODO: Palo Alto Prisma Access -->
<!-- TODO: Cisco Umbrella -->
<!-- TODO: Cloudflare One -->
<!-- TODO: Netskope -->

## SASE vs. SSE

<!-- TODO: SSE = Security Service Edge (ohne SD-WAN) -->
<!-- TODO: Gartner Kategorien -->

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - SASE-Komponenten (ZTNA, SWG, CASB, FWaaS)
> - Zero Trust Prinzip erklärt
> - Warum Cloud-Native wichtig ist
> - Unterschied SASE vs. SSE

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[02-SD-WAN]] - Netzwerk-Komponente
- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] - ZTNA ersetzt VPN teilweise

## Quellen

- Gartner: "The Future of Network Security Is in the Cloud" (2019)
- Gartner SASE/SSE Magic Quadrant

