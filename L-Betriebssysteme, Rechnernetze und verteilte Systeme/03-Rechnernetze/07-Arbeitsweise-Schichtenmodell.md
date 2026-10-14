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

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    SCHICHTENDURCHLAUF: CLIENT → ROUTER → SERVER                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│      CLIENT                    ROUTER                    SERVER                 │
│   (Sender)                  (Vermittler)              (Empfänger)              │
│                                                                                 │
│  ┌─────────┐                                          ┌─────────┐              │
│  │ 7 Anw.  │─────────────────────────────────────────►│ 7 Anw.  │              │
│  ├─────────┤                                          ├─────────┤              │
│  │ 6 Darst.│                                          │ 6 Darst.│              │
│  ├─────────┤                                          ├─────────┤              │
│  │ 5 Sitz. │                                          │ 5 Sitz. │              │
│  ├─────────┤                                          ├─────────┤              │
│  │ 4 Trans.│─────────────────────────────────────────►│ 4 Trans.│              │
│  ├─────────┤              ┌─────────┐                 ├─────────┤              │
│  │ 3 Verm. │─────────────►│ 3 Verm. │────────────────►│ 3 Verm. │              │
│  ├─────────┤              ├─────────┤                 ├─────────┤              │
│  │ 2 Sich. │─────────────►│ 2 Sich. │────────────────►│ 2 Sich. │              │
│  ├─────────┤              ├─────────┤                 ├─────────┤              │
│  │ 1 Bit.  │══════════════│ 1 Bit.  │═════════════════│ 1 Bit.  │              │
│  └─────────┘              └─────────┘                 └─────────┘              │
│       │                        │                           ▲                   │
│       │                        │                           │                   │
│       ▼                        ▼                           │                   │
│  ════════════════════════════════════════════════════════════                  │
│           LAN 1                         LAN 2                                  │
│   (physisches Medium)          (physisches Medium)                             │
│                                                                                 │
│  LEGENDE:                                                                       │
│  ───────► Logische Verbindung (Ende-zu-Ende)                                   │
│  ═══════ Physische Übertragung                                                 │
│                                                                                 │
│  CLIENT: Daten wandern von Schicht 7 → 4 → 3 → 2 → 1 (Einkapselung)           │
│  ROUTER: Empfang 1 → 2 → 3, dann Senden 3 → 2 → 1 (nur Layer 1-3)             │
│  SERVER: Daten wandern von Schicht 1 → 2 → 3 → 4 → 7 (Entkapselung)           │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Detailansicht mit Datenfluss

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         DATENFLUSS DURCH DIE SCHICHTEN                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  CLIENT (Einkapselung)         ROUTER              SERVER (Entkapselung)        │
│                                                                                 │
│  7 │ HTTP-Daten │                                        │ HTTP-Daten │ 7      │
│    └─────┬──────┘                                        └──────▲─────┘        │
│          │ erzeugen                                      lesen  │              │
│          ▼                                                      │              │
│  4 │ TCP │ Daten │                                      │ TCP │ Daten │ 4      │
│    └──┬──┴───────┘                                      └──▲──┴───────┘        │
│       │ +Header                                    -Header │                   │
│       ▼                                                    │                   │
│  3 │ IP │ TCP │ Daten │         │ IP │ TCP │ Daten │      │ IP │ TCP │ Daten │ 3
│    └─┬──┴─────┴───────┘         └──┬─┴─────┴───────┘      └──▲─┴─────┴───────┘ │
│      │ +Header              Routing│TTL--                    │ -Header         │
│      ▼                             ▼                         │                 │
│  2 │Eth│ IP │ TCP │ Daten │FCS│  │Eth'│ IP │ TCP │ Daten │FCS'│  │Eth│...│FCS│ 2
│    └─┬─┴────┴─────┴───────┴───┘  └──┬─┴────┴─────┴───────┴────┘  └─▲─┴───┴───┘ │
│      │ +Header/Trailer    MAC ändern│                              │ -H/T      │
│      ▼                              ▼                              │           │
│  1   ══════════════════════════════════════════════════════════════            │
│      Bits auf Kupfer/LWL/Funk      Bits auf Kupfer/LWL/Funk                    │
│                                                                                 │
│  ──────────────────────────────────────────────────────────────────────────────│
│                                                                                 │
│  Schicht  │ Client           │ Router              │ Server                    │
│  ─────────┼──────────────────┼─────────────────────┼───────────────────────────│
│  7-5      │ Daten erzeugen   │ —                   │ Daten verarbeiten         │
│  4        │ +TCP-Header      │ —                   │ -TCP-Header               │
│  3        │ +IP-Header       │ Routing, TTL--      │ -IP-Header                │
│  2        │ +Eth-Header/FCS  │ MAC-Adressen ändern │ -Eth-Header/FCS           │
│  1        │ Bits senden      │ Bits weiterleiten   │ Bits empfangen            │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

