---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - ipv4
  - subnetting
  - adressklassen
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# IPv4-Adressklassen und Subnetting

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die historischen IPv4-Adressklassen A, B, C kennen
> - Private und öffentliche Adressbereiche unterscheiden können
> - Subnetze berechnen können (Netzwerkadresse, Broadcast, Hosts)
> - Subnetting praktisch anwenden können

---

## Überblick

Die ursprüngliche Klasseneinteilung (Classful Addressing) wurde durch CIDR (Classless Inter-Domain Routing) abgelöst, ist aber für das Grundverständnis und Prüfungen weiterhin relevant.

## Historische Adressklassen

### Klasseneinteilung

| Klasse | Erstes Bit | Bereich | Standard-Maske | Netzwerke | Hosts/Netz |
|--------|-----------|---------|----------------|-----------|------------|
| **A** | 0xxx | 1.0.0.0 – 126.255.255.255 | /8 | 126 | 16.777.214 |
| **B** | 10xx | 128.0.0.0 – 191.255.255.255 | /16 | 16.384 | 65.534 |
| **C** | 110x | 192.0.0.0 – 223.255.255.255 | /24 | 2.097.152 | 254 |
| **D** | 1110 | 224.0.0.0 – 239.255.255.255 | — | Multicast | — |
| **E** | 1111 | 240.0.0.0 – 255.255.255.255 | — | Reserviert | — |

> [!note] **Warum nur 126 Klasse-A-Netzwerke?**
> - 0.x.x.x ist reserviert ("dieses Netzwerk")
> - 127.x.x.x ist für Loopback (localhost) reserviert

### Private Adressbereiche (RFC 1918)

Diese Adressen sind im Internet **nicht routbar** und für interne Netzwerke vorgesehen:

| Klasse | Bereich | CIDR | Anzahl Adressen |
|--------|---------|------|-----------------|
| A | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | 16.777.216 |
| B | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 1.048.576 |
| C | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 65.536 |

> [!tip] **Merkhilfe private Adressen**
> - **10.x.x.x** — Eine Zehn, ein großes Netz
> - **172.16-31.x.x** — Siebzehn bis einunddreißig
> - **192.168.x.x** — Der Heimnetz-Klassiker

## Subnetting

### Warum Subnetting?

- **Effizienz**: Aufteilung großer Netzwerke in kleinere
- **Organisation**: Logische Trennung von Abteilungen
- **Sicherheit**: Isolierung von Netzwerkbereichen
- **Performance**: Reduzierung von Broadcast-Traffic

### Subnetting-Berechnungen

Für ein Netzwerk mit gegebenem CIDR-Präfix:

| Berechnung | Formel |
|------------|--------|
| **Anzahl Subnetze** | 2^(neue Bits) |
| **Hosts pro Subnetz** | 2^(Hostbits) - 2 |
| **Subnetzmaske** | Dezimal aus Binär |
| **Netzwerkadresse** | IP AND Maske |
| **Broadcastadresse** | Netzwerk + alle Hostbits auf 1 |
| **Erste nutzbare IP** | Netzwerkadresse + 1 |
| **Letzte nutzbare IP** | Broadcastadresse - 1 |

### Beispiel: /24 aufteilen in /26

**Aufgabe**: Teile 192.168.1.0/24 in 4 Subnetze auf.

**Lösung**:
- Original: /24 = 256 Adressen
- Benötigt: 4 Subnetze → 2 zusätzliche Bits → /26
- Pro Subnetz: 2^6 = 64 Adressen, davon 62 nutzbar

| Subnetz | Netzwerkadresse | Bereich | Broadcast |
|---------|-----------------|---------|-----------|
| 1 | 192.168.1.0/26 | .1 – .62 | 192.168.1.63 |
| 2 | 192.168.1.64/26 | .65 – .126 | 192.168.1.127 |
| 3 | 192.168.1.128/26 | .129 – .190 | 192.168.1.191 |
| 4 | 192.168.1.192/26 | .193 – .254 | 192.168.1.255 |

### CIDR-Tabelle (wichtig für Prüfungen!)

| CIDR | Maske | Hosts | Inkrement |
|------|-------|-------|-----------|
| /24 | 255.255.255.0 | 254 | 256 |
| /25 | 255.255.255.128 | 126 | 128 |
| /26 | 255.255.255.192 | 62 | 64 |
| /27 | 255.255.255.224 | 30 | 32 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 |
| /31 | 255.255.255.254 | 0* | 2 |
| /32 | 255.255.255.255 | 1 | 1 |

**/30 ist typisch für Point-to-Point-Verbindungen** (nur 2 Hosts nötig).

> [!example] **Übung: Subnetting**
> **Aufgabe**: Ein Unternehmen hat das Netzwerk 10.20.0.0/16 und benötigt 50 Subnetze mit je mindestens 500 Hosts.
> 
> - [ ] Wie viele Bits werden für die Subnetze benötigt?
> - [ ] Welche Subnetzmaske ergibt sich?
> - [ ] Wie viele Hosts pro Subnetz sind möglich?
> - [ ] Gib die ersten 3 Subnetze an.

**Lösung**:
- 50 Subnetze → mindestens 6 Bits (2^6 = 64)
- 500 Hosts → mindestens 9 Bits (2^9 - 2 = 510)
- /16 + 6 Subnetz-Bits = /22
- Maske: 255.255.252.0
- Subnetze: 10.20.0.0/22, 10.20.4.0/22, 10.20.8.0/22, ...

## VLSM (Variable Length Subnet Masking)

Bei VLSM verwendet man unterschiedliche Subnetzgrößen je nach Bedarf:

```
Hauptnetz: 192.168.1.0/24

├── Server-Netz:   192.168.1.0/27   (30 Hosts)
├── Büro-Netz:     192.168.1.32/27  (30 Hosts)
├── Gäste-Netz:    192.168.1.64/28  (14 Hosts)
└── Point-to-Point: 192.168.1.80/30 (2 Hosts)
```

## Zusammenhänge

- → [[08-IPv4-Adressen|IPv4-Adressen Grundlagen]]
- → [[07-Binaeroperationen|Binäroperationen für Subnetting]]
- → [[10-IPv6-Adressen|IPv6-Adressen]]

> [!warning] **Prüfungsrelevant**
> - Adressklassen A, B, C mit Bereichen
> - Private Adressbereiche (RFC 1918)
> - Subnetting-Berechnungen
> - CIDR-Notation und Subnetzmasken-Tabelle
> - Netzwerk- und Broadcastadresse berechnen

> [!question] **Typische Prüfungsfragen**
> - Zu welcher Klasse gehört die IP 172.20.5.1?
> - Ist 192.168.50.1 eine private oder öffentliche Adresse?
> - Berechnen Sie für 10.0.0.0/8 die Anzahl möglicher Hosts.
> - Teilen Sie 192.168.0.0/24 in 8 Subnetze auf.
> - Welche Subnetzmaske entspricht /27?

## Quellen

- proTirone: LF03:10 IPv4-Klassen (Karsten Reincke, CC-BY-4.0)
- RFC 1918: Address Allocation for Private Internets
- RFC 4632: CIDR

> [!tip] **Weiterführende Links**
> - [Subnet Calculator](https://www.subnet-calculator.com/)
> - [CIDR Visualizer](https://cidr.xyz/)
> - [[10-IPv6-Adressen|Nächstes Kapitel: IPv6-Adressen]]
