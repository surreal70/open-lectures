---
author: Andreas Hümmer
title: IEEE 802 Standards
tags:
  - vorlesung
  - rn
  - standards
  - ieee
  - ethernet
  - wlan
  - wifi
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# IEEE 802 Standards

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Struktur der IEEE 802 Arbeitsgruppen erklären
> - Die wichtigsten 802.x Standards und ihre Anwendungsgebiete zuordnen
> - Die Ethernet-Namenskonvention interpretieren (z.B. 1000BASE-T)
> - Die Evolution von Ethernet von 10 Mbit/s bis 400 Gbit/s nachvollziehen
> - WiFi-Generationen und ihre Eigenschaften unterscheiden
> - Den Zusammenhang zwischen 802.11-Varianten und WiFi-Marketing-Namen erklären

## IEEE 802 – Die Netzwerk-Arbeitsgruppe

Die [[07-Anhang/IT-Related-Organisations/IEEE|IEEE]] 802 Arbeitsgruppe ist verantwortlich für Standards im Bereich lokaler und metropolitaner Netzwerke (LAN/MAN).

> [!info] Warum „802"?
> Die Nummer „802" stammt aus dem Jahr **1980**, Monat **Februar** – dem Gründungsdatum der Arbeitsgruppe. Seitdem ist 802.x das Synonym für LAN-Standards.

### Übersicht der IEEE 802 Arbeitsgruppen

```
┌────────────────────────────────────────────────────────────────┐
│                     IEEE 802 ARBEITSGRUPPEN                    │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   AKTIV UND RELEVANT                                          │
│   ──────────────────                                          │
│   802.1   Higher Layer LAN Protocols (Bridging, VLANs)        │
│   802.3   CSMA/CD → Ethernet                                  │
│   802.11  Wireless LAN (WLAN / WiFi)                          │
│   802.15  Wireless Personal Area Network (Bluetooth, ZigBee)  │
│   802.16  Broadband Wireless Access (WiMAX)                   │
│   802.18  Radio Regulatory TAG                                │
│   802.19  Wireless Coexistence                                │
│   802.22  Wireless Regional Area Networks                     │
│   802.23  Emergency Services                                  │
│                                                                │
│   HISTORISCH / INAKTIV                                        │
│   ────────────────────                                        │
│   802.2   Logical Link Control (LLC)                          │
│   802.4   Token Bus                                           │
│   802.5   Token Ring                                          │
│   802.6   MAN (DQDB)                                          │
│   802.7   Broadband TAG                                       │
│   802.8   Fiber Optic TAG                                     │
│   802.9   Integrated Services                                 │
│   802.10  Security (aufgelöst)                                │
│   802.12  Demand Priority (100VG-AnyLAN)                      │
│   802.14  Cable-TV Based Broadband                            │
│   802.17  Resilient Packet Ring                               │
│   802.20  Mobile Broadband Wireless Access                    │
│   802.21  Media Independent Handover                          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

> [!merke] Die „Big Three"
> Die drei praxisrelevantesten 802-Arbeitsgruppen sind:
> - **802.1** – Bridging, VLANs, Spanning Tree
> - **802.3** – Ethernet (kabelgebunden)
> - **802.11** – WLAN/WiFi (drahtlos)

## IEEE 802.3 – Ethernet

→ Detailseiten: [[07-Anhang/IEEE-802-Standards/IEEE 802.3|IEEE 802.3]]

Die 802.3 Arbeitsgruppe definiert alle kabelgebundenen Ethernet-Standards. Ethernet ist heute die dominierende Technologie für lokale Netzwerke.

### Namenskonvention

Die Ethernet-Bezeichnungen folgen einem Schema:

```
┌─────────────────────────────────────────────────────────────────┐
│                  ETHERNET-NAMENSKONVENTION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│         [Geschwindigkeit][Signalart][Medium/Segment]           │
│                                                                 │
│   Beispiel: 1000BASE-T                                         │
│             ────┬──── ─┬── ─┬─                                 │
│                 │      │    │                                   │
│                 │      │    └── T = Twisted Pair (Kupfer)      │
│                 │      │                                        │
│                 │      └────── BASE = Baseband                 │
│                 │              (Gegenteil: BROAD = Broadband)  │
│                 │                                               │
│                 └────────────── 1000 = 1000 Mbit/s = 1 Gbit/s  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│   GESCHWINDIGKEIT                                               │
│   ───────────────                                               │
│   10, 100, 1000       → Mbit/s                                 │
│   10G, 25G, 40G, 100G → Gbit/s (G = Giga)                      │
│   200G, 400G, 800G    → Gbit/s                                 │
│                                                                 │
│   MEDIUM-SUFFIXE                                                │
│   ──────────────                                                │
│   -T    Twisted Pair (Kupfer, Cat5/6/7/8)                      │
│   -TX   Twisted Pair, 2 Paare                                  │
│   -CX   Twinax Kupferkabel (kurze Distanzen, Rechenzentrum)    │
│   -SR   Short Range, Multimode-Glasfaser                       │
│   -LR   Long Range, Singlemode-Glasfaser                       │
│   -ER   Extended Range, Singlemode-Glasfaser                   │
│   -ZR   „Zero" Range (eigentlich sehr lang, ~80km)             │
│   -SX   Short Wavelength, Multimode (850nm)                    │
│   -LX   Long Wavelength, Singlemode (1310nm)                   │
│                                                                 │
│   Bei parallelen Verbindungen: SR4 = 4× Short Range           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Ethernet-Evolution

