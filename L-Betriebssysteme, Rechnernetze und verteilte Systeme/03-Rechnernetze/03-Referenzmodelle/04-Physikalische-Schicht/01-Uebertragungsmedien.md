---
author: Andreas Hümmer
title: Übertragungsmedien
tags:
  - vorlesung
  - rn
  - layer1
  - kabel
  - glasfaser
  - wlan
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Übertragungsmedien

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die verschiedenen Übertragungsmedien und ihre Eigenschaften benennen
> - Kupferkabel-Kategorien und ihre Anwendungen unterscheiden
> - Glasfaser-Typen (Singlemode, Multimode) erklären
> - Stecker- und Kabeltypen zuordnen
> - Vor- und Nachteile der verschiedenen Medien abwägen

## Übersicht der Übertragungsmedien

| Leitungsgebunden | Beschreibung | Drahtlos | Beschreibung |
|------------------|--------------|----------|--------------|
| **Twisted Pair** | Kupferkabel (Cat5e-Cat8) | **WLAN (802.11)** | 2,4 / 5 / 6 GHz |
| **Koaxialkabel** | Historisch (10BASE2/5) | **Bluetooth** | 2,4 GHz, PAN |
| **Glasfaser** | Lichtübertragung | **Mobilfunk** | LTE, 5G |
| **Twinax** | Rechenzentrum (kurz) | **Satellit/Richtfunk** | Weitverkehr |

## Twisted-Pair-Kabel (Kupfer)

### Aufbau

Twisted-Pair-Kabel bestehen aus **verdrillten Adernpaaren**, die elektromagnetische Störungen reduzieren:

![[UTP_cable.jpg|300]]
*<span class="fig-id">03-03-04-01-utp-cable</span>: Twisted-Pair-Kabel mit 4 verdrillten Adernpaaren (8 Adern). Quelle: Wikimedia Commons.*

**Abschirmungstypen:**

| Bezeichnung | Beschreibung |
|-------------|--------------|
| **U/UTP** | Ungeschirmt (Unshielded) |
| **F/UTP** | Folienschirm um alle Paare |
| **S/FTP** | Geflechtschirm + Folie pro Paar |
| **SF/FTP** | Geflecht + Folie gesamt + Folie pro Paar |

### Kabelkategorien

| Kategorie | Max. Frequenz | Anwendung | Max. Geschwindigkeit |
|-----------|---------------|-----------|---------------------|
| Cat3 | 16 MHz | Telefon, 10BASE-T | 10 Mbit/s |
| Cat5 | 100 MHz | 100BASE-TX | 100 Mbit/s |
| Cat5e | 100 MHz | 1000BASE-T | 1 Gbit/s |
| Cat6 | 250 MHz | 1000BASE-T, 10GBASE-T* | 10 Gbit/s (55m) |
| Cat6a | 500 MHz | 10GBASE-T | 10 Gbit/s (100m) |
| Cat7 | 600 MHz | 10GBASE-T | 10 Gbit/s |
| Cat7a | 1000 MHz | 10GBASE-T+ | 10+ Gbit/s |
| Cat8 | 2000 MHz | 25/40GBASE-T | 40 Gbit/s (30m) |

### Stecker: RJ45

![[Stecker_RJ45_568B.jpg|300]]
*<span class="fig-id">03-03-04-01-stecker-rj45-568b</span>: RJ45-Stecker mit T568B Farbcodierung. Quelle: Wikimedia Commons.*

![[rj45-pinbelegung.png]]
*<span class="fig-id">03-03-04-01-rj45-pinbelegung</span>: RJ45-Stecker (8P8C) mit T568B-Pinbelegung.*

**Pinbelegung T568A vs. T568B:**

