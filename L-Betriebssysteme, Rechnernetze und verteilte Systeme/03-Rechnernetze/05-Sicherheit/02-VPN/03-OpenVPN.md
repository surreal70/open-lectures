---
author: Andreas Hümmer
title: OpenVPN
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - openvpn
  - ssl
  - open-source
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# OpenVPN

## Definition

> [!quote] Definition
> **OpenVPN** ist eine Open-Source VPN-Lösung, die SSL/TLS für den Schlüsselaustausch und verschiedene Verschlüsselungsalgorithmen für den Datentransport verwendet.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 2/3 (TAP/TUN) |
| **Port** | UDP 1194 (Standard), auch TCP möglich |
| **Verschlüsselung** | OpenSSL-Bibliothek (AES, ChaCha20, etc.) |
| **Authentifizierung** | Zertifikate, Pre-Shared Keys, Username/Password |
| **Lizenz** | GPL v2 |

## Modi

```
┌─────────────────────────────────────────────────────────────────┐
│                    OpenVPN-Modi                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   TUN-Modus (Layer 3)                                           │
│   └─► Routet IP-Pakete                                         │
│   └─► Punkt-zu-Punkt-Verbindung                                │
│   └─► Effizienter, häufiger verwendet                          │
│                                                                  │
│   TAP-Modus (Layer 2)                                           │
│   └─► Bridged Ethernet                                         │
│   └─► Ethernet-Frames werden getunnelt                         │
│   └─► Für Broadcasts/Multicast nötig                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Architektur

<!-- TODO: Client-Server-Modell -->
<!-- TODO: PKI und Zertifikate -->
<!-- TODO: Control Channel vs. Data Channel -->

## Konfiguration

<!-- TODO: Server-Konfiguration -->
<!-- TODO: Client-Konfiguration -->
<!-- TODO: easy-rsa für Zertifikate -->

## Vor- und Nachteile

<!-- TODO: Flexibilität und Portabilität -->
<!-- TODO: Nachteile: Userspace, Performance -->

## Prüfungsrelevante Themen

> [!tip] Prüfungshinweis
> - Unterschied TUN vs. TAP
> - Warum UDP bevorzugt wird
> - Zertifikat-basierte Authentifizierung

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[../03-TLS|TLS]] - Verwendetes Sicherheitsprotokoll
- [[02-WireGuard]] - Modernere Alternative

## Quellen

- https://openvpn.net/
- https://community.openvpn.net/openvpn/wiki

