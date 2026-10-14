---
author: Andreas Hümmer
title: TCP/IP-Modell (DoD-Modell)
tags:
  - vorlesung
  - rn
  - referenzmodell
  - tcp-ip
  - dod
  - internet
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# TCP/IP-Modell (DoD-Modell)

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die vier Schichten des TCP/IP-Modells benennen und ihre Aufgaben erklären
> - Die historische Entwicklung des Modells aus dem ARPANET beschreiben
> - Protokolle den entsprechenden Schichten zuordnen
> - Die praktischen Vorteile gegenüber dem OSI-Modell erläutern
> - Die Kommunikationsarten (Unicast, Broadcast, Multicast) unterscheiden

## Einführung

### Historischer Hintergrund

Das TCP/IP-Modell entstand in den 1970er Jahren im Rahmen des **ARPANET**-Projekts des US-Verteidigungsministeriums (Department of Defense – **DoD**). Daher wird es auch als **DoD-Modell** bezeichnet.

> [!info] Warum "TCP/IP"?
> Der Name stammt von den beiden wichtigsten Protokollen:
> - **TCP** (Transmission Control Protocol) – Transportschicht
> - **IP** (Internet Protocol) – Internetschicht
> 
> Zusammen bilden sie den Kern der Internet-Protokollfamilie.

### Pragmatischer Ansatz

Im Gegensatz zum theoretischen OSI-Modell wurde TCP/IP **praxisorientiert** entwickelt:

- Erst die Protokolle, dann das Modell (bottom-up)
- Fokus auf funktionierende Implementierungen
- "Rough consensus and running code" (IETF-Philosophie)

## Das TCP/IP-Modell im Überblick

```
┌─────────────────────────────────────────────────────────────────┐
│                    DAS TCP/IP-MODELL (DoD)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Nr.   Schicht              Auch genannt        Dateneinheit   │
│   ───   ───────              ───────────         ──────────     │
│                                                                 │
│    4    Anwendung            Application         Daten          │
│         (Application)        Process Layer       Nachrichten    │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│    3    Transport            Host-to-Host        Segmente (TCP) │
│         (Transport)          Transport           Datagramme(UDP)│
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│    2    Internet             Internetwork        Pakete         │
│         (Internet)           Network Layer       Datagramme     │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│    1    Netzzugang           Network Access      Frames         │
│         (Network Access)     Link Layer          Bits           │
│                              Host-to-Network                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Die vier Schichten im Detail

### Schicht 1 – Netzzugang (Network Access Layer)

**Entspricht:** OSI-Schichten 1 + 2

**Aufgabe:** Physikalische Übertragung und Zugang zum lokalen Netzwerk.

```
┌─────────────────────────────────────────────────────────────────┐
│                SCHICHT 1 – NETZZUGANG                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Aufgaben:                                                     │
│   • Physikalische Adressierung (MAC-Adressen)                  │
│   • Rahmenbildung (Framing)                                    │
│   • Medienzugriffskontrolle                                    │
│   • Fehlererkennung auf Frame-Ebene                            │
│   • Signalübertragung                                          │
│                                                                 │
│   Protokolle/Standards:                                         │
│   • Ethernet (IEEE 802.3)                                      │
│   • WLAN (IEEE 802.11)                                         │
│   • PPP (Point-to-Point Protocol)                              │
│   • PPPoE (PPP over Ethernet)                                  │
│   • L2TP (Layer 2 Tunneling Protocol)                          │
│   • Token Ring (historisch)                                    │
│                                                                 │
│   Besonderheit im TCP/IP-Modell:                               │
│   • Nicht detailliert spezifiziert                             │
│   • "Beliebige" Netzwerktechnologie verwendbar                 │
│   • Fokus liegt auf den höheren Schichten                      │
│                                                                 │
│   Verbindungstyp: Punkt-zu-Punkt                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Schicht 2 – Internet (Internet Layer)

