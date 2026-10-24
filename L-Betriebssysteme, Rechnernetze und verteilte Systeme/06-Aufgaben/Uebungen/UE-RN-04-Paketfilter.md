---
author: Andreas Hümmer
title: Übung - Paketfilter-Regelwerk
tags:
  - uebung
  - rn
  - sicherheit
  - firewall
  - paketfilter
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Übung: Paketfilter-Regelwerk

## Ausgangssituation

Sie sind als Netzwerkadministrator für die Konfiguration einer Perimeter-Firewall verantwortlich. Das Unternehmen hat ein internes Netzwerk (LAN), eine DMZ mit öffentlichen Servern und einen Internetzugang. Sie sollen ein einfaches Paketfilter-Regelwerk erstellen.

---

## Netzwerktopologie

```
                         ┌─────────────┐
                         │  Internet   │
                         │ 0.0.0.0/0   │
                         └──────┬──────┘
                                │
                         ┌──────┴──────┐
                         │  FIREWALL   │
                         │             │
                         │ eth0: WAN   │──── 203.0.113.1 (öffentliche IP)
                         │ eth1: DMZ   │
                         │ eth2: LAN   │
                         └─┬────┬────┬─┘
                           │    │    │
          ┌────────────────┘    │    └────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │     DMZ     │      │     LAN     │      │             │
   │192.168.10.0 │      │192.168.1.0  │      │             │
   │    /24      │      │    /24      │      │             │
   ├─────────────┤      ├─────────────┤      │             │
   │ Webserver   │      │ DNS-Server  │      │             │
   │ .10.10      │      │ .1.10       │      │             │
   │             │      │             │      │             │
   │ Mailserver  │      │ Clients     │      │             │
   │ .10.20      │      │ .1.100-.199 │      │             │
   └─────────────┘      └─────────────┘      └─────────────┘
```

---

## Netzwerkdaten

### Subnetze

| Zone | Subnetz | Interface | Öffentliche IP | Beschreibung |
|------|---------|-----------|----------------|--------------|
| **Internet** | 0.0.0.0/0 | eth0 (WAN) | 203.0.113.1 | Untrusted |
| **DMZ** | 192.168.10.0/24 | eth1 | - | Semi-Trusted |
| **LAN** | 192.168.1.0/24 | eth2 | - | Trusted |

### Server und Clients

| Gerät | Private IP | Öffentliche IP | Zone | Dienste |
|-------|------------|----------------|------|---------|
| **Webserver** | 192.168.10.10 | 203.0.113.10 | DMZ | HTTP (80), HTTPS (443) |
| **Mailserver** | 192.168.10.20 | 203.0.113.20 | DMZ | SMTP (25), SMTPS (465), IMAPS (993) |
| **DNS-Server** | 192.168.1.10 | - | LAN | DNS (53/UDP, 53/TCP) |
| **Clients** | 192.168.1.100-199 | 203.0.113.1 (SNAT) | LAN | Arbeitsplatzrechner |

> [!info] NAT-Konzept
> - **LAN → Internet**: Source-NAT (SNAT/Masquerading) – alle Clients erscheinen mit der öffentlichen IP 203.0.113.1
> - **Internet → DMZ**: Destination-NAT (DNAT/Port-Forwarding) – öffentliche IPs werden auf private DMZ-Server umgesetzt

---

## Anforderungen

### Allgemeine Sicherheitsrichtlinien

1. **Default Policy**: Alles, was nicht explizit erlaubt ist, wird blockiert (Default-Deny)
2. **Minimalprinzip**: Nur die notwendigen Ports und Protokolle erlauben
3. **Zonentrennung**: DMZ und LAN sind strikt getrennt

### Gewünschte Kommunikation

#### Clients → Internet (Web-Browsing)

- LAN-Clients sollen Webseiten im Internet aufrufen können
- Benötigte Protokolle: HTTP (80), HTTPS (443)
- DNS-Auflösung über internen DNS-Server

#### DNS-Auflösung

- Clients fragen den internen DNS-Server (192.168.1.10)
- Der DNS-Server darf DNS-Anfragen ins Internet weiterleiten (Forwarding)

#### DMZ-Zugriff aus dem Internet

- Der Webserver soll aus dem Internet erreichbar sein (HTTP/HTTPS)
- Der Mailserver soll E-Mails empfangen können (SMTP)

#### Verbotene Kommunikation

- **DMZ → LAN**: Kein direkter Zugriff (Schutz vor kompromittierten DMZ-Servern)
- **Internet → LAN**: Kein direkter Zugriff

---

## Aufgaben

### Aufgabe 1: Regelwerk-Tabelle erstellen (10 Punkte)