> [!important] Kernkonzept
> - **Endgeräte (Client, Server):** Verarbeiten alle 7 Schichten
> - **Router:** Verarbeiten nur Schichten 1-3 (Netzzugang + Internet)
> - **Switches:** Verarbeiten nur Schichten 1-2 (Netzzugang)

## Szenario

```
┌─────────────────────────────────────────────────────────────────┐
│                         SZENARIO                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Client                    Router                  Server      │
│   (Browser)                                        (Webserver)  │
│                                                                 │
│   ┌─────────┐            ┌─────────┐            ┌─────────┐    │
│   │   PC    │────────────│  Router │────────────│ Server  │    │
│   │         │   LAN 1    │         │   LAN 2    │         │    │
│   └─────────┘            └─────────┘            └─────────┘    │
│                                                                 │
│   IP: 192.168.1.10       192.168.1.1             10.0.0.5      │
│   MAC: AA:AA:AA:AA:AA:AA 10.0.0.1                CC:CC:CC:CC:  │
│                          BB:BB:BB:BB:BB:BB       CC:CC         │
│                          (LAN1 / LAN2)                         │
│                                                                 │
│   Anfrage: GET http://10.0.0.5/index.html                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Client – Daten senden

### Übersicht der Einkapselung

```
┌─────────────────────────────────────────────────────────────────┐
│              EINKAPSELUNG (ENCAPSULATION) – CLIENT              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Anwendung erzeugt Daten                                        │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HTTP-Request                          │   │
│  │         "GET /index.html HTTP/1.1..."                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│         │                                                       │
│         ▼  Transportschicht fügt TCP-Header hinzu              │
│  ┌──────────┬──────────────────────────────────────────────┐   │
│  │TCP-Header│              HTTP-Request                     │   │
│  │(20 Bytes)│                                               │   │
│  └──────────┴──────────────────────────────────────────────┘   │
│         │                                                       │
│         ▼  Internetschicht fügt IP-Header hinzu                │
│  ┌──────────┬──────────┬───────────────────────────────────┐   │
│  │IP-Header │TCP-Header│         HTTP-Request              │   │
│  │(20 Bytes)│          │                                   │   │
│  └──────────┴──────────┴───────────────────────────────────┘   │
│         │                                                       │
│         ▼  Netzzugangsschicht fügt Ethernet-Header/Trailer     │
│  ┌──────────┬──────────┬──────────┬───────────────────┬─────┐  │
│  │Eth-Header│IP-Header │TCP-Header│   HTTP-Request    │ FCS │  │
│  │(14 Bytes)│          │          │                   │(4 B)│  │
│  └──────────┴──────────┴──────────┴───────────────────┴─────┘  │
│         │                                                       │
│         ▼  Bits auf das Medium                                 │
│  ═══════════════════════════════════════════════════════════   │
│  0110100101010101010101010101010101010101010101010101010...    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Schritt 1: Anwendungsschicht (Application Layer)

**Aufgabe:** Erzeugt die Nutzdaten für die Kommunikation

