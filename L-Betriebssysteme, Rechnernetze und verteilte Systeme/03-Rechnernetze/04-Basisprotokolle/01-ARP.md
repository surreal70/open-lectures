---
author: Andreas Hümmer
title: ARP - Address Resolution Protocol
tags:
  - content
  - rn
  - protokolle
  - arp
  - layer2
  - mac
  - adressauflösung
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# ARP – Address Resolution Protocol

## Definition

Das **Address Resolution Protocol (ARP)** löst IP-Adressen in MAC-Adressen auf. Es ist die essenzielle Brücke zwischen Layer 3 (Netzwerkschicht/IP) und Layer 2 (Sicherungsschicht/Ethernet) und ermöglicht die Kommunikation im lokalen Netzwerk.

> [!info] Schichtzuordnung
> ARP arbeitet auf **Layer 2/3** – es nutzt Ethernet-Frames (Layer 2) zur Übertragung, löst aber IP-Adressen (Layer 3) auf. Im IP-Header wird ARP nicht als Protokoll geführt, da es direkt in Ethernet gekapselt wird (EtherType: 0x0806).

## Einordnung im Protokollstapel

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARP im Protokollstapel                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Netzwerkschicht (Layer 3)                  │   │
│   │                       IP                                 │   │
│   │   "Ich will an 192.168.1.20 senden"                     │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                       ARP                                │   │
│   │   "Welche MAC-Adresse hat 192.168.1.20?"                │   │
│   │   Antwort: "00:1A:2B:3C:4D:5E"                          │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Sicherungsschicht (Layer 2)                │   │
│   │                    Ethernet                              │   │
│   │   Ziel-MAC: 00:1A:2B:3C:4D:5E                           │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Warum ist ARP notwendig?

```
┌─────────────────────────────────────────────────────────────────┐
│              Das Problem: IP kennt keine MAC-Adressen          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Anwendung will Daten an 192.168.1.20 senden                  │
│                                                                  │
│   IP-Schicht:   "Ziel-IP: 192.168.1.20" ✓                      │
│   Ethernet:     "Ziel-MAC: ???"         ✗                      │
│                                                                  │
│   ──────────────────────────────────────────────────────────   │
│                                                                  │
│   Problem: Switches arbeiten mit MAC-Adressen!                  │
│   Ohne MAC-Adresse kann das Paket nicht zugestellt werden.     │
│                                                                  │
│   Lösung: ARP fragt im Netzwerk nach der MAC-Adresse           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## ARP-Ablauf

> [!info] RFC-Referenz
> ARP ist definiert in [[A-RFC-Index#RFC 826|RFC 826]] (1982).

### ARP Request und Reply

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARP Request/Reply                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Host A                      Switch                  Host B    │
│   192.168.1.10                                    192.168.1.20  │
│   AA:AA:AA:AA:AA:AA                              BB:BB:BB:BB:..│
│       │                                               │         │
│       │                                               │         │
│       │  1. ARP Request (Broadcast)                   │         │
│       │     Ziel-MAC: FF:FF:FF:FF:FF:FF              │         │
│       │     "Wer hat IP 192.168.1.20?                │         │
│       │      Sagt es 192.168.1.10"                    │         │
│       │───────────────────────────────────────────────┼────────>│
│       │               (an alle Ports)                 │         │
│       │                                               │         │
│       │  2. ARP Reply (Unicast)                       │         │
│       │     Ziel-MAC: AA:AA:AA:AA:AA:AA              │         │
│       │     "192.168.1.20 ist bei BB:BB:BB:BB:BB:BB" │         │
│       │<──────────────────────────────────────────────┼─────────│
│       │                                               │         │
│       │  3. Kommunikation möglich                     │         │
│       │     IP-Paket mit korrekter Ziel-MAC          │         │
│       │───────────────────────────────────────────────┼────────>│
│       │                                               │         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Detaillierter Ablauf

1. **Host A** will ein IP-Paket an **192.168.1.20** senden
2. Host A prüft den **ARP-Cache** – Eintrag nicht vorhanden
3. Host A sendet **ARP Request** als **Broadcast** (FF:FF:FF:FF:FF:FF)
4. **Alle Hosts** im Netzwerk empfangen den Request
5. Nur **Host B** (192.168.1.20) antwortet mit **ARP Reply** (Unicast)
6. Host A speichert die Zuordnung im **ARP-Cache**
7. Host A kann nun das IP-Paket mit korrekter Ziel-MAC senden

## ARP-Paketformat

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│         Hardware Type         │         Protocol Type         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│ HW Addr Len   │ Proto Addr Len│           Operation           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    Sender Hardware Address                    │
│                         (6 Bytes MAC)                         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    Sender Protocol Address                    │
│                         (4 Bytes IP)                          │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    Target Hardware Address                    │
│                         (6 Bytes MAC)                         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    Target Protocol Address                    │
│                         (4 Bytes IP)                          │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Feld | Bytes | Wert (Ethernet/IPv4) | Beschreibung |
|------|-------|---------------------|--------------|
| **Hardware Type** | 2 | 0x0001 | Ethernet |
| **Protocol Type** | 2 | 0x0800 | IPv4 |
| **HW Addr Len** | 1 | 6 | MAC-Adresse = 6 Bytes |
| **Proto Addr Len** | 1 | 4 | IPv4-Adresse = 4 Bytes |
| **Operation** | 2 | 1 oder 2 | 1 = Request, 2 = Reply |
| **Sender HW Addr** | 6 | MAC | MAC des Absenders |
| **Sender Proto Addr** | 4 | IP | IP des Absenders |
| **Target HW Addr** | 6 | MAC/00:00:... | MAC des Ziels (bei Request: 00:00:00:00:00:00) |
| **Target Proto Addr** | 4 | IP | IP des Ziels |

### Ethernet-Frame mit ARP

```
┌─────────────────────────────────────────────────────────────────┐
│                    Ethernet-Frame mit ARP                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────┬──────────┬───────────┬─────────────┬─────────┐  │
│   │ Dest MAC │ Src MAC  │ EtherType │  ARP-Paket  │   FCS   │  │
│   │ 6 Bytes  │ 6 Bytes  │  2 Bytes  │  28 Bytes   │ 4 Bytes │  │
│   └──────────┴──────────┴───────────┴─────────────┴─────────┘  │
│                                                                  │
│   ARP Request:  Dest MAC = FF:FF:FF:FF:FF:FF (Broadcast)       │
│   ARP Reply:    Dest MAC = MAC des ursprünglichen Anfragenden  │
│                                                                  │
│   EtherType für ARP: 0x0806                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## ARP-Cache

