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

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Funktion von IPsec auf Layer 3 erklären
> - Den Unterschied zwischen ESP und AH beschreiben
> - Transport- und Tunnel-Modus unterscheiden
> - Die Rolle von IKE beim Schlüsselaustausch verstehen

## Einordnung

**IPsec (Internet Protocol Security)** ist eine Protokollsuite, die direkt auf **Layer 3 (Netzwerkschicht)** arbeitet. Sie sichert IP-Pakete durch Verschlüsselung und Authentifizierung ab.

> [!info] Detaillierte Informationen
> Für eine ausführliche Behandlung von IPsec siehe: [[../../05-Sicherheit/02-VPN/01-IPsec|IPsec im VPN-Kapitel]]

### Warum IPsec auf Layer 3?

| Vorteil | Beschreibung |
|---------|--------------|
| **Transparenz** | Anwendungen müssen nicht angepasst werden |
| **Universalität** | Schützt alle höheren Protokolle (TCP, UDP, ICMP, ...) |
| **End-to-End** | Kann Host-to-Host oder Gateway-to-Gateway arbeiten |
| **Netzwerk-Integration** | Funktioniert mit Routing und Firewalls |

> [!tip] Vergleich mit TLS
> - **TLS** (Layer 4/5): Schützt einzelne Verbindungen (HTTPS, SMTPS)
> - **IPsec** (Layer 3): Schützt kompletten IP-Verkehr zwischen Endpunkten

## Layer-3-Integration

![[ipsec-protokollstapel.png]]
*<span class="fig-id">03-06-06-ipsec-protokollstapel</span>: IPsec im OSI-Modell – ESP und AH als Layer-3-Protokolle.*

## IPsec-Protokolle

| Protokoll | IP-Protocol | Funktion |
|-----------|-------------|----------|
| **ESP** | 50 | Encapsulating Security Payload – Verschlüsselung + Authentifizierung |
| **AH** | 51 | Authentication Header – Nur Authentifizierung |

### ESP (Encapsulating Security Payload)

ESP bietet **Vertraulichkeit** (Verschlüsselung) und **Integrität** (Authentifizierung):

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Verschlüsselung** | AES, 3DES, ChaCha20 |
| **Authentifizierung** | HMAC-SHA256, HMAC-SHA512 |
| **Replay-Schutz** | Sequenznummern verhindern Wiederholungsangriffe |

> [!tip] ESP ist der Standard
> In der Praxis wird fast ausschließlich ESP verwendet, da es sowohl verschlüsselt als auch authentifiziert.

### AH (Authentication Header)

AH bietet **nur Integrität** – keine Verschlüsselung:

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Authentifizierung** | Ja – komplettes Paket inkl. IP-Header |
| **Verschlüsselung** | Nein |
| **NAT-Kompatibilität** | Nein – IP-Header wird authentifiziert |

> [!warning] AH und NAT
> AH authentifiziert auch den IP-Header. Da NAT die IP-Adressen ändert, ist AH **nicht NAT-kompatibel**. Deshalb wird AH kaum noch eingesetzt.

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

## Schlüsselaustausch (IKE)

IPsec benötigt gemeinsame Schlüssel für Verschlüsselung und Authentifizierung. Der **Internet Key Exchange (IKE)** handelt diese automatisch aus.

| Protokoll | Port | Verwendung |
|-----------|------|------------|
| **IKEv2** | UDP 500, 4500 | Aktueller Standard |
| **IKEv1** | UDP 500 | Ältere Version |

### IKE-Phasen

| Phase | Funktion | Ergebnis |
|-------|----------|----------|
| **Phase 1** | Authentifizierung der Peers | IKE SA (sichere Verbindung für Phase 2) |
| **Phase 2** | Aushandeln der IPsec-Parameter | IPsec SA (Schlüssel für ESP/AH) |

### Security Association (SA)

Eine **SA** ist ein Satz von Sicherheitsparametern für eine Richtung:

- **SPI** (Security Parameter Index): Identifiziert die SA
- **Algorithmen**: Verschlüsselung + Authentifizierung
- **Schlüssel**: Für ESP/AH
- **Lifetime**: Gültigkeitsdauer

> [!note] Zwei SAs pro Verbindung
> Da eine SA unidirektional ist, werden für eine bidirektionale Verbindung **zwei SAs** benötigt (eine pro Richtung).

### NAT-Traversal (NAT-T)

Problem: ESP-Pakete haben keine Ports → NAT kann sie nicht zuordnen.

Lösung: **NAT-T** kapselt ESP in UDP (Port 4500):

```
[IP] [UDP 4500] [ESP] [Daten]
```

> [!tip] NAT-T wird automatisch erkannt
> IKE erkennt NAT automatisch und aktiviert NAT-T bei Bedarf.

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz
> - IPsec arbeitet auf Layer 3
> - ESP (Protocol 50) vs. AH (Protocol 51)
> - Transport-Modus vs. Tunnel-Modus
> - Bei IPv6 als Extension Header integriert
> - IKE für Schlüsselaustausch (Phase 1 + Phase 2)
> - NAT-T für NAT-Kompatibilität

### Typische Prüfungsfragen

> [!question] Beispielfragen
> - Warum wird AH kaum noch verwendet? → Nicht NAT-kompatibel
> - Was ist der Unterschied zwischen Transport- und Tunnel-Modus?
> - Welche IP-Protokollnummer hat ESP? → 50
> - Warum braucht IPsec zwei Security Associations? → Unidirektional
> - Wie löst NAT-T das NAT-Problem? → ESP in UDP kapseln

## Einsatzszenarien

| Szenario | Modus | Typische Konfiguration |
|----------|-------|------------------------|
| **Site-to-Site VPN** | Tunnel | Gateway ↔ Gateway, schützt ganzes Netzwerk |
| **Remote Access VPN** | Tunnel | Client ↔ Gateway, Roadwarrior-Zugang |
| **Host-to-Host** | Transport | Server ↔ Server, direkte Verschlüsselung |
| **DMVPN** | Tunnel | Dynamische Tunnels zwischen Standorten |

> [!example] Praxisbeispiel: Site-to-Site VPN
> ```
> Büro A (192.168.1.0/24) ←──IPsec-Tunnel──→ Büro B (192.168.2.0/24)
>        Gateway A                                  Gateway B
>        (öffentliche IP)                          (öffentliche IP)
> ```
> - Alle Pakete zwischen den Netzen werden automatisch verschlüsselt
> - Für Endgeräte transparent (kein VPN-Client nötig)

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

