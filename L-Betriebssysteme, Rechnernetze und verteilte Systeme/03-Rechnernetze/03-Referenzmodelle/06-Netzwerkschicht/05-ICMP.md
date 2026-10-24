---
author: Andreas Hümmer
title: ICMP - Internet Control Message Protocol
tags:
  - content
  - rn
  - network-layer
  - icmp
  - ping
  - traceroute
  - fehlerbehandlung
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# ICMP - Internet Control Message Protocol

> [!info] Lernziele
> Nach diesem Kapitel können Sie...
> - Die Rolle von ICMP in IP-Netzwerken erklären
> - Die wichtigsten ICMP-Nachrichtentypen nennen
> - Die Funktionsweise von Ping und Traceroute beschreiben
> - ICMP-Fehlermeldungen interpretieren
> - Sicherheitsaspekte von ICMP einschätzen

## Definition

> [!quote] Definition
> Das **Internet Control Message Protocol (ICMP)** ist ein Hilfsprotokoll der Netzwerkschicht, das Fehler- und Statusmeldungen zwischen Netzwerkgeräten übermittelt. Es dient der Diagnose und Verwaltung von IP-Netzwerken.
>
> > [!info] Schichtzuordnung
> > ICMP ist ein **Layer-3-Protokoll** (Netzwerkschicht), obwohl es in IP-Paketen gekapselt wird. Es nutzt IP zur Übertragung, gehört aber funktional zur Netzwerkschicht, da es IP-Fehlermeldungen und Netzwerkdiagnose bereitstellt.
## Einordnung im Protokollstapel

![[icmp-protokollstapel.png]]
*<span class="fig-id">03-06-05-icmp-protokollstapel</span>: ICMP im OSI-Modell – ein Layer-3-Protokoll, das in IP gekapselt wird.*

## ICMP-Header (ICMPv4)

Der ICMP-Header beginnt direkt nach dem IP-Header:

![[icmp-header.png]]
*<span class="fig-id">03-06-05-icmp-header</span>: ICMP-Header-Format mit Type, Code, Checksum und variablen Daten.*

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **Type** | 8 | Art der ICMP-Nachricht |
| **Code** | 8 | Subtyp der Nachricht |
| **Checksum** | 16 | Prüfsumme des ICMP-Pakets |
| **Rest of Header** | 32 | Typ-abhängige Daten |
| **Data** | variabel | Zusatzdaten (oft Original-IP-Header) |

## Wichtige ICMP-Nachrichtentypen (ICMPv4)

### Fehlermeldungen

| Type | Code | Name | Beschreibung |
|------|------|------|--------------|
| **3** | 0 | Destination Unreachable | Netz nicht erreichbar |
| **3** | 1 | Destination Unreachable | Host nicht erreichbar |
| **3** | 2 | Destination Unreachable | Protokoll nicht erreichbar |
| **3** | 3 | Destination Unreachable | Port nicht erreichbar |
| **3** | 4 | Destination Unreachable | Fragmentierung nötig, DF gesetzt |
| **3** | 13 | Destination Unreachable | Administrativ verboten (Firewall) |
| **4** | 0 | Source Quench | Überlastung (deprecated) |
| **5** | 0-3 | Redirect | Bessere Route verfügbar |
| **11** | 0 | Time Exceeded | TTL abgelaufen (bei Transit) |
| **11** | 1 | Time Exceeded | Fragment-Reassembly-Zeit überschritten |
| **12** | 0 | Parameter Problem | Fehler im IP-Header |

### Informationsmeldungen

| Type | Code | Name | Beschreibung |
|------|------|------|--------------|
| **0** | 0 | Echo Reply | Antwort auf Ping |
| **8** | 0 | Echo Request | Ping-Anfrage |
| **13** | 0 | Timestamp Request | Zeitstempel-Anfrage |
| **14** | 0 | Timestamp Reply | Zeitstempel-Antwort |

## Echo Request / Echo Reply (Ping)

![[icmp-ping-ablauf.png]]
*<span class="fig-id">03-06-05-icmp-ping-ablauf</span>: Ping-Ablauf – Echo Request und Echo Reply mit RTT-Messung.*

**Echo Request/Reply Header:**

![[icmp-echo-header.png]]
*<span class="fig-id">03-06-05-icmp-echo-header</span>: Echo Request/Reply Header mit Identifier und Sequence Number.*

> [!example] Ping-Beispiel
> ```bash
> $ ping 192.168.1.1
> PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
> 64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.5 ms
> 64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.4 ms
> 64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.4 ms
> ```

## Time Exceeded (TTL)

Wird gesendet, wenn ein Router ein Paket verwirft, weil der TTL-Wert auf 0 gefallen ist:

![[icmp-time-exceeded.png]]
*<span class="fig-id">03-06-05-icmp-time-exceeded</span>: Time Exceeded – Router sendet ICMP-Nachricht wenn TTL=0.*

## Destination Unreachable

