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
modified: '2026-10-24'
bereich: RN
---

# WAN-Technologien

## Definition

> [!quote] Definition
> **Wide Area Network (WAN)**-Technologien verbinden geografisch verteilte Standorte über große Entfernungen. Dieses Kapitel behandelt moderne WAN-Architekturen und deren Evolution.
## Evolution der WAN-Technologien

![[wan-evolution.png]]
*<span class="fig-id">03-06-00-wan-evolution</span>: Entwicklung der WAN-Technologien von Frame Relay/ATM über MPLS und SD-WAN bis zu SASE.*

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

![[wan-vs-sdwan.png]]
*<span class="fig-id">03-06-00-wan-vs-sdwan</span>: Vergleich traditioneller MPLS-basierter WANs mit softwaredefinierten SD-WAN-Architekturen.*

## SASE-Konzept

![[sase-concept.png]]
*<span class="fig-id">03-06-00-sase-concept</span>: SASE kombiniert SD-WAN mit Cloud-nativen Sicherheitsdiensten (ZTNA, SWG, CASB, FWaaS).*

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
NA

---

## Prüfungstipps

> [!warning] Häufige Fehler
> - MPLS und SD-WAN verwechseln: MPLS ist provider-managed, SD-WAN ist software-defined
> - Overlay/Underlay-Konzept nicht verstehen: Overlay ist das logische Netz, Underlay der physische Transport
> - SASE-Komponenten nicht kennen: ZTNA, SWG, CASB, FWaaS

> [!question] Typische Prüfungsfragen
> - Erklären Sie den Unterschied zwischen traditionellem WAN und SD-WAN
> - Was versteht man unter SASE und welche Komponenten gehören dazu?
> - Warum ist SD-WAN flexibler als MPLS?
> - Was bedeutet "Underlay" und "Overlay" im Kontext von SD-WAN?

> [!tip] Lernstrategie
> - Die Evolution verstehen: Dediziert → Provider-Managed → Software-Defined → Cloud
> - Fokus auf Kosten-Flexibilität-Trade-off zwischen den Technologien
> - SASE als Konvergenz von Netzwerk und Security begreifen

---

## Weiterführende Ressourcen

- [Gartner: Magic Quadrant for SD-WAN](https://www.gartner.com/en/documents/sd-wan) - Marktübersicht SD-WAN-Anbieter
- [Cisco SD-WAN Documentation](https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html)
- [SASE Architecture (Gartner)](https://www.gartner.com/en/information-technology/glossary/secure-access-service-edge-sase)

---

## Zusammenhänge

- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] - VPN als Teil von SD-WAN
- [[../05-Sicherheit/04-Overlay-Netzwerke/00-Overlay-Index|Overlay-Netzwerke]] - Verwandte Konzepte
- [[../03-Referenzmodelle/06-Netzwerkschicht/02-Routing|Routing]] - Grundlagen

---

## Quellen

- Tanenbaum, A. S., & Wetherall, D. J. (2021). *Computer Networks* (6th ed.). Pearson.
- Gartner (2019). *The Future of Network Security Is in the Cloud*. (SASE-Definition)
- MEF (2020). *SD-WAN Service Attributes and Service Framework*.

