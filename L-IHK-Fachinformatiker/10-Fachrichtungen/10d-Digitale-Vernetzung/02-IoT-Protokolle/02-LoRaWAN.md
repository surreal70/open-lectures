---
title: "LoRaWAN – Long Range Wide Area Network"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11d
  - iot
  - lorawan
  - lora
  - lpwan
  - funkprotokoll
source: proTirone (CC-BY-4.0)
---

# LoRaWAN – Long Range Wide Area Network

> [!info] Lernziele
> - LoRa und LoRaWAN unterscheiden können
> - LoRaWAN-Architektur verstehen
> - Einsatzgebiete und Eigenschaften kennen

## Begriffstrennung

### LoRa (Physical Layer)

**LoRa** (*Long Range*) ist ein proprietäres, patentiertes Funkübertragungsverfahren auf der **Bitübertragungsschicht** (OSI Layer 1).

**Eigenschaften:**
- Entwickelt von Semtech
- Chirp-Spread-Spectrum-Modulation
- Energieeffizient
- Reichweiten über 10 km (ländlich) / 2-5 km (städtisch)
- Datenrate: 292 bit/s bis 50 kbit/s
- Asymmetrische Übertragung

### LoRaWAN (Network Layer)

**LoRaWAN** (*Long Range Wide Area Network*) ist ein offenes Netzwerkprotokoll auf der **Vermittlungsschicht** (OSI Layer 3), das LoRa als Übertragungsverfahren nutzt.

**Eigenschaften:**
- Open-Source-Spezifikation
- Verwaltet von der LoRa Alliance
- 128-bit AES-Verschlüsselung
- Bidirektionale Kommunikation

```
┌─────────────────────────────────────┐
│        LoRaWAN (Layer 3)            │  ← Offener Standard
│   Netzwerkprotokoll, Routing        │
├─────────────────────────────────────┤
│          LoRa (Layer 1)             │  ← Proprietär (Semtech)
│   Funkübertragung, Modulation       │
└─────────────────────────────────────┘
```

## LoRaWAN-Architektur

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Endgerät │    │ Endgerät │    │ Endgerät │
│ (Sensor) │    │ (Sensor) │    │ (Sensor) │
└────┬─────┘    └────┬─────┘    └────┬─────┘
     │LoRa           │LoRa           │LoRa
     └───────────────┼───────────────┘
                     ↓
            ┌────────────────┐
            │   LoRa-Gateway │
            │   (Empfänger)  │
            └───────┬────────┘
                    │ IP/Ethernet
                    ↓
            ┌────────────────┐
            │ LoRaWAN-Server │
            │  (Netzbetreiber)│
            └───────┬────────┘
                    │ API
                    ↓
            ┌────────────────┐
            │ IoT-Plattform  │
            │  (Anwendung)   │
            └────────────────┘
```

### Komponenten

| Komponente | Funktion |
|------------|----------|
| **Endgerät** | Sensor/Aktor mit LoRa-Modul |
| **Gateway** | Empfängt LoRa-Signale, leitet an Server weiter |
| **Network Server** | Routing, Deduplizierung, Sicherheit |
| **Application Server** | Anwendungslogik, Datenverarbeitung |

## Geräteklassen

| Klasse | Empfang | Latenz | Energieverbrauch |
|--------|---------|--------|------------------|
| **A** | Nach eigenem Senden | Hoch | Sehr niedrig |
| **B** | Regelmäßige Zeitfenster | Mittel | Niedrig |
| **C** | Dauerhaft | Niedrig | Hoch |

### Klasse A (Baseline)

```
Endgerät sendet
       │
       ↓
    ┌──────┐     ┌──────┐
    │ RX1  │     │ RX2  │   ← Empfangsfenster
    └──────┘     └──────┘
    1 Sek        2 Sek
    
    Danach: Schlafmodus (Energiesparen)
```

## Frequenzbänder

| Region | Frequenz | Bemerkung |
|--------|----------|-----------|
| Europa | 868 MHz | ISM-Band, lizenzfrei |
| USA | 915 MHz | ISM-Band |
| Asien | 433 MHz | Verschiedene Regelungen |

> [!note] ISM-Band
> Industrial, Scientific, Medical – lizenzfreie Frequenzbänder für industrielle, wissenschaftliche und medizinische Anwendungen.

## Vergleich mit anderen Technologien

| Eigenschaft | LoRaWAN | WiFi | Bluetooth | NB-IoT |
|-------------|---------|------|-----------|--------|
| **Reichweite** | 10+ km | 50 m | 10 m | 10 km |
| **Datenrate** | 50 kbit/s | 1 Gbit/s | 2 Mbit/s | 250 kbit/s |
| **Energieverbrauch** | Sehr niedrig | Hoch | Niedrig | Niedrig |
| **Lizenz** | Frei | Frei | Frei | Mobilfunk |
| **Infrastruktur** | Gateway | Router | - | Mobilfunkmast |

## Einsatzgebiete

> [!example] Typische Anwendungen
> - **Smart City**: Parkplatzsensoren, Straßenbeleuchtung
> - **Landwirtschaft**: Bodenfeuchtigkeit, Tierverfolgung
> - **Logistik**: Asset-Tracking, Kühlkettenüberwachung
> - **Umwelt**: Wetter- und Luftqualitätsmessung
> - **Versorgung**: Wasserzähler, Gaszähler

## Sicherheit

LoRaWAN verwendet mehrschichtige Verschlüsselung:

| Schlüssel | Ebene | Zweck |
|-----------|-------|-------|
| **NwkSKey** | Netzwerk | Integritätsprüfung |
| **AppSKey** | Anwendung | Payload-Verschlüsselung |
| **AppKey** | Gerät | Aktivierung (OTAA) |

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Was ist der Unterschied zwischen LoRa und LoRaWAN?
> - Beschreiben Sie die LoRaWAN-Architektur
> - Welche Geräteklassen gibt es und worin unterscheiden sie sich?
> - Für welche Anwendungen eignet sich LoRaWAN?

## Querverweise

- → [[01-MQTT|MQTT]] – Messaging-Protokoll für IoT
- → [[../../../03-LF03-Netzwerke/01-Grundlagen/01-Netzwerkgrundlagen|Netzwerkgrundlagen]] – OSI-Modell
- → [[../../../09-LF09-Netzwerke-Erweitert/01-Verschluesselung/01-Kryptographie|Verschlüsselung]] – AES

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