```
┌────────────────────────────────────────────────────────────────┐
│                    ANWENDUNGSSCHICHT                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Browser erzeugt HTTP-Request:                                 │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ GET /index.html HTTP/1.1                                 │ │
│  │ Host: 10.0.0.5                                           │ │
│  │ User-Agent: Mozilla/5.0                                  │ │
│  │ Accept: text/html                                        │ │
│  │ Accept-Language: de-DE                                   │ │
│  │ Connection: keep-alive                                   │ │
│  │                                                          │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  Beitrag der Schicht:                                          │
│  ✓ Anwendungsprotokolle (HTTP, DNS, SMTP, FTP, ...)           │
│  ✓ Datenformat und -kodierung                                 │
│  ✓ Benutzerinteraktion                                        │
│                                                                │
│  Übergabe an: Transportschicht                                │
│  PDU-Bezeichnung: Daten / Nachricht (Message)                 │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Schritt 2: Transportschicht (Transport Layer)

**Aufgabe:** Ende-zu-Ende-Verbindung, Segmentierung, Portzuordnung

```
┌────────────────────────────────────────────────────────────────┐
│                    TRANSPORTSCHICHT                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  TCP-Header wird hinzugefügt:                                  │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │                    TCP-HEADER (20 Bytes)               │   │
│  ├────────────────────────────────────────────────────────┤   │
│  │ Source Port:        52345  (ephemeral, vom OS gewählt) │   │
│  │ Destination Port:   80     (HTTP Well-Known Port)      │   │
│  │ Sequence Number:    1000   (initiale Sequenznummer)    │   │
│  │ Acknowledgment:     0      (noch keine ACKs)           │   │
│  │ Flags:              SYN    (Verbindungsaufbau)*        │   │
│  │ Window Size:        65535  (Empfangspuffer)            │   │
│  │ Checksum:           0x3A7F (berechnet)                 │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  * Hinweis: Vor dem HTTP-Request findet der 3-Way-Handshake   │
│    statt (SYN → SYN-ACK → ACK), hier vereinfacht dargestellt. │
│                                                                │
│  Resultat:                                                     │
│  ┌──────────┬──────────────────────────────────────────────┐  │
│  │TCP-Header│              HTTP-Request                    │  │
│  │  20 B    │                 ~200 B                       │  │
│  └──────────┴──────────────────────────────────────────────┘  │
│                                                                │
│  Beitrag der Schicht:                                          │
│  ✓ Multiplexing durch Portnummern                             │
│  ✓ Verbindungsaufbau (TCP) oder verbindungslos (UDP)          │
│  ✓ Zuverlässigkeit (Sequenznummern, ACKs bei TCP)             │
│  ✓ Flusskontrolle (Sliding Window bei TCP)                    │
│                                                                │
│  Übergabe an: Internetschicht                                 │
│  PDU-Bezeichnung: Segment (TCP) / Datagramm (UDP)             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Schritt 3: Internetschicht (Internet Layer)

**Aufgabe:** Logische Adressierung, Routing, Fragmentierung

