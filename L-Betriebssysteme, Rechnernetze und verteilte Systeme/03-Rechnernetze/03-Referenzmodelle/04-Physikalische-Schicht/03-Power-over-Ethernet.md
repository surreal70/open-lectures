---
author: Andreas Hümmer
title: Power over Ethernet (PoE)
tags:
  - vorlesung
  - rn
  - layer1
  - poe
  - stromversorgung
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Power over Ethernet (PoE)

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Das Prinzip von Power over Ethernet erklären
> - Die verschiedenen PoE-Standards und ihre Leistungsklassen unterscheiden
> - Die beiden Einspeisungsverfahren (Mode A und Mode B) beschreiben
> - Typische Anwendungsfälle für PoE nennen
> - Die Vorteile und Einschränkungen von PoE bewerten

## Einführung

**Power over Ethernet (PoE)** ermöglicht die gleichzeitige Übertragung von Daten und elektrischer Energie über ein einziges Ethernet-Kabel. Dadurch entfällt für viele Endgeräte ein separates Netzteil.

> [!info] Vorteile von PoE
> - **Vereinfachte Installation**: Nur ein Kabel für Daten und Strom
> - **Zentrale Stromversorgung**: USV-Schutz für alle PoE-Geräte möglich
> - **Flexibilität**: Geräte können dort installiert werden, wo keine Steckdose verfügbar ist
> - **Kosteneinsparung**: Weniger Verkabelung, keine separaten Netzteile
> - **Fernsteuerung**: Geräte können remote neu gestartet werden

## PoE-Standards (IEEE 802.3)

| Standard | Bezeichnung | Max. Leistung (PSE) | Max. Leistung (PD) | Paare | Jahr |
|----------|-------------|---------------------|---------------------|-------|------|
| IEEE 802.3af | PoE | 15,4 W | 12,95 W | 2 | 2003 |
| IEEE 802.3at | PoE+ | 30 W | 25,5 W | 2 | 2009 |
| IEEE 802.3bt Type 3 | PoE++ / 4PPoE | 60 W | 51 W | 4 | 2018 |
| IEEE 802.3bt Type 4 | PoE++ / 4PPoE | 100 W | 71 W | 4 | 2018 |

> [!info] Leistungsverlust
> Die Differenz zwischen PSE- und PD-Leistung entsteht durch Leitungsverluste im Kabel. Bei 100 m Kabellänge und Cat5e können bis zu 20% der Leistung verloren gehen.

## Komponenten

### Power Sourcing Equipment (PSE)

Das **PSE** ist die Stromquelle und speist die Energie ins Ethernet-Kabel ein:

- **Endspan (PoE-Switch)**: Switch mit integrierter PoE-Funktion
- **Midspan (PoE-Injektor)**: Separates Gerät zwischen Switch und Endgerät

### Powered Device (PD)

Das **PD** ist das Endgerät, das über PoE mit Strom versorgt wird:

- IP-Telefone
- WLAN Access Points
- IP-Kameras (Überwachung)
- IoT-Sensoren
- Thin Clients
- LED-Beleuchtung

## Einspeisungsverfahren

### Mode A (Phantomspeisung)

Bei **Mode A** wird die Spannung über die datenführenden Paare übertragen:

| Paar | Pins | Funktion | Polarität |
|------|------|----------|-----------|
| 1 | 1, 2 | TX (Daten + Strom) | + |
| 2 | 3, 6 | RX (Daten + Strom) | − |

- Funktioniert mit 10/100BASE-T (nur 2 Paare für Daten)
- Strom wird als Gleichtakt-Signal (Common Mode) aufmoduliert
- Transformatoren im Ethernet-Interface trennen Daten und Strom

### Mode B (Spare Pair)

Bei **Mode B** werden die ungenutzten Adernpaare für die Stromversorgung verwendet:

| Paar | Pins | Funktion |
|------|------|----------|
| 3 | 4, 5 | Nur Strom (+) |
| 4 | 7, 8 | Nur Strom (−) |

- Einfacher zu implementieren
- Nutzt bei 10/100BASE-T die "Spare Pairs"
- Bei Gigabit Ethernet (alle 4 Paare für Daten) wird Mode A oder Kombination verwendet

### 4-Pair PoE (IEEE 802.3bt)

Ab **PoE++** werden alle 4 Adernpaare sowohl für Daten als auch für Strom verwendet:

- Mode A auf Paaren 1 und 2
- Mode B auf Paaren 3 und 4
- Ermöglicht höhere Leistung (bis 100 W)

## Leistungsklassen

Das PSE erkennt automatisch den Leistungsbedarf des PD durch einen Klassifizierungsprozess:

