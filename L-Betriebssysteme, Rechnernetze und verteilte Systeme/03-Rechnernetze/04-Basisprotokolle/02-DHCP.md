---
author: Andreas Hümmer
title: DHCP - Dynamic Host Configuration Protocol
tags:
  - content
  - rn
  - protokolle
  - dhcp
  - layer3
  - layer7
  - ip-konfiguration
  - netzwerkdienst
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# DHCP – Dynamic Host Configuration Protocol

## Definition

Das **Dynamic Host Configuration Protocol (DHCP)** automatisiert die Netzwerkkonfiguration von Endgeräten. Es vergibt IP-Adressen, Subnetzmasken, Default Gateways, DNS-Server und weitere Parameter dynamisch an Clients.

> [!info] Schichtzuordnung
> DHCP ist ein **Layer 7-Protokoll** (Anwendungsschicht), das auf UDP aufsetzt. Es hat jedoch eine Besonderheit: Es muss funktionieren, **bevor** der Client eine IP-Adresse hat. Deshalb nutzt es Broadcast auf Layer 2/3 mit den speziellen Adressen 0.0.0.0 (Quelle) und 255.255.255.255 (Ziel).

## Einordnung im Protokollstapel

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP im Protokollstapel                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Anwendungsschicht (Layer 7)                │   │
│   │                      DHCP                                │   │
│   │           Client-Port: 68 / Server-Port: 67             │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Transportschicht (Layer 4)                 │   │
│   │                       UDP                                │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Netzwerkschicht (Layer 3)                  │   │
│   │                        IP                                │   │
│   │   Quelle: 0.0.0.0 / Ziel: 255.255.255.255 (Broadcast)  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              Sicherungsschicht (Layer 2)                │   │
│   │                     Ethernet                             │   │
│   │          Ziel-MAC: FF:FF:FF:FF:FF:FF (Broadcast)        │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Portnummern

| Protokoll | Port | Verwendung |
|-----------|------|------------|
| UDP | **67** | DHCP-Server (IPv4) / Relay Agent |
| UDP | **68** | DHCP-Client (IPv4) |
| UDP | **547** | DHCPv6-Server / Relay Agent |
| UDP | **546** | DHCPv6-Client |

> [!tip] Merkregel Ports
> **67** = Server, **68** = Client (aufsteigende Reihenfolge)

## DORA-Prozess