#### Historische Entwicklung

| Standard | Jahr | Geschwindigkeit | Medium | Max. Länge | Status |
|----------|------|-----------------|--------|------------|--------|
| 10BASE5 | 1983 | 10 Mbit/s | Thick Coax (Yellow Cable) | 500 m | obsolet |
| 10BASE2 | 1985 | 10 Mbit/s | Thin Coax (Cheapernet) | 185 m | obsolet |
| 10BASE-T | 1990 | 10 Mbit/s | Cat3 UTP | 100 m | selten |
| 100BASE-TX | 1995 | 100 Mbit/s | Cat5 UTP | 100 m | verbreitet |
| 100BASE-FX | 1995 | 100 Mbit/s | MM Fiber | 2 km | selten |

> [!info] Koaxial-Ethernet
> Die frühen Ethernet-Standards (10BASE5, 10BASE2) verwendeten Koaxialkabel in einer Bus-Topologie. Mit 10BASE-T kam der Wechsel zu Twisted-Pair-Kabeln und Stern-Topologie, was die Installation und Fehlersuche erheblich vereinfachte.

#### Gigabit Ethernet

| Standard | Jahr | Geschwindigkeit | Medium | Max. Länge |
|----------|------|-----------------|--------|------------|
| 1000BASE-SX | 1998 | 1 Gbit/s | MM Fiber (850nm) | 550 m |
| 1000BASE-LX | 1998 | 1 Gbit/s | SM Fiber (1310nm) | 5 km |
| 1000BASE-T | 1999 | 1 Gbit/s | Cat5e UTP | 100 m |
| 1000BASE-CX | 1998 | 1 Gbit/s | Twinax Kupfer | 25 m |

#### 10 Gigabit Ethernet

| Standard | Jahr | Geschwindigkeit | Medium | Max. Länge |
|----------|------|-----------------|--------|------------|
| 10GBASE-SR | 2002 | 10 Gbit/s | MM Fiber | 300 m |
| 10GBASE-LR | 2002 | 10 Gbit/s | SM Fiber | 10 km |
| 10GBASE-ER | 2002 | 10 Gbit/s | SM Fiber | 40 km |
| 10GBASE-T | 2006 | 10 Gbit/s | Cat6a UTP | 100 m |
| 10GBASE-CX4 | 2002 | 10 Gbit/s | Twinax (4×) | 15 m |

#### 25/40/100 Gigabit Ethernet

| Standard | Jahr | Geschwindigkeit | Medium | Max. Länge |
|----------|------|-----------------|--------|------------|
| 25GBASE-T | 2016 | 25 Gbit/s | Cat8 | 30 m |
| 40GBASE-T | 2016 | 40 Gbit/s | Cat8 | 30 m |
| 40GBASE-SR4 | 2010 | 40 Gbit/s | MM Fiber (4×) | 100 m |
| 40GBASE-LR4 | 2010 | 40 Gbit/s | SM Fiber | 10 km |
| 100GBASE-SR4 | 2010 | 100 Gbit/s | MM Fiber (4×) | 100 m |
| 100GBASE-LR4 | 2010 | 100 Gbit/s | SM Fiber | 10 km |
| 100GBASE-CR4 | 2014 | 100 Gbit/s | Twinax (4×) | 5 m |

#### 200/400/800 Gigabit Ethernet

