---
author: Andreas Hümmer
created: '2026-10-13'
modified: '2026-10-13'
tags:
  - content
  - rn
  - protokolle
  - ntp
  - layer7
bereich: RN
---

# NTP – Network Time Protocol

## Lernziele

- [ ] Bedeutung von Zeitsynchronisation verstehen
- [ ] NTP-Stratum-Hierarchie erklären können
- [ ] Synchronisationsverfahren kennen
- [ ] Unterschied NTP vs. SNTP verstehen

## Überblick

Das **Network Time Protocol (NTP)** synchronisiert Systemuhren in Netzwerken. Präzise Zeitsynchronisation ist kritisch für Logging, Authentifizierung, Zertifikate und verteilte Systeme.

**Verwendete Ports:** 123 UDP und TCP

```
┌─────────────────────────────────────────────────────────────┐
│                    NTP-Stratum-Hierarchie                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Stratum 0    ┌─────────────────────────────────────┐      │
│   (Referenz)   │  GPS  │  Atomuhr  │  DCF77  │  PPS  │      │
│                └───────────────┬─────────────────────┘      │
│                                │                            │
│   Stratum 1    ┌───────────────┴───────────────┐            │
│   (Primary)    │     Primäre NTP-Server        │            │
│                │   (direkt an Stratum 0)       │            │
│                └───────────────┬───────────────┘            │
│                                │                            │
│   Stratum 2    ┌───────────────┴───────────────┐            │
│   (Secondary)  │    Sekundäre NTP-Server       │            │
│                └───────────────┬───────────────┘            │
│                                │                            │
│   Stratum 3+   ┌───────────────┴───────────────┐            │
│   (Clients)    │   Clients, weitere Server     │            │
│                └───────────────────────────────┘            │
│                                                              │
│   Stratum 16 = unsynchronisiert                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Funktionsweise

> [!info] RFC-Referenz
> - NTPv4: [[A-RFC-Index#RFC 5905|RFC 5905]]
> - SNTP: [[A-RFC-Index#RFC 4330|RFC 4330]]

### Stratum-Konzept

TODO: Hierarchische Struktur, Stratum 0-15, Stratum 16 = unsync

### Zeitmessung

TODO: Round-Trip-Delay, Offset-Berechnung

```
      t1              t2              t3              t4
Client ─────────────> Server ─────────────> Client
       Request          │       Response
                        │
       Offset = ((t2-t1) + (t3-t4)) / 2
       Delay  = (t4-t1) - (t3-t2)
```

### Algorithmen

TODO: Clock Filter, Clock Selection, Clock Discipline

## Paketformat

TODO: NTP-Paketstruktur (48 Bytes)

## NTP vs. SNTP

| Aspekt | NTP | SNTP |
|--------|-----|------|
| Genauigkeit | Millisekunden | 100+ ms |
| Komplexität | Hoch | Niedrig |
| Algorithmen | Vollständig | Vereinfacht |
| Einsatz | Server, Clients | Embedded, einfache Clients |

TODO: Detaillierter Vergleich

## Sicherheit

### NTP-Amplification-Angriffe

TODO: DDoS via monlist

### NTS (Network Time Security)

TODO: Authentifizierung für NTP

## Alternativen

### PTP (Precision Time Protocol)

TODO: IEEE 1588, Sub-Mikrosekunden-Genauigkeit

### Chrony

TODO: Moderne NTP-Implementierung

## Praxisbeispiele

TODO: ntpq, chronyc, Konfiguration

## Prüfungsrelevanz

> [!warning] Prüfungsrelevant
> - Stratum-Hierarchie
> - Warum Zeitsynchronisation wichtig ist
> - Grundprinzip der Offset-Berechnung

## Zusammenfassung

TODO: Kernpunkte zusammenfassen

## Querverweise

- [[../05-Sicherheit/03-TLS|TLS]] – Zertifikate benötigen korrekte Zeit
- [[../../02-Betriebssysteme/04-Synchronisation/00-Synchronisation-Index|Synchronisation (BS)]] – Zeitstempel in verteilten Systemen