| Pin | T568B (Standard) | T568A | Funktion (100M) | Funktion (1G) |
|-----|------------------|-------|-----------------|---------------|
| 1 | Weiß/Orange | Weiß/Grün | TX+ | BI_DA+ |
| 2 | Orange | Grün | TX- | BI_DA- |
| 3 | Weiß/Grün | Weiß/Orange | RX+ | BI_DB+ |
| 4 | Blau | Blau | – | BI_DC+ |
| 5 | Weiß/Blau | Weiß/Blau | – | BI_DC- |
| 6 | Grün | Orange | RX- | BI_DB- |
| 7 | Weiß/Braun | Weiß/Braun | – | BI_DD+ |
| 8 | Braun | Braun | – | BI_DD- |

> [!info] Hinweis
> Bei 100BASE-TX werden nur Paare 1-2 und 3-6 verwendet. Bei 1000BASE-T sind alle 4 Paare bidirektional aktiv.

## Glasfaserkabel

### Funktionsprinzip

Glasfaser überträgt Daten als **Lichtimpulse** durch Totalreflexion im Glasfaserkern:

![[glasfaser-aufbau.png]]
*<span class="fig-id">03-03-04-01-glasfaser-aufbau</span>: Glasfaser-Querschnitt (Core, Cladding, Mantel) und Totalreflexion der Lichtwelle.*

### Singlemode vs. Multimode

| Eigenschaft | Singlemode (SMF) | Multimode (MMF) |
|-------------|------------------|-----------------|
| Kerndurchmesser | 9 µm | 50 oder 62,5 µm |
| Lichtquelle | Laser | LED oder VCSEL |
| Wellenlänge | 1310 nm, 1550 nm | 850 nm, 1300 nm |
| Reichweite | bis 100 km | bis 2 km |
| Bandbreite | Sehr hoch | Begrenzt |
| Kosten | Höher | Niedriger |
| Typischer Einsatz | WAN, Backbone | LAN, Rechenzentrum |
| Farbcodierung | Gelb | Orange (OM1/2), Aqua (OM3/4), Lime (OM5) |

### Faserklassen nach IEEE 802.3

Die Faserklassen definieren die standardisierten Eigenschaften von Glasfaserkabeln und deren maximale Reichweiten bei verschiedenen Übertragungsgeschwindigkeiten. Die Klassifizierung unterscheidet zwischen **OS** (Optical Singlemode) und **OM** (Optical Multimode):

- **OS2**: Singlemode-Faser für Weitverkehr – erreicht bei allen Geschwindigkeiten bis zu 40 km
- **OM1/OM2**: Ältere Multimode-Fasern mit 62,5 bzw. 50 µm Kern – nur für 1G/10G geeignet
- **OM3/OM4**: Moderne laseroptimierte Multimode-Fasern – unterstützen 40G und 100G
- **OM5**: Breitband-Multimode für SWDM (Short Wavelength Division Multiplexing) – nutzt 4 Wellenlängen parallel

![[faserklassen.png]]
*<span class="fig-id">03-03-04-01-faserklassen</span>: Übersicht der Glasfaser-Klassen mit maximalen Reichweiten nach IEEE 802.3.*

> [!tip] Farbcodierung
> Die Mantelfarbe der Kabel entspricht der Faserklasse: **Gelb** = Singlemode (OS2), **Orange** = OM1/OM2, **Aqua/Türkis** = OM3, **Violett** = OM4, **Lime-Grün** = OM5.

### Glasfaser-Steckertypen

![[SC-optical-fiber-connector-hdr-0a.jpg|300]]
*<span class="fig-id">03-03-04-01-sc-connector</span>: SC-Stecker (Subscriber Connector). Quelle: Wikimedia Commons.*

![[LWLLCSTECKER.jpg|300]]
*<span class="fig-id">03-03-04-01-lc-connector</span>: LC-Stecker (Lucent Connector). Quelle: Wikimedia Commons.*

![[ST-optical-fiber-connector-hdr-0a.jpg|300]]
*<span class="fig-id">03-03-04-01-st-connector</span>: ST-Stecker (Straight Tip). Quelle: Wikimedia Commons.*

![[MPO_Stecker_HR_crop.jpg|300]]
*<span class="fig-id">03-03-04-01-mpo-connector</span>: MPO/MTP-Stecker für Multifaser-Verbindungen. Quelle: Wikimedia Commons.*

