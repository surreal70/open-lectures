---
author: Andreas Hümmer
title: WireGuard
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - wireguard
  - modern
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# WireGuard

## Definition

**WireGuard** ist ein modernes, schlankes VPN-Protokoll, das auf Layer 3 arbeitet. Es zeichnet sich durch minimalen Code, hohe Geschwindigkeit und starke Kryptographie aus.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 3 (Netzwerk) |
| **Port** | UDP 51820 (Standard) |
| **Codezeilen** | ~4.000 (vs. ~400.000 bei OpenVPN) |
| **Kryptographie** | ChaCha20, Poly1305, Curve25519, BLAKE2s |
| **Kernel-Integration** | Ja (Linux seit 5.6) |

## Vorteile

<!-- TODO: Einfachheit und Auditierbarkeit -->
<!-- TODO: Geschwindigkeit und Latenz -->
<!-- TODO: Roaming-Unterstützung -->
<!-- TODO: Cryptokey Routing -->

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    WireGuard-Konzept                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Peer A                                           Peer B       │
│   ┌─────────────┐                           ┌─────────────┐    │
│   │ Public Key  │◄─────── Cryptokey ───────►│ Public Key  │    │
│   │ Private Key │         Routing           │ Private Key │    │
│   │ Allowed IPs │                           │ Allowed IPs │    │
│   └─────────────┘                           └─────────────┘    │
│                                                                  │
│   Kein Handshake-State, keine Zertifikate                      │
│   → Jeder Peer kennt Public Keys der anderen                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Konfiguration

<!-- TODO: Beispielkonfiguration -->
<!-- TODO: wg-quick Befehle -->

## Vergleich mit IPsec/OpenVPN

<!-- TODO: Performance-Vergleich -->
<!-- TODO: Komplexitätsvergleich -->

## Prüfungsrelevante Themen

> [!tip] Prüfungshinweis
> - Warum ist WireGuard schneller als IPsec/OpenVPN?
> - Cryptokey Routing Konzept
> - Verwendete Kryptographie-Algorithmen

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[01-IPsec]] - Klassischer Vergleich
- [[03-OpenVPN]] - Alternativer Ansatz

## Quellen

- https://www.wireguard.com/
- https://www.wireguard.com/papers/wireguard.pdf

