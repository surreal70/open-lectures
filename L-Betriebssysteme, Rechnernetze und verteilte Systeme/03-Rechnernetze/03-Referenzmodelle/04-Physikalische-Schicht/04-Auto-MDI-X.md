---
author: Andreas Hümmer
title: Auto-MDI/MDI-X
tags:
  - vorlesung
  - rn
  - layer1
  - ethernet
  - kabel
  - crossover
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Auto-MDI/MDI-X

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Unterschied zwischen MDI und MDI-X erklären
> - Verstehen, wann Crossover-Kabel benötigt wurden
> - Die Funktionsweise von Auto-MDI/MDI-X beschreiben
> - Die historische Entwicklung und heutige Relevanz einordnen

## Grundlagen

### MDI und MDI-X

Bei Ethernet über Twisted-Pair-Kabel gibt es zwei Anschlussarten:

**MDI (Medium Dependent Interface)**
- Standard-Pinbelegung für Endgeräte
- Pins 1, 2: Sendepaar (TX+, TX−)
- Pins 3, 6: Empfangspaar (RX+, RX−)
- Verwendet bei: PCs, Server, Router-Ports

**MDI-X (MDI Crossover)**
- Gekreuzte Pinbelegung für Infrastrukturgeräte
- Pins 1, 2: Empfangspaar (RX+, RX−)
- Pins 3, 6: Sendepaar (TX+, TX−)
- Verwendet bei: Switches, Hubs

### Pinbelegung im Vergleich

| Pin | MDI (PC) | MDI-X (Switch) |
|-----|----------|----------------|
| 1 | TX+ | RX+ |
| 2 | TX− | RX− |
| 3 | RX+ | TX+ |
| 6 | RX− | TX− |

## Kabeltypen

### Patch-Kabel (Straight-Through)

Ein **Patch-Kabel** verbindet beide Enden 1:1 – Pin 1 auf Pin 1, Pin 2 auf Pin 2, usw.

```
MDI (PC)          Patch-Kabel          MDI-X (Switch)
┌────────┐        ═══════════          ┌────────┐
│ TX+ (1)├────────────────────────────►│ RX+ (1)│
│ TX- (2)├────────────────────────────►│ RX- (2)│
│ RX+ (3)│◄────────────────────────────┤ TX+ (3)│
│ RX- (6)│◄────────────────────────────┤ TX- (6)│
└────────┘                             └────────┘
```

**Verwendung**: MDI ↔ MDI-X (PC zu Switch, Router zu Switch)

### Crossover-Kabel

Ein **Crossover-Kabel** kreuzt die Sende- und Empfangspaare:

```
MDI (PC 1)        Crossover-Kabel       MDI (PC 2)
┌────────┐        ═══════╳═════          ┌────────┐
│ TX+ (1)├────────────────╲─────────────►│ RX+ (3)│
│ TX- (2)├─────────────────╲────────────►│ RX- (6)│
│ RX+ (3)│◄─────────────────╱───────────┤ TX+ (1)│
│ RX- (6)│◄────────────────╱────────────┤ TX- (2)│
└────────┘                             └────────┘
```

**Verwendung**: MDI ↔ MDI oder MDI-X ↔ MDI-X (PC zu PC, Switch zu Switch)

### Übersicht Kabelwahl (ohne Auto-MDI/X)

| Verbindung | Kabeltyp |
|------------|----------|
| PC ↔ Switch | Patch-Kabel |
| PC ↔ Hub | Patch-Kabel |
| PC ↔ Router | Patch-Kabel |
| PC ↔ PC | Crossover-Kabel |
| Switch ↔ Switch | Crossover-Kabel |
| Switch ↔ Hub | Crossover-Kabel |
| Router ↔ Router | Crossover-Kabel |

## Auto-MDI/MDI-X

### Funktionsweise

**Auto-MDI/MDI-X** (auch **Auto-MDIX** oder **HP Auto-Sensing**) ist eine Funktion moderner Ethernet-Ports, die automatisch erkennt, welche Kabelart verwendet wird, und die Pinbelegung entsprechend anpasst.

Der Erkennungsprozess:

1. **Link-Pulse-Erkennung**: Beim Einstecken des Kabels sendet der Port Testimpulse
2. **Polaritätsprüfung**: Der Port prüft, ob Signale auf den erwarteten Pins ankommen
3. **Automatische Umschaltung**: Bei Bedarf wird intern zwischen MDI und MDI-X umgeschaltet
4. **Link-Aufbau**: Nach erfolgreicher Erkennung wird die Verbindung hergestellt

