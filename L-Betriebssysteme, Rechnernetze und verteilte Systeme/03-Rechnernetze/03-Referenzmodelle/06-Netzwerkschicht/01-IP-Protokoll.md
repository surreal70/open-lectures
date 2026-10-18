---
author: Andreas Hümmer
title: IP-Protokoll (IPv4)
tags:
  - content
  - rn
  - network-layer
  - ip
  - ipv4
  - adressierung
  - subnetting
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# IP-Protokoll (IPv4)

## Definition

Das **Internet Protocol Version 4 (IPv4)** ist das zentrale Protokoll der Netzwerkschicht (Layer 3), das die logische Adressierung und Weiterleitung von Paketen über Netzwerkgrenzen hinweg ermöglicht.

## Grundlegende Eigenschaften

IPv4 ist durch folgende Merkmale charakterisiert:

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Verbindungslos** | Kein Verbindungsaufbau vor Datentransfer |
| **Unzuverlässig** | Best-Effort-Zustellung, keine Garantie |
| **Paketorientiert** | Daten werden in einzelne Pakete aufgeteilt |
| **Adressraum** | 32-Bit-Adressen (ca. 4,3 Milliarden) |

> [!info] Best-Effort-Prinzip
> IP garantiert weder die Zustellung, noch die Reihenfolge, noch die Fehlerfreiheit der Pakete. Diese Aufgaben übernehmen höhere Schichten wie [[01-TCP|TCP]].

## IPv4-Header-Aufbau

Der IPv4-Header ist mindestens 20 Bytes lang (ohne Optionen):

![[ipv4-header.png]]
*<span class="fig-id">03-03-06-01-ipv4-header</span>: Aufbau des IPv4-Headers mit allen Feldern und ihrer Bitbreite.*

