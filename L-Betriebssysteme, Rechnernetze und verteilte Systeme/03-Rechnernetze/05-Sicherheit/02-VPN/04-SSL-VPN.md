---
author: Andreas Hümmer
title: SSL VPN
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - ssl
  - tls
  - browser
  - enterprise
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# SSL VPN

## Definition

> [!quote] Definition
> **SSL VPN** (auch TLS VPN) bezeichnet VPN-Lösungen, die auf SSL/TLS basieren und oft über einen Webbrowser zugänglich sind. Sie arbeiten typischerweise auf Layer 7 (Anwendungsschicht).
## Typen

```
┌─────────────────────────────────────────────────────────────────┐
│                    SSL VPN-Typen                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Portal VPN (Clientless)                                       │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Zugriff über Webbrowser                               │  │
│   │ • Kein Client-Software nötig                            │  │
│   │ • Beschränkt auf Web-Anwendungen                        │  │
│   │ • Reverse Proxy für interne Ressourcen                  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Tunnel VPN (Full Tunnel)                                      │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Client-Software erforderlich                          │  │
│   │ • Vollständiger Netzwerkzugriff                         │  │
│   │ • Alle Anwendungen nutzbar                              │  │
│   │ • Ähnlich wie IPsec VPN                                 │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 7 (Anwendung) / 4 (Transport) |
| **Port** | TCP 443 (HTTPS) |
| **Firewall-Freundlich** | Ja (Standard HTTPS-Port) |
| **Client** | Browser oder dedizierte Software |

## Anbieter/Produkte

<!-- TODO: Cisco AnyConnect -->
<!-- TODO: Palo Alto GlobalProtect -->
<!-- TODO: Fortinet FortiClient -->
<!-- TODO: F5 BIG-IP APM -->

## Vor- und Nachteile

<!-- TODO: Einfache Bereitstellung -->
<!-- TODO: Firewall-Freundlichkeit -->
<!-- TODO: Nachteile: Overhead, nur TCP -->

## Prüfungsrelevante Themen

> [!tip] Prüfungshinweis
> - Unterschied Portal VPN vs. Tunnel VPN
> - Warum ist Port 443 vorteilhaft?
> - Vergleich mit IPsec VPN

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[../03-TLS|TLS]] - Zugrundeliegendes Protokoll
- [[01-IPsec]] - Alternative Technologie

## Quellen

- *Enterprise-VPN-Dokumentationen*

