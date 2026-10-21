---
author: Andreas Hümmer
title: Routing
tags:
  - content
  - rn
  - network-layer
  - routing
  - router
  - wegfindung
  - ospf
  - bgp
created: '2026-10-07'
modified: '2026-10-21'
bereich: RN
---

# Routing

> [!info] Lernziele
> Nach diesem Kapitel können Sie...
> - Den Unterschied zwischen Routing und Switching erklären
> - Statisches und dynamisches Routing unterscheiden
> - Distance-Vector- und Link-State-Protokolle vergleichen
> - Die Funktionsweise von RIP, OSPF und BGP beschreiben
> - Routing-Tabellen interpretieren

## Definition

> [!quote] Definition
> **Routing** ist der Prozess der Wegfindung und Weiterleitung von IP-Paketen durch ein Netzwerk, bei dem Router anhand von Routing-Tabellen die optimale Route zum Ziel bestimmen.
## Grundkonzepte

### Routing vs. Switching

| Aspekt | Switching (Layer 2) | Routing (Layer 3) |
|--------|--------------------|--------------------|
| **Adressierung** | MAC-Adressen | IP-Adressen |
| **Reichweite** | Lokales Netzwerk | Netzwerkübergreifend |
| **Gerät** | Switch | Router |
| **Tabelle** | MAC-Adresstabelle | Routing-Tabelle |
| **Broadcast** | Wird weitergeleitet | Wird blockiert |

### Routing-Entscheidung

![[routing-entscheidung.png]]
*<span class="fig-id">03-03-06-routing-entscheidung</span>: Ablauf einer Routing-Entscheidung im Router.*

## Routing-Tabelle

### Aufbau einer Routing-Tabelle

```shell
Destination     Gateway         Genmask         Flags   Interface
─────────────────────────────────────────────────────────────────
0.0.0.0         192.168.1.1     0.0.0.0         UG      eth0
10.0.0.0        192.168.1.254   255.0.0.0       UG      eth0
192.168.1.0     0.0.0.0         255.255.255.0   U       eth0
192.168.2.0     192.168.1.2     255.255.255.0   UG      eth0
```

### Routing-Tabellen-Einträge

| Feld | Beschreibung |
|------|--------------|
| **Destination** | Zielnetzwerk |
| **Gateway** | Next-Hop-Adresse (0.0.0.0 = direkt verbunden) |
| **Genmask** | Subnetzmaske |
| **Flags** | U=Up, G=Gateway, H=Host |
| **Interface** | Ausgangsschnittstelle |

> [!tip] Longest Prefix Match
> Bei mehreren passenden Routen wird die **spezifischste Route** (längste Subnetzmaske) verwendet.
> - 10.0.0.0/8 vs. 10.1.0.0/16 → /16 gewinnt für 10.1.x.x

## Statisches vs. Dynamisches Routing

### Statisches Routing

Manuell konfigurierte Routen:

```bash
# Linux: Statische Route hinzufügen
ip route add 10.0.0.0/8 via 192.168.1.254
ip route add default via 192.168.1.1      # Default-Route

# Windows: Statische Route hinzufügen
route add 10.0.0.0 mask 255.0.0.0 192.168.1.254
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1 -p    # -p = persistent
```

> [!info] Routing-Tabelle anzeigen
> ```bash
> # Linux
> ip route show             # Alle Routen
> ip route get 8.8.8.8      # Welche Route wird für Ziel verwendet?
> ip -6 route show          # IPv6-Routen
> 
> # Windows
> route print               # Komplette Routing-Tabelle
> route print -4            # Nur IPv4-Routen
> netstat -rn               # Alternative Darstellung
> ```

> [!info] Route verfolgen (Traceroute)
> ```bash
> # Linux
> traceroute google.com     # UDP-basiert (Standard)
> traceroute -I google.com  # ICMP-basiert
> mtr google.com            # Kontinuierliches Traceroute mit Statistiken
> 
> # Windows
> tracert google.com        # ICMP-basiert
> pathping google.com       # Kombination aus ping und tracert
> ```

**Vorteile:**
- Kein Protokoll-Overhead
- Vorhersagbares Verhalten
- Sicherheit (keine Routing-Updates)

**Nachteile:**
- Kein automatisches Failover
- Hoher Administrationsaufwand
- Nicht skalierbar

### Dynamisches Routing

Router tauschen automatisch Routing-Informationen aus:

![[routing-updates.png]]
*<span class="fig-id">03-03-06-routing-updates</span>: Austausch von Routing-Informationen zwischen Routern.*

**Vorteile:**
- Automatische Anpassung bei Änderungen
- Skalierbar
- Redundanz und Load-Balancing

**Nachteile:**
- Protokoll-Overhead
- Konvergenzzeit
- Komplexere Konfiguration

## Routing-Protokoll-Klassifizierung

### Interior vs. Exterior Gateway Protocols

![[igp-egp-struktur.png]]
*<span class="fig-id">03-03-06-igp-egp-struktur</span>: Interior Gateway Protocols (IGP) innerhalb von Autonomous Systems, Exterior Gateway Protocols (EGP/BGP) zwischen AS.*

### Distance-Vector vs. Link-State

| Eigenschaft | Distance-Vector | Link-State |
|-------------|-----------------|------------|
| **Beispiele** | RIP, EIGRP | OSPF, IS-IS |
| **Information** | Distanz zum Ziel | Gesamte Topologie |
| **Austausch** | Mit Nachbarn | Mit allen Routern |
| **Algorithmus** | Bellman-Ford | Dijkstra (SPF) |
| **Konvergenz** | Langsam | Schnell |
| **Speicher** | Gering | Hoch |
| **CPU** | Gering | Hoch |

## Wichtige Routing-Protokolle

