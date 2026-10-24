---
author: Andreas Hümmer
title: Tailscale
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - tailscale
  - wireguard
  - mesh
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# Tailscale

## Definition

> [!quote] Definition
> **Tailscale** ist eine Overlay-Netzwerk-Lösung, die auf WireGuard basiert und ein automatisches Mesh-VPN mit zentraler Verwaltung bietet. Es kombiniert die Sicherheit von WireGuard mit einfacher Einrichtung und Identity-Management.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Basis** | WireGuard |
| **Layer** | 3 (Netzwerk) |
| **Architektur** | Mesh mit zentralem Control Plane |
| **Adressbereich** | 100.x.x.x (CGNAT-Bereich) |
| **Control Server** | Tailscale Coordination Server |
| **Lizenz** | Proprietär (Freemium) |

## Architektur

![[tailscale-arch.png]]
*<span class="fig-id">05-04-01-tailscale-arch</span>: Tailscale Architektur – Control Plane (Metadaten) + Data Plane (WireGuard P2P).*

**Trennung von Control Plane und Data Plane:**
- **Control Plane:** Coordination Server verwaltet Schlüssel, ACLs, Peer-Discovery
- **Data Plane:** Direkter WireGuard-Tunnel zwischen Nodes (P2P)
- Kein Traffic über Tailscale-Server – nur Metadaten!

## Kernkomponenten

### Coordination Server

- Zentrale Verwaltung aller Nodes im Tailnet
- Speichert und verteilt öffentliche WireGuard-Schlüssel
- Verwaltet ACLs (Access Control Lists)
- Kein Traffic – nur Metadaten und Konfiguration

### DERP (Designated Encrypted Relay for Packets)

Fallback wenn direkter P2P-Kontakt unmöglich:
- Relays in weltweit verteilten Rechenzentren
- Verschlüsselter Relay-Traffic (Ende-zu-Ende)
- Automatische Auswahl des nächsten DERP-Servers
- Typische Ursachen: Symmetrisches NAT, restriktive Firewalls

### MagicDNS

- Automatische DNS-Namen für alle Nodes
- Format: `hostname.tailnet-name.ts.net`
- Lokale DNS-Auflösung (100.100.100.100)
- Keine manuelle DNS-Konfiguration nötig

### Tailscale SSH

- SSH-Zugriff ohne klassische Schlüsselverwaltung
- Authentifizierung über Tailscale-Identity
- ACL-basierte Zugriffskontrolle
- Session-Recording optional

### ACLs und Tags

- JSON-basierte Zugriffskontrolle
- Tags für Gerätegruppen (z.B. `tag:server`, `tag:developer`)
- Granulare Regeln: Wer darf wohin auf welchen Ports?
- GitOps-Integration (ACLs im Repository)

## Features

### SSO-Integration

- Google Workspace, Microsoft 365, GitHub, Okta, etc.
- Keine separate Benutzerverwaltung nötig
- MFA aus dem Identity Provider übernommen
- SCIM-Provisioning für automatische Benutzeranlage

### Subnet Router

- Zugriff auf ganze Subnetze ohne Tailscale-Client auf jedem Gerät
- Ein Node "advertised" ein lokales Netzwerk
- Ideal für Legacy-Systeme, IoT-Geräte, Drucker
- Konfiguration: `tailscale up --advertise-routes=192.168.1.0/24`

### Exit Nodes

- Gesamter Internet-Traffic über einen Tailscale-Node
- Ähnlich wie klassischer VPN-Exit
- Nützlich für: Geo-Restriktionen, unsichere WLANs
- Jeder Node kann Exit Node werden

### Taildrop

- Direkte Dateiübertragung zwischen Nodes
- Verschlüsselt über WireGuard-Tunnel
- Keine Cloud-Uploads
- `tailscale file cp datei.txt node-name:`

## Headscale-Alternative

Für Self-Hosting: [[04-Headscale]]

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> NA

---

## Prüfungstipps

> [!warning] **Häufige Klausurfehler**
> - Verwechslung Control Plane vs. Data Plane
> - CGNAT-Bereich nicht kennen
> - DERP-Relays als Performance-Problem fehlinterpretieren

> [!question] **Häufige Prüfungsfragen**
> 1. Welche Daten gehen über den Coordination Server?
> 2. Was ist DERP und wann wird es genutzt?
> 3. Warum nutzt Tailscale den CGNAT-Bereich?
> 4. Wie unterscheidet sich Tailscale von klassischem VPN?
> 5. Was ist der Vorteil der Control/Data Plane Trennung?

> [!tip] **Merkhilfen**
> - **Control Plane** = Nur Metadaten (Schlüssel, ACLs)
> - **Data Plane** = WireGuard P2P (kein Umweg)
> - **100.x.x.x** = CGNAT = keine Konflikte mit privaten IPs
> - **DERP** = Relay wenn P2P scheitert
> - **MagicDNS** = Automatische Namen für alle Nodes
> - **Mesh** = Jeder Node verbindet sich direkt mit jedem

---

## Weiterführende Ressourcen

> [!note] **Offizielle Dokumentation**
> - [tailscale.com](https://tailscale.com/) – Offizielle Projektseite
> - [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works/) – Technischer Deep-Dive

> [!tip] **Praktische Tools**
> - `tailscale status` – Zeigt verbundene Nodes
> - `tailscale ping node-name` – Testet Verbindung (P2P oder DERP?)
> - `tailscale netcheck` – Diagnostik für NAT-Traversal

---

## Zusammenhänge

- [[00-Overlay-Index]] → Overlay-Netzwerke Übersicht
- [[../02-VPN/02-WireGuard|WireGuard]] → Zugrundeliegendes Protokoll
- [[04-Headscale]] → Open-Source Control Server Alternative
- [[02-ZeroTier]] → Ähnliches Konzept, anderer Ansatz

---

## Quellen

- Tailscale Inc.: How Tailscale Works – Technische Dokumentation.
- tailscale.com – Offizielle Projektseite und Blog.
- Pennarun, A.: "How NAT traversal works" – Tailscale Blog, detaillierte NAT-Analyse.

