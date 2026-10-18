---
author: Andreas Hümmer
title: Netzwerktopologien
tags:
  - vorlesung
  - rn
  - grundlagen
  - topologie
  - netzwerkstruktur
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Netzwerktopologien

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Unterschied zwischen physischer und logischer Topologie erklären
> - Die Grundtopologien (Bus, Ring, Stern, Baum, Mesh) beschreiben und zeichnen
> - Vor- und Nachteile jeder Topologie benennen
> - Das Ausfallverhalten verschiedener Topologien analysieren
> - Reale Netzwerke den Topologieformen zuordnen

## Physische vs. Logische Topologie

Eine wichtige Unterscheidung:

| Aspekt | Physische Topologie | Logische Topologie |
|--------|--------------------|--------------------|
| **Definition** | Tatsächliche Verkabelung/Verbindung | Datenfluss im Netzwerk |
| **Sichtbarkeit** | Kabel, Geräte, Räumlichkeiten | Protokolle, Adressen |
| **Beispiel** | Stern (Kabel zu Switch) | Bus (Ethernet-Broadcast) |

> [!merke] Merke
> Ein physischer Stern kann logisch wie ein Bus arbeiten (klassisches Ethernet über Hub) oder wie ein Stern (Ethernet über Switch mit Punkt-zu-Punkt-Verbindungen).

## Grundtopologien

### Bus-Topologie

Alle Geräte sind an ein gemeinsames Übertragungsmedium angeschlossen.

![[bus-topologie.png]]
*<span class="fig-id">03-01-03-bus-topologie</span>: Bus-Topologie mit Terminatoren an beiden Enden.*

**Eigenschaften:**
- Alle Geräte empfangen alle Signale
- Kollisionen möglich (CSMA/CD erforderlich)
- Terminatoren an den Enden verhindern Signalreflexion

| Vorteile | Nachteile |
|----------|-----------|
| Einfache Installation | Single Point of Failure (Kabel) |
| Geringer Kabelaufwand | Schwierige Fehlersuche |
| Kostengünstig | Kollisionen reduzieren Durchsatz |
| Leicht erweiterbar | Begrenzte Kabellänge |
| | Keine Privatsphäre (alle hören mit) |

**Historische Anwendung:**
- 10BASE2 (Thin Ethernet, Koaxialkabel)
- 10BASE5 (Thick Ethernet)

### Ring-Topologie

Geräte sind in einer geschlossenen Schleife verbunden. Daten fließen in eine Richtung.

![[ring-topologie.png]]
*<span class="fig-id">03-01-03-ring-topologie</span>: Ring-Topologie mit unidirektionalem Datenfluss.*

**Eigenschaften:**
- Jedes Gerät hat genau zwei Nachbarn
- Daten passieren jeden Knoten
- Token-basierter Zugriff (Token Ring)
- Dual Ring für Redundanz möglich

| Vorteile | Nachteile |
|----------|-----------|
| Keine Kollisionen | Ausfall eines Geräts unterbricht Ring |
| Deterministischer Zugriff | Hohe Latenz bei vielen Knoten |
| Gleichberechtigter Zugang | Schwierige Erweiterung |
| Gute Performance unter Last | Aufwändige Fehlersuche |

**Varianten:**
- **Single Ring**: Einfacher Ring, anfällig für Ausfälle
- **Dual Ring (FDDI)**: Zwei gegenläufige Ringe für Redundanz

![[dual-ring-fddi.png]]
*<span class="fig-id">03-01-03-dual-ring-fddi</span>: Dual Ring (FDDI) mit primärem und sekundärem Ring für Ausfallsicherheit.*

**Anwendungen:**
- Token Ring (IBM, historisch)
- FDDI (Fiber Distributed Data Interface)
- SONET/SDH (WAN-Backbones)

### Stern-Topologie

Alle Geräte sind mit einem zentralen Knoten (Hub, Switch) verbunden.

![[stern-topologie.png]]
*<span class="fig-id">03-01-03-stern-topologie</span>: Stern-Topologie mit zentralem Switch und radialen Verbindungen zu den Endgeräten.*

**Eigenschaften:**
- Zentrale Komponente koordiniert Kommunikation
- Jedes Gerät hat dedizierte Verbindung zum Zentrum
- Ausfall eines Endgeräts betrifft nur dieses

| Vorteile | Nachteile |
|----------|-----------|
| Einfache Fehlersuche | Single Point of Failure (Zentrale) |
| Ausfall isoliert | Hoher Kabelaufwand |
| Leicht erweiterbar | Kosten für zentrale Komponente |
| Hohe Performance (Switch) | Begrenzte Entfernung zum Zentrum |
| Einfache Verwaltung | |

**Hub vs. Switch:**

| Aspekt | Hub | Switch |
|--------|-----|--------|
| Logische Topologie | Bus | Stern |
| Kollisionsdomäne | Eine (alle Ports) | Pro Port |
| Bandbreite | Geteilt | Dediziert pro Port |
| Kosten | Niedrig | Höher |
| Heute noch relevant | Nein | Ja |

**Anwendung:**
- Nahezu alle modernen LANs
- Heimnetzwerke
- Rechenzentren

### Baum-Topologie (Hierarchische Topologie)

Erweiterung der Stern-Topologie mit mehreren Ebenen.

