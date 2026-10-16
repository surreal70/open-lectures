---
author: Andreas Hümmer
title: Netzwerktypen
tags:
  - vorlesung
  - rn
  - grundlagen
  - netzwerktypen
  - lan
  - wan
  - pan
  - man
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Netzwerktypen

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Netzwerke nach ihrer räumlichen Ausdehnung klassifizieren
> - Die Unterschiede zwischen PAN, LAN, MAN, WAN und GAN erläutern
> - Netzwerke nach Funktion und Zugriffsart einteilen
> - Typische Technologien und Bandbreiten den Netzwerktypen zuordnen

## Klassifikation nach räumlicher Ausdehnung

Die gebräuchlichste Klassifikation von Netzwerken erfolgt nach ihrer geografischen Reichweite:

### Übersicht der Netzwerkdimensionen

| Kürzel | Bezeichnung | Dimension | Typische Technologien | Bandbreite |
|--------|-------------|-----------|----------------------|------------|
| **CN/NOC** | Network on a Chip | µm - mm | I²C, SPI, PCIe | Gbps - Tbps |
| **BAN** | Body Area Network | Am Körper | Bluetooth LE, ANT+ | kbps - Mbps |
| **PAN** | Personal Area Network | ~10 m | Bluetooth, ZigBee, NFC | kbps - Mbps |
| **LAN** | Local Area Network | Haus/Campus | Ethernet, WiFi | Mbps - Gbps |
| **CAN** | Cluster Area Network | Rechenzentrum | InfiniBand, RoCE | 100+ Gbps |
| **MAN** | Metropolitan Area Network | Stadt/Region | Glasfaser, WiMAX | Gbps |
| **WAN** | Wide Area Network | Land/Kontinent | MPLS, Glasfaser | Gbps |
| **GAN** | Global Area Network | Weltweit | Internet, Satellit | variabel |
| **IPN** | Interplanetary Network | Sonnensystem | Richtfunk, Laser | kbps - Mbps |

## Extreme Netzwerktypen

### Network on a Chip (NoC)

Am unteren Ende der Skala: Kommunikation **innerhalb eines einzelnen Chips**.

**Was ist das?**
Moderne Prozessoren enthalten Milliarden von Transistoren, die miteinander kommunizieren müssen. Ein NoC ist ein miniaturisiertes Netzwerk auf einem Chip, das verschiedene Komponenten (CPU-Kerne, Cache, Memory Controller) verbindet.

**Warum wird das gebraucht?**
- Traditionelle Bus-Architekturen skalieren nicht mit steigender Kernzahl
- Punkt-zu-Punkt-Verbindungen werden bei vielen Komponenten zu komplex
- NoC ermöglicht parallele Kommunikation zwischen vielen Komponenten

**Herausforderungen:**

| Herausforderung | Beschreibung |
|-----------------|--------------|
| **Latenz** | Wenige Nanosekunden tolerierbar |
| **Energieverbrauch** | Jedes pJ zählt bei Milliarden Operationen/s |
| **Fläche** | Router und Leitungen konkurrieren mit Logik um Chipfläche |
| **Wärme** | Hotspots bei hoher Kommunikationsdichte |
| **Zuverlässigkeit** | Fertigungsfehler in nm-Strukturen |

**Technologien:**
- **I²C** (Inter-Integrated Circuit): Einfach, langsam (100 kbps - 3,4 Mbps)
- **SPI** (Serial Peripheral Interface): Schneller, mehr Pins
- **PCIe** (intern): Zwischen CPU und Peripherie
- **Mesh/Torus-Topologien** auf dem Chip

> [!beispiel] Beispiel: Intel Mesh Architecture
> Moderne Intel-Prozessoren (ab Skylake-X) verwenden eine Mesh-Topologie auf dem Chip: Jeder Kern ist mit seinen Nachbarn verbunden, was die Latenz beim Cache-Zugriff reduziert und die Bandbreite skaliert.

---

### Cluster Area Network / High-Performance Computing Network (CAN/HPC)

Verbindung von Hochleistungsrechnern in **Supercomputer-Clustern**.

**Was ist das?**
Ein spezialisiertes Netzwerk, das Tausende von Rechenknoten in einem Cluster verbindet. Hier zählt jede Mikrosekunde Latenz und jedes Bit/s Bandbreite.

**Warum wird das gebraucht?**
- Wissenschaftliche Simulationen (Klima, Teilchenphysik, Genomik)
- KI-Training mit verteilten GPUs
- Finanzmodellierung in Echtzeit
- Jeder Knoten muss ständig mit anderen kommunizieren (MPI)

**Herausforderungen:**