![[E2000-Connector.jpg|300]]
*<span class="fig-id">03-03-04-01-e2000-connector</span>: E2000-Stecker mit Schutzkappe. Quelle: Wikimedia Commons.*

![[glasfaser-stecker.png]]
*<span class="fig-id">03-03-04-01-glasfaser-stecker</span>: Gängige Glasfaser-Steckertypen – SC, LC, ST und MPO/MTP.*

**Stecker-Übersicht:**

| Stecker | Form | Anwendung | Besonderheit |
|---------|------|-----------|--------------|
| **SC** | Rechteckig | LAN, FTTH | Push-Pull |
| **LC** | Klein | Rechenzentrum, SFP | Halb so groß wie SC |
| **ST** | Rund | Ältere Netze | Bajonettverschluss |
| **MPO/MTP** | Mehrfach | 40G/100G+ | 12/24 Fasern parallel |

**Politur (Ferrule-Ende):**

| Typ | Beschreibung | Farbcodierung |
|-----|--------------|---------------|
| **PC** | Physical Contact – leicht gewölbt | Blau |
| **UPC** | Ultra PC – stärker poliert | Blau |
| **APC** | Angled PC – 8° Winkel, weniger Reflexion | Grün |

### Ferrule-Schliff (Politur)

Die Qualität der Glasfaser-Verbindung hängt wesentlich vom **Schliff der Ferrule** (Steckerendfläche) ab:

**Gerade Politur (PC/UPC):**
- Die Endfläche ist senkrecht zur Faserachse poliert
- **PC** (Physical Contact): Leicht konvex, minimiert Luftspalte
- **UPC** (Ultra Physical Contact): Feiner poliert, geringere Rückflussdämpfung (~-55 dB)
- Farbcodierung: **Blau**

**Schrägschliff (APC):**
- Die Endfläche ist um **8°** zur Faserachse geneigt
- Reflektiertes Licht wird in den Mantel abgelenkt statt zurück in den Kern
- Sehr geringe Rückflussdämpfung (~-65 dB)
- Farbcodierung: **Grün**
- Wichtig für analoge Signale (CATV) und empfindliche Anwendungen

> [!warning] Achtung
> APC- und UPC-Stecker sind **nicht kompatibel**! Das Verbinden führt zu Beschädigung der Ferrule und hohen Verlusten.

| Eigenschaft | PC/UPC (Gerade) | APC (Schräg) |
|-------------|-----------------|--------------|
| Schliffwinkel | 0° | 8° |
| Rückflussdämpfung | -40 bis -55 dB | -60 bis -65 dB |
| Farbcodierung | Blau | Grün |
| Anwendung | Daten, Digital-TV | CATV, FTTH, PON |
| Kompatibilität | Nur mit PC/UPC | Nur mit APC |

## Transceiver und Schnittstellen

### GBIC und SFP

**GBIC** (Gigabit Interface Converter) und **SFP** (Small Form-factor Pluggable) sind austauschbare Transceiver-Module, die elektrische Signale in optische (oder andere) Signale umwandeln.

![[NORTEL_AA1419001_SC_connectorGBIC.jpg|300]]
*<span class="fig-id">03-03-04-01-gbic</span>: GBIC-Modul mit SC-Stecker. Quelle: Wikimedia Commons.*

![[Mini_GBIC_Transceiver_IMGP7824_wp.jpg|300]]
*<span class="fig-id">03-03-04-01-sfp</span>: SFP-Modul (Mini-GBIC) mit LC-Stecker. Quelle: Wikimedia Commons.*

| Eigenschaft | GBIC | SFP (Mini-GBIC) | SFP+ | QSFP/QSFP+ |
|-------------|------|-----------------|------|------------|
| Größe | Groß | Klein | Klein | Mittel |
| Geschwindigkeit | 1 Gbit/s | 1 Gbit/s | 10 Gbit/s | 40/100 Gbit/s |
| Stecker | SC | LC | LC | MPO/LC |
| Status | Veraltet | Standard | Standard | Aktuell |