### Header-Felder im Detail

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **Version** | 4 | IP-Version (4 für IPv4) |
| **IHL** | 4 | Internet Header Length in 32-Bit-Worten |
| **ToS/DSCP** | 8 | Type of Service / Differentiated Services |
| **Total Length** | 16 | Gesamtlänge des Pakets in Bytes |
| **Identification** | 16 | Eindeutige Paket-ID (für Fragmentierung) |
| **Flags** | 3 | DF (Don't Fragment), MF (More Fragments) |
| **Fragment Offset** | 13 | Position des Fragments im Originalpaket |
| **TTL** | 8 | Time to Live (Hop-Limit) |
| **Protocol** | 8 | Protokoll der nächsten Schicht (6=TCP, 17=UDP) |
| **Header Checksum** | 16 | Prüfsumme des Headers |
| **Source Address** | 32 | Quell-IP-Adresse |
| **Destination Address** | 32 | Ziel-IP-Adresse |

> [!tip] TTL (Time to Live)
> Der TTL-Wert wird bei jedem Router um 1 dekrementiert. Erreicht er 0, wird das Paket verworfen und eine ICMP-Fehlermeldung (Time Exceeded) an den Absender geschickt. Dies verhindert Endlosschleifen im Netzwerk.

## IPv4-Adressierung

### Adressformat

Eine IPv4-Adresse besteht aus **32 Bit**, dargestellt als vier dezimale Oktette:

```
Binär:      11000000.10101000.00000001.00001010
Dezimal:    192     .168     .1       .10
```

### Netzwerk- und Hostanteil

Jede IP-Adresse besteht aus zwei Teilen:

![[ip-netzwerk-host.png]]
*<span class="fig-id">03-03-06-01-ip-netzwerk-host</span>: Aufteilung einer IPv4-Adresse in Netzwerk- und Hostanteil am Beispiel 192.168.1.10/24.*

### Subnetzmaske und CIDR

Die Subnetzmaske definiert die Grenze zwischen Netzwerk- und Hostanteil:

| CIDR | Subnetzmaske | Binär | Hosts |
|------|--------------|-------|-------|
| /8 | 255.0.0.0 | 11111111.00000000.00000000.00000000 | 16.777.214 |
| /16 | 255.255.0.0 | 11111111.11111111.00000000.00000000 | 65.534 |
| /24 | 255.255.255.0 | 11111111.11111111.11111111.00000000 | 254 |
| /25 | 255.255.255.128 | 11111111.11111111.11111111.10000000 | 126 |
| /26 | 255.255.255.192 | 11111111.11111111.11111111.11000000 | 62 |
| /27 | 255.255.255.224 | 11111111.11111111.11111111.11100000 | 30 |
| /28 | 255.255.255.240 | 11111111.11111111.11111111.11110000 | 14 |
| /30 | 255.255.255.252 | 11111111.11111111.11111111.11111100 | 2 |

> [!note] Berechnung der Hostanzahl
> **Formel:** $2^{(32-\text{Präfixlänge})} - 2$
> 
> Die Subtraktion von 2 berücksichtigt:
> - Netzwerkadresse (alle Hostbits = 0)
> - Broadcast-Adresse (alle Hostbits = 1)

### Subnetting-Beispiel

**Aufgabe:** Teile das Netzwerk 192.168.1.0/24 in 4 Subnetze

Originalnetzwerk: 192.168.1.0/24 (254 Hosts)
Subnetting auf /26 ergibt 4 Subnetze mit je 62 Hosts:

| Subnetz | Netzwerkadresse | Hostbereich | Broadcast |
|---------|-----------------|-------------|-----------|
| 1 | 192.168.1.0/26 | 192.168.1.1 – 192.168.1.62 | 192.168.1.63 |
| 2 | 192.168.1.64/26 | 192.168.1.65 – 192.168.1.126 | 192.168.1.127 |
| 3 | 192.168.1.128/26 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191 |
| 4 | 192.168.1.192/26 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255 |

## IP-Adressklassen (historisch)

> [!warning] Veraltet
> Das Klassensystem wurde durch **CIDR (Classless Inter-Domain Routing)** ersetzt, ist aber für das Verständnis historischer Netze relevant.

| Klasse | Bereich | Präfix | Netzwerke | Hosts/Netz |
|--------|---------|--------|-----------|------------|
| A | 1.0.0.0 - 126.255.255.255 | /8 | 126 | 16.777.214 |
| B | 128.0.0.0 - 191.255.255.255 | /16 | 16.384 | 65.534 |
| C | 192.0.0.0 - 223.255.255.255 | /24 | 2.097.152 | 254 |
| D | 224.0.0.0 - 239.255.255.255 | - | Multicast | - |
| E | 240.0.0.0 - 255.255.255.255 | - | Reserviert | - |

## Private und öffentliche Adressen

### Private Adressbereiche (RFC 1918)

Diese Adressen sind nicht im Internet routbar:

| Klasse | Bereich | CIDR | Anwendung |
|--------|---------|------|-----------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 | Große Unternehmen |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 | Mittlere Netze |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 | Heimnetzwerke |

### Spezielle und reservierte IPv4-Adressbereiche

Die IANA hat verschiedene Adressbereiche für spezielle Zwecke reserviert:

| Adressbereich | CIDR | Zweck | RFC |
|---------------|------|-------|-----|
| 0.0.0.0/8 | /8 | "Dieses Netzwerk" (This host) | [[A-RFC-Index#RFC 1122\|RFC 1122]] |
| 10.0.0.0/8 | /8 | Privat (Klasse A) | [[A-RFC-Index#RFC 1918\|RFC 1918]] |
| 100.64.0.0/10 | /10 | Carrier-Grade NAT (CGNAT) | [[A-RFC-Index#RFC 6598\|RFC 6598]] |
| 127.0.0.0/8 | /8 | Loopback | [[A-RFC-Index#RFC 1122\|RFC 1122]] |
| 169.254.0.0/16 | /16 | Link-Local (APIPA) | [[A-RFC-Index#RFC 3927\|RFC 3927]] |
| 172.16.0.0/12 | /12 | Privat (Klasse B) | [[A-RFC-Index#RFC 1918\|RFC 1918]] |
| 192.0.0.0/24 | /24 | IETF Protocol Assignments | [[A-RFC-Index#RFC 6890\|RFC 6890]], [[A-RFC-Index#RFC 8190\|RFC 8190]] |
| 192.0.2.0/24 | /24 | Dokumentation (TEST-NET-1) | [[A-RFC-Index#RFC 5737\|RFC 5737]] |
| 192.88.99.0/24 | /24 | 6to4 Relay Anycast (deprecated) | [[A-RFC-Index#RFC 7526\|RFC 7526]] |
| 192.168.0.0/16 | /16 | Privat (Klasse C) | [[A-RFC-Index#RFC 1918\|RFC 1918]] |
| 198.18.0.0/15 | /15 | Benchmark-Tests | [[A-RFC-Index#RFC 2544\|RFC 2544]] |
| 198.51.100.0/24 | /24 | Dokumentation (TEST-NET-2) | [[A-RFC-Index#RFC 5737\|RFC 5737]] |
| 203.0.113.0/24 | /24 | Dokumentation (TEST-NET-3) | [[A-RFC-Index#RFC 5737\|RFC 5737]] |
| 224.0.0.0/4 | /4 | Multicast | [[A-RFC-Index#RFC 5771\|RFC 5771]] |
| 233.252.0.0/24 | /24 | Multicast-Dokumentation (MCAST-TEST-NET) | [[A-RFC-Index#RFC 5771\|RFC 5771]] |
| 240.0.0.0/4 | /4 | Reserviert (ehem. Klasse E) | [[A-RFC-Index#RFC 1112\|RFC 1112]] |
| 255.255.255.255/32 | /32 | Limited Broadcast | [[A-RFC-Index#RFC 919\|RFC 919]] |

> [!info] RFC-Updates
> Die zentralen Registries für spezielle IP-Adressen werden in [[A-RFC-Index#RFC 6890|RFC 6890]] definiert und durch [[A-RFC-Index#RFC 8190|RFC 8190]] (2017) aktualisiert.

#### Wichtige Kategorien

![[private-adressbereiche.png]]
*<span class="fig-id">03-03-06-01-private-adressbereiche</span>: Die drei privaten IPv4-Adressbereiche nach RFC 1918 im Größenvergleich.*

#### Dokumentations-Adressbereiche

Für Dokumentation, Bücher und Beispielkonfigurationen sind drei TEST-NET-Bereiche reserviert (siehe auch Tabelle „Spezielle und reservierte IPv4-Adressbereiche" oben):

- **192.0.2.0/24** (TEST-NET-1)
- **198.51.100.0/24** (TEST-NET-2)
- **203.0.113.0/24** (TEST-NET-3)

> [!warning] Niemals produktiv nutzen
> Diese Adressen sollten nie in produktiven Netzen oder im Internet auftauchen.

#### Carrier-Grade NAT (CGNAT)

![[cgnat.png]]
*<span class="fig-id">03-03-06-01-cgnat</span>: CGNAT ermöglicht ISPs, mehrere Kunden hinter einer öffentlichen IP-Adresse zu betreiben.*

**Nachteile von CGNAT:**
- Doppeltes NAT (Kunde-NAT + ISP-NAT)
- Probleme mit Portweiterleitung
- Peer-to-Peer-Verbindungen erschwert
- Einschränkungen bei Online-Gaming und VoIP

#### Link-Local (APIPA)

#### Link-Local (APIPA)

**Automatische Zuweisung wenn:**
- Kein DHCP-Server erreichbar
- Statische IP nicht konfiguriert

![[link-local.png]]
*<span class="fig-id">03-03-06-01-link-local</span>: Zwei PCs mit automatisch zugewiesenen Link-Local-Adressen.*

**Reservierte Bereiche:**
- 169.254.0.0/24 → Reserviert
- 169.254.255.0/24 → Reserviert
- 169.254.1.0 – 169.254.254.255 → Nutzbar

> [!info] Nicht routbar
> Link-Local-Adressen sind nur im lokalen Segment gültig und können nicht über Router weitergeleitet werden.

#### Multicast-Adressbereiche

| Bereich | Scope | Verwendung |
|---------|-------|------------|
| 224.0.0.0/24 | Link-Local | Routing-Protokolle (OSPF, RIP) |
| 224.0.0.1 | Link-Local | Alle Hosts im Segment |
| 224.0.0.2 | Link-Local | Alle Router im Segment |
| 224.0.0.5 | Link-Local | OSPF-Router |
| 224.0.0.6 | Link-Local | OSPF Designated Router |
| 224.0.0.9 | Link-Local | RIPv2-Router |
| 224.0.1.0/24 | Internetwork | Kontrollierte Multicast-Dienste |
| 239.0.0.0/8 | Administrativ | Privater Multicast (wie RFC 1918) |

> [!tip] Prüfungshinweis
> Die speziellen Adressbereiche sind ein beliebtes Prüfungsthema:
> - Private Adressen (10/172.16/192.168) und deren Größe
> - Dokumentationsadressen für Beispiele
> - Loopback (127.0.0.1) und Link-Local (169.254.x.x)
> - CGNAT als Übergangslösung

## NAT - Network Address Translation

NAT ermöglicht die Nutzung privater Adressen hinter einer öffentlichen IP:

![[nat-schema.png]]
*<span class="fig-id">03-03-06-01-nat-schema</span>: NAT übersetzt private Adressen in eine öffentliche IP-Adresse.*

**Beispiel NAT-Tabelle:**

| Interne Adresse | Externe Adresse | Protokoll |
|-----------------|-----------------|-----------|
| 192.168.1.10:4521 | 203.0.113.5:10001 | TCP |
| 192.168.1.11:3389 | 203.0.113.5:10002 | TCP |
| 192.168.1.12:8080 | 203.0.113.5:10003 | TCP |

### NAT-Varianten

- **Static NAT:** 1:1-Zuordnung intern ↔ extern
- **Dynamic NAT:** Pool von öffentlichen Adressen
- **PAT (Port Address Translation):** Viele interne → eine externe + Ports

## ICMP - Internet Control Message Protocol

ICMP dient der Fehler- und Statusmeldung auf Netzwerkebene:

| Typ | Code | Bezeichnung | Verwendung |
|-----|------|-------------|------------|
| 0 | 0 | Echo Reply | Antwort auf Ping |
| 3 | 0-15 | Destination Unreachable | Ziel nicht erreichbar |
| 8 | 0 | Echo Request | Ping-Anfrage |
| 11 | 0 | Time Exceeded | TTL abgelaufen |

> [!example] Ping und Traceroute
> - **Ping:** Sendet ICMP Echo Request, empfängt Echo Reply
> - **Traceroute:** Nutzt TTL-Inkrement und ICMP Time Exceeded

## ARP - Address Resolution Protocol

ARP löst IP-Adressen zu MAC-Adressen im lokalen Netzwerk auf:

![[arp-ablauf.png]]
*<span class="fig-id">03-03-06-01-arp-ablauf</span>: ARP-Ablauf zur Auflösung von IP- zu MAC-Adressen.*

> [!info] Weiterführend
> Details zu ARP und weiteren Basisprotokollen siehe [[../04-Basisprotokolle/01-ARP|ARP]].

> [!tip] ARP-Cache anzeigen
> ```bash
> # Windows
> arp -a
> 
> # Linux
> ip neigh show
> ```

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Subnetting-Berechnungen durchführen (Netzwerkadresse, Broadcast, Hostbereich)
> - Private vs. öffentliche Adressen unterscheiden (RFC 1918)
> - NAT-Funktionsweise und PAT erklären
> - Spezielle Adressbereiche kennen (Loopback, Link-Local, CGNAT)

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie für das Netzwerk X.X.X.X/Y: Netzwerkadresse, Broadcast, Hostbereich
> - Erklären Sie den Unterschied zwischen statischem NAT und PAT
> - Warum sind private IP-Adressen nicht im Internet routbar?
> - Was passiert mit einem IP-Paket, wenn TTL den Wert 0 erreicht?
> - Welche Aufgabe hat das Protocol-Feld im IPv4-Header?

### Merkregeln

> [!tip] Merkhilfe: Private Adressbereiche
> **"10 - 172 - 192"**
> - **10**.x.x.x (1 × Klasse A)
> - **172**.16-31.x.x (16 × Klasse B)
> - **192.168**.x.x (256 × Klasse C)

## Zusammenhänge

- [[02-Routing]] - Weiterleitung von IP-Paketen
- [[03-IPv6]] - Nachfolger mit 128-Bit-Adressen
- [[01-TCP|TCP]] / [[02-UDP|UDP]] - Transportprotokolle über IP
- [[05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] - MAC-Adressen, ARP

## Quellen

- [[A-RFC-Index|RFC 791]] - Internet Protocol
- [[A-RFC-Index|RFC 1918]] - Private Address Space
- [[A-RFC-Index|RFC 826]] - ARP
- [[A-RFC-Index|RFC 792]] - ICMP
- Tanenbaum, A. S.: Computernetzwerke, Kap. 5
