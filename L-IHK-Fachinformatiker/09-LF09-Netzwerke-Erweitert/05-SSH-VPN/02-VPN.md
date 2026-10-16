---
title: "VPN – Virtual Private Network"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - vpn
  - sicherheit
  - tunnel
source: proTirone (CC-BY-4.0)
---

# VPN – Virtual Private Network

> [!info] Lernziele
> - VPN-Konzept verstehen
> - Unterschied zwischen SSH-Tunnel und VPN erklären
> - VPN-Typen unterscheiden
> - Einsatzszenarien kennen

## Definition

> [!quote] Wikipedia
> "Virtual Private Network (deutsch ‚virtuelles privates Netzwerk'; kurz: VPN) bezeichnet eine Netzwerkverbindung, die von Unbeteiligten nicht einsehbar ist."

Ein VPN schafft eine **private Netzwerkverbindung** zwischen Geräten über das Internet:
- **Sichere** und **anonyme** Datenübertragung über öffentliche Netze
- **Maskierung** der IP-Adressen
- **Verschlüsselung** aller Daten

## VPN vs. SSH-Tunnel

### SSH-Tunnel

```
┌─────────┐                    ┌─────────┐
│ Client  │═══════════════════▶│ Server  │
│         │   SSH-Verbindung   │         │
│ Port X  │◄══════════════════▶│ Port Y  │
└─────────┘                    └─────────┘
         Einzelne Portweiterleitung
```

- Leitet **einzelne Ports** weiter
- Temporär für spezifische Anwendungen
- Keine Systemweite Integration

### VPN

```
┌─────────────────────────────────────────────────────────────────┐
│                         VPN-TUNNEL                              │
│  ┌─────────┐                                    ┌─────────┐     │
│  │VPN-Client│══════════════════════════════════▶│VPN-Server│    │
│  └────┬────┘         Verschlüsselt              └────┬────┘     │
│       │                                              │          │
│  ┌────┴────┐                                    ┌────┴────┐     │
│  │  Alle   │                                    │ Intranet│     │
│  │ Apps    │                                    │ Internet│     │
│  └─────────┘                                    └─────────┘     │
└─────────────────────────────────────────────────────────────────┘
              Gesamter Netzwerkverkehr getunnelt
```

- Leitet **gesamten Netzwerkverkehr** um
- Dauerhafte Systemintegration
- Alle Anwendungen nutzen den Tunnel

## VPN-Funktionsweise

### Ablauf

1. **VPN-Client** fängt alle Netzwerkaufrufe ab
2. **Verschlüsselung** der Daten
3. **Übertragung** zum VPN-Server
4. **VPN-Server** entschlüsselt und leitet weiter:
   - Ins **Intranet** (bei Firmenzugang)
   - Ins **Internet** (bei Anonymisierung)
5. **Antworten** werden verschlüsselt zurückgesendet

### Vorteile

| Vorteil | Beschreibung |
|---------|--------------|
| **Sicherheit** | Ende-zu-Ende-Verschlüsselung |
| **Anonymität** | Externe sehen nur VPN-Server-IP |
| **Zugang** | Zugriff auf interne Ressourcen |
| **Standortunabhängig** | Arbeiten wie im Büro |

## VPN-Typen

### Remote Access VPN

Einzelne Benutzer verbinden sich mit einem Firmennetzwerk:

```
┌─────────┐
│Mitarbeiter│────┐
│ (Home)    │    │
└───────────┘    │     ┌─────────────┐
                 ├────▶│ VPN-Server  │────▶ Firmennetz
┌───────────┐    │     │ (Gateway)   │
│Mitarbeiter│────┘     └─────────────┘
│ (mobil)   │
└───────────┘
```

**Anwendung:** Home-Office, Außendienst

### Site-to-Site VPN

Verbindung ganzer Netzwerke:

