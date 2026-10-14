---
author: Andreas Hümmer
title: IPsec - Kurzübersicht (Netzwerkschicht)
tags:
  - content
  - rn
  - network-layer
  - ipsec
  - sicherheit
  - verschluesselung
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# IPsec in der Netzwerkschicht

## Einordnung

**IPsec (Internet Protocol Security)** ist eine Protokollsuite, die direkt auf **Layer 3 (Netzwerkschicht)** arbeitet. Sie sichert IP-Pakete durch Verschlüsselung und Authentifizierung ab.

> [!info] Detaillierte Informationen
> Für eine ausführliche Behandlung von IPsec siehe: [[../../05-Sicherheit/02-VPN/01-IPsec|IPsec im VPN-Kapitel]]

## Layer-3-Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                IPsec im Protokollstapel                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Transportschicht (Layer 4)                 │   │
│   │                    TCP / UDP                            │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Netzwerkschicht (Layer 3)                  │   │
│   │  ┌────────────────────────────────────────────────────┐ │   │
│   │  │                      IP                            │ │   │
│   │  │  ┌──────────────┐  ┌──────────────┐               │ │   │
│   │  │  │  ESP (50)    │  │   AH (51)    │  ← IPsec     │ │   │
│   │  │  │ Verschlüss.  │  │ Authentif.   │               │ │   │
│   │  │  └──────────────┘  └──────────────┘               │ │   │
│   │  └────────────────────────────────────────────────────┘ │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## IPsec-Protokolle

| Protokoll | IP-Protocol | Funktion |
|-----------|-------------|----------|
| **ESP** | 50 | Encapsulating Security Payload – Verschlüsselung + Authentifizierung |
| **AH** | 51 | Authentication Header – Nur Authentifizierung |

## IPv6-Integration

Bei IPv6 ist IPsec als **Extension Header** definiert:

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌────────┐
│   IPv6       │──►│     ESP      │──►│     TCP      │──►│ Daten  │
│   Header     │   │ Next Hdr: 6  │   │   Header     │   │        │
│ Next Hdr: 50 │   │              │   │              │   │        │
└──────────────┘   └──────────────┘   └──────────────┘   └────────┘
```

> [!note] IPv6 und IPsec
> In der ursprünglichen IPv6-Spezifikation war IPsec als **verpflichtend** vorgesehen. Dies wurde später zu "sollte unterstützt werden" abgeschwächt ([[A-RFC-Index#RFC 6434|RFC 6434]]).

## Modi-Übersicht

| Modus | Verwendung | Charakteristik |
|-------|------------|----------------|
| **Transport** | Host-to-Host | Original-IP-Header bleibt |
| **Tunnel** | Gateway-to-Gateway | Komplettes Paket gekapselt |

```
Transport:  [IP-Hdr] [ESP/AH] [TCP] [Daten]
                              └──verschlüsselt──┘

Tunnel:     [Neuer IP] [ESP/AH] [Orig. IP] [TCP] [Daten]
                                └─────verschlüsselt─────┘
```

## Schlüsselaustausch

| Protokoll | Port | Verwendung |
|-----------|------|------------|
| **IKEv2** | UDP 500, 4500 | Aktueller Standard |
| **IKEv1** | UDP 500 | Ältere Version |

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - IPsec arbeitet auf Layer 3
> - ESP (Protocol 50) vs. AH (Protocol 51)
> - Transport-Modus vs. Tunnel-Modus
> - Bei IPv6 als Extension Header integriert

## Zusammenhänge

- [[01-IP-Protokoll]] - IPsec sichert IP-Pakete
- [[03-IPv6]] - IPsec als Extension Header
- [[../../05-Sicherheit/02-VPN/01-IPsec|IPsec (Detail)]] - Ausführliche Beschreibung
- [[../../05-Sicherheit/02-VPN/00-VPN-Index|VPN-Übersicht]] - IPsec als VPN-Technologie

## Quellen

- [[A-RFC-Index#RFC 4301|RFC 4301]] - Security Architecture for IP
- [[A-RFC-Index#RFC 4303|RFC 4303]] - ESP
- [[A-RFC-Index#RFC 4302|RFC 4302]] - AH

