---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - adressierung
  - netzwerk
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# Adressierungskonzepte in Netzwerken

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Adresstypen im Netzwerk unterscheiden können
> - Den Zusammenhang zwischen MAC- und IP-Adresse verstehen
> - Unicast, Broadcast und Multicast erklären können
> - Die Rolle von Ports verstehen

---

## Überblick

In Netzwerken werden verschiedene Adressierungsebenen verwendet, um Daten an das richtige Ziel zu leiten. Jede OSI-Schicht hat ihre eigene Adressierungsmethode.

## Adressierungsebenen

| OSI-Layer | Adresstyp | Beispiel | Reichweite |
|-----------|-----------|----------|------------|
| **Layer 2** | MAC-Adresse | `00:1A:2B:3C:4D:5E` | Lokal (Broadcastdomain) |
| **Layer 3** | IP-Adresse | `192.168.1.100` | Global (Internet) |
| **Layer 4** | Port | `80`, `443`, `22` | Anwendung auf Host |
| **Layer 7** | Hostname/URL | `www.example.com` | Logisch (DNS) |

## Adresstypen

### Unicast
- **Ziel**: Genau ein Empfänger
- **Beispiel**: `192.168.1.50`
- **Verwendung**: Normale Kommunikation zwischen zwei Hosts

### Broadcast
- **Ziel**: Alle Geräte im Netzwerk
- **Layer 2**: `FF:FF:FF:FF:FF:FF`
- **Layer 3**: Höchste IP im Subnetz (z.B. `192.168.1.255`)
- **Verwendung**: ARP-Requests, DHCP-Discovery

### Multicast
- **Ziel**: Definierte Gruppe von Empfängern
- **IPv4-Bereich**: `224.0.0.0` – `239.255.255.255`
- **Verwendung**: Streaming, Routing-Protokolle

```
UNICAST              BROADCAST            MULTICAST
    
  ○                    ○ ○ ○               ○   ○
  │                    │ │ │               │   │
  ↓                    ↓ ↓ ↓               ↓   ↓
  ●                    ● ● ●               ●   ●
                       ↑                       │
Ein Sender,         Ein Sender,          Ein Sender,
ein Empfänger      alle Empfänger      Gruppe Empfänger
```

## Ports (Layer 4)

Ports identifizieren Anwendungen auf einem Host:

### Portbereiche

| Bereich | Portnummern | Bezeichnung |
|---------|-------------|-------------|
| Well-Known | 0 – 1023 | Standarddienste |
| Registered | 1024 – 49151 | Registrierte Anwendungen |
| Dynamic | 49152 – 65535 | Temporäre Ports |

### Wichtige Well-Known Ports

| Port | Protokoll | Dienst |
|------|-----------|--------|
| 20/21 | TCP | FTP (Daten/Steuerung) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (Server/Client) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 3389 | TCP | RDP |

## Socket-Adresse

Eine vollständige Verbindung wird durch einen **Socket** identifiziert:

```
IP-Adresse : Port
192.168.1.100:443
```

Eine TCP-Verbindung ist eindeutig durch:
- Quell-IP + Quell-Port
- Ziel-IP + Ziel-Port

## Adressauflösung

### ARP (Address Resolution Protocol)

Löst IP-Adressen in MAC-Adressen auf (Layer 3 → Layer 2):

```
1. Host A: "Wer hat 192.168.1.5?" (Broadcast)
2. Host B: "Ich! MAC = 00:1A:2B:3C:4D:5E"
3. Host A speichert Zuordnung im ARP-Cache
```

### DNS (Domain Name System)

Löst Hostnamen in IP-Adressen auf:

```
www.example.com → 93.184.216.34
```

## NAT (Network Address Translation)

Übersetzt private IP-Adressen in öffentliche:

```
Intern:  192.168.1.100:54321
         ↓ NAT
Extern:  203.0.113.1:12345
```

**Typen:**
- **SNAT**: Source NAT (ausgehend)
- **DNAT**: Destination NAT (Port-Forwarding)
- **PAT**: Port Address Translation (viele intern → eine extern)

## Zusammenhänge

- → [[06-MAC-Adressen|MAC-Adressen (Layer 2)]]
- → [[08-IPv4-Adressen|IPv4-Adressen (Layer 3)]]
- → [[02-Grundbegriffe|Grundbegriffe]]

> [!warning] **Prüfungsrelevant**
> - Unterschied MAC-Adresse vs. IP-Adresse
> - Unicast, Broadcast, Multicast
> - Well-Known Ports (HTTP=80, HTTPS=443, SSH=22, DNS=53)
> - ARP-Funktion
> - NAT-Grundprinzip

> [!question] **Typische Prüfungsfragen**
> - Auf welcher Schicht arbeiten Ports?
> - Welcher Port wird für HTTPS verwendet?
> - Was ist der Unterschied zwischen Unicast und Broadcast?
> - Erklären Sie die Funktion von ARP.
> - Warum wird NAT eingesetzt?

## Quellen

- proTirone: LF03:06 Adressierung (Karsten Reincke, CC-BY-4.0)
- RFC 1918: Private Adressen
- RFC 826: ARP

> [!tip] **Weiterführende Links**
> - [IANA Port Numbers](https://www.iana.org/assignments/service-names-port-numbers)
> - [[06-MAC-Adressen|Nächstes Kapitel: MAC-Adressen]]