```
┌────────────────────────────────────────────────────────────────┐
│                    INTERNETSCHICHT                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  IP-Header wird hinzugefügt:                                   │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │                    IP-HEADER (20 Bytes)                │   │
│  ├────────────────────────────────────────────────────────┤   │
│  │ Version:            4       (IPv4)                     │   │
│  │ Header Length:      5       (20 Bytes, keine Options)  │   │
│  │ Total Length:       240     (20 IP + 20 TCP + 200 Data)│   │
│  │ Identification:     0x1A2B  (für Fragmentierung)       │   │
│  │ Flags:              DF      (Don't Fragment)           │   │
│  │ TTL:                64      (max. 64 Hops)             │   │
│  │ Protocol:           6       (TCP)                      │   │
│  │ Header Checksum:    0x8F21  (berechnet)                │   │
│  │                                                        │   │
│  │ Source IP:          192.168.1.10   (Client)           │   │
│  │ Destination IP:     10.0.0.5       (Server)           │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Routing-Entscheidung:                                         │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Ziel 10.0.0.5 ist NICHT im lokalen Netz 192.168.1.0/24│   │
│  │ → Paket muss an Default Gateway 192.168.1.1 gesendet  │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Resultat:                                                     │
│  ┌──────────┬──────────┬───────────────────────────────────┐  │
│  │IP-Header │TCP-Header│         HTTP-Request              │  │
│  │  20 B    │  20 B    │            ~200 B                 │  │
│  └──────────┴──────────┴───────────────────────────────────┘  │
│                                                                │
│  Beitrag der Schicht:                                          │
│  ✓ Logische Adressierung (IP-Adressen)                        │
│  ✓ Routing-Entscheidung (lokal oder Gateway)                  │
│  ✓ Fragmentierung bei Bedarf                                  │
│  ✓ TTL zur Schleifenvermeidung                                │
│                                                                │
│  Übergabe an: Netzzugangsschicht                              │
│  PDU-Bezeichnung: Paket (Packet) / IP-Datagramm               │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Schritt 4: Netzzugangsschicht (Network Access Layer)

**Aufgabe:** Physische Adressierung, Medienzugriff, Bitübertragung

```
┌────────────────────────────────────────────────────────────────┐
│                   NETZZUGANGSSCHICHT                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ARP-Auflösung (falls nötig):                                  │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Client muss MAC-Adresse des Gateways 192.168.1.1      │   │
│  │ ermitteln → ARP Request (Broadcast)                    │   │
│  │ Gateway antwortet: "192.168.1.1 ist BB:BB:BB:BB:BB:BB"│   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Ethernet-Header wird hinzugefügt:                             │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │              ETHERNET-HEADER (14 Bytes)                │   │
│  ├────────────────────────────────────────────────────────┤   │
│  │ Destination MAC:   BB:BB:BB:BB:BB:BB  (Router LAN1)   │   │
│  │ Source MAC:        AA:AA:AA:AA:AA:AA  (Client)        │   │
│  │ EtherType:         0x0800             (IPv4)          │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Ethernet-Trailer (FCS) wird angehängt:                        │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │              FRAME CHECK SEQUENCE (4 Bytes)            │   │
│  ├────────────────────────────────────────────────────────┤   │
│  │ CRC-32:            0xA1B2C3D4  (Prüfsumme des Frames) │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Resultat – Kompletter Ethernet-Frame:                         │
│  ┌──────┬──────┬──────┬─────────────────────────┬──────┐      │
│  │ Dst  │ Src  │ Type │      IP-Paket           │ FCS  │      │
│  │ MAC  │ MAC  │      │ (IP+TCP+HTTP)           │      │      │
│  │ 6 B  │ 6 B  │ 2 B  │       240 B             │ 4 B  │      │
│  └──────┴──────┴──────┴─────────────────────────┴──────┘      │
│                                                                │
│  Gesamtgröße: 14 + 240 + 4 = 258 Bytes                        │
│                                                                │
│  Beitrag der Schicht:                                          │
│  ✓ Physische Adressierung (MAC-Adressen)                      │
│  ✓ ARP für MAC-Auflösung                                      │
│  ✓ Medienzugriffssteuerung (CSMA/CD)                          │
│  ✓ Fehlererkennung (CRC/FCS)                                  │
│  ✓ Bitübertragung auf das Medium                              │
│                                                                │
│  PDU-Bezeichnung: Frame (Rahmen)                              │
│                                                                │
│  Übertragung auf das Medium:                                   │
│  ════════════════════════════════════════════════════════     │
│  Elektrische Signale / Lichtimpulse / Funkwellen              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Phase 2: Router – Weiterleitung

