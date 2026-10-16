---
author: Andreas Hümmer
title: RFCs und IETF
tags:
  - vorlesung
  - rn
  - standards
  - ietf
  - rfc
  - internet
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# RFCs und IETF

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den RFC-Prozess und seine Besonderheiten erklären
> - Die verschiedenen RFC-Kategorien und Status unterscheiden
> - Wichtige RFCs und ihre Bedeutung für das Internet benennen
> - Die Struktur und Arbeitsweise der IETF beschreiben
> - Die Bedeutung von RFC 2119 für das Lesen von Standards erklären

## Die IETF

Die [[07-Anhang/IT-Related-Organisations/IETF|Internet Engineering Task Force]] ist die zentrale Organisation für die Entwicklung von Internet-Standards.

### Grundphilosophie

> [!zitat] David Clark, 1992
> „We reject kings, presidents, and voting. We believe in rough consensus and running code."

Diese Philosophie prägt die IETF bis heute:
- **Rough Consensus**: Keine formellen Abstimmungen, sondern Konsensbildung
- **Running Code**: Standards müssen in der Praxis funktionieren
- **Offenheit**: Jeder kann teilnehmen und Vorschläge einreichen

### IETF-Struktur

![[ietf-organisation.png]]
*<span class="fig-id">03-02-03-ietf-organisation</span>: Struktur der IETF mit IAB, IESG, IRTF, IANA und den Working Groups.*

### Wichtige Gremien

| Gremium | Funktion |
|---------|----------|
| **IAB** | Internet Architecture Board – strategische Ausrichtung |
| **IESG** | Internet Engineering Steering Group – Leitung der IETF |
| **IANA** | [[07-Anhang/IT-Related-Organisations/IANA\|Internet Assigned Numbers Authority]] – Nummernverwaltung |
| **IRTF** | Internet Research Task Force – Forschung |
| **RFC Editor** | Veröffentlichung und Archivierung von RFCs |

## Request for Comments (RFCs)

### Was ist ein RFC?

> [!info] RFC – Mehr als „Bitte um Kommentare"
> Trotz des bescheidenen Namens sind RFCs die verbindlichen Spezifikationen des Internets. Der Name stammt aus der Frühzeit des ARPANET (1969), als Steve Crocker das erste RFC schrieb und einen unverbindlichen Ton wählte, um andere zur Mitarbeit zu ermutigen.

