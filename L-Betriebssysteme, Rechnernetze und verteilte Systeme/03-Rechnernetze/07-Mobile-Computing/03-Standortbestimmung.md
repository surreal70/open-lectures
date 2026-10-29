---
author: Andreas Hümmer
title: Standortbestimmung und Lokalisierung
tags:
  - content
  - rn
  - mobile-computing
  - gnss
  - gps
  - location
  - positioning
created: '2026-10-24'
modified: '2026-10-29'
bereich: RN
---

# Standortbestimmung und Lokalisierung

## Lernziele

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Verschiedene Lokalisierungstechnologien erklären
> - GNSS-Systeme (GPS, Galileo, GLONASS) unterscheiden
> - Alternative Ortungsverfahren (WLAN, Funkzellen) benennen
> - Genauigkeiten und Anwendungsfälle einordnen

## Übersicht Lokalisierungsmethoden

| Methode | Genauigkeit | Einsatzbereich |
|---------|-------------|----------------|
| **GNSS (Satellit)** | 2-15 m | Outdoor |
| **WLAN (WiFi)** | 10-50 m | Indoor/Outdoor |
| **Mobilfunk (Zellen)** | 50-300 m | Outdoor |

## GNSS - Global Navigation Satellite System

> [!quote] Definition
> **GNSS** (Global Navigation Satellite System) ist der Oberbegriff für satellitengestützte Navigationssysteme, die eine globale Positionsbestimmung ermöglichen.

### Satellitennavigationssysteme im Vergleich

| System | Betreiber | Satelliten | Status | Abdeckung |
|--------|-----------|------------|--------|-----------|
| **GPS** | USA | 31 operativ | Voll operativ seit 1995 | Global |
| **GLONASS** | Russland | 24 operativ | Voll operativ | Global |
| **Galileo** | EU | 28 operativ | Voll operativ seit 2016 | Global |
| **BeiDou** | China | 35+ operativ | Voll operativ seit 2020 | Global |
| **QZSS** | Japan | 4 operativ | Regional | Asien-Pazifik |
| **NavIC** | Indien | 7 operativ | Regional | Indien + 1500km |

### Funktionsprinzip GNSS

![[gnss-triangulation.png]]
*<span class="fig-id">03-07-03-gnss-triangulation</span>: GNSS-Positionsbestimmung durch Trilateration – aus den Entfernungen d1, d2, d3 zu mindestens drei Satelliten wird die Position berechnet.*

**Triangulation durch Laufzeitmessung:**

1. Satellit sendet Zeitstempel in seinem Signal
2. Empfänger berechnet Signallaufzeit
3. Aus Laufzeit ergibt sich Entfernung: $d = c \cdot t$
4. Mit 3 Satelliten: Position in 3D
5. Mit 4 Satelliten: zusätzlich Zeitkorrektur (Empfängeruhr)

> [!info] Warum 4 Satelliten?
> Der Empfänger hat keine atomgenaue Uhr. Der 4. Satellit ermöglicht die Korrektur des Zeitfehlers im Empfänger.

### Genauigkeit

| Modus | Genauigkeit | Beschreibung |
|-------|-------------|--------------|
| **Standard (zivil)** | 2-15 m | Normale GPS-Nutzung |
| **Multi-GNSS** | 1-5 m | Kombination mehrerer Systeme |
| **SBAS/EGNOS** | 1-3 m | Korrektursignale via Satellit |
| **DGPS** | 0,5-2 m | Differentielle Korrektur via Funk |
| **RTK** | 1-4 cm | Echtzeit-Kinematik mit Referenzstation |
| **PPP** | 5-20 cm | Precise Point Positioning |

### Fehlerquellen

| Fehlerquelle | Auswirkung | Korrektur |
|--------------|------------|-----------|
| **Ionosphäre** | Signalverzögerung | Dual-Frequenz, Modelle |
| **Troposphäre** | Signalverzögerung | Wettermodelle |
| **Mehrwegausbreitung** | Reflexionen verfälschen Signal | Antennendesign |
| **Satellitengeometrie** | DOP-Wert (schlechte Verteilung) | Mehr Satelliten nutzen |
| **Uhrenabweichung** | Zeitfehler | 4. Satellit |

> [!tip] DOP - Dilution of Precision
> DOP beschreibt die geometrische Qualität der Satellitenverteilung. Niedrige DOP-Werte (< 2) bedeuten gute Geometrie und höhere Genauigkeit.

## WLAN-Ortung (WiFi Positioning)

### Funktionsprinzip

![[wlan-positioning.png]]
*<span class="fig-id">03-07-03-wlan-positioning</span>: WLAN-Ortung durch Trilateration – aus den Signalstärken mehrerer Access Points wird die Position bestimmt.*

**Methoden:**