Der Router empfängt den Frame und verarbeitet ihn nur bis Layer 3:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ROUTER – VERARBEITUNG                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EMPFANG auf LAN 1 (192.168.1.0/24):                           │
│                                                                 │
│  ┌──────┬──────┬──────┬─────────────────────────┬──────┐       │
│  │BB:BB │AA:AA │0x0800│      IP-Paket           │ FCS  │       │
│  └──────┴──────┴──────┴─────────────────────────┴──────┘       │
│                                                                 │
│  Schritt 1: Netzzugangsschicht (Layer 2)                       │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ ✓ FCS prüfen → OK                                      │    │
│  │ ✓ Destination MAC = eigene MAC (BB:BB:BB:BB:BB:BB)?   │    │
│  │   → JA, Frame ist für mich                             │    │
│  │ ✓ Ethernet-Header und FCS entfernen                    │    │
│  │ ✓ EtherType 0x0800 → an IPv4-Verarbeitung übergeben   │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                 │
│  Schritt 2: Internetschicht (Layer 3)                          │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ ✓ IP-Header analysieren                                │    │
│  │   Source IP:      192.168.1.10                         │    │
│  │   Destination IP: 10.0.0.5                             │    │
│  │                                                        │    │
│  │ ✓ Bin ich das Ziel (10.0.0.5)?                        │    │
│  │   → NEIN, ich muss weiterleiten (routen)              │    │
│  │                                                        │    │
│  │ ✓ TTL dekrementieren: 64 → 63                         │    │
│  │   (Bei TTL=0 → Paket verwerfen, ICMP Time Exceeded)   │    │
│  │                                                        │    │
│  │ ✓ Header Checksum neu berechnen (TTL hat sich geändert)│    │
│  │                                                        │    │
│  │ ✓ Routing-Tabelle konsultieren:                        │    │
│  │   ┌────────────────────────────────────────────────┐  │    │
│  │   │ Ziel         Gateway      Interface            │  │    │
│  │   │ 10.0.0.0/24  directly     eth1 (LAN 2)        │  │    │
│  │   │ 192.168.1.0  directly     eth0 (LAN 1)        │  │    │
│  │   │ 0.0.0.0/0    ISP-Router   eth2                │  │    │
│  │   └────────────────────────────────────────────────┘  │    │
│  │                                                        │    │
│  │ ✓ Ziel 10.0.0.5 → Match mit 10.0.0.0/24              │    │
│  │   → Direkt erreichbar über eth1 (LAN 2)               │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                 │
│  Schritt 3: Neuer Frame für LAN 2                              │
│  ┌────────────────────────────────────────────────────────┐    │
│  │ ✓ ARP für 10.0.0.5 (falls nicht im Cache)             │    │
│  │   → Server MAC: CC:CC:CC:CC:CC:CC                     │    │
│  │                                                        │    │
│  │ ✓ Neuen Ethernet-Header erstellen:                    │    │
│  │   Destination MAC: CC:CC:CC:CC:CC:CC (Server)         │    │
│  │   Source MAC:      DD:DD:DD:DD:DD:DD (Router eth1)    │    │
│  │   EtherType:       0x0800                             │    │
│  │                                                        │    │
│  │ ✓ Neue FCS berechnen                                  │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                 │
│  VERSAND auf LAN 2 (10.0.0.0/24):                              │
│                                                                 │
│  ┌──────┬──────┬──────┬─────────────────────────┬──────┐       │
│  │CC:CC │DD:DD │0x0800│   IP-Paket (TTL=63)     │ FCS' │       │
│  └──────┴──────┴──────┴─────────────────────────┴──────┘       │
│                                                                 │
│  WICHTIG: IP-Adressen bleiben unverändert!                     │
│           Nur MAC-Adressen und TTL ändern sich                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Router: Nur Layer 1-3

