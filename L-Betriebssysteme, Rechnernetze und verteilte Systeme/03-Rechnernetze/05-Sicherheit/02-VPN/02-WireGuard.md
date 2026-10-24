---
author: Andreas Hümmer
title: WireGuard
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - wireguard
  - modern
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# WireGuard

## Definition

> [!quote] Definition
> **WireGuard** ist ein modernes, schlankes VPN-Protokoll, das auf Layer 3 arbeitet. Es zeichnet sich durch minimalen Code, hohe Geschwindigkeit und starke Kryptographie aus.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 3 (Netzwerk) |
| **Port** | UDP 51820 (Standard) |
| **Codezeilen** | ~4.000 (vs. ~400.000 bei OpenVPN) |
| **Kryptographie** | ChaCha20, Poly1305, Curve25519, BLAKE2s |
| **Kernel-Integration** | Ja (Linux seit 5.6) |

## Vorteile

### Einfachheit und Auditierbarkeit

- **~4.000 Zeilen Code** (vs. ~400.000 bei OpenVPN, ~600.000 bei IPsec-Implementierungen)
- Vollständiger Code-Review in wenigen Stunden möglich
- Weniger Angriffsfläche durch minimale Codebasis
- Keine Legacy-Optionen oder veraltete Algorithmen

### Geschwindigkeit und Latenz

- **Kernel-Space-Implementierung** (kein Context-Switch User/Kernel)
- Deutlich höherer Durchsatz als OpenVPN (oft 2-4x schneller)
- Geringere Latenz durch effizientes Protokolldesign
- Ideal für mobile Anwendungen und Echtzeit-Traffic

### Roaming-Unterstützung

- **Verbindungslos:** Kein Session-State auf Protokollebene
- Automatischer Wechsel zwischen Netzwerken (WLAN → Mobilfunk)
- Peer-Adresse wird bei eingehendem Paket automatisch aktualisiert
- Keine Reconnects nötig bei IP-Wechsel

### Cryptokey Routing

WireGuards innovatives Konzept: Die Routing-Tabelle basiert auf Public Keys.

| Peer Public Key | Allowed IPs |
|-----------------|-------------|
| `abc123...` | 10.0.0.2/32, 192.168.1.0/24 |
| `def456...` | 10.0.0.3/32 |

- **Eingehend:** Paket wird nur akzeptiert, wenn Quell-IP in `AllowedIPs` des Peers
- **Ausgehend:** Ziel-IP bestimmt, welcher Peer-Key für Verschlüsselung verwendet wird
- Einfache Konfiguration: Ein Public Key, eine Liste erlaubter IPs

## Architektur

![[wireguard-concept.png]]
*<span class="fig-id">05-02-02-wireguard-concept</span>: WireGuard Cryptokey Routing – Peers authentifizieren sich nur über Public Keys.*

**Kernprinzipien:**
- Kein zentraler Server – alle Teilnehmer sind gleichberechtigte Peers
- Authentifizierung ausschließlich über Public Keys (keine Zertifikate)
- Kein persistenter Handshake-State auf Protokollebene
- Minimale Angriffsfläche durch feste Kryptographie-Auswahl

## Konfiguration

### Beispielkonfiguration (Server/Peer A)

```ini
[Interface]
PrivateKey = SERVER_PRIVATE_KEY
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = CLIENT_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32
```

### Beispielkonfiguration (Client/Peer B)

```ini
[Interface]
PrivateKey = CLIENT_PRIVATE_KEY
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = vpn.example.com:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

### wg-quick Befehle

```bash
# Schlüsselpaar generieren
wg genkey | tee privatekey | wg pubkey > publickey

# Interface starten
wg-quick up wg0

# Interface stoppen
wg-quick down wg0

# Status anzeigen
wg show

# Detaillierter Status
wg show wg0
```

> [!tip] **PersistentKeepalive**
> Wichtig für Clients hinter NAT: Sendet alle 25 Sekunden ein Keepalive-Paket, um die NAT-Zuordnung aufrechtzuerhalten.

## Vergleich mit IPsec/OpenVPN

### Performance-Vergleich

| Kriterium     | WireGuard   | IPsec (IKEv2) | OpenVPN       |
| ------------- | ----------- | ------------- | ------------- |
| **Durchsatz** | ~1000 Mbps  | ~500-800 Mbps | ~200-400 Mbps |
| **Latenz**    | Sehr gering | Gering        | Mittel        |
| **CPU-Last**  | Niedrig     | Mittel        | Hoch          |
| **Handshake** | 1-RTT       | 2-4 RTT       | 4+ RTT        |

> [!info] **Benchmark-Hinweis**
> Werte variieren stark je nach Hardware, Konfiguration und Verschlüsselungsalgorithmen. WireGuard profitiert besonders von Kernel-Integration.

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
N/A

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist Cryptokey Routing und wie funktioniert es?
> 2. Warum hat WireGuard nur ~4.000 Codezeilen?
> 3. Welche Vorteile bietet die Kernel-Integration?
> 4. Wie funktioniert Roaming bei WireGuard?
> 5. Warum verwendet WireGuard keine Zertifikate?
> 6. Was bedeutet "feste Kryptographie-Auswahl"?

> [!tip] **Merkhilfen**
> - **Cryptokey Routing** = Public Key bestimmt erlaubte IPs
> - **4.000 Zeilen** = Auditierbar, weniger Bugs
> - **Kernel-Space** = Kein Context-Switch = schneller
> - **ChaCha20** = Verschlüsselung (schnell in Software)
> - **Curve25519** = Schlüsselaustausch (ECDH)
> - **UDP 51820** = Standardport
> - **Stateless** = Kein Handshake-State = Roaming funktioniert

---

## Weiterführende Ressourcen

> [!note] **Offizielle Dokumentation**
> - [wireguard.com](https://www.wireguard.com/) – Offizielle Projektseite
> - [WireGuard Whitepaper](https://www.wireguard.com/papers/wireguard.pdf) – Technische Spezifikation

> [!tip] **Praktische Tools**
> - **wg** → WireGuard CLI-Tool für Konfiguration und Status
> - **wg-quick** → Vereinfachte Interface-Verwaltung
> - **Wireshark** → WireGuard-Traffic analysieren (ab Version 3.0)

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[01-IPsec]] → Klassischer Vergleich (komplexer, aber mehr Features)
- [[03-OpenVPN]] → User-Space Alternative (mehr Plattformen)
- [[../03-TLS|TLS]] → Ähnliche moderne Kryptographie-Auswahl

---

## Quellen

- Donenfeld, Jason A.: WireGuard: Next Generation Kernel Network Tunnel – Das offizielle Whitepaper.
- wireguard.com – Offizielle Projektdokumentation und Referenz.
- Linux Kernel Documentation – WireGuard Kernel-Modul (seit Linux 5.6).

