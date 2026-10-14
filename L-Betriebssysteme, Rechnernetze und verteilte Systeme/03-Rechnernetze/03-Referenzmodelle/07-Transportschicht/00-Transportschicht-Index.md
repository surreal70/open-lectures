---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - transport-layer
bereich: RN
---

# Transportschicht (Layer 4)

> [!info] Einordnung im OSI-Modell
> Die Transportschicht ist **Schicht 4** des OSI-Modells und entspricht der **Transportschicht** im TCP/IP-Modell. Sie ermöglicht die Ende-zu-Ende-Kommunikation zwischen Anwendungen auf verschiedenen Hosts.

## Lernziele

Nach diesem Kapitel sollten Sie:

- [ ] Die Aufgaben der Transportschicht erklären können
- [ ] TCP und UDP unterscheiden und deren Einsatzgebiete kennen
- [ ] Den TCP-Verbindungsaufbau (3-Way-Handshake) verstehen
- [ ] Portnummern und ihre Bedeutung erklären können
- [ ] Fluss- und Staukontrolle bei TCP verstehen

## Kernaufgaben der Transportschicht

```
┌─────────────────────────────────────────────────────────────────┐
│                   TRANSPORTSCHICHT (Layer 4)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  MULTIPLEXING    │    │  SEGMENTIERUNG   │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • Portnummern    │    │ • Datenaufteilung│                  │
│   │ • Socket-Bindung │    │ • Reassembly     │                  │
│   │ • Demultiplexing │    │ • Sequenznummern │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│   ┌──────────────────┐    ┌──────────────────┐                  │
│   │  FLUSSKONTROLLE  │    │  STAUKONTROLLE   │                  │
│   ├──────────────────┤    ├──────────────────┤                  │
│   │ • Receive Window │    │ • Congestion     │                  │
│   │ • Überlastschutz │    │   Avoidance      │                  │
│   │   (Empfänger)    │    │ • Slow Start     │                  │
│   └──────────────────┘    └──────────────────┘                  │
│                                                                  │
│         PDU: Segment (TCP) / Datagramm (UDP)                    │
└─────────────────────────────────────────────────────────────────┘
```

## TCP vs. UDP im Überblick

| Eigenschaft | TCP | UDP |
|-------------|-----|-----|
| **Verbindung** | Verbindungsorientiert | Verbindungslos |
| **Zuverlässigkeit** | Garantierte Zustellung | Best-Effort |
| **Reihenfolge** | Garantiert | Nicht garantiert |
| **Header-Größe** | 20-60 Bytes | 8 Bytes |
| **Overhead** | Hoch | Niedrig |
| **Geschwindigkeit** | Langsamer | Schneller |
| **Anwendung** | Web, E-Mail, Datei | DNS, Streaming, VoIP |

## Inhaltsverzeichnis

1. [[01-TCP]] - Transmission Control Protocol
2. [[02-UDP]] - User Datagram Protocol
3. [[03-Ports]] - Portnummern und Sockets

## Ende-zu-Ende-Prinzip

```
┌─────────────┐                                    ┌─────────────┐
│ Anwendung A │                                    │ Anwendung B │
│  (Client)   │                                    │  (Server)   │
└──────┬──────┘                                    └──────┬──────┘
       │                                                  │
       │  ◄──────── Transportschicht-Verbindung ────────► │
       │           (Ende-zu-Ende)                         │
       │                                                  │
┌──────┴──────┐    ┌─────────┐    ┌─────────┐    ┌──────┴──────┐
│   Host A    │────│ Router  │────│ Router  │────│   Host B    │
│192.168.1.10 │    │         │    │         │    │ 10.0.0.5    │
│   :50000    │    │         │    │         │    │   :80       │
└─────────────┘    └─────────┘    └─────────┘    └─────────────┘

Router verarbeiten nur Layer 1-3 (IP)
Transportschicht ist End-to-End (Host-zu-Host)
```

> [!tip] Prüfungsrelevanz
> Die Transportschicht ist ein **Kernthema** in der Prüfung. Besonders wichtig sind:
> - TCP vs. UDP Unterschiede
> - TCP 3-Way-Handshake
> - Portnummern (Well-Known, Registered, Dynamic)
> - Flusskontrolle und Sliding Window

## Weiterführende Themen

- [[01-OSI-Modell]] - Einordnung im Schichtenmodell
- [[02-TCP-IP-Modell]] - Transportschicht
- [[06-Netzwerkschicht/00-Netzwerkschicht-Index|Netzwerkschicht]] - Darunterliegende Schicht
- [[08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] - Darüberliegende Schicht
