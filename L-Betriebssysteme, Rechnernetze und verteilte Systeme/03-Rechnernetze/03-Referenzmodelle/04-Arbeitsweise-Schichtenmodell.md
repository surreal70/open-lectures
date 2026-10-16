---
author: Andreas Hümmer
title: Arbeitsweise des Schichtenmodells am Beispiel DoD
tags:
  - content
  - rn
  - tcp-ip
  - dod
  - encapsulation
  - paketfluss
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Arbeitsweise des Schichtenmodells am Beispiel DoD

## Einführung

Dieses Kapitel demonstriert die praktische Arbeitsweise des TCP/IP-Schichtenmodells (DoD-Modell) anhand eines konkreten Beispiels: Eine HTTP-Anfrage von einem Client über einen Router zu einem Webserver.

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Den vollständigen Weg eines Pakets durch alle Schichten beschreiben
> - Die Einkapselung (Encapsulation) und Entkapselung erklären
> - Den Beitrag jeder Schicht zur Kommunikation benennen
> - Die unterschiedliche Verarbeitung in Endgeräten und Routern verstehen

## Übersichtsgrafik: Schichtendurchlauf

Die folgende Grafik zeigt den kompletten Weg der Daten durch die Schichten (OSI-Nummerierung):

![[schichtendurchlauf.png]]
*<span class="fig-id">03-03-04-schichtendurchlauf</span>: Schichtendurchlauf vom Client über den Router zum Server mit logischen (Ende-zu-Ende) und physischen (Hop-by-Hop) Verbindungen.*

### Detailansicht mit Datenfluss

![[datenfluss.png]]
*<span class="fig-id">03-03-04-datenfluss</span>: Datenfluss durch die Schichten mit Ein- und Entkapselung der Header auf jeder Ebene.*

> [!important] Kernkonzept
> - **Endgeräte (Client, Server):** Verarbeiten alle 7 Schichten
> - **Router:** Verarbeiten nur Schichten 1-3 (Netzzugang + Internet)
> - **Switches:** Verarbeiten nur Schichten 1-2 (Netzzugang)

## Szenario

![[szenario.png]]
*<span class="fig-id">03-03-04-szenario</span>: Netzwerkszenario mit Client, Router und Webserver in zwei LANs.*

## Phase 1: Client – Daten senden

### Übersicht der Einkapselung

![[einkapselung.png]]
*<span class="fig-id">03-03-04-einkapselung</span>: Einkapselung (Encapsulation) – schrittweises Hinzufügen von Headern auf dem Client.*

### Schritt 1: Anwendungsschicht (Application Layer)

**Aufgabe:** Erzeugt die Nutzdaten für die Kommunikation

![[schicht-anwendung.png]]
*<span class="fig-id">03-03-04-schicht-anwendung</span>: Anwendungsschicht erzeugt HTTP-Request.*