- **RFC Editor**: [rfc-editor.org](https://www.rfc-editor.org/)
- **Datatracker**: [datatracker.ietf.org](https://datatracker.ietf.org/)
- **Nummerierung**: Fortlaufend seit RFC 1 (1969), aktuell über 9500

### RFC-Streams

RFCs können aus verschiedenen Quellen stammen:

| Stream | Beschreibung |
|--------|--------------|
| **IETF** | Standards Track und Best Current Practice |
| **IRTF** | Forschungsergebnisse der Research Task Force |
| **IAB** | Architektur-Dokumente und Stellungnahmen |
| **Independent** | Unabhängige Einreichungen |

### RFC-Kategorien

![[rfc-standards-track.png]]
*<span class="fig-id">03-02-03-rfc-standards-track</span>: Der RFC Standards Track – von Proposed Standard über Draft Standard zum Internet Standard.*

**Andere Kategorien:**

| Kategorie | Beschreibung |
|-----------|--------------|
| **Best Current Practice (BCP)** | Empfehlungen und Best Practices |
| **Informational** | Informationen, keine verbindlichen Standards |
| **Experimental** | Experimente, nicht für Produktion gedacht |
| **Historic** | Veraltet, nur noch als Referenz |

**Status eines RFCs:**

| Status | Bedeutung |
|--------|-----------|
| **Active** | Aktuell gültig |
| **Obsoleted by** | Ersetzt durch neueren RFC |
| **Updated by** | Ergänzt/korrigiert durch anderen RFC |

### Der RFC-Prozess

![[rfc-entwicklungsprozess.png]]
*<span class="fig-id">03-02-03-rfc-entwicklungsprozess</span>: Der RFC-Entwicklungsprozess von der ersten Einreichung bis zur Veröffentlichung.*

## RFC 2119 – Die Schlüsselwörter

RFC 2119 definiert die Bedeutung von Schlüsselwörtern in technischen Standards. Diese Wörter werden in RFCs **GROSSGESCHRIEBEN**, um ihre spezielle Bedeutung anzuzeigen.

> [!wichtig] RFC 2119 Schlüsselwörter
> 
> | Schlüsselwort | Bedeutung |
> |---------------|-----------|
> | **MUST** / **REQUIRED** / **SHALL** | Absolute Anforderung |
> | **MUST NOT** / **SHALL NOT** | Absolutes Verbot |
> | **SHOULD** / **RECOMMENDED** | Dringend empfohlen, aber begründete Ausnahmen möglich |
> | **SHOULD NOT** / **NOT RECOMMENDED** | Dringend abgeraten, aber begründete Ausnahmen möglich |
> | **MAY** / **OPTIONAL** | Wirklich optional, volle Wahlfreiheit |

> [!beispiel] Anwendung in der Praxis
> Aus RFC 5321 (SMTP):
> 
> *„A client MUST NOT send commands before receiving the welcome message."*
> 
> → Ein SMTP-Client, der Befehle vor der Begrüßung sendet, ist **nicht konform**.

## Wichtige RFCs nach Themengebiet

### Netzwerkschicht (IP)

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 791 IPv4\|RFC 791]] | 1981 | Internet Protocol (IPv4) | [[07-Anhang/RFCs/RFC 791 IPv4\|→]] |
| [[07-Anhang/RFCs/RFC 950 Subnetting\|RFC 950]] | 1985 | Internet Subnetting | [[07-Anhang/RFCs/RFC 950 Subnetting\|→]] |
| [[07-Anhang/RFCs/RFC 1918 Private Networks\|RFC 1918]] | 1996 | Private Address Space | [[07-Anhang/RFCs/RFC 1918 Private Networks\|→]] |
| [[07-Anhang/RFCs/RFC 8200 IPv6\|RFC 8200]] | 2017 | Internet Protocol Version 6 | [[07-Anhang/RFCs/RFC 8200 IPv6\|→]] |
| [[07-Anhang/RFCs/RFC 4291 IPv6 Addressing\|RFC 4291]] | 2006 | IPv6 Addressing Architecture | [[07-Anhang/RFCs/RFC 4291 IPv6 Addressing\|→]] |

### Adressauflösung

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 826 ARP\|RFC 826]] | 1982 | Address Resolution Protocol (ARP) | [[07-Anhang/RFCs/RFC 826 ARP\|→]] |
| [[07-Anhang/RFCs/RFC 4862 IPv6 SLAAC\|RFC 4862]] | 2007 | IPv6 SLAAC | [[07-Anhang/RFCs/RFC 4862 IPv6 SLAAC\|→]] |

### Transportschicht

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| RFC 793 | 1981 | Transmission Control Protocol (TCP) | – |
| RFC 768 | 1980 | User Datagram Protocol (UDP) | – |
| RFC 9000 | 2021 | QUIC: A UDP-Based Multiplexed Transport | – |

### DNS

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 1034 DNS Concepts\|RFC 1034]] | 1987 | DNS Concepts and Facilities | [[07-Anhang/RFCs/RFC 1034 DNS Concepts\|→]] |
| [[07-Anhang/RFCs/RFC 1035 DNS\|RFC 1035]] | 1987 | DNS Implementation | [[07-Anhang/RFCs/RFC 1035 DNS\|→]] |
| [[07-Anhang/RFCs/RFC 4033-4035 DNSSEC\|RFC 4033-4035]] | 2005 | DNSSEC | [[07-Anhang/RFCs/RFC 4033-4035 DNSSEC\|→]] |
| [[07-Anhang/RFCs/RFC 7858 DoT\|RFC 7858]] | 2016 | DNS over TLS (DoT) | [[07-Anhang/RFCs/RFC 7858 DoT\|→]] |
| [[07-Anhang/RFCs/RFC 8484 DoH\|RFC 8484]] | 2018 | DNS over HTTPS (DoH) | [[07-Anhang/RFCs/RFC 8484 DoH\|→]] |

### DHCP

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 2131 DHCP\|RFC 2131]] | 1997 | DHCP | [[07-Anhang/RFCs/RFC 2131 DHCP\|→]] |
| [[07-Anhang/RFCs/RFC 2132 DHCP Options\|RFC 2132]] | 1997 | DHCP Options | [[07-Anhang/RFCs/RFC 2132 DHCP Options\|→]] |
| [[07-Anhang/RFCs/RFC 3927 Link-Local\|RFC 3927]] | 2005 | Link-Local Addressing | [[07-Anhang/RFCs/RFC 3927 Link-Local\|→]] |