**Transceiver-Typen nach Medium:**

| Bezeichnung | Medium | Wellenlänge | Reichweite |
|-------------|--------|-------------|------------|
| **SX** | Multimode | 850 nm | 550 m |
| **LX** | Singlemode | 1310 nm | 10 km |
| **ZX** | Singlemode | 1550 nm | 80 km |
| **T** | Kupfer (RJ45) | – | 100 m |
| **CWDM/DWDM** | Singlemode | Diverse | 40-120 km |

> [!info] Hot-Pluggable
> SFP-Module können im laufenden Betrieb gewechselt werden (Hot-Swap), was die Flexibilität bei der Netzwerkkonfiguration erhöht.

## Netzwerkgeräte (Layer 1)

### Netzwerkkarte (NIC)

Die **Network Interface Card** (NIC) ist die physikalische Schnittstelle zwischen Computer und Netzwerk.

![[gb_network_pci_card.jpg|300]]
*<span class="fig-id">03-03-04-01-nic</span>: PCI-Netzwerkkarte mit RJ45-Anschluss. Quelle: Wikimedia Commons.*

![[host-bus-adapter.jpg|300]]
*<span class="fig-id">03-03-04-01-hba</span>: Host-Bus-Adapter (HBA) für Fibre-Channel-Anbindung. Quelle: Wikimedia Commons.*

**Funktionen:**
- Serialisierung/Deserialisierung von Daten
- Leitungscodierung (z.B. Manchester, 4B5B)
- Taktrückgewinnung
- Kollisionserkennung (bei Half-Duplex)
- MAC-Adresse (eindeutige Hardware-Adresse)

**Formfaktoren:**

| Formfaktor | Beschreibung |
|------------|--------------|
| **PCI/PCIe** | Steckkarte für Desktop-PCs |
| **Onboard** | Integriert auf dem Mainboard |
| **USB** | Externe Adapter |
| **M.2** | Kompakte Steckkarten (Notebooks) |

### Switches und Hubs

![[Netgear_Gigabit_Switch_5-port.jpg|300]]
*<span class="fig-id">03-03-04-01-switch</span>: 5-Port Gigabit-Switch. Quelle: Wikimedia Commons.*

![[RJ45_Switch_Ports.jpg|300]]
*<span class="fig-id">03-03-04-01-switch-ports</span>: RJ45-Ports eines Ethernet-Switches. Quelle: Wikimedia Commons.*

| Gerät | Layer | Funktion | Kollisionsdomäne |
|-------|-------|----------|------------------|
| **Hub** | 1 | Signalverstärkung, Broadcast | Gemeinsam |
| **Switch** | 2 | MAC-basierte Weiterleitung | Pro Port |
| **Repeater** | 1 | Signalverstärkung | Gemeinsam |

> [!info] Hub vs. Switch
> **Hubs** sind heute praktisch ausgestorben. Sie leiteten Signale an alle Ports weiter (Broadcast). **Switches** lernen MAC-Adressen und leiten Frames nur an den Ziel-Port weiter (Unicast), was die Bandbreite deutlich erhöht.

## Koaxialkabel (historisch)

Koaxialkabel wurden in frühen Ethernet-Netzen verwendet:

![[bnc_tee_connector.jpg|300]]
*<span class="fig-id">03-03-04-01-bnc-tee</span>: BNC-T-Stück für 10BASE2 (Thin Ethernet). Quelle: Wikimedia Commons.*

| Standard | Kabeltyp | Bezeichnung | Max. Länge |
|----------|----------|-------------|------------|
| 10BASE5 | RG-8 (Thick Coax) | Yellow Cable | 500 m |
| 10BASE2 | RG-58 (Thin Coax) | Cheapernet | 185 m |

> [!info] Heute
> Koaxialkabel werden in der Netzwerktechnik kaum noch verwendet, sind aber im Kabel-TV/Internet-Bereich (DOCSIS) weiterhin verbreitet.

### Media Access Unit (MAU)

