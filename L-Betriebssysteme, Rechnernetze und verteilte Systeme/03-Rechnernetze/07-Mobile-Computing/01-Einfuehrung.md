---
author: Andreas Hümmer
title: Einführung Mobile Computing
tags:
  - content
  - rn
  - mobile-computing
  - wireless
  - mobility
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Einführung Mobile Computing

## Definition

> [!quote] Definition
> **Mobile Computing** bezeichnet die Nutzung von tragbaren Computern und mobilen Endgeräten, die über drahtlose Netzwerke kommunizieren und dabei ihren Standort wechseln können. Es umfasst Hardware, Software, Netzwerktechnologien und Anwendungen für mobile Szenarien.

## Lernziele

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Die Charakteristiken von Mobile Computing benennen
> - Unterschiede zu stationären Systemen erklären
> - Herausforderungen mobiler Kommunikation verstehen
> - Mobile Computing im Kontext verteilter Systeme einordnen

## Charakteristiken

### Mobilität und Standortwechsel

Mobile Geräte wechseln häufig ihren Standort – teilweise sehr schnell (z.B. im Zug mit 300 km/h). Dies führt zu besonderen Anforderungen:

| Aspekt | Auswirkung |
|--------|------------|
| **Häufige Neukonfiguration** | Netzwerk muss sich dynamisch anpassen |
| **Handover** | Wechsel zwischen Funkzellen während der Verbindung |
| **Roaming** | Wechsel zwischen Netzbetreibern/Netzwerken |
| **Variable Bandbreite** | Übertragungsrate schwankt je nach Standort |

### Drahtlose Kommunikation

> [!important] Funkbasierte Übertragung
> Mobile Datenübertragung setzt ein **Funknetz** voraus und ist standortunabhängig. Das Mobilgerät kommuniziert mit anderen mobilen oder stationären Geräten über elektromagnetische Wellen.

**Konsequenzen:**
- Geringere Verfügbarkeit im Vergleich zu kabelgebundenen Netzen
- Leichteres Abhören (Wiretapping) als bei Kabeln
- Störanfälligkeit durch Interferenzen
- Shared Medium – alle Teilnehmer teilen sich das Funkspektrum

### Ressourcenbeschränkungen

| Ressource | Einschränkung | Konsequenz |
|-----------|---------------|------------|
| **Akku** | Begrenzte Kapazität | Energieeffiziente Protokolle nötig |
| **CPU** | Geringere Leistung | Offloading in die Cloud |
| **Speicher** | Limitiert | Cloud-Speicher, Streaming |
| **Display** | Kleine Bildschirme | Angepasste UI/UX |

## Abgrenzung zu verwandten Konzepten

```
┌─────────────────────────────────────────────────────────────┐
│                    Verteilte Systeme                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Mobile Computing                        │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │         Ubiquitous Computing                │    │   │
│  │  │  (Allgegenwärtige Vernetzung, IoT)         │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

| Begriff | Fokus | Beispiel |
|---------|-------|----------|
| **Mobile Computing** | Mobilität des Nutzers | Smartphone, Laptop |
| **Ubiquitous Computing** | Allgegenwärtige Vernetzung | Smart Home, Wearables |
| **Pervasive Computing** | Unsichtbare Integration | Ambient Intelligence |
| **Nomadic Computing** | Arbeiten an wechselnden Orten | Laptop mit Docking Station |

## Herausforderungen

### Verbindungsunterbrechungen

> [!warning] Disconnected Operation
> Es kann jederzeit zu **Verbindungsunterbrechungen** kommen:
> - Funklöcher, Tunnel, Gebäude
> - Überlastete Funkzellen
> - Handover-Probleme
> - Energiesparmodus des Geräts

### Abkopplungen (Disconnection)

Geplante oder ungeplante Trennung vom Netzwerk erfordert:
- **Caching**: Lokale Zwischenspeicherung von Daten
- **Synchronisation**: Abgleich nach Wiederverbindung
- **Konfliktauflösung**: Bei gleichzeitigen Änderungen

### Sicherheit

| Bedrohung | Beschreibung | Gegenmaßnahme |
|-----------|--------------|---------------|
| **Abhören** | Funkverkehr kann abgefangen werden | Verschlüsselung (WPA3, TLS) |
| **Man-in-the-Middle** | Angreifer schaltet sich dazwischen | Zertifikate, VPN |
| **Rogue Access Points** | Gefälschte Zugangspunkte | 802.1X, Zertifikate |
| **Geräteverlust** | Physischer Diebstahl | Verschlüsselung, Remote Wipe |

## Mobile Computing im OSI-Modell

Mobile Technologien betreffen mehrere Schichten:

| Schicht | Mobile Aspekte |
|---------|----------------|
| **7 - Anwendung** | Mobile Apps, Progressive Web Apps |
| **6 - Darstellung** | Adaptive Content, Kompression |
| **5 - Sitzung** | Session-Persistenz bei Unterbrechungen |
| **4 - Transport** | TCP-Optimierungen, QUIC |
| **3 - Netzwerk** | Mobile IP, Roaming |
| **2 - Sicherung** | WLAN (802.11), LTE MAC |
| **1 - Bitübertragung** | Funktechnologien, Antennen |

## Anwendungsgebiete

### Consumer

- Smartphones und Tablets
- Wearables (Smartwatches, Fitness-Tracker)
- Mobile Gaming
- Navigation und Standortdienste

### Enterprise

- Mobile Workforce (Außendienst)
- Bring Your Own Device (BYOD)
- Mobile Device Management (MDM)
- Enterprise Mobility Management (EMM)

### Industrie

- Industrie 4.0 / IIoT
- Logistik und Tracking
- Telemedizin
- Smart Agriculture

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Definition und Charakteristiken von Mobile Computing
> - Unterschiede zu stationären Systemen
> - Herausforderungen: Unterbrechungen, Sicherheit, Ressourcen
> - Einordnung im Kontext verteilter Systeme

> [!question] Typische Prüfungsfragen
> - Welche besonderen Herausforderungen gibt es bei Mobile Computing?
> - Warum ist die Sicherheit bei drahtloser Kommunikation kritischer?
> - Was versteht man unter Disconnected Operation?
> - Wie unterscheidet sich Mobile Computing von Ubiquitous Computing?

## Zusammenhänge

- [[02-Kommunikation]] – Anforderungen an mobile Kommunikation
- [[03-Standortbestimmung]] – Lokalisierungstechnologien
- [[04-Funknetze]] – Reichweiten und Technologien
- [[05-Kanalaufteilung]] – Multiplexing im Funkbereich

## Quellen

- Tanenbaum, A. S.: Verteilte Systeme
- Schiller, J.: Mobile Communications
- Satyanarayanan, M.: Pervasive Computing – Vision and Challenges

---

*Dateiende*