### HTTP

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 9110 HTTP Semantics\|RFC 9110]] | 2022 | HTTP Semantics | [[07-Anhang/RFCs/RFC 9110 HTTP Semantics\|→]] |
| [[07-Anhang/RFCs/RFC 9111 HTTP Caching\|RFC 9111]] | 2022 | HTTP Caching | [[07-Anhang/RFCs/RFC 9111 HTTP Caching\|→]] |
| [[07-Anhang/RFCs/RFC 9112 HTTP 1.1\|RFC 9112]] | 2022 | HTTP/1.1 | [[07-Anhang/RFCs/RFC 9112 HTTP 1.1\|→]] |
| [[07-Anhang/RFCs/RFC 9113 HTTP 2\|RFC 9113]] | 2022 | HTTP/2 | [[07-Anhang/RFCs/RFC 9113 HTTP 2\|→]] |
| [[07-Anhang/RFCs/RFC 9114 HTTP 3\|RFC 9114]] | 2022 | HTTP/3 | [[07-Anhang/RFCs/RFC 9114 HTTP 3\|→]] |

### E-Mail

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 5321 SMTP\|RFC 5321]] | 2008 | SMTP | [[07-Anhang/RFCs/RFC 5321 SMTP\|→]] |
| [[07-Anhang/RFCs/RFC 7208 SPF\|RFC 7208]] | 2014 | SPF | [[07-Anhang/RFCs/RFC 7208 SPF\|→]] |
| [[07-Anhang/RFCs/RFC 6376 DKIM\|RFC 6376]] | 2011 | DKIM | [[07-Anhang/RFCs/RFC 6376 DKIM\|→]] |
| [[07-Anhang/RFCs/RFC 7489 DMARC\|RFC 7489]] | 2015 | DMARC | [[07-Anhang/RFCs/RFC 7489 DMARC\|→]] |

### TLS/Sicherheit

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 8446 TLS 1.3\|RFC 8446]] | 2018 | TLS 1.3 | [[07-Anhang/RFCs/RFC 8446 TLS 1.3\|→]] |
| [[07-Anhang/RFCs/RFC 8555 ACME\|RFC 8555]] | 2019 | ACME (Let's Encrypt) | [[07-Anhang/RFCs/RFC 8555 ACME\|→]] |

### Authentifizierung

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 6749 OAuth 2.0\|RFC 6749]] | 2012 | OAuth 2.0 | [[07-Anhang/RFCs/RFC 6749 OAuth 2.0\|→]] |
| [[07-Anhang/RFCs/RFC 7519 JWT\|RFC 7519]] | 2015 | JSON Web Token (JWT) | [[07-Anhang/RFCs/RFC 7519 JWT\|→]] |
| [[07-Anhang/RFCs/RFC 7636 PKCE\|RFC 7636]] | 2015 | PKCE | [[07-Anhang/RFCs/RFC 7636 PKCE\|→]] |

### Zeit

| RFC | Jahr | Titel | Detailseite |
|-----|------|-------|-------------|
| [[07-Anhang/RFCs/RFC 5905 NTP\|RFC 5905]] | 2010 | NTP Version 4 | [[07-Anhang/RFCs/RFC 5905 NTP\|→]] |

## Historische und besondere RFCs

### Die Anfänge

| RFC | Jahr | Bedeutung |
|-----|------|-----------|
| RFC 1 | 1969 | Erster RFC überhaupt (Host Software) |
| RFC 791/793 | 1981 | IPv4 und TCP – das Fundament des Internets |
| RFC 822 | 1982 | E-Mail-Format (ersetzt durch RFC 5322) |

### Humor und Tradition

> [!info] April Fools' Day RFCs
> Seit 1978 veröffentlicht die IETF am 1. April humorvolle RFCs:
> 
> - **RFC 1149** (1990): IP over Avian Carriers (Brieftauben)
> - **RFC 2324** (1998): HTCPCP – Hyper Text Coffee Pot Control Protocol
> - **RFC 7168** (2014): HTCPCP-TEA – The Hyper Text Coffee Pot Control Protocol for Tea
> - **RFC 8771** (2020): Internationalized Deliberately Unreadable Network NOtation (I-DUNNO)

### Meta-RFCs

| RFC | Bedeutung |
|-----|-----------|
| RFC 2026 | Der Internet Standards Process |
| RFC 2119 | Schlüsselwörter in RFCs |
| RFC 7322 | RFC Style Guide |
| RFC 8174 | Klarstellung zu RFC 2119 |

