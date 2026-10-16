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
> - Die grundlegenden Anforderungen an erfolgreiche Kommunikation benennen
> - Die Meilensteine der Netzwerkentwicklung (ALOHA, ARPANET, Ethernet) einordnen
> - Den Zusammenhang zwischen ALOHA-Protokoll und Ethernet erklären

## Geschichte der Kommunikation

### Die Natur der Kommunikation

Bevor wir uns mit technischen Netzwerken beschäftigen, lohnt ein Blick auf die fundamentale Natur der Kommunikation. Die Herausforderungen, die unsere Vorfahren bei der Fernkommunikation lösen mussten, sind dieselben, die wir heute bei Netzwerkprotokollen adressieren.

> [!merke] Fundamentale Fragen der Kommunikation
> Jede Form der Kommunikation – ob Rauchzeichen oder Glasfaser – muss dieselben grundlegenden Fragen beantworten:
> - **Was** wird übertragen? (Alphabet, Codierung)
> - **Wie weit** kann das Signal reichen? (Reichweite)
> - **Wie schnell** kommen Informationen an? (Bandbreite)
> - **Wer** kommuniziert mit **wem**? (Topologie)
> - **Wie komplex** kann die Nachricht sein? (Informationstiefe)

### Frühe Kommunikationsformen

Lange bevor es elektronische Netzwerke gab, entwickelten Menschen verschiedene Methoden zur Fernkommunikation. Jede dieser Methoden illustriert einen anderen Aspekt der Kommunikationsparameter:

#### Sprache
- **Reichweite:** Einige Meter (begrenzt durch Lautstärke)
- **Kommunikationsmatrix:** 1:1, 1:n, n:n (Gespräch, Vortrag, Diskussion)
- **Informationstiefe:** Sehr hoch – komplexe Ideen, Emotionen, Nuancen
- **Voraussetzung:** Gemeinsame Sprache (Protokoll!)

> [!beispiel] Parallele zur Netzwerktechnik
> Sprache ist wie eine **Punkt-zu-Punkt-Verbindung mit hoher Bandbreite aber geringer Reichweite**. Die "gemeinsame Sprache" entspricht dem **Protokoll** – ohne Einigung auf die Bedeutung der Zeichen keine Kommunikation.

#### Gesten und Handzeichen
- **Reichweite:** Sichtweite (Meter bis wenige hundert Meter)
- **Kommunikationsmatrix:** 1:1, 1:n
- **Informationstiefe:** Begrenzt – einfache Nachrichten
- **Voraussetzung:** Vereinbarung über Bedeutung der Gesten

> [!beispiel] Parallele zur Netzwerktechnik
> Vergleichbar mit **Signalisierungsprotokollen**: Die Gesten der Fluglotsen auf dem Rollfeld sind ein standardisiertes "Protokoll" mit definiertem "Alphabet" von Handzeichen.

#### Trommeln und Blasinstrumente
- **Reichweite:** Mehrere Kilometer (Schall trägt weiter als Stimme)
- **Kommunikationsmatrix:** 1:n (Broadcast)
- **Informationstiefe:** Sehr begrenzt – wenige vordefinierte Nachrichten
- **Voraussetzung:** Vereinbartes "Alphabet" von Rhythmen/Melodien

> [!beispiel] Parallele zur Netzwerktechnik
> Dies entspricht einem **Broadcast-Medium mit niedriger Bandbreite**: Alle in Reichweite empfangen die Nachricht, aber nur wenige Bit Information pro "Übertragung". Afrikanische Nachrichtentrommeln konnten Nachrichten über Hunderte Kilometer weiterleiten – ein frühes **Store-and-Forward-Netzwerk**!

#### Rauchzeichen
- **Reichweite:** Viele Kilometer (bei guter Sicht)
- **Kommunikationsmatrix:** 1:n (Broadcast)
- **Informationstiefe:** Minimal – oft nur "Achtung!" oder "Hier bin ich"
- **Voraussetzung:** Sichtverbindung, gutes Wetter

> [!beispiel] Parallele zur Netzwerktechnik
> **Line-of-Sight-Kommunikation** wie bei Richtfunk oder Laser. Die chinesische Mauer nutzte Signalfeuer als **Relay-Netzwerk**: Eine Nachricht konnte in Stunden Tausende Kilometer zurücklegen, indem jeder Wachturm das Signal weiterleitete.