Die **MAU** (Media Access Unit) war ein wichtiges Gerät in frühen Ethernet-Netzwerken (10BASE5, 10BASE2). Sie diente als Schnittstelle zwischen dem Endgerät und dem Koaxialkabel.

![[ThicknetTransceiver.jpg|300]]
*<span class="fig-id">03-03-04-01-thicknet-transceiver</span>: Thicknet-Transceiver (MAU) für 10BASE5. Quelle: Wikimedia Commons.*

**Funktionen der MAU:**
- **Signalumwandlung** zwischen AUI (Attachment Unit Interface) und Koaxialkabel
- **Kollisionserkennung** auf dem gemeinsamen Medium
- **Jabber-Kontrolle** (Erkennung von Dauersendern)

| MAU-Typ | Standard | Medium | Anschluss |
|---------|----------|--------|-----------|
| 10BASE5 | Thick Ethernet | RG-8 Koax | Vampire Tap |
| 10BASE2 | Thin Ethernet | RG-58 Koax | BNC T-Stück |
| 10BASE-T | Twisted Pair | Cat3+ | RJ45 |
| 10BASE-FL | Glasfaser | Multimode | ST |

> [!info] Historisch
> MAUs wurden mit dem Übergang zu integrierten Netzwerkkarten und Switches obsolet. Das Konzept lebt in modernen SFP-Modulen weiter.

## Drahtlose Medien

### WLAN (IEEE 802.11)

→ Siehe auch: [[../../02-Standards-und-Gremien/02-IEEE-Standards#IEEE 802.11 – WLAN/WiFi|IEEE 802.11 Standards]]

| Frequenzband | Eigenschaften |
|--------------|---------------|
| 2,4 GHz | Bessere Reichweite, mehr Interferenzen, weniger Kanäle |
| 5 GHz | Höhere Bandbreite, kürzere Reichweite, mehr Kanäle |
| 6 GHz | Nur WiFi 6E/7, noch weniger Interferenzen |

### Weitere drahtlose Technologien

| Technologie | Frequenz | Reichweite | Anwendung |
|-------------|----------|------------|-----------|
| Bluetooth | 2,4 GHz | 10-100 m | PAN, Peripherie |
| ZigBee | 2,4 GHz | 10-100 m | IoT, Smart Home |
| LTE/5G | Diverse | km-Bereich | Mobilfunk |
| Richtfunk | Diverse | km-Bereich | Backbone |

## Vergleich der Medien

| Medium | Bandbreite | Reichweite | Störanfällig | Kosten | Sicherheit |
|--------|------------|------------|--------------|--------|------------|
| UTP | Bis 40 Gbit/s | 100 m | Mittel | Niedrig | Niedrig |
| STP | Bis 40 Gbit/s | 100 m | Gering | Mittel | Mittel |
| Multimode | Bis 400 Gbit/s | 2 km | Sehr gering | Mittel | Hoch |
| Singlemode | Bis 400 Gbit/s | 100 km | Sehr gering | Hoch | Hoch |
| WLAN | Bis 46 Gbit/s | 100 m | Hoch | Niedrig | Mittel |

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **Twisted Pair** (Cat5e bis Cat8) ist das häufigste LAN-Medium
> - **Glasfaser** bietet höchste Bandbreite und Reichweite
> - **Singlemode** für Weitstrecken, **Multimode** für kurze Distanzen
> - **RJ45** ist der Standard-Stecker für Kupfer-Ethernet
> - **LC** und **SC** sind gängige Glasfaser-Stecker
> - **WLAN** bietet Flexibilität, aber geringere Sicherheit

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Kabelkategorien (Cat5e, Cat6, Cat6a) und ihre Geschwindigkeiten
> - Verstehen Sie den Unterschied Singlemode vs. Multimode
> - Können Sie T568A/B Pinbelegung erklären
> - Wissen Sie, welche Reichweiten die verschiedenen Medien haben

## Verwandte Themen

- [[02-Signale]] – Leitungscodierung und Modulation
- [[../05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] – Ethernet-Frames
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE Standards]] – 802.3, 802.11

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- TIA/EIA-568 – Verkabelungsstandards
