---
author: Andreas Hümmer
title: Übertragungsmedien
tags:
  - vorlesung
  - rn
  - layer1
  - kabel
  - glasfaser
  - wlan
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Übertragungsmedien

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die verschiedenen Übertragungsmedien und ihre Eigenschaften benennen
> - Kupferkabel-Kategorien und ihre Anwendungen unterscheiden
> - Glasfaser-Typen (Singlemode, Multimode) erklären
> - Stecker- und Kabeltypen zuordnen
> - Vor- und Nachteile der verschiedenen Medien abwägen

## Übersicht der Übertragungsmedien

```
┌─────────────────────────────────────────────────────────────────┐
│                    ÜBERTRAGUNGSMEDIEN                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   LEITUNGSGEBUNDEN                    DRAHTLOS                  │
│   ────────────────                    ────────                  │
│                                                                 │
│   ┌─────────────────┐                ┌─────────────────┐       │
│   │ Twisted Pair    │                │ WLAN (802.11)   │       │
│   │ (Kupfer)        │                │ 2,4/5/6 GHz     │       │
│   └─────────────────┘                └─────────────────┘       │
│                                                                 │
│   ┌─────────────────┐                ┌─────────────────┐       │
│   │ Koaxialkabel    │                │ Bluetooth       │       │
│   │ (historisch)    │                │ 2,4 GHz         │       │
│   └─────────────────┘                └─────────────────┘       │
│                                                                 │
│   ┌─────────────────┐                ┌─────────────────┐       │
│   │ Glasfaser       │                │ Mobilfunk       │       │
│   │ (Licht)         │                │ LTE, 5G         │       │
│   └─────────────────┘                └─────────────────┘       │
│                                                                 │
│   ┌─────────────────┐                ┌─────────────────┐       │
│   │ Twinax          │                │ Satellit        │       │
│   │ (Rechenzentrum) │                │ Richtfunk       │       │
│   └─────────────────┘                └─────────────────┘       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Twisted-Pair-Kabel (Kupfer)

### Aufbau

Twisted-Pair-Kabel bestehen aus **verdrillten Adernpaaren**, die elektromagnetische Störungen reduzieren:

```
┌─────────────────────────────────────────────────────────────────┐
│                TWISTED-PAIR-KABEL AUFBAU                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   UTP (Unshielded Twisted Pair)                                │
│   ┌─────────────────────────────────────────────────┐          │
│   │  ╭──╮ ╭──╮ ╭──╮ ╭──╮                           │          │
│   │  │╲╱│ │╲╱│ │╲╱│ │╲╱│   4 verdrillte Paare     │          │
│   │  │╱╲│ │╱╲│ │╱╲│ │╱╲│   = 8 Adern              │          │
│   │  ╰──╯ ╰──╯ ╰──╯ ╰──╯                           │          │
│   └─────────────────────────────────────────────────┘          │
│                                                                 │
│   STP (Shielded Twisted Pair)                                  │
│   ┌─────────────────────────────────────────────────┐          │
│   │ ┌───────────────────────────────────────────┐  │          │
│   │ │ ╭──╮ ╭──╮ ╭──╮ ╭──╮   Zusätzliche        │  │          │
│   │ │ │╲╱│ │╲╱│ │╲╱│ │╲╱│   Abschirmung        │  │          │
│   │ │ │╱╲│ │╱╲│ │╱╲│ │╱╲│   (Folie/Geflecht)   │  │          │
│   │ │ ╰──╯ ╰──╯ ╰──╯ ╰──╯                       │  │          │
│   │ └───────────────────────────────────────────┘  │          │
│   └─────────────────────────────────────────────────┘          │
│                                                                 │
│   Abschirmungstypen:                                           │
│   • U/UTP – Ungeschirmt                                        │
│   • F/UTP – Folienschirm um alle Paare                        │
│   • S/FTP – Geflechtschirm + Folie pro Paar                   │
│   • SF/FTP – Geflecht + Folie gesamt + Folie pro Paar         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Kabelkategorien

