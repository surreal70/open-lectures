---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - ipv6
  - layer3
  - adressierung
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# IPv6-Adressen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Aufbau einer IPv6-Adresse erklären können
> - IPv6-Adressen kürzen und expandieren können
> - Wichtige IPv6-Adresstypen kennen
> - Den Unterschied zwischen IPv4 und IPv6 verstehen

---

## Überblick

**IPv6** (Internet Protocol Version 6) wurde entwickelt, um den Adressmangel von IPv4 zu beheben. Mit 128 Bit statt 32 Bit bietet IPv6 einen praktisch unerschöpflichen Adressraum.

## Warum IPv6?

| Problem bei IPv4 | Lösung durch IPv6 |
|------------------|-------------------|
| Nur ~4,3 Milliarden Adressen | ~340 Sextillionen Adressen |
| NAT erforderlich | Ende-zu-Ende-Konnektivität |
| Komplexes Subnetting | Vereinfachte Hierarchie |
| Manuelle Konfiguration | Autokonfiguration (SLAAC) |

## Aufbau einer IPv6-Adresse

Eine IPv6-Adresse besteht aus **128 Bit**, dargestellt als 8 Gruppen von je 4 Hexadezimalziffern:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
└──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘
  1    2    3    4    5    6    7    8
       (je 16 Bit = 4 Hex-Ziffern)
```

### Struktur

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
└────────────────┘ └────────────────────┘
   Präfix (64 Bit)    Interface ID (64 Bit)
   (Netzwerkanteil)   (Hostanteil)
```

## Kurzschreibweise

### Regel 1: Führende Nullen weglassen

```
2001:0db8:0000:0000:0000:0000:0000:0001
     ↓
2001:db8:0:0:0:0:0:1
```

### Regel 2: Aufeinanderfolgende Null-Gruppen mit :: ersetzen (nur einmal!)

```
2001:db8:0:0:0:0:0:1
     ↓
2001:db8::1
```

### Beispiele

| Vollständig | Gekürzt |
|-------------|---------|
| `2001:0db8:0000:0000:0000:0000:0000:0001` | `2001:db8::1` |
| `fe80:0000:0000:0000:0000:0000:0000:0001` | `fe80::1` |
| `0000:0000:0000:0000:0000:0000:0000:0001` | `::1` |
| `0000:0000:0000:0000:0000:0000:0000:0000` | `::` |

> [!warning] **Achtung**
> `::` darf nur **einmal** in einer Adresse vorkommen, sonst ist die Adresse nicht eindeutig!
> 
> ❌ `2001::db8::1` — Ungültig!

## IPv6-Adresstypen

| Typ | Präfix | Beschreibung |
|-----|--------|--------------|
| **Global Unicast** | 2000::/3 | Öffentlich routbar (wie öffentliche IPv4) |
| **Link-Local** | fe80::/10 | Nur im lokalen Netzwerksegment gültig |
| **Unique Local** | fc00::/7 | Privat, nicht im Internet routbar |
| **Loopback** | ::1/128 | localhost (wie 127.0.0.1) |
| **Unspecified** | ::/128 | Keine Adresse (wie 0.0.0.0) |
| **Multicast** | ff00::/8 | Gruppenadressierung |

### Link-Local-Adressen

Jedes IPv6-Interface hat **automatisch** eine Link-Local-Adresse:

```
fe80::    +    Interface ID (aus MAC-Adresse)
fe80::1a2b:3c4d:5e6f:7890
```

> [!note] **Wichtig für die Praxis**
> Link-Local-Adressen werden für Router-Discovery, Neighbor Discovery und andere lokale Kommunikation benötigt.

## IPv4 vs. IPv6

| Eigenschaft | IPv4 | IPv6 |
|-------------|------|------|
| **Adresslänge** | 32 Bit | 128 Bit |
| **Notation** | Dezimal (192.168.1.1) | Hexadezimal (2001:db8::1) |
| **Adressraum** | ~4,3 × 10⁹ | ~3,4 × 10³⁸ |
| **Header** | 20-60 Byte, variabel | 40 Byte, fix |
| **Prüfsumme** | Ja | Nein (von oberen Schichten) |
| **Broadcast** | Ja | Nein (Multicast stattdessen) |
| **ARP** | Ja | NDP (Neighbor Discovery Protocol) |
| **Konfiguration** | DHCP, manuell | SLAAC, DHCPv6, manuell |

## Praktische Befehle

### Windows

```cmd
# IPv6-Konfiguration anzeigen
ipconfig /all

# IPv6-Adresse pingen
ping -6 ::1
ping -6 fe80::1%12  (mit Interface-ID)
```

### Linux

```bash
# IPv6-Adressen anzeigen
ip -6 addr show

# IPv6 pingen
ping6 ::1
ping6 fe80::1%eth0
```

> [!example] **Übung: IPv6 erkunden**
> - [ ] Finde die Link-Local-Adresse deines Rechners
> - [ ] Ping die Loopback-Adresse `::1`
> - [ ] Kürze: `2001:0db8:0000:0042:0000:0000:0000:8329`
> - [ ] Expandiere: `fe80::1`

## Zusammenhänge

- → [[08-IPv4-Adressen|IPv4-Adressen (Vergleich)]]
- → [[02-Grundbegriffe|Grundbegriffe (OSI-Modell)]]
- → [[Glossar#I|Glossar: IPv6]]

> [!warning] **Prüfungsrelevant**
> - IPv6-Aufbau: 128 Bit, 8 Gruppen Hexadezimal
> - Kurzschreibregeln (führende Nullen, ::)
> - Wichtige Adresstypen: Global Unicast, Link-Local, Loopback
> - Unterschiede IPv4 vs. IPv6
> - Standard-Präfixlänge: /64 für Subnetze

> [!question] **Typische Prüfungsfragen**
> - Aus wie vielen Bits besteht eine IPv6-Adresse?
> - Kürzen Sie die Adresse 2001:0db8:0000:0000:0000:ff00:0042:8329
> - Was ist eine Link-Local-Adresse und woran erkennt man sie?
> - Nennen Sie zwei Unterschiede zwischen IPv4 und IPv6.
> - Welche IPv6-Adresse entspricht localhost?

## Quellen

- proTirone: LF03:11 IPv6-Adressen (Karsten Reincke, CC-BY-4.0)
- RFC 4291: IPv6 Addressing Architecture

> [!tip] **Weiterführende Links**
> - [IPv6 Test](https://test-ipv6.com/)
> - [Wikipedia: IPv6](https://de.wikipedia.org/wiki/IPv6)
> - [[00-LF03-Index|Zurück zur LF03-Übersicht]]
