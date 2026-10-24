---
author: Andreas Hümmer
title: Headscale
tags:
  - content
  - rn
  - sicherheit
  - overlay
  - headscale
  - tailscale
  - self-hosted
  - open-source
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# Headscale

## Definition

> [!quote] Definition
> **Headscale** ist eine Open-Source-Implementierung des Tailscale Coordination Servers. Es ermöglicht Self-Hosting eines Tailscale-kompatiblen Netzwerks ohne Abhängigkeit von Tailscale's Cloud-Diensten.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Basis** | Tailscale-kompatibel (WireGuard) |
| **Layer** | 3 (Netzwerk) |
| **Architektur** | Self-hosted Control Plane |
| **Client** | Standard Tailscale-Client |
| **Lizenz** | BSD-3-Clause |

## Architektur

![[headscale-vs-tailscale.png]]
*<span class="fig-id">05-04-04-headscale-vs-tailscale</span>: Headscale als Self-Hosted-Alternative zum Tailscale Coordination Server – gleiche Clients, eigene Infrastruktur.*

## Features

### User/Namespace-Management

- **Namespaces** (früher "Users"): Logische Trennung von Gerätegruppen
- Jeder Namespace hat eigene Geräte und Zugriffsregeln
- Mehrere Namespaces auf einem Server möglich
- Geräte können zwischen Namespaces geteilt werden (via ACLs)

### Pre-Auth Keys

- Vorgenerierte Schlüssel für automatisierte Registrierung
- Einmal- oder Mehrfachverwendung konfigurierbar
- Ablaufdatum einstellbar
- Ideal für automatisiertes Deployment (Ansible, Terraform)

```bash
# Key erstellen
headscale preauthkeys create --namespace mynamespace --expiration 24h

# Gerät mit Key registrieren
tailscale up --login-server https://headscale.example.com --authkey <key>
```

### ACL-Unterstützung

- Zugriffskontrolllisten im Tailscale-Format (HuJSON)
- Definiert, welche Geräte miteinander kommunizieren dürfen
- Unterstützt Tags für gruppenbasierte Regeln

```json
{
  "acls": [
    {"action": "accept", "src": ["tag:server"], "dst": ["tag:server:*"]},
    {"action": "accept", "src": ["tag:client"], "dst": ["tag:server:80,443"]}
  ]
}
```

### DERP-Server

- **DERP** (Designated Encrypted Relay for Packets): Relay für NAT-Traversal
- Tailscale betreibt globale DERP-Server (default)
- Headscale kann eigene DERP-Server nutzen:
  - Volle Kontrolle über Relay-Infrastruktur
  - Geringere Latenz bei lokaler Installation
  - Keine Abhängigkeit von Tailscale-Infrastruktur

### DNS-Konfiguration

- MagicDNS-Grundfunktionen verfügbar
- Eigene DNS-Server konfigurierbar
- Split-DNS für interne Domains
- Automatische Hostnamen-Auflösung im Netzwerk

## Einschränkungen

| Feature | Tailscale | Headscale |
|---------|-----------|-----------|
| **MagicDNS** | Vollständig | Teilweise (Basis-Funktionen) |
| **Taildrop** | ✓ Dateitransfer | ✗ Nicht unterstützt |
| **SSO/OIDC** | Integriert | Nur mit Zusatztools |
| **Funnel** | ✓ | ✗ Nicht verfügbar |
| **SSH** | ✓ Tailscale SSH | ✗ Nicht unterstützt |
| **Admin UI** | Webkonsole | CLI + Community-UIs |

### Workarounds

- **SSO**: Integration über OIDC-Proxy (z.B. Authentik, Keycloak)
- **Admin UI**: Community-Projekte wie `headscale-ui` oder `headscale-admin`
- **Taildrop-Alternative**: Direkte Dateiübertragung via SSH/SCP

## Deployment

### Docker/Podman

```yaml
# docker-compose.yml
version: '3'
services:
  headscale:
    image: headscale/headscale:latest
    container_name: headscale
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    ports:
      - "8080:8080"      # HTTP
      - "9090:9090"      # gRPC
    command: headscale serve
    restart: unless-stopped
```

### Systemd (Native)

```bash
# Installation
wget https://github.com/juanfont/headscale/releases/latest/download/headscale_linux_amd64
sudo mv headscale_linux_amd64 /usr/local/bin/headscale
sudo chmod +x /usr/local/bin/headscale

# Konfiguration
sudo mkdir -p /etc/headscale
sudo headscale generate private-key > /etc/headscale/private.key
```

```ini
# /etc/systemd/system/headscale.service
[Unit]
Description=Headscale coordination server
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/headscale serve
Restart=always

[Install]
WantedBy=multi-user.target
```

### Kubernetes

- Helm Chart verfügbar: `helm repo add headscale https://charts.headscale.net`
- Ingress für HTTPS-Terminierung
- Persistent Volume für Datenbank (SQLite/PostgreSQL)
- Optional: PostgreSQL als externes Backend für HA

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Headscale als Open-Source-Alternative zu Tailscale Control Server
> - Trennung Control Plane vs. Data Plane
> - Self-Hosting-Gründe: Datensouveränität, Compliance, Air-Gapped
> - Vergleich mit Tailscale, Nebula, ZeroTier

---

## Prüfungstipps

> [!warning] Häufige Klausurfehler
N/A

> [!question] Typische Prüfungsfragen
> - Welche Vorteile bietet Self-Hosting eines Coordination Servers?
> - Wie unterscheidet sich Headscale von vollständig dezentralen Lösungen wie Nebula?
> - Welche Komponenten von Tailscale ersetzt Headscale, welche nicht?
> - Warum könnte ein Unternehmen Headscale gegenüber Tailscale bevorzugen?

> [!tip] Prüfungsvorbereitung
> - Verstehe die Trennung: Control Plane (Koordination, Auth) vs. Data Plane (verschlüsselter Traffic)
> - Kenne die Gründe für Self-Hosting: Datensouveränität, Compliance, Air-Gapped-Umgebungen
> - Vergleiche mit Alternativen: Tailscale (SaaS), Nebula (dezentral), ZeroTier (hybrid)

---

## Weiterführende Ressourcen

- [Headscale Dokumentation](https://headscale.net/) – Offizielle Dokumentation
- [GitHub Repository](https://github.com/juanfont/headscale) – Quellcode und Issues
- [Tailscale Dokumentation](https://tailscale.com/kb/) – Protokoll-Details (gilt auch für Headscale)
- [WireGuard Whitepaper](https://www.wireguard.com/papers/wireguard.pdf) – Kryptographische Grundlagen

---

## Zusammenhänge

- [[00-Overlay-Index]] – Overlay-Netzwerke Übersicht
- [[01-Tailscale]] – Kommerzielle SaaS-Variante mit gleichem Protokoll
- [[02-ZeroTier]] – Alternative mit eigenem Protokoll
- [[03-Nebula]] – Vollständig dezentraler Ansatz ohne zentralen Server

---

## Quellen

- https://github.com/juanfont/headscale
- https://headscale.net/
- https://tailscale.com/blog/how-tailscale-works/

