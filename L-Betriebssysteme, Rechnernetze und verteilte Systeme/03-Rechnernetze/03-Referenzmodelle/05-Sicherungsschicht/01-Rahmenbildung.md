---
author: Andreas Hümmer
title: Rahmenbildung und Ethernet-Frame
tags:
  - vorlesung
  - rn
  - layer2
  - ethernet
  - frame
  - mac
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Rahmenbildung und Ethernet-Frame

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Aufbau eines Ethernet-Frames erklären
> - MAC-Adressen lesen und interpretieren
> - Den Unterschied zwischen Ethernet II und 802.3 erklären
> - VLAN-Tagging (802.1Q) verstehen
> - Die Bedeutung von MTU und Jumbo Frames erläutern

## Ethernet-Frame-Formate

### Ethernet II (DIX) vs. IEEE 802.3

![[ethernet-frame-formate.png]]
*<span class="fig-id">03-03-05-01-ethernet-frame-formate</span>: Ethernet II (DIX) und IEEE 802.3 Frame-Struktur im Vergleich.*

**Unterscheidung über das Type/Length-Feld:**
- Wert ≤ 1500 (0x05DC) → **Length** (IEEE 802.3)
- Wert ≥ 1536 (0x0600) → **EtherType** (Ethernet II)

> [!info] Heute Standard
> Ethernet II ist heute der de-facto Standard. IEEE 802.3 mit LLC wird nur noch selten verwendet (z.B. bei älteren Protokollen wie NetBEUI oder IPX/SPX).

### Ethernet-Frame im Detail

**Präambel (7 Bytes)**
- Bitfolge: 10101010 10101010 10101010 ... (7×)
- Zweck: Taktsynchronisation des Empfängers

**SFD – Start Frame Delimiter (1 Byte)**
- Bitfolge: 10101011
- Markiert Beginn des eigentlichen Frames

**Destination MAC (6 Bytes)**
- MAC-Adresse des Empfängers
- Kann Unicast, Multicast oder Broadcast sein

**Source MAC (6 Bytes)**
- MAC-Adresse des Senders
- Immer Unicast

**EtherType (2 Bytes)**
- Identifiziert Protokoll der Nutzlast
- 0x0800 = IPv4
- 0x0806 = ARP
- 0x86DD = IPv6
- 0x8100 = 802.1Q VLAN Tag

**Payload (46–1500 Bytes)**
- Nutzdaten (z.B. IP-Paket)
- Minimum 46 Bytes (sonst Padding)
- Maximum 1500 Bytes (MTU)

**FCS – Frame Check Sequence (4 Bytes)**
- CRC-32 Prüfsumme
- Berechnet über Dst MAC bis Payload

> [!info] Framegrößen
> - Ohne Präambel/SFD: **64–1518 Bytes**
> - Mit Präambel/SFD: **72–1526 Bytes**

### Wichtige EtherTypes

| EtherType | Protokoll |
|-----------|-----------|
| 0x0800 | IPv4 |
| 0x0806 | ARP |
| 0x8035 | RARP |
| 0x8100 | 802.1Q VLAN Tag |
| 0x86DD | IPv6 |
| 0x8847 | MPLS Unicast |
| 0x8848 | MPLS Multicast |
| 0x88A8 | 802.1ad (QinQ) |
| 0x88CC | LLDP |

## MAC-Adressen

### Aufbau

![[mac-adresse.png]]
*<span class="fig-id">03-03-05-01-mac-adresse</span>: Aufbau einer MAC-Adresse mit OUI (Hersteller) und NIC (Geräte-ID).*

**Spezielle Bits im ersten Byte:**

![[mac-adresse-bits.png]]
*<span class="fig-id">03-03-05-01-mac-adresse-bits</span>: Position der speziellen Bits im ersten Byte einer MAC-Adresse.*

- **Bit 0 – I/G-Bit (Individual/Group):**
  - 0 = Unicast (Einzeladresse)
  - 1 = Multicast/Broadcast (Gruppenadresse)

- **Bit 1 – U/L-Bit (Universal/Local):**
  - 0 = Universally Administered (OUI von IEEE vergeben)
  - 1 = Locally Administered (lokal zugewiesen)

### Spezielle MAC-Adressen

| Adresse | Bedeutung |
|---------|-----------|
| FF:FF:FF:FF:FF:FF | Broadcast (an alle) |
| 01:00:5E:xx:xx:xx | IPv4 Multicast |
| 33:33:xx:xx:xx:xx | IPv6 Multicast |
| 01:80:C2:00:00:00 | STP (Spanning Tree) |
| 01:80:C2:00:00:0E | LLDP |