| Kategorie | Max. Frequenz | Anwendung | Max. Geschwindigkeit |
|-----------|---------------|-----------|---------------------|
| Cat3 | 16 MHz | Telefon, 10BASE-T | 10 Mbit/s |
| Cat5 | 100 MHz | 100BASE-TX | 100 Mbit/s |
| Cat5e | 100 MHz | 1000BASE-T | 1 Gbit/s |
| Cat6 | 250 MHz | 1000BASE-T, 10GBASE-T* | 10 Gbit/s (55m) |
| Cat6a | 500 MHz | 10GBASE-T | 10 Gbit/s (100m) |
| Cat7 | 600 MHz | 10GBASE-T | 10 Gbit/s |
| Cat7a | 1000 MHz | 10GBASE-T+ | 10+ Gbit/s |
| Cat8 | 2000 MHz | 25/40GBASE-T | 40 Gbit/s (30m) |

### Stecker: RJ45

```
┌─────────────────────────────────────────────────────────────────┐
│                    RJ45 STECKER (8P8C)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Pinbelegung (T568B – Standard):                              │
│                                                                 │
│   ┌─────────────────────────────────────┐                      │
│   │  1   2   3   4   5   6   7   8      │                      │
│   │  │   │   │   │   │   │   │   │      │                      │
│   │  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼      │                      │
│   │ w/o  o w/g  bl w/bl  g w/br br      │                      │
│   └─────────────────────────────────────┘                      │
│                                                                 │
│   Pin  Farbe T568B      Farbe T568A      Funktion (1G)         │
│   ───  ───────────      ───────────      ───────────           │
│   1    Weiß/Orange      Weiß/Grün        TX+ (Senden)          │
│   2    Orange           Grün             TX- (Senden)          │
│   3    Weiß/Grün        Weiß/Orange      RX+ (Empfangen)       │
│   4    Blau             Blau             (bei 1G: BI_D+)       │
│   5    Weiß/Blau        Weiß/Blau        (bei 1G: BI_D-)       │
│   6    Grün             Orange           RX- (Empfangen)       │
│   7    Weiß/Braun       Weiß/Braun       (bei 1G: BI_C+)       │
│   8    Braun            Braun            (bei 1G: BI_C-)       │
│                                                                 │
│   w/o = weiß/orange, o = orange, etc.                          │
│                                                                 │
│   Bei 100BASE-TX: nur Paare 1-2 und 3-6 verwendet             │
│   Bei 1000BASE-T: alle 4 Paare bidirektional                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Glasfaserkabel

### Funktionsprinzip

Glasfaser überträgt Daten als **Lichtimpulse** durch Totalreflexion im Glasfaserkern:

```
┌─────────────────────────────────────────────────────────────────┐
│                    GLASFASER AUFBAU                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Querschnitt:                                                  │
│   ┌─────────────────────────────────────────────────┐          │
│   │               ┌───────────────┐                 │          │
│   │    Mantel     │    Cladding   │                 │          │
│   │  (Schutz)     │   (Umhüllung) │                 │          │
│   │               │  ┌─────────┐  │                 │          │
│   │               │  │  Core   │  │  ← Lichtwelle  │          │
│   │               │  │ (Kern)  │  │                 │          │
│   │               │  └─────────┘  │                 │          │
│   │               └───────────────┘                 │          │
│   └─────────────────────────────────────────────────┘          │
│                                                                 │
│   Totalreflexion:                                               │
│                    n₁ > n₂ (Brechungsindex)                    │
│                                                                 │
│   ════════════════════════════════════════  Cladding (n₂)      │
│         ↗    ↗    ↗    ↗    ↗    ↗                             │
│        ↙    ↙    ↙    ↙    ↙    ↙      Lichtwelle              │
│   ════════════════════════════════════════  Cladding (n₂)      │
│                      Core (n₁)                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Singlemode vs. Multimode

| Eigenschaft | Singlemode (SMF) | Multimode (MMF) |
|-------------|------------------|-----------------|
| Kerndurchmesser | 9 µm | 50 oder 62,5 µm |
| Lichtquelle | Laser | LED oder VCSEL |
| Wellenlänge | 1310 nm, 1550 nm | 850 nm, 1300 nm |
| Reichweite | bis 100 km | bis 2 km |
| Bandbreite | Sehr hoch | Begrenzt |
| Kosten | Höher | Niedriger |
| Typischer Einsatz | WAN, Backbone | LAN, Rechenzentrum |
| Farbcodierung | Gelb | Orange (OM1/2), Aqua (OM3/4), Lime (OM5) |

### Glasfaser-Steckertypen

