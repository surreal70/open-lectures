---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - ipv4
  - layer3
  - adressierung
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# IPv4-Adressen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Aufbau einer IPv4-Adresse erklären können
> - Dezimal- und Binärdarstellung umrechnen können
> - Netzwerk- und Hostanteil einer IP-Adresse bestimmen können
> - Die CIDR-Notation verstehen und anwenden können

---

## Überblick

Eine **IPv4-Adresse** identifiziert ein Netzwerkinterface eindeutig im Netzwerk. Sie arbeitet auf **Layer 3** (Vermittlungsschicht) des OSI-Modells.

## Aufbau einer IPv4-Adresse

Eine IPv4-Adresse besteht aus **32 Bit** (4 Byte), dargestellt als vier durch Punkte getrennte Dezimalzahlen (Dotted Decimal Notation):

```
192.168.1.100
│   │   │  │
│   │   │  └── 4. Oktett (8 Bit): 100 = 01100100
│   │   └───── 3. Oktett (8 Bit):   1 = 00000001
│   └───────── 2. Oktett (8 Bit): 168 = 10101000
└───────────── 1. Oktett (8 Bit): 192 = 11000000
```

### Wertebereich

Jedes Oktett kann Werte von **0 bis 255** annehmen (2⁸ = 256 Möglichkeiten).

| Dezimal | Binär |
|---------|-------|
| 0 | `00000000` |
| 1 | `00000001` |
| 128 | `10000000` |
| 255 | `11111111` |

## Netzwerk- und Hostanteil

Jede IP-Adresse besteht aus zwei Teilen:

```
       Netzwerkanteil    Hostanteil
       ┌───────────┐    ┌────┐
       192.168.1   .    100
       └───────────┘    └────┘
```

Die **Subnetzmaske** bestimmt, welche Bits zum Netzwerk gehören:

| Subnetzmaske | Binär | Netzwerkbits |
|--------------|-------|--------------|
| 255.0.0.0 | `11111111.00000000.00000000.00000000` | /8 |
| 255.255.0.0 | `11111111.11111111.00000000.00000000` | /16 |
| 255.255.255.0 | `11111111.11111111.11111111.00000000` | /24 |

## CIDR-Notation

Die **Classless Inter-Domain Routing (CIDR)** Notation gibt die Anzahl der Netzwerkbits an:

```
192.168.1.100/24
              └── 24 Bit = Netzwerkanteil
                   8 Bit = Hostanteil
```

| CIDR | Subnetzmaske | Hosts |
|------|--------------|-------|
| /8 | 255.0.0.0 | 16.777.214 |
| /16 | 255.255.0.0 | 65.534 |
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /30 | 255.255.255.252 | 2 |

> [!note] **Hosts berechnen**
> Anzahl nutzbarer Hosts = 2^(32-CIDR) - 2
> 
> Die "-2" berücksichtigt Netzwerkadresse und Broadcastadresse.

## Wichtige Berechnungen

### Netzwerkadresse berechnen

IP-Adresse AND Subnetzmaske = Netzwerkadresse

```
IP:     192.168.1.100  = 11000000.10101000.00000001.01100100
Maske:  255.255.255.0  = 11111111.11111111.11111111.00000000
        ─────────────────────────────────────────────────────
Netz:   192.168.1.0    = 11000000.10101000.00000001.00000000
```

### Broadcastadresse berechnen

Netzwerkadresse mit allen Hostbits auf 1:

```
Netz:      192.168.1.0   = 11000000.10101000.00000001.00000000
Broadcast: 192.168.1.255 = 11000000.10101000.00000001.11111111
```

> [!example] **Übung: Netzwerkberechnung**
> Gegeben: IP `172.16.45.200/20`
> 
> - [ ] Berechne die Subnetzmaske in Dezimalschreibweise
> - [ ] Berechne die Netzwerkadresse
> - [ ] Berechne die Broadcastadresse
> - [ ] Berechne die Anzahl möglicher Hosts

## Spezielle IPv4-Adressen

| Adresse/Bereich | Verwendung |
|-----------------|------------|
| `0.0.0.0` | "Alle Netzwerke" / Default |
| `127.0.0.0/8` | Loopback (localhost) |
| `255.255.255.255` | Limited Broadcast |
| `10.0.0.0/8` | Privat (Klasse A) |
| `172.16.0.0/12` | Privat (Klasse B) |
| `192.168.0.0/16` | Privat (Klasse C) |
| `169.254.0.0/16` | Link-Local (APIPA) |

> [!warning] **Private vs. Öffentliche Adressen**
> Private Adressen werden nur intern verwendet und sind im Internet nicht routbar. Sie werden per NAT (Network Address Translation) in öffentliche Adressen übersetzt.

## Praktische Befehle

### Windows

```cmd
# IP-Konfiguration anzeigen
ipconfig /all

# IP-Adresse erneuern (DHCP)
ipconfig /release
ipconfig /renew
```

### Linux

```bash
# IP-Adressen anzeigen
ip addr show

# Kurz
ip a

# Spezifisches Interface
ip addr show eth0
```

## Zusammenhänge

- → [[09-IPv4-Klassen|IPv4-Adressklassen]]
- → [[07-Binaeroperationen|Binäroperationen]]
- → [[10-IPv6-Adressen|IPv6-Adressen]]
- → [[06-MAC-Adressen|MAC-Adressen (Layer 2)]]

> [!warning] **Prüfungsrelevant**
> - IPv4-Aufbau: 32 Bit, 4 Oktette
> - Netzwerk- und Hostanteil
> - CIDR-Notation und Subnetzmasken
> - Berechnung von Netzwerk- und Broadcastadresse
> - Private IP-Adressbereiche

> [!question] **Typische Prüfungsfragen**
> - Aus wie vielen Bits besteht eine IPv4-Adresse?
> - Berechnen Sie die Netzwerkadresse für 192.168.10.50/24
> - Welche privaten IP-Adressbereiche gibt es?
> - Wie viele Hosts sind in einem /26-Netzwerk möglich?
> - Was bedeutet die CIDR-Notation /24?

## Quellen

- proTirone: LF03:09 IPv4-Adressen (Karsten Reincke, CC-BY-4.0)
- RFC 791: Internet Protocol

> [!tip] **Weiterführende Links**
> - [Subnet Calculator](https://www.subnet-calculator.com/)
> - [Wikipedia: IPv4](https://de.wikipedia.org/wiki/IPv4)
> - [[09-IPv4-Klassen|Nächstes Kapitel: IPv4-Adressklassen]]
