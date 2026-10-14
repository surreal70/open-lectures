---
author: Andreas Hümmer
title: Nebula
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - nebula
  - slack
  - mesh
  - open-source
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Nebula

## Definition

**Nebula** ist ein Open-Source Overlay-Netzwerk, das von Slack entwickelt wurde. Es nutzt das Noise-Protokoll für Verschlüsselung und ein einzigartiges "Lighthouse"-Konzept für die Peer-Discovery.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 3 (Netzwerk) |
| **Protokoll** | Noise Protocol Framework |
| **Verschlüsselung** | Curve25519, ChaCha20-Poly1305 |
| **Architektur** | Mesh mit Lighthouses |
| **Lizenz** | MIT (vollständig Open Source) |
| **Entwickler** | Slack (jetzt Salesforce) |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    Nebula-Architektur                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│            ┌───────────────────────────────┐                    │
│            │       Lighthouse(s)           │                    │
│            │  • Öffentliche IP             │                    │
│            │  • Peer-Discovery             │                    │
│            │  • NAT Hole Punching Helper   │                    │
│            │  (kein Traffic-Relay!)        │                    │
│            └───────────────┬───────────────┘                    │
│                            │                                    │
│              ┌─────────────┼─────────────┐                      │
│              ▼             ▼             ▼                      │
│         ┌────────┐    ┌────────┐    ┌────────┐                 │
│         │ Node A │◄══►│ Node B │◄══►│ Node C │                 │
│         │(hinter │    │(hinter │    │(öffentl│                 │
│         │  NAT)  │    │  NAT)  │    │  IP)   │                 │
│         └────────┘    └────────┘    └────────┘                 │
│                                                                  │
│   Alle Nodes sind gleichberechtigt (kein zentraler Relay)      │
│   Lighthouse hilft nur beim Finden, nicht beim Relaying        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Zertifikatsbasierte Identität

```
┌─────────────────────────────────────────────────────────────────┐
│                    Nebula PKI                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Certificate Authority (CA)                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Erstellt Root-Zertifikat (offline aufbewahren!)       │  │
│   │ • Signiert Node-Zertifikate                             │  │
│   │ • Definiert Gruppen und Netzwerk-Zugehörigkeit          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Node-Zertifikat enthält:                                      │
│   • Nebula-IP-Adresse                                          │
│   • Gruppenmitgliedschaften                                    │
│   • Gültigkeitszeitraum                                        │
│   • Public Key                                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Besonderheiten

<!-- TODO: Kein Traffic über Lighthouse -->
<!-- TODO: Firewall-Regeln im Zertifikat -->
<!-- TODO: Gruppen-basierte Zugriffskontrolle -->
<!-- TODO: Unsafe Routes für Subnet-Routing -->

## Prüfungsrelevante Themen

> [!info] Prüfungshinweis
> - Lighthouse ist kein Relay (Unterschied zu DERP/Root-Servern)
> - Zertifikatsbasierte vs. Account-basierte Identität
> - Vollständig dezentral nach initialem Handshake

## Zusammenhänge

- [[00-Overlay-Index]] - Overlay-Netzwerke
- [[01-Tailscale]] - Alternative mit managed Service
- [[../02-VPN/02-WireGuard|WireGuard]] - Ähnliches Verschlüsselungskonzept

## Quellen

- https://github.com/slackhq/nebula
- https://nebula.defined.net/docs/

