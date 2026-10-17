---
author: Andreas Hümmer
title: Physikalische Schicht (Layer 1)
tags:
  - vorlesung
  - rn
  - osi
  - layer1
  - physical
  - index
created: '2026-10-09'
modified: '2026-10-13'
bereich: RN
---

# Physikalische Schicht (Layer 1)

Die Physikalische Schicht ist die unterste Schicht des OSI-Modells und der TCP/IP-Netzzugangsschicht. Sie ist verantwortlich für die **Übertragung von Bits** über das physikalische Medium.

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Aufgaben der Physikalischen Schicht benennen
> - Verschiedene Übertragungsmedien und ihre Eigenschaften vergleichen
> - Leitungscodierungen erklären (Manchester, 4B5B, 8B10B)
> - Stecker- und Kabeltypen zuordnen
> - Die Begriffe Bandbreite, Dämpfung und Signalqualität erklären

## Kapitelübersicht

| Nr. | Thema | Beschreibung |
|-----|-------|--------------|
| 01 | [[01-Uebertragungsmedien]] | Kupfer, Glasfaser, Funk |
| 02 | [[02-Signale]] | Codierung, Modulation, Signalqualität |

## Aufgaben der Physikalischen Schicht

![[physikalische-schicht-aufgaben.png]]
*<span class="fig-id">03-03-04-00-physikalische-schicht-aufgaben</span>: Datenfluss durch die Physikalische Schicht – von Bits über Leitungscodierung und Signalübertragung zum physikalischen Medium.*

## Geräte auf Layer 1

| Gerät | Funktion |
|-------|----------|
| **Hub** | Signalverstärkung, Broadcast an alle Ports |
| **Repeater** | Signalverstärkung über größere Distanzen |
| **MAU** | Media Access Unit – Transceiver |
| **Netzwerkkarte** | Physikalische Schnittstelle (NIC) |
| **Kabel/Stecker** | Physikalisches Medium |

## Verwandte Themen

- [[../01-OSI-Modell|OSI-Modell]] – Die 7 Schichten im Überblick
- [[../05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Die nächsthöhere Schicht
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE 802.3]] – Ethernet-Standards

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