**Entspricht:** OSI-Schicht 3

**Aufgabe:** Logische Adressierung und Routing über Netzwerkgrenzen hinweg.

```
┌─────────────────────────────────────────────────────────────────┐
│                SCHICHT 2 – INTERNET                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Aufgaben:                                                     │
│   • Logische Adressierung (IP-Adressen)                        │
│   • Routing zwischen Netzwerken                                │
│   • Fragmentierung und Reassemblierung                         │
│   • Verbindungsloses Paket-Switching                           │
│                                                                 │
│   Kernprotokolle:                                               │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  IP (Internet Protocol)                                 │  │
│   │  • IPv4 (RFC 791) – 32-Bit-Adressen                    │  │
│   │  • IPv6 (RFC 8200) – 128-Bit-Adressen                  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│   Hilfssprotokolle:                                             │
│   • ICMP – Fehlermeldungen, Diagnose (Ping, Traceroute)       │
│   • IGMP – Multicast-Gruppenverwaltung                         │
│   • ARP – Adressauflösung IP → MAC (streng genommen L2)       │
│   • IPsec – Verschlüsselung auf IP-Ebene                      │
│                                                                 │
│   Routing-Protokolle (auf dieser Ebene):                       │
│   • OSPF, BGP, RIP, EIGRP                                      │
│                                                                 │
│   Geräte: Router                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Schicht 3 – Transport (Transport Layer)

**Entspricht:** OSI-Schicht 4

**Aufgabe:** Ende-zu-Ende-Kommunikation zwischen Prozessen.

```
┌─────────────────────────────────────────────────────────────────┐
│                SCHICHT 3 – TRANSPORT                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Aufgaben:                                                     │
│   • Ende-zu-Ende-Verbindung zwischen Anwendungen               │
│   • Multiplexing über Ports (0-65535)                          │
│   • Segmentierung und Reassemblierung                          │
│   • Flusskontrolle und Staukontrolle (bei TCP)                │
│                                                                 │
│   Die zwei Hauptprotokolle:                                     │
│                                                                 │
│   ┌──────────────────────┬──────────────────────┐              │
│   │         TCP          │         UDP          │              │
│   ├──────────────────────┼──────────────────────┤              │
│   │ Verbindungsorientiert│ Verbindungslos       │              │
│   │ Zuverlässig          │ Best-Effort          │              │
│   │ Reihenfolgegarantie  │ Keine Garantien      │              │
│   │ Flusskontrolle       │ Kein Overhead        │              │
│   │ 3-Way-Handshake      │ Fire-and-Forget      │              │
│   │ Segmente             │ Datagramme           │              │
│   ├──────────────────────┼──────────────────────┤              │
│   │ HTTP, HTTPS, FTP,    │ DNS, DHCP, NTP,      │              │
│   │ SMTP, SSH, Telnet    │ VoIP, Streaming,     │              │
│   │                      │ Gaming, SNMP         │              │
│   └──────────────────────┴──────────────────────┘              │
│                                                                 │
│   Weitere Protokolle:                                           │
│   • SCTP (Stream Control Transmission Protocol)                │
│   • QUIC (Quick UDP Internet Connections)                      │
│   • DCCP (Datagram Congestion Control Protocol)                │
│                                                                 │
│   Verbindungstyp: Ende-zu-Ende                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Schicht 4 – Anwendung (Application Layer)

**Entspricht:** OSI-Schichten 5 + 6 + 7

**Aufgabe:** Netzwerkdienste für Anwendungsprogramme.

