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
modified: '2026-10-24'
bereich: RN
---

# Ports und Sockets

> [!info] Lernziele
> Nach diesem Kapitel können Sie...
> - Die Funktion von Ports für Multiplexing/Demultiplexing erklären
> - Die Port-Bereiche (Well-Known, Registered, Dynamic) unterscheiden
> - Wichtige Port-Nummern und deren Dienste nennen
> - Den Unterschied zwischen Ports und Sockets erklären

## Definition

> [!quote] Definition
> **Ports** sind 16-Bit-Nummern (0-65535), die auf der Transportschicht die Zuordnung von Netzwerkverkehr zu spezifischen Anwendungen oder Diensten ermöglichen (Multiplexing/Demultiplexing).
## Multiplexing und Demultiplexing

![[multiplexing-demultiplexing.png]]
*<span class="fig-id">03-07-03-multiplexing-demultiplexing</span>: Multiplexing am Sender und Demultiplexing am Empfänger*

## Port-Bereiche

Die IANA (Internet Assigned Numbers Authority) teilt Ports in drei Bereiche:

| Bereich | Portnummern | Bezeichnung | Verwendung |
|---------|-------------|-------------|------------|
| **Well-Known** | 0 - 1023 | System Ports | Standarddienste (privilegiert) |
| **Registered** | 1024 - 49151 | User Ports | Registrierte Anwendungen |
| **Dynamic** | 49152 - 65535 | Ephemeral Ports | Temporäre Client-Ports |

> [!warning] Privilegierte Ports
> Die Well-Known Ports (0-1023) sind **privilegierte Ports**. Anwendungen, die sich an diese Ports binden wollen, benötigen erhöhte Systemrechte:
> - **Linux/Unix:** Root-Rechte (`sudo`) oder `CAP_NET_BIND_SERVICE` Capability
> - **Windows:** Administrator-Rechte
> 
> Dies ist ein Sicherheitsmechanismus: Nur vertrauenswürdige Systemdienste sollen auf Standardports lauschen können.

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

| Element | Beschreibung | Beispielwert |
|---------|--------------|--------------|
| **Protokoll** | TCP oder UDP | TCP |
| **Quell-IP** | IP-Adresse des Clients | 192.168.1.10 |
| **Quell-Port** | Port des Clients (ephemeral) | 52345 |
| **Ziel-IP** | IP-Adresse des Servers | 93.184.216.34 |
| **Ziel-Port** | Port des Dienstes (well-known) | 443 |

> [!example] Beispiel-Verbindung
> **Client-Socket:** `192.168.1.10:52345` (ephemeral Port)
> **Server-Socket:** `93.184.216.34:443` (HTTPS)
> 
> Das vollständige 5-Tupel: `(TCP, 192.168.1.10, 52345, 93.184.216.34, 443)`

### Mehrere Verbindungen zum gleichen Server

![[multiple-clients-server.png]]
*<span class="fig-id">03-07-03-multiple-clients-server</span>: Mehrere Clients verbunden mit einem Server auf Port 80*

**Drei unterschiedliche Verbindungen:**
1. `(TCP, 192.168.1.10, 50001, 10.0.0.5, 80)` – Client A, erste Verbindung
2. `(TCP, 192.168.1.10, 50002, 10.0.0.5, 80)` – Client A, zweite Verbindung
3. `(TCP, 192.168.1.20, 50001, 10.0.0.5, 80)` – Client B

> [!tip] Eindeutigkeit durch 5-Tupel
> Obwohl Client A und Client B beide Port 50001 verwenden, sind die Verbindungen durch unterschiedliche Quell-IPs eindeutig unterscheidbar.

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

![[pat-nat-overload.png]]
*<span class="fig-id">03-07-03-pat-nat-overload</span>: PAT/NAT Overload – Eine öffentliche IP für viele interne Hosts*

> [!info] NAT Overload / PAT
> Bei PAT (Port Address Translation) teilen sich mehrere interne Hosts eine einzige öffentliche IP-Adresse. Der Router unterscheidet die Verbindungen anhand der **Port-Nummern** in seiner NAT-Tabelle.

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

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Port-Bereiche (Well-Known, Registered, Dynamic)
> - Wichtige Portnummern auswendig kennen
> - Socket-Definition und 5-Tupel
> - Multiplexing/Demultiplexing erklären
> - NAT/PAT-Funktionsweise

> [!question] Typische Prüfungsfragen
> - Nennen Sie die drei Port-Bereiche und ihre Nummerierung.
> - Was ist ein Socket und aus welchen Komponenten besteht das 5-Tupel?
> - Erklären Sie Multiplexing und Demultiplexing auf der Transportschicht.
> - Welche Portnummer hat HTTP/HTTPS/SSH/DNS?
> - Wie funktioniert NAT/PAT und welche Rolle spielen Ports dabei?

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