#### Optische Telegraphie (Semaphore)
- **Reichweite:** 10-30 km zwischen Stationen
- **Kommunikationsmatrix:** Punkt-zu-Punkt mit Relais
- **Informationstiefe:** Mittel – Buchstaben und Wörter möglich
- **Voraussetzung:** Sichtverbindung, Stationsnetzwerk

![[optische-telegrafie-chappe.png]]
*<span class="fig-id">03-01-01-optische-telegrafie-chappe</span>: Schematische Darstellung einer Chappe-Telegrafenlinie mit drei Stationen.*

![[chappe-telegraf-rees-cyclopaedia.png]]
*<span class="fig-id">03-01-01-chappe-telegraf-rees-cyclopaedia</span>: Historische Darstellung des Chappe-Telegrafen aus Rees's Cyclopaedia (frühes 19. Jh.). Quelle: Wikimedia Commons, Public Domain.*

> [!beispiel] Parallele zur Netzwerktechnik
> Der optische Telegraf war das erste echte **Weitverkehrsnetz mit Routing**: Nachrichten wurden von Station zu Station weitergeleitet. Das System hatte bereits **Adressierung** (Zielstation), **Fehlerkorrektur** (Wiederholung bei Missverständnis) und **Priorisierung** (militärische Nachrichten zuerst).

### Bestimmende Aspekte der Kommunikation

Aus diesen frühen Formen lassen sich die fundamentalen Parameter ableiten, die jedes Kommunikationssystem – auch moderne Netzwerke – charakterisieren:

| Parameter | Beschreibung | Frühe Beispiele | Moderne Entsprechung |
|-----------|--------------|-----------------|----------------------|
| **Gemeinsames Alphabet** | Sender und Empfänger müssen die Zeichen verstehen | Sprache, Morse, Gesten | Protokolle (TCP/IP, HTTP) |
| **Reichweite** | Maximale Distanz für Signalübertragung | Stimme < Trommel < Rauchzeichen | LAN < WAN < Satellit |
| **Bandbreite** | Informationsmenge pro Zeiteinheit | Sprache: hoch, Rauchzeichen: minimal | bps, Mbps, Gbps |
| **Kommunikationspartner** | Wer kann mit wem kommunizieren? | 1:1, 1:n, n:n | Unicast, Broadcast, Multicast |
| **Informationstiefe** | Komplexität der übertragbaren Inhalte | Emotionen (Sprache) vs. "Alarm" (Feuer) | Text, Audio, Video, VR |
| **Zuverlässigkeit** | Kommt die Nachricht korrekt an? | Wiederholung, Bestätigung | ARQ, Checksummen, FEC |
| **Latenz** | Zeit bis die Nachricht ankommt | Sofort (Sprache) vs. Stunden (Bote) | ms (LAN) bis Minuten (Mars) |

> [!zusammenfassung] Die zeitlosen Herausforderungen
> Die fünf fundamentalen Herausforderungen der Kommunikation sind seit Jahrtausenden dieselben:
> 1. **Verständigung**: Gemeinsames Alphabet / Protokoll
> 2. **Distanz**: Signalverstärkung / Relais
> 3. **Geschwindigkeit**: Bandbreite / Kompression
> 4. **Adressierung**: Wer soll die Nachricht erhalten?
> 5. **Zuverlässigkeit**: Fehlererkennung / -korrektur

## Einführung: Was ist ein Netzwerk?

Kommunikationsnetzwerke sind heute allgegenwärtig. Sie kommen in vielen Ausprägungen vor und erfüllen verschiedenste Zwecke, was die Beschreibung und Durchdringung nicht leicht macht.

Um diese Komplexität aufzulösen, betrachten wir Rechnernetze aus verschiedenen Sichtweisen:

- **Physische Ausprägung** – Kabel, Leitungen, Medien
- **Physische Datenübertragung** – Codierung der Signale
- **Topologieformen** – Wie sind die Knoten verbunden?
- **Logische Kommunikation** – Aufteilung nach Layern
- **Protokolle** – Regeln für den Datenaustausch

## Dimension von Netzwerken

Netzwerke lassen sich nach ihrer räumlichen Ausdehnung klassifizieren – von chip-internen Verbindungen bis zu interplanetaren Netzen.

