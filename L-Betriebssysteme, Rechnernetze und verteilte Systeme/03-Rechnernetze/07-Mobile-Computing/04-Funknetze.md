---
author: Andreas Hümmer
title: Funknetze und Reichweiten
tags:
  - content
  - rn
  - mobile-computing
  - wireless
  - wlan
  - lte
  - 5g
  - bluetooth
created: '2026-10-24'
modified: '2026-10-29'
bereich: RN
---

# Funknetze und Reichweiten

## Lernziele

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Funknetze nach Reichweite klassifizieren (PAN, LAN, MAN, WAN)
> - Mobilfunkgenerationen (2G-5G) unterscheiden
> - WLAN-Standards und ihre Eigenschaften benennen
> - Kurzstreckenfunk (Bluetooth, NFC) einordnen
> - LPWAN-Technologien für IoT erklären

## Klassifikation nach Reichweite

| Reichweite | Kategorie | Technologien |
|------------|-----------|--------------|
| < 10 m | **PAN** (Personal) | NFC, Bluetooth, ZigBee |
| 10-100 m | **LAN** (Local) | WLAN/WiFi, DECT |
| 100 m - 10 km | **MAN** (Metropolitan) | LPWAN, LoRaWAN |
| > 10 km | **WAN** (Wide) | GSM, LTE, 5G, Satellit |

## WAN – Zelluläre Mobilfunknetze

### Mobilfunkgenerationen

| Generation | Name | Einführung | Max. Datenrate | Merkmale |
|------------|------|------------|----------------|----------|
| **1G** | AMPS, C-Netz | 1980er | Nur Sprache | Analog |
| **2G** | GSM | 1991 | 9,6 kbit/s | Digital, SMS |
| **2.5G** | GPRS | 2000 | 53,6 kbit/s | Paketdaten |
| **2.75G** | EDGE | 2003 | 236 kbit/s | Verbesserte Modulation |
| **3G** | UMTS | 2004 | 384 kbit/s | Breitband |
| **3.5G** | HSPA | 2006 | 14,4 Mbit/s | High Speed Packet Access |
| **3.75G** | HSPA+ | 2008 | 42 Mbit/s | Dual Carrier |
| **4G** | LTE | 2010 | 150 Mbit/s | All-IP, OFDMA |
| **4.5G** | LTE-A | 2013 | 1 Gbit/s | Carrier Aggregation |
| **5G** | NR | 2019 | 20 Gbit/s | mmWave, MIMO, Low Latency |

### GSM (2G)

> [!info] GSM – Global System for Mobile Communications
> GSM war der erste digitale Mobilfunkstandard und ist noch heute weltweit in Betrieb (wird aber abgeschaltet).

**Architektur:**

![[gsm-architecture.png]]
*<span class="fig-id">03-07-04-gsm-architecture</span>: GSM-Netzarchitektur – vom Mobilgerät (MS) über Basisstationen (BTS/BSC) zur Vermittlung (MSC) und ins Festnetz.*

**Frequenzen:** 900 MHz, 1800 MHz
**Zellgröße:** 2-35 km

### LTE (4G)

> [!info] LTE – Long Term Evolution
> LTE ist ein vollständig IP-basiertes Netz (All-IP) mit deutlich höheren Datenraten und geringerer Latenz als 3G.

**Merkmale:**
- **OFDMA** (Orthogonal Frequency Division Multiple Access) im Downlink
- **SC-FDMA** (Single Carrier FDMA) im Uplink
- **MIMO** (Multiple Input Multiple Output) – mehrere Antennen
- Latenz: 10-50 ms
- Frequenzen: 700-2600 MHz

### 5G (NR – New Radio)

**5G Use Cases:**

- **eMBB** (enhanced Mobile Broadband)
  - Bis 20 Gbit/s Datenrate
  - 4K/8K Video, VR/AR
  
- **mMTC** (massive Machine Type Communications)
  - Bis 1 Mio. Geräte/km²
  - IoT, Sensoren, Smart City
  
