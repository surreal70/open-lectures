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
modified: '2026-10-24'
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

OpenVPN unterstützt zwei Modi für unterschiedliche Einsatzszenarien:

### TUN-Modus (Layer 3)

- Routet **IP-Pakete** durch den Tunnel
- Punkt-zu-Punkt-Verbindung zwischen Client und Server
- Effizienter, da nur IP-Traffic übertragen wird
- **Standardwahl** für die meisten VPN-Szenarien

### TAP-Modus (Layer 2)

- Bridged Ethernet – tunnelt komplette **Ethernet-Frames**
- Ermöglicht Layer-2-Protokolle (ARP, DHCP, NetBIOS)
- Notwendig für **Broadcasts und Multicast**
- Anwendung: Windows-Dateifreigaben, Wake-on-LAN über VPN

> [!tip] **Wann welchen Modus?**
> - **TUN:** Standard für Internet-Zugang, Site-to-Site VPN, Remote Access
> - **TAP:** Wenn das entfernte Netz wie ein lokales LAN erscheinen soll

## Architektur

### Client-Server-Modell

OpenVPN arbeitet im klassischen Client-Server-Modell:
- **Server:** Wartet auf eingehende Verbindungen, verwaltet Clients
- **Clients:** Verbinden sich zum Server, erhalten IP-Konfiguration
- Multi-Client-Fähig: Ein Server kann viele Clients bedienen

### PKI und Zertifikate

OpenVPN nutzt eine Public Key Infrastructure (PKI) für sichere Authentifizierung:

| Komponente | Funktion |
|------------|----------|
| **CA (Certificate Authority)** | Signiert alle Zertifikate, Vertrauensanker |
| **Server-Zertifikat** | Authentifiziert den Server gegenüber Clients |
| **Client-Zertifikat** | Authentifiziert jeden Client individuell |
| **DH-Parameter** | Diffie-Hellman für Perfect Forward Secrecy |
| **TLS-Auth Key** | Zusätzlicher HMAC-Schutz gegen DoS |

> [!info] **easy-rsa**
> Das Tool `easy-rsa` vereinfacht die PKI-Verwaltung: CA erstellen, Zertifikate ausstellen, CRLs verwalten.

### Control Channel vs. Data Channel

OpenVPN trennt Steuerung und Daten:

**Control Channel (TLS):**
- Handshake, Authentifizierung, Schlüsselaustausch
- Verwendet vollständiges TLS-Protokoll
- Zertifikatvalidierung, Renegotiation

**Data Channel:**
- Eigentlicher VPN-Traffic (verschlüsselte Pakete)
- Verwendet ausgehandelte symmetrische Schlüssel
- Optimiert für Durchsatz (weniger Overhead als TLS)

## Konfiguration

### Server-Konfiguration

```ini
# /etc/openvpn/server.conf
port 1194
proto udp
dev tun

ca ca.crt
cert server.crt
key server.key
dh dh2048.pem

server 10.8.0.0 255.255.255.0
push "redirect-gateway def1"
push "dhcp-option DNS 1.1.1.1"

keepalive 10 120
cipher AES-256-GCM
auth SHA256

persist-key
persist-tun
verb 3
```

### Client-Konfiguration

```ini
# client.ovpn
client
dev tun
proto udp
remote vpn.example.com 1194

ca ca.crt
cert client.crt
key client.key

cipher AES-256-GCM
auth SHA256
verb 3
```

### easy-rsa für Zertifikate

```bash
# PKI initialisieren
./easyrsa init-pki

# CA erstellen
./easyrsa build-ca

# Server-Zertifikat
./easyrsa gen-req server nopass
./easyrsa sign-req server server

# Client-Zertifikat
./easyrsa gen-req client1 nopass
./easyrsa sign-req client client1

# Diffie-Hellman Parameter
./easyrsa gen-dh
```

## Vor- und Nachteile

### Vorteile

