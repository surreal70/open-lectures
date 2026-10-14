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

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Zweck von DHCP verstehen (automatische Netzwerkkonfiguration)
> - Den DORA-Prozess (Discover, Offer, Request, Acknowledge) erklären können
> - Die Lease-Verwaltung mit T1 und T2 verstehen
> - Die wichtigsten DHCP-Optionen kennen
> - DHCP-Relay und dessen Notwendigkeit verstehen
> - Sicherheitsrisiken (Starvation, Rogue Server) und Gegenmaßnahmen kennen
> - Den Unterschied zwischen DHCPv4 und DHCPv6/SLAAC verstehen

---

## Das Problem: Manuelle Konfiguration skaliert nicht

> [!important] **Kernkonzept**
> Das **Dynamic Host Configuration Protocol (DHCP)** automatisiert die Netzwerkkonfiguration von Endgeräten. Es vergibt IP-Adressen, Subnetzmasken, Default Gateways, DNS-Server und weitere Parameter dynamisch an Clients – ohne manuelle Konfiguration jedes einzelnen Geräts.

### Warum ist DHCP notwendig?

Ohne DHCP müsste jedes Gerät manuell konfiguriert werden:

```
┌─────────────────────────────────────────────────────────────────┐
│              Das Konfigurationsproblem                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Ohne DHCP:                                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Jedes Gerät manuell konfigurieren                     │  │
│   │ • IP-Adressen manuell vergeben und dokumentieren       │  │
│   │ • Bei Änderungen: alle Geräte anfassen                 │  │
│   │ • Fehleranfällig: Tippfehler, Duplikate                │  │
│   │ • Hoher Administrationsaufwand                          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Mit DHCP:                                                     │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Gerät anschließen → automatisch konfiguriert         │  │
│   │ • Zentrale Verwaltung aller IP-Parameter               │  │
│   │ • Änderungen nur am Server → alle Clients aktualisiert │  │
│   │ • Keine Duplikate möglich                               │  │
│   │ • Skaliert auf tausende Geräte                         │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!example] **Analogie: Hotel-Rezeption**
> - Du kommst in ein Hotel (= Netzwerk) und brauchst ein Zimmer (= IP-Adresse)
> - Die **Rezeption** (= DHCP-Server) weist dir ein freies Zimmer zu
> - Du bekommst einen **Schlüssel** (= vollständige Netzwerkkonfiguration)
> - Das Zimmer ist für deine **Aufenthaltsdauer reserviert** (= Lease-Zeit)
> - Beim Auschecken wird das Zimmer wieder **freigegeben** (= Release)

---

## DHCP im Protokollstapel

> [!info] **Schichtzuordnung**
> DHCP ist ein **Layer 7-Protokoll** (Anwendungsschicht), das auf UDP aufsetzt. Es hat jedoch eine Besonderheit: Es muss funktionieren, **bevor** der Client eine IP-Adresse hat. Deshalb nutzt es Broadcast auf Layer 2/3 mit den speziellen Adressen 0.0.0.0 (Quelle) und 255.255.255.255 (Ziel).

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

### Portnummern

| Protokoll | Port | Verwendung |
|-----------|------|------------|
| UDP | **67** | DHCP-Server (IPv4) / Relay Agent |
| UDP | **68** | DHCP-Client (IPv4) |
| UDP | **547** | DHCPv6-Server / Relay Agent |
| UDP | **546** | DHCPv6-Client |

---

## DORA-Prozess

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

---

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

---

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

---

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
| **yiaddr** | 4 | "Your" IP (vom Server angeboten) |
| **giaddr** | 4 | Gateway/Relay IP |
| **chaddr** | 16 | Client Hardware Address (MAC) |

---

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

---

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

---

## DHCPv6

DHCPv6 unterscheidet sich von DHCPv4:

| Aspekt | DHCPv4 | DHCPv6 |
|--------|--------|--------|
| **Ports** | 67/68 UDP | 546/547 UDP |
| **Adressen** | Broadcast | Multicast (ff02::1:2) |
| **Nachrichten** | DISCOVER, OFFER, REQUEST, ACK | SOLICIT, ADVERTISE, REQUEST, REPLY |
| **Alternative** | Keine | SLAAC (Stateless) |

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

---

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

| Maßnahme | Beschreibung |
|----------|--------------|
| **DHCP Snooping** | Switch lernt legitime DHCP-Server, blockiert andere |
| **Port Security** | Begrenzt MAC-Adressen pro Port |
| **Rate Limiting** | Begrenzt DHCP-Nachrichten pro Zeiteinheit |
| **802.1X** | Authentifizierung vor Netzwerkzugang |
| **IP Source Guard** | Blockiert Traffic mit gefälschter Quell-IP |

---

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
> ```