```
┌────────────────────────────────────────────────────────────────┐
│             ROUTER – SCHICHTENVERARBEITUNG                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│        Anwendung      │ ░░░░░░░░░░░░░░░░░░░░░ │  Nicht        │
│        ───────────────┤ ░░░░░░░░░░░░░░░░░░░░░ │  verarbeitet  │
│        Transport      │ ░░░░░░░░░░░░░░░░░░░░░ │               │
│        ───────────────┼───────────────────────┼───────────────│
│        Internet       │ ✓ Routing-Entscheidung│  Layer 3      │
│        ───────────────┼───────────────────────┼───────────────│
│        Netzzugang     │ ✓ MAC-Adressen ändern │  Layer 1-2    │
│                       │ ✓ Frame neu aufbauen  │               │
│                                                                │
│  Router "sehen" nicht in TCP-Header oder HTTP-Daten!          │
│  (Ausnahme: Deep Packet Inspection bei Firewalls)             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Phase 3: Server – Daten empfangen

### Übersicht der Entkapselung

```
┌─────────────────────────────────────────────────────────────────┐
│            ENTKAPSELUNG (DECAPSULATION) – SERVER                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Empfangener Frame auf dem Medium:                             │
│  ═══════════════════════════════════════════════════════════   │
│  0110100101010101010101010101010101010101010101010101010...    │
│         │                                                       │
│         ▼  Netzzugangsschicht entfernt Ethernet-Header/Trailer │
│  ┌──────────┬──────────┬──────────┬───────────────────┬─────┐  │
│  │Eth-Header│IP-Header │TCP-Header│   HTTP-Request    │ FCS │  │
│  └──────────┴──────────┴──────────┴───────────────────┴─────┘  │
│         │              ▲                              ▲         │
│         │              │                              │         │
│         └──────────────┴───────────── entfernt ───────┘        │
│         │                                                       │
│         ▼  Internetschicht entfernt IP-Header                  │
│  ┌──────────┬──────────┬───────────────────────────────────┐   │
│  │IP-Header │TCP-Header│         HTTP-Request              │   │
│  └──────────┴──────────┴───────────────────────────────────┘   │
│         │   ▲                                                   │
│         │   └──────────────────────── entfernt                 │
│         │                                                       │
│         ▼  Transportschicht entfernt TCP-Header                │
│  ┌──────────┬──────────────────────────────────────────────┐   │
│  │TCP-Header│              HTTP-Request                     │   │
│  └──────────┴──────────────────────────────────────────────┘   │
│         │   ▲                                                   │
│         │   └──────────────────────── entfernt                 │
│         │                                                       │
│         ▼  Anwendungsschicht erhält reine Nutzdaten           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HTTP-Request                          │   │
│  │         "GET /index.html HTTP/1.1..."                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Detaillierter Empfangsprozess

