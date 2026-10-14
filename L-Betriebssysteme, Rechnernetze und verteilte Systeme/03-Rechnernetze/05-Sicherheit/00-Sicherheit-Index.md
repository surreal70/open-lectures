---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - sicherheit
bereich: RN
---

# Netzwerksicherheit

## Übersicht

Dieses Kapitel behandelt Sicherheitskonzepte und -technologien in Rechnernetzen.

```
┌─────────────────────────────────────────────────────────────────┐
│                 Netzwerksicherheit                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │   FIREWALLS      │    │      VPN         │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • Paketfilter    │    │ • IPsec          │                  │
│   │ • Stateful       │    │ • WireGuard      │                  │
│   │ • Application    │    │ • OpenVPN        │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │      TLS         │    │  OVERLAY-NETZE   │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • HTTPS          │    │ • Tailscale      │                  │
│   │ • Zertifikate    │    │ • ZeroTier       │                  │
│   │ • Handshake      │    │ • Nebula         │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Inhaltsverzeichnis

1. [[01-Firewalls]] - Paketfilter, Stateful Inspection, Application Firewall
2. [[02-VPN/00-VPN-Index|VPN]] - Virtual Private Networks
   - [[02-VPN/01-IPsec|IPsec]] - Industriestandard
   - [[02-VPN/02-WireGuard|WireGuard]] - Modernes Protokoll
   - [[02-VPN/03-OpenVPN|OpenVPN]] - Open-Source-Lösung
   - [[02-VPN/04-SSL-VPN|SSL VPN]] - Browser-basiert
   - [[02-VPN/05-L2TP|L2TP]] - Layer 2 Tunneling
   - [[02-VPN/06-PPTP|PPTP]] - Veraltet (unsicher!)
   - [[02-VPN/07-Hamachi|Hamachi]] - Proprietäre P2P-Lösung
3. [[03-TLS]] - Transport Layer Security
4. [[04-Overlay-Netzwerke/00-Overlay-Index|Overlay-Netzwerke]] - Moderne P2P-Mesh-Lösungen
   - [[04-Overlay-Netzwerke/01-Tailscale|Tailscale]] - WireGuard-basiertes Mesh
   - [[04-Overlay-Netzwerke/02-ZeroTier|ZeroTier]] - Virtuelles Ethernet
   - [[04-Overlay-Netzwerke/03-Nebula|Nebula]] - Open-Source von Slack
   - [[04-Overlay-Netzwerke/04-Headscale|Headscale]] - Self-hosted Tailscale

## Zusammenhänge

- [[../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec (Netzwerkschicht)]] - Layer-3-Sicherheit
- [[../03-Referenzmodelle/08-Anwendungsschicht/02-HTTP|HTTPS]] - TLS für Web