![[baum-topologie.png]]
*<span class="fig-id">03-01-03-baum-topologie</span>: Hierarchische Baum-Topologie mit Core-, Distribution- und Access-Ebene.*

**Eigenschaften:**
- Hierarchische Struktur (Core → Distribution → Access)
- Skalierbar durch Hinzufügen von Ebenen
- Kombiniert Stern-Topologien

| Vorteile | Nachteile |
|----------|-----------|
| Sehr skalierbar | Ausfall der Wurzel kritisch |
| Gute Strukturierung | Komplexe Konfiguration |
| Segmentierung möglich | Höhere Kosten |
| Broadcast-Kontrolle | Längere Pfade möglich |

**Anwendung:**
- Große Unternehmensnetzwerke
- Campus-Netzwerke
- Rechenzentren (3-Tier-Architektur)

### Vermaschte Topologie (Mesh)

Jeder Knoten ist mit mehreren anderen verbunden. Bietet Redundanz.

![[mesh-topologie.png]]
*<span class="fig-id">03-01-03-mesh-topologie</span>: Vermaschte Topologie – links vollvermascht (alle 10 Verbindungen), rechts teilvermascht (6 von 10 Verbindungen).*

**Eigenschaften:**
- Vollvermascht: Jeder mit jedem verbunden
- Teilvermascht: Ausgewählte Redundanzpfade
- Hohe Ausfallsicherheit

| Vorteile | Nachteile |
|----------|-----------|
| Hohe Redundanz | Sehr hoher Kabelaufwand |
| Kein Single Point of Failure | Komplexe Konfiguration |
| Multiple Pfade (Load Balancing) | Hohe Kosten |
| Ausfallsicher | Skaliert schlecht (O(n²)) |

**Formel für vollvermaschte Verbindungen:**
$$\text{Anzahl Verbindungen} = \frac{n \cdot (n-1)}{2}$$

| Knoten | Verbindungen |
|--------|--------------|
| 4 | 6 |
| 5 | 10 |
| 10 | 45 |
| 20 | 190 |
| 100 | 4.950 |

**Anwendung:**
- WAN-Backbones
- Internet-Kernnetze
- Kritische Infrastruktur
- WLAN-Mesh-Systeme (teilvermascht)

## Hybride Topologien

Reale Netzwerke kombinieren oft mehrere Grundtopologien:

### Stern-Bus

Mehrere Stern-Segmente über einen Bus verbunden.

### Stern-Ring

Stern-Topologie mit Ring-Verbindung der zentralen Switches.

### Spine-Leaf (Datacenter)

Moderne Rechenzentren nutzen eine spezielle Mesh-Variante:

![[spine-leaf.png]]
*<span class="fig-id">03-01-03-spine-leaf</span>: Spine-Leaf-Architektur – jeder Leaf-Switch ist mit allen Spine-Switches verbunden (Full-Mesh zwischen den Ebenen), wodurch maximal 2 Hops zwischen beliebigen Servern entstehen.*

## Vergleich der Topologien

| Topologie | Ausfallsicherheit | Kosten | Skalierbarkeit | Komplexität |
|-----------|-------------------|--------|----------------|-------------|
| Bus | ⚠️ Niedrig | 💰 Niedrig | ⚠️ Begrenzt | ✅ Einfach |
| Ring | ⚠️ Niedrig* | 💰💰 Mittel | ⚠️ Begrenzt | 💻 Mittel |
| Stern | ⚠️ Mittel** | 💰💰 Mittel | ✅ Gut | ✅ Einfach |
| Baum | ⚠️ Mittel** | 💰💰💰 Hoch | ✅✅ Sehr gut | 💻💻 Hoch |
| Mesh | ✅✅ Hoch | 💰💰💰💰 Sehr hoch | ⚠️ O(n²) | 💻💻💻 Sehr hoch |

\* Dual Ring verbessert Ausfallsicherheit  
\** Single Point of Failure am zentralen Knoten

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Physische Topologie ≠ Logische Topologie
> - Grundtopologien: Bus, Ring, Stern, Baum, Mesh
> - Stern ist heute der Standard für LANs
> - Mesh bietet höchste Redundanz, aber O(n²) Komplexität
> - Reale Netze sind meist hybride Topologien
> - Spine-Leaf ist der moderne Datacenter-Standard

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Grundtopologien: Bus, Ring, Stern, Baum, Mesh (zeichnen können)
> - Vor- und Nachteile jeder Topologie (je 3)
> - Ausfallverhalten der verschiedenen Topologien
> - Unterschied physische vs. logische Topologie


> [!question] **Typische Prüfungsfragen**
> - Zeichnen Sie eine Stern-Topologie und nennen Sie 3 Vorteile
> - Wie viele Verbindungen hat ein vollvermaschtes Netz mit 10 Knoten?
> - Warum ist die physische Topologie bei Ethernet oft ein Stern, die logische aber ein Bus?
> - Welche Topologie bietet die höchste Ausfallsicherheit und warum?

## Verwandte Themen

- [[01-Historie]] – Entwicklung der Netzwerktechnologien
- [[02-Standards-und-Gremien]] – Standardisierungsgremien und IEEE 802
- [[03-Netzwerktypen]] – Klassifikation nach Reichweite
- [[01-Ethernet|Ethernet]] – Der dominierende LAN-Standard
- [[00-Sicherungsschicht-Index|Sicherungsschicht]] – MAC-Adressen und Switching

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
- Cisco: Campus Network Design Guide
