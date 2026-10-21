---
author: Andreas Hümmer
title: PPTP - Point-to-Point Tunneling Protocol
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - pptp
  - veraltet
  - unsicher
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# PPTP - Point-to-Point Tunneling Protocol

## Definition

> [!quote] Definition
> **PPTP (Point-to-Point Tunneling Protocol)** ist ein von Microsoft entwickeltes VPN-Protokoll auf Layer 2. Es gilt heute als **unsicher** und sollte nicht mehr verwendet werden.
>
> > [!danger] Sicherheitswarnung
> > PPTP ist **kryptographisch gebrochen** und sollte **nicht mehr verwendet** werden. Die MS-CHAPv2-Authentifizierung kann in wenigen Stunden geknackt werden.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 2 (Sicherung) |
| **Control Port** | TCP 1723 |
| **Datenprotokoll** | GRE (Protocol 47) |
| **Verschlüsselung** | MPPE (Microsoft Point-to-Point Encryption) |
| **Status** | ⚠️ **Veraltet und unsicher** |

## Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    PPTP-Struktur                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                    PPP-Frame                            │  │
│   │              (Nutzdaten + PPP-Header)                   │  │
│   └─────────────────────────────────────────────────────────┘  │
│                            │                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                    GRE-Header                           │  │
│   │              (Generic Routing Encapsulation)            │  │
│   └─────────────────────────────────────────────────────────┘  │
│                            │                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                    IP-Header                            │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Zusätzlich: TCP-Verbindung auf Port 1723 für Kontrolle       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Sicherheitsprobleme

```
┌─────────────────────────────────────────────────────────────────┐
│                 PPTP-Sicherheitsprobleme                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✗ MS-CHAPv2 ist gebrochen                                    │
│     └─► Kann mit cloudcracker.com in ~24h geknackt werden      │
│                                                                  │
│   ✗ MPPE-Verschlüsselung ist schwach                           │
│     └─► Basiert auf RC4                                        │
│     └─► Schlüssel aus Passwort-Hash abgeleitet                 │
│                                                                  │
│   ✗ Keine Perfect Forward Secrecy                              │
│     └─► Kompromittierter Schlüssel = alle Daten lesbar         │
│                                                                  │
│   ✗ Bekannte Angriffe seit 2012                                │
│     └─► Moxie Marlinspike: "ChapCrack"                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Warum wird PPTP noch verwendet?

<!-- TODO: Legacy-Systeme -->
<!-- TODO: Einfache Einrichtung -->
<!-- TODO: Native Windows-Unterstützung -->

## Alternativen

| Statt PPTP | Verwende |
|------------|----------|
| Remote Access | [[02-WireGuard]], [[03-OpenVPN]] |
| Site-to-Site | [[01-IPsec]] |
| Mobile Geräte | [[01-IPsec\|IKEv2/IPsec]] |

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - Warum ist PPTP unsicher? (MS-CHAPv2, MPPE)
> - Seit wann gilt PPTP als gebrochen? (2012)
> - Welche Alternativen gibt es?

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[05-L2TP]] - Nachfolger (mit IPsec)
- [[01-IPsec]] - Sichere Alternative

## Quellen

- [[A-RFC-Index#RFC 2637|RFC 2637]] - PPTP
- Marlinspike, M. (2012): "Defeating PPTP VPNs and WPA2-Enterprise with MS-CHAPv2"