| Standard | Jahr | Geschwindigkeit | Medium | Max. Länge |
|----------|------|-----------------|--------|------------|
| 200GBASE-SR4 | 2017 | 200 Gbit/s | MM Fiber (4×) | 100 m |
| 200GBASE-LR4 | 2017 | 200 Gbit/s | SM Fiber | 10 km |
| 400GBASE-SR8 | 2017 | 400 Gbit/s | MM Fiber (8×) | 100 m |
| 400GBASE-LR8 | 2017 | 400 Gbit/s | SM Fiber | 10 km |
| 400GBASE-DR4 | 2017 | 400 Gbit/s | SM Fiber (4×) | 500 m |
| 800GBASE-* | 2024 | 800 Gbit/s | verschiedene | variiert |

> [!merke] Abkürzungen
> - **UTP**: Unshielded Twisted Pair
> - **MM**: Multimode (Glasfaser, mehrere Lichtpfade)
> - **SM**: Singlemode (Glasfaser, ein Lichtpfad)
> - **Cat**: Kategorie (Kabelqualität nach TIA/EIA-568)

### Kabelkategorien für Twisted Pair

| Kategorie | Max. Frequenz | Typische Anwendung |
|-----------|---------------|-------------------|
| Cat3 | 16 MHz | 10BASE-T, Telefon |
| Cat5 | 100 MHz | 100BASE-TX |
| Cat5e | 100 MHz | 1000BASE-T |
| Cat6 | 250 MHz | 1000BASE-T, 10GBASE-T (55m) |
| Cat6a | 500 MHz | 10GBASE-T (100m) |
| Cat7 | 600 MHz | 10GBASE-T |
| Cat8 | 2000 MHz | 25/40GBASE-T |

## IEEE 802.11 – WLAN/WiFi

→ Detailseiten: [[07-Anhang/IEEE-802-Standards/IEEE 802.11|IEEE 802.11]], [[07-Anhang/IEEE-802-Standards/IEEE 802.11ax|IEEE 802.11ax]]

Die 802.11 Arbeitsgruppe definiert die drahtlosen Netzwerkstandards, im Marketing als „WiFi" bezeichnet.

### WiFi vs. WLAN

> [!merke] Begriffe
> - **WLAN** = Wireless Local Area Network (technischer Begriff)
> - **WiFi** = Marketingbegriff der WiFi Alliance (Zertifizierungsprogramm)
> 
> Nicht jedes WLAN ist WiFi-zertifiziert, aber praktisch alle Consumer-Geräte sind es.

### WiFi-Generationen

| Generation | Standard | Jahr | Max. Geschwindigkeit | Frequenz | MIMO |
|------------|----------|------|---------------------|----------|------|
| – | [[07-Anhang/IEEE-802-Standards/IEEE 802.11\|802.11]] | 1997 | 2 Mbit/s | 2,4 GHz | – |
| WiFi 1 | 802.11b | 1999 | 11 Mbit/s | 2,4 GHz | – |
| WiFi 2 | [[07-Anhang/IEEE-802-Standards/IEEE 802.11a\|802.11a]] | 1999 | 54 Mbit/s | 5 GHz | – |
| WiFi 3 | [[07-Anhang/IEEE-802-Standards/IEEE 802.11g\|802.11g]] | 2003 | 54 Mbit/s | 2,4 GHz | – |
| WiFi 4 | [[07-Anhang/IEEE-802-Standards/IEEE 802.11n\|802.11n]] | 2009 | 600 Mbit/s | 2,4/5 GHz | 4×4 |
| WiFi 5 | [[07-Anhang/IEEE-802-Standards/IEEE 802.11ac\|802.11ac]] | 2014 | 6,9 Gbit/s | 5 GHz | 8×8, MU-MIMO |
| WiFi 6 | [[07-Anhang/IEEE-802-Standards/IEEE 802.11ax\|802.11ax]] | 2021 | 9,6 Gbit/s | 2,4/5 GHz | MU-MIMO, OFDMA |
| WiFi 6E | 802.11ax | 2021 | 9,6 Gbit/s | 6 GHz | MU-MIMO, OFDMA |
| WiFi 7 | 802.11be | 2024 | 46 Gbit/s | 2,4/5/6 GHz | 16×16, MLO |
| WiFi 8 | 802.11bn | ~2028 | >100 Gbit/s | TBD | TBD |

> [!info] Rückwirkende Benennung
> Die WiFi Alliance führte die Generationsnummern (WiFi 4, 5, 6...) erst 2018 ein, um die Kommunikation mit Endanwendern zu vereinfachen. 802.11a/b/g wurden rückwirkend als WiFi 1-3 bezeichnet.

### Frequenzbänder

