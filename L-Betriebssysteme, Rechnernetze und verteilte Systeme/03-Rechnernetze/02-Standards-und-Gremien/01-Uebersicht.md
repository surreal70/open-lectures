---
author: Andreas Hümmer
title: Standardisierung – Übersicht
tags:
  - vorlesung
  - rn
  - standards
  - ieee
  - ietf
  - iso
  - itu
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Standardisierung – Übersicht

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Erklären, warum Standards in der Netzwerktechnik unverzichtbar sind
> - De-facto- und De-jure-Standards unterscheiden
> - Die wichtigsten Standardisierungsgremien und ihre Zuständigkeiten benennen
> - Den Standardisierungsprozess in Grundzügen beschreiben

## Warum Standards?

Ohne Standards wäre Kommunikation zwischen Geräten verschiedener Hersteller unmöglich. Standards gewährleisten:

- **Interoperabilität**: Geräte verschiedener Hersteller können kommunizieren
- **Investitionssicherheit**: Technologien bleiben langfristig nutzbar
- **Wettbewerb**: Mehrere Anbieter können kompatible Produkte herstellen
- **Innovation**: Aufbau auf etablierten Grundlagen statt Neuentwicklung

> [!beispiel] Ohne Standards: Proprietäre Inseln
> In den 1980er Jahren existierten zahlreiche inkompatible Netzwerktechnologien:
> - IBM Token Ring
> - DECnet
> - AppleTalk
> - Novell IPX/SPX
> 
> Heute dominieren standardisierte Technologien (Ethernet, TCP/IP), die herstellerübergreifende Kommunikation ermöglichen.

## De-facto vs. De-jure Standards

