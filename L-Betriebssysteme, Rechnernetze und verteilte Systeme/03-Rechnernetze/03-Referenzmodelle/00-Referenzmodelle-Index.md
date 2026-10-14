---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-13'
tags:
  - content
  - index
  - rn
  - osi
  - tcp-ip
---

# Referenzmodelle

Dieses Kapitel behandelt die Referenzmodelle der Netzwerktechnik sowie die einzelnen Schichten im Detail.

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Das OSI-Referenzmodell und seine sieben Schichten erklären
> - Das TCP/IP-Modell und seine vier Schichten beschreiben
> - Die beiden Modelle vergleichen und Unterschiede benennen
> - Die Aufgaben jeder Schicht und typische Protokolle zuordnen

## Die Modelle

| Nr. | Thema | Beschreibung |
|-----|-------|--------------|
| 01 | [[01-OSI-Modell]] | Das ISO/OSI-Referenzmodell mit 7 Schichten |
| 02 | [[02-TCP-IP-Modell]] | Das DoD/TCP-IP-Modell mit 4 Schichten |
| 03 | [[03-Schichtenvergleich]] | Gegenüberstellung beider Modelle |

## Die Schichten im Detail

Nach dem Verständnis der Modelle werden die einzelnen Schichten vertieft:

| Nr. | Schicht | OSI | TCP/IP | Inhalt |
|-----|---------|-----|--------|--------|
| 04 | [[04-Physikalische-Schicht/00-Physikalische-Schicht-Index\|Physikalische Schicht]] | 1 | Netzzugang | Übertragungsmedien, Signale |
| 05 | [[05-Sicherungsschicht/00-Sicherungsschicht-Index\|Sicherungsschicht]] | 2 | Netzzugang | Frames, MAC, Ethernet |
| 06 | [[06-Netzwerkschicht/00-Netzwerkschicht-Index\|Netzwerkschicht]] | 3 | Internet | IP, Routing, ICMP |
| 07 | [[07-Transportschicht/00-Transportschicht-Index\|Transportschicht]] | 4 | Transport | TCP, UDP, Ports |
| 08 | [[08-Anwendungsschicht/00-Anwendungsschicht-Index\|Anwendungsschicht]] | 5-7 | Anwendung | HTTP, DNS, SMTP |

## Schichtenübersicht

```
┌─────────────────────────────────────────────────────────────────┐
│                    SCHICHTEN IM ÜBERBLICK                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   OSI-Modell              TCP/IP-Modell        Kapitel          │
│   ──────────              ─────────────        ───────          │
│                                                                 │
│   7. Anwendung    ┐                                             │
│   6. Darstellung  ├───── Anwendung ─────────── 08               │
│   5. Sitzung      ┘                                             │
│                                                                 │
│   4. Transport    ─────── Transport ─────────── 07              │
│                                                                 │
│   3. Vermittlung  ─────── Internet ──────────── 06              │
│                                                                 │
│   2. Sicherung    ┐                                             │
│                   ├───── Netzzugang ─────────── 05, 04          │
│   1. Bitübertrag. ┘                                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Verwandte Themen

- [[01-Grundlagen/00-Grundlagen-Index|Grundlagen]] – Einführung in Netzwerke
- [[02-Standards-und-Gremien/00-Standards-Index|Standards]] – IEEE, IETF und ihre Standards
- [[04-Sicherheit/00-Sicherheit-Index|Sicherheit]] – Schichtübergreifende Sicherheitsthemen