Der ARP-Cache speichert gelernte IP-MAC-Zuordnungen, um wiederholte ARP-Anfragen zu vermeiden.

### Cache-Einträge

| Typ | Beschreibung | Timeout |
|-----|--------------|---------|
| **Dynamisch** | Durch ARP gelernt | Typisch 2-20 Minuten |
| **Statisch** | Manuell konfiguriert | Kein Timeout |
| **Incomplete** | ARP Request gesendet, keine Antwort | Kurz (wenige Sekunden) |

### Kommandos

> [!example] ARP-Cache anzeigen
> 
> **Linux:**
> ```bash
> $ ip neigh show
> 192.168.1.1 dev eth0 lladdr 00:1a:2b:3c:4d:5e REACHABLE
> 192.168.1.20 dev eth0 lladdr aa:bb:cc:dd:ee:ff STALE
> 
> $ arp -a
> gateway (192.168.1.1) at 00:1a:2b:3c:4d:5e [ether] on eth0
> ```
> 
> **Windows:**
> ```cmd
> C:\> arp -a
> Schnittstelle: 192.168.1.10 --- 0x5
>   Internetadresse       Physische Adresse     Typ
>   192.168.1.1           00-1a-2b-3c-4d-5e     dynamisch
>   192.168.1.20          aa-bb-cc-dd-ee-ff     dynamisch
> ```

### Cache-Zustände (Linux)

| Zustand | Bedeutung |
|---------|-----------|
| **REACHABLE** | Kürzlich bestätigt, verwendbar |
| **STALE** | Veraltet, wird bei nächster Nutzung neu geprüft |
| **DELAY** | Warte auf Bestätigung |
| **PROBE** | Sende ARP zur Bestätigung |
| **FAILED** | Keine Antwort erhalten |

## ARP-Varianten

### Gratuitous ARP