```
┌─────────────────────────────────────────────────────────────────┐
│                  GLASFASER-STECKER                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Stecker    Form        Anwendung           Besonderheit       │
│   ───────    ────        ─────────           ────────────       │
│                                                                 │
│   SC         Rechteckig  LAN, FTTH           Push-Pull          │
│              ┌──┐                                               │
│              │▓▓│                                               │
│              └──┘                                               │
│                                                                 │
│   LC         Klein       Rechenzentrum       Halb so groß       │
│              ┌─┐         SFP-Module          wie SC             │
│              │▓│                                                │
│              └─┘                                                │
│                                                                 │
│   ST         Rund        Ältere Netze        Bajonett-          │
│              (●)                             verschluss         │
│                                                                 │
│   MPO/MTP    Mehrf.      40G/100G+           12/24 Fasern       │
│              ┌──────┐    Parallel Optics                        │
│              │▓▓▓▓▓▓│                                           │
│              └──────┘                                           │
│                                                                 │
│   Politur (Ferrule-Ende):                                       │
│   • PC (Physical Contact) – leicht gewölbt                     │
│   • UPC (Ultra PC) – stärker poliert, blau                     │
│   • APC (Angled PC) – 8° Winkel, grün, weniger Reflexion       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Koaxialkabel (historisch)

Koaxialkabel wurden in frühen Ethernet-Netzen verwendet:

| Standard | Kabeltyp | Bezeichnung | Max. Länge |
|----------|----------|-------------|------------|
| 10BASE5 | RG-8 (Thick Coax) | Yellow Cable | 500 m |
| 10BASE2 | RG-58 (Thin Coax) | Cheapernet | 185 m |

> [!info] Heute
> Koaxialkabel werden in der Netzwerktechnik kaum noch verwendet, sind aber im Kabel-TV/Internet-Bereich (DOCSIS) weiterhin verbreitet.

## Drahtlose Medien

### WLAN (IEEE 802.11)

→ Siehe auch: [[../../02-Standards-und-Gremien/02-IEEE-Standards#IEEE 802.11 – WLAN/WiFi|IEEE 802.11 Standards]]

| Frequenzband | Eigenschaften |
|--------------|---------------|
| 2,4 GHz | Bessere Reichweite, mehr Interferenzen, weniger Kanäle |
| 5 GHz | Höhere Bandbreite, kürzere Reichweite, mehr Kanäle |
| 6 GHz | Nur WiFi 6E/7, noch weniger Interferenzen |

### Weitere drahtlose Technologien

| Technologie | Frequenz | Reichweite | Anwendung |
|-------------|----------|------------|-----------|
| Bluetooth | 2,4 GHz | 10-100 m | PAN, Peripherie |
| ZigBee | 2,4 GHz | 10-100 m | IoT, Smart Home |
| LTE/5G | Diverse | km-Bereich | Mobilfunk |
| Richtfunk | Diverse | km-Bereich | Backbone |

## Vergleich der Medien

| Medium | Bandbreite | Reichweite | Störanfällig | Kosten | Sicherheit |
|--------|------------|------------|--------------|--------|------------|
| UTP | Bis 40 Gbit/s | 100 m | Mittel | Niedrig | Niedrig |
| STP | Bis 40 Gbit/s | 100 m | Gering | Mittel | Mittel |
| Multimode | Bis 400 Gbit/s | 2 km | Sehr gering | Mittel | Hoch |
| Singlemode | Bis 400 Gbit/s | 100 km | Sehr gering | Hoch | Hoch |
| WLAN | Bis 46 Gbit/s | 100 m | Hoch | Niedrig | Mittel |

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **Twisted Pair** (Cat5e bis Cat8) ist das häufigste LAN-Medium
> - **Glasfaser** bietet höchste Bandbreite und Reichweite
> - **Singlemode** für Weitstrecken, **Multimode** für kurze Distanzen
> - **RJ45** ist der Standard-Stecker für Kupfer-Ethernet
> - **LC** und **SC** sind gängige Glasfaser-Stecker
> - **WLAN** bietet Flexibilität, aber geringere Sicherheit

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Kabelkategorien (Cat5e, Cat6, Cat6a) und ihre Geschwindigkeiten
> - Verstehen Sie den Unterschied Singlemode vs. Multimode
> - Können Sie T568A/B Pinbelegung erklären
> - Wissen Sie, welche Reichweiten die verschiedenen Medien haben

## Verwandte Themen

- [[02-Signale]] – Leitungscodierung und Modulation
- [[../05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Ethernet-Frames
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE Standards]] – 802.3, 802.11

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- TIA/EIA-568 – Verkabelungsstandards