```
┌────────────────────────────────────────────────────────────────┐
│                    WLAN FREQUENZBÄNDER                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   2,4 GHz Band (2400-2483,5 MHz)                              │
│   ├── Kanäle 1-13 (Europa), 1-11 (USA), 1-14 (Japan)          │
│   ├── Kanalbreite: 20 MHz (802.11b/g), 40 MHz (802.11n)       │
│   ├── Überlappungsfrei: nur Kanäle 1, 6, 11                   │
│   ├── Pro: Bessere Reichweite, Durchdringung                  │
│   └── Contra: Überfüllt, Interferenzen (Mikrowelle, BT)       │
│                                                                │
│   5 GHz Band (5150-5875 MHz)                                  │
│   ├── Mehr Kanäle (19 nicht-überlappend in Europa)            │
│   ├── Kanalbreite: 20/40/80/160 MHz                           │
│   ├── Weniger Interferenzen                                   │
│   ├── Teilweise DFS erforderlich (Radar-Erkennung)            │
│   └── Contra: Kürzere Reichweite, schlechtere Durchdringung   │
│                                                                │
│   6 GHz Band (5925-7125 MHz) – WiFi 6E/7                      │
│   ├── 1200 MHz zusätzliches Spektrum                          │
│   ├── Bis zu 7 × 160 MHz oder 3 × 320 MHz Kanäle             │
│   ├── Noch weniger Interferenzen (nur WiFi 6E+ Geräte)        │
│   └── Contra: Noch kürzere Reichweite                         │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Wichtige 802.11-Erweiterungen

| Amendment | Beschreibung |
|-----------|--------------|
| 802.11i | Sicherheit (WPA2, AES-CCMP) |
| 802.11e | QoS (Quality of Service, WMM) |
| 802.11r | Fast BSS Transition (schnelles Roaming) |
| 802.11k | Radio Resource Measurement |
| 802.11v | Wireless Network Management |
| 802.11w | Protected Management Frames |
| 802.11s | Mesh Networking |

### Technologien

| Technologie | Einführung | Beschreibung |
|-------------|------------|--------------|
| **MIMO** | 802.11n | Multiple Input/Multiple Output – mehrere Antennen |
| **MU-MIMO** | 802.11ac W2 | Multi-User MIMO – gleichzeitig mehrere Clients |
| **OFDMA** | 802.11ax | Orthogonal Frequency Division Multiple Access |
| **BSS Coloring** | 802.11ax | Unterscheidung überlappender Netze |
| **TWT** | 802.11ax | Target Wake Time – Stromsparen für IoT |
| **MLO** | 802.11be | Multi-Link Operation – mehrere Bänder gleichzeitig |

## IEEE 802.15 – Wireless PAN

→ Detailseite: [[07-Anhang/IEEE-802-Standards/IEEE 802.15|IEEE 802.15]]

Standards für Personal Area Networks (kurze Distanzen, niedriger Stromverbrauch):

| Standard | Technologie | Reichweite | Anwendung |
|----------|-------------|------------|-----------|
| 802.15.1 | Bluetooth | 10-100 m | Kopfhörer, Peripherie |
| 802.15.4 | ZigBee, Thread, Matter | 10-100 m | IoT, Smart Home |
| 802.15.4g | Wi-SUN | 1+ km | Smart Metering |
| 802.15.6 | BAN | 1-2 m | Body Area Networks |

## IEEE 802.1 – Bridging und VLANs

Die 802.1 Arbeitsgruppe definiert höhere Protokolle für geswitchte Netzwerke.

### Wichtige 802.1 Standards

| Standard | Name | Beschreibung | Detailseite |
|----------|------|--------------|-------------|
| [[07-Anhang/IEEE-802-Standards/IEEE 802.1D\|802.1D]] | STP | Spanning Tree Protocol | [[07-Anhang/IEEE-802-Standards/IEEE 802.1D\|→]] |
| [[07-Anhang/IEEE-802-Standards/IEEE 802.1w\|802.1w]] | RSTP | Rapid Spanning Tree Protocol | [[07-Anhang/IEEE-802-Standards/IEEE 802.1w\|→]] |
| [[07-Anhang/IEEE-802-Standards/IEEE 802.1s\|802.1s]] | MSTP | Multiple Spanning Tree Protocol | [[07-Anhang/IEEE-802-Standards/IEEE 802.1s\|→]] |
| [[07-Anhang/IEEE-802-Standards/IEEE 802.1Q\|802.1Q]] | VLANs | Virtual LANs, VLAN Tagging | [[07-Anhang/IEEE-802-Standards/IEEE 802.1Q\|→]] |
| [[07-Anhang/IEEE-802-Standards/IEEE 802.1X\|802.1X]] | Port Auth | Port-basierte Zugangskontrolle | [[07-Anhang/IEEE-802-Standards/IEEE 802.1X\|→]] |
| 802.1AX | LACP | Link Aggregation Control Protocol | – |
| 802.1AB | LLDP | Link Layer Discovery Protocol | – |
| 802.1AS | gPTP | Generalized Precision Time Protocol | – |

### 802.1Q VLAN Tagging

```
┌─────────────────────────────────────────────────────────────────┐
│                    802.1Q VLAN TAG FORMAT                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Ethernet-Frame ohne Tag:                                      │
│   ┌─────────┬─────────┬──────┬─────────────┬─────┐             │
│   │ Dst MAC │ Src MAC │ Type │   Payload   │ FCS │             │
│   │  6 B    │  6 B    │ 2 B  │  46-1500 B  │ 4 B │             │
│   └─────────┴─────────┴──────┴─────────────┴─────┘             │
│                                                                 │
│   Ethernet-Frame mit 802.1Q Tag:                                │
│   ┌─────────┬─────────┬──────────┬──────┬─────────────┬─────┐  │
│   │ Dst MAC │ Src MAC │ 802.1Q   │ Type │   Payload   │ FCS │  │
│   │  6 B    │  6 B    │  4 B     │ 2 B  │  46-1500 B  │ 4 B │  │
│   └─────────┴─────────┴──────────┴──────┴─────────────┴─────┘  │
│                         │                                       │
│                         ▼                                       │
│   ┌─────────────────────────────────────────┐                  │
│   │              802.1Q Tag (4 Bytes)       │                  │
│   ├─────────────┬─────┬───────┬────────────┤                  │
│   │    TPID     │ PCP │  DEI  │    VID     │                  │
│   │   0x8100    │ 3b  │  1b   │   12 bit   │                  │
│   │  (2 Bytes)  │     │       │  (0-4095)  │                  │
│   └─────────────┴─────┴───────┴────────────┘                  │
│                                                                 │
│   TPID = Tag Protocol Identifier                               │
│   PCP  = Priority Code Point (QoS, 0-7)                        │
│   DEI  = Drop Eligible Indicator                               │
│   VID  = VLAN Identifier (4094 nutzbare VLANs)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **IEEE 802** ist die zentrale Arbeitsgruppe für LAN/MAN-Standards
> - **802.3 (Ethernet)** hat sich von 10 Mbit/s (1983) zu 800 Gbit/s (2024) entwickelt
> - **802.11 (WLAN)** ist bei WiFi 7 mit 46 Gbit/s und 6 GHz-Band angekommen
> - **802.1** definiert VLANs (802.1Q) und Spanning Tree (802.1D/w/s)
> - **802.15** deckt Personal Area Networks ab (Bluetooth, ZigBee)
> - Die Ethernet-Namenskonvention (z.B. 1000BASE-T) kodiert Geschwindigkeit und Medium

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die drei wichtigsten 802-Gruppen (802.1, 802.3, 802.11)
> - Können Sie die Ethernet-Namenskonvention erklären
> - Wissen Sie, welche Kabelkategorie für welche Geschwindigkeit nötig ist
> - Kennen Sie die WiFi-Generationen und ihre ungefähren Geschwindigkeiten
> - Verstehen Sie den Zweck von 802.1Q (VLANs) und 802.1X (Authentifizierung)