| Code | Name | Beschreibung |
|------|------|--------------|
| **0** | Network Unreachable | Keine Route zum Zielnetzwerk |
| **1** | Host Unreachable | Host im Zielnetzwerk nicht erreichbar (ARP fehlgeschlagen) |
| **3** | Port Unreachable | UDP-Port geschlossen (keine Anwendung lauscht) |
| **4** | Fragmentation Needed | Paket zu groß, aber Don't Fragment gesetzt → **wichtig für Path MTU Discovery!** |
| **13** | Administratively Prohibited | Firewall blockiert das Paket |

## Traceroute / Tracert

Traceroute nutzt **Time Exceeded**-Nachrichten, um den Weg durch das Netzwerk zu ermitteln:

![[icmp-traceroute.png]]
*<span class="fig-id">03-06-05-icmp-traceroute</span>: Traceroute-Prinzip – TTL wird schrittweise erhöht, jeder Router antwortet mit Time Exceeded.*

**Unterschiede der Implementierungen:**

| System | Methode | Antwort vom Ziel |
|--------|---------|------------------|
| **Unix/Linux** | UDP-Pakete an hohe Ports | ICMP Port Unreachable (Type 3, Code 3) |
| **Windows** | ICMP Echo Request | ICMP Echo Reply (Type 0) |
| **Beide** | Optional: TCP SYN | TCP RST oder SYN-ACK |

> [!example] Traceroute-Beispiel
> ```bash
> $ traceroute google.com
>  1  192.168.1.1 (192.168.1.1)  1.234 ms  1.123 ms  1.089 ms
>  2  10.0.0.1 (10.0.0.1)  5.678 ms  5.432 ms  5.321 ms
>  3  172.16.0.1 (172.16.0.1)  10.123 ms  9.987 ms  10.234 ms
>  4  * * *                     (keine Antwort - Firewall?)
>  5  142.250.185.78 (142.250.185.78)  15.678 ms  15.432 ms  15.321 ms
> ```

## ICMPv6

ICMPv6 erweitert ICMP um zusätzliche Funktionen für IPv6:

### ICMPv6-Header

![[icmpv6-header.png]]
*<span class="fig-id">03-06-05-icmpv6-header</span>: ICMPv6-Header – gleiche Grundstruktur, aber andere Type-Nummern.*

### Wichtige ICMPv6-Typen

| Type | Name | Funktion |
|------|------|----------|
| **1** | Destination Unreachable | Ziel nicht erreichbar |
| **2** | Packet Too Big | MTU-Information für PMTUD |
| **3** | Time Exceeded | Hop Limit überschritten |
| **4** | Parameter Problem | Fehler im Header |
| **128** | Echo Request | Ping (wie Type 8 bei ICMPv4) |
| **129** | Echo Reply | Ping-Antwort (wie Type 0) |
| **133** | Router Solicitation | Router suchen (NDP) |
| **134** | Router Advertisement | Router antwortet (NDP) |
| **135** | Neighbor Solicitation | MAC-Auflösung (ersetzt ARP) |
| **136** | Neighbor Advertisement | MAC-Antwort (ersetzt ARP) |
| **137** | Redirect | Besserer Router |

### ICMPv6 vs. ICMPv4

| Funktion | ICMPv4 | ICMPv6 |
|----------|--------|--------|
| **Echo Request** | Type 8 | Type 128 |
| **Echo Reply** | Type 0 | Type 129 |
| **Destination Unreachable** | Type 3 | Type 1 |
| **Time Exceeded** | Type 11 | Type 3 |
| **Packet Too Big** | Type 3, Code 4 | Type 2 (eigener Typ!) |
| **ARP-Ersatz** | — | NDP (Type 135, 136) |
| **Router Discovery** | IRDP (optional) | NDP (obligatorisch) |

### Neighbor Discovery Protocol (NDP)

ICMPv6 ersetzt ARP vollständig durch NDP:

![[icmpv6-ndp.png]]
*<span class="fig-id">03-06-05-icmpv6-ndp</span>: NDP MAC-Auflösung – Neighbor Solicitation/Advertisement statt ARP.*

## ICMP und Sicherheit

### Sicherheitsaspekte

> [!warning] Potenzielle Risiken
> - **Ping Flood / Smurf-Attacke** – ICMP-basiertes DDoS
> - **Ping of Death** – übergroße ICMP-Pakete
> - **Netzwerk-Reconnaissance** – Hosts im Netzwerk entdecken
> - **Covert Channels** – Daten in ICMP-Paketen verstecken
> - **ICMP Redirect-Attacken** – Traffic umleiten

**Empfehlungen:**
- Echo Reply nur bei Bedarf erlauben
- ICMP Redirect blockieren
- Rate-Limiting für ICMP-Nachrichten
- ICMP für PMTUD erlauben (Type 3, Code 4)
- Source Quench ignorieren (deprecated)

**NICHT blockieren:**
- Type 3, Code 4 (Fragmentation Needed) → PMTUD funktioniert sonst nicht!
- Type 11 (Time Exceeded) → Traceroute benötigt diese Antworten
- ICMPv6 generell → NDP ist essentiell für IPv6!

