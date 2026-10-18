---
author: Andreas Hümmer
title: OSI-Referenzmodell
tags:
  - vorlesung
  - rn
  - referenzmodell
  - osi
  - schichtenmodell
  - iso
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# OSI-Referenzmodell

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die sieben Schichten des OSI-Modells benennen und ihre Aufgaben erklären
> - Die Bedeutung von Schichtenmodellen für die Netzwerkkommunikation beschreiben
> - Protokolle und Geräte den entsprechenden Schichten zuordnen
> - Die Datenkapselung beim Durchlaufen der Schichten erklären
> - Die Eselsbrücken für die Schichtenreihenfolge anwenden

## Einführung

### Was ist ein Protokoll?

> [!definition] Protokoll
> Ein **Protokoll** definiert das Format und die Reihenfolge, in der Nachrichten von Systemen in Netzwerken gesendet und empfangen werden, sowie die Aktionen, die durch die Nachrichten ausgelöst werden.

Diese Definition ist universell und gilt für **jede Ebene** der Netzwerkkommunikation. Betrachtet man den Weg einer Nachricht von einer Anwendung zur anderen, durchläuft sie mehrere Protokolle – einen **Protokoll-Stack**.

### Warum Schichtenmodelle?

Schichtenmodelle bieten mehrere Vorteile:

- **Abstraktion**: Komplexe Systeme werden in handhabbare Teile zerlegt
- **Unabhängigkeit**: Änderungen in einer Schicht betreffen andere nicht
- **Standardisierung**: Klare Schnittstellen zwischen den Schichten
- **Wiederverwendbarkeit**: Protokolle können kombiniert werden
- **Interoperabilität**: Geräte verschiedener Hersteller können kommunizieren

## Das OSI-Modell im Überblick

Das **Open Systems Interconnection (OSI)** Modell wurde 1984 von der [[07-Anhang/IT-Related-Organisations/ISO|ISO]] als Referenzmodell veröffentlicht (ISO/IEC 7498).

![[osi-referenzmodell.png]]
*<span class="fig-id">03-03-01-osi-referenzmodell</span>: Die sieben Schichten des OSI-Referenzmodells mit deutschen und englischen Bezeichnungen sowie den jeweiligen Dateneinheiten.*

### Eselsbrücken

> [!tip] Merkhilfen für die Schichtenreihenfolge
> 
> **Von unten nach oben (1→7):**
> - **P**lease **D**o **N**ot **T**hrow **S**alami **P**izza **A**way
> - **P**hysical **D**ata **N**etwork **T**ransport **S**ession **P**resentation **A**pplication
> 
> **Von oben nach unten (7→1):**
> - **A**lle **P**riester **S**aufen **T**equila **N**ach **D**er **P**redigt
> - **A**lle **d**eutschen **S**tudenten **t**rinken **v**erschiedene **S**orten **B**ier

## Die sieben Schichten im Detail

### Schicht 1 – Bitübertragung (Physical Layer)

→ Vertiefung: [[04-Physikalische-Schicht/00-Physikalische-Schicht-Index|Physikalische Schicht]]

**Aufgabe:** Übertragung einzelner Bits über das physikalische Medium.

**Aufgaben:**
- Umwandlung von Bits in physikalische Signale
- Leitungscodierung (z.B. Manchester, 4B5B, 8B10B)
- Signalverstärkung und Taktrückgewinnung
- Definition von Steckern, Kabeln, Spannungspegeln

**Protokolle/Standards:**
- Ethernet Physical Layer (10BASE-T, 1000BASE-T, etc.)
- Token Ring Physical
- RS-232, V.24

**Geräte:**
- Hub, Repeater
- Kabel, Stecker
- MAU (Media Access Unit)
- Transceiver, Netzwerkkarte (physisch)

**Dateneinheit:** Bits / Symbole

### Schicht 2 – Sicherung (Data Link Layer)

→ Vertiefung: [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]]

**Aufgabe:** Zuverlässige Übertragung von Datenrahmen zwischen direkt verbundenen Knoten.

**Zwei Unterschichten:**

| Unterschicht | Standard | Aufgaben |
|--------------|----------|----------|
| **LLC** (Logical Link Control) | IEEE 802.2 | Flusskontrolle, Multiplexing höherer Protokolle |
| **MAC** (Media Access Control) | IEEE 802.3/11/etc. | Medienzugriffskontrolle (CSMA/CD, CSMA/CA), MAC-Adressierung, Frame-Aufbau und Prüfsummen |

