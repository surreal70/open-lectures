---
author: Andreas Hümmer
title: Tailscale
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - tailscale
  - wireguard
  - mesh
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Tailscale

## Definition

**Tailscale** ist eine Overlay-Netzwerk-Lösung, die auf WireGuard basiert und ein automatisches Mesh-VPN mit zentraler Verwaltung bietet. Es kombiniert die Sicherheit von WireGuard mit einfacher Einrichtung und Identity-Management.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Basis** | WireGuard |
| **Layer** | 3 (Netzwerk) |
| **Architektur** | Mesh mit zentralem Control Plane |
| **Adressbereich** | 100.x.x.x (CGNAT-Bereich) |
| **Control Server** | Tailscale Coordination Server |
| **Lizenz** | Proprietär (Freemium) |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    Tailscale-Architektur                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│            ┌───────────────────────────────┐                    │
│            │  Tailscale Coordination Server │                    │
│            │  • Schlüsselaustausch          │                    │
│            │  • Peer-Discovery              │                    │
│            │  • ACLs                         │                    │
│            │  • MagicDNS                     │                    │
│            └───────────────┬───────────────┘                    │
│                            │ (nur Metadaten)                    │
│              ┌─────────────┼─────────────┐                      │
│              ▼             ▼             ▼                      │
│         ┌────────┐    ┌────────┐    ┌────────┐                 │
│         │ Node A │◄══►│ Node B │◄══►│ Node C │                 │
│         │100.x.1 │    │100.x.2 │    │100.x.3 │                 │
│         └────────┘    └────────┘    └────────┘                 │
│              ▲              ▲                                   │
│              └──────════════┘                                   │
│                WireGuard-Tunnel (direkt P2P)                   │
│                                                                  │
│   Falls P2P nicht möglich: DERP-Relay                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Kernkomponenten

<!-- TODO: Coordination Server -->
<!-- TODO: DERP (Designated Encrypted Relay for Packets) -->
<!-- TODO: MagicDNS -->
<!-- TODO: Tailscale SSH -->
<!-- TODO: ACLs und Tags -->

## Features

<!-- TODO: SSO-Integration (Google, Microsoft, GitHub, etc.) -->
<!-- TODO: Subnet Router -->
<!-- TODO: Exit Nodes -->
<!-- TODO: Taildrop (Dateiübertragung) -->

## Headscale-Alternative

Für Self-Hosting: [[04-Headscale]]

## Prüfungsrelevante Themen

> [!info] Prüfungshinweis
> - Unterschied Control Plane vs. Data Plane
> - Warum CGNAT-Bereich (100.64.0.0/10)?
> - NAT-Traversal-Techniken (STUN, DERP)

## Zusammenhänge

- [[00-Overlay-Index]] - Overlay-Netzwerke
- [[../02-VPN/02-WireGuard|WireGuard]] - Zugrundeliegendes Protokoll
- [[04-Headscale]] - Open-Source Control Server

## Quellen

- https://tailscale.com/
- https://tailscale.com/blog/how-tailscale-works/

