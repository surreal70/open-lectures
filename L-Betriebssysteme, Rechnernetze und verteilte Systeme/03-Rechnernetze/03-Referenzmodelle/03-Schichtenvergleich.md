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

![[osi-tcpip-vergleich.png]]
*<span class="fig-id">03-03-03-osi-tcpip-vergleich</span>: Gegenüberstellung des OSI-Modells (7 Schichten) und des TCP/IP-Modells (4 Schichten) mit ihren Entsprechungen.*

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

| OSI | TCP/IP | Gerät | Funktion |
|-----|--------|-------|----------|
| 7 | 4 | Application Gateway / Proxy | Protokollkonvertierung, Inhaltsfilterung |
| 4 | 3 | Load Balancer (Layer 4) | Lastverteilung nach Port/Verbindung |
| 3 | 2 | Router, Layer-3-Switch | Paketweiterleitung nach IP-Adresse |
| 2 | 1 | Switch, Bridge | Frame-Weiterleitung nach MAC-Adresse |
| 1 | 1 | Hub, Repeater | Signalverstärkung, Broadcast an alle Ports |

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

| OSI | TCP/IP | PDU-Name | Auch genannt |
|-----|--------|----------|--------------|
| 7-5 | 4 | Daten (Data) | Message, Request, Response, Payload |
| 4 | 3 | Segment (TCP) / Datagramm (UDP) | TPDU |
| 3 | 2 | Paket (Packet) | Datagramm (IP), NPDU |
| 2 | 1 | Rahmen (Frame) | LPDU |
| 1 | 1 | Bit / Symbol | Signal |

**Merkhilfen:**
- „Daten Segmentieren, Pakete Framen, Bits senden"
- „**D**o **S**ome **P**eople **F**ear **B**irthdays?" (Data, Segment, Packet, Frame, Bit)

## Protokollzuordnung – Vollständige Übersicht

![[protokoll-schichten.png]]
*<span class="fig-id">03-03-03-protokoll-schichten</span>: Vollständige Übersicht der Protokolle mit Zuordnung zu OSI- und TCP/IP-Schichten, Dateneinheiten, Kopplungselementen und Kommunikationsart.*

## Hybridmodell für die Praxis

In der Praxis wird oft ein **5-Schichten-Hybridmodell** verwendet:

| Nr. | Name | OSI | TCP/IP | Beispiele |
|-----|------|-----|--------|-----------|
| 5 | Anwendung | 5-7 | 4 | HTTP, DNS, SMTP |
| 4 | Transport | 4 | 3 | TCP, UDP |
| 3 | Netzwerk | 3 | 2 | IP, ICMP |
| 2 | Sicherung | 2 | 1 | Ethernet, WLAN |
| 1 | Physikalisch | 1 | 1 | Kabel, Signale |

Dieses Modell kombiniert:
- Die Klarheit der unteren OSI-Schichten (1+2 getrennt)
- Die Einfachheit der TCP/IP-Anwendungsschicht (5-7 → 5)

**Verwendung:** Lehrbücher, Cisco-Kurse, praktische Netzwerke

## Fehlersuche mit dem Schichtenmodell

Das Schichtenmodell hilft bei der systematischen Fehlersuche:

### Von unten nach oben prüfen (Bottom-Up)

| Schicht | Prüfung | Diagnosebefehle |
|---------|---------|-----------------|
| 1. Physikalisch | Kabel eingesteckt? Link-LED leuchtet? | `ping localhost` (127.0.0.1) |
| 2. Sicherung | MAC-Adresse gelernt? VLAN korrekt? | `arp -a`, `show mac address-table` |
| 3. Netzwerk | IP-Adresse korrekt? Gateway erreichbar? | `ping Gateway`, `traceroute` |
| 4. Transport | Port offen? Firewall blockiert? | `telnet host port`, `netstat -an` |
| 5. Anwendung | Dienst läuft? Konfiguration korrekt? | `curl`, `nslookup`, Anwendungslogs |

### Typische Fehler pro Schicht

| Schicht | Typische Fehler |
|---------|-----------------|
| L1 | Kabelbruch, falscher Stecker, Wackelkontakt |
| L2 | Falsches VLAN, STP-Blocking, Duplex-Mismatch |
| L3 | Falsche IP/Subnetz, fehlendes Routing, ACL |
| L4 | Firewall, Port nicht offen, Timeout |
| L5+ | Falsche Konfiguration, Zertifikate, Authentifizierung |

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **OSI** hat 7 Schichten, **TCP/IP** hat 4 Schichten
> - OSI-Schichten 5-7 entsprechen der TCP/IP-Anwendungsschicht
> - OSI-Schichten 1-2 entsprechen der TCP/IP-Netzzugangsschicht
> - **OSI** ist ein Lehrmodell, **TCP/IP** ein Praxismodell
> - In der Praxis wird oft ein **5-Schichten-Hybridmodell** verwendet
> - Das Schichtenmodell hilft bei der systematischen **Fehlersuche**

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Entsprechungen zwischen OSI (7 Schichten) und TCP/IP (4 Schichten)
> - Vor- und Nachteile beider Modelle
> - Protokolle in beiden Modellen korrekt einordnen
> - Geräte und ihre Arbeitsschichten (Hub=L1, Switch=L2, Router=L3)
> - PDU-Namen: Daten, Segment, Paket, Frame, Bit

> [!question] **Typische Prüfungsfragen**
> - Welchen OSI-Schichten entspricht die TCP/IP-Anwendungsschicht?
> - Nennen Sie je 2 Vor- und Nachteile des OSI- und TCP/IP-Modells
> - Auf welcher Schicht arbeitet ein Layer-3-Switch?
> - Was ist eine PDU und wie heißt sie auf Schicht 4?

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