## Verwandte Themen

- [[01-Uebersicht]] – Standardisierungsgremien
- [[03-RFCs]] – Internet-Standards der IETF
- [[04-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Ethernet im OSI-Modell
- [[07-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] – WiFi-Authentifizierung

## Referenzen im Anhang

### IEEE 802 Standards

- [[07-Anhang/IEEE-802-Standards/00-IEEE-802-Standards-Index|IEEE 802 Standards Index]]
- [[07-Anhang/IEEE-802-Standards/IEEE 802.3|IEEE 802.3 – Ethernet]]
- [[07-Anhang/IEEE-802-Standards/IEEE 802.11|IEEE 802.11 – WLAN]]
- [[07-Anhang/IEEE-802-Standards/IEEE 802.1Q|IEEE 802.1Q – VLANs]]
- [[07-Anhang/IEEE-802-Standards/IEEE 802.1X|IEEE 802.1X – Port Authentication]]

### Organisationen

- [[07-Anhang/IT-Related-Organisations/IEEE|IEEE]]

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- IEEE Standards Association: [standards.ieee.org](https://standards.ieee.org/)
- IEEE 802 LAN/MAN Standards Committee: [ieee802.org](https://www.ieee802.org/)
- WiFi Alliance: [wi-fi.org](https://www.wi-fi.org/)