> [!merke] Arten von Standards
> - **De-jure** („nach Recht"): Offiziell durch Gremien verabschiedet
>   - Beispiele: ISO-Normen, IEEE 802.x, ITU-Empfehlungen
> - **De-facto** („nach Tatsache"): Durch Marktdominanz zum Standard geworden
>   - Beispiele: TCP/IP (vor RFC-Standardisierung), Windows, PDF

### Entstehungswege

![[standardisierungswege.png]]
*<span class="fig-id">03-02-01-standardisierungswege</span>: Vergleich der Standardisierungswege – formelle De-jure-Standards (links) und informelle De-facto-Standards (rechts).*

## Standardisierungsgremien – Übersicht

### Die wichtigsten Organisationen

| Organisation | Vollständiger Name | Fokus | Beispiel-Standards |
|--------------|-------------------|-------|-------------------|
| [[07-Anhang/IT-Related-Organisations/IEEE\|IEEE]] | Institute of Electrical and Electronics Engineers | LAN/WLAN-Technologien | 802.3 (Ethernet), 802.11 (WLAN) |
| [[07-Anhang/IT-Related-Organisations/IETF\|IETF]] | Internet Engineering Task Force | Internet-Protokolle | TCP/IP, HTTP, DNS (als RFCs) |
| [[07-Anhang/IT-Related-Organisations/ISO\|ISO]] | International Organization for Standardization | Allgemeine Standards | OSI-Modell, ISO 27001 |
| [[07-Anhang/IT-Related-Organisations/ITU\|ITU]] | International Telecommunication Union | Telekommunikation | H.264, G.711, xDSL |
| [[07-Anhang/IT-Related-Organisations/IEC\|IEC]] | International Electrotechnical Commission | Elektrotechnik | Gemeinsame Standards mit ISO |
| [[07-Anhang/IT-Related-Organisations/IANA\|IANA]] | Internet Assigned Numbers Authority | Nummernverwaltung | IP-Adressen, Port-Nummern |
| [[07-Anhang/IT-Related-Organisations/ICANN\|ICANN]] | Internet Corporation for Assigned Names and Numbers | Domain-Namen | DNS-Root, TLDs |
| [[07-Anhang/IT-Related-Organisations/W3C\|W3C]] | World Wide Web Consortium | Web-Standards | HTML, CSS, XML |

### Zuständigkeitsbereiche

| Schicht | Hauptverantwortlich |
|---------|---------------------|
| **Anwendung** | W3C (Web), IETF (Protokolle), OASIS (Enterprise) |
| **Transport** | IETF (TCP, UDP, QUIC) |
| **Netzwerk** | IETF (IP), IANA (Adressen) |
| **Sicherung** | IEEE 802 (Ethernet, WLAN) |
| **Physikalisch** | IEEE 802, ITU-T (Telekom), IEC (Kabel, Stecker) |
| *Übergreifend* | ISO (Modelle, Sicherheit), ITU (Telekommunikation) |

## IEEE – Institute of Electrical and Electronics Engineers

Die [[07-Anhang/IT-Related-Organisations/IEEE|IEEE]] ist eine der wichtigsten Organisationen für Netzwerkstandards.

**Website:** [ieee.org](http://www.ieee.org/)

**Kennzahlen:**
- Über 400.000 Mitglieder weltweit
- Mehr als 1.300 aktive Standards
- 39 Fachgesellschaften

**Struktur:**
- Standards Association (IEEE-SA) verantwortet Standardisierung
- Arbeitsgruppen (Working Groups) für spezifische Technologien
- Standards werden nach Abstimmung veröffentlicht

> [!info] IEEE 802 – Die Netzwerk-Arbeitsgruppe
> Die **IEEE 802** ist die Arbeitsgruppe, die sich speziell mit der Standardisierung von lokalen und metropolitanen Netzwerken (LAN/MAN) befasst.
> 
> → Detaillierte Behandlung in [[02-IEEE-Standards]]

### IEEE-Standardisierungsprozess

| Schritt | Phase | Beschreibung |
|---------|-------|--------------|
| 1 | **Project Authorization Request (PAR)** | Vorschlag einer neuen Arbeitsgruppe |
| 2 | **Task Group Formation** | Bildung der Arbeitsgruppe |
| 3 | **Draft Development** | Erstellung des Entwurfs |
| 4 | **Working Group Ballot** | Abstimmung in der Arbeitsgruppe (75% Zustimmung) |
| 5 | **Sponsor Ballot** | Breitere Abstimmung (75% Zustimmung) |
| 6 | **RevCom Approval** | Review Committee Genehmigung |
| 7 | **IEEE-SA Standards Board Approval** | Finale Genehmigung |
| 8 | **Publication** | Veröffentlichung des Standards |

*Typische Dauer: 2-5 Jahre*

## IETF – Internet Engineering Task Force

Die [[07-Anhang/IT-Related-Organisations/IETF|IETF]] entwickelt und pflegt Internet-Standards durch einen offenen Prozess.

**Website:** [ietf.org](https://www.ietf.org/)

**Philosophie:** *„Rough Consensus and Running Code"*

> [!info] RFCs – Request for Comments
> Standards der IETF werden als **RFCs** veröffentlicht. Trotz des Namens („Bitte um Kommentare") handelt es sich um verbindliche Spezifikationen.
> 
> → Detaillierte Behandlung in [[03-RFCs]]

### IETF-Prozess

| Schritt | Phase | Beschreibung |
|---------|-------|--------------|
| 1 | **Internet-Draft (I-D)** | Erste Version, 6 Monate gültig, erneuerbar |
| 2 | **Working Group Adoption** | Übernahme durch eine Arbeitsgruppe |
| 3 | **Working Group Last Call (WGLC)** | Finale Überprüfung in der WG |
| 4 | **IETF Last Call** | Öffentliche Kommentierung (2 Wochen) |
| 5 | **IESG Review** | Prüfung durch Internet Engineering Steering Group |
| 6 | **RFC Publication** | Veröffentlichung durch RFC Editor |

*Typische Dauer: 1-3 Jahre*

## ISO – International Organization for Standardization

Die [[07-Anhang/IT-Related-Organisations/ISO|ISO]] entwickelt internationale Standards für praktisch alle Branchen.

**Website:** [iso.org](http://www.iso.org/)

**Netzwerk-relevante Standards:**

| Standard | Beschreibung |
|----------|--------------|
| ISO/IEC 7498 | OSI-Referenzmodell |
| ISO/IEC 8802 | LAN-Standards (identisch mit IEEE 802) |
| ISO 27001 | Informationssicherheits-Management |
| ISO 27002 | Sicherheitsmaßnahmen (Code of Practice) |

> [!info] ISO und IEEE
> Durch ein Liaison-Abkommen werden IEEE 802 Standards auch als ISO/IEC 8802 veröffentlicht, wodurch sie internationalen Normenstatus erhalten.

## ITU – International Telecommunication Union

Die [[07-Anhang/IT-Related-Organisations/ITU|ITU]] ist eine Sonderorganisation der Vereinten Nationen für Telekommunikation.

**Sektoren:**
- **ITU-T**: Telekommunikationsstandardisierung
- **ITU-R**: Funkfrequenz-Regulierung
- **ITU-D**: Entwicklung

**Relevante Standards:**

| Standard | Beschreibung |
|----------|--------------|
| V.24 / V.28 | Serielle Schnittstellen (≈ RS-232) |
| V.90 / V.92 | Modem-Standards (56 kbit/s) |
| G.711 | Audio-Codec (PCM, 64 kbit/s) |
| G.729 | Audio-Codec (8 kbit/s, VoIP) |
| H.264 / H.265 | Video-Codecs |
| G.992.x | ADSL-Standards |
| G.984.x | GPON (Glasfaser-Zugangsnetz) |

## Weitere relevante Organisationen

### ECMA International

Die [[07-Anhang/IT-Related-Organisations/ECMA|ECMA]] standardisiert Informations- und Kommunikationssysteme.

**Bekannte Standards:**
- ECMA-262: ECMAScript (JavaScript)
- ECMA-404: JSON
- ECMA-376: Office Open XML

### OASIS

[[07-Anhang/IT-Related-Organisations/OASIS|OASIS]] fokussiert auf Enterprise-Standards.

**Bekannte Standards:**
- SAML (Security Assertion Markup Language)
- MQTT (Message Queuing Telemetry Transport)
- OpenDocument Format (ODF)

### Regionale Organisationen

| Organisation | Region | Fokus |
|--------------|--------|-------|
| [[07-Anhang/IT-Related-Organisations/ANSI\|ANSI]] | USA | Nationale Standards |
| [[07-Anhang/IT-Related-Organisations/DIN\|DIN]] | Deutschland | Nationale Standards |
| CEN/CENELEC | Europa | Europäische Normen |
| [[07-Anhang/IT-Related-Organisations/BSI\|BSI]] (UK) | UK | British Standards |

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - Standards ermöglichen Interoperabilität und fairen Wettbewerb
> - **De-jure-Standards** entstehen durch formelle Prozesse (IEEE, ISO, IETF)
> - **De-facto-Standards** setzen sich durch Marktdominanz durch
> - **IEEE** ist primär für LAN/WLAN-Standards zuständig (802.x)
> - **IETF** entwickelt Internet-Protokolle als RFCs
> - **ISO** definiert übergeordnete internationale Normen
> - **ITU** standardisiert Telekommunikation
> - Standardisierung dauert typischerweise 2-5 Jahre

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Kennen Sie die vier Hauptgremien (IEEE, IETF, ISO, ITU) und ihre Zuständigkeiten
> - Verstehen Sie den Unterschied zwischen De-facto und De-jure
> - Wissen Sie, dass IEEE 802.x für lokale Netze zuständig ist
> - Kennen Sie den groben Ablauf eines Standardisierungsprozesses

## Verwandte Themen

- [[02-IEEE-Standards]] – IEEE 802.x Standards im Detail
- [[03-RFCs]] – RFCs und der IETF-Prozess
- [[01-Grundlagen/01-Historie|Historie]] – Historische Entwicklung der Netzwerke
- [[03-Referenzmodelle/00-Referenzmodelle-Index|Referenzmodelle]] – OSI und TCP/IP Modell

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- IEEE Standards Association: [standards.ieee.org](https://standards.ieee.org/)
- IETF: [ietf.org](https://www.ietf.org/)
- ISO: [iso.org](https://www.iso.org/)
- ITU: [itu.int](https://www.itu.int/)