| Klasse | Max. Leistung (PD) | Typische Anwendung |
|--------|--------------------|--------------------|
| 0 | 12,95 W | Standard (Klasse unbekannt) |
| 1 | 3,84 W | VoIP-Telefone |
| 2 | 6,49 W | IP-Kameras (einfach) |
| 3 | 12,95 W | WLAN Access Points |
| 4 | 25,5 W | PTZ-Kameras, Video-Telefone |
| 5 | 40 W | High-Power Access Points |
| 6 | 51 W | Laptops, Thin Clients |
| 7 | 62 W | LED-Displays |
| 8 | 71 W | Laptops mit hoher Leistung |

## Erkennung und Handshake

Bevor Strom geliefert wird, führt das PSE einen **Erkennungsprozess** durch:

1. **Detection**: PSE legt kleine Spannung an und misst Widerstand
   - Gültiges PD: 25 kΩ Signaturwiderstand
   - Ungültiges Gerät: Kein oder falscher Widerstand → kein Strom
   
2. **Classification**: PSE ermittelt Leistungsbedarf des PD
   - PD signalisiert Klasse durch definierten Stromfluss
   
3. **Power-Up**: PSE schaltet Versorgungsspannung frei
   - Nominale Spannung: 48 V DC (44–57 V)
   
4. **Operation**: Kontinuierliche Überwachung
   - Unterschreitung des Mindeststroms → Abschaltung (Disconnect)

> [!warning] Sicherheit
> Der Erkennungsmechanismus verhindert, dass nicht-PoE-fähige Geräte beschädigt werden. Niemals versuchen, PoE-Spannung direkt an Geräte anzuschließen!

## Kabelanforderungen

| Standard | Mindest-Kabelkategorie | Max. Länge |
|----------|------------------------|------------|
| PoE (802.3af) | Cat3 | 100 m |
| PoE+ (802.3at) | Cat5 | 100 m |
| PoE++ (802.3bt) | Cat5e (empfohlen: Cat6) | 100 m |

> [!tip] Empfehlung
> Für PoE++ sollte mindestens **Cat6** verwendet werden, um Wärmeverluste zu minimieren. Dickere Adern (AWG23 statt AWG24) reduzieren den Widerstand und damit die Verlustleistung.

## Anwendungsbeispiele

### Typische PoE-Geräte

| Gerät | Typische Leistung | PoE-Standard |
|-------|-------------------|--------------|
| VoIP-Telefon | 3–5 W | PoE |
| WLAN Access Point | 10–15 W | PoE / PoE+ |
| IP-Kamera (fest) | 5–10 W | PoE |
| PTZ-Kamera | 20–30 W | PoE+ |
| Videokonferenz-System | 30–50 W | PoE++ |
| Thin Client | 40–60 W | PoE++ |

### Netzwerkdesign mit PoE

![[poe-netzwerk.png]]
*<span class="fig-id">03-03-04-03-poe-netzwerk</span>: PoE-Netzwerk mit zentraler Stromversorgung – alle Endgeräte erhalten Daten und Strom über ein Kabel.*

## Vorteile und Einschränkungen

### Vorteile

- ✅ Vereinfachte Installation und Verkabelung
- ✅ Zentrale Stromversorgung und USV-Schutz
- ✅ Remote-Management (Neustart, Scheduling)
- ✅ Kostenersparnis bei Installation
- ✅ Flexibilität bei der Gerätepositionierung

### Einschränkungen

- ❌ Begrenzte Leistung (max. 71 W am Gerät)
- ❌ Leitungsverluste bei langen Kabeln
- ❌ Wärmeentwicklung in Kabelbündeln
- ❌ Zusätzliche Kosten für PoE-fähige Switches
- ❌ Nicht für Hochleistungsgeräte geeignet

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **PoE** überträgt Daten und Strom über ein Ethernet-Kabel
> - **IEEE 802.3af/at/bt** definieren Standards mit 15 W bis 100 W
> - **PSE** (Switch/Injektor) versorgt **PD** (Endgerät) mit Strom
> - **Mode A** nutzt Datenpaare, **Mode B** nutzt Spare Pairs
> - **Erkennungsprozess** schützt nicht-PoE-Geräte vor Beschädigung
> - Typische Anwendungen: IP-Telefone, Access Points, Kameras

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> N/A

> [!question] **Typische Prüfungsfragen**
> - Keine typischen Prüfungsfragen zu diesem Thema

## Verwandte Themen

- [[01-Uebertragungsmedien]] – Twisted-Pair-Kabel und RJ45
- [[02-Signale]] – Signalübertragung auf Kupferkabeln
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE Standards]] – 802.3af/at/bt

## Quellen

- IEEE 802.3af-2003, 802.3at-2009, 802.3bt-2018
- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