```
┌─────────────────────────────────────────────────────────────────┐
│                SCHICHT 4 – ANWENDUNG                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Aufgaben (vereint OSI-Schichten 5-7):                        │
│   • Sitzungsverwaltung                                         │
│   • Datenformatierung und -konvertierung                       │
│   • Verschlüsselung (TLS)                                      │
│   • Netzwerkdienste für Anwendungen                            │
│                                                                 │
│   Protokolle nach Anwendungsbereich:                            │
│                                                                 │
│   Web:          HTTP, HTTPS, WebSocket                         │
│   E-Mail:       SMTP, POP3, IMAP                               │
│   Dateitransfer: FTP, SFTP, TFTP, SCP                          │
│   Namensauflösung: DNS                                         │
│   Fernzugriff:  SSH, Telnet, RDP                               │
│   Netzwerkdienste: DHCP, NTP, SNMP, LDAP                       │
│   Sicherheit:   TLS/SSL, Kerberos                              │
│   Medien:       RTP, RTSP, SIP                                 │
│                                                                 │
│   Geräte:                                                       │
│   • Application Gateway                                        │
│   • Proxy Server                                               │
│   • Layer-7-Load-Balancer                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Kommunikationsarten

Das TCP/IP-Modell unterstützt verschiedene Kommunikationsformen:

```
┌─────────────────────────────────────────────────────────────────┐
│                   KOMMUNIKATIONSARTEN                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Art          Beziehung   Beschreibung        Maßgeblich       │
│   ───          ─────────   ───────────         ──────────       │
│                                                                 │
│   Unicast      1:1         One-to-One          Adresse          │
│                            An genau einen                       │
│                            Empfänger                            │
│                                                                 │
│   Broadcast    1:n         One-to-All          Topologie        │
│                            An alle im                           │
│                            Netzwerk                             │
│                                                                 │
│   Multicast    1:m         One-to-Many         Abonnement       │
│                            An eine Gruppe                       │
│                            (Subscription)                       │
│                                                                 │
│   Anycast      1:1*        One-to-Nearest      Routing          │
│                            An den nächsten                      │
│                            aus einer Gruppe                     │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│      ┌───┐                  ┌───┐   ┌───┐   ┌───┐              │
│      │ S │──────────────────│ E │   │   │   │   │   Unicast    │
│      └───┘                  └───┘   └───┘   └───┘              │
│                                                                 │
│      ┌───┐                  ┌───┐   ┌───┐   ┌───┐              │
│      │ S │──────────────────│ E │───│ E │───│ E │   Broadcast  │
│      └───┘                  └───┘   └───┘   └───┘              │
│                                                                 │
│      ┌───┐                  ┌───┐   ┌───┐   ┌───┐              │
│      │ S │──────────────────│ E │───│   │───│ E │   Multicast  │
│      └───┘                  └───┘   └───┘   └───┘              │
│                              (Mitglieder der Gruppe)           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Datenkapselung im TCP/IP-Modell