### RIP (Routing Information Protocol)

> [!info] RIP - Der Klassiker
> - **Typ:** Distance-Vector (IGP)
> - **Metrik:** Hop-Count (max. 15, 16 = unreachable)
> - **Updates:** Alle 30 Sekunden (Broadcast/Multicast)
> - **Standard:** [[A-RFC-Index|RFC 2453]] (RIPv2)

```
Hop-Count-Metrik:

    A ───(1)──► B ───(1)──► C ───(1)──► D
    
    Route A→D: 3 Hops
    
    Limitation: Max. 15 Hops (16 = infinity)
```

### OSPF (Open Shortest Path First)

> [!info] OSPF - Der Enterprise-Standard
> - **Typ:** Link-State (IGP)
> - **Metrik:** Cost (basierend auf Bandbreite)
> - **Algorithmus:** Dijkstra (Shortest Path First)
> - **Standard:** [[A-RFC-Index|RFC 2328]]

![[ospf-hierarchie.png]]
*<span class="fig-id">03-03-06-ospf-hierarchie</span>: OSPF-Domäne mit Backbone Area 0 und Area Border Routern (ABR).*

**OSPF-Nachbarschaftszustände:**
1. **Down** - Keine Verbindung
2. **Init** - Hello empfangen
3. **2-Way** - Bidirektionale Kommunikation
4. **ExStart** - Master/Slave-Wahl
5. **Exchange** - DBD-Austausch
6. **Loading** - LSA-Anforderung
7. **Full** - Vollständig synchronisiert

### BGP (Border Gateway Protocol)

> [!info] BGP - Das Protokoll des Internets
> - **Typ:** Path-Vector (EGP)
> - **Metrik:** Pfad-Attribute (AS-Path, etc.)
> - **Port:** TCP 179
> - **Standard:** [[A-RFC-Index|RFC 4271]]

**BGP Path Selection (vereinfacht):**

1. Höchstes Weight (Cisco-spezifisch)
2. Höchste Local Preference
3. Locally originated
4. Kürzester AS-Path
5. Niedrigster Origin-Typ (IGP < EGP < Incomplete)
6. Niedrigster MED
7. eBGP vor iBGP
8. Niedrigste Router-ID

**AS-Path-Beispiel:**
```
Ziel: 203.0.113.0/24

Router A (AS 100):
  Path: AS 200 → AS 300 → AS 400
  AS-Path: 200 300 400
  
Router B (AS 100):
  Path: AS 500 → AS 400
  AS-Path: 500 400   ← Kürzerer Pfad, wird bevorzugt
```

## Routing-Metriken im Vergleich

| Protokoll | Metrik | Beschreibung |
|-----------|--------|--------------|
| **RIP** | Hop-Count | Anzahl der Router |
| **OSPF** | Cost | 10^8 / Bandbreite (bps) |
| **EIGRP** | Composite | Bandbreite, Delay, Load, Reliability |
| **BGP** | Path Attributes | AS-Path, Policies |

### OSPF-Cost-Berechnung

$$\text{Cost} = \frac{10^8}{\text{Bandbreite (bps)}}$$

| Verbindung | Bandbreite | OSPF Cost |
|------------|------------|-----------|
| 10 Gbps | 10.000.000.000 | 1 |
| 1 Gbps | 1.000.000.000 | 1 |
| 100 Mbps | 100.000.000 | 1 |
| 10 Mbps | 10.000.000 | 10 |
| 1 Mbps | 1.000.000 | 100 |

> [!warning] Anpassung erforderlich
> Bei modernen Hochgeschwindigkeitsnetzen muss die Referenzbandbreite angepasst werden, da sonst alle schnellen Links den gleichen Cost haben.

## Default-Route und Gateway

Die Default-Route (0.0.0.0/0) wird verwendet, wenn keine spezifischere Route existiert:

![[default-route-entscheidung.png]]
*<span class="fig-id">03-03-06-default-route-entscheidung</span>: Routing-Tabellen-Lookup mit Fallback auf Default-Route.*

## Prüfungsrelevante Themen

> [!warning] **Prüfungsrelevant**
> Routing ist ein zentrales Thema in der Netzwerktechnik und wird regelmäßig in Prüfungen abgefragt.

> [!question] **Typische Prüfungsfragen**
> 1. Erklären Sie den Unterschied zwischen statischem und dynamischem Routing.
> 2. Vergleichen Sie Distance-Vector- und Link-State-Protokolle.
> 3. Was unterscheidet IGP von EGP? Nennen Sie je zwei Beispiele.
> 4. Wie funktioniert der Longest Prefix Match?
> 5. Beschreiben Sie die OSPF-Area-Hierarchie und die Rolle von Area 0.

### Vergleichstabelle der Routing-Protokolle

| Protokoll | Typ | Metrik | Max. Hops | Konvergenz |
|-----------|-----|--------|-----------|------------|
| RIP | DV/IGP | Hop-Count | 15 | Langsam |
| OSPF | LS/IGP | Cost | Unbegrenzt | Schnell |
| IS-IS | LS/IGP | Cost | Unbegrenzt | Schnell |
| EIGRP | Hybrid/IGP | Composite | 255 | Sehr schnell |
| BGP | PV/EGP | Path | Unbegrenzt | Langsam |

## Zusammenhänge

- [[01-IP-Protokoll]] - IP-Adressierung als Basis für Routing
- [[03-IPv6]] - Routing mit IPv6
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - Routing-Security, BGP-Hijacking

## Quellen

- [[A-RFC-Index|RFC 2453]] - RIP Version 2
- [[A-RFC-Index|RFC 2328]] - OSPF Version 2
- [[A-RFC-Index|RFC 4271]] - BGP-4
- Tanenbaum, A. S.: Computernetzwerke, Kap. 5