```
┌────────────────────────────────────────────────────────────────┐
│              SERVER – ENTKAPSELUNG IM DETAIL                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  SCHRITT 1: Netzzugangsschicht                                │
│  ─────────────────────────────────────────────────────────────│
│  ┌────────────────────────────────────────────────────────┐   │
│  │ ✓ Frame vom Medium empfangen (elektrische Signale)     │   │
│  │ ✓ Preamble/SFD erkennen (Synchronisation)              │   │
│  │ ✓ Destination MAC prüfen:                              │   │
│  │   CC:CC:CC:CC:CC:CC = eigene MAC? → JA                │   │
│  │ ✓ FCS/CRC prüfen → Keine Übertragungsfehler           │   │
│  │ ✓ EtherType 0x0800 → IPv4, an IP-Stack übergeben      │   │
│  │ ✓ Ethernet-Header und FCS entfernen                    │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Verbleibend: IP-Paket (240 Bytes)                            │
│                                                                │
│  SCHRITT 2: Internetschicht                                   │
│  ─────────────────────────────────────────────────────────────│
│  ┌────────────────────────────────────────────────────────┐   │
│  │ ✓ IP-Version prüfen: 4 → IPv4                          │   │
│  │ ✓ Header Checksum validieren → OK                      │   │
│  │ ✓ Destination IP prüfen:                               │   │
│  │   10.0.0.5 = eigene IP? → JA, Paket ist für mich      │   │
│  │ ✓ Protocol-Feld auslesen: 6 → TCP                      │   │
│  │ ✓ IP-Header entfernen, an TCP-Stack übergeben          │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Verbleibend: TCP-Segment (220 Bytes)                         │
│                                                                │
│  SCHRITT 3: Transportschicht                                  │
│  ─────────────────────────────────────────────────────────────│
│  ┌────────────────────────────────────────────────────────┐   │
│  │ ✓ TCP Checksum validieren → OK                         │   │
│  │ ✓ Destination Port: 80 → HTTP-Dienst                   │   │
│  │ ✓ Socket-Zuordnung:                                    │   │
│  │   (TCP, 192.168.1.10, 52345, 10.0.0.5, 80)            │   │
│  │ ✓ Sequenznummer prüfen (Reihenfolge)                   │   │
│  │ ✓ ACK senden (Bestätigung)                             │   │
│  │ ✓ TCP-Header entfernen                                 │   │
│  │ ✓ Daten an Port 80 (Webserver-Prozess) übergeben      │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  Verbleibend: HTTP-Request (~200 Bytes)                       │
│                                                                │
│  SCHRITT 4: Anwendungsschicht                                 │
│  ─────────────────────────────────────────────────────────────│
│  ┌────────────────────────────────────────────────────────┐   │
│  │ ✓ Webserver (z.B. Apache, nginx) empfängt Request      │   │
│  │ ✓ HTTP-Request parsen:                                 │   │
│  │   - Methode: GET                                       │   │
│  │   - Pfad: /index.html                                  │   │
│  │   - Headers: Host, User-Agent, Accept, ...             │   │
│  │ ✓ Datei /var/www/html/index.html laden                │   │
│  │ ✓ HTTP-Response generieren                             │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Gesamtübersicht: Der komplette Paketfluss

```
┌─────────────────────────────────────────────────────────────────┐
│                    KOMPLETTER PAKETFLUSS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLIENT              ROUTER                SERVER               │
│  192.168.1.10        192.168.1.1           10.0.0.5            │
│                      10.0.0.1                                   │
│                                                                 │
│  ┌───────────┐                                                 │
│  │Application│ HTTP-Request                                    │
│  ├───────────┤ erstellen                                       │
│  │ Transport │ +TCP-Header                                     │
│  │           │ (Port 52345→80)                                 │
│  ├───────────┤ +IP-Header                                      │
│  │ Internet  │ (192.168.1.10                                   │
│  │           │  →10.0.0.5)                                     │
│  ├───────────┤ +Eth-Header                                     │
│  │ Net Access│ (AA:AA→BB:BB)         ┌───────────┐            │
│  └─────┬─────┘                       │           │            │
│        │                             │ Internet  │ Routing    │
│        │  ══════════════════════════►├───────────┤ TTL--      │
│        │      Ethernet LAN 1         │ Net Access│ MAC ändern │
│        │                             └─────┬─────┘            │
│        │                                   │                   │
│        │                                   │  ════════════════►│
│        │                                   │   Ethernet LAN 2  │
│        │                                   │                   │
│        │                                   │         ┌─────────┴─┐
│        │                                   │         │ Net Access│
│        │                                   │         ├───────────┤
│        │                                   │         │ Internet  │
│        │                                   │         ├───────────┤
│        │                                   │         │ Transport │
│        │                                   │         ├───────────┤
│        │                                   │         │Application│
│        │                                   │         └───────────┘
│        │                                   │         HTTP-Request
│        │                                   │         verarbeiten
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## PDU-Bezeichnungen pro Schicht

```
┌────────────────────────────────────────────────────────────────┐
│                PDU (Protocol Data Unit) pro Schicht            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  DoD-Schicht          PDU-Name            Enthält              │
│  ──────────────────────────────────────────────────────────── │
│                                                                │
│  Anwendung            Daten / Message     Nutzdaten            │
│                       (Nachricht)                              │
│                                                                │
│  Transport            Segment (TCP)       TCP-Header + Daten   │
│                       Datagramm (UDP)     UDP-Header + Daten   │
│                                                                │
│  Internet             Paket / Packet      IP-Header + Segment  │
│                       (IP-Datagramm)                           │
│                                                                │
│  Netzzugang           Frame / Rahmen      Eth-Header + Paket   │
│                                           + FCS                │
│                                                                │
│  (Physikalisch)       Bits                0 und 1 auf Medium   │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │        Daten                                            │  │
│  ├──────┬──────────────────────────────────────────────────┤  │
│  │ TCP  │                    Segment                       │  │
│  ├──────┼──────┬───────────────────────────────────────────┤  │
│  │  IP  │ TCP  │                  Paket                    │  │
│  ├──────┼──────┼──────┬────────────────────────────┬───────┤  │
│  │ Eth  │  IP  │ TCP  │           Frame            │  FCS  │  │
│  └──────┴──────┴──────┴────────────────────────────┴───────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

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
