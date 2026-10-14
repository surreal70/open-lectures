---
author: Andreas Hümmer
title: Headscale
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - headscale
  - tailscale
  - self-hosted
  - open-source
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Headscale

## Definition

**Headscale** ist eine Open-Source-Implementierung des Tailscale Coordination Servers. Es ermöglicht Self-Hosting eines Tailscale-kompatiblen Netzwerks ohne Abhängigkeit von Tailscale's Cloud-Diensten.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Basis** | Tailscale-kompatibel (WireGuard) |
| **Layer** | 3 (Netzwerk) |
| **Architektur** | Self-hosted Control Plane |
| **Client** | Standard Tailscale-Client |
| **Lizenz** | BSD-3-Clause |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                 Headscale vs. Tailscale                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Tailscale (Cloud)              Headscale (Self-Hosted)        │
│   ┌─────────────────┐            ┌─────────────────┐           │
│   │ Tailscale       │            │ Headscale       │           │
│   │ Coordination    │            │ Server          │           │
│   │ Server          │            │ (self-hosted)   │           │
│   │ (SaaS)          │            │                 │           │
│   └────────┬────────┘            └────────┬────────┘           │
│            │                              │                     │
│   ┌────────┴────────┐            ┌────────┴────────┐           │
│   │ Tailscale       │            │ Tailscale       │           │
│   │ Clients         │            │ Clients         │           │
│   │ (unverändert)   │            │ (unverändert)   │           │
│   └─────────────────┘            └─────────────────┘           │
│                                                                  │
│   Gleiche Clients, anderer Control Server                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Features

<!-- TODO: User/Namespace-Management -->
<!-- TODO: Pre-Auth Keys -->
<!-- TODO: ACL-Unterstützung -->
<!-- TODO: DERP-Server (selbst betrieben) -->
<!-- TODO: DNS-Konfiguration -->

## Einschränkungen

<!-- TODO: Kein MagicDNS (teilweise) -->
<!-- TODO: Kein Taildrop -->
<!-- TODO: Keine SSO-Integration (ohne Zusatztools) -->

## Deployment

<!-- TODO: Docker/Podman -->
<!-- TODO: Systemd -->
<!-- TODO: Kubernetes -->

## Prüfungsrelevante Themen

> [!info] Prüfungshinweis
> - Control Plane vs. Data Plane Trennung
> - Warum Self-Hosting? (Datensouveränität, Compliance)
> - Unterschied zu vollständig dezentralen Lösungen (Nebula)

## Zusammenhänge

- [[00-Overlay-Index]] - Overlay-Netzwerke
- [[01-Tailscale]] - Kommerzielle Variante
- [[03-Nebula]] - Alternative ohne zentralen Control Server

## Quellen

- https://github.com/juanfont/headscale
- https://headscale.net/