```
┌─────────────────────────────────────────────────────────────────┐
│                    Gratuitous ARP                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Host sendet ARP Request für seine EIGENE IP-Adresse          │
│                                                                  │
│   Sender IP:  192.168.1.10                                      │
│   Target IP:  192.168.1.10   ← Gleich!                         │
│                                                                  │
│   Verwendungszwecke:                                            │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ 1. Duplicate Address Detection (DAD)                    │  │
│   │    → Prüft, ob IP bereits vergeben ist                  │  │
│   │                                                          │  │
│   │ 2. ARP-Cache-Update bei anderen Hosts                   │  │
│   │    → Aktualisiert Einträge nach MAC-Änderung           │  │
│   │                                                          │  │
│   │ 3. Failover-Szenarien (VRRP, HSRP)                      │  │
│   │    → Neuer Master übernimmt IP                          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Proxy ARP

```
┌─────────────────────────────────────────────────────────────────┐
│                    Proxy ARP                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Netz A                    Router                    Netz B    │
│   192.168.1.0/24                                 192.168.2.0/24 │
│                                                                  │
│   Host A                                              Host B    │
│   192.168.1.10                                    192.168.2.20  │
│       │                                               │         │
│       │  ARP Request: "Wer hat 192.168.2.20?"        │         │
│       │─────────────────────────>│                    │         │
│       │                          │                    │         │
│       │  ARP Reply mit           │                    │         │
│       │  ROUTER-MAC!             │                    │         │
│       │<─────────────────────────│                    │         │
│       │                          │                    │         │
│       │                          │                    │         │
│   Host A denkt: "192.168.2.20 ist direkt erreichbar"           │
│   → Sendet an Router-MAC, Router leitet weiter                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!warning] Proxy ARP
> Proxy ARP ermöglicht Kommunikation über Subnetzgrenzen ohne explizites Routing auf dem Client. Es wird heute selten verwendet und kann Sicherheitsrisiken bergen.

### RARP (Reverse ARP)

**Historisches Protokoll** – löste MAC-Adressen in IP-Adressen auf (für disklose Workstations).

```
RARP: "Ich habe MAC AA:BB:CC:DD:EE:FF – welche IP habe ich?"
```

> [!info] Veraltet
> RARP wurde durch **BOOTP** und später **DHCP** ersetzt, die deutlich mehr Konfigurationsmöglichkeiten bieten.

## Sicherheit

### ARP-Spoofing / ARP-Poisoning

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARP-Spoofing-Angriff                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Opfer A         Angreifer          Gateway                    │
│   192.168.1.10    192.168.1.99       192.168.1.1                │
│       │               │                   │                     │
│       │               │                   │                     │
│       │  Gefälschte ARP Replies          │                     │
│       │◄──────────────│                   │                     │
│       │  "192.168.1.1 ist bei            │                     │
│       │   ANGREIFER-MAC"                  │                     │
│       │               │                   │                     │
│       │               │──────────────────►│                     │
│       │               │  "192.168.1.10    │                     │
│       │               │   ist bei         │                     │
│       │               │   ANGREIFER-MAC"  │                     │
│       │               │                   │                     │
│       │                                   │                     │
│       │──────────────►│──────────────────►│                     │
│       │    Traffic    │    Traffic        │                     │
│       │  (abgehört!)  │  (weitergeleitet) │                     │
│       │               │                   │                     │
│                                                                  │
│   → Man-in-the-Middle: Angreifer sieht allen Traffic!          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Angriffsszenarien

| Angriff | Beschreibung |
|---------|--------------|
| **Man-in-the-Middle** | Abfangen und Mitlesen des Traffics |
| **DoS (Denial of Service)** | Umleiten von Traffic ins Nichts |
| **Session Hijacking** | Übernahme aktiver Verbindungen |
| **DNS-Spoofing** | Kombination mit gefälschten DNS-Antworten |

### Gegenmaßnahmen

