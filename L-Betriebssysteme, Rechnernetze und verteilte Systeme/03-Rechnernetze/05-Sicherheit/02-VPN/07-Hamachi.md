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
modified: '2026-10-24'
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

Hamachi kombiniert Peer-to-Peer mit zentraler Vermittlung:

**Hamachi Cloud (Mediation Server):**
- Zentrale Registrierung und Authentifizierung
- Vermittelt Verbindungen zwischen Peers
- Relay-Funktion wenn direkter P2P-Kontakt unmöglich

**Peer-to-Peer-Verbindungen:**
- Direkte verschlüsselte Verbindung zwischen Clients
- NAT-Traversal (UDP Hole Punching)
- Virtuelle IP-Adressen im 25.x.x.x-Bereich

**Verbindungsaufbau:**
1. Peers registrieren sich bei Hamachi Cloud
2. Cloud vermittelt Verbindungsinformationen
3. Peers versuchen direkte P2P-Verbindung (NAT-Traversal)
4. Bei Fehlschlag: Traffic über Relay-Server

> [!info] **25.x.x.x Adressbereich**
> Hamachi nutzt den reservierten, aber nicht standardmäßigen Bereich 25.0.0.0/8. Dies kann zu Konflikten führen, wenn dieser Bereich anderweitig genutzt wird.

## Anwendungsfälle

**Gaming (LAN-Spiele über Internet):**
- Klassischer Use Case – ältere Spiele ohne Online-Multiplayer
- Simuliert lokales Netzwerk für LAN-Party-Feeling
- Minecraft, Age of Empires, etc.

**Kleine Büro-Netzwerke:**
- Verbindung von Home-Office-Mitarbeitern
- Zugriff auf Dateifreigaben und Drucker
- Einfache Alternative zu komplexen VPN-Setups

**Remote-Desktop-Zugriff:**
- Zugriff auf entfernte Computer ohne Port-Forwarding
- Funktioniert auch hinter NAT/Firewall
- Kombination mit RDP, VNC, etc.

## Vor- und Nachteile

### Vorteile

- **Extrem einfache Einrichtung** – wenige Klicks, keine Netzwerkkenntnisse nötig
- **NAT-Traversal funktioniert meist automatisch** – kein Port-Forwarding erforderlich
- **Kostenlose Version verfügbar** – für kleine Netzwerke ausreichend
- **Plattformübergreifend** – Windows, macOS, Linux

### Nachteile

- **Proprietär** – Quellcode nicht einsehbar, nicht auditierbar
- **Abhängigkeit von LogMeIn-Servern** – ohne Cloud-Service kein Betrieb
- **Kostenlose Version limitiert** – maximal 5 Geräte pro Netzwerk
- **25.x.x.x Adressbereich** – kann Konflikte mit anderen Netzwerken verursachen
- **Nicht für Enterprise geeignet** – keine granulare Zugriffskontrolle, keine Compliance

> [!warning] **Datenschutzbedenken**
> Der gesamte Traffic wird über LogMeIn-Server vermittelt. Für sensible Daten ist Hamachi nicht empfehlenswert.

## Alternativen

| Für | Alternative |
|-----|-------------|
| Gaming | ZeroTier, Tailscale |
| Enterprise | [[01-IPsec]], [[03-OpenVPN]] |
| Einfache Nutzung | [[02-WireGuard]] mit Tailscale |

## Prüfungstipps

> [!info] **Prüfungshinweis**
> Hamachi ist in Prüfungen eher selten relevant, aber als Beispiel für:
> - Proprietäre VPN-Lösungen
> - P2P-VPN-Architektur
> - NAT-Traversal-Techniken

> [!question] **Mögliche Prüfungsfragen**
> 1. Was unterscheidet Hamachi von klassischen VPN-Lösungen?
> 2. Welche Vor- und Nachteile hat ein P2P-VPN?
> 3. Warum ist der 25.x.x.x-Adressbereich problematisch?

> [!tip] **Merkhilfen**
> - **P2P + Cloud** = Hamachi-Architektur
> - **25.x.x.x** = Hamachi-Adressbereich
> - **Gaming** = Klassischer Anwendungsfall
> - **Proprietär** = Keine Audit-Möglichkeit

---

## Weiterführende Ressourcen

> [!note] **Moderne Alternativen**
> - **Tailscale** – WireGuard-basiert, ähnlich einfach wie Hamachi
> - **ZeroTier** – Open-Source P2P-VPN
> - **Nebula** – Open-Source Overlay-Netzwerk (von Slack entwickelt)

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[02-WireGuard]] → Moderne Alternative (mit Tailscale)
- [[../04-Overlay-Netzwerke/00-Overlay-Index|Overlay-Netzwerke]] → Ähnliches Konzept

---

## Quellen

- LogMeIn: Hamachi Documentation – vpn.net
- Wikipedia: Hamachi (software) – Übersicht und Geschichte.

