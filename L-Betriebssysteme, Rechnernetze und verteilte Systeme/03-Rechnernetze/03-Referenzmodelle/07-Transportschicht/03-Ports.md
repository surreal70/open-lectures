---
author: Andreas Hümmer
title: Ports und Sockets
tags:
  - content
  - rn
  - transport-layer
  - ports
  - sockets
  - multiplexing
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Ports und Sockets

## Definition

**Ports** sind 16-Bit-Nummern (0-65535), die auf der Transportschicht die Zuordnung von Netzwerkverkehr zu spezifischen Anwendungen oder Diensten ermöglichen (Multiplexing/Demultiplexing).

## Multiplexing und Demultiplexing

```
┌────────────────────────────────────────────────────────────────┐
│                    Multiplexing/Demultiplexing                 │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  SENDER (Multiplexing):                                        │
│                                                                │
│    Browser    E-Mail     SSH                                   │
│    (HTTP)     (SMTP)    Client                                 │
│       │          │         │                                   │
│       ▼          ▼         ▼                                   │
│    ┌─────────────────────────────┐                            │
│    │      Transportschicht       │                            │
│    │  Fügt Quell-/Zielport hinzu │                            │
│    └─────────────────────────────┘                            │
│                   │                                            │
│                   ▼                                            │
│              Netzwerk                                          │
│                                                                │
│  EMPFÄNGER (Demultiplexing):                                   │
│                                                                │
│              Netzwerk                                          │
│                   │                                            │
│                   ▼                                            │
│    ┌─────────────────────────────┐                            │
│    │      Transportschicht       │                            │
│    │  Verteilt nach Zielport     │                            │
│    └─────────────────────────────┘                            │
│       │          │         │                                   │
│       ▼          ▼         ▼                                   │
│    Webserver  Mailserver  SSH                                  │
│    (Port 80)  (Port 25)   (Port 22)                           │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Port-Bereiche

Die IANA (Internet Assigned Numbers Authority) teilt Ports in drei Bereiche:

| Bereich | Portnummern | Bezeichnung | Verwendung |
|---------|-------------|-------------|------------|
| **Well-Known** | 0 - 1023 | System Ports | Standarddienste (root erforderlich) |
| **Registered** | 1024 - 49151 | User Ports | Registrierte Anwendungen |
| **Dynamic** | 49152 - 65535 | Ephemeral Ports | Temporäre Client-Ports |

```
┌────────────────────────────────────────────────────────────────┐
│                      Port-Bereiche                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  0        1023      49151        65535                        │
│  │         │          │            │                          │
│  ├─────────┼──────────┼────────────┤                          │
│  │Well-Known│Registered│  Dynamic   │                          │
│  │  Ports  │  Ports   │   Ports    │                          │
│  ├─────────┼──────────┼────────────┤                          │
│  │         │          │            │                          │
│  │ HTTP:80 │MySQL:3306│ Client-    │                          │
│  │ SSH:22  │RDP:3389  │ Verbind.   │                          │
│  │ DNS:53  │          │ 49152-     │                          │
│  │         │          │ 65535      │                          │
│  └─────────┴──────────┴────────────┘                          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Wichtige Well-Known Ports

### TCP-Ports

| Port | Dienst | Beschreibung |
|------|--------|--------------|
| 20 | FTP-Data | Datenübertragung |
| 21 | FTP-Control | Steuerkanal |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Unverschlüsselter Remote-Zugang |
| 25 | SMTP | E-Mail-Versand |
| 53 | DNS | Namensauflösung (auch UDP) |
| 80 | HTTP | Webserver |
| 110 | POP3 | E-Mail-Abruf |
| 143 | IMAP | E-Mail-Zugriff |
| 443 | HTTPS | Verschlüsseltes HTTP |
| 465 | SMTPS | SMTP über TLS |
| 587 | SMTP-Submission | E-Mail-Einlieferung |
| 993 | IMAPS | IMAP über TLS |
| 995 | POP3S | POP3 über TLS |

### UDP-Ports

