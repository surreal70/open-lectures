---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - osi
  - tcpip
  - architektur
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# Netzwerkarchitekturen: OSI und TCP/IP

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das OSI-Referenzmodell mit allen 7 Schichten erklären können
> - Das TCP/IP-Modell verstehen und mit OSI vergleichen können
> - Protokolle den richtigen Schichten zuordnen können
> - Die Datenkapselung (Encapsulation) verstehen

---

## Überblick

Referenzmodelle beschreiben, wie Netzwerkkommunikation in logische Schichten aufgeteilt wird. Die zwei wichtigsten Modelle sind das **OSI-Modell** (theoretisch) und das **TCP/IP-Modell** (praktisch).

## OSI-Referenzmodell

Das **Open Systems Interconnection Model** (ISO/IEC 7498) teilt Netzwerkkommunikation in 7 Schichten:

### Die 7 Schichten

| Layer | Name (EN) | Name (DE) | Aufgabe | Beispiele |
|-------|-----------|-----------|---------|-----------|
| **7** | Application | Anwendung | Anwendungsschnittstelle | HTTP, FTP, SMTP, DNS |
| **6** | Presentation | Darstellung | Datenformat, Verschlüsselung | JPEG, ASCII, SSL/TLS |
| **5** | Session | Sitzung | Verbindungsverwaltung | NetBIOS, RPC |
| **4** | Transport | Transport | Ende-zu-Ende-Verbindung | TCP, UDP |
| **3** | Network | Vermittlung | Routing, Adressierung | IP, ICMP, Router |
| **2** | Data Link | Sicherung | Rahmenbildung, MAC | Ethernet, Switch |
| **1** | Physical | Bitübertragung | Signale, Kabel | Kabel, Hub, Repeater |

> [!tip] **Merkhilfe (von oben nach unten)**
> **A**lle **P**riester **S**aufen **T**equila **N**ach **D**er **P**redigt
> 
> **Merkhilfe (von unten nach oben)**
> **P**lease **D**o **N**ot **T**hrow **S**alami **P**izza **A**way

### Schichten im Detail

#### Layer 1: Physical (Bitübertragung)
- Übertragung von Bits als elektrische/optische Signale
- Kabeltypen, Stecker, Spannungen, Frequenzen
- **Geräte**: Hub, Repeater, Kabel

#### Layer 2: Data Link (Sicherung)
- Rahmenbildung (Frames)
- MAC-Adressierung
- Fehlererkennung (CRC)
- **Geräte**: Switch, Bridge

#### Layer 3: Network (Vermittlung)
- Logische Adressierung (IP)
- Routing zwischen Netzen
- Fragmentierung
- **Geräte**: Router, Layer-3-Switch

#### Layer 4: Transport
- Ende-zu-Ende-Kommunikation
- Ports für Anwendungen
- Zuverlässigkeit (TCP) oder Geschwindigkeit (UDP)

#### Layer 5-7: Obere Schichten
- Anwendungsbezogene Funktionen
- In der Praxis oft zusammengefasst

## TCP/IP-Modell

Das praktisch verwendete Modell hat nur 4 Schichten:

| TCP/IP Layer | Name | OSI-Entsprechung |
|--------------|------|------------------|
| **4** | Application | Layer 5-7 |
| **3** | Transport | Layer 4 |
| **2** | Internet | Layer 3 |
| **1** | Network Access / Link | Layer 1-2 |

### Vergleich OSI vs. TCP/IP

```
    OSI                    TCP/IP
┌─────────────┐       ┌─────────────┐
│ Application │       │             │
├─────────────┤       │ Application │
│Presentation │       │             │
├─────────────┤       │             │
│   Session   │       └─────────────┘
├─────────────┤       ┌─────────────┐
│  Transport  │ ───── │  Transport  │
├─────────────┤       └─────────────┘
│   Network   │ ───── ┌─────────────┐
├─────────────┤       │   Internet  │
│  Data Link  │       └─────────────┘
├─────────────┤       ┌─────────────┐
│  Physical   │       │Network Access│
└─────────────┘       └─────────────┘
```

## Datenkapselung (Encapsulation)

Beim Senden werden Daten schichtweise "verpackt":

```
Layer 7-5: Daten
           ↓
Layer 4:   [TCP-Header] + Daten = Segment
           ↓
Layer 3:   [IP-Header] + Segment = Paket
           ↓
Layer 2:   [Frame-Header] + Paket + [Frame-Trailer] = Frame
           ↓
Layer 1:   Bits → Signale
```

| Schicht | Dateneinheit (PDU) |
|---------|-------------------|
| Layer 7-5 | Daten |
| Layer 4 | Segment (TCP) / Datagram (UDP) |
| Layer 3 | Paket |
| Layer 2 | Frame |
| Layer 1 | Bits |

## Protokollzuordnung

### Wichtige Protokolle nach Schicht

| Layer | Protokolle |
|-------|------------|
| **7** | HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, SSH, Telnet |
| **6** | SSL/TLS, JPEG, MPEG, ASCII |
| **5** | NetBIOS, RPC, SIP |
| **4** | TCP, UDP, SCTP |
| **3** | IP (IPv4, IPv6), ICMP, ARP*, OSPF, BGP |
| **2** | Ethernet, Wi-Fi (802.11), PPP |
| **1** | RS-232, DSL, ISDN, Bluetooth PHY |

> [!note] **ARP-Einordnung**
> ARP arbeitet zwischen Layer 2 und 3 und wird unterschiedlich eingeordnet.

## Zusammenhänge

- → [[02-Grundbegriffe|Grundbegriffe]]
- → [[04-Uebertragungsstandards|Übertragungsstandards (Layer 1-2)]]
- → [[08-IPv4-Adressen|IPv4-Adressen (Layer 3)]]

> [!warning] **Prüfungsrelevant**
> - Alle 7 OSI-Schichten mit Namen und Funktion
> - Zuordnung von Geräten zu Schichten
> - Vergleich OSI vs. TCP/IP
> - Datenkapselung und PDU-Bezeichnungen
> - Protokollzuordnung

> [!question] **Typische Prüfungsfragen**
> - Nennen Sie die 7 Schichten des OSI-Modells.
> - Auf welcher Schicht arbeitet ein Router?
> - Wie heißt die Dateneinheit auf Layer 2?
> - Ordnen Sie HTTP, IP und Ethernet den OSI-Schichten zu.
> - Welche Schichten fasst TCP/IP zusammen?

## Quellen

- proTirone: LF03:03 Architekturen (Karsten Reincke, CC-BY-4.0)
- ISO/IEC 7498-1: OSI Basic Reference Model
- RFC 1122: Requirements for Internet Hosts

> [!tip] **Weiterführende Links**
> - [Wikipedia: OSI-Modell](https://de.wikipedia.org/wiki/OSI-Modell)
> - [Wikipedia: TCP/IP](https://de.wikipedia.org/wiki/Internetprotokollfamilie)
