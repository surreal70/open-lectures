---
title: "Ports und Services – Netzwerkkommunikation"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - ports
  - sockets
  - tcp
  - udp
source: proTirone (CC-BY-4.0)
---

# Ports und Services – Netzwerkkommunikation

> [!info] Lernziele
> - Port-Konzept verstehen
> - TCP vs. UDP unterscheiden
> - Wichtige Well-Known Ports kennen
> - Netzwerkverbindungen analysieren

## Grundprinzip

### Apps kommunizieren, nicht Rechner

Es reden **nicht Rechner mit Rechner**, sondern **(Client-)App mit (Server-)App**!

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT-RECHNER                           │
│  ┌─────────┐                                                    │
│  │ Browser │ ◄──────────────────┐                               │
│  └────┬────┘                    │                               │
│       │ (Port 54321)            │                               │
│       ▼                         │                               │
│  ┌─────────────┐           ┌────┴────┐                          │
│  │   Socket    │◄─────────▶│Betriebs-│                          │
│  └──────┬──────┘           │ system  │                          │
│         ▼                  └─────────┘                          │
│  ┌─────────────┐                                                │
│  │Netzwerkkarte│                                                │
│  └──────┬──────┘                                                │
└─────────┼───────────────────────────────────────────────────────┘
          │
          │ Internet
          │
┌─────────┼───────────────────────────────────────────────────────┐
│  ┌──────┴──────┐                                                │
│  │Netzwerkkarte│                                                │
│  └──────┬──────┘                          SERVER-RECHNER        │
│         ▼                                                       │
│  ┌─────────────┐           ┌─────────┐                          │
│  │   Socket    │◄─────────▶│Betriebs-│                          │
│  └──────┬──────┘           │ system  │                          │
│         │ (Port 80)        └────┬────┘                          │
│         ▼                       │                               │
│  ┌─────────────┐                │                               │
│  │ Webserver   │ ◄──────────────┘                               │
│  └─────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

### Socket-Kommunikation

**Server-Seite:**
1. Server-App registriert sich beim OS für einen Port
2. OS gibt einen an den Port gebundenen Socket zurück
3. Server lauscht auf dem Socket
4. Bei eingehenden Nachrichten: OS schreibt auf Socket
5. Server liest vom Socket und verarbeitet

**Client-Seite:**
1. Client-App fordert temporären Port (Interimsport) an
2. Client schreibt Nachricht auf Socket
3. OS versendet mit Source-IP und Source-Port

## Port-Systematik

### Portbereiche

| Bereich | Nummern | Bezeichnung | Verwendung |
|---------|---------|-------------|------------|
| **System** | 0 – 1023 | Well-Known Ports | Registriert bei IANA |
| **Registriert** | 1024 – 49151 | Registered Ports | Konventionen/Registrierungen |
| **Dynamisch** | 49152 – 65535 | Dynamic Ports | Für Clients und temporäre Dienste |

### Wichtige Well-Known Ports

| Port | Dienst | Protokoll | Beschreibung |
|------|--------|-----------|--------------|
| **20** | FTP-Data | TCP | Dateiübertragung (Datenkanal) |
| **21** | FTP | TCP/UDP | Dateiübertragung (Steuerung) |
| **22** | SSH | TCP/UDP | Secure Shell |
| **23** | Telnet | TCP | Unverschlüsselte Shell (⚠️) |
| **25** | SMTP | TCP | E-Mail-Versand |
| **53** | DNS | TCP/UDP | Namensauflösung |
| **67/68** | DHCP | UDP | IP-Adressvergabe |
| **80** | HTTP | TCP | Webserver |
| **110** | POP3 | TCP | E-Mail-Abruf |
| **123** | NTP | UDP | Zeitsynchronisation |
| **143** | IMAP | TCP | E-Mail-Abruf (mit Sync) |
| **443** | HTTPS | TCP | Verschlüsselter Webserver |
| **993** | IMAPS | TCP | IMAP mit TLS |