**Aufgaben:**
- Rahmenbildung (Framing)
- MAC-Adressierung (48-Bit Hardware-Adressen)
- Fehlererkennung (CRC/FCS)
- Medienzugriffskontrolle

**Protokolle/Standards:**
- IEEE 802.3 (Ethernet)
- IEEE 802.11 (WLAN)
- IEEE 802.5 (Token Ring)
- PPP, HDLC

**Geräte:**
- Switch, Bridge
- Netzwerkkarte (MAC-Ebene)

**Dateneinheit:** Rahmen (Frames)

### Schicht 3 – Vermittlung (Network Layer)

→ Vertiefung: [[06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]]

**Aufgabe:** Wegewahl (Routing) und logische Adressierung über Netzwerkgrenzen hinweg.

**Aufgaben:**
- Logische Adressierung (IP-Adressen)
- Routing zwischen Netzwerken
- Fragmentierung und Reassemblierung
- Paketweiterleitung (Forwarding)

**Protokolle:**
- IP (IPv4, IPv6)
- ICMP (Fehlermeldungen, Ping)
- IGMP (Multicast)
- IPsec (Verschlüsselung auf L3)
- Routing-Protokolle: OSPF, BGP, RIP

**Geräte:**
- Router
- Layer-3-Switch

**Dateneinheit:** Pakete (Packets)

### Schicht 4 – Transport (Transport Layer)

→ Vertiefung: [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]]

**Aufgabe:** Ende-zu-Ende-Kommunikation zwischen Anwendungen.

**Aufgaben:**
- Segmentierung und Reassemblierung
- Ende-zu-Ende-Verbindung
- Flusskontrolle
- Fehlerkorrektur (bei TCP)
- Multiplexing über Ports

**Protokolle:**
- TCP (verbindungsorientiert, zuverlässig)
- UDP (verbindungslos, best-effort)
- SCTP (Stream Control)
- QUIC (UDP-basiert, multiplexed)

**Geräte:**
- (Endgeräte – Software-basiert)
- Load Balancer (Layer 4)

**Dateneinheit:** Segmente (TCP) / Datagramme (UDP)

### Schicht 5 – Sitzung (Session Layer)

**Aufgabe:** Verwaltung von Dialogsteuerung und Synchronisation.

**Aufgaben:**
- Auf- und Abbau von Sitzungen
- Dialogsteuerung (Simplex, Half-Duplex, Full-Duplex)
- Synchronisation (Checkpoints)
- Token-Verwaltung

**Protokolle/Technologien:**
- RPC (Remote Procedure Call)
- NetBIOS
- PPTP (teilweise)
- SIP (Session Initiation Protocol – teilweise)

**In der Praxis:**
- Oft in Anwendungsprotokollen integriert
- Im TCP/IP-Modell Teil der Anwendungsschicht

**Dateneinheit:** Daten

### Schicht 6 – Darstellung (Presentation Layer)

**Aufgabe:** Datenformatierung, Verschlüsselung und Komprimierung.

**Aufgaben:**
- Datenformatkonvertierung
- Zeichensatzumwandlung (ASCII ↔ EBCDIC, UTF-8)
- Datenkomprimierung
- Verschlüsselung/Entschlüsselung
- Serialisierung

**Protokolle/Formate:**
- SSL/TLS (Verschlüsselung – teilweise)
- JPEG, GIF, PNG (Bildformate)
- MPEG, H.264 (Videoformate)
- ASCII, Unicode
- ASN.1, XDR

**In der Praxis:**
- Oft in Anwendungsprotokollen integriert
- TLS wird heute meist der Transportschicht zugerechnet

**Dateneinheit:** Daten

### Schicht 7 – Anwendung (Application Layer)

→ Vertiefung: [[08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]]

**Aufgabe:** Schnittstelle zwischen Netzwerk und Anwendungsprozessen.

**Aufgaben:**
- Bereitstellung von Netzwerkdiensten für Anwendungen
- Identifikation von Kommunikationspartnern
- Ressourcenverfügbarkeit prüfen
- Synchronisation der Kommunikation

**Protokolle:**
- HTTP/HTTPS (Web)
- SMTP, POP3, IMAP (E-Mail)
- DNS (Namensauflösung)
- FTP, SFTP (Dateitransfer)
- SSH (Secure Shell)
- SNMP (Netzwerkmanagement)
- DHCP (Adressvergabe)