> [!info] Transparenz
> Auto-MDI/MDI-X arbeitet vollständig transparent. Der Benutzer muss sich keine Gedanken mehr über Kabeltypen machen – jedes Kabel funktioniert.

### Standardisierung

| Standard | Auto-MDI/X | Jahr |
|----------|------------|------|
| 100BASE-TX | Optional | 1995 |
| 1000BASE-T | **Pflicht** | 1999 |
| 10GBASE-T | Pflicht | 2006 |

> [!wichtig] Gigabit Ethernet
> Seit **1000BASE-T (Gigabit Ethernet)** ist Auto-MDI/MDI-X im Standard vorgeschrieben. Alle Gigabit-Ports unterstützen diese Funktion.

### Vorteile

- ✅ **Vereinfachte Verkabelung**: Kein Nachdenken über Kabeltypen
- ✅ **Weniger Fehlerquellen**: Falsche Kabel funktionieren trotzdem
- ✅ **Reduzierte Lagerhaltung**: Nur noch ein Kabeltyp notwendig
- ✅ **Flexibilität**: Geräte können beliebig verbunden werden

## Gigabit Ethernet und 4-Paar-Übertragung

Bei **1000BASE-T** wird die Unterscheidung MDI/MDI-X komplexer, da alle 4 Adernpaare bidirektional genutzt werden:

| Paar | Pins | Funktion |
|------|------|----------|
| 1 | 1, 2 | Bidirektional (BI_DA) |
| 2 | 3, 6 | Bidirektional (BI_DB) |
| 3 | 4, 5 | Bidirektional (BI_DC) |
| 4 | 7, 8 | Bidirektional (BI_DD) |

Bei Gigabit Ethernet übernimmt **Auto-Negotiation** nicht nur die Geschwindigkeitsaushandlung, sondern auch die Master/Slave-Zuweisung:

- **Master**: Gibt den Takt vor
- **Slave**: Synchronisiert sich auf den Master

Die Rolle wird automatisch ausgehandelt – unabhängig vom verwendeten Kabeltyp.

## Praktische Relevanz heute

### Wann Crossover-Kabel noch relevant sind

| Szenario | Crossover nötig? |
|----------|------------------|
| Moderne Gigabit-Geräte | Nein (Auto-MDI/X) |
| Ältere 100 Mbit-Switches | Möglicherweise |
| Industrielle Steuerungen | Möglicherweise |
| Embedded Systems | Prüfen |

### Uplink-Ports

Manche älteren Switches haben einen speziellen **Uplink-Port**:

- Fest auf MDI konfiguriert (statt MDI-X wie normale Ports)
- Ermöglicht Kaskadierung mit Patch-Kabel
- Oft mit normalem Port kombiniert (entweder/oder)
- Bei Auto-MDI/X obsolet

## Fehlerbehebung

### Symptome bei falschem Kabeltyp (ohne Auto-MDI/X)

- Keine Link-LED
- Kein Netzwerkzugriff
- Intermittierende Verbindung

### Diagnose

1. **Link-LEDs prüfen**: Leuchten sie auf beiden Seiten?
2. **Kabeltyp identifizieren**: Patch oder Crossover?
3. **Gerätetypen**: Beide MDI oder beide MDI-X?
4. **Auto-MDI/X-Fähigkeit**: Unterstützen beide Geräte die Funktion?

> [!tip] Tipp
> Im Zweifelsfall ein Gigabit-fähiges Gerät (Switch, USB-Adapter) als Zwischenstation nutzen – diese unterstützen immer Auto-MDI/X.

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **MDI**: Standard-Pinbelegung für Endgeräte (TX auf 1/2, RX auf 3/6)
> - **MDI-X**: Gekreuzte Pinbelegung für Switches (RX auf 1/2, TX auf 3/6)
> - **Patch-Kabel**: Für MDI ↔ MDI-X Verbindungen
> - **Crossover-Kabel**: Für MDI ↔ MDI oder MDI-X ↔ MDI-X
> - **Auto-MDI/MDI-X**: Automatische Erkennung und Anpassung
> - Seit **Gigabit Ethernet** ist Auto-MDI/X Pflicht – Crossover-Kabel sind obsolet

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
N/A

## Verwandte Themen

- [[01-Uebertragungsmedien]] – Twisted-Pair-Kabel und RJ45-Pinbelegung
- [[02-Signale]] – Signalübertragung und Leitungscodierung
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE 802.3]] – Ethernet-Standards

## Quellen

- IEEE 802.3-2018, Clause 40 (1000BASE-T)
- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