---

## Zusammenhänge

```mermaid
graph LR
    A[DHCP] --> B[IP-Adresse]
    A --> C[DNS-Server]
    A --> D[Default Gateway]
    A --> E[NTP-Server]
    A --> F[ARP]
    B --> G[Netzwerkschicht]
    C --> H[Namensauflösung]
    F --> I[Duplicate Detection]
```

- [[01-ARP|ARP]] → DHCP nutzt ARP für Duplicate Address Detection
- [[03-DNS|DNS]] → DNS-Server-Adressen werden via DHCP verteilt
- [[04-NTP|NTP]] → NTP-Server können via DHCP verteilt werden
- [[06-NDP|NDP]] → IPv6 Alternative: SLAAC via Router Advertisement

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - DORA-Prozess (Discover, Offer, Request, Acknowledge)
> - Warum ist DHCPREQUEST ein Broadcast?
> - Lease-Konzept (T1 = 50%, T2 = 87.5%)
> - DHCP-Relay: Warum nötig? Wie funktioniert es?
> - Wichtige DHCP-Optionen (1, 3, 6, 51, 53)
> - Sicherheitsrisiken (Starvation, Rogue Server)

> [!question] **Häufige Prüfungsfragen**
> 1. Beschreiben Sie den DORA-Prozess.
> 2. Was passiert, wenn T1 erreicht wird und der ursprüngliche Server nicht antwortet?
> 3. Warum kann ein DHCP-Server nicht in einem anderen Subnetz stehen (ohne Relay)?
> 4. Wie schützt DHCP Snooping vor Rogue-Servern?
> 5. Was ist der Unterschied zwischen DHCPv4 und SLAAC?

> [!tip] **Merkhilfen**
> - **D**iscover = "**D**arf ich eine IP haben?"
> - **O**ffer = "**O**k, hier ist ein Angebot"
> - **R**equest = "**R**eserviere mir diese IP"
> - **A**ck = "**A**lles klar, sie gehört dir"
> - **Port 67** = Server, **Port 68** = Client (aufsteigend)
> - **T1 = 50%**, **T2 = 87.5%** (Renewal, Rebind)

---

## Weiterführende Ressourcen

> [!note] **RFC und Standards**
> - [[A-RFC-Index#RFC 2131|RFC 2131]] - Dynamic Host Configuration Protocol
> - [[A-RFC-Index#RFC 2132|RFC 2132]] - DHCP Options and BOOTP Vendor Extensions
> - [[A-RFC-Index#RFC 8415|RFC 8415]] - DHCPv6

> [!tip] **Praktische Tools**
> - **Wireshark** → DHCP-Traffic analysieren (Filter: `bootp` oder `dhcp`)
> - **dhcpdump** → DHCP-Pakete im Klartext anzeigen
> - **dnsmasq** → Einfacher DHCP-Server für Tests

---

## Quellen

- Tanenbaum, Andrew S.: Computernetzwerke – Die Standardreferenz für Netzwerkprotokolle mit detaillierter Beschreibung von DHCP und anderen Basisdiensten.
- Kurose, Ross: Computernetze – Ein Top-Down-Ansatz – Didaktisch aufbereitete Darstellung der Anwendungsschicht-Protokolle.
- RFC 2131 – Dynamic Host Configuration Protocol – Die maßgebliche Spezifikation für DHCPv4.
