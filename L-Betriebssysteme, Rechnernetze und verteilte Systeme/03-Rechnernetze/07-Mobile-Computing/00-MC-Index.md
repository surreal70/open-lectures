---
author: Andreas Hümmer
title: Mobile Computing - Index
tags:
  - index
  - rn
  - mobile-computing
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# Mobile Computing

Übersicht über den Bereich **Mobile Computing** im Kontext von Rechnernetzen.

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Die Besonderheiten mobiler Kommunikation gegenüber stationären Systemen erklären
> - Herausforderungen wie Verbindungsunterbrechungen und Sicherheit einordnen
> - Standortbestimmung mittels GNSS und alternativer Verfahren verstehen
> - Funktechnologien nach Reichweite klassifizieren (PAN, LAN, MAN, WAN)
> - Multiplexing-Verfahren im Funkbereich (FDMA, TDMA, CDMA) unterscheiden

## Inhalte

| Nr. | Kapitel | Beschreibung |
|-----|---------|--------------|
| 01 | [[01-Einfuehrung\|Einführung]] | Definition, Charakteristiken, Herausforderungen |
| 02 | [[02-Kommunikation\|Kommunikation]] | Anforderungen, Proxies, VPN, QUIC/HTTP/3 |
| 03 | [[03-Standortbestimmung\|Standortbestimmung]] | GNSS, WLAN-Ortung, Funkzellen |
| 04 | [[04-Funknetze\|Funknetze]] | Mobilfunk (2G-5G), WLAN, Bluetooth, NFC |
| 05 | [[05-Kanalaufteilung\|Kanalaufteilung]] | FDMA, TDMA, CDMA, SDMA, OFDMA |

---

## Kapitelübersicht

### 01 – Einführung Mobile Computing

- **Definition** – Was ist Mobile Computing?
- **Charakteristiken** – Mobilität, drahtlose Kommunikation, Ressourcenbeschränkungen
- **Herausforderungen** – Unterbrechungen, Abkopplungen, Sicherheit
- **Abgrenzung** – Ubiquitous Computing, Pervasive Computing

### 02 – Kommunikationsanforderungen

- **Verbindungsunterbrechungen** – Funklöcher, Handover, Netzüberlastung
- **Kompensationsmaßnahmen** – TCP-Retransmission, Proxies
- **Resiliente VPNs** – WireGuard, IKEv2/MOBIKE
- **Moderne Protokolle** – QUIC, HTTP/3, Connection Migration

### 03 – Standortbestimmung

- **GNSS** – GPS, GLONASS, Galileo, BeiDou
- **Funktionsprinzip** – Trilateration, Laufzeitmessung
- **Genauigkeit** – Standard (2-15m), DGPS, RTK (cm-Bereich)
- **Alternative Verfahren** – WLAN-Ortung, Funkzellen-Triangulation

### 04 – Funknetze und Reichweiten

- **WAN** – Mobilfunk: GSM, UMTS, LTE, 5G
- **LAN** – WLAN/WiFi (802.11 a/b/g/n/ac/ax), DECT
- **MAN** – LPWAN, LoRaWAN, NB-IoT
- **PAN** – Bluetooth, NFC, ZigBee

### 05 – Kanalaufteilung im Funkbereich

- **FDMA** – Frequency Division Multiple Access
- **TDMA** – Time Division Multiple Access
- **CDMA** – Code Division Multiple Access
- **SDMA** – Space Division (Zellen, Beamforming)
- **OFDMA** – Orthogonal Frequency Division (LTE, WiFi 6)

---

## Zusammenhänge

```
┌─────────────────────────────────────────────────────────────┐
│                    Mobile Computing                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Rechnernetze          Verteilte Systeme       Sicherheit  │
│  ┌───────────┐         ┌───────────┐          ┌─────────┐  │
│  │Protokolle │◄───────►│ Sync,     │◄────────►│ VPN,    │  │
│  │TCP/IP,    │         │ Replikat. │          │ TLS,    │  │
│  │QUIC       │         │           │          │ WLAN-   │  │
│  └───────────┘         └───────────┘          │ Security│  │
│       ▲                      ▲                └─────────┘  │
│       │                      │                     ▲       │
│       └──────────┬───────────┴─────────────────────┘       │
│                  │                                          │
│           ┌──────┴──────┐                                  │
│           │   Mobile    │                                  │
│           │  Computing  │                                  │
│           └─────────────┘                                  │
└─────────────────────────────────────────────────────────────┘
```

## Verwandte Themen

- [[../04-Bitübertragungsschicht/01-Uebertragungsmedien|Übertragungsmedien]] – Funktechnologien
- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] – Sichere mobile Verbindungen
- [[../04-Basisprotokolle/00-Basisprotokolle-Index|Basisprotokolle]] – DNS, DHCP für Mobile
- [[../../04-Verteilte-Systeme/00-VS-Index|Verteilte Systeme]] – Cloud, Synchronisation

---

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Charakteristiken und Herausforderungen von Mobile Computing
> - GNSS-Funktionsprinzip (Trilateration, 4 Satelliten)
> - Mobilfunkgenerationen (2G-5G) und ihre Merkmale
> - Multiplexing-Verfahren: FDMA, TDMA, CDMA

> [!question] Typische Prüfungsfragen
> - Welche besonderen Herausforderungen gibt es bei Mobile Computing?
> - Wie funktioniert GPS? Warum werden 4 Satelliten benötigt?
> - Ordnen Sie die Technologien nach Reichweite: NFC, WLAN, LTE, Bluetooth
> - Erklären Sie den Unterschied zwischen FDMA und TDMA.
> - Welches Multiplexing nutzt GSM? Welches nutzt LTE?

---

*Dateiende*
