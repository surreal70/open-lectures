---
author: Andreas Hümmer
title: Overlay-Netzwerke
tags:
  - content
  - index
  - rn
  - sicherheit
  - overlay
  - mesh
  - p2p
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Overlay-Netzwerke

## Definition

**Overlay-Netzwerke** sind virtuelle Netzwerke, die über einem bestehenden Netzwerk (Underlay) aufgebaut werden. Sie kombinieren VPN-Technologien mit Mesh-Topologien, zentraler Verwaltung und oft Zero-Trust-Prinzipien.

## Abgrenzung zu klassischen VPNs

```
┌─────────────────────────────────────────────────────────────────┐
│            Klassisches VPN vs. Overlay-Netzwerk                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Klassisches VPN (z.B. IPsec, OpenVPN)                        │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Hub-and-Spoke oder Site-to-Site                       │  │
│   │ • Manuelle Konfiguration der Peers                      │  │
│   │ • Statische Tunnel-Definitionen                         │  │
│   │ • Fokus auf Protokoll/Verschlüsselung                   │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Overlay-Netzwerk (z.B. Tailscale, ZeroTier)                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Automatisches Mesh zwischen allen Peers               │  │
│   │ • Zentrale Koordination, dezentrale Datenebene         │  │
│   │ • Dynamische Peer-Discovery                             │  │
│   │ • Identity-basierte Zugriffskontrolle                   │  │
│   │ • NAT-Traversal automatisch                             │  │
│   │ • Oft Zero-Trust-Prinzipien integriert                  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Architekturprinzip

```
┌─────────────────────────────────────────────────────────────────┐
│                    Overlay-Architektur                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │ Control Plane   │                          │
│                    │ (Koordination)  │                          │
│                    │ • Key Exchange  │                          │
│                    │ • Peer Discovery│                          │
│                    │ • ACL/Policy    │                          │
│                    └────────┬────────┘                          │
│                             │                                    │
│              ┌──────────────┼──────────────┐                    │
│              │              │              │                    │
│              ▼              ▼              ▼                    │
│        ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│        │  Peer A │◄══►│  Peer B │◄══►│  Peer C │              │
│        └─────────┘    └─────────┘    └─────────┘              │
│              ▲                              ▲                   │
│              └──────────────════════════────┘                   │
│                                                                  │
│        Data Plane: Direkter P2P-Traffic (wenn möglich)         │
│        Fallback: Relay über DERP/Root-Server                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Overlay-Lösungen im Vergleich

| Lösung | Basis-VPN | Layer | Besonderheit | Lizenz |
|--------|-----------|-------|--------------|--------|
| [[01-Tailscale\|Tailscale]] | WireGuard | 3 | SSO-Integration, MagicDNS | Proprietär (Freemium) |
| [[02-ZeroTier\|ZeroTier]] | Eigenes | 2 | Virtuelles Ethernet, SDN | BSL / Proprietär |
| [[03-Nebula\|Nebula]] | Eigenes (Noise) | 3 | Lighthouse-Konzept | MIT |
| [[04-Headscale\|Headscale]] | WireGuard | 3 | Open-Source Tailscale-kompatibel | BSD |
| Tinc | Eigenes | 2/3 | Älteres Mesh-VPN | GPL |

## Inhaltsverzeichnis

1. [[01-Tailscale]] - WireGuard-basiertes Mesh mit SSO
2. [[02-ZeroTier]] - Virtuelles Layer-2-Netzwerk
3. [[03-Nebula]] - Slack's Open-Source Mesh-VPN
4. [[04-Headscale]] - Self-hosted Tailscale Control Server

## Anwendungsfälle

```
┌─────────────────────────────────────────────────────────────────┐
│                 Typische Anwendungsfälle                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Remote-Arbeit mit vielen verteilten Mitarbeitern           │
│   ✓ Multi-Cloud-Vernetzung                                     │
│   ✓ IoT-Geräte sicher verbinden                                │
│   ✓ Entwickler-Umgebungen (Zugriff auf Services)               │
│   ✓ Homelab-Vernetzung                                         │
│   ✓ Gaming (Alternative zu Hamachi)                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenhänge

- [[../02-VPN/00-VPN-Index|VPN]] - Zugrundeliegende Technologien
- [[../02-VPN/02-WireGuard|WireGuard]] - Basis für Tailscale
- [[../../06-WAN-Technologien/00-WAN-Index|WAN-Technologien]] - SD-WAN, SASE