Erstellen Sie ein vereinfachtes Paketfilter-Regelwerk als Tabelle. Verwenden Sie folgendes Format:

| Nr. | Aktion | Protokoll | Quelle | Ziel | Dest-Port | NAT | Beschreibung |
|-----|--------|-----------|--------|------|-----------|-----|--------------|
| 1 | ? | ? | ? | ? | ? | ? | ? |
| ... | | | | | | | |

**NAT-Spalte:**
- **SNAT**: Source-NAT – Quell-IP wird auf öffentliche IP umgeschrieben (für ausgehenden Traffic)
- **DNAT**: Destination-NAT – Ziel-IP wird auf private IP umgeschrieben (für eingehenden Traffic zu DMZ-Servern)
- **-**: Kein NAT erforderlich (interner Traffic)

**Hinweise:**
- Beginnen Sie mit den spezifischsten Regeln
- Beenden Sie mit der Default-Deny-Regel
- Verwenden Sie "any" für beliebige Quellen/Ziele
- Denken Sie an die **Antwortpakete** (bei Stateless Paketfiltern!)
- Berücksichtigen Sie, dass LAN-Clients mit der öffentlichen IP 203.0.113.1 im Internet erscheinen
- DMZ-Server sind über ihre öffentlichen IPs (203.0.113.10, 203.0.113.20) erreichbar

---

### Aufgabe 2: Abarbeitungsreihenfolge (4 Punkte)

Ein Paket mit folgenden Eigenschaften trifft ein:

```
Protokoll: TCP
Quell-IP: 192.168.1.150 (LAN-Client)
Ziel-IP: 93.184.216.34 (Internet)
Quell-Port: 52431
Ziel-Port: 443
```

**a)** Beschreiben Sie, wie die Firewall dieses Paket gegen Ihr Regelwerk prüft. (2 Punkte)

**b)** Welche Regel greift und was passiert mit dem Paket? (2 Punkte)

---

### Aufgabe 3: Antwortpaket-Problem (4 Punkte)

Bei einem **Stateless** Paketfilter müssen Antwortpakete explizit erlaubt werden.

**a)** Welches Problem entsteht, wenn ein Client eine HTTPS-Verbindung zu einem Webserver im Internet aufbaut? (2 Punkte)

**b)** Welche zusätzliche Regel wäre bei einem reinen Stateless-Filter nötig und welches Sicherheitsrisiko birgt diese? (2 Punkte)

---

### Aufgabe 4: Stateful vs. Stateless (2 Punkte)

Erklären Sie in zwei bis drei Sätzen, wie eine **Stateful Firewall** das Problem aus Aufgabe 3 löst.

---

## Hinweise

### Vereinfachte Notation

Für diese Übung verwenden wir eine vereinfachte Notation:

| Notation | Bedeutung |
|----------|-----------|
| `any` | Beliebige IP-Adresse (0.0.0.0/0) |
| `LAN` | 192.168.1.0/24 |
| `DMZ` | 192.168.10.0/24 |
| `Internet` | Alles außer LAN und DMZ |
| `DNS-Server` | 192.168.1.10 |
| `Webserver` | 192.168.10.10 |
| `Mailserver` | 192.168.10.20 |

### Wichtige Ports

| Port | Protokoll | Dienst |
|------|-----------|--------|
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 25 | TCP | SMTP |
| 465 | TCP | SMTPS |
| 993 | TCP | IMAPS |

### First-Match-Wins

> [!warning] Reihenfolge beachten!
> Die Firewall arbeitet die Regeln **von oben nach unten** ab. Die **erste passende Regel** entscheidet – nachfolgende Regeln werden nicht mehr geprüft.

---

## Bewertung

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Regelwerk-Tabelle | 10 |
| 2 | Abarbeitungsreihenfolge | 4 |
| 3 | Antwortpaket-Problem | 4 |
| 4 | Stateful vs. Stateless | 2 |
| **Gesamt** | | **20** |

---

## Musterlösung

> [!tip] **Für Dozenten**
> Die ausführliche Musterlösung finden Sie hier:
> 
> [[../Loesungen/LOE-UE-RN-04-Paketfilter|→ Musterlösung Paketfilter-Regelwerk]]

---

## Weiterführende Themen

- [[../../03-Rechnernetze/05-Sicherheit/01-Firewalls|Firewalls]] – Paketfilter, Stateful, NGFW
- [[../../03-Rechnernetze/05-Sicherheit/03-TLS|TLS]] – Verschlüsselte Kommunikation
- [[../../03-Rechnernetze/04-Basisprotokolle/03-DNS|DNS]] – Domain Name System