| Methode | Beschreibung | Genauigkeit |
|---------|--------------|-------------|
| **Signalstärke (RSSI)** | Entfernung aus Dämpfung | 10-30 m |
| **Fingerprinting** | Vergleich mit Referenzdatenbank | 2-10 m |
| **Time of Arrival** | Laufzeitmessung | 1-5 m |
| **Angle of Arrival** | Richtungsbestimmung | 1-3 m |

### Datenbanken für WLAN-Ortung

Große Technologieunternehmen betreiben Datenbanken mit WLAN-Standorten:

- **Google Location Services**: Gesammelt durch Android-Geräte
- **Apple Location Services**: Gesammelt durch iOS-Geräte
- **Mozilla Location Service**: Open-Source-Alternative
- **Skyhook**: Kommerzieller Anbieter

> [!warning] Datenschutz
> WLAN-Ortung funktioniert durch das Sammeln von BSSID (MAC-Adresse) und Standort. Dies wirft Datenschutzfragen auf, insbesondere bei der Erfassung privater Access Points.

## Funkzellen-Ortung (Cell-ID)

### Funktionsprinzip

Das Mobilgerät ist immer mit einer oder mehreren Funkzellen verbunden:

![[cell-triangulation.png]]
*<span class="fig-id">03-07-03-cell-triangulation</span>: Funkzellen-Triangulation – durch Messung zu mehreren Basisstationen wird die Position eingegrenzt.*

### Genauigkeit nach Technologie

| Methode | Genauigkeit | Beschreibung |
|---------|-------------|--------------|
| **Cell-ID** | 100 m - 3 km | Nur aktive Zelle bekannt |
| **Cell-ID + TA** | 50-200 m | Timing Advance hinzugefügt |
| **E-CID** | 50-150 m | Enhanced Cell-ID (LTE) |
| **OTDOA** | 20-50 m | Observed Time Difference of Arrival |
| **U-TDOA** | 50-100 m | Uplink TDOA |

### Vorteile der Funkzellen-Ortung

- ✅ Funktioniert indoor und in Gebäuden
- ✅ Geringer Energieverbrauch
- ✅ Schnelle erste Positionsschätzung (A-GPS)
- ✅ Keine zusätzliche Hardware nötig

### Nachteile

- ❌ Geringe Genauigkeit in ländlichen Gebieten (große Zellen)
- ❌ Abhängig von Netzbetreiber-Infrastruktur
- ❌ Keine Höheninformation

## Hybride Ortung

Moderne Smartphones kombinieren mehrere Verfahren:

![[sensor-fusion.png]]
*<span class="fig-id">03-07-03-sensor-fusion</span>: Hybride Ortung durch Sensor Fusion – verschiedene Quellen werden mittels Kalman-Filter zu einer optimierten Position kombiniert.*

**Komponenten:**
- **GNSS**: Primäre Quelle outdoor
- **WLAN**: Indoor und urbane Gebiete
- **Cell-ID**: Schnelle Initialisierung, Fallback
- **Bluetooth Beacons**: Indoor-Navigation
- **IMU** (Beschleunigungssensor, Gyroskop): Dead Reckoning zwischen Fixes

## Indoor-Positionierung

Für Gebäude existieren spezielle Systeme:

| Technologie | Genauigkeit | Infrastruktur |
|-------------|-------------|---------------|
| **WLAN Fingerprinting** | 2-10 m | Vorhandene APs |
| **Bluetooth Beacons** | 1-3 m | iBeacon, Eddystone |
| **UWB** | 10-30 cm | Ultra-Wideband-Anker |
| **Ultraschall** | 1-5 cm | Spezialsender |
| **Magnetfeld-Mapping** | 1-2 m | Keine (Erdmagnetfeld) |
| **Visual Positioning** | < 1 m | Kameras + KI |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - GNSS-Systeme: GPS, GLONASS, Galileo, BeiDou
> - Alternative Ortung: WLAN, Funkzellen
> - Hybride Ortung und Sensor Fusion

> [!question] Typische Prüfungsfragen
> - Wie funktioniert die Positionsbestimmung per GPS?
> - Warum werden mindestens 4 Satelliten benötigt?
> - Welche Alternativen zu GNSS gibt es für die Standortbestimmung?
> - Was ist der Unterschied zwischen Cell-ID und OTDOA?
> - Wie funktioniert WLAN-Fingerprinting?

## Zusammenhänge

- [[01-Einfuehrung]] – Grundlagen Mobile Computing
- [[02-Kommunikation]] – Kommunikationsanforderungen
- [[04-Funknetze]] – Mobilfunktechnologien (LTE, 5G)
- [[05-Kanalaufteilung]] – Frequenznutzung

## Quellen

- GPS.gov – Official U.S. Government Information
- European GNSS Agency – Galileo
- Hofmann-Wellenhof, B.: GNSS – Global Navigation Satellite Systems
- Kaplan, E.: Understanding GPS/GNSS

---

*Dateiende*