| Herausforderung | Beschreibung |
|-----------------|--------------|
| **Ultra-Low Latency** | < 1 µs für Message Passing |
| **Extreme Bandbreite** | 200-400 Gbps pro Link |
| **RDMA** | Remote Direct Memory Access ohne CPU-Overhead |
| **Skalierung** | Tausende Knoten, Millionen von Nachrichten/s |
| **Kosten** | Spezial-Hardware, teuer |

**Technologien:**

| Technologie | Bandbreite | Latenz | Anmerkung |
|-------------|------------|--------|-----------|
| **InfiniBand HDR** | 200 Gbps | < 1 µs | HPC-Standard |
| **InfiniBand NDR** | 400 Gbps | < 1 µs | Aktuell |
| **RoCE v2** | 100-400 Gbps | < 2 µs | RDMA over Ethernet |
| **Slingshot** | 200 Gbps | < 1 µs | Cray/HPE |
| **NVIDIA NVLink** | 900 GB/s | - | GPU-zu-GPU |

![[hpc-cluster-infiniband.png]]
*<span class="fig-id">03-01-02-hpc-cluster-infiniband</span>: Vereinfachte Darstellung eines HPC-Clusters mit InfiniBand Fabric.*

> [!info] RDMA - Remote Direct Memory Access
> Bei RDMA kann ein Knoten direkt in den Speicher eines anderen schreiben, ohne dass dessen CPU beteiligt ist. Das reduziert Latenz drastisch und entlastet die CPU für Berechnungen.

---

### Interplanetary Network (IPN) / Deep Space Network

Am oberen Ende der Skala: Kommunikation über **Millionen von Kilometern**.

**Was ist das?**
Ein Netzwerk zur Kommunikation mit Raumsonden, Rovern und zukünftigen Kolonien im Sonnensystem. Die NASA und andere Raumfahrtagenturen arbeiten an Protokollen für ein "interplanetares Internet".

**Warum wird das gebraucht?**
- Kommunikation mit Mars-Rovern und -Orbitern
- Zukünftige bemannte Missionen
- Wissenschaftliche Datenübertragung von Sonden
- Autonome Raumfahrzeuge brauchen Koordination

**Die fundamentalen Herausforderungen:**

| Herausforderung | Erde ↔ Mars | Erde ↔ Jupiter | Anmerkung |
|-----------------|-------------|----------------|-----------|
| **Entfernung** | 55-400 Mio. km | 588-968 Mio. km | Variiert stark |
| **Lichtlaufzeit (one-way)** | 3-22 min | 33-53 min | TCP unmöglich! |
| **Round-Trip-Time** | 6-44 min | 66-106 min | Kein Handshake |
| **Signaldämpfung** | -270 dB | -290 dB | Enorm |
| **Bandbreite** | kbps - Mbps | kbps | Sehr begrenzt |
| **Verfügbarkeit** | Unterbrochen | Unterbrochen | Planetenrotation, Sonne |

**Warum TCP/IP nicht funktioniert:**
- TCP erwartet Acknowledgments innerhalb von Sekunden → Timeout
- IP-Routing erwartet stabile Pfade → Planeten bewegen sich
- DNS-Lookups unmöglich bei 20 Minuten Latenz

**Lösung: Delay-Tolerant Networking (DTN)**

![[dtn-store-forward.png]]
*<span class="fig-id">03-01-02-dtn-store-forward</span>: DTN Bundle Protocol – Nachrichten werden gespeichert und weitergeleitet, wenn Kontakt möglich ist.*

**Technologien:**
- **DSN** (Deep Space Network): 3 Bodenstationen (Goldstone, Madrid, Canberra)
- **X-Band/Ka-Band**: Mikrowellen-Frequenzen für Daten
- **Optical Communication**: Laser für höhere Bandbreiten (LCRD, DSOC)
- **Bundle Protocol (BP)**: Ersetzt TCP/IP für DTN
- **LTP** (Licklider Transmission Protocol): Ersetzt TCP

> [!beispiel] Beispiel: Mars Reconnaissance Orbiter
> Aktuelle Mars-Kommunikation nutzt den MRO als Relais:
> - Rover → MRO: UHF, ~2 Mbps
> - MRO → Erde: X-Band, ~6 Mbps (bei günstiger Position)
> - Gesamtdatenrate zur Erde: variiert von kbps bis wenige Mbps

**Zukünftige Entwicklungen:**
- **Lunar Gateway**: Kommunikations-Hub im Mondorbit
- **Mars-Relay-Netzwerk**: Mehrere Orbitersatelliten
- **Laser-Kommunikation**: 10-100x höhere Datenraten als Funk

---