### OUI-Beispiele (Hersteller)

| OUI | Hersteller |
|-----|------------|
| 00:00:0C | Cisco |
| 00:1A:A0 | Dell |
| 3C:D9:2B | HP |
| FC:AA:14 | Giga-Byte |
| 00:50:56 | VMware |
| 08:00:27 | VirtualBox |

## VLAN-Tagging (IEEE 802.1Q)

![[vlan-tag.png]]
*<span class="fig-id">03-03-05-01-vlan-tag</span>: Ethernet-Frame mit und ohne 802.1Q VLAN Tag sowie Aufbau des 4-Byte-Tags.*

**Tag-Felder:**

| Feld | Größe | Beschreibung |
|------|-------|--------------|
| **TPID** | 2 Bytes | Tag Protocol Identifier (0x8100) |
| **PCP** | 3 Bit | Priority Code Point (0-7, für QoS) |
| **DEI** | 1 Bit | Drop Eligible Indicator |
| **VID** | 12 Bit | VLAN Identifier (0-4095) |

**Reservierte VLANs:**
- VID 0: Priority Tagged (nur QoS, kein VLAN)
- VID 1: Default VLAN
- VID 4095: Reserviert

> [!info] Frame-Größe
> Mit 802.1Q Tag erhöht sich die maximale Frame-Größe von 1518 auf **1522 Bytes**.

## Padding (Auffüllung)

### Warum Padding?

Ethernet erfordert eine **Mindestframegröße von 64 Bytes** (ohne Präambel/SFD). Der Grund liegt in der Kollisionserkennung (CSMA/CD):

**Problem:** Der Sender muss während der gesamten Übertragung eine mögliche Kollision erkennen können. Das Frame muss mindestens so lange sein, dass es die maximale Netzausdehnung (2× Laufzeit = Round-Trip-Time) überbrückt.

**Slot Time bei 10 Mbps:**
- 51,2 µs = 512 Bit = **64 Bytes**
- Maximale Kabellänge: 2500 m (mit Repeatern)

**Berechnung der Mindestgröße:**

| Feld | Größe |
|------|-------|
| Dst MAC | 6 Bytes |
| Src MAC | 6 Bytes |
| Type | 2 Bytes |
| Payload | **min. 46 Bytes** |
| FCS | 4 Bytes |
| **Gesamt** | **64 Bytes** |

→ Wenn die Nutzdaten kleiner als 46 Bytes sind, wird **Padding** (Null-Bytes) hinzugefügt.

### Wie funktioniert Padding?

![[padding-beispiel.png]]
*<span class="fig-id">03-03-05-01-padding-beispiel</span>: ARP-Frame ohne und mit Padding zur Erreichung der Mindestgröße von 64 Bytes.*

Das Padding besteht aus **Null-Bytes** (0x00).

> [!warning] Wichtig
> - Padding wird vom **Sender** hinzugefügt
> - Padding wird **nicht** als separates Feld im Header markiert
> - Der Empfänger erkennt das echte Payload-Ende anhand des übergeordneten Protokolls (z.B. IP Total Length)

> [!info] Padding bei Gigabit-Ethernet
> Bei Gigabit-Ethernet (1000 Mbps) wäre die Slot Time nur 0,512 µs – viel zu kurz für vernünftige Kabellängen. Daher wird **Carrier Extension** verwendet: Der Frame wird auf mindestens 512 Bytes erweitert (nicht die Nutzdaten, sondern spezielle Extension-Symbole nach dem FCS).

## MTU und Jumbo Frames

| Begriff | Größe | Beschreibung |
|---------|-------|--------------|
| **MTU** | 1500 Bytes | Standard Maximum Transmission Unit |
| **Jumbo Frame** | 9000 Bytes | Für Rechenzentren, reduziert Overhead |
| **Baby Giant** | 1504-1600 Bytes | Leicht vergrößert (für Tags) |

> [!warning] Jumbo Frames
> Jumbo Frames müssen auf **allen** Geräten im Pfad konfiguriert sein. Unterschiedliche MTU-Größen führen zu Fragmentierung oder Paketverlust.

## Leitungskodierung vs. Kanalkodierung

### Begriffsunterscheidung

![[kodierung-schichten.png]]
*<span class="fig-id">03-03-05-01-kodierung-schichten</span>: Einordnung von Kanal- und Leitungskodierung in das Schichtenmodell.*

### Leitungskodierung (Physical Layer – Layer 1)

**Zweck:** Umsetzung von Bits in physikalische Signale