| Port | Dienst | Beschreibung |
|------|--------|--------------|
| 53 | DNS | Namensauflösung |
| 67 | DHCP-Server | IP-Adressvergabe |
| 68 | DHCP-Client | IP-Adressanfrage |
| 69 | TFTP | Trivial File Transfer |
| 123 | NTP | Zeitsynchronisation |
| 161 | SNMP | Netzwerkmanagement |
| 162 | SNMP-Trap | SNMP-Benachrichtigungen |
| 500 | IKE | IPsec Key Exchange |
| 514 | Syslog | System-Logging |

### Häufige Registered Ports

| Port | Dienst | Beschreibung |
|------|--------|--------------|
| 1433 | MS-SQL | Microsoft SQL Server |
| 1521 | Oracle | Oracle Database |
| 3306 | MySQL | MySQL/MariaDB |
| 3389 | RDP | Remote Desktop Protocol |
| 5432 | PostgreSQL | PostgreSQL Database |
| 5900 | VNC | Virtual Network Computing |
| 6379 | Redis | Redis Database |
| 8080 | HTTP-Alt | Alternativer HTTP-Port |
| 8443 | HTTPS-Alt | Alternativer HTTPS-Port |
| 27017 | MongoDB | MongoDB Database |

## Sockets

### Socket-Definition

Ein **Socket** ist ein Kommunikationsendpunkt, definiert durch:

```
Socket = (IP-Adresse, Portnummer, Protokoll)

Beispiel:
  TCP-Socket: (192.168.1.10, 50000, TCP)
  UDP-Socket: (192.168.1.10, 50000, UDP)
```

### Verbindungs-Tupel

Eine TCP-Verbindung ist eindeutig durch ein **5-Tupel** identifiziert:

```
┌────────────────────────────────────────────────────────────────┐
│                    TCP-Verbindungs-Tupel                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  (Protokoll, Quell-IP, Quell-Port, Ziel-IP, Ziel-Port)        │
│                                                                │
│  Beispiel:                                                     │
│  (TCP, 192.168.1.10, 52345, 93.184.216.34, 443)               │
│        └────────────────┘   └───────────────────┘              │
│           Client-Socket        Server-Socket                   │
│                                                                │
│  ┌─────────────────┐           ┌─────────────────┐            │
│  │    Client       │           │     Server      │            │
│  │ 192.168.1.10    │           │ 93.184.216.34   │            │
│  │                 │           │                 │            │
│  │ Socket:         │           │ Socket:         │            │
│  │ Port 52345  ────┼───────────┼──► Port 443     │            │
│  │ (ephemeral)     │           │ (well-known)    │            │
│  └─────────────────┘           └─────────────────┘            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Mehrere Verbindungen zum gleichen Server

```
┌────────────────────────────────────────────────────────────────┐
│              Mehrere Clients, ein Server                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Client A                        Server                        │
│  192.168.1.10                    10.0.0.5                      │
│  ┌───────────┐                   ┌───────────┐                │
│  │Port 50001 │───────────────────│           │                │
│  │Port 50002 │───────────────────│  Port 80  │                │
│  └───────────┘                   │           │                │
│                                  │           │                │
│  Client B                        │           │                │
│  192.168.1.20                    │           │                │
│  ┌───────────┐                   │           │                │
│  │Port 50001 │───────────────────│           │                │
│  └───────────┘                   └───────────┘                │
│                                                                │
│  Drei unterschiedliche Verbindungen:                          │
│  1. (TCP, 192.168.1.10, 50001, 10.0.0.5, 80)                  │
│  2. (TCP, 192.168.1.10, 50002, 10.0.0.5, 80)                  │
│  3. (TCP, 192.168.1.20, 50001, 10.0.0.5, 80)                  │
│                                                                │
│  Alle drei sind unterscheidbar durch das 5-Tupel!             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Port-Zustandsprüfung

### Netstat / SS

```bash
# Linux: Offene Ports anzeigen
ss -tuln

# Oder mit netstat
netstat -tuln

# Ausgabe:
Proto  Local Address     Foreign Address    State
tcp    0.0.0.0:22        0.0.0.0:*          LISTEN
tcp    0.0.0.0:80        0.0.0.0:*          LISTEN
tcp    192.168.1.10:443  93.184.216.34:52345 ESTABLISHED
udp    0.0.0.0:53        0.0.0.0:*

# Windows: Offene Ports anzeigen
netstat -an
```

### Port-Zustände

