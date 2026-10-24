---
author: Andreas Hümmer
title: SSL VPN
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - ssl
  - tls
  - browser
  - enterprise
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# SSL VPN

## Definition

> [!quote] Definition
> **SSL VPN** (auch TLS VPN) bezeichnet VPN-Lösungen, die auf SSL/TLS basieren und oft über einen Webbrowser zugänglich sind. Sie arbeiten typischerweise auf Layer 7 (Anwendungsschicht).
## Typen

SSL VPNs gibt es in zwei Varianten mit unterschiedlichem Funktionsumfang:

### Portal VPN (Clientless)

- Zugriff **über Webbrowser** – keine Software-Installation nötig
- Reverse Proxy für interne Ressourcen
- **Beschränkt auf Web-Anwendungen** (HTTP/HTTPS)
- Ideal für BYOD und öffentliche Computer
- Typische Funktionen: Webmail, Intranet, Web-basierte Apps

### Tunnel VPN (Full Tunnel)

- **Client-Software erforderlich** (Agent)
- Vollständiger Netzwerkzugriff wie bei IPsec
- Alle Anwendungen nutzbar (nicht nur Web)
- Virtueller Netzwerkadapter wird erstellt
- Split-Tunneling oder Full-Tunneling konfigurierbar

> [!info] **Hybride Lösungen**
> Viele Enterprise-Produkte bieten beide Modi: Portal für einfachen Zugriff, Tunnel für vollständige Konnektivität.

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 7 (Anwendung) / 4 (Transport) |
| **Port** | TCP 443 (HTTPS) |
| **Firewall-Freundlich** | Ja (Standard HTTPS-Port) |
| **Client** | Browser oder dedizierte Software |

## Anbieter/Produkte

Die wichtigsten Enterprise SSL VPN-Lösungen:

| Hersteller | Produkt | Besonderheiten |
|------------|---------|----------------|
| **Cisco** | AnyConnect | Marktführer, umfangreiche Features, Multi-Plattform |
| **Palo Alto** | GlobalProtect | Integration mit Next-Gen Firewall, Always-On VPN |
| **Fortinet** | FortiClient | Teil der Fortinet Security Fabric, kostenlose Basisversion |
| **F5** | BIG-IP APM | Access Policy Manager, starke Authentifizierung |
| **Pulse Secure** | Pulse Connect | Ehemals Juniper, verbreitet in Enterprises |
| **Citrix** | Gateway | Integration mit Citrix-Umgebungen |

> [!info] **Zero Trust Network Access (ZTNA)**
> Moderne SSL VPN-Lösungen entwickeln sich zu ZTNA-Produkten: Statt Netzwerkzugang nur Zugriff auf einzelne Anwendungen, basierend auf Identität und Gerätestatus.

## Vor- und Nachteile

### Vorteile

**Einfache Bereitstellung:**
- Keine Client-Installation bei Portal VPN
- Funktioniert auf jedem Gerät mit Browser
- Ideal für BYOD und Contractor-Zugriff

**Firewall-Freundlichkeit:**
- Port 443 (HTTPS) ist fast überall offen
- Kein Problem mit NAT oder restriktiven Firewalls
- Funktioniert in Hotels, Flughäfen, Unternehmensnetzwerken

**Granulare Zugriffskontrolle:**
- Zugriff auf Anwendungsebene steuerbar
- Integration mit Identity Providern (SAML, LDAP, RADIUS)
- Posture Checking (Gerätestatus prüfen)

### Nachteile

**Performance:**
- Overhead durch TLS-Handshake
- Nur TCP (kein UDP) bei reinem SSL
- Langsamer als IPsec oder WireGuard

**Einschränkungen:**
- Portal VPN: Nur Web-Anwendungen
- Tunnel VPN: Client-Software erforderlich
- Komplexere Architektur als einfache VPNs

| Vergleich | SSL VPN | IPsec VPN |
|-----------|---------|-----------|
| Firewall-Traversal | Exzellent (Port 443) | Problematisch (ESP, UDP 500/4500) |
| Client-Software | Optional (Portal) | Immer erforderlich |
| Performance | Mittel | Gut |
| Zugriffskontrolle | Granular (App-Level) | Netzwerk-Level |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Portal VPN (clientless, Browser-basiert) vs. Tunnel VPN (Client-Software)
> - Firewall-Traversal über HTTPS (Port 443)
> - TLS-basierte Verschlüsselung
> - Granulare Zugriffskontrolle auf Anwendungsebene
> - Typische Anbieter: Cisco AnyConnect, Pulse Secure, F5 BIG-IP

---

## Prüfungstipps

> [!warning] **Häufige Klausurfehler**
> - Portal VPN und Tunnel VPN verwechseln
> - SSL VPN mit OpenVPN verwechseln (SSL VPN ist meist kommerziell)

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen Portal VPN und Tunnel VPN?
> 2. Warum ist SSL VPN firewall-freundlicher als IPsec?
> 3. Welche Einschränkungen hat ein Portal VPN?
> 4. Auf welcher Schicht arbeitet SSL VPN?
> 5. Wann würde man SSL VPN statt IPsec wählen?

> [!tip] **Merkhilfen**
> - **Portal** = Browser-basiert = nur Web-Apps
> - **Tunnel** = Client-Software = voller Netzwerkzugriff
> - **Port 443** = HTTPS = überall offen
> - **Layer 7** = Anwendungsschicht (Portal)
> - **ZTNA** = Nachfolger von SSL VPN

---

## Weiterführende Ressourcen

> [!note] **Enterprise-Dokumentation**
> - Cisco AnyConnect Administrator Guide
> - Palo Alto GlobalProtect Admin Guide
> - NIST SP 800-77: Guide to IPsec VPNs (Vergleich)

> [!tip] **Praktische Tools**
> - **Browser Developer Tools** → TLS-Handshake analysieren
> - **Wireshark** → SSL/TLS-Traffic inspizieren

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[../03-TLS|TLS]] → Zugrundeliegendes Sicherheitsprotokoll
- [[01-IPsec]] → Alternative Technologie (Layer 3)
- [[03-OpenVPN]] → Open-Source SSL-basiertes VPN

---

## Quellen

- NIST SP 800-113: Guide to SSL VPNs – Referenzarchitektur und Sicherheitsempfehlungen.
- Cisco Systems: AnyConnect Secure Mobility Client Administrator Guide.
- Gartner: Magic Quadrant for Enterprise Network Firewalls – Marktübersicht SSL VPN-Anbieter.