> [!info] Mehr Details
> Siehe [[08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] für HTTP, DNS, SMTP und weitere Protokolle.

### Schritt 2: Transportschicht (Transport Layer)

**Aufgabe:** Ende-zu-Ende-Verbindung, Segmentierung, Portzuordnung

![[schicht-transport.png]]
*<span class="fig-id">03-03-04-schicht-transport</span>: Transportschicht fügt TCP-Header hinzu.*

> [!info] Mehr Details
> Siehe [[07-Transportschicht/00-Transportschicht-Index|Transportschicht]] für TCP, UDP und Portnummern.

### Schritt 3: Internetschicht (Internet Layer)

**Aufgabe:** Logische Adressierung, Routing, Fragmentierung

![[schicht-internet.png]]
*<span class="fig-id">03-03-04-schicht-internet</span>: Internetschicht fügt IP-Header hinzu und trifft Routing-Entscheidung.*

> [!info] Mehr Details
> Siehe [[06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] für IP, ICMP und Routing.

### Schritt 4: Netzzugangsschicht (Network Access Layer)

**Aufgabe:** Physische Adressierung, Medienzugriff, Bitübertragung

![[schicht-netzzugang.png]]
*<span class="fig-id">03-03-04-schicht-netzzugang</span>: Netzzugangsschicht fügt Ethernet-Header und FCS hinzu, überträgt Bits auf das Medium.*

> [!info] Mehr Details
> Siehe [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] für Ethernet, MAC-Adressen und ARP.

## Phase 2: Router – Weiterleitung

Der Router empfängt den Frame und verarbeitet ihn nur bis Layer 3:

![[router-verarbeitung.png]]
*<span class="fig-id">03-03-04-router-verarbeitung</span>: Router-Verarbeitung – Empfang, Routing-Entscheidung und Versand mit neuen MAC-Adressen.*

### Router: Nur Layer 1-3

![[router-schichten.png]]
*<span class="fig-id">03-03-04-router-schichten</span>: Router verarbeiten nur Layer 1-3 (Netzzugang und Internet), höhere Schichten bleiben unberührt.*

## Phase 3: Server – Daten empfangen

### Übersicht der Entkapselung

![[entkapselung.png]]
*<span class="fig-id">03-03-04-entkapselung</span>: Entkapselung (Decapsulation) – schrittweises Entfernen der Header auf dem Server.*

### Detaillierter Empfangsprozess

![[empfangsprozess.png]]
*<span class="fig-id">03-03-04-empfangsprozess</span>: Detaillierter Empfangsprozess – Verarbeitung auf jeder Schicht des Servers.*

## Gesamtübersicht: Der komplette Paketfluss

![[paketfluss.png]]
*<span class="fig-id">03-03-04-paketfluss</span>: Kompletter Paketfluss vom Client über den Router zum Server mit Ein- und Entkapselung.*

## PDU-Bezeichnungen pro Schicht

![[pdu.png]]
*<span class="fig-id">03-03-04-pdu</span>: PDU-Bezeichnungen (Protocol Data Units) für jede Schicht mit visueller Einkapselungsdarstellung.*

## Zusammenfassung: Beitrag jeder Schicht

| Schicht | Hauptaufgabe | Adressierung | PDU | Geräte |
|---------|--------------|--------------|-----|--------|
| **Anwendung** | Nutzerdienste, Protokolle | URL, Hostname | Daten | - |
| **Transport** | Ende-zu-Ende, Zuverlässigkeit | Portnummern | Segment | - |
| **Internet** | Routing, logische Adress. | IP-Adressen | Paket | Router |
| **Netzzugang** | Physische Übertragung | MAC-Adressen | Frame | Switch, NIC |

## Prüfungsrelevante Konzepte

> [!warning] Klausurrelevanz: Sehr hoch
>
> **Häufige Prüfungsfragen:**
> 1. Beschreiben Sie den Weg eines Pakets durch die Schichten
> 2. Was ist Einkapselung (Encapsulation)?
> 3. Welche Header werden auf welcher Schicht hinzugefügt?
> 4. Was ändert sich beim Durchgang durch einen Router?
> 5. Warum sieht der Router nicht in die TCP-Daten?

### Wichtige Merksätze

> [!tip] Merkhilfen
> 
> **Encapsulation:** "Jede Schicht packt ein Geschenk ein"
> - Anwendung: Das Geschenk (Daten)
> - Transport: Innere Verpackung (Segment)
> - Internet: Karton (Paket)
> - Netzzugang: Versandkarton mit Adresse (Frame)
>
> **Router-Verarbeitung:** "Router lesen nur die Adresse auf dem Karton"
> - Öffnen nicht das innere Geschenk (Anwendungsdaten)
> - Ändern nur die äußere Verpackung (MAC-Adressen)
> - Notieren sich die Route (TTL dekrementieren)

## Zusammenhänge

- [[03-Referenzmodelle/01-OSI-Modell|OSI-Modell]] - Detaillierteres 7-Schichten-Modell
- [[03-Referenzmodelle/02-TCP-IP-Modell|TCP/IP-Modell]] - Das verwendete DoD-Modell
- [[03-Referenzmodelle/03-Schichtenvergleich|Schichtenvergleich]] - OSI vs. TCP/IP
- [[03-Referenzmodelle/06-Netzwerkschicht/02-Routing|Routing]] - Router-Verarbeitung im Detail

## Quellen

- Tanenbaum, A. S.: Computernetzwerke, Kap. 1.4
- Kurose, J., Ross, K.: Computernetze, Kap. 1.5
- [[A-RFC-Index|RFC 1122]] - Requirements for Internet Hosts