- **URLLC** (Ultra Reliable Low Latency Communications)
  - < 1 ms Latenz
  - 99,999% Zuverlässigkeit
  - Autonomes Fahren, Industrie 4.0

**5G Frequenzbereiche:**

| Band | Frequenz | Reichweite | Datenrate | Anwendung |
|------|----------|------------|-----------|-----------|
| **Low-Band** | < 1 GHz | Groß (km) | Mittel | Flächenabdeckung |
| **Mid-Band** | 1-6 GHz | Mittel | Hoch | Städtische Gebiete |
| **High-Band (mmWave)** | 24-100 GHz | Gering (m) | Sehr hoch | Hotspots, Stadien |

## LAN – WLAN/WiFi

### WLAN-Standards (IEEE 802.11)

| Standard | Frequenz | Max. Datenrate | Reichweite | Jahr |
|----------|----------|----------------|------------|------|
| **802.11b** | 2,4 GHz | 11 Mbit/s | 35 m | 1999 |
| **802.11a** | 5 GHz | 54 Mbit/s | 25 m | 1999 |
| **802.11g** | 2,4 GHz | 54 Mbit/s | 35 m | 2003 |
| **802.11n** (WiFi 4) | 2,4/5 GHz | 600 Mbit/s | 50 m | 2009 |
| **802.11ac** (WiFi 5) | 5 GHz | 6,9 Gbit/s | 35 m | 2013 |
| **802.11ax** (WiFi 6) | 2,4/5/6 GHz | 9,6 Gbit/s | 35 m | 2019 |
| **802.11be** (WiFi 7) | 2,4/5/6 GHz | 46 Gbit/s | 35 m | 2024 |

### WLAN-Architektur

![[wlan-modi.png]]
*<span class="fig-id">03-07-04-wlan-modi</span>: WLAN-Betriebsmodi – Infrastructure Mode mit zentralem Access Point vs. Ad-hoc Mode mit direkter Peer-to-Peer-Kommunikation.*

### DECT

> [!info] DECT – Digital Enhanced Cordless Telecommunications
> Standard für schnurlose Telefone im Heimbereich.

- Frequenz: 1880-1900 MHz (Europa)
- Reichweite: 50 m indoor, 300 m outdoor
- Verschlüsselung: DSAA (optional)

**Kanalzugriff:** DECT verwendet TDMA/FDMA mit 10 Trägerfrequenzen und 24 Zeitschlitzen pro Träger (12 Duplex-Kanäle). Ein Rahmen dauert 10 ms – die ersten 12 Slots dienen dem Downlink (Basisstation → Mobilteil), die letzten 12 dem Uplink.

## MAN – LPWAN für IoT

### LoRaWAN

> [!info] LoRaWAN – Long Range Wide Area Network
> Speziell für IoT-Anwendungen mit geringem Datenaufkommen und langer Batterielaufzeit.

| Eigenschaft | Wert |
|-------------|------|
| **Reichweite** | 2-15 km (urban), bis 40 km (rural) |
| **Datenrate** | 0,3-50 kbit/s |
| **Frequenz** | 868 MHz (EU), 915 MHz (US) |
| **Batterielaufzeit** | Bis zu 10 Jahre |
| **Anwendungen** | Sensoren, Smart Metering, Tracking |

### Weitere LPWAN-Technologien

| Technologie | Reichweite | Datenrate | Lizenz |
|-------------|------------|-----------|--------|
| **LoRaWAN** | 2-40 km | 50 kbit/s | Unlizenziert |
| **Sigfox** | 3-50 km | 100 bit/s | Proprietär |
| **NB-IoT** | 1-10 km | 250 kbit/s | Lizenziert (LTE) |
| **LTE-M** | 1-10 km | 1 Mbit/s | Lizenziert (LTE) |

## PAN – Kurzstreckenfunk

### Bluetooth

