---
author: Andreas Hümmer
title: ZeroTier
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - zerotier
  - sdn
  - layer2
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# ZeroTier

## Definition

> [!quote] Definition
> **ZeroTier** ist eine Overlay-Netzwerk-Lösung, die ein virtuelles Layer-2-Netzwerk über das Internet erstellt. Anders als WireGuard-basierte Lösungen emuliert ZeroTier ein vollständiges Ethernet-Netzwerk mit Broadcast-Support.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 2 (Sicherung) – virtuelles Ethernet |
| **Protokoll** | Eigenes (ZeroTier Protocol) |
| **Verschlüsselung** | Curve25519, Salsa20, Poly1305 |
| **Architektur** | P2P-Mesh mit Root-Servern |
| **Network-ID** | 16-stellige Hex-ID |
| **Lizenz** | BSL (Business Source License) |

## Architektur

![[zerotier-arch.png]]
*<span class="fig-id">05-04-02-zerotier-arch</span>: ZeroTier Architektur – Root Servers (Planet) und virtuelles Layer-2-Netzwerk.*

**Komponenten:**
- **Root Servers (Planet):** Peer-Discovery und NAT-Traversal-Vermittlung
- **Nodes:** Clients mit virtuellem zt-Interface
- **Virtuelles L2-Netzwerk:** Verhält sich wie ein Ethernet-Switch

## Besonderheiten

### Layer 2 vs. Layer 3

| Aspekt | ZeroTier (L2) | Tailscale (L3) |
|--------|---------------|----------------|
| Ebene | Ethernet-Frames | IP-Pakete |
| Broadcast | ✓ Ja | ✗ Nein |
| Multicast | ✓ Ja | ✗ Nein |
| ARP | ✓ Funktioniert | Nicht nötig |
| Use Case | LAN-Emulation | Einfaches VPN |

### Broadcast/Multicast-Support

- Echte Ethernet-Broadcasts möglich (255.255.255.255)
- Multicast für mDNS, SSDP, DLNA funktioniert
- Wichtig für: Windows-Netzwerkumgebung, Drucker-Discovery, Gaming
- Nachteil: Mehr Traffic als bei Layer-3-Lösungen

### Managed Routes und Flow Rules

- Zentrales Traffic-Management über Network Controller
- Flow Rules: Firewall-ähnliche Regeln im Netzwerk
- Managed Routes: Routing-Einträge für alle Nodes
- Ethernet Tags für VLAN-ähnliche Segmentierung

### Moon (eigene Root-Server)

- Private Root-Server für Air-Gapped-Umgebungen
- Reduzierte Latenz durch lokale Roots
- Unabhängigkeit von ZeroTier-Infrastruktur
- Konfiguration: `zerotier-cli orbit <world-id> <seed>`

## Network Controller

### ZeroTier Central (Cloud)

- Web-basierte Verwaltung unter my.zerotier.com
- Kostenlos bis 25 Nodes pro Netzwerk
- Netzwerk erstellen, Nodes autorisieren, IPs zuweisen
- Flow Rules und Managed Routes konfigurieren

### Self-Hosted Controller

- Open-Source Controller für komplette Selbstverwaltung
- Keine Abhängigkeit von ZeroTier-Servern
- Projekte: ztncui, zero-ui, ZeroTier Controller API
- Ideal für: Compliance, Air-Gapped, volle Kontrolle

### Network Rules Engine

Mächtige regelbasierte Traffic-Kontrolle:

```
# Beispiel: Nur bestimmte Ports erlauben
drop not ipprotocol tcp;
accept dport 22 or dport 80 or dport 443;
drop;
```

- Tag-basierte Zugriffskontrolle
- Capability-Modell für granulare Rechte
- Ähnlich wie SDN-Controller (Software-Defined Networking)

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> NA

---

## Prüfungstipps

> [!question] **Häufige Prüfungsfragen**
> 1. Warum arbeitet ZeroTier auf Layer 2?
> 2. Wann ist Broadcast-Support wichtig?
> 3. Was ist der Unterschied zwischen Planet und Moon?
> 4. Wie unterscheidet sich ZeroTier von Tailscale?
> 5. Was ermöglicht die Network Rules Engine?

> [!tip] **Merkhilfen**
> - **Layer 2** = Ethernet-Frames = Broadcast funktioniert
> - **Planet** = Öffentliche Root-Server (Standard)
> - **Moon** = Private Root-Server (Self-Hosted)
> - **16-stellige Hex-ID** = Network-ID
> - **zt-iface** = Virtuelles Netzwerk-Interface
> - **Flow Rules** = SDN-ähnliche Traffic-Kontrolle

---

## Weiterführende Ressourcen

> [!note] **Offizielle Dokumentation**
> - [zerotier.com](https://www.zerotier.com/) – Offizielle Projektseite
> - [docs.zerotier.com](https://docs.zerotier.com/) – Technische Dokumentation

> [!tip] **Praktische Tools**
> - `zerotier-cli status` – Zeigt Node-Status
> - `zerotier-cli listnetworks` – Zeigt verbundene Netzwerke
> - `zerotier-cli peers` – Zeigt verbundene Peers

---

## Zusammenhänge

- [[00-Overlay-Index]] → Overlay-Netzwerke Übersicht
- [[01-Tailscale]] → Alternative (Layer 3, WireGuard-basiert)
- [[03-Nebula]] → Open-Source Alternative
- [[../02-VPN/07-Hamachi|Hamachi]] → Ähnliches Konzept (proprietär)

---

## Quellen

- ZeroTier Inc.: ZeroTier Manual – Offizielle Dokumentation.
- zerotier.com – Projektseite und Blog.
- GitHub: zerotier/ZeroTierOne – Open-Source Client-Implementierung.