> [!info] Detaillierte Informationen
> Eine ausführliche Behandlung der Netzwerktypen mit Technologien, Bandbreiten und Anwendungsbeispielen finden Sie in [[03-Netzwerktypen]].

Die wichtigsten Kategorien im Überblick:
- **PAN** (Personal Area Network) – Bluetooth, wenige Meter
- **LAN** (Local Area Network) – Ethernet/WiFi, Gebäude/Campus
- **MAN** (Metropolitan Area Network) – Stadtweite Vernetzung
- **WAN** (Wide Area Network) – Länder/Kontinente
- **GAN** (Global Area Network) – Das Internet

## Kommunikationsarten

Die Art der Kommunikation in Netzwerken hängt von der Anzahl der Empfänger ab:

- **Unicast** (1:1) – Direkte Kommunikation zwischen zwei Partnern
- **Broadcast** (1:alle) – Nachricht an alle im Netzwerk
- **Multicast** (1:Gruppe) – Nachricht an eine Abonnentengruppe
- **Anycast** (1:nächster) – Nachricht an den nächsten aus einer Gruppe

> [!info] Detaillierte Informationen
> Eine ausführliche Behandlung der Kommunikationsarten mit Beispielen und Anwendungsfällen finden Sie in [[03-Netzwerktypen#Kommunikationsarten in Netzwerken]].

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

![[arpanet-erste-knoten.png]]
*<span class="fig-id">03-01-01-arpanet-erste-knoten</span>: Die ersten vier ARPANET-Knoten im Dezember 1969.*

| Abkürzung | Vollständiger Name | Standort |
|-----------|-------------------|----------|
| **UCLA** | University of California, Los Angeles | Los Angeles, Kalifornien |
| **SRI** | Stanford Research Institute | Menlo Park, Kalifornien |
| **UCSB** | University of California, Santa Barbara | Santa Barbara, Kalifornien |
| **Utah** | University of Utah | Salt Lake City, Utah |

![[A_sketch_of_the_ARPANET_in_December_1969.png]]
*<span class="fig-id">03-01-01-arpanet-sketch-1969</span>: Originale Handskizze der ARPANET-Topologie vom Dezember 1969. Quelle: Wikimedia Commons, Public Domain.*

### Ethernet (1977)

Entwickelt bei **XEROX PARC** als „Distributed Packet Switching":

- Ursprünglich **2,94 Mbit/s** (später 10, 100, 1000 Mbit/s, heute bis 400 Gbit/s)
- Nutzung von **CSMA/CD** für den Medienzugriff
- Wurde zum dominierenden LAN-Standard

## Zeitleiste der Netzwerkentwicklung

![[netzwerk-zeitleiste.png]]
*<span class="fig-id">03-01-01-netzwerk-zeitleiste</span>: Meilensteine der Netzwerkentwicklung von 1960 bis heute.*

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Grundlegende Kommunikationsanforderungen sind zeitlos: gemeinsames Alphabet, Reichweite, Bandbreite
> - Frühe Kommunikationsformen (Sprache, Trommeln, Rauchzeichen, Semaphore) illustrieren moderne Netzwerkkonzepte
> - Von der optischen Telegraphie zur seriellen Kommunikation (RS-232/RS-485) zur Netzwerktechnologie
> - ALOHA (1970) führte das Konzept des Medienzugriffs ein (Basis für CSMA/CD)
> - ARPANET (1969) war das erste paketvermittelte WAN und Vorläufer des Internets
> - Ethernet (1977) wurde zum dominierenden LAN-Standard

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Nennen Sie die fundamentalen Aspekte jeder Kommunikation (Alphabet, Reichweite, Bandbreite, Partner, Zuverlässigkeit)
> - Erklären Sie, warum ARPANET als Vorläufer des Internets gilt
> - Verstehen Sie den Zusammenhang zwischen ALOHA und Ethernet (CSMA/CD)
> - Kennen Sie die wichtigsten Meilensteine der Netzwerkentwicklung
> - Unterscheiden Sie RS-232 und RS-485

## Verwandte Themen

- [[02-Standards-und-Gremien]] – Standardisierungsgremien und IEEE 802
- [[03-Netzwerktypen]] – Klassifikation nach Funktion und Einsatz
- [[04-Topologien]] – Physische und logische Netzwerkstrukturen
- [[00-Referenzmodelle-Index|Referenzmodelle]] – OSI und TCP/IP Modell

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
