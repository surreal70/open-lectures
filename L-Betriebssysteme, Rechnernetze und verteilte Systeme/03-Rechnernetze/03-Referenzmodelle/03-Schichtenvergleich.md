---
author: Andreas Hümmer
title: Schichtenvergleich – OSI vs. TCP/IP
tags:
  - vorlesung
  - rn
  - referenzmodell
  - osi
  - tcp-ip
  - vergleich
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Schichtenvergleich – OSI vs. TCP/IP

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Entsprechungen zwischen OSI- und TCP/IP-Modell aufzeigen
> - Die Vor- und Nachteile beider Modelle gegenüberstellen
> - Protokolle in beiden Modellen korrekt einordnen
> - Erklären, warum beide Modelle in der Praxis verwendet werden
> - Die Dateneinheiten (PDUs) den Schichten zuordnen

## Gegenüberstellung der Modelle

```
┌─────────────────────────────────────────────────────────────────┐
│               OSI-MODELL vs. TCP/IP-MODELL                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   OSI                              TCP/IP                       │
│   ───                              ──────                       │
│                                                                 │
│   ┌─────────────────────┐                                      │
│   │ 7  Anwendung        │                                      │
│   ├─────────────────────┤          ┌─────────────────────┐     │
│   │ 6  Darstellung      │  ◄────►  │ 4  Anwendung        │     │
│   ├─────────────────────┤          │    (Application)    │     │
│   │ 5  Sitzung          │          └─────────────────────┘     │
│   └─────────────────────┘                                      │
│                                                                 │
│   ┌─────────────────────┐          ┌─────────────────────┐     │
│   │ 4  Transport        │  ◄────►  │ 3  Transport        │     │
│   └─────────────────────┘          └─────────────────────┘     │
│                                                                 │
│   ┌─────────────────────┐          ┌─────────────────────┐     │
│   │ 3  Vermittlung      │  ◄────►  │ 2  Internet         │     │
│   └─────────────────────┘          └─────────────────────┘     │
│                                                                 │
│   ┌─────────────────────┐                                      │
│   │ 2  Sicherung        │          ┌─────────────────────┐     │
│   ├─────────────────────┤  ◄────►  │ 1  Netzzugang       │     │
│   │ 1  Bitübertragung   │          │    (Network Access) │     │
│   └─────────────────────┘          └─────────────────────┘     │
│                                                                 │
│   7 Schichten                      4 Schichten                  │
│   Theoretisches Modell             Praktisches Modell           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Detaillierter Vergleich

### Schicht-für-Schicht-Zuordnung

| OSI | OSI-Name | TCP/IP | TCP/IP-Name | Protokollbeispiele | PDU |
|-----|----------|--------|-------------|-------------------|-----|
| 7 | Anwendung | 4 | Anwendung | HTTP, DNS, SMTP, SSH | Daten |
| 6 | Darstellung | 4 | Anwendung | TLS*, JPEG, ASCII | Daten |
| 5 | Sitzung | 4 | Anwendung | RPC, NetBIOS | Daten |
| 4 | Transport | 3 | Transport | TCP, UDP, QUIC | Segment/Datagramm |
| 3 | Vermittlung | 2 | Internet | IP, ICMP, IGMP | Paket |
| 2 | Sicherung | 1 | Netzzugang | Ethernet, WLAN, PPP | Frame |
| 1 | Bitübertragung | 1 | Netzzugang | Kabel, Funk, Glasfaser | Bit |

*TLS wird manchmal auch der Transportschicht zugeordnet

### Geräte und ihre Schichtzuordnung

```
┌─────────────────────────────────────────────────────────────────┐
│                GERÄTE IM SCHICHTENMODELL                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   OSI    TCP/IP    Gerät              Funktion                  │
│   ───    ──────    ─────              ────────                  │
│                                                                 │
│    7       4       Application        Protokollkonvertierung    │
│                    Gateway/Proxy      Inhaltsfilterung          │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    4       3       Load Balancer      Lastverteilung            │
│                    (Layer 4)          nach Port/Verbindung      │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    3       2       Router             Paketweiterleitung        │
│                    Layer-3-Switch     nach IP-Adresse           │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    2       1       Switch             Frame-Weiterleitung       │
│                    Bridge             nach MAC-Adresse          │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    1       1       Hub                Signalverstärkung         │
│                    Repeater           Broadcast an alle Ports   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Vor- und Nachteile

### OSI-Modell