### Personal Area Network (PAN)

Ein PAN verbindet Geräte im unmittelbaren persönlichen Umfeld (typisch 10 m Reichweite).

**Typische Anwendungen:**
- Bluetooth-Kopfhörer mit Smartphone
- Smartwatch mit Handy
- Wireless-Tastatur und -Maus
- Fitness-Tracker

**Technologien:**

| Technologie | Reichweite | Bandbreite | Energieverbrauch |
|-------------|------------|------------|------------------|
| Bluetooth Classic | 10-100 m | 1-3 Mbps | Mittel |
| Bluetooth LE | 10-50 m | 125 kbps - 2 Mbps | Sehr niedrig |
| ZigBee | 10-100 m | 250 kbps | Sehr niedrig |
| NFC | < 10 cm | 424 kbps | Minimal |
| IrDA | < 1 m | 4-16 Mbps | Niedrig |

> [!beispiel] Beispiel: Bluetooth-Piconet
> Ein Bluetooth-PAN bildet ein sogenanntes **Piconet**: Ein Master-Gerät (z.B. Smartphone) koordiniert bis zu 7 aktive Slave-Geräte. Mehrere Piconets können zu einem **Scatternet** verbunden werden.

### Local Area Network (LAN)

Ein LAN verbindet Geräte innerhalb eines begrenzten geografischen Bereichs (Gebäude, Campus).

**Charakteristiken:**
- Hohe Bandbreite (100 Mbps - 100 Gbps)
- Niedrige Latenz (< 1 ms)
- Typisch ein Eigentümer/Administrator
- Private IP-Adressierung

**Technologien:**

| Technologie | Standard | Bandbreite | Medium |
|-------------|----------|------------|--------|
| Fast Ethernet | 802.3u | 100 Mbps | Kupfer (Cat5) |
| Gigabit Ethernet | 802.3ab | 1 Gbps | Kupfer (Cat5e/6) |
| 10 Gigabit Ethernet | 802.3ae | 10 Gbps | Glasfaser/Cat6a |
| WiFi 5 | 802.11ac | bis 6,9 Gbps | Funk (5 GHz) |
| WiFi 6 | 802.11ax | bis 9,6 Gbps | Funk (2,4/5/6 GHz) |
| WiFi 7 | 802.11be | bis 46 Gbps | Funk (2,4/5/6 GHz) |

![[lan-struktur.png]]
*<span class="fig-id">03-01-02-lan-struktur</span>: Typische LAN-Struktur mit Router, Switch, kabelgebundenen PCs und WLAN-Anbindung über Access Point.*

### Metropolitan Area Network (MAN)

Ein MAN verbindet mehrere LANs innerhalb einer Stadt oder Region.

**Typische Anwendungen:**
- Universitäts-Campus-Vernetzung
- Stadtverwaltungs-Netzwerke
- Cable-TV-Netze
- Mobilfunk-Backhaul

**Technologien:**
- Metro-Ethernet
- SONET/SDH
- WiMAX (802.16)
- Glasfaserring

> [!info] Carrier Ethernet
> Moderne MANs nutzen häufig **Carrier Ethernet** – eine Weiterentwicklung von Ethernet für Provider-Netze mit Quality of Service (QoS), Skalierbarkeit und Management-Features.

### Wide Area Network (WAN)

Ein WAN erstreckt sich über große geografische Distanzen (Länder, Kontinente).

**Charakteristiken:**
- Niedrigere Bandbreite als LAN (historisch)
- Höhere Latenz
- Typisch über Provider/Carrier
- Öffentliche oder gemietete Leitungen

**Technologien:**

| Technologie      | Beschreibung                   | Typische Nutzung      |
| ---------------- | ------------------------------ | --------------------- |
| **MPLS**         | Multi-Protocol Label Switching | Enterprise-WANs       |
| **SD-WAN**       | Software-Defined WAN           | Moderne Unternehmen   |
| **Leased Lines** | Dedizierte Verbindungen        | Kritische Anwendungen |
| **VPN**          | Virtual Private Network        | Sichere Verbindungen  |
| **Frame Relay**  | Legacy-Technologie             | (veraltet)            |
| **ATM**          | Asynchronous Transfer Mode     | (veraltet)            |

### Global Area Network (GAN) / Internet

Das Internet ist das größte GAN – ein Netzwerk von Netzwerken.

**Struktur:**

![[internet-hierarchie.png]]
*<span class="fig-id">03-01-02-internet-hierarchie</span>: Hierarchische Struktur des Internets mit Tier 1, 2 und 3 Providern.*

