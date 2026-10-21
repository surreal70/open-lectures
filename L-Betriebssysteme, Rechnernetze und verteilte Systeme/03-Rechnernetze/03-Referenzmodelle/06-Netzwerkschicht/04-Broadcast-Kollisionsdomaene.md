---
author: Andreas Hümmer
title: Broadcast- und Kollisionsdomäne
tags:
  - content
  - rn
  - network-layer
  - broadcast
  - kollision
  - switch
  - router
created: '2026-10-13'
modified: '2026-10-21'
bereich: RN
---

# Broadcast- und Kollisionsdomäne

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Begriffe Broadcast- und Kollisionsdomäne definieren
> - Die Unterschiede zwischen beiden Konzepten erklären
> - Erkennen, welche Geräte Domänen trennen oder verbinden
> - Netzwerke hinsichtlich ihrer Domänenstruktur analysieren

## Definitionen

### Kollisionsdomäne (Collision Domain)

Eine **Kollisionsdomäne** ist der Netzwerkbereich, in dem Datenpakete miteinander kollidieren können, wenn zwei oder mehr Geräte gleichzeitig senden.

**Eigenschaften:**
- Layer 1 / Layer 2 Konzept (Physisch/Sicherung)
- Betrifft das gemeinsam genutzte Übertragungsmedium
- Nur relevant bei Half-Duplex und Shared Media
- Alle Geräte "hören" die gleichen Signale
- CSMA/CD regelt den Zugriff

![[kollisionsdomaene-koaxial.png]]
*<span class="fig-id">03-06-04-kollisionsdomaene-koaxial</span>: Koaxial-Ethernet (10BASE2/10BASE5) – alle Geräte teilen sich eine Kollisionsdomäne.*

### Broadcast-Domäne (Broadcast Domain)

Eine **Broadcast-Domäne** ist der Netzwerkbereich, in dem ein Broadcast-Frame (Ziel: FF:FF:FF:FF:FF:FF) alle Geräte erreicht.

**Eigenschaften:**
- Layer 2 / Layer 3 Konzept (Sicherung/Vermittlung)
- Betrifft die logische Netzwerkstruktur
- Alle Geräte empfangen Broadcast-Frames
- Entspricht typischerweise einem IP-Subnetz
- Begrenzt durch Router (Layer 3 Geräte)

![[broadcastdomaene-switch.png]]
*<span class="fig-id">03-06-04-broadcastdomaene-switch</span>: Geswitchtes Ethernet – alle Geräte teilen sich eine Broadcast-Domäne, aber keine Kollisionen mehr.*

## Gegenüberstellung

### Vergleichstabelle

| Aspekt | Kollisionsdomäne | Broadcast-Domäne |
|--------|------------------|------------------|
| **OSI-Schicht** | Layer 1 (physisch) | Layer 2 (logisch) |
| **Trennung durch** | Switch, Bridge | Router, Layer-3-Switch |
| **Relevanz** | Shared Media, Half-Duplex | Immer (auch Full-Duplex) |
| **Betrifft** | Signalübertragung | Frame-Verteilung |
| **Problem** | Kollisionen, Durchsatz | Broadcast-Stürme, Skalierung |
| **Adressierung** | - | MAC FF:FF:FF:FF:FF:FF |

### Visuelle Gegenüberstellung

![[szenarien-vergleich.png]]
*<span class="fig-id">03-06-04-szenarien-vergleich</span>: Vergleich Hub vs. Switch vs. Router – Auswirkung auf Kollisions- und Broadcast-Domänen.*

## Geräte und ihre Wirkung auf Domänen

### Übersicht

| Gerät          | Kollisions-Domäne | Broadcast-Domäne | OSI-Layer |
| -------------- | ----------------- | ---------------- | --------- |
| Repeater/Hub   | Verbindet         | Verbindet        | Layer 1   |
| Bridge         | **TRENNT**        | Verbindet        | Layer 2   |
| Switch         | **TRENNT**        | Verbindet        | Layer 2   |
| Router         | **TRENNT**        | **TRENNT**       | Layer 3   |
| Layer-3-Switch | **TRENNT**        | **TRENNT**       | Layer 3   |
|                |                   |                  |           |

*\* Bei Routing zwischen VLANs*

> [!tip] Merksätze
> - **Router** trennen **BEIDE** Domänen
> - **Switches** trennen **NUR** Kollisionsdomänen
> - **Hubs** trennen **NICHTS**

### Detailbetrachtung: Switch

Ein Switch mit n Ports erzeugt:
- **n Kollisionsdomänen** (eine pro Port)
- **1 Broadcast-Domäne** (alle Ports)

![[switch-mikrosegmentierung.png]]
*<span class="fig-id">03-06-04-switch-mikrosegmentierung</span>: Switch mit MAC-Adresstabelle – jeder Port ist eine eigene Kollisionsdomäne.*

- **Unicast:** Switch leitet gezielt an den richtigen Port (MAC-Tabelle)
- **Broadcast:** Switch flutet an ALLE Ports (außer Quell-Port)

### Detailbetrachtung: Router

