---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - application-layer
bereich: RN
---

# Anwendungsschicht (Layer 7/5)

> [!info] Einordnung in den Referenzmodellen
> Die Anwendungsschicht ist **Schicht 7** im OSI-Modell bzw. **Schicht 5** (Application Layer) im TCP/IP-Modell. Sie umfasst alle Protokolle, die direkt mit Benutzeranwendungen interagieren.

## Lernziele

Nach diesem Kapitel sollten Sie:

- [ ] Die Aufgaben der Anwendungsschicht erklären können
- [ ] DNS-Funktionsweise und Record-Typen verstehen
- [ ] HTTP/HTTPS-Grundlagen kennen
- [ ] E-Mail-Protokolle (SMTP, IMAP, POP3) unterscheiden können
- [ ] Das Client-Server-Modell erklären können

## Kernaufgaben der Anwendungsschicht

```
┌─────────────────────────────────────────────────────────────────┐
│                   ANWENDUNGSSCHICHT (Layer 7)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  DIENSTE FÜR     │    │  DATENFORMATE    │                  │
│   │  ANWENDUNGEN     │    │  UND KODIERUNG   │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • Namensauflösung│    │ • MIME-Types     │                  │
│   │ • Dateitransfer  │    │ • Zeichensätze   │                  │
│   │ • E-Mail         │    │ • Komprimierung  │                  │
│   │ • Webdienste     │    │ • Verschlüsselung│                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  SITZUNGS-       │    │  BENUTZER-       │                  │
│   │  MANAGEMENT      │    │  AUTHENTIFIZIER. │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • Sessions       │    │ • Login          │                  │
│   │ • Cookies        │    │ • Tokens         │                  │
│   │ • State Mgmt.    │    │ • Zertifikate    │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│              PDU: Nachricht (Message) / Daten                   │
└─────────────────────────────────────────────────────────────────┘
```

## Client-Server vs. Peer-to-Peer

```
┌────────────────────────────────────────────────────────────────┐
│                    Architekturmodelle                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  CLIENT-SERVER:                    PEER-TO-PEER (P2P):         │
│                                                                │
│       ┌─────────┐                   ┌───┐   ┌───┐             │
│       │ Server  │                   │ P │───│ P │             │
│       └────┬────┘                   └─┬─┘   └─┬─┘             │
│      ┌─────┼─────┐                    │   ╲   │               │
│      │     │     │                    │    ╲  │               │
│      ▼     ▼     ▼                  ┌─┴─┐   └─┴─┐             │
│   ┌───┐ ┌───┐ ┌───┐                │ P │─────│ P │             │
│   │ C │ │ C │ │ C │                └───┘     └───┘             │
│   └───┘ └───┘ └───┘                                           │
│                                                                │
│  Beispiele:                        Beispiele:                  │
│  • HTTP, FTP, SMTP                 • BitTorrent                │
│  • DNS, DHCP                       • Blockchain                │
│  • Datenbanken                     • Skype (hybrid)            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Wichtige Anwendungsprotokolle

### Übersicht nach Kategorie

| Kategorie | Protokolle | Ports |
|-----------|------------|-------|
| **Web** | HTTP, HTTPS | 80, 443 |
| **E-Mail** | SMTP, IMAP, POP3 | 25/587, 143/993, 110/995 |
| **Dateitransfer** | FTP, SFTP, TFTP | 20/21, 22, 69 |
| **Namensauflösung** | DNS | 53 |
| **Konfiguration** | DHCP, NTP | 67/68, 123 |
| **Remote Access** | SSH, Telnet, RDP | 22, 23, 3389 |
| **Verzeichnis** | LDAP | 389, 636 |

### Protokoll-Stack-Beispiel

```
┌────────────────────────────────────────────────────────────────┐
│                    HTTP über TCP/IP                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ HTTP GET /index.html HTTP/1.1                            │ │
│  │ Host: www.example.com                                    │ │
│  │ User-Agent: Mozilla/5.0                                  │ │
│  └──────────────────────────────────────────────────────────┘ │
│                         │                                      │
│                         ▼                                      │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ TCP: Src-Port: 52345, Dst-Port: 80, Seq: 1000, ...      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                         │                                      │
│                         ▼                                      │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ IP: Src: 192.168.1.10, Dst: 93.184.216.34, TTL: 64     │ │
│  └──────────────────────────────────────────────────────────┘ │
│                         │                                      │
│                         ▼                                      │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ Ethernet: Src-MAC, Dst-MAC, Type: 0x0800                │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Inhaltsverzeichnis

1. [[../../../04-Basisprotokolle/03-DNS|DNS]] - Domain Name System (→ Basisprotokolle)
2. [[02-HTTP]] - Hypertext Transfer Protocol
3. [[03-SMTP]] - E-Mail-Protokolle

## Weitere wichtige Protokolle (Kurzübersicht)

### DHCP (Dynamic Host Configuration Protocol)

- **Funktion:** Automatische IP-Konfiguration
- **Ports:** UDP 67 (Server), UDP 68 (Client)
- **Ablauf:** DORA (Discover, Offer, Request, Acknowledge)
- **Siehe auch:** [[06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]]

### NTP (Network Time Protocol)

- **Funktion:** Zeitsynchronisation im Netzwerk
- **Port:** UDP 123
- **Hierarchie:** Stratum-Ebenen (0 = Atomuhr, 1 = primärer Server)
- **Standard:** [[A-RFC-Index|RFC 5905]]

### SSH (Secure Shell)

- **Funktion:** Verschlüsselter Remote-Zugang
- **Port:** TCP 22
- **Ersetzt:** Telnet (unsicher)
- **Features:** Shell-Zugang, SFTP, Port-Forwarding

### FTP (File Transfer Protocol)

- **Funktion:** Dateitransfer
- **Ports:** TCP 21 (Control), TCP 20 (Data im Active Mode)
- **Modi:** Active vs. Passive Mode
- **Modern:** SFTP (über SSH) oder FTPS (über TLS) bevorzugt

> [!tip] Prüfungsrelevanz
> Die Anwendungsschicht ist prüfungsrelevant, besonders:
> - DNS-Auflösung und Record-Typen
> - HTTP-Methoden und Statuscodes
> - E-Mail-Protokoll-Unterschiede
> - Wichtige Portnummern

## Weiterführende Themen

- [[01-OSI-Modell]] - Einordnung im Schichtenmodell
- [[02-TCP-IP-Modell]] - Application Layer
- [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]] - Darunterliegende Schicht
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - TLS/SSL, Verschlüsselung