| Zustand | Beschreibung |
|---------|--------------|
| **LISTEN** | Wartet auf eingehende Verbindungen |
| **ESTABLISHED** | Aktive Verbindung |
| **TIME_WAIT** | Warte auf verspätete Pakete |
| **CLOSE_WAIT** | Warte auf Schließen durch Anwendung |
| **SYN_SENT** | SYN gesendet, warte auf SYN-ACK |
| **SYN_RECEIVED** | SYN-ACK gesendet, warte auf ACK |

## NAT und Ports

### PAT (Port Address Translation)

```
┌────────────────────────────────────────────────────────────────┐
│                  PAT / NAT Overload                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Internes Netzwerk          NAT-Router         Internet        │
│                                                                │
│  PC1: 192.168.1.10:50001 ─┐                                   │
│                           │   203.0.113.5:10001 ──► Web       │
│  PC2: 192.168.1.11:50001 ─┼─► NAT-Tabelle                     │
│                           │   203.0.113.5:10002 ──► Web       │
│  PC3: 192.168.1.12:52000 ─┘                                   │
│                               203.0.113.5:10003 ──► Web       │
│                                                                │
│  NAT-Tabelle:                                                  │
│  ┌──────────────────────┬──────────────────────┐              │
│  │ Intern               │ Extern               │              │
│  ├──────────────────────┼──────────────────────┤              │
│  │ 192.168.1.10:50001   │ 203.0.113.5:10001    │              │
│  │ 192.168.1.11:50001   │ 203.0.113.5:10002    │              │
│  │ 192.168.1.12:52000   │ 203.0.113.5:10003    │              │
│  └──────────────────────┴──────────────────────┘              │
│                                                                │
│  Eine öffentliche IP, viele interne Hosts!                    │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Port-Scanning und Sicherheit

### Häufige Scan-Techniken

| Technik | Beschreibung | Erkennbarkeit |
|---------|--------------|---------------|
| **TCP Connect** | Vollständiger Handshake | Hoch (geloggt) |
| **SYN Scan** | Nur SYN, kein ACK | Mittel |
| **UDP Scan** | ICMP Port Unreachable | Langsam |
| **FIN/XMAS/NULL** | Ungewöhnliche Flags | Niedrig |

> [!warning] Sicherheitshinweis
> - Nur notwendige Ports öffnen
> - Firewall-Regeln verwenden
> - Regelmäßige Port-Scans zur Überprüfung
> - Dienste auf nicht-Standard-Ports (Security through Obscurity) ist **keine** echte Sicherheit

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. Port-Bereiche (Well-Known, Registered, Dynamic)
> 2. Wichtige Portnummern auswendig kennen
> 3. Socket-Definition und 5-Tupel
> 4. Multiplexing/Demultiplexing erklären
> 5. NAT/PAT-Funktionsweise

### Merkregeln für wichtige Ports

> [!tip] Merkhilfe: Wichtigste Ports
> 
> **Web:** 80 (HTTP), 443 (HTTPS)
> **E-Mail:** 25 (SMTP), 110 (POP3), 143 (IMAP)
> **Datei:** 20/21 (FTP), 22 (SSH/SFTP)
> **Netzwerk:** 53 (DNS), 67/68 (DHCP)
> **Remote:** 22 (SSH), 23 (Telnet), 3389 (RDP)

### Zusammenfassung: Port-Auswahl

```
Client-Anfrage an Webserver:

1. Client wählt ephemeral Port (z.B. 52345)
2. Client verbindet zu Server Port 80 (HTTP)
3. Server antwortet von Port 80 an Port 52345
4. Demultiplexing ordnet Antwort dem Browser zu

Quell-Port: Identifiziert sendende Anwendung
Ziel-Port:  Identifiziert Zieldienst
```

## Zusammenhänge

- [[01-TCP]] - TCP nutzt Ports
- [[02-UDP]] - UDP nutzt Ports
- [[06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]] - IP-Adressen + Ports = Socket
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - Firewall-Regeln basieren auf Ports

## Quellen

- IANA Port Numbers: https://www.iana.org/assignments/service-names-port-numbers
- [[A-RFC-Index|RFC 6335]] - IANA Procedures for Port Assignments
- Tanenbaum, A. S.: Computernetzwerke, Kap. 6
