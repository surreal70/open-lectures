---
author: Andreas Hümmer
title: Sicherungsschicht (Layer 2)
tags:
  - vorlesung
  - rn
  - osi
  - layer2
  - datalink
  - ethernet
  - index
created: '2026-10-09'
modified: '2026-10-13'
bereich: RN
---

# Sicherungsschicht (Layer 2)

Die Sicherungsschicht (Data Link Layer) ist für die **zuverlässige Übertragung von Frames** zwischen direkt verbundenen Knoten verantwortlich. Sie bildet zusammen mit der Physikalischen Schicht die TCP/IP-Netzzugangsschicht.

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Aufgaben der Sicherungsschicht benennen
> - Den Aufbau eines Ethernet-Frames erklären
> - MAC-Adressen verstehen und interpretieren
> - Die Unterschicht LLC und MAC unterscheiden
> - CSMA/CD und seine Bedeutung erklären
> - Spanning Tree Protocol verstehen

## Kapitelübersicht

| Nr. | Thema | Beschreibung |
|-----|-------|--------------|
| 01 | [[01-Rahmenbildung]] | Ethernet-Frame, MAC-Adressen |
| 02 | [[02-Fehlererkennung]] | CRC, FCS, Prüfsummen |
| 03 | [[03-MAC-Protokolle]] | CSMA/CD, Spanning Tree |

## Aufgaben der Sicherungsschicht

```
┌─────────────────────────────────────────────────────────────────┐
│              SICHERUNGSSCHICHT – AUFGABEN                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │  LLC (Logical Link Control) – IEEE 802.2                │  │
│   │  • Flusskontrolle                                       │  │
│   │  • Multiplexing höherer Protokolle                     │  │
│   │  • Fehlerkorrektur (optional)                          │  │
│   ├─────────────────────────────────────────────────────────┤  │
│   │  MAC (Media Access Control) – IEEE 802.3/11/etc.       │  │
│   │  • Rahmenbildung (Framing)                             │  │
│   │  • MAC-Adressierung (48-Bit)                           │  │
│   │  • Medienzugriffskontrolle (CSMA/CD, CSMA/CA)         │  │
│   │  • Fehlererkennung (CRC)                               │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│   Kernaufgaben:                                                 │
│   ─────────────                                                 │
│   1. Rahmenbildung → Daten in Frames kapseln                   │
│   2. Adressierung → Quelle und Ziel identifizieren (MAC)       │
│   3. Fehlererkennung → CRC/FCS berechnen und prüfen           │
│   4. Medienzugriff → Wer darf wann senden?                     │
│   5. Flusskontrolle → Sender nicht überlasten                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Geräte auf Layer 2

| Gerät | Funktion | Arbeitet mit |
|-------|----------|--------------|
| **Switch** | Frame-Weiterleitung | MAC-Adressen |
| **Bridge** | Verbindet Segmente | MAC-Adressen |
| **Access Point** | WLAN-Anbindung | MAC-Adressen |
| **Netzwerkkarte** | Frame-Verarbeitung | MAC-Adresse |

## Protokolle und Standards

- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE 802.3]] – Ethernet
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE 802.11]] – WLAN
- [[07-Anhang/IEEE-802-Standards/IEEE 802.1Q|IEEE 802.1Q]] – VLANs
- [[07-Anhang/IEEE-802-Standards/IEEE 802.1D|IEEE 802.1D]] – Spanning Tree
- PPP, HDLC – Punkt-zu-Punkt

## Verwandte Themen

- [[../01-OSI-Modell|OSI-Modell]] – Die 7 Schichten im Überblick
- [[../04-Physikalische-Schicht/00-Physikalische-Schicht-Index|Physikalische Schicht]] – Layer 1
- [[../06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] – Layer 3

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