| Vorteile | Nachteile |
|----------|-----------|
| Klare Trennung der Funktionen | Zu komplex für einfache Anwendungen |
| Gutes Lehrmodell | Schichten 5+6 oft überflüssig |
| Internationale Standardisierung (ISO) | Kam zu spät (TCP/IP war etabliert) |
| Herstellerunabhängig | Theoretisch, wenig Implementierungen |
| Detaillierte Schichtdefinition | "Design by Committee" |

### TCP/IP-Modell

| Vorteile | Nachteile |
|----------|-----------|
| Praxiserprobt | Weniger klare Schichttrennung |
| Einfacher (4 Schichten) | Netzzugang nicht detailliert |
| De-facto-Standard des Internets | "Erst Code, dann Modell" |
| Offene RFCs | Sicherheit nachträglich hinzugefügt |
| Flexibel | Weniger geeignet als Lehrmodell |

### Wann welches Modell verwenden?

> [!tip] Praktische Empfehlung
> 
> **OSI-Modell verwenden für:**
> - Lernen und Lehren von Netzwerkkonzepten
> - Detaillierte Fehleranalyse ("Auf welcher Schicht liegt das Problem?")
> - Herstellerunabhängige Kommunikation
> - Zertifizierungsprüfungen
> 
> **TCP/IP-Modell verwenden für:**
> - Praktische Netzwerkimplementierung
> - Internet-Protokoll-Entwicklung
> - Dokumentation realer Systeme
> - Alltägliche Netzwerkarbeit

## Dateneinheiten (Protocol Data Units)

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROTOCOL DATA UNITS (PDUs)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   OSI    TCP/IP    PDU-Name            Auch genannt             │
│   ───    ──────    ────────            ───────────              │
│                                                                 │
│   7-5      4       Daten               Message, Request,        │
│                    (Data)              Response, Payload        │
│                                                                 │
│    4       3       Segment (TCP)       Datagramm (UDP)          │
│                    (Segment)           TPDU                     │
│                                                                 │
│    3       2       Paket               Datagramm (IP),          │
│                    (Packet)            NPDU                     │
│                                                                 │
│    2       1       Rahmen              LPDU, Frame              │
│                    (Frame)                                      │
│                                                                 │
│    1       1       Bit / Symbol        Signal                   │
│                    (Bit)                                        │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   Merkhilfe: "Daten Segmentieren, Pakete Framen, Bits senden"  │
│                                                                 │
│   Alternative: "Do Some People Fear Birthdays?"                 │
│                (Data, Segment, Packet, Frame, Bit)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Protokollzuordnung – Vollständige Übersicht

