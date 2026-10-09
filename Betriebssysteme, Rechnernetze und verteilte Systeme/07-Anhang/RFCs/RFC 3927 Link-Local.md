---
title: "RFC 3927 - Dynamic Configuration of IPv4 Link-Local Addresses"
rfc_number: 3927
version: "May 2005"
status: Proposed Standard
author: "S. Cheshire, B. Aboba, E. Guttman"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - ipv4
  - link-local
  - apipa
  - zeroconf
---

# RFC 3927 - IPv4 Link-Local-Adressen

## Überblick

RFC 3927 beschreibt, wie Hosts automatisch IPv4-Adressen im Bereich 169.254.0.0/16 konfigurieren können, wenn kein DHCP-Server verfügbar ist. Dies ermöglicht grundlegende Netzwerkkonnektivität ohne manuelle Konfiguration oder DHCP-Infrastruktur.

## Zusammenfassung

Link-Local-Adressierung bietet Fallback-Konnektivität:

- **Automatische Zuweisung**: Keine DHCP- oder manuelle Konfiguration erforderlich
- **Adressbereich**: 169.254.1.0 – 169.254.254.255
- **Lokaler Geltungsbereich**: Nicht über die Verbindung hinaus routbar
- **Konflikterkennung**: ARP-Prüfung vor Verwendung
- **Koexistenz**: Kann parallel zu DHCP laufen

## Adressauswahlprozess

```
1. Zufällige Adresse aus 169.254.1.0 – 169.254.254.255 auswählen
2. ARP-Probes senden (prüfen ob Adresse in Verwendung)
3. Bei Konflikt: neue zufällige Adresse auswählen, wiederholen
4. Bei keinem Konflikt: Adresse beanspruchen, Gratuitous ARP senden
5. Während der Nutzung auf Konflikte überwachen
```

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Adressbereich | 169.254.0.0/16 |
| Nutzbarer Bereich | 169.254.1.0 – 169.254.254.255 |
| Reserviert | 169.254.0.0/24, 169.254.255.0/24 |
| Geltungsbereich | Nur Link-lokal (nicht routbar) |

## Implementierungsnamen

| Betriebssystem | Name |
|----------------|------|
| Windows | APIPA (Automatic Private IP Addressing) |
| macOS | Bonjour / mDNSResponder |
| Linux | avahi, systemd-networkd |
| Allgemein | Zeroconf |

## ARP-Prüfung

Bevor eine Adresse verwendet wird, müssen Hosts prüfen:

| Schritt | Aktion | Zweck |
|---------|--------|-------|
| 1 | ARP Probe senden (3x) | Prüfen ob Adresse in Verwendung |
| 2 | 2 Sekunden warten | Auf Antworten warten |
| 3 | Bei Antwort: Konflikt | Neue Adresse auswählen |
| 4 | Bei keiner Antwort: beanspruchen | Adresse verfügbar |
| 5 | ARP Announcement senden | Nachbarn informieren |
Link-Local-Adressen dienen als DHCP-Fallback:
- [[RFC 2131 DHCP]] - Primäre Konfigurationsmethode
- Windows/Linux-Clients: Automatischer Fallback aktiviert

**Hinweis:** Link-Local-Adressen weisen auf DHCP-Ausfall hin und sollten eine Untersuchung auslösen.

## Offizielles Dokument

**RFC 3927**: [https://www.rfc-editor.org/rfc/rfc3927](https://www.rfc-editor.org/rfc/rfc3927)

## Verwandte RFCs

- [[RFC 2131 DHCP]] - Primäre IP-Konfiguration
- [[RFC 826 ARP]] - Address Resolution Protocol
- [[RFC 6890 Special-Purpose Addresses]] - Sonderzweck-Adressregister
- [[RFC 5227 ARP Conflict Detection]] - IPv4 Address Conflict Detection