Ein Router mit n Interfaces erzeugt:
- **n Kollisionsdomänen** (eine pro Interface)
- **n Broadcast-Domänen** (eine pro Interface/Subnetz)

![[router-broadcast-grenze.png]]
*<span class="fig-id">03-06-04-router-broadcast-grenze</span>: Router mit 3 Interfaces – jedes Interface ist eine eigene Broadcast-Domäne.*

- Broadcast von PC1 erreicht PC2, PC3 (gleiches Subnetz)
- Broadcast erreicht **NICHT** PC4–PC9 (Router blockiert!)

## Überlappung und Zusammenhang

### Wann sind beide Domänen identisch?

**Fall 1: Shared Medium (Hub/Koaxial)**
- Kollisionsdomäne = Broadcast-Domäne (identisch)
- Keine Trennung vorhanden

**Fall 2: Switched Network (ohne Router)**
- Mehrere Kollisionsdomänen ⊂ eine Broadcast-Domäne
- Kollisionsdomänen sind Teilmengen der Broadcast-Domäne

**Fall 3: Routed Network**
- Kollisionsdomänen und Broadcast-Domänen unabhängig
- BD₁ ∩ BD₂ = ∅ (Broadcast-Domänen sind disjunkt)

## Praktische Auswirkungen

### Probleme großer Kollisionsdomänen

> [!warning] Große Kollisionsdomäne (z.B. Hub-Netzwerk)
> **Probleme:**
> - Häufige Kollisionen bei gleichzeitigem Senden
> - Geringe effektive Bandbreite (alle teilen sich das Medium)
> - Wartezeiten durch Backoff-Algorithmus
> - Maximale Ausdehnung begrenzt (5-4-3-Regel)
> 
> **Lösung:** Switches einsetzen (Mikrosegmentierung) → jeder Port wird zur eigenen Kollisionsdomäne

### Probleme großer Broadcast-Domänen

> [!warning] Große Broadcast-Domäne (z.B. flaches L2-Netzwerk)
> **Probleme:**
> - Broadcast-Stürme möglich (z.B. durch Switching-Loops)
> - Jedes Gerät verarbeitet jeden Broadcast → CPU-Last
> - ARP-Tabellen werden groß und langsam
> - Sicherheitsrisiko: alle Geräte sehen alle Broadcasts
> - Skalierungsprobleme ab ca. 500 Hosts
> 
> **Lösungen:**
> - Router einsetzen (L3-Segmentierung)
> - VLANs konfigurieren (virtuelle Trennung auf einem Switch)
> - Layer-3-Switches mit Inter-VLAN-Routing

### Empfehlungen für das Netzwerkdesign

| Größe | Kollisionsdomänen | Broadcast-Domänen | Empfehlung |
|-------|-------------------|-------------------|------------|
| Klein (<50 Hosts) | Via Switch segmentiert | 1 reicht oft | Flaches L2-Netz OK |
| Mittel (50-200) | Via Switch segmentiert | 1-5 VLANs | VLANs empfohlen |
| Groß (>200 Hosts) | Via Switch segmentiert | Viele VLANs/Subnetze | L3-Design Pflicht |

## VLANs und Broadcast-Domänen

VLANs (Virtual Local Area Networks) teilen einen physischen Switch in mehrere logische Switches und damit in separate Broadcast-Domänen.

![[vlan-broadcast-domaenen.png]]
*<span class="fig-id">03-06-04-vlan-broadcast-domaenen</span>: VLANs erzeugen virtuelle Broadcast-Domänen – gleicher Switch, aber logisch getrennt.*

**Eigenschaften:**
- Broadcast von PC1 erreicht nur PC2, PC3 (VLAN 10)
- Broadcast von PC4 erreicht nur PC5, PC6 (VLAN 20)
- Kommunikation zwischen VLANs nur über Router oder Layer-3-Switch

## WLANs und Domänen

Im Vergleich zu kabelgebundenen Netzwerken verhalten sich WLANs (802.11) bezüglich Kollisions- und Broadcast-Domänen anders:

### Kollisionsdomäne im WLAN

**Alle Geräte eines Access Points teilen sich eine Kollisionsdomäne:**
- Das Funkmedium ist ein Shared Medium (wie früher Koaxial-Ethernet)
- Gleichzeitiges Senden führt zu Kollisionen (Interferenz)
- WLAN nutzt **CSMA/CA** (Collision Avoidance) statt CSMA/CD
- Kollisionserkennung ist im Funk nicht möglich → Kollisionsvermeidung durch RTS/CTS

> [!info] CSMA/CA vs. CSMA/CD
> - **CSMA/CD** (Ethernet): Senden, Kollision erkennen, Backoff
> - **CSMA/CA** (WLAN): Vor dem Senden prüfen, ob Medium frei ist, Wartezeit einhalten, dann senden

### Broadcast-Domäne im WLAN

**Ein WLAN-Netzwerk (SSID) entspricht einer Broadcast-Domäne:**
- Alle mit demselben AP verbundenen Clients empfangen Broadcasts
- Der Access Point leitet Broadcasts an alle assoziierten Clients weiter
- Bei mehreren APs mit gleicher SSID (ESS): gemeinsame Broadcast-Domäne