| Version | Datenrate | Reichweite | Merkmale |
|---------|-----------|------------|----------|
| **1.0** | 1 Mbit/s | 10 m | Erste Version |
| **2.0 + EDR** | 3 Mbit/s | 10 m | Enhanced Data Rate |
| **4.0 (BLE)** | 1 Mbit/s | 50 m | Low Energy |
| **5.0** | 2 Mbit/s | 200 m | IoT-optimiert |
| **5.2** | 2 Mbit/s | 200 m | LE Audio |

**Bluetooth-Klassen:**

| Klasse | Sendeleistung | Reichweite |
|--------|---------------|------------|
| Class 1 | 100 mW | 100 m |
| Class 2 | 2,5 mW | 10 m |
| Class 3 | 1 mW | 1 m |

### NFC – Near Field Communication

> [!info] NFC
> Kontaktlose Kommunikation über sehr kurze Distanz (< 10 cm).

| Eigenschaft | Wert |
|-------------|------|
| **Frequenz** | 13,56 MHz |
| **Reichweite** | < 10 cm |
| **Datenrate** | 424 kbit/s |
| **Modi** | Passiv (Tag), Aktiv (P2P), Card Emulation |

**Anwendungen:**
- Kontaktloses Bezahlen (Apple Pay, Google Pay)
- Zutrittskontrolle
- Pairing von Bluetooth-Geräten
- Digitale Visitenkarten

### ZigBee (IEEE 802.15.4)

- Frequenz: 2,4 GHz
- Reichweite: 10-100 m
- Datenrate: 250 kbit/s
- Anwendung: Smart Home, Industrieautomation
- Mesh-Netzwerk-fähig

## Vergleichsübersicht

| Technologie | Reichweite | Datenrate | Energieverbrauch | Anwendung |
|-------------|------------|-----------|------------------|-----------|
| **NFC** | < 10 cm | 424 kbit/s | Sehr gering | Bezahlen |
| **Bluetooth** | 10-200 m | 2 Mbit/s | Gering | Audio, Wearables |
| **ZigBee** | 10-100 m | 250 kbit/s | Sehr gering | Smart Home |
| **WLAN** | 50-100 m | 9,6 Gbit/s | Hoch | Internet |
| **LoRaWAN** | 2-40 km | 50 kbit/s | Sehr gering | IoT-Sensoren |
| **LTE** | 2-35 km | 1 Gbit/s | Hoch | Mobile Breitband |
| **5G** | 0,1-10 km | 20 Gbit/s | Hoch | Alles |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Klassifikation: PAN, LAN, MAN, WAN
> - Mobilfunkgenerationen 2G-5G und ihre Merkmale
> - WLAN-Standards (802.11 a/b/g/n/ac/ax)
> - Kurzstreckenfunk: Bluetooth, NFC
> - LPWAN für IoT: LoRaWAN, NB-IoT

> [!question] Typische Prüfungsfragen
> - Ordnen Sie folgende Technologien nach Reichweite: NFC, WLAN, LTE, Bluetooth
> - Was sind die drei Use Cases von 5G (eMBB, mMTC, URLLC)?
> - Welcher WLAN-Standard verwendet welche Frequenz?
> - Wofür eignet sich LoRaWAN besonders?
> - Was ist der Unterschied zwischen Bluetooth Classic und BLE?

## Zusammenhänge

- [[01-Einfuehrung]] – Grundlagen Mobile Computing
- [[02-Kommunikation]] – Kommunikationsanforderungen
- [[03-Standortbestimmung]] – Ortung via Funkzellen
- [[05-Kanalaufteilung]] – Multiplexing-Verfahren
- [[../04-Bitübertragungsschicht/01-Uebertragungsmedien|Übertragungsmedien]] – Physikalische Grundlagen

## Quellen

- IEEE 802.11 Standards
- 3GPP Specifications (LTE, 5G)
- Bluetooth SIG
- LoRa Alliance

---

*Dateiende*
