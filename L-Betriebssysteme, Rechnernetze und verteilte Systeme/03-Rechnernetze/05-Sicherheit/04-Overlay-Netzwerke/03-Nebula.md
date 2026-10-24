---
author: Andreas Hümmer
title: Nebula
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - nebula
  - slack
  - mesh
  - open-source
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# Nebula

## Definition

> [!quote] Definition
> **Nebula** ist ein Open-Source Overlay-Netzwerk, das von Slack entwickelt wurde. Es nutzt das Noise-Protokoll für Verschlüsselung und ein einzigartiges "Lighthouse"-Konzept für die Peer-Discovery.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 3 (Netzwerk) |
| **Protokoll** | Noise Protocol Framework |
| **Verschlüsselung** | Curve25519, ChaCha20-Poly1305 |
| **Architektur** | Mesh mit Lighthouses |
| **Lizenz** | MIT (vollständig Open Source) |
| **Entwickler** | Slack (jetzt Salesforce) |

## Architektur

Nebula nutzt ein **Lighthouse-Konzept** für dezentrale Peer-Discovery:

### Lighthouse

- Server mit öffentlicher IP-Adresse
- Aufgaben: Peer-Discovery, NAT Hole Punching vermitteln
- **Kein Traffic-Relay!** – Nur Verbindungsvermittlung
- Mehrere Lighthouses für Redundanz möglich

### Nodes

- Alle Nodes sind gleichberechtigt (echtes Mesh)
- Direkte verschlüsselte Verbindungen untereinander
- Können hinter NAT oder mit öffentlicher IP sein
- Nach initialem Handshake: Kommunikation ohne Lighthouse

> [!important] **Unterschied zu anderen Lösungen**
> Anders als bei Tailscale (DERP) oder ZeroTier (Root Servers) gibt es **keinen Relay**. Wenn NAT Hole Punching scheitert, ist keine Verbindung möglich.

## Zertifikatsbasierte Identität

Nebula nutzt eine eigene PKI statt zentraler Accounts:

### Certificate Authority (CA)

- Erstellt Root-Zertifikat (offline aufbewahren!)
- Signiert alle Node-Zertifikate
- Definiert Netzwerk-Zugehörigkeit und Gruppen
- Tool: `nebula-cert ca`

### Node-Zertifikat

Jedes Zertifikat enthält:
- **Nebula-IP-Adresse** – Feste IP im Overlay
- **Gruppenmitgliedschaften** – Für Firewall-Regeln
- **Gültigkeitszeitraum** – Automatischer Ablauf
- **Public Key** – Für Verschlüsselung

```bash
# CA erstellen
nebula-cert ca -name "MyOrg"

# Node-Zertifikat erstellen
nebula-cert sign -name "server1" -ip "10.42.0.1/24" -groups "servers,production"
```

> [!tip] **Vorteil der PKI**
> Keine zentrale Datenbank nötig – Zertifikate sind selbstbeschreibend. Offline-Deployment möglich.

## Besonderheiten

### Kein Traffic über Lighthouse

- Lighthouse vermittelt nur Verbindungen
- Gesamter Daten-Traffic geht direkt P2P
- Bei NAT-Problemen: Keine Fallback-Option (anders als DERP)
- Vorteil: Keine Single-Point-of-Failure für Traffic

### Firewall-Regeln im Zertifikat

Gruppen im Zertifikat ermöglichen policy-basierte Firewall:

```yaml
firewall:
  inbound:
    - port: 22
      proto: tcp
      groups:
        - admins
    - port: 443
      proto: tcp
      groups:
        - web-clients
```

### Gruppen-basierte Zugriffskontrolle

- Gruppen werden bei Zertifikatserstellung definiert
- Firewall-Regeln referenzieren Gruppen
- Änderung erfordert neues Zertifikat
- Zero-Trust-Ansatz: Standardmäßig alles blockiert

### Unsafe Routes für Subnet-Routing

Zugriff auf Netze hinter einem Nebula-Node:

```yaml
tun:
  unsafe_routes:
    - route: 192.168.1.0/24
      via: 10.42.0.1
```

- Ähnlich wie Tailscale Subnet Router
- "Unsafe" weil Traffic nicht Ende-zu-Ende verschlüsselt

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
N/A

> [!question] **Häufige Prüfungsfragen**
> 1. Was unterscheidet einen Lighthouse von einem DERP-Relay?
> 2. Warum nutzt Nebula Zertifikate statt Accounts?
> 3. Wie funktioniert die gruppenbasierte Zugriffskontrolle?
> 4. Was passiert, wenn NAT Hole Punching scheitert?
> 5. Was sind "Unsafe Routes" und warum heißen sie so?

> [!tip] **Merkhilfen**
> - **Lighthouse** = Leuchturm = zeigt den Weg, trägt nicht
> - **Kein Relay** = Kein Fallback bei NAT-Problemen
> - **PKI** = Offline-fähig, selbstbeschreibende Identität
> - **Gruppen im Zertifikat** = Policy ist portable
> - **Noise Protocol** = Auch in WireGuard verwendet

---

## Weiterführende Ressourcen

> [!note] **Offizielle Dokumentation**
> - [github.com/slackhq/nebula](https://github.com/slackhq/nebula) – GitHub Repository
> - [nebula.defined.net](https://nebula.defined.net/docs/) – Dokumentation

> [!tip] **Praktische Tools**
> - `nebula-cert` – Zertifikatsverwaltung
> - `nebula -test` – Konfiguration testen
> - Defined.net – Managed Nebula Service

---

## Zusammenhänge

- [[00-Overlay-Index]] → Overlay-Netzwerke Übersicht
- [[01-Tailscale]] → Alternative mit managed Service
- [[02-ZeroTier]] → Alternative mit Layer-2-Support
- [[../02-VPN/02-WireGuard|WireGuard]] → Ähnliches Verschlüsselungskonzept (Noise)

---

## Quellen

- Slack Engineering: Nebula – Scalable overlay networking tool.
- GitHub: slackhq/nebula – Open-Source Repository.
- defined.net – Managed Nebula Dokumentation und Service.