| Tier | Beschreibung | Beispiele |
|------|--------------|-----------|
| **Tier 1** | Globale Backbone-Provider, peeren untereinander kostenlos (Settlement-Free Peering) | AT&T, NTT, Lumen (Level3), Cogent |
| **Tier 2** | Regionale/nationale Provider, kaufen Transit von Tier 1, peeren mit anderen Tier 2 | Deutsche Telekom, Vodafone, Comcast |
| **Tier 3** | Lokale ISPs und Access-Provider, kaufen Transit von Tier 1 oder 2 | Lokale Stadtwerke, 1&1, o2 |

## Klassifikation nach Funktion

### Client-Server-Netzwerke

Zentrale Server stellen Dienste bereit, Clients nutzen sie.

**Vorteile:**
- Zentrale Verwaltung
- Bessere Sicherheit
- Einfache Backups
- Skalierbar

**Nachteile:**
- Single Point of Failure
- Höhere Kosten
- Server-Überlastung möglich

### Peer-to-Peer-Netzwerke (P2P)

Alle Teilnehmer sind gleichberechtigt und können sowohl Dienste anbieten als auch nutzen.

**Vorteile:**
- Kein zentraler Server nötig
- Ressourcen-Sharing
- Ausfallsicher (dezentral)

**Nachteile:**
- Schwer zu verwalten
- Sicherheitsrisiken
- Inkonsistente Verfügbarkeit

> [!beispiel] Beispiele für P2P
> - BitTorrent (File-Sharing)
> - Bitcoin (Blockchain)
> - Skype (teilweise)
> - IPFS (InterPlanetary File System)

### Hybride Netzwerke

Kombination aus Client-Server und P2P-Elementen.

**Beispiel:** Moderne Streaming-Dienste nutzen zentrale Server für Katalog und Authentifizierung, aber P2P für Content-Delivery.

## Klassifikation nach Zugriffsart

### Private Netzwerke

- Nur für autorisierte Nutzer
- Eigene Infrastruktur oder VPN
- Typisch: Unternehmens-LANs

### Öffentliche Netzwerke

- Für alle zugänglich
- Beispiel: Internet, öffentliches WLAN

### Virtual Private Networks (VPN)

Sichere Verbindung über öffentliche Netze:

![[vpn-tunnel.png]]
*<span class="fig-id">03-01-02-vpn-tunnel</span>: VPN-Tunnel – verschlüsselte Verbindung durch das öffentliche Internet.*

## Kommunikationsarten in Netzwerken

Die Art der Datenübertragung hängt von der Anzahl der Empfänger ab:

| Art | Beschreibung | Anwendung | Beispiel |
|-----|--------------|-----------|----------|
| **Unicast** | 1:1 | Direkte Kommunikation | HTTP-Request, E-Mail |
| **Broadcast** | 1:alle | An alle im Netz | ARP, DHCP-Discover |
| **Multicast** | 1:Gruppe | An Abonnenten | IPTV, Video-Konferenz |
| **Anycast** | 1:nächster | An nächsten aus Gruppe | DNS-Root-Server, CDN |

![[kommunikationsarten.png]]
*<span class="fig-id">03-01-02-kommunikationsarten</span>: Vergleich der vier Kommunikationsarten: Unicast, Broadcast, Multicast und Anycast.*

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Netzwerke werden primär nach räumlicher Ausdehnung klassifiziert: PAN → LAN → MAN → WAN → GAN
> - Jeder Netzwerktyp hat charakteristische Technologien, Bandbreiten und Latenzen
> - Funktionale Klassifikation: Client-Server vs. Peer-to-Peer vs. Hybrid
> - Zugriffsklassifikation: Privat vs. Öffentlich vs. VPN
> - Kommunikationsarten: Unicast, Broadcast, Multicast, Anycast

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Unterschiede zwischen PAN, LAN, MAN, WAN bezüglich Reichweite und Technologie
> - Nennen Sie typische Bandbreiten für jede Netzwerkklasse
> - Erklären Sie den Unterschied zwischen Client-Server und P2P
> - Unterscheiden Sie Unicast, Broadcast, Multicast und Anycast mit Beispielen
> - Wissen Sie, was ein VPN ist und wofür es eingesetzt wird

## Verwandte Themen

- [[01-Historie]] – Entwicklung der Netzwerktechnologien
- [[02-Standards-und-Gremien]] – Standardisierungsgremien und IEEE 802
- [[04-Topologien]] – Physische und logische Netzwerkstrukturen
- [[00-Referenzmodelle-Index|Referenzmodelle]] – OSI und TCP/IP Modell
- [[01-Ethernet|Ethernet]] – Der dominierende LAN-Standard

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
- IEEE 802 Standards