**Anforderungen:**
- Taktrückgewinnung (Synchronisation)
- Gleichstromfreiheit (DC-Balance)
- Geringe Bandbreite
- Fehlererkennung auf Symbolebene

#### Manchester-Kodierung (10BASE-T)

![[Manchester_encoding_both_conventions.svg]]
*<span class="fig-id">03-03-05-01-manchester-kodierung</span>: Manchester-Kodierung in beiden Konventionen (Quelle: Wikipedia).*

- Jedes Bit wird durch einen **Pegelwechsel in der Bitmitte** kodiert
- **IEEE 802.3 (Ethernet):** Steigende Flanke = 1, Fallende Flanke = 0
- **G.E. Thomas:** Steigende Flanke = 0, Fallende Flanke = 1
- **Vorteil:** Takt ist im Signal enthalten (selbsttaktend)
- **Nachteil:** Doppelte Bandbreite nötig (10 Mbps → 20 MHz)

#### 4B/5B + MLT-3 (100BASE-TX)

- 4 Datenbits werden auf 5 Symbole abgebildet
- Garantiert maximal 3 aufeinanderfolgende gleiche Bits
- MLT-3: Drei Pegel (-V, 0, +V) für Signalübertragung
- **Effizienz:** 4/5 = 80% (besser als Manchester mit 50%)

#### 8B/10B (1000BASE-X, Gigabit Ethernet)

- 8 Datenbits → 10 Symbole
- DC-Balance durch Running Disparity
- Spezielle Kontrollsymbole (K-Codes) für Framing
- **Effizienz:** 8/10 = 80%

### Kanalkodierung (Data Link Layer – Layer 2)

**Zweck:** Hinzufügen von Redundanz zur Fehlererkennung/-korrektur

**Fehlererkennung (Detection):**
- Parität (einfach, erkennt 1-Bit-Fehler)
- Prüfsummen (Checksums)
- **CRC (Cyclic Redundancy Check)** ← bei Ethernet!

**Ethernet verwendet CRC-32:**
- 32-Bit Prüfsumme im FCS-Feld
- Erkennt alle 1-Bit, 2-Bit und ungerade Bitfehler
- Erkennt alle Burst-Fehler ≤ 32 Bit
- Fehlerhafte Frames werden verworfen (kein ARQ bei Ethernet)

**Fehlerkorrektur (FEC – Forward Error Correction):**
- Hamming-Code (korrigiert 1-Bit-Fehler)
- Reed-Solomon (Block-Codes, z.B. bei CDs, DVDs)
- Convolutional Codes (Faltungscodes, z.B. bei WLAN)
- LDPC (Low-Density Parity Check, z.B. bei 10GBASE-T)

**Bei Ethernet:**
- Klassisches Ethernet: Nur Fehlererkennung (CRC)
- 10GBASE-T: FEC (LDPC) wegen schlechterer Kanalqualität

![[crc-berechnung.png]]
*<span class="fig-id">03-03-05-01-crc-berechnung</span>: CRC-32 Prüfsumme wird an die Nutzdaten angehängt (FCS-Feld).*

### Vergleich: Leitungs- vs. Kanalkodierung

| Aspekt | Leitungskodierung | Kanalkodierung |
|--------|-------------------|----------------|
| **Schicht** | Layer 1 (Physical) | Layer 2 (Data Link) |
| **Zweck** | Bitdarstellung auf Medium | Fehlerschutz |
| **Redundanz** | Für Synchronisation | Für Integrität |
| **Beispiele** | Manchester, 4B/5B, 8B/10B | CRC, Hamming, LDPC |
| **Bei Ethernet** | 4B/5B (100M), 8B/10B (1G) | CRC-32 (FCS) |

## Übergang Layer 1 ↔ Layer 2: Die Netzwerkkarte (NIC)

### Aufbau einer Netzwerkkarte

![[nic-struktur.png]]
*<span class="fig-id">03-03-05-01-nic-struktur</span>: Aufbau einer Netzwerkkarte (NIC) mit MAC-Controller (Layer 2) und PHY-Chip (Layer 1).*

### Zusammenspiel MAC-Controller und PHY

**MAC-PHY-Schnittstelle (MII/GMII/RGMII)**

**Senden (Host → Medium):**

1. Host übergibt Daten an MAC-Controller
2. **MAC-Controller:**
   - Baut Ethernet-Frame auf (Header + FCS)
   - Prüft ob Medium frei (CSMA/CD bei Half-Duplex)
   - Wartet ggf. auf IFG (Inter-Frame Gap, 96 Bit-Zeiten)
