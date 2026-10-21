---
author: Andreas Hümmer
title: SD-WAN - Software-Defined WAN
tags:
  - content
  - rn
  - wan
  - sd-wan
  - sdn
  - overlay
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# SD-WAN - Software-Defined WAN

> [!info] Lernziele
> - Verstehen des Overlay/Underlay-Konzepts bei SD-WAN
> - Kennenlernen der zentralen Steuerung über den SD-WAN Controller
> - Verstehen der Vorteile gegenüber traditionellem WAN (MPLS)
> - Kennen der unterstützten Transporttypen (MPLS, Internet, LTE/5G)
> - Verstehen von Application-aware Routing und QoS-Funktionen

## Definition

> [!quote] Definition
> **SD-WAN (Software-Defined Wide Area Network)** ist eine Architektur, die Software-Defined-Networking-Konzepte auf WAN-Verbindungen anwendet. Es abstrahiert die Transportschicht und ermöglicht zentrale Steuerung über verschiedene Verbindungstypen hinweg.
## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Architektur** | Overlay über beliebige Underlay-Netze |
| **Steuerung** | Zentraler Controller (Orchestrator) |
| **Transport** | MPLS, Internet, LTE/5G, Satellit, ... |
| **Verschlüsselung** | IPsec oder proprietär |
| **Management** | Cloud-basiert oder On-Premise |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    SD-WAN-Architektur                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                  ┌─────────────────────────┐                    │
│                  │    SD-WAN Controller    │                    │
│                  │    (Orchestrator)       │                    │
│                  │  • Zentrale Policies    │                    │
│                  │  • Monitoring           │                    │
│                  │  • Analytics            │                    │
│                  └───────────┬─────────────┘                    │
│                              │ Management Plane                 │
│              ┌───────────────┼───────────────┐                  │
│              ▼               ▼               ▼                  │
│        ┌──────────┐    ┌──────────┐    ┌──────────┐           │
│        │ SD-WAN   │    │ SD-WAN   │    │ SD-WAN   │           │
│        │ Edge     │    │ Edge     │    │ Edge     │           │
│        │ (Branch) │    │ (DC)     │    │ (Cloud)  │           │
│        └────┬─────┘    └────┬─────┘    └────┬─────┘           │
│             │               │               │                   │
│   ┌─────────┴───────────────┴───────────────┴─────────┐        │
│   │                    Underlay                        │        │
│   │  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  │        │
│   │  │  MPLS  │  │Internet│  │ LTE/5G │  │Starlink│  │        │
│   │  └────────┘  └────────┘  └────────┘  └────────┘  │        │
│   └───────────────────────────────────────────────────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Kernfunktionen

<!-- TODO: Dynamic Path Selection -->
<!-- TODO: Application-Aware Routing -->
<!-- TODO: WAN Optimization -->
<!-- TODO: Zero-Touch Provisioning -->
<!-- TODO: Segmentation -->

## SD-WAN vs. MPLS

| Aspekt | MPLS | SD-WAN |
|--------|------|--------|
| **Kosten** | Hoch | Niedriger |
| **Flexibilität** | Gering | Hoch |
| **Deployment-Zeit** | Wochen/Monate | Minuten/Stunden |
| **Multi-Cloud** | Schwierig | Native Unterstützung |
| **Sicherheit** | Provider-abhängig | Integriert |
| **QoS** | Garantiert | Anwendungsbasiert |

## Anbieter

<!-- TODO: Cisco Viptela/Meraki -->
<!-- TODO: VMware VeloCloud -->
<!-- TODO: Fortinet -->
<!-- TODO: Palo Alto Prisma -->
<!-- TODO: Zscaler -->

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - Overlay vs. Underlay erklärt
> - Warum ersetzt SD-WAN MPLS?
> - Application-Aware Routing Konzept
> - Zero-Touch Provisioning

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[01-MPLS]] - Traditionelle Alternative
- [[03-SASE]] - SD-WAN + Security
- [[../05-Sicherheit/02-VPN/01-IPsec|IPsec]] - Verschlüsselung

## Quellen

- Gartner SD-WAN Magic Quadrant
- Herstellerdokumentation