**Flexibilität:**
- Läuft auf fast allen Plattformen (Windows, macOS, Linux, BSD, Android, iOS)
- TCP-Modus ermöglicht Traversal durch restriktive Firewalls (Port 443)
- Layer 2 (TAP) oder Layer 3 (TUN) wählbar
- Viele Authentifizierungsoptionen (Zertifikate, LDAP, RADIUS, 2FA)

**Portabilität:**
- User-Space-Implementierung – keine Kernel-Module nötig
- Einfache Installation ohne Root-Rechte möglich
- Gut geeignet für eingeschränkte Umgebungen

**Reife und Ökosystem:**
- Seit 2001 entwickelt, sehr ausgereift
- Große Community, umfangreiche Dokumentation
- Viele GUI-Clients verfügbar

### Nachteile

**Performance:**
- User-Space = Context-Switches zwischen Kernel und User-Space
- Deutlich langsamer als WireGuard oder IPsec (Kernel)
- Höhere CPU-Last bei gleicher Bandbreite

**Komplexität:**
- PKI-Setup erfordert Wissen über Zertifikate
- Viele Konfigurationsoptionen können verwirren
- ~100.000 Zeilen Code (schwerer zu auditieren)

| Aspekt | OpenVPN | WireGuard |
|--------|---------|-----------|
| Durchsatz | ~200-400 Mbps | ~1000 Mbps |
| CPU-Last | Hoch | Niedrig |
| Plattformen | Sehr viele | Viele (weniger) |
| Firewall-Traversal | Exzellent (TCP 443) | Eingeschränkt (nur UDP) |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - TUN (Layer 3, IP-Routing) vs. TAP (Layer 2, Bridging)
> - TLS-basierte Verschlüsselung
> - PKI mit CA, Server- und Client-Zertifikaten
> - Control Channel (TLS) vs. Data Channel (symmetrisch)
> - UDP bevorzugt, TCP möglich (Firewall-Traversal)
> - TCP-over-TCP-Problem

---

## Prüfungstipps

> [!warning] **Häufige Klausurfehler**
> - TUN und TAP verwechseln
> - TCP-over-TCP-Problem nicht kennen

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen TUN und TAP?
> 2. Warum ist TCP-over-TCP problematisch?
> 3. Welche Komponenten gehören zur OpenVPN-PKI?
> 4. Warum ist OpenVPN langsamer als WireGuard?
> 5. Wann würde man TAP statt TUN verwenden?
> 6. Was macht der Control Channel vs. Data Channel?

> [!tip] **Merkhilfen**
> - **TUN** = **TUN**nel = Layer 3 = IP-Pakete routen
> - **TAP** = **TAP** = Layer 2 = Ethernet bridgen
> - **UDP 1194** = Standardport (UDP bevorzugt!)
> - **TCP 443** = Firewall-Traversal (HTTPS-Port)
> - **User-Space** = Portabel aber langsamer
> - **easy-rsa** = PKI-Management-Tool

---

## Weiterführende Ressourcen

> [!note] **Offizielle Dokumentation**
> - [openvpn.net](https://openvpn.net/) – Offizielle Projektseite
> - [Community Wiki](https://community.openvpn.net/openvpn/wiki) – Anleitungen und HOWTOs

> [!tip] **Praktische Tools**
> - **easy-rsa** → PKI-Verwaltung für Zertifikate
> - **OpenVPN GUI** → Windows-Client mit Tray-Icon
> - **Tunnelblick** → macOS-Client
> - **Wireshark** → OpenVPN-Traffic analysieren (Filter: `openvpn`)

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[../03-TLS|TLS]] → Verwendetes Sicherheitsprotokoll für Control Channel
- [[02-WireGuard]] → Modernere, schnellere Alternative
- [[01-IPsec]] → Kernel-basierte Alternative mit ähnlicher Komplexität

---

## Quellen

- OpenVPN Inc.: OpenVPN Documentation – Offizielle Referenz und Konfigurationsanleitungen.
- openvpn.net – Projektseite mit Downloads und Community-Ressourcen.
- Feilner, Markus: OpenVPN – Building and Integrating Virtual Private Networks – Praxisbuch zur OpenVPN-Administration.

