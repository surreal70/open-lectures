---
author: Andreas Hümmer
title: VPN - Virtual Private Networks
tags:
  - content
  - index
  - rn
  - sicherheit
  - vpn
  - tunnel
  - verschluesselung
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# VPN - Virtual Private Networks

## Definition

> [!quote] Definition
> Ein **Virtual Private Network (VPN)** ermöglicht eine sichere, verschlüsselte Verbindung über ein unsicheres Netzwerk (typischerweise das Internet). VPNs erstellen einen "Tunnel", durch den Daten geschützt übertragen werden.
## Grundprinzip

```
┌─────────────────────────────────────────────────────────────────┐
│                       VPN-Tunnel                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Standort A                                       Standort B   │
│   ┌─────────────┐                               ┌─────────────┐ │
│   │ Privates    │                               │ Privates    │ │
│   │ Netzwerk    │                               │ Netzwerk    │ │
│   │ 10.0.1.0/24 │                               │ 10.0.2.0/24 │ │
│   └──────┬──────┘                               └──────┬──────┘ │
│          │                                             │        │
│   ┌──────┴──────┐      ╔═══════════════╗      ┌──────┴──────┐  │
│   │ VPN-Gateway │══════║  VERSCHLÜSS.  ║══════│ VPN-Gateway │  │
│   │             │      ║    TUNNEL     ║      │             │  │
│   └─────────────┘      ╚═══════════════╝      └─────────────┘  │
│                              │                                  │
│                    ┌─────────┴─────────┐                       │
│                    │     INTERNET      │                       │
│                    │  (unsicher)       │                       │
│                    └───────────────────┘                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## VPN-Typen

### Nach Einsatzzweck

| Typ | Beschreibung | Anwendung |
|-----|--------------|-----------|
| **Site-to-Site** | Verbindet zwei Netzwerke | Standortvernetzung |
| **Remote Access** | Einzelner Client zu Netzwerk | Homeoffice, mobiles Arbeiten |
| **Host-to-Host** | Direkte Verbindung zweier Hosts | Spezielle Anwendungen |

### Nach OSI-Schicht

```
┌─────────────────────────────────────────────────────────────────┐
│                  VPN-Protokolle nach Schicht                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Layer 7 (Anwendung)                                           │
│   └─► SSL/TLS VPN (z.B. OpenVPN im SSL-Modus)                  │
│                                                                  │
│   Layer 4 (Transport)                                           │
│   └─► SSH-Tunnel, SSTP                                         │
│                                                                  │
│   Layer 3 (Netzwerk)                                            │
│   └─► IPsec, WireGuard                                         │
│                                                                  │
│   Layer 2 (Sicherung)                                           │
│   └─► L2TP, PPTP, L2F                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## VPN-Protokolle im Überblick

| Protokoll | Layer | Sicherheit | Geschwindigkeit | Status |
|-----------|-------|------------|-----------------|--------|
| [[01-IPsec\|IPsec]] | 3 | ★★★★★ | ★★★★☆ | Standard |
| [[02-WireGuard\|WireGuard]] | 3 | ★★★★★ | ★★★★★ | Modern |
| [[03-OpenVPN\|OpenVPN]] | 3-7 | ★★★★★ | ★★★☆☆ | Verbreitet |
| [[04-SSL-VPN\|SSL VPN]] | 7 | ★★★★☆ | ★★★☆☆ | Enterprise |
| [[05-L2TP\|L2TP/IPsec]] | 2 | ★★★★☆ | ★★★☆☆ | Älterer Standard |
| [[06-PPTP\|PPTP]] | 2 | ★☆☆☆☆ | ★★★★☆ | ⚠️ Veraltet |
| [[07-Hamachi\|Hamachi]] | 3 | ★★★☆☆ | ★★★☆☆ | Proprietär |

## Inhaltsverzeichnis

1. [[01-IPsec]] - Internet Protocol Security (Industriestandard)
2. [[02-WireGuard]] - Modernes, schlankes VPN-Protokoll
3. [[03-OpenVPN]] - Open-Source SSL-basiertes VPN
4. [[04-SSL-VPN]] - Browser-basierte VPN-Lösungen
5. [[05-L2TP]] - Layer 2 Tunneling Protocol
6. [[06-PPTP]] - Point-to-Point Tunneling Protocol (veraltet)
7. [[07-Hamachi]] - Proprietäre P2P-VPN-Lösung

## Sicherheitsaspekte

```
┌─────────────────────────────────────────────────────────────────┐
│                  VPN-Sicherheitseigenschaften                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Vertraulichkeit (Confidentiality)                          │
│     └─► Verschlüsselung der Nutzdaten                          │
│                                                                  │
│   ✓ Integrität (Integrity)                                     │
│     └─► Schutz vor Manipulation (HMAC, Checksums)              │
│                                                                  │
│   ✓ Authentizität (Authentication)                             │
│     └─► Identitätsprüfung der Endpunkte                        │
│                                                                  │
│   ✓ Replay-Schutz                                              │
│     └─► Sequenznummern verhindern Wiederholungsangriffe        │
│                                                                  │
│   ○ Perfect Forward Secrecy (PFS)                              │
│     └─► Nicht alle Protokolle unterstützen dies                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - Unterschied Site-to-Site vs. Remote Access VPN
> - IPsec-Modi: Tunnel vs. Transport
> - Warum ist PPTP unsicher?
> - Vergleich der VPN-Protokolle nach Schicht

## Zusammenhänge

- [[../01-Firewalls|Firewalls]] - VPN-Traffic durch Firewalls
- [[../03-TLS|TLS]] - Grundlage für SSL VPN
- [[../../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec (Netzwerkschicht)]] - Layer-3-Einordnung