> [!warning] ICMPv6 nicht blockieren!
> Anders als bei IPv4 ist ICMPv6 **essentiell** für die Funktion von IPv6:
> - NDP ersetzt ARP → Ohne ICMPv6 keine MAC-Auflösung
> - SLAAC benötigt Router Advertisement
> - PMTUD erfordert "Packet Too Big"

## Diagnose-Tools

| Tool | Funktion | ICMP-Typen |
|------|----------|------------|
| **ping** | Erreichbarkeit testen | Echo Request/Reply |
| **traceroute/tracert** | Route ermitteln | Time Exceeded, Echo |
| **pathping** (Windows) | Kombination ping + tracert | Echo, Time Exceeded |
| **mtr** (Linux) | Kontinuierliches Traceroute | Echo, Time Exceeded |

## Nützliche ICMP-Befehle

> [!info] Ping mit Optionen
> ```bash
> # Linux
> ping -c 5 google.com              # 5 Pakete senden
> ping -i 0.2 google.com            # Intervall 0.2 Sekunden
> ping -s 1472 google.com           # Paketgröße (MTU-Test)
> ping -t 10 google.com             # TTL auf 10 setzen
> ping -f google.com                # Flood-Ping (root, Vorsicht!)
> 
> # Windows
> ping -n 5 google.com              # 5 Pakete senden
> ping -t google.com                # Endlos-Ping (Strg+C stoppt)
> ping -l 1472 google.com           # Paketgröße
> ping -i 10 google.com             # TTL auf 10 setzen
> ```

> [!info] Traceroute mit Optionen
> ```bash
> # Linux
> traceroute google.com             # UDP-basiert (Standard)
> traceroute -I google.com          # ICMP-basiert
> traceroute -T google.com          # TCP-basiert (Port 80)
> traceroute -n google.com          # Keine DNS-Auflösung
> traceroute -m 15 google.com       # Max. 15 Hops
> mtr google.com                    # Kontinuierlich mit Statistik
> mtr -r -c 10 google.com           # Report-Modus, 10 Zyklen
> 
> # Windows
> tracert google.com                # ICMP-basiert
> tracert -d google.com             # Keine DNS-Auflösung
> tracert -h 15 google.com          # Max. 15 Hops
> pathping google.com               # Ausführliche Analyse
> ```

> [!info] MTU und Path MTU Discovery testen
> ```bash
> # Linux - MTU finden (1472 + 28 Byte Header = 1500 MTU)
> ping -M do -s 1472 google.com     # -M do = Don't Fragment
> 
> # Windows - MTU finden
> ping -f -l 1472 google.com        # -f = Don't Fragment
> 
> # Bei "Packet needs to be fragmented" → Größe reduzieren
> ```

> [!info] ICMP-Traffic analysieren
> ```bash
> # Linux (mit tcpdump)
> tcpdump -i eth0 icmp              # Alle ICMP-Pakete
> tcpdump -i eth0 'icmp[icmptype] = icmp-echo'  # Nur Echo Request
> 
> # Mit Wireshark (beide Systeme)
> # Filter: icmp oder icmpv6
> ```

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - ICMP-Nachrichtentypen (Echo, Time Exceeded, Destination Unreachable)
> - Wie funktioniert Ping? (Type 8 → Type 0)
> - Wie funktioniert Traceroute? (TTL-Trick)
> - Unterschied ICMPv4 vs. ICMPv6
> - Warum ist ICMPv6 wichtiger als ICMPv4? (NDP)

> [!question] Typische Prüfungsfragen
> - Welche ICMP-Typen werden bei Ping verwendet?
> - Wie ermittelt Traceroute den Pfad durch das Netzwerk?
> - Was passiert, wenn der TTL-Wert eines Pakets auf 0 fällt?
> - Warum ist ICMPv6 für IPv6-Netzwerke essentiell?
> - Welche Funktion übernimmt NDP in IPv6?

### Merkregeln

> [!tip] Merkhilfe: ICMP-Typen
> - **Type 0** = Echo Reply (Antwort)
> - **Type 3** = Destination Unreachable
> - **Type 8** = Echo Request (Ping)
> - **Type 11** = Time Exceeded (TTL=0)
>
> **ICMPv6:** Type-Nummern sind anders!
> - Echo Request = **128** (nicht 8)
> - Echo Reply = **129** (nicht 0)

## Zusammenhänge

- [[01-IP-Protokoll]] - ICMP wird in IP gekapselt
- [[03-IPv6]] - ICMPv6 und NDP
- [[02-Routing]] - ICMP Redirect
- [[03-IPv6#Fragmentierung: IPv4 vs. IPv6|Fragmentierung]] - PMTUD nutzt ICMP

## Quellen

- [[A-RFC-Index#RFC 792|RFC 792]] - ICMP (IPv4)
- [[A-RFC-Index#RFC 4443|RFC 4443]] - ICMPv6
- [[A-RFC-Index#RFC 4861|RFC 4861]] - Neighbor Discovery Protocol
- [[A-RFC-Index#RFC 1191|RFC 1191]] - Path MTU Discovery