**Geräte:**
- Application Gateway, Proxy
- Layer-7-Load-Balancer

**Dateneinheit:** Daten / Nachrichten

## Datenkapselung (Encapsulation)

Beim Durchlaufen der Schichten werden die Daten **gekapselt** – jede Schicht fügt ihren eigenen Header (und ggf. Trailer) hinzu:

![[osi-kapselung-isdn.png]]
*<span class="fig-id">03-03-01-osi-kapselung-isdn</span>: Datenkapselung im OSI-Modell am Beispiel von ISDN – jede der 7 Schichten fügt ihren eigenen Header hinzu.*

## Netzwerkgeräte und ihre Schichten

| Gerät | Arbeitet auf Schicht | Funktion |
|-------|---------------------|----------|
| Hub | 1 | Signalverstärkung, Broadcast |
| Repeater | 1 | Signalverstärkung |
| Bridge | 2 | Trennt Kollisionsdomänen |
| Switch | 2 (L2) | Frame-Weiterleitung nach MAC |
| Switch L3 | 3 | Routing + Switching |
| Router | 3 | Paket-Weiterleitung nach IP |
| Gateway | 7 | Protokollkonvertierung |
| Proxy | 7 | Stellvertreter für Anwendungen |
| Firewall | 3-7 | Paketfilterung (je nach Typ) |

### Kollisions- und Broadcast-Domänen

| Gerätetyp | Kollisionsdomäne | Broadcast-Domäne |
|-----------|------------------|------------------|
| Hub | 1 (geteilt) | 1 (geteilt) |
| Repeater | 1 (geteilt) | 1 (geteilt) |
| Bridge | Pro Port getrennt | 1 (geteilt) |
| Switch | Pro Port getrennt | Pro VLAN getrennt |
| Router | Pro Port getrennt | Pro Port getrennt |

## Kritik am OSI-Modell

> [!warning] Einschränkungen des OSI-Modells
> - **Theoretisch**: Wurde als Referenz entwickelt, nicht als Implementierung
> - **Komplexität**: 7 Schichten sind für viele Anwendungen zu granular
> - **Schichten 5-6**: In der Praxis selten eigenständig implementiert
> - **Timing**: Kam zu spät – TCP/IP war bereits etabliert
> - **"OSI = Open Systems Interconnection = Open Sores Infection"** (Kritiker-Witz)

Dennoch ist das OSI-Modell als **Referenzmodell für das Verständnis** von Netzwerkkommunikation unverzichtbar.

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Das OSI-Modell hat **7 Schichten** (1=Physical bis 7=Application)
> - Schichten 1-4 sind **transportorientiert**, 5-7 sind **anwendungsorientiert**
> - Jede Schicht hat spezifische **Aufgaben** und **Dateneinheiten**
> - **Datenkapselung**: Jede Schicht fügt Header hinzu
> - **Geräte** arbeiten auf unterschiedlichen Schichten (Hub=L1, Switch=L2, Router=L3)
> - In der Praxis wird oft das **TCP/IP-Modell** verwendet

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Alle 7 OSI-Schichten in der richtigen Reihenfolge (1=Physical bis 7=Application)
> - Protokolle den Schichten zuordnen (HTTP=L7, TCP=L4, IP=L3, Ethernet=L2)
> - Datenkapselung verstehen (Frame enthält Paket enthält Segment)
> - Geräte und ihre Arbeitsschichten (Hub=L1, Switch=L2, Router=L3)
> - Dateneinheiten jeder Schicht (Bit, Frame, Paket, Segment, Daten)

> [!question] **Typische Prüfungsfragen**
> - Nennen Sie alle 7 OSI-Schichten von unten nach oben
> - Auf welcher Schicht arbeitet ein Switch/Router?
> - Welche Dateneinheit verwendet die Transportschicht?
> - Ordnen Sie folgende Protokolle den OSI-Schichten zu: HTTP, TCP, IP, Ethernet

## Verwandte Themen

- [[02-TCP-IP-Modell]] – Das praktisch verwendete 4-Schichten-Modell
- [[03-Schichtenvergleich]] – OSI vs. TCP/IP
- [[04-Physikalische-Schicht/00-Physikalische-Schicht-Index|Physikalische Schicht]] – Layer 1 im Detail
- [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Layer 2 im Detail

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- ISO/IEC 7498-1:1994 – OSI Basic Reference Model
- Tanenbaum, A. S.: Computer Networks, 5th Edition
