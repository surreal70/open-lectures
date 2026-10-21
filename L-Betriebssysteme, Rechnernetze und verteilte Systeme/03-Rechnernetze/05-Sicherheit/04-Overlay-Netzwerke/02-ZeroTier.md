---
author: Andreas Hümmer
title: ZeroTier
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - zerotier
  - sdn
  - layer2
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# ZeroTier

## Definition

> [!quote] Definition
> **ZeroTier** ist eine Overlay-Netzwerk-Lösung, die ein virtuelles Layer-2-Netzwerk über das Internet erstellt. Anders als WireGuard-basierte Lösungen emuliert ZeroTier ein vollständiges Ethernet-Netzwerk mit Broadcast-Support.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 2 (Sicherung) – virtuelles Ethernet |
| **Protokoll** | Eigenes (ZeroTier Protocol) |
| **Verschlüsselung** | Curve25519, Salsa20, Poly1305 |
| **Architektur** | P2P-Mesh mit Root-Servern |
| **Network-ID** | 16-stellige Hex-ID |
| **Lizenz** | BSL (Business Source License) |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    ZeroTier-Architektur                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │  ZeroTier       │                          │
│                    │  Root Servers   │                          │
│                    │  (Planet)       │                          │
│                    └────────┬────────┘                          │
│                             │                                    │
│              ┌──────────────┼──────────────┐                    │
│              ▼              ▼              ▼                    │
│        ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│        │  Node A │    │  Node B │    │  Node C │              │
│        │zt-iface │    │zt-iface │    │zt-iface │              │
│        └────┬────┘    └────┬────┘    └────┬────┘              │
│             │              │              │                     │
│             └──────────════┴══════════════┘                     │
│                  Virtuelles Layer-2-Netzwerk                   │
│                  (wie ein Switch)                               │
│                                                                  │
│   Ethernet-Frames werden über UDP/443 getunnelt                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Besonderheiten

<!-- TODO: Layer 2 vs. Layer 3 -->
<!-- TODO: Broadcast/Multicast-Support -->
<!-- TODO: Managed Routes und Flow Rules -->
<!-- TODO: Self-Hosted Controller -->
<!-- TODO: Moon (eigene Root-Server) -->

## Network Controller

<!-- TODO: ZeroTier Central (Cloud) -->
<!-- TODO: Self-Hosted Controller -->
<!-- TODO: Network Rules Engine -->

## Prüfungsrelevante Themen

> [!info] Prüfungshinweis
> - Unterschied Layer-2 (ZeroTier) vs. Layer-3 (Tailscale)
> - Wann braucht man Broadcast-Support?
> - Planet vs. Moon (Root-Server-Konzept)

## Zusammenhänge

- [[00-Overlay-Index]] - Overlay-Netzwerke
- [[01-Tailscale]] - Alternative (Layer 3)
- [[../02-VPN/07-Hamachi|Hamachi]] - Ähnliches Konzept (proprietär)

## Quellen

- https://www.zerotier.com/
- https://docs.zerotier.com/

