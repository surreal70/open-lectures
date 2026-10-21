---
author: Andreas Hümmer
title: Hamachi
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - hamachi
  - p2p
  - proprietaer
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Hamachi (LogMeIn Hamachi)

## Definition

> [!quote] Definition
> **Hamachi** ist eine proprietäre VPN-Lösung von LogMeIn, die ein virtuelles LAN über das Internet erstellt. Sie ermöglicht einfache Peer-to-Peer-Verbindungen ohne komplexe Konfiguration.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 3 (Netzwerk) |
| **Architektur** | Peer-to-Peer mit zentralem Relay |
| **Adressbereich** | 25.x.x.x (privater, nicht-standardmäßiger Bereich) |
| **Lizenz** | Proprietär (Freemium-Modell) |
| **Hersteller** | LogMeIn (jetzt GoTo) |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    Hamachi-Netzwerk                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │  Hamachi Cloud  │                          │
│                    │  (Mediation &   │                          │
│                    │   Relay Server) │                          │
│                    └────────┬────────┘                          │
│                             │                                    │
│              ┌──────────────┼──────────────┐                    │
│              │              │              │                    │
│              ▼              ▼              ▼                    │
│        ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│        │  Peer A │◄──►│  Peer B │◄──►│  Peer C │              │
│        │25.0.0.1 │    │25.0.0.2 │    │25.0.0.3 │              │
│        └─────────┘    └─────────┘    └─────────┘              │
│                                                                  │
│   Direkte P2P-Verbindung wenn möglich (NAT Traversal)          │
│   Relay über Cloud wenn direkter Kontakt nicht möglich         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Anwendungsfälle

<!-- TODO: Gaming (LAN-Spiele über Internet) -->
<!-- TODO: Kleine Büro-Netzwerke -->
<!-- TODO: Remote-Desktop-Zugriff -->

## Vor- und Nachteile

```
┌─────────────────────────────────────────────────────────────────┐
│                Hamachi: Vor- und Nachteile                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Vorteile:                                                   │
│     • Extrem einfache Einrichtung                              │
│     • Keine Netzwerkkenntnisse nötig                           │
│     • NAT-Traversal funktioniert meist automatisch             │
│     • Kostenlose Version verfügbar                             │
│                                                                  │
│   ✗ Nachteile:                                                  │
│     • Proprietär (nicht auditierbar)                           │
│     • Abhängigkeit von LogMeIn-Servern                         │
│     • Kostenlose Version auf 5 Geräte limitiert                │
│     • 25.x.x.x kann Konflikte verursachen                      │
│     • Nicht für Enterprise geeignet                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Alternativen

| Für | Alternative |
|-----|-------------|
| Gaming | ZeroTier, Tailscale |
| Enterprise | [[01-IPsec]], [[03-OpenVPN]] |
| Einfache Nutzung | [[02-WireGuard]] mit Tailscale |

## Prüfungsrelevante Themen

> [!info] Prüfungshinweis
> Hamachi ist in Prüfungen eher selten relevant, aber als Beispiel für:
> - Proprietäre VPN-Lösungen
> - P2P-VPN-Architektur
> - NAT-Traversal-Techniken

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[02-WireGuard]] - Moderne Alternative

## Quellen

- https://www.vpn.net/ (LogMeIn Hamachi)