```
┌─────────────┐         VPN-Tunnel         ┌─────────────┐
│ Standort A  │═══════════════════════════▶│ Standort B  │
│             │                            │             │
│ ┌─────────┐ │                            │ ┌─────────┐ │
│ │Router/FW│◄┼────────────────────────────┼▶│Router/FW│ │
│ └─────────┘ │                            │ └─────────┘ │
│             │                            │             │
│ ┌───┐ ┌───┐ │                            │ ┌───┐ ┌───┐ │
│ │PC │ │PC │ │                            │ │PC │ │PC │ │
│ └───┘ └───┘ │                            │ └───┘ └───┘ │
└─────────────┘                            └─────────────┘
```

**Anwendung:** Filialvernetzung, Rechenzentren

## VPN-Protokolle

| Protokoll | Layer | Beschreibung |
|-----------|-------|--------------|
| **IPsec** | 3 | Direkt auf IP-Ebene, sehr sicher |
| **OpenVPN** | 4-7 | Open Source, flexibel, SSL/TLS-basiert |
| **WireGuard** | 3 | Modern, schnell, einfache Konfiguration |
| **L2TP/IPsec** | 2-3 | Layer 2 Tunneling mit IPsec-Verschlüsselung |
| **PPTP** | 2 | Veraltet, unsicher ⚠️ |

### IPsec

- Arbeitet auf **Layer 3** (Vermittlungsschicht)
- Verschlüsselt IP-Pakete direkt
- Kann bei NAT Probleme bereiten
- Standard für Site-to-Site VPNs

### OpenVPN

- **SSL/TLS**-basiert
- Läuft über **UDP** (bevorzugt) oder **TCP**
- Sehr verbreitet und gut dokumentiert
- Flexible Konfiguration

### WireGuard

- **Modernes** Protokoll (2020)
- Sehr **schnell** und **effizient**
- Einfache Konfiguration
- Im Linux-Kernel integriert

## Praktische Einrichtung

### WireGuard-Beispiel

**Server-Konfiguration:**
```ini
# /etc/wireguard/wg0.conf
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <server-private-key>

[Peer]
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
```

**Client-Konfiguration:**
```ini
# /etc/wireguard/wg0.conf
[Interface]
Address = 10.0.0.2/24
PrivateKey = <client-private-key>
DNS = 1.1.1.1

[Peer]
PublicKey = <server-public-key>
Endpoint = vpn.example.com:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

**Verbindung starten:**
```bash
# Interface aktivieren
sudo wg-quick up wg0

# Status prüfen
sudo wg show

# Interface deaktivieren
sudo wg-quick down wg0
```

## Sicherheitsaspekte

> [!warning] Wichtige Hinweise
> 1. **VPN ≠ Anonymität**: Der VPN-Anbieter sieht allen Verkehr
> 2. **Vertrauenswürdigkeit**: Nur vertrauenswürdige VPN-Server nutzen
> 3. **Logging-Policy**: Prüfen, ob Anbieter Logs speichert
> 4. **Kill-Switch**: Bei VPN-Abbruch Internet trennen

### Split Tunneling

| Modus | Beschreibung |
|-------|--------------|
| **Full Tunnel** | Gesamter Verkehr durch VPN |
| **Split Tunnel** | Nur bestimmter Verkehr durch VPN |

**Split Tunnel Vorteile:**
- Geringere Latenz für lokale Dienste
- Weniger VPN-Serverbelastung

**Split Tunnel Risiken:**
- Lokaler Verkehr unverschlüsselt
- Potenzielle Sicherheitslücke

---

> [!tip] Übungen
> 1. Vergleichen Sie SSH-Tunnel und VPN anhand konkreter Szenarien
> 2. Richten Sie einen WireGuard-VPN zwischen zwei virtuellen Maschinen ein
> 3. Analysieren Sie den Netzwerkverkehr vor und nach VPN-Aktivierung

## Weiterführende Links

- [WireGuard](https://www.wireguard.com/)
- [OpenVPN](https://openvpn.net/)
- [AWS: Was ist ein VPN?](https://aws.amazon.com/de/what-is/vpn/)
- [Wikipedia: VPN](https://de.wikipedia.org/wiki/Virtual_Private_Network)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