### Registrierte Ports (Auswahl)

| Port | Dienst | Beschreibung |
|------|--------|--------------|
| **1433** | MSSQL | Microsoft SQL Server |
| **1883** | MQTT | IoT-Messaging |
| **3306** | MySQL | MySQL-Datenbank |
| **5432** | PostgreSQL | PostgreSQL-Datenbank |
| **8080** | HTTP-Alt | Alternative/Proxy |

## TCP vs. UDP

### UDP – User Datagram Protocol

**Verbindungslos** und **nicht-zuverlässig**:

- Keine Garantie für Ankunft
- Keine Garantie für Reihenfolge
- Keine Garantie gegen Duplikate
- **Fire-and-Forget**-Prinzip

```
┌────────────────────────────────────────┐
│           UDP-Paket                    │
├──────────────┬─────────────────────────┤
│ Source Port  │ Destination Port        │
├──────────────┼─────────────────────────┤
│ Length       │ Checksum                │
├──────────────┴─────────────────────────┤
│              Payload                   │
└────────────────────────────────────────┘
```

**Anwendungen:** DNS, DHCP, Streaming, VoIP, Gaming

### TCP – Transmission Control Protocol

**Verbindungsorientiert** und **zuverlässig**:

- Garantiert Ankunft (oder meldet Fehler)
- Garantiert Reihenfolge
- Garantiert keine Duplikate
- Ende-zu-Ende-Verbindung im Duplex-Mode

**Verbindung definiert durch:**
```
[<Lokaler Rechner:Port>, <Entfernter Rechner:Port>]
```

### TCP 3-Wege-Handshake

```
CLIENT                                    SERVER
   │                                         │
   │──────────── SYN (seq=x) ───────────────▶│
   │                                         │
   │◀────────── SYN/ACK (seq=y, ack=x+1) ────│
   │                                         │
   │──────────── ACK (ack=y+1) ─────────────▶│
   │                                         │
   │         VERBINDUNG HERGESTELLT          │
   │                                         │
```

### TCP-Verbindungszustände

| Zustand | Beschreibung |
|---------|--------------|
| **LISTEN** | Server wartet auf Verbindungen |
| **SYN-SENT** | Client wartet auf Bestätigung |
| **SYN-RECEIVED** | Server wartet auf Client-ACK |
| **ESTABLISHED** | Verbindung aktiv |
| **FIN-WAIT-1/2** | Verbindungsabbau eingeleitet |
| **TIME-WAIT** | Warten auf ablaufende Pakete |
| **CLOSED** | Keine Verbindung |

## Netzwerkanalyse

### Offene Ports anzeigen

```bash
# Linux: Alle TCP-Verbindungen
netstat -ano | grep tcp

# Linux: Lauschende Dienste (als root)
sudo lsof -i -n | grep LISTEN

# Linux: Mit ss (modern)
ss -tuln

# Windows PowerShell
netstat -ano | Select-String TCP
Get-NetTCPConnection
```

### Beispielausgabe

```
Proto  Local Address      Foreign Address    State
TCP    0.0.0.0:22         0.0.0.0:*          LISTEN
TCP    0.0.0.0:80         0.0.0.0:*          LISTEN
TCP    192.168.1.100:443  93.184.216.34:443  ESTABLISHED
```

---

> [!tip] Übungen
> 1. Listen Sie alle lauschenden TCP-Ports auf Ihrem System auf
> 2. Identifizieren Sie, welche Prozesse auf Port 80/443 lauschen
> 3. Programmieren Sie einen einfachen Echo-Server in Python mit dem `socket`-Modul

## Weiterführende Links

- [Wikipedia: TCP](https://de.wikipedia.org/wiki/Transmission_Control_Protocol)
- [Wikipedia: UDP](https://de.wikipedia.org/wiki/User_Datagram_Protocol)
- [Liste der Portnummern](https://de.wikipedia.org/wiki/Liste_der_standardisierten_Ports)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
