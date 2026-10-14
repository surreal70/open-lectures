---
author: Andreas Hümmer
title: Historie der Rechnernetze
tags:
  - vorlesung
  - rn
  - grundlagen
  - historie
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Historie der Rechnernetze

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Evolution der Kommunikationstechnologien von frühen Methoden bis zu modernen Netzwerken nachvollziehen
> - Netzwerke nach ihrer räumlichen Dimension klassifizieren (PAN bis GAN)
> - Die verschiedenen Kommunikationsarten (Unicast, Broadcast, Multicast) unterscheiden
> - Die Meilensteine der Netzwerkentwicklung (ALOHA, ARPANET, Ethernet) einordnen

## Einführung: Was ist ein Netzwerk?

Kommunikationsnetzwerke sind heute allgegenwärtig. Sie kommen in vielen Ausprägungen vor und erfüllen verschiedenste Zwecke, was die Beschreibung und Durchdringung nicht leicht macht.

Um diese Komplexität aufzulösen, betrachten wir Rechnernetze aus verschiedenen Sichtweisen:

- **Physische Ausprägung** – Kabel, Leitungen, Medien
- **Physische Datenübertragung** – Codierung der Signale
- **Topologieformen** – Wie sind die Knoten verbunden?
- **Logische Kommunikation** – Aufteilung nach Layern
- **Protokolle** – Regeln für den Datenaustausch

## Dimension von Netzwerken

Netzwerke lassen sich nach ihrer räumlichen Ausdehnung klassifizieren:

| Kürzel | Bezeichnung | Dimension | Typische Komponenten |
|--------|-------------|-----------|---------------------|
| **CN/NOC** | ChipNet / Network on a Chip | µm | Chipintegriert, I²C, SPI |
| **SN/CN** | SystemNet / ClusterNet | Wenige Meter | High-Performance (z.B. InfiniBand) |
| **PAN** | Personal Area Network | Persönlicher Wirkbereich | Bluetooth, WiFi |
| **LAN** | Local Area Network | Haus/Campus | Switch, Router, VPN |
| **MAN** | Metropolitan Area Network | Urbaner Bereich | Switch, Router |
| **WAN** | Wide Area Network | Region/Land | Switch, Router |
| **GAN/Internet** | Global Area Network | Die Erde | Switch, Router, Satelliten |
| **SAN** | Solar Area Network | Das Sonnensystem | Richtlaser, Richtfunk |

> [!merke] Merke
> Die Netzwerkdimension bestimmt maßgeblich die verwendeten Technologien, Protokolle und Herausforderungen (Latenz, Bandbreite, Fehlerrate).

## Geschichte der Kommunikation

### Frühe Kommunikationsformen

Lange bevor es elektronische Netzwerke gab, entwickelten Menschen verschiedene Methoden zur Fernkommunikation:

| Methode | Reichweite | Kommunikationsmatrix | Komplexität |
|---------|------------|---------------------|-------------|
| **Sprache** | Einige Meter | 1:1, 1:n, n:n | Komplex |
| **Gesten** | Wenige Meter | 1:1, 1:n | Einfach |
| **Trommeln/Blasinstrumente** | Weiter | 1:n | Sehr einfach |
| **Rauchzeichen** | Kilometerweit | 1:n | Ganz einfach |

### Bedingungen für erfolgreiche Kommunikation

Aus diesen frühen Formen lassen sich grundlegende Anforderungen ableiten:

1. **Gemeinsames Alphabet** – Sender und Empfänger müssen die Zeichen verstehen
2. **Reichweite** – Das Signal muss ankommen
3. **Anzahl der Kommunikationspartner** – Wer kommuniziert mit wem?
4. **Bandbreite** – Wie viel Information pro Zeiteinheit?
5. **Informationstiefe** – Wie komplex ist der Inhalt?

## Kommunikationsarten

Anhand der Beteiligten und ihrer Beziehung unterscheiden wir:

| Art | Beschreibung | Strukturelement | Terminus |
|-----|--------------|-----------------|----------|
| **1:n** | One to all | Topologie | **Broadcast** |
| **1:m** | One to many | Topologie | **Netcast** |
| **1:1** | One to one | Adresse | **Unicast** |
| **1:l** | One to many (Abonnement) | Abonnement | **Multicast** |

> [!beispiel] Beispiele
> - **Unicast**: E-Mail an eine Person, Telefongespräch
> - **Broadcast**: ARP-Request im LAN, Radio
> - **Multicast**: Video-Streaming an Abonnenten, IPTV

## Moderne Kommunikationstechnologien

### Vor-elektronische Ära

