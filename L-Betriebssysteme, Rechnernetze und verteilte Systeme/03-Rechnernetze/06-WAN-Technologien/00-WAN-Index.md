---
author: Andreas Hümmer
title: WAN-Technologien
tags:
  - content
  - index
  - rn
  - wan
  - sd-wan
  - mpls
  - sase
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# WAN-Technologien

## Definition

> [!quote] Definition
> **Wide Area Network (WAN)**-Technologien verbinden geografisch verteilte Standorte über große Entfernungen. Dieses Kapitel behandelt moderne WAN-Architekturen und deren Evolution.
## Evolution der WAN-Technologien

```
┌─────────────────────────────────────────────────────────────────┐
│                WAN-Evolution                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1990er           2000er           2010er           2020er     │
│     │                │                │                │        │
│     ▼                ▼                ▼                ▼        │
│   ┌────┐          ┌────┐          ┌────┐          ┌────┐       │
│   │Frame│   →     │MPLS│    →     │Hybr.│   →     │SASE│       │
│   │Relay│          │    │          │WAN │          │    │       │
│   │ATM  │          │    │          │SD- │          │    │       │
│   └────┘          └────┘          │WAN │          └────┘       │
│                                    └────┘                       │
│                                                                  │
│   Dediziert  →  Provider-Managed  →  Software-Defined  →  Cloud │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Technologien im Vergleich

| Technologie | Typ | Kosten | Flexibilität | Sicherheit |
|-------------|-----|--------|--------------|------------|
| **MPLS** | Provider-Managed | Hoch | Niedrig | Hoch (privat) |
| **Internet VPN** | Self-Managed | Niedrig | Mittel | Mittel-Hoch |
| **SD-WAN** | Software-Defined | Mittel | Hoch | Hoch |
| **SASE** | Cloud-Native | Mittel-Hoch | Sehr hoch | Sehr hoch |

## Inhaltsverzeichnis

1. [[01-MPLS]] - Multiprotocol Label Switching (klassisch)
2. [[02-SD-WAN]] - Software-Defined WAN
3. [[03-SASE]] - Secure Access Service Edge

## Architekturvergleich

```
┌─────────────────────────────────────────────────────────────────┐
│                Traditionelles WAN vs. SD-WAN                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Traditionell (MPLS)                                           │
│   ┌─────────┐         ┌─────────┐         ┌─────────┐          │
│   │Standort │─────────│  MPLS   │─────────│Standort │          │
│   │   A     │         │Provider │         │   B     │          │
│   └─────────┘         │Backbone │         └─────────┘          │
│                       └─────────┘                               │
│   • Teuer, aber garantierte QoS                                │
│   • Lange Bereitstellungszeiten                                │
│   • Inflexibel bei Änderungen                                  │
│                                                                  │
│   ─────────────────────────────────────────────────────────    │
│                                                                  │
│   SD-WAN                                                        │
│   ┌─────────┐    ┌──────────────────────┐    ┌─────────┐       │
│   │Standort │    │      SD-WAN          │    │Standort │       │
│   │   A     │────│    Controller        │────│   B     │       │
│   │         │    │    (Orchestrator)    │    │         │       │
│   └────┬────┘    └──────────────────────┘    └────┬────┘       │
│        │                                          │             │
│   ┌────┴─────────────────────────────────────────┴────┐        │
│   │  MPLS │ Internet │ LTE/5G │ Starlink │ ...       │        │
│   │  (Underlay - mehrere Transportwege)               │        │
│   └───────────────────────────────────────────────────┘        │
│   • Multi-Path, automatisches Failover                         │
│   • Zentrale Verwaltung, schnelle Änderungen                   │
│   • Nutzung günstiger Internet-Leitungen                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## SASE-Konzept

```
┌─────────────────────────────────────────────────────────────────┐
│            SASE = SD-WAN + Security (Cloud-Native)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────────┐                      │
│                    │     SASE Cloud      │                      │
│                    │  ┌───────────────┐  │                      │
│                    │  │ SD-WAN        │  │                      │
│                    │  │ ZTNA          │  │                      │
│                    │  │ SWG           │  │                      │
│                    │  │ CASB          │  │                      │
│                    │  │ FWaaS         │  │                      │
│                    │  └───────────────┘  │                      │
│                    └──────────┬──────────┘                      │
│                               │                                  │
│         ┌─────────────────────┼─────────────────────┐           │
│         ▼                     ▼                     ▼           │
│    ┌─────────┐          ┌─────────┐          ┌─────────┐       │
│    │ Büro    │          │ Remote  │          │ Cloud   │       │
│    │         │          │ User    │          │ Apps    │       │
│    └─────────┘          └─────────┘          └─────────┘       │
│                                                                  │
│   ZTNA = Zero Trust Network Access                             │
│   SWG  = Secure Web Gateway                                    │
│   CASB = Cloud Access Security Broker                          │
│   FWaaS = Firewall as a Service                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - Unterschied MPLS vs. SD-WAN
> - Was ist das Overlay/Underlay-Konzept?
> - SASE-Komponenten (ZTNA, SWG, CASB)
> - Warum SD-WAN? (Kosten, Flexibilität, Multi-Cloud)

## Zusammenhänge

- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] - VPN als Teil von SD-WAN
- [[../05-Sicherheit/04-Overlay-Netzwerke/00-Overlay-Index|Overlay-Netzwerke]] - Verwandte Konzepte
- [[../03-Referenzmodelle/06-Netzwerkschicht/02-Routing|Routing]] - Grundlagen

