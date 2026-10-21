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
modified: '2026-10-21'
bereich: RN
---

# IPsec in der Netzwerkschicht

## Einordnung

**IPsec (Internet Protocol Security)** ist eine Protokollsuite, die direkt auf **Layer 3 (Netzwerkschicht)** arbeitet. Sie sichert IP-Pakete durch Verschlüsselung und Authentifizierung ab.

> [!info] Detaillierte Informationen
> Für eine ausführliche Behandlung von IPsec siehe: [[../../05-Sicherheit/02-VPN/01-IPsec|IPsec im VPN-Kapitel]]

## Layer-3-Integration

![[ipsec-protokollstapel.png]]
*<span class="fig-id">03-06-06-ipsec-protokollstapel</span>: IPsec im OSI-Modell – ESP und AH als Layer-3-Protokolle.*

## IPsec-Protokolle

| Protokoll | IP-Protocol | Funktion |
|-----------|-------------|----------|
| **ESP** | 50 | Encapsulating Security Payload – Verschlüsselung + Authentifizierung |
| **AH** | 51 | Authentication Header – Nur Authentifizierung |

## IPv6-Integration

Bei IPv6 ist IPsec als **Extension Header** definiert:

![[ipsec-ipv6-extension.png]]
*<span class="fig-id">03-06-06-ipsec-ipv6-extension</span>: IPsec als IPv6 Extension Header in der Header-Kette.*

> [!note] IPv6 und IPsec
> In der ursprünglichen IPv6-Spezifikation war IPsec als **verpflichtend** vorgesehen. Dies wurde später zu "sollte unterstützt werden" abgeschwächt ([[A-RFC-Index#RFC 6434|RFC 6434]]).

## Modi-Übersicht

| Modus | Verwendung | Charakteristik |
|-------|------------|----------------|
| **Transport** | Host-to-Host | Original-IP-Header bleibt |
| **Tunnel** | Gateway-to-Gateway | Komplettes Paket gekapselt |

![[ipsec-modi.png]]
*<span class="fig-id">03-06-06-ipsec-modi</span>: Transport- vs. Tunnel-Modus – unterschiedliche Kapselung der Daten.*

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

## Nützliche IPsec-Befehle

> [!info] IPsec-Status anzeigen
> ```bash
> # Linux (mit strongSwan)
> ipsec status                       # Tunnel-Status
> ipsec statusall                    # Detaillierter Status
> ip xfrm state                      # SA (Security Associations)
> ip xfrm policy                     # Policies anzeigen
> 
> # Linux (mit Libreswan)
> ipsec whack --status               # Verbindungsstatus
> ipsec auto --status                # Alle Verbindungen
> ```

> [!info] IPsec-Traffic analysieren
> ```bash
> # Linux - ESP-Pakete anzeigen
> tcpdump -i eth0 esp                # ESP-Traffic
> tcpdump -i eth0 'ip proto 50'      # ESP (Protocol 50)
> tcpdump -i eth0 'ip proto 51'      # AH (Protocol 51)
> tcpdump -i eth0 port 500 or port 4500  # IKE-Handshake
> 
> # Wireshark Filter
> # esp, ah, isakmp, ikev2
> ```

> [!info] Windows IPsec
> ```powershell
> # Windows - IPsec-Policies anzeigen
> netsh ipsec static show all        # Statische Policies
> netsh ipsec dynamic show all       # Dynamische Policies
> 
> # Windows - IPsec-Statistiken
> netsh ipsec dynamic show stats
> 
> # Windows Firewall mit Advanced Security (GUI)
> # wf.msc → Connection Security Rules
> ```

> [!info] IKE-Debugging
> ```bash
> # Linux - IKE-Verhandlung debuggen
> journalctl -u strongswan -f        # strongSwan Logs
> ipsec stroke loglevel ike 4        # Debug-Level erhöhen
> 
> # Windows - Event Viewer
> # Applications and Services → Microsoft → Windows → IPSEC-SRV
> ```