| Technologie | Ab ca. | Bandbreite | Reichweite | Signalalphabet |
|-------------|--------|------------|------------|----------------|
| Optische Telegraphie | Ende 18. Jhd | 2-4 Signale/s | mehrere km | Codewörter |
| Kabelgebundene Telegraphie | Mitte 19. Jhd | 2-3 Signale/s | mehrere km | Morse |
| Funk-Telegraphie | Anfang 20. Jhd | 1-2 Signale/s | mehrere km | Morse |
| Telefonie | Mitte 19. Jhd | bis 8 kHz | mehrere km | Sprache |

### Serielle Kommunikation

Die ersten direkten Verbindungen zwischen Computern nutzten serielle Schnittstellen:

| Standard | Ab ca. | Bandbreite | Reichweite | Typ |
|----------|--------|------------|------------|-----|
| Terminal-to-Host | 1950er | Einige Baud | wenige m | Spannungsschnittstelle |
| **RS-232** (V.24) | 1964 | längenabhängig | längenabhängig | Spannungsschnittstelle |
| **RS-485** (V.11) | 1960er | max 10 Mbps | 1200 m | Stromschnittstelle |

> [!info] RS-232 vs RS-485
> - **RS-232**: Einfache Punkt-zu-Punkt-Verbindung, spannungsbasiert
> - **RS-485**: Differenzielle Signalübertragung, störungsresistenter, längere Reichweiten

## Die ersten Rechnernetze

### ALOHA (1970)

Das ALOHA-Netz der University of Hawaii war eines der ersten drahtlosen Computernetzwerke:

- **Funk-basiert** mit 9600 bit/s
- Einführung des **ALOHA-Protokolls** für den Medienzugriff
- Grundlage für spätere Ethernet-Entwicklung (CSMA/CD)

### ARPANET (1969)

Das ARPANET gilt als Vorläufer des heutigen Internets:

- Finanziert durch die **DARPA** (US-Verteidigungsministerium)
- Erstes **paketvermitteltes Weitverkehrsnetz**
- Verwendete zunächst **NCP**, später **TCP/IP** (ab 1983)
- Dezentrale Struktur – überlebt Ausfälle einzelner Knoten

```
   UCLA ─────── SRI
     │           │
     │           │
   UCSB ─────── Utah

   Die ersten vier ARPANET-Knoten (1969)
```

### Ethernet (1977)

Entwickelt bei **XEROX PARC** als „Distributed Packet Switching":

- Ursprünglich **2,94 Mbit/s** (später 10, 100, 1000 Mbit/s, heute bis 400 Gbit/s)
- Nutzung von **CSMA/CD** für den Medienzugriff
- Wurde zum dominierenden LAN-Standard

## Zeitleiste der Netzwerkentwicklung

```
1960        1970        1980        1990        2000        2010        2020
  │           │           │           │           │           │           │
  ├── RS-232 (1964)
  │           ├── ARPANET (1969)
  │           ├── ALOHA (1970)
  │           │           ├── Ethernet (1977)
  │           │           ├── TCP/IP Standard (1983)
  │           │           │           ├── WWW (1991)
  │           │           │           ├── 100 Mbit Ethernet (1995)
  │           │           │           │           ├── Gigabit Ethernet (1998)
  │           │           │           │           ├── WiFi 802.11 (1999)
  │           │           │           │           │           ├── 10 GbE (2002)
  │           │           │           │           │           ├── WiFi 6 (2019)
  │           │           │           │           │           ├── 400 GbE (2017)
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Netzwerke reichen von Chip-internen Verbindungen (NOC) bis zu interplanetaren Netzen (SAN)
> - Grundlegende Kommunikationsanforderungen sind zeitlos: gemeinsames Alphabet, Reichweite, Bandbreite
> - Die Kommunikationsarten Unicast, Broadcast und Multicast bilden die Basis aller Netzwerkprotokolle
> - ARPANET (1969) und Ethernet (1977) sind die wichtigsten Meilensteine der Netzwerkgeschichte

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Netzwerkdimensionen (PAN, LAN, MAN, WAN, GAN) und ihre typischen Einsatzbereiche
> - Unterscheiden Sie Unicast, Broadcast und Multicast mit Beispielen
> - Wissen Sie, warum ARPANET als Vorläufer des Internets gilt
> - Verstehen Sie den Zusammenhang zwischen ALOHA und Ethernet (CSMA/CD)

## Verwandte Themen

- [[02-Netzwerktypen]] – Klassifikation nach Funktion und Einsatz
- [[03-Topologien]] – Physische und logische Netzwerkstrukturen
- [[00-Referenzmodelle-Index|Referenzmodelle]] – OSI und TCP/IP Modell

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
