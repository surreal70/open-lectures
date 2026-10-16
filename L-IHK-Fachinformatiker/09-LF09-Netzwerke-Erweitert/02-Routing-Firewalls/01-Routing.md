---
title: "Routing – Grundlagen und Techniken"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - routing
  - netzwerk
  - router
source: proTirone (CC-BY-4.0)
---

# Routing – Grundlagen und Techniken

> [!info] Lernziele
> - Routing-Prinzipien verstehen
> - Unterschied zwischen statischem und dynamischem Routing erklären
> - Routingprotokolle klassifizieren
> - Routingtabellen lesen und konfigurieren

## Grundprinzip

### Was Router tun

Router **informieren** ihre benachbarten Router über:
- Welche Netze direkt angeschlossen sind
- Welche Netze die Nachbarrouter kennen

Sie **kommunizieren** über Routingprotokolle, **berechnen** mögliche Routen und **schreiben** diese in ihre Routingtabellen.

### Routing-Kriterien

Bei der Routenwahl werden mehrere Faktoren berücksichtigt:

| Kriterium | Beschreibung |
|-----------|--------------|
| **Hop Count** | Anzahl der Router auf dem Weg |
| **Durchsatz** | Bandbreite der Verbindungen |
| **Auslastung** | Aktuelle Last auf den Leitungen |
| **Latenz** | Verzögerungszeit |

### Grundsatz

> [!important] Merksatz
> Sind mehrere Router in einer Broadcast-Domäne eingebunden, gibt es (sofern nicht durch Firewalls unterbunden) auch mehrere Wege (Hopping-Sequenzen), einen Rechner auf Layer-III-Ebene zu erreichen.

## Routing-Typen

### Statisches Routing

**Manuelles Eintragen** fester Routen an Routern:

- Meist an **Grenzroutern** eingesetzt
- Typische Form: *"Route alles, was nicht zu deinem Adressbereich gehört, über Interface X zu Router Y"*
- Lokale Variante: *"Route alles aus Subnetz X an Subnetz Y über Router Z"*

```bash
# Linux: Statische Route hinzufügen
ip route add 192.168.1.0/24 via 10.0.0.1

# Windows: Statische Route hinzufügen
route add 192.168.1.0 mask 255.255.255.0 10.0.0.1
```

### Dynamisches Routing

**Automatische Berechnung** von Routen:
- Anhand von Informationen in Routingtabellen
- Mittels Austausch von Informationen zwischen Routern
- Ermöglicht **Umlernen** bei Netzwerkänderungen

## Routingprotokolle

### Klassifikation

```
┌─────────────────────────────────────────────────────────────┐
│                    Routingprotokolle                        │
├────────────────────────┬────────────────────────────────────┤
│  Distance Vector       │  Link State                        │
├────────────────────────┼────────────────────────────────────┤
│ • Tauschen Tabellen    │ • Senden Netzbeschreibungen        │
│ • Erwarten Format-     │ • Erlauben eigene Berechnung       │
│   verständnis          │ • Flexibler, größere Reichweite    │
│ • Einfach, ressourcen- │ • Rechenintensiver                 │
│   sparend              │                                    │
├────────────────────────┼────────────────────────────────────┤
│ Beispiele:             │ Beispiele:                         │
│ • RIP                  │ • OSPF                             │
│ • IGRP                 │ • IS-IS                            │
└────────────────────────┴────────────────────────────────────┘
```

### Wichtige Protokolle

| Protokoll | Typ | Beschreibung |
|-----------|-----|--------------|
| **RIP** | Distance Vector | Router Information Protocol |
| **OSPF** | Link State | Open Shortest Path First |
| **IGRP** | Distance Vector | Interior Gateway Routing Protocol |
| **BGP** | Path Vector | Border Gateway Protocol (Weitverkehr) |

> [!note] VLSM-Unterstützung
> Moderne Protokolle unterstützen **VLSM** (Variable Length Subnet Masks) für flexible Segmentierung. Ältere Protokolle können das nicht.

### Vendor-Problematik

> [!warning] Kompatibilität
> Viele Protokolle sind proprietär und NICHT auf Kompatibilität ausgelegt.
> 
> Empfehlung: In dynamisch gerouteten Umgebungen lieber einen definierten Hersteller wählen und eine möglichst homogene Umgebung aufbauen.

## Routingtabellen

### Aufbau

Eine Routingtabelle enthält typischerweise:

| Feld | Beschreibung |
|------|--------------|
| Zielnetz | Netzwerkadresse + Maske |
| Gateway | Nächster Hop (Router) |
| Interface | Ausgangs-Schnittstelle |
| Metrik | Kosten/Priorität der Route |

### Anzeigen und Konfigurieren

```bash
# Linux: Routingtabelle anzeigen
ip route show
# oder
route -n

# Windows: Routingtabelle anzeigen
route print

# Linux: Route hinzufügen
sudo ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0

# Linux: Route entfernen
sudo ip route del 10.0.0.0/8
```

### Beispiel-Routingtabelle

```
Ziel            Gateway         Genmask         Flags Metric Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    100    eth0
10.0.0.0        192.168.1.254   255.0.0.0       UG    0      eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     100    eth0
```

---

> [!tip] Übung
> 1. Zeigen Sie die Routingtabelle Ihres Rechners an
> 2. Identifizieren Sie das Default-Gateway
> 3. Fügen Sie eine temporäre statische Route hinzu und entfernen Sie sie wieder

## Weiterführende Literatur

- Schreiner: Computernetzwerke, 2014, S. 86-88

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