## RFCs lesen und verstehen

### Aufbau eines RFCs

| Nr. | Abschnitt | Beschreibung |
|-----|-----------|--------------|
| 1 | **Header** | RFC-Nummer, Titel, Autoren, Status, Updates/Obsoletes |
| 2 | **Abstract** | Kurze Zusammenfassung |
| 3 | **Table of Contents** | Inhaltsverzeichnis |
| 4 | **Introduction** | Motivation und Überblick |
| 5 | **Terminology** | Verweis auf RFC 2119 |
| 6 | **Technical Specification** | Der eigentliche Standard |
| 7 | **Security Considerations** | PFLICHT seit RFC 3552 |
| 8 | **IANA Considerations** | Registrierte Nummern, Ports, etc. |
| 9 | **References** | Normative (MÜSSEN implementiert) / Informative |
| 10 | **Authors' Addresses** | Kontaktdaten der Autoren |

### Tipps zum Lesen

> [!tip] RFCs effektiv lesen
> 1. **Abstract und Introduction** zuerst – verstehen, worum es geht
> 2. **Terminology** beachten – RFC 2119 Schlüsselwörter ernst nehmen
> 3. **Security Considerations** nicht überspringen – oft kritisch
> 4. **Normative References** sind Pflichtlektüre für Implementierer
> 5. **Errata prüfen** – viele RFCs haben bekannte Fehler

## IANA und Nummernverwaltung

Die [[07-Anhang/IT-Related-Organisations/IANA|IANA]] verwaltet zentrale Internet-Ressourcen:

| Ressource | Beschreibung |
|-----------|--------------|
| **IP-Adressen** | Zuweisung an RIRs (RIPE, ARIN, etc.) |
| **Port-Nummern** | 0-65535, Well-Known Ports 0-1023 |
| **Protokoll-Nummern** | IP Protocol Field (TCP=6, UDP=17, etc.) |
| **DNS Root** | Root-Server und TLD-Verwaltung |
| **Zeichensätze** | Character Sets, Media Types |

> [!beispiel] Well-Known Ports
> - 20/21: FTP
> - 22: SSH
> - 23: Telnet
> - 25: SMTP
> - 53: DNS
> - 80: HTTP
> - 443: HTTPS

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **IETF** entwickelt Internet-Standards nach dem Prinzip „Rough Consensus and Running Code"
> - **RFCs** sind die verbindlichen Spezifikationen des Internets
> - Der RFC-Prozess ist offen – jeder kann Internet-Drafts einreichen
> - **RFC 2119** definiert die Schlüsselwörter (MUST, SHOULD, MAY)
> - Standards durchlaufen: Proposed Standard → Internet Standard
> - **IANA** verwaltet zentrale Nummern (Ports, IP-Adressen, etc.)
> - April Fools' Day RFCs sind Tradition seit 1978

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Wissen Sie, was ein RFC ist und wer sie veröffentlicht
> - Kennen Sie die RFC 2119 Schlüsselwörter und ihre Bedeutung
> - Können Sie den Unterschied zwischen Proposed/Internet Standard erklären
> - Kennen Sie einige wichtige RFC-Nummern (791=IPv4, 793=TCP, 8200=IPv6)
> - Verstehen Sie die Rolle der IANA

## Verwandte Themen

- [[01-Uebersicht]] – Standardisierungsgremien im Überblick
- [[02-IEEE-Standards]] – IEEE 802.x Standards
- [[03-Referenzmodelle/00-Referenzmodelle-Index|Referenzmodelle]] – OSI und TCP/IP

## Referenzen im Anhang

### RFCs

- [[07-Anhang/RFCs/00-RFCs-Index|RFC-Index]] – Vollständige Sammlung

### Organisationen

- [[07-Anhang/IT-Related-Organisations/IETF|IETF]]
- [[07-Anhang/IT-Related-Organisations/IANA|IANA]]
- [[07-Anhang/IT-Related-Organisations/ICANN|ICANN]]

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- IETF: [ietf.org](https://www.ietf.org/)
- RFC Editor: [rfc-editor.org](https://www.rfc-editor.org/)
- IETF Datatracker: [datatracker.ietf.org](https://datatracker.ietf.org/)
- RFC 2119: [Key words for use in RFCs](https://www.rfc-editor.org/rfc/rfc2119)