```
┌─────────────────────────────────────────────────────────────────┐
│              PROTOKOLLE IM SCHICHTENMODELL                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   OSI  TCP/IP  Kategorie        Protokolle                      │
│   ───  ──────  ─────────        ──────────                      │
│                                                                 │
│    7     4     Web              HTTP, HTTPS, WebSocket          │
│                E-Mail           SMTP, POP3, IMAP                │
│                Datei            FTP, SFTP, TFTP, NFS, SMB       │
│                Namen            DNS                             │
│                Fernzugriff      SSH, Telnet, RDP, VNC           │
│                Verzeichnis      LDAP, Active Directory          │
│                Zeit             NTP, SNTP                       │
│                Management       SNMP, Syslog                    │
│                Netzwerk         DHCP, BOOTP                     │
│                                                                 │
│    6     4     Codierung        TLS/SSL, MIME, XDR              │
│                Kompression      (in Anwendungen)                │
│                                                                 │
│    5     4     Sitzung          RPC, NetBIOS, PPTP              │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    4     3     Zuverlässig      TCP, SCTP                       │
│                Unzuverlässig    UDP, DCCP                       │
│                Modern           QUIC                            │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    3     2     Adressierung     IPv4, IPv6                      │
│                Hilfsprotokolle  ICMP, ICMPv6                    │
│                Multicast        IGMP                            │
│                Sicherheit       IPsec (AH, ESP)                 │
│                Tunneling        GRE                             │
│                Routing          OSPF, BGP, RIP, EIGRP, IS-IS    │
│                Adressauflösung  ARP, NDP (eigentlich L2)        │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│    2     1     LAN kabelgeb.    Ethernet (802.3)                │
│                LAN drahtlos     WLAN (802.11)                   │
│                PAN              Bluetooth (802.15.1)            │
│                WAN              PPP, HDLC, Frame Relay          │
│                Tunneling        PPPoE, L2TP                     │
│                Bridging         STP, RSTP, VLANs (802.1Q)       │
│                                                                 │
│    1     1     Kupfer           10/100/1000BASE-T               │
│                Glasfaser        1000BASE-SX/LX, 10GBASE-SR      │
│                Drahtlos         802.11 PHY, Bluetooth PHY       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Hybridmodell für die Praxis

In der Praxis wird oft ein **5-Schichten-Hybridmodell** verwendet:

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYBRIDMODELL (5 SCHICHTEN)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Nr.  Name              OSI      TCP/IP    Beispiele           │
│   ───  ────              ───      ──────    ─────────           │
│                                                                 │
│    5   Anwendung         5-7        4       HTTP, DNS, SMTP     │
│                                                                 │
│    4   Transport          4         3       TCP, UDP            │
│                                                                 │
│    3   Netzwerk           3         2       IP, ICMP            │
│                                                                 │
│    2   Sicherung          2         1       Ethernet, WLAN      │
│                                                                 │
│    1   Physikalisch       1         1       Kabel, Signale      │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   Dieses Modell kombiniert:                                     │
│   • Die Klarheit der unteren OSI-Schichten (1+2 getrennt)      │
│   • Die Einfachheit der TCP/IP-Anwendungsschicht (5-7 → 5)     │
│                                                                 │
│   Verwendung: Lehrbücher, Cisco-Kurse, praktische Netzwerke    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Fehlersuche mit dem Schichtenmodell

Das Schichtenmodell hilft bei der systematischen Fehlersuche:

```
┌─────────────────────────────────────────────────────────────────┐
│              TROUBLESHOOTING MIT DEM SCHICHTENMODELL            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Von unten nach oben prüfen (Bottom-Up):                       │
│                                                                 │
│   1. Physikalisch:  Kabel eingesteckt? Link-LED leuchtet?      │
│                     → ping localhost (127.0.0.1)                │
│                                                                 │
│   2. Sicherung:     MAC-Adresse gelernt? VLAN korrekt?         │
│                     → arp -a, show mac address-table            │
│                                                                 │
│   3. Netzwerk:      IP-Adresse korrekt? Gateway erreichbar?    │
│                     → ping Gateway, traceroute                  │
│                                                                 │
│   4. Transport:     Port offen? Firewall blockiert?            │
│                     → telnet host port, netstat -an             │
│                                                                 │
│   5. Anwendung:     Dienst läuft? Konfiguration korrekt?       │
│                     → curl, nslookup, Anwendungslogs           │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   Typische Fehler pro Schicht:                                  │
│                                                                 │
│   L1: Kabelbruch, falscher Stecker, Wackelkontakt              │
│   L2: Falsches VLAN, STP-Blocking, Duplex-Mismatch             │
│   L3: Falsche IP/Subnetz, fehlendes Routing, ACL               │
│   L4: Firewall, Port nicht offen, Timeout                      │
│   L5+: Falsche Konfiguration, Zertifikate, Authentifizierung   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **OSI** hat 7 Schichten, **TCP/IP** hat 4 Schichten
> - OSI-Schichten 5-7 entsprechen der TCP/IP-Anwendungsschicht
> - OSI-Schichten 1-2 entsprechen der TCP/IP-Netzzugangsschicht
> - **OSI** ist ein Lehrmodell, **TCP/IP** ein Praxismodell
> - In der Praxis wird oft ein **5-Schichten-Hybridmodell** verwendet
> - Das Schichtenmodell hilft bei der systematischen **Fehlersuche**

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Können Sie die **Entsprechungen** zwischen OSI und TCP/IP aufzeigen?
> - Kennen Sie die **Vor- und Nachteile** beider Modelle?
> - Können Sie **Protokolle** in beiden Modellen korrekt einordnen?
> - Wissen Sie, welche **Geräte** auf welcher Schicht arbeiten?
> - Kennen Sie die **PDU-Namen** (Daten, Segment, Paket, Frame, Bit)?

## Verwandte Themen

- [[01-OSI-Modell]] – Das 7-Schichten-Referenzmodell
- [[02-TCP-IP-Modell]] – Das 4-Schichten-Praxismodell
- [[04-Physikalische-Schicht/00-Physikalische-Schicht-Index|Physikalische Schicht]] – Layer 1 im Detail
- [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Layer 2 im Detail
- [[06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] – Layer 3 im Detail
- [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]] – Layer 4 im Detail
- [[08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] – Layer 5-7 im Detail

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- ISO/IEC 7498-1:1994 – OSI Basic Reference Model
- Tanenbaum, A. S.: Computer Networks, 5th Edition
- Comer, D. E.: Internetworking with TCP/IP
