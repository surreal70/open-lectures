---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - mac
  - layer2
  - adressierung
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# MAC-Adressen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Aufbau einer MAC-Adresse erklären können
> - Den Unterschied zwischen MAC- und IP-Adresse kennen
> - Die Rolle von MAC-Adressen im ARP-Protokoll verstehen
> - MAC-Adressen auf deinem System anzeigen können

---

## Überblick

Die **MAC-Adresse** (Media Access Control) ist die Hardware-Adresse einer Netzwerkschnittstelle. Sie arbeitet auf **Layer 2** (Sicherungsschicht) des OSI-Modells und ist weltweit eindeutig.

## Aufbau einer MAC-Adresse

Eine MAC-Adresse besteht aus **48 Bit** (6 Byte) und wird hexadezimal dargestellt:

```
00:1A:2B:3C:4D:5E
└─────┘ └─────┘
  OUI    NIC
```

| Teil | Bits | Beschreibung |
|------|------|--------------|
| **OUI** | 24 | Organizationally Unique Identifier (Herstellerkennung) |
| **NIC** | 24 | Network Interface Controller (Gerätekennung) |

### Schreibweisen

Die gleiche MAC-Adresse kann unterschiedlich notiert werden:

| Format | Beispiel |
|--------|----------|
| Doppelpunkt | `00:1A:2B:3C:4D:5E` |
| Bindestrich | `00-1A-2B-3C-4D-5E` |
| Cisco-Format | `001A.2B3C.4D5E` |
| Ohne Trenner | `001A2B3C4D5E` |

### Spezielle MAC-Adressen

| Adresse | Bedeutung |
|---------|-----------|
| `FF:FF:FF:FF:FF:FF` | Broadcast (alle Geräte) |
| `00:00:00:00:00:00` | Ungültig/nicht gesetzt |
| `01:xx:xx:xx:xx:xx` | Multicast (Bit 0 des ersten Bytes = 1) |

## MAC vs. IP-Adresse

| Eigenschaft | MAC-Adresse | IP-Adresse |
|-------------|-------------|------------|
| **Layer** | 2 (Data Link) | 3 (Network) |
| **Länge** | 48 Bit | 32 Bit (IPv4) / 128 Bit (IPv6) |
| **Zuweisung** | Vom Hersteller | Vom Administrator/DHCP |
| **Reichweite** | Lokal (Broadcastdomain) | Global (Internet) |
| **Änderbar** | Schwer (fest in Hardware) | Leicht (Konfiguration) |

## ARP: Verbindung zwischen MAC und IP

Das **Address Resolution Protocol (ARP)** löst IP-Adressen in MAC-Adressen auf:

```
1. Host A will an 192.168.1.5 senden
2. Host A: "Wer hat 192.168.1.5?" (ARP-Request, Broadcast)
3. Host B: "Ich! Meine MAC ist 00:1A:2B:3C:4D:5E" (ARP-Reply)
4. Host A speichert die Zuordnung im ARP-Cache
5. Host A sendet Daten an MAC 00:1A:2B:3C:4D:5E
```

> [!note] **ARP-Cache**
> Jedes Gerät speichert bekannte IP-zu-MAC-Zuordnungen im ARP-Cache, um wiederholte ARP-Anfragen zu vermeiden.

## Praktische Befehle

### Windows

```cmd
# ARP-Cache anzeigen
arp -a

# MAC-Adresse der eigenen Interfaces
ipconfig /all

# ARP-Cache löschen (Admin)
arp -d *
```

### Linux

```bash
# ARP-Cache anzeigen
arp -n
# oder
ip neigh show

# MAC-Adresse anzeigen
ip link show

# ARP-Cache löschen
sudo ip neigh flush all
```

> [!example] **Übung: ARP-Cache untersuchen**
> - [ ] Öffne eine Kommandozeile
> - [ ] Führe `ping 8.8.8.8` aus
> - [ ] Zeige den ARP-Cache an (`arp -a` / `ip neigh`)
> - [ ] Identifiziere die MAC-Adresse deines Gateways
> - [ ] Finde heraus, von welchem Hersteller dein Router stammt (OUI-Lookup)

## OUI-Lookup

Die ersten 3 Bytes einer MAC-Adresse identifizieren den Hersteller:

| OUI | Hersteller |
|-----|------------|
| `00:00:0C` | Cisco |
| `00:1A:2B` | Ayecom Technology |
| `00:50:56` | VMware |
| `08:00:27` | VirtualBox |
| `DC:A6:32` | Raspberry Pi |

> [!tip] **Online OUI-Lookup**
> Unter [macvendors.com](https://macvendors.com) oder [macaddress.io](https://macaddress.io) kannst du den Hersteller einer MAC-Adresse nachschlagen.

## Zusammenhänge

- → [[02-Grundbegriffe|Grundbegriffe (OSI-Modell)]]
- → [[08-IPv4-Adressen|IPv4-Adressen (Layer 3)]]
- → [[05-Adressierung|Adressierungskonzepte]]
- → [[Glossar#M|Glossar: MAC-Adresse]]

> [!warning] **Prüfungsrelevant**
> - Aufbau einer MAC-Adresse (48 Bit, OUI + NIC)
> - Unterschied MAC vs. IP-Adresse
> - Funktion des ARP-Protokolls
> - Broadcast-MAC-Adresse: `FF:FF:FF:FF:FF:FF`

> [!question] **Typische Prüfungsfragen**
> - Aus wie vielen Bits besteht eine MAC-Adresse?
> - Auf welcher OSI-Schicht arbeitet die MAC-Adresse?
> - Erklären Sie den ARP-Prozess.
> - Wie lautet die Broadcast-MAC-Adresse?
> - Wozu dient der OUI-Teil einer MAC-Adresse?

## Quellen

- proTirone: LF03:07 MAC-Adressen (Karsten Reincke, CC-BY-4.0)
- IEEE OUI Registry

> [!tip] **Weiterführende Links**
> - [IEEE OUI Lookup](https://standards-oui.ieee.org/)
> - [Wikipedia: MAC-Adresse](https://de.wikipedia.org/wiki/MAC-Adresse)
> - [[07-Binaeroperationen|Nächstes Kapitel: Binäroperationen]]