```
┌─────────────────────────────────────────────────────────────────┐
│              Schutzmaßnahmen gegen ARP-Spoofing                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Dynamic ARP Inspection (DAI)                               │
│     → Switch prüft ARP-Pakete gegen DHCP-Snooping-Datenbank   │
│                                                                  │
│   ✓ Static ARP Entries                                         │
│     → Manuelle MAC-IP-Zuordnung für kritische Hosts           │
│     → Skaliert nicht gut                                       │
│                                                                  │
│   ✓ Port Security                                              │
│     → Begrenzt MAC-Adressen pro Switch-Port                   │
│                                                                  │
│   ✓ Private VLANs                                              │
│     → Isoliert Hosts im gleichen VLAN                          │
│                                                                  │
│   ✓ 802.1X (Port-based Network Access Control)                 │
│     → Authentifizierung vor Netzwerkzugriff                    │
│                                                                  │
│   ✓ VPN / Verschlüsselung                                      │
│     → Selbst bei MITM sind Daten verschlüsselt                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!example] Statischen ARP-Eintrag setzen
> 
> **Linux:**
> ```bash
> $ sudo ip neigh add 192.168.1.1 lladdr 00:1a:2b:3c:4d:5e dev eth0 nud permanent
> ```
> 
> **Windows:**
> ```cmd
> C:\> netsh interface ip add neighbors "Ethernet" 192.168.1.1 00-1a-2b-3c-4d-5e
> ```

## ARP vs. NDP (IPv6)

| Aspekt | ARP (IPv4) | NDP (IPv6) |
|--------|------------|------------|
| **Transportmethode** | Eigenes Protokoll (EtherType 0x0806) | ICMPv6 (Type 135/136) |
| **Request** | Broadcast (FF:FF:FF:FF:FF:FF) | Multicast (Solicited-Node) |
| **Sicherheit** | Keine eingebaute | SEND (optional) |
| **Zusatzfunktionen** | Nur Adressauflösung | + Router Discovery, SLAAC, DAD |
| **Effizienz** | Alle Hosts empfangen Broadcast | Nur relevante Hosts |

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. ARP-Ablauf (Request als Broadcast, Reply als Unicast)
> 2. Warum ist ARP notwendig? (Brücke L2/L3)
> 3. ARP-Paketformat (Operation: 1=Request, 2=Reply)
> 4. ARP-Cache und Timeouts
> 5. ARP-Spoofing als Sicherheitsrisiko
> 6. Unterschied ARP vs. NDP

### Typische Prüfungsfragen

> [!question] Übungsfragen
> 1. Warum wird ein ARP-Request als Broadcast gesendet?
> 2. Warum wird ein ARP-Reply als Unicast gesendet?
> 3. Was passiert, wenn der Zielhost in einem anderen Subnetz ist?
> 4. Wie kann ein Angreifer ARP-Spoofing durchführen?
> 5. Welche Gegenmaßnahmen gibt es?

### Merkhilfen

> [!tip] Merkregel: ARP-Ablauf
> - **Request** = **Broadcast** ("Ich frage alle")
> - **Reply** = **Unicast** ("Ich antworte direkt")
> - **Cache** = **Speicher** ("Damit ich nicht nochmal fragen muss")

## Zusammenfassung

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARP auf einen Blick                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zweck:      IP-Adresse → MAC-Adresse auflösen                │
│   Schicht:    Layer 2/3 (zwischen IP und Ethernet)             │
│   Standard:   RFC 826 (1982)                                   │
│   EtherType:  0x0806                                           │
│                                                                  │
│   Ablauf:                                                       │
│   1. ARP Request (Broadcast) - "Wer hat IP X?"                 │
│   2. ARP Reply (Unicast) - "Ich habe IP X, meine MAC ist Y"    │
│   3. Speichern im ARP-Cache                                    │
│                                                                  │
│   Varianten:  Gratuitous ARP, Proxy ARP, RARP (veraltet)       │
│   Sicherheit: ARP-Spoofing → DAI, Static Entries, 802.1X       │
│   IPv6:       Ersetzt durch NDP (Neighbor Discovery Protocol)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Querverweise

- [[../03-Referenzmodelle/05-Sicherungsschicht/02-MAC-Adressen|MAC-Adressen]] – Ziel der Auflösung
- [[../03-Referenzmodelle/06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]] – Quelle der Auflösung
- [[02-DHCP|DHCP]] – Nutzt ARP für Duplicate Address Detection
- [[06-NDP|NDP]] – IPv6-Ersatz für ARP
- [[../05-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] – ARP-Spoofing-Prävention

## Quellen

- [[A-RFC-Index#RFC 826|RFC 826]] - An Ethernet Address Resolution Protocol (1982)
- [[A-RFC-Index#RFC 5227|RFC 5227]] - IPv4 Address Conflict Detection
