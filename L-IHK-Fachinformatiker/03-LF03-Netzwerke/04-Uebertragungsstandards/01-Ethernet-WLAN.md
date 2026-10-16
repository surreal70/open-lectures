---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - ethernet
  - wlan
  - standards
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# Übertragungsstandards: Ethernet und WLAN

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die wichtigsten Ethernet-Standards kennen
> - WLAN-Standards und ihre Geschwindigkeiten unterscheiden können
> - Kabeltypen und ihre Eigenschaften kennen
> - Bandbreite und Durchsatz unterscheiden können

---

## Überblick

Übertragungsstandards definieren, wie Daten physikalisch übertragen werden. Sie bestimmen Geschwindigkeit, Reichweite und Kabeltyp.

## Ethernet-Standards (IEEE 802.3)

### Gängige Standards

| Standard | Name | Geschwindigkeit | Kabel | Max. Länge |
|----------|------|-----------------|-------|------------|
| 10BASE-T | Ethernet | 10 Mbit/s | Cat 3+ | 100 m |
| 100BASE-TX | Fast Ethernet | 100 Mbit/s | Cat 5+ | 100 m |
| 1000BASE-T | Gigabit Ethernet | 1 Gbit/s | Cat 5e+ | 100 m |
| 2.5GBASE-T | 2.5G Ethernet | 2,5 Gbit/s | Cat 5e+ | 100 m |
| 5GBASE-T | 5G Ethernet | 5 Gbit/s | Cat 6+ | 100 m |
| 10GBASE-T | 10G Ethernet | 10 Gbit/s | Cat 6a+ | 100 m |

### Namenskonvention

```
1000  BASE  -T
 │      │    │
 │      │    └── Übertragungsmedium (T=Twisted Pair, F=Fiber)
 │      └─────── Basisband-Übertragung
 └────────────── Geschwindigkeit in Mbit/s
```

## Kabeltypen

### Twisted Pair (Kupfer)

| Kategorie | Max. Frequenz | Typische Verwendung |
|-----------|---------------|---------------------|
| Cat 5 | 100 MHz | Fast Ethernet |
| Cat 5e | 100 MHz | Gigabit Ethernet |
| Cat 6 | 250 MHz | Gigabit, 10G (kurz) |
| Cat 6a | 500 MHz | 10 Gigabit Ethernet |
| Cat 7 | 600 MHz | 10G+ (geschirmt) |
| Cat 8 | 2000 MHz | 25G/40G Datacenter |

### Schirmung

| Kürzel | Bedeutung |
|--------|-----------|
| **UTP** | Unshielded Twisted Pair (ungeschirmt) |
| **STP** | Shielded Twisted Pair (geschirmt) |
| **S/FTP** | Gesamtschirm + Folienschirm pro Paar |
| **S/STP** | Gesamtschirm + Geflechtschirm pro Paar |

### Glasfaser (Fiber)

| Typ | Kern | Reichweite | Verwendung |
|-----|------|------------|------------|
| **Multimode (MM)** | 50/62,5 µm | bis 550 m | Gebäude, Campus |
| **Singlemode (SM)** | 9 µm | bis 40+ km | WAN, Backbone |

## WLAN-Standards (IEEE 802.11)

| Standard | Name | Frequenz | Max. Geschwindigkeit | Jahr |
|----------|------|----------|---------------------|------|
| 802.11b | — | 2,4 GHz | 11 Mbit/s | 1999 |
| 802.11a | — | 5 GHz | 54 Mbit/s | 1999 |
| 802.11g | — | 2,4 GHz | 54 Mbit/s | 2003 |
| 802.11n | Wi-Fi 4 | 2,4/5 GHz | 600 Mbit/s | 2009 |
| 802.11ac | Wi-Fi 5 | 5 GHz | 6,9 Gbit/s | 2013 |
| 802.11ax | Wi-Fi 6 | 2,4/5/6 GHz | 9,6 Gbit/s | 2019 |
| 802.11be | Wi-Fi 7 | 2,4/5/6 GHz | 46 Gbit/s | 2024 |

### Frequenzbänder

| Band | Vorteile | Nachteile |
|------|----------|-----------|
| **2,4 GHz** | Bessere Reichweite, durchdringt Wände | Überfüllt, weniger Kanäle |
| **5 GHz** | Mehr Kanäle, weniger Störungen | Geringere Reichweite |
| **6 GHz** | Viele Kanäle, hohe Bandbreite | Nur Wi-Fi 6E/7, kurze Reichweite |

## Bandbreite vs. Durchsatz

| Begriff | Definition |
|---------|------------|
| **Bandbreite** | Maximale theoretische Übertragungsrate |
| **Durchsatz** | Tatsächlich erreichbare Datenrate |
| **Latenz** | Verzögerung der Datenübertragung |

> [!note] **Praxiswert**
> Der reale Durchsatz liegt typischerweise bei 50-70% der theoretischen Bandbreite aufgrund von Protokoll-Overhead, Kollisionen und Störungen.

## Zusammenhänge

- → [[02-Grundbegriffe|Grundbegriffe (OSI Layer 1)]]
- → [[06-MAC-Adressen|MAC-Adressen (Layer 2)]]
- → [[03-Architekturen|Netzwerkarchitekturen]]

> [!warning] **Prüfungsrelevant**
> - Ethernet-Standards und Geschwindigkeiten
> - Kabelkategorien (Cat 5, Cat 6, etc.)
> - WLAN-Standards (Wi-Fi 4/5/6)
> - Unterschied Bandbreite vs. Durchsatz

> [!question] **Typische Prüfungsfragen**
> - Welche Geschwindigkeit erreicht Gigabit Ethernet?
> - Welches Kabel benötigt man für 10 Gigabit Ethernet?
> - Was bedeutet die Bezeichnung "1000BASE-T"?
> - Welchen WLAN-Standard bezeichnet Wi-Fi 6?

## Quellen

- proTirone: LF03:04 Übertragungsstandards (Karsten Reincke, CC-BY-4.0)
- IEEE 802.3 Standard
- IEEE 802.11 Standard

> [!tip] **Weiterführende Links**
> - [Wikipedia: Ethernet](https://de.wikipedia.org/wiki/Ethernet)
> - [Wikipedia: WLAN](https://de.wikipedia.org/wiki/Wireless_Local_Area_Network)
