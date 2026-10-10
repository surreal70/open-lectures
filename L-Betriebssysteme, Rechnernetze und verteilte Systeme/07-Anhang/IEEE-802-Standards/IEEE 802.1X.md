---
author: Andreas Hümmer
title: IEEE 802.1X - Port-based Network Access Control
tags:
  - ieee
  - security
  - authentication
  - 802.1X
  - radius
created: '2026-10-07'
---

# IEEE 802.1X - Port-based Network Access Control

## Kurzübersicht

**IEEE 802.1X** definiert einen Authentifizierungsmechanismus für den Zugang zu LANs. Geräte müssen sich authentifizieren, bevor sie Netzwerkzugang erhalten. Weit verbreitet in Enterprise-WLANs und gesicherten kabelgebundenen Netzen.

| Eigenschaft | Wert |
|-------------|------|
| Erste Veröffentlichung | 2001 |
| Aktuelle Version | IEEE 802.1X-2020 |
| Authentifizierung | EAP (Extensible Authentication Protocol) |
| Backend | RADIUS Server |

## Architektur

```
┌─────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Supplicant │────│   Authenticator  │────│  Authentication │
│   (Client)  │    │ (Switch/AP)      │    │     Server      │
│             │    │                  │    │    (RADIUS)     │
└─────────────┘    └─────────────────┘    └─────────────────┘
     EAP              EAP over LAN           RADIUS
```

## Rollen

| Rolle | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Supplicant** | Client der Zugang anfordert | PC, Smartphone |
| **Authenticator** | Netzwerkgerät als Gatekeeper | Switch, Access Point |
| **Authentication Server** | Prüft Credentials | RADIUS-Server |

## Port-Zustände

| Zustand | Beschreibung |
|---------|--------------|
| **Unauthorized** | Nur EAP-Traffic erlaubt |
| **Authorized** | Voller Netzwerkzugang |

## Häufige EAP-Methoden

| Methode | Beschreibung | Credentials |
|---------|--------------|-------------|
| EAP-TLS | Zertifikatsbasiert | Client-Zertifikat |
| EAP-TTLS | Tunneled TLS | Username/Passwort |
| PEAP | Protected EAP | Username/Passwort |
| EAP-FAST | Cisco proprietär | PAC + Passwort |

## Offizielle Quelle

> [!tip] IEEE-Referenz
> **IEEE 802.1X-2020**: Port-Based Network Access Control
> - URL: https://standards.ieee.org/ieee/802.1X/7345/
> - Working Group: https://www.ieee802.org/1/

---

*Quelle: IEEE Standards Association*