> [!info] RFC-Referenz
> - DHCPv4: [[A-RFC-Index#RFC 2131|RFC 2131]]
> - DHCP-Optionen: [[A-RFC-Index#RFC 2132|RFC 2132]]
> - DHCPv6: [[A-RFC-Index#RFC 8415|RFC 8415]]

Der DHCP-Prozess besteht aus vier Schritten – **DORA**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP DORA-Prozess                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Client                                         DHCP-Server    │
│   (keine IP)                                     192.168.1.1    │
│       │                                               │         │
│       │  ┌─────────────────────────────────────────┐ │         │
│       │  │ 1. DHCPDISCOVER (Broadcast)             │ │         │
│       │  │    Quelle: 0.0.0.0:68                   │ │         │
│       │  │    Ziel: 255.255.255.255:67             │ │         │
│       │  │    "Gibt es einen DHCP-Server?"         │ │         │
│       │──┴─────────────────────────────────────────┴─┼────────>│
│       │                                               │         │
│       │  ┌─────────────────────────────────────────┐ │         │
│       │  │ 2. DHCPOFFER (Broadcast/Unicast)        │ │         │
│       │  │    "Ich biete dir 192.168.1.100 an"     │ │         │
│       │  │    Lease: 24 Stunden                    │ │         │
│       │<─┴─────────────────────────────────────────┴─┼─────────│
│       │                                               │         │
│       │  ┌─────────────────────────────────────────┐ │         │
│       │  │ 3. DHCPREQUEST (Broadcast)              │ │         │
│       │  │    "Ich nehme das Angebot von           │ │         │
│       │  │     Server 192.168.1.1 an"              │ │         │
│       │──┴─────────────────────────────────────────┴─┼────────>│
│       │                                               │         │
│       │  ┌─────────────────────────────────────────┐ │         │
│       │  │ 4. DHCPACK (Broadcast/Unicast)          │ │         │
│       │  │    "Bestätigt! Deine IP ist             │ │         │
│       │  │     192.168.1.100 für 24h"              │ │         │
│       │<─┴─────────────────────────────────────────┴─┼─────────│
│       │                                               │         │
│   Client hat jetzt:                                   │         │
│   • IP: 192.168.1.100                                │         │
│   • Subnet: 255.255.255.0                            │         │
│   • Gateway: 192.168.1.1                             │         │
│   • DNS: 8.8.8.8                                     │         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Die vier DORA-Schritte im Detail

| Schritt | Name | Richtung | Übertragung | Beschreibung |
|---------|------|----------|-------------|--------------|
| **D** | DHCPDISCOVER | Client → Server | Broadcast | Client sucht DHCP-Server |
| **O** | DHCPOFFER | Server → Client | Broadcast/Unicast | Server bietet IP an |
| **R** | DHCPREQUEST | Client → Server | Broadcast | Client akzeptiert Angebot |
| **A** | DHCPACK | Server → Client | Broadcast/Unicast | Server bestätigt |

> [!question] Warum ist DHCPREQUEST ein Broadcast?
> Der Client sendet DHCPREQUEST als **Broadcast**, damit **alle** DHCP-Server im Netzwerk erfahren, welchen Server der Client gewählt hat. Die nicht gewählten Server können ihre Angebote dann zurücknehmen.

## Weitere DHCP-Nachrichten

| Nachricht | Richtung | Beschreibung |
|-----------|----------|--------------|
| **DHCPNAK** | Server → Client | Server lehnt Request ab (IP nicht mehr verfügbar) |
| **DHCPDECLINE** | Client → Server | Client lehnt ab (IP bereits in Verwendung - ARP-Test) |
| **DHCPRELEASE** | Client → Server | Client gibt IP vorzeitig frei |
| **DHCPINFORM** | Client → Server | Client hat statische IP, fragt nur nach Optionen |

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP-Nachrichtenübersicht                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Normaler Ablauf:    D → O → R → A                            │
│                                                                  │
│   Fehlerfall:         D → O → R → NAK (Server lehnt ab)        │
│                                                                  │
│   IP-Konflikt:        D → O → R → A → DECLINE (Client)         │
│                                                                  │
│   Vorzeitige Freigabe: RELEASE (Client gibt IP zurück)         │
│                                                                  │
│   Nur Optionen:       INFORM (Client hat statische IP)         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Lease-Verwaltung

Die IP-Adresse wird für eine **Lease-Zeit** vergeben – nicht dauerhaft.

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP Lease-Zeitleiste                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Lease Start                                      Lease Ende   │
│       │                                               │         │
│       │         T1 (50%)           T2 (87.5%)        │         │
│       │            │                   │              │         │
│       ├────────────┼───────────────────┼──────────────┤         │
│       │            │                   │              │         │
│       │  Normale   │  Renewal-Phase    │  Rebind-    │         │
│       │  Nutzung   │  (Unicast an      │  Phase      │         │
│       │            │   ursprünglichen  │  (Broadcast │         │
│       │            │   Server)         │   an alle)  │         │
│       │            │                   │              │         │
│                                                                  │
│   Bei Lease = 24h:                                              │
│   • T1 = 12h  → Renewal-Versuch (Unicast)                      │
│   • T2 = 21h  → Rebind-Versuch (Broadcast)                     │
│   • 24h       → Lease abgelaufen, IP muss aufgegeben werden    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Lease-Erneuerung

| Zeitpunkt | Name | Verhalten |
|-----------|------|-----------|
| **T1 (50%)** | Renewal | Client sendet DHCPREQUEST direkt an ursprünglichen Server |
| **T2 (87.5%)** | Rebinding | Client sendet DHCPREQUEST als Broadcast an alle Server |
| **100%** | Lease Expired | Client **muss** IP aufgeben, startet DORA neu |

> [!tip] Typische Lease-Zeiten
> - **Unternehmensnetz**: 8-24 Stunden
> - **Heimnetz**: 24 Stunden bis 7 Tage
> - **Öffentliches WLAN**: 1-4 Stunden
> - **Mobilfunk**: Oft unbegrenzt (Carrier-Grade NAT)

## DHCP-Paketformat

DHCP basiert auf dem älteren **BOOTP**-Format:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│     op (1)    │   htype (1)   │   hlen (1)    │   hops (1)    │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                            xid (4)                            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│           secs (2)            │           flags (2)           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          ciaddr (4)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          yiaddr (4)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          siaddr (4)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          giaddr (4)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          chaddr (16)                          │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          sname (64)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                          file (128)                           │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    options (variable)                         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Feld | Bytes | Beschreibung |
|------|-------|--------------|
| **op** | 1 | Operation: 1 = Request (Client), 2 = Reply (Server) |
| **htype** | 1 | Hardware-Typ: 1 = Ethernet |
| **hlen** | 1 | Hardware-Adresslänge: 6 (MAC) |
| **hops** | 1 | Relay-Hop-Count |
| **xid** | 4 | Transaction ID (zufällig, zur Zuordnung) |
| **secs** | 2 | Sekunden seit DHCP-Start |
| **flags** | 2 | Flags (Bit 0: Broadcast-Flag) |
| **ciaddr** | 4 | Client IP (falls bekannt) |
| **yiaddr** | 4 | "Your" IP (vom Server angeboten) |
| **siaddr** | 4 | Server IP |
| **giaddr** | 4 | Gateway/Relay IP |
| **chaddr** | 16 | Client Hardware Address (MAC) |
| **sname** | 64 | Server Hostname (optional) |
| **file** | 128 | Boot-Dateiname (PXE) |
| **options** | var | DHCP-Optionen |

## DHCP-Optionen

DHCP-Optionen transportieren die eigentlichen Konfigurationsparameter:

| Option | Name | Beschreibung |
|--------|------|--------------|
| **1** | Subnet Mask | z.B. 255.255.255.0 |
| **3** | Router | Default Gateway |
| **6** | DNS Server | DNS-Server-Adressen |
| **15** | Domain Name | z.B. "firma.local" |
| **42** | NTP Server | Zeitserver |
| **51** | Lease Time | Gültigkeitsdauer in Sekunden |
| **53** | Message Type | DISCOVER, OFFER, REQUEST, ACK, etc. |
| **54** | Server Identifier | IP des DHCP-Servers |
| **55** | Parameter Request | Vom Client gewünschte Optionen |
| **61** | Client Identifier | Eindeutige Client-ID |
| **66** | TFTP Server | Für PXE-Boot |
| **67** | Bootfile Name | Für PXE-Boot |

> [!example] DHCP-Optionen im Wireshark
> ```
> Option: (53) DHCP Message Type (Discover)
> Option: (55) Parameter Request List
>     Parameter Request List Item: (1) Subnet Mask
>     Parameter Request List Item: (3) Router
>     Parameter Request List Item: (6) Domain Name Server
>     Parameter Request List Item: (15) Domain Name
> Option: (61) Client identifier
>     Hardware type: Ethernet (0x01)
>     Client MAC address: aa:bb:cc:dd:ee:ff
> ```

## DHCP-Relay

Da DHCP Broadcasts verwendet, funktioniert es nur im lokalen Netzwerk. Ein **DHCP-Relay-Agent** leitet Anfragen an Server in anderen Netzen weiter.

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP-Relay-Agent                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Netz A: 192.168.1.0/24          Netz B: 10.0.0.0/24          │
│                                                                  │
│   Client                Router               DHCP-Server        │
│   (keine IP)           (Relay Agent)         10.0.0.5           │
│       │                     │                     │             │
│       │  DISCOVER           │                     │             │
│       │  (Broadcast)        │                     │             │
│       │────────────────────>│                     │             │
│       │                     │                     │             │
│       │                     │  DISCOVER           │             │
│       │                     │  (Unicast)          │             │
│       │                     │  giaddr=192.168.1.1 │             │
│       │                     │────────────────────>│             │
│       │                     │                     │             │
│       │                     │  OFFER              │             │
│       │                     │  (Unicast)          │             │
│       │                     │<────────────────────│             │
│       │                     │                     │             │
│       │  OFFER              │                     │             │
│       │  (Broadcast)        │                     │             │
│       │<────────────────────│                     │             │
│       │                     │                     │             │
│                                                                  │
│   giaddr = Gateway IP Address                                   │
│   → Teilt dem Server mit, aus welchem Netz die Anfrage kam     │
│   → Server wählt passenden IP-Pool für dieses Netz             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!tip] Relay-Konfiguration
> Der Relay-Agent wird oft auf dem Router konfiguriert:
> - **Cisco IOS**: `ip helper-address 10.0.0.5`
> - **Linux (dhcrelay)**: `dhcrelay -i eth0 10.0.0.5`

## DHCPv6

DHCPv6 unterscheidet sich von DHCPv4:

| Aspekt | DHCPv4 | DHCPv6 |
|--------|--------|--------|
| **Ports** | 67/68 UDP | 546/547 UDP |
| **Adressen** | Broadcast | Multicast (ff02::1:2) |
| **Nachrichten** | DISCOVER, OFFER, REQUEST, ACK | SOLICIT, ADVERTISE, REQUEST, REPLY |
| **Alternative** | Keine | SLAAC (Stateless) |
| **Identifier** | MAC-basiert | DUID (DHCP Unique ID) |

### Stateful vs. Stateless

```
┌─────────────────────────────────────────────────────────────────┐
│              DHCPv6: Stateful vs. Stateless                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Stateless (SLAAC + DHCPv6):                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • IP-Adresse: Router Advertisement (SLAAC)              │  │
│   │ • DNS, NTP, etc.: DHCPv6                                │  │
│   │ • Server speichert keine IP-Zuordnungen                 │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Stateful (nur DHCPv6):                                       │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • IP-Adresse: DHCPv6                                    │  │
│   │ • Alle Optionen: DHCPv6                                 │  │
│   │ • Server führt Lease-Datenbank                          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Steuerung über Router Advertisement Flags:                    │
│   • M-Flag (Managed): Stateful DHCPv6 verwenden                │
│   • O-Flag (Other): Zusätzliche Infos per DHCPv6              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Sicherheit

### DHCP-Starvation

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP Starvation Attack                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Angreifer sendet massenhaft DHCPDISCOVER mit                 │
│   gefälschten MAC-Adressen                                     │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ DISCOVER (MAC: AA:...) → Server vergibt IP 1           │  │
│   │ DISCOVER (MAC: BB:...) → Server vergibt IP 2           │  │
│   │ DISCOVER (MAC: CC:...) → Server vergibt IP 3           │  │
│   │ ...                                                      │  │
│   │ DISCOVER (MAC: ZZ:...) → Pool erschöpft!               │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Folge: Legitime Clients bekommen keine IP mehr!              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rogue DHCP Server

```
┌─────────────────────────────────────────────────────────────────┐
│                    Rogue DHCP Server                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Client        Legitimer Server       Rogue Server            │
│      │               │                      │                   │
│      │  DISCOVER     │                      │                   │
│      │───────────────┼──────────────────────┼─────────────>     │
│      │               │                      │                   │
│      │  OFFER        │    OFFER (schneller!)│                   │
│      │◄──────────────│◄─────────────────────│                   │
│      │               │                      │                   │
│      │                                      │                   │
│   Client akzeptiert Rogue-Angebot:         │                   │
│   • Gateway: Angreifer-IP (MITM!)          │                   │
│   • DNS: Angreifer-DNS (Phishing!)         │                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Gegenmaßnahmen

```
┌─────────────────────────────────────────────────────────────────┐
│              DHCP-Sicherheitsmaßnahmen                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ DHCP Snooping (Switch-Feature)                             │
│     → Switch lernt legitime DHCP-Server                        │
│     → Blockiert DHCP-Antworten von nicht-trusted Ports        │
│     → Baut Binding-Tabelle auf (MAC ↔ IP ↔ Port)              │
│                                                                  │
│   ✓ Port Security                                              │
│     → Begrenzt MAC-Adressen pro Port                           │
│     → Verhindert Starvation mit vielen MACs                    │
│                                                                  │
│   ✓ Rate Limiting                                              │
│     → Begrenzt DHCP-Nachrichten pro Zeiteinheit                │
│                                                                  │
│   ✓ 802.1X                                                     │
│     → Authentifizierung vor Netzwerkzugang                     │
│     → Nur autorisierte Geräte erhalten DHCP                    │
│                                                                  │
│   ✓ IP Source Guard                                            │
│     → Nutzt DHCP-Snooping-Tabelle                              │
│     → Blockiert Traffic mit gefälschter Quell-IP              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Praxisbeispiele

> [!example] DHCP-Client-Befehle
> 
> **Linux:**
> ```bash
> # IP erneuern
> $ sudo dhclient -r eth0    # Release
> $ sudo dhclient eth0       # Neue IP anfordern
> 
> # Lease-Informationen anzeigen
> $ cat /var/lib/dhcp/dhclient.leases
> ```
> 
> **Windows:**
> ```cmd
> C:\> ipconfig /release      # IP freigeben
> C:\> ipconfig /renew        # Neue IP anfordern
> C:\> ipconfig /all          # Lease-Infos anzeigen
> 
> DHCP-Server . . . . . . . . : 192.168.1.1
> Lease erhalten. . . . . . . : 13.10.2026 10:00:00
> Lease läuft ab. . . . . . . : 14.10.2026 10:00:00
> ```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. DORA-Prozess (Discover, Offer, Request, Acknowledge)
> 2. Warum ist DHCPREQUEST ein Broadcast?
> 3. Lease-Konzept (T1 = 50%, T2 = 87.5%)
> 4. DHCP-Relay: Warum nötig? Wie funktioniert es?
> 5. Wichtige DHCP-Optionen (1, 3, 6, 51, 53)
> 6. Sicherheitsrisiken (Starvation, Rogue Server)

### Typische Prüfungsfragen

> [!question] Übungsfragen
> 1. Beschreiben Sie den DORA-Prozess.
> 2. Was passiert, wenn T1 erreicht wird und der ursprüngliche Server nicht antwortet?
> 3. Warum kann ein DHCP-Server nicht in einem anderen Subnetz stehen (ohne Relay)?
> 4. Wie schützt DHCP Snooping vor Rogue-Servern?
> 5. Was ist der Unterschied zwischen DHCPv4 und SLAAC?

### Merkhilfen

> [!tip] Merkregel: DORA
> - **D**iscover = "**D**arf ich eine IP haben?"
> - **O**ffer = "**O**k, hier ist ein Angebot"
> - **R**equest = "**R**eserviere mir diese IP"
> - **A**ck = "**A**lles klar, sie gehört dir"

## Zusammenfassung

```
┌─────────────────────────────────────────────────────────────────┐
│                    DHCP auf einen Blick                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zweck:      Automatische Netzwerkkonfiguration               │
│   Schicht:    Layer 7 (UDP), arbeitet mit Layer 2/3 Broadcast  │
│   Standard:   RFC 2131 (DHCPv4), RFC 8415 (DHCPv6)             │
│   Ports:      67 (Server), 68 (Client)                         │
│                                                                  │
│   Ablauf (DORA):                                               │
│   1. Discover (Broadcast) - Client sucht Server                │
│   2. Offer - Server bietet IP an                               │
│   3. Request (Broadcast) - Client akzeptiert                   │
│   4. Acknowledge - Server bestätigt                            │
│                                                                  │
│   Lease:      T1 (50%) → Renewal, T2 (87.5%) → Rebind         │
│   Relay:      Für DHCP über Subnetzgrenzen hinweg             │
│   Optionen:   Subnet, Gateway, DNS, NTP, Domain, etc.         │
│   Sicherheit: DHCP Snooping, Port Security, 802.1X            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Querverweise

- [[01-ARP|ARP]] – DHCP nutzt ARP für Duplicate Address Detection
- [[03-DNS|DNS]] – DNS-Server-Adressen werden via DHCP verteilt
- [[04-NTP|NTP]] – NTP-Server können via DHCP verteilt werden
- [[06-NDP|NDP]] – IPv6 Alternative: SLAAC via Router Advertisement
- [[../03-Referenzmodelle/06-Netzwerkschicht/03-IPv6|IPv6]] – DHCPv6 vs. SLAAC

## Quellen

- [[A-RFC-Index#RFC 2131|RFC 2131]] - Dynamic Host Configuration Protocol
- [[A-RFC-Index#RFC 2132|RFC 2132]] - DHCP Options and BOOTP Vendor Extensions
- [[A-RFC-Index#RFC 8415|RFC 8415]] - DHCPv6