3. MAC übergibt Frame bitweise an PHY (über MII: 4 Bit parallel @ 25 MHz bei 100 Mbps)
4. **PHY-Chip:**
   - Kodiert Bits (z.B. 4B/5B-Kodierung)
   - Wandelt in Signale um (MLT-3 Pegel)
   - Sendet über Transformer auf das Kabel

**Empfangen (Medium → Host):**

1. **PHY-Chip** empfängt Signale vom Kabel:
   - Taktrückgewinnung aus Präambel
   - Dekodierung (z.B. 5B/4B)
   - Übergabe an MAC
2. **MAC-Controller:**
   - Erkennt SFD (Start Frame Delimiter)
   - Prüft Destination MAC (für mich? Broadcast? Multicast?)
   - Prüft FCS (CRC-32)
   - Verwirft bei Fehler oder gibt an Host weiter

### CSMA/CD im Detail (Übergang L1/L2)

![[csma-cd.png]]
*<span class="fig-id">03-03-05-01-csma-cd</span>: CSMA/CD-Ablauf mit Kooperation zwischen Layer 1 (PHY) und Layer 2 (MAC).*

**CSMA/CD = Carrier Sense Multiple Access / Collision Detection**

**Layer 1 (PHY) liefert:**
- Carrier Sense Signal (CRS) – „Medium belegt"
- Collision Detect Signal (COL) – „Kollision erkannt"

**Layer 2 (MAC) steuert:**
- Entscheidung wann senden
- JAM-Signal bei Kollision
- Exponentieller Backoff-Algorithmus

### Exponentieller Backoff (Binary Exponential Backoff)

Nach Kollision Nr. $n$ berechnet sich die Wartezeit wie folgt:

$$
\text{Wartezeit} = k \times \text{Slot Time}, \quad k \in \{0, 1, 2, \ldots, 2^n - 1\}
$$

wobei:
- **Slot Time** = 51,2 µs (bei 10 Mbps) = 512 Bitzeiten
- $k$ wird **zufällig** aus dem Bereich gewählt
- Nach Kollision 10 wird der Bereich bei $2^{10} - 1 = 1023$ **gedeckelt**

| Kollision $n$ | Bereich für $k$ | Max. Wartezeit |
|---------------|-----------------|----------------|
| 1 | $0$ oder $1$ | $1 \times 51{,}2\,\mu s = 51{,}2\,\mu s$ |
| 2 | $0$ bis $3$ | $3 \times 51{,}2\,\mu s = 153{,}6\,\mu s$ |
| 3 | $0$ bis $7$ | $7 \times 51{,}2\,\mu s = 358{,}4\,\mu s$ |
| 4 | $0$ bis $15$ | $15 \times 51{,}2\,\mu s$ |
| ... | ... | ... |
| 10 | $0$ bis $1023$ | $1023 \times 51{,}2\,\mu s \approx 52\,ms$ |
| 11–15 | $0$ bis $1023$ | (gedeckelt) |
| **16** | **ABBRUCH** | Frame wird verworfen |

> [!warning] Abbruch nach 16 Kollisionen
> Nach 16 erfolglosen Sendeversuchen wird die Übertragung abgebrochen und der Frame an die höhere Schicht mit Fehlermeldung zurückgegeben.

> [!info] Full-Duplex und Switches
> Bei modernem Switched Ethernet im **Full-Duplex-Modus** ist CSMA/CD **deaktiviert**, da jeder Port eine dedizierte, kollisionsfreie Verbindung hat. Stattdessen wird **Flow Control** (Pause Frames nach IEEE 802.3x) verwendet.

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Ethernet II ist das heute übliche Frame-Format
> - **MAC-Adressen** sind 48 Bit lang (OUI + NIC)
> - **Broadcast**: FF:FF:FF:FF:FF:FF
> - **EtherType** identifiziert das Nutzlast-Protokoll (0x0800 = IPv4)
> - **802.1Q** fügt 4 Bytes VLAN-Tag hinzu
> - **FCS** enthält CRC-32 zur Fehlererkennung
> - Standard-MTU: **1500 Bytes**

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die Felder eines Ethernet-Frames
> - Verstehen Sie MAC-Adressen (48 Bit, OUI + NIC)
> - Wissen Sie, was Broadcast und Multicast bedeuten
> - Können Sie 802.1Q VLAN-Tagging erklären

## Verwandte Themen

- [[02-Fehlererkennung]] – CRC und FCS
- [[03-MAC-Protokolle]] – Medienzugriffssteuerung
- [[../06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]] – Die Nutzlast des Frames

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- [[07-Anhang/IEEE-802-Standards/IEEE 802.3|IEEE 802.3]] – Ethernet-Standard