```
┌─────────────────────────────────────────────────────────────────┐
│              DATENKAPSELUNG IM TCP/IP-MODELL                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Anwendung        │     HTTP-Request (Daten)      │           │
│                    └──────────────┬────────────────┘           │
│                                   ▼                             │
│   Transport        │ TCP │    HTTP-Request          │          │
│                    │ Hdr │      (Daten)             │          │
│                    └─────┴───────────┬──────────────┘          │
│                                      ▼                          │
│   Internet         │ IP  │ TCP │  HTTP-Request      │          │
│                    │ Hdr │ Hdr │    (Daten)         │          │
│                    └─────┴─────┴─────────┬──────────┘          │
│                                          ▼                      │
│   Netzzugang   │Eth│ IP  │ TCP │ HTTP-Request │FCS│            │
│                │Hdr│ Hdr │ Hdr │   (Daten)    │   │            │
│                └───┴─────┴─────┴──────────────┴───┘            │
│                                   ▼                             │
│   Physikalisch     01101001010110110100...                     │
│                                                                 │
│   ─────────────────────────────────────────────────────────    │
│                                                                 │
│   Typische Header-Größen:                                      │
│   • Ethernet: 14 Bytes (+ 4 Bytes FCS)                        │
│   • IPv4: 20-60 Bytes                                          │
│   • TCP: 20-60 Bytes                                           │
│   • UDP: 8 Bytes                                               │
│                                                                 │
│   Maximale Ethernet-Frame-Größe: 1518 Bytes                    │
│   → MTU (Maximum Transmission Unit): 1500 Bytes Nutzdaten      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Protokoll-Stack in der Praxis

### Beispiel: Web-Request

```
┌─────────────────────────────────────────────────────────────────┐
│           PROTOKOLL-STACK: HTTPS-ANFRAGE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Browser                                                       │
│      │                                                          │
│      ▼                                                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Anwendung: HTTP/2 + TLS 1.3                            │  │
│   │  GET /index.html HTTP/2                                 │  │
│   └─────────────────────────────────────────────────────────┘  │
│      │                                                          │
│      ▼                                                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Transport: TCP                                         │  │
│   │  Src Port: 52431, Dst Port: 443                        │  │
│   │  Seq: 1000, Ack: 1, Flags: PSH,ACK                     │  │
│   └─────────────────────────────────────────────────────────┘  │
│      │                                                          │
│      ▼                                                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Internet: IPv4                                         │  │
│   │  Src: 192.168.1.100, Dst: 93.184.216.34                │  │
│   │  TTL: 64, Protocol: TCP (6)                            │  │
│   └─────────────────────────────────────────────────────────┘  │
│      │                                                          │
│      ▼                                                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  Netzzugang: Ethernet                                   │  │
│   │  Src MAC: aa:bb:cc:dd:ee:ff                            │  │
│   │  Dst MAC: 11:22:33:44:55:66 (Gateway)                  │  │
│   │  EtherType: 0x0800 (IPv4)                              │  │
│   └─────────────────────────────────────────────────────────┘  │
│      │                                                          │
│      ▼                                                          │
│   ═══════════════════════════════════════════════════════════  │
│                        Netzwerk                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Vorteile des TCP/IP-Modells

| Vorteil | Erläuterung |
|---------|-------------|
| **Praxisnähe** | Basiert auf funktionierenden Implementierungen |
| **Einfachheit** | 4 statt 7 Schichten |
| **Flexibilität** | Netzzugangsschicht ist technologie-unabhängig |
| **Verbreitung** | De-facto-Standard des Internets |
| **Offene Standards** | RFCs sind frei verfügbar |
| **Bewährt** | Über 40 Jahre Praxiseinsatz |

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Das TCP/IP-Modell hat **4 Schichten** (Netzzugang, Internet, Transport, Anwendung)
> - Es ist das **praktisch verwendete** Modell des Internets
> - Die **Netzzugangsschicht** ist bewusst unspezifiziert (Technologie-Unabhängigkeit)
> - **IP** sorgt für Routing, **TCP/UDP** für Ende-zu-Ende-Kommunikation
> - **Kommunikationsarten**: Unicast, Broadcast, Multicast, Anycast
> - Protokoll-Stack: Anwendung → Transport → Internet → Netzzugang

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die **4 Schichten** und ihre Aufgaben
> - Können Sie **Protokolle** zuordnen (HTTP=Anwendung, TCP=Transport, IP=Internet)
> - Verstehen Sie den **Unterschied TCP vs. UDP**
> - Kennen Sie die **Kommunikationsarten** (Unicast, Broadcast, Multicast)
> - Wissen Sie, warum TCP/IP "DoD-Modell" heißt

## Verwandte Themen

- [[01-OSI-Modell]] – Das 7-Schichten-Referenzmodell
- [[03-Schichtenvergleich]] – OSI vs. TCP/IP
- [[06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] – IP im Detail
- [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]] – TCP und UDP im Detail

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- [[07-Anhang/RFCs/RFC 791 IPv4|RFC 791]] – Internet Protocol
- [[07-Anhang/RFCs/RFC 8200 IPv6|RFC 8200]] – Internet Protocol Version 6
- Comer, D. E.: Internetworking with TCP/IP