### Besonderheiten

| Aspekt | Kabel (Switch) | WLAN (Access Point) |
|--------|----------------|---------------------|
| Kollisionsdomäne | Pro Port getrennt | Alle Clients teilen sich eine |
| Broadcast-Domäne | Alle Ports gemeinsam | Alle Clients gemeinsam |
| Kollisionsvermeidung | Full-Duplex | CSMA/CA |
| Durchsatz | Dediziert pro Port | Geteilt unter allen Clients |

> [!warning] Praxisrelevanz
> Ein stark genutzter WLAN Access Point mit vielen Clients leidet unter:
> - Geteilter Bandbreite (alle teilen sich das Medium)
> - Erhöhten Wartezeiten durch CSMA/CA
> - Broadcast-Traffic belastet alle Clients
> 
> **Lösungen:** Mehrere APs, verschiedene Kanäle, VLANs über WLAN (Multiple SSIDs)

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> 
> **Kollisionsdomäne:**
> - Layer 1 Konzept
> - Bereich, wo Signale kollidieren können
> - Getrennt durch: Switch, Bridge
> - Bei Full-Duplex/Switches: Pro Port eine Domäne
> 
> **Broadcast-Domäne:**
> - Layer 2/3 Konzept
> - Bereich, den ein Broadcast erreicht
> - Getrennt durch: Router, Layer-3-Switch, VLAN
> - Entspricht typischerweise einem IP-Subnetz
> 
> **Beziehung:**
> - Kollisionsdomänen ⊆ Broadcast-Domäne
> - Bei Hubs: Beide identisch
> - Bei Switches: Viele Kollisions-D., eine Broadcast-D.
> - Bei Routern: Beide getrennt

## Nützliche Diagnose-Befehle

> [!info] Netzwerkgeräte und Interfaces anzeigen
> ```bash
> # Linux
> ip link show                       # Alle Interfaces
> ip -s link show                    # Mit Statistiken (Kollisionen!)
> ethtool eth0                       # Interface-Details (Duplex, Speed)
> bridge fdb show                    # MAC-Adresstabelle (bei Linux-Bridge)
> 
> # Windows
> ipconfig /all                      # Alle Interfaces
> netsh interface show interface     # Interface-Status
> getmac /v                          # MAC-Adressen aller Interfaces
> ```

> [!info] ARP/Neighbor-Tabelle (zeigt lokale Broadcast-Domäne)
> ```bash
> # Linux
> ip neigh show                      # ARP-Cache (IPv4 + IPv6)
> arp -n                             # Nur IPv4 ARP
> 
> # Windows
> arp -a                             # ARP-Cache anzeigen
> netsh interface ipv6 show neighbors # IPv6 Neighbor Cache
> ```

> [!info] Switch-ähnliche Informationen
> ```bash
> # Linux (wenn als Bridge konfiguriert)
> brctl showmacs br0                 # MAC-Tabelle der Bridge
> bridge link show                   # Bridge-Ports
> 
> # Windows
> # Auf managed Switches: Web-Interface oder CLI (show mac-address-table)
> ```

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Kollisionsdomäne: Layer 1/2 Konzept, getrennt durch Switch/Bridge
> - Broadcast-Domäne: Layer 2/3 Konzept, getrennt durch Router
> - Anzahl der Domänen in Netzwerkdiagrammen zählen können
> - Probleme großer Broadcast-Domänen (Broadcast-Stürme, Skalierung)

> [!question] **Typische Prüfungsfragen**
> - Was ist der Unterschied zwischen Kollisions- und Broadcast-Domäne?
> - Welches Gerät trennt Kollisionsdomänen? Welches trennt Broadcast-Domänen?
> - Ein Netzwerk hat 2 Switches (je 10 PCs) verbunden durch einen Router. Wie viele Kollisions- und Broadcast-Domänen gibt es?
> - Warum sind große Broadcast-Domänen problematisch?

### Typische Prüfungsaufgabe

> [!example] Beispiel
> **Frage:** Ein Netzwerk besteht aus 2 Switches, verbunden durch einen Router. An jedem Switch hängen 10 PCs. Wie viele Kollisions- und Broadcast-Domänen gibt es?
> 
> **Antwort:**
> - Kollisionsdomänen: 20 + 2 = 22 (10 pro Switch + je 1 für Router-Port)
> - Broadcast-Domänen: 2 (eine pro Switch/Subnetz, Router trennt)

## Verwandte Themen

- [[../05-Sicherungsschicht/03-MAC-Protokolle|CSMA/CD]] – Kollisionserkennung
- [[01-IP-Protokoll]] – Subnetting und Broadcast-Adressen
- [[02-Routing]] – Router als Broadcast-Grenze
- [[../05-Sicherungsschicht/01-Rahmenbildung|Ethernet-Frame]] – Broadcast-MAC-Adresse

## Quellen

- Tanenbaum, A. S.: Computernetzwerke, Kap. 4
- Kurose, J., Ross, K.: Computernetze, Kap. 6
