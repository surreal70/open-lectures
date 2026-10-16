---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - netzwerk
  - begriffe
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# Grundlegende Netzwerkbegriffe

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die wichtigsten Netzwerkbegriffe definieren können
> - Netzwerkkomponenten unterscheiden können
> - Netztaxonomien nach Reichweite, Funktion und Topologie kennen
> - Das OSI-Modell und TCP/IP-Referenzmodell erklären können

---

## Überblick

Im Lernfeld 03 geht es zunächst darum, Begriffe und Konzepte kennenzulernen. In der Mittelstufe (Lernfeld 09) wird es dann um das Zusammenwirken und Ineinandergreifen dieser Konzepte gehen.

## Grundlegende Begriffe

### Netzwerkkomponenten

| Begriff | Definition |
|---------|------------|
| **Host** | Ein Gerät mit eigenständiger Netzwerkadresse |
| **Server** | Komponente, die Dienste für andere Geräte bereitstellt |
| **Client** | Komponente, die Dienste von Servern nutzt |
| **Router** | Verbindet verschiedene Netzwerke (Layer 3) |
| **Switch** | Verbindet Geräte innerhalb eines Netzwerks (Layer 2) |
| **Gateway** | Übergangspunkt zwischen Netzwerken |

### Adressierung

| Begriff | Definition |
|---------|------------|
| **IP-Adresse** | Logische Adresse eines Netzwerkinterfaces (Layer 3) |
| **MAC-Adresse** | Physische Hardware-Adresse (Layer 2) |
| **Broadcastadresse** | Adresse für alle Geräte einer Broadcastdomain |
| **Unicastadresse** | Adresse eines einzelnen Geräts |
| **Multicastadresse** | Adresse einer Gruppe von Geräten |

### Netzwerkbereiche

| Begriff | Definition |
|---------|------------|
| **Broadcastdomain** | Bereich, in dem Broadcasts empfangen werden (Switch-Bereich) |
| **LAN** | Local Area Network — lokales Netzwerk |
| **WLAN** | Wireless LAN — drahtloses lokales Netzwerk |
| **DMZ** | Demilitarisierte Zone — Pufferbereich zwischen Netzen |

> [!example] **Übung: Begriffe zuordnen**
> Erstelle eine Mindmap mit den obigen Begriffen. Nutze dafür Freeplane oder draw.io.
> 
> - [ ] Installiere Freeplane auf deinem Rechner
> - [ ] Erstelle Kategorien: Geräte, Adressen, Bereiche
> - [ ] Ordne alle Begriffe den Kategorien zu
> - [ ] Ergänze fehlende Begriffe, die dir einfallen

## Netztaxonomien

### Nach Reichweite

| Typ | Name | Reichweite | Beispiel |
|-----|------|------------|----------|
| **PAN** | Personal Area Network | Wenige Meter | Bluetooth-Headset |
| **LAN** | Local Area Network | Gebäude/Campus | Firmennetzwerk |
| **WLAN** | Wireless LAN | 50-500m | WiFi |
| **MAN** | Metropolitan Area Network | Stadt (~100km) | Stadtnetz |
| **WAN** | Wide Area Network | Land/Kontinent | Firmennetz |
| **GAN** | Global Area Network | Weltweit | Internet |

### Nach Funktion

| Typ | Beschreibung |
|-----|--------------|
| **Office-LAN** | Arbeitsplatzrechner, Drucker |
| **Server-LAN** | Dedizierte Server, meist ohne Monitor |
| **Intranet** | Internes Firmennetzwerk |
| **Internet** | Netzwerk zwischen Intranets |
| **Providernetz** | ISP-Infrastruktur |

### Nach Topologie

| Topologie | Eigenschaften |
|-----------|---------------|
| **Stern** | Zentrale Komponente (Switch/Hub), gute Erweiterbarkeit |
| **Bus** | Alle Geräte an einem Medium, heute selten |
| **Ring** | Pakete kreisen, hohe Ausfallgefahr |
| **Baum** | Hierarchische Struktur, gut skalierbar |
| **Masche** | Mehrfache Verbindungen, hohe Redundanz |

```
STERN              BUS                RING
  
   ○                                   ○
   │              ○──○──○──○          ╱ ╲
○──●──○                              ○   ○
   │                                  ╲ ╱
   ○                                   ○
```

## OSI-Referenzmodell

Das **Open Systems Interconnection Model** teilt die Netzwerkkommunikation in 7 Schichten:

| Layer | Name | Deutsch | Beispiele |
|-------|------|---------|-----------|
| 7 | Application | Anwendung | HTTP, FTP, SMTP |
| 6 | Presentation | Darstellung | JPEG, ASCII, SSL |
| 5 | Session | Sitzung | SMB, SSH |
| 4 | Transport | Transport | TCP, UDP |
| 3 | Network | Vermittlung | IP, ICMP, Router |
| 2 | Data Link | Sicherung | Ethernet, Switch, MAC |
| 1 | Physical | Physikalisch | Kabel, Hub, Signale |

> [!tip] **Merkhilfe OSI-Modell**
> **A**lle **P**riester **S**aufen **T**equila **N**ach **D**er **P**redigt
> (Application → Physical, von oben nach unten)

## TCP/IP-Referenzmodell

Das praktisch verwendete Modell hat nur 4 Schichten:

| Layer | Name | OSI-Entsprechung |
|-------|------|------------------|
| 4 | Application | Layer 5-7 |
| 3 | Transport | Layer 4 |
| 2 | Internet | Layer 3 |
| 1 | Link | Layer 1-2 |

## Zusammenhänge

- → [[03-Architekturen|Netzwerkarchitekturen (Vertiefung)]]
- → [[06-MAC-Adressen|MAC-Adressen (Layer 2)]]
- → [[08-IPv4-Adressen|IP-Adressen (Layer 3)]]
- → [[Glossar|Glossar]]

> [!warning] **Prüfungsrelevant**
> - Die 7 Schichten des OSI-Modells mit Beispielen
> - Unterschied OSI-Modell vs. TCP/IP-Modell
> - Netztaxonomien (PAN, LAN, WAN, etc.)
> - Topologien und ihre Vor-/Nachteile

> [!question] **Typische Prüfungsfragen**
> - Nennen Sie die 7 Schichten des OSI-Modells.
> - Auf welcher Schicht arbeitet ein Switch?
> - Was unterscheidet einen Router von einem Switch?
> - Welche Vor- und Nachteile hat eine Stern-Topologie?

## Quellen

- Schreiner: Computernetzwerke, 2014, S.3ff
- Baun: Computernetze kompakt, 2022, S.39ff
- proTirone: LF03:02 Begriffe (Karsten Reincke, CC-BY-4.0)

> [!tip] **Weiterführende Links**
> - [Wikipedia: OSI-Modell](https://de.wikipedia.org/wiki/OSI-Modell)
> - [Wikipedia: TCP/IP-Referenzmodell](https://de.wikipedia.org/wiki/Internetprotokollfamilie)
> - [[03-Architekturen|Nächstes Kapitel: Netzwerkarchitekturen]]
