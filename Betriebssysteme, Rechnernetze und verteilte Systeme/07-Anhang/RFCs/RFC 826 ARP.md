---
title: "RFC 826 - Address Resolution Protocol (ARP)"
rfc_number: 826
version: "November 1982"
status: Internet Standard
author: "D. Plummer"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - networking
  - arp
  - layer2
  - ethernet
---

# RFC 826 - Address Resolution Protocol (ARP)

## Überblick

RFC 826 definiert das Address Resolution Protocol (ARP), das Netzwerkschicht-Adressen (IPv4) auf Verbindungsschicht-Adressen (MAC/Ethernet) abbildet. ARP ist essentiell für die Kommunikation in lokalen Ethernet-Netzwerken.

## Zusammenfassung

ARP löst IP-Adressen zu MAC-Adressen auf:

- **Request/Reply-Modell**: Broadcast-Anfrage, Unicast-Antwort
- **Cache**: ARP-Tabelle speichert aktuelle Zuordnungen
- **Broadcast**: ARP-Anfragen werden an alle Hosts im Segment gesendet
- **Gratuitous ARP**: Ankündigung/Aktualisierung der IP-MAC-Zuordnung

## ARP-Ablauf

```
Host A möchte an Host B senden (kennt IP, benötigt MAC):

1. Host A: ARP-Anfrage (Broadcast)
   "Wer hat 192.168.1.10? Sag es 192.168.1.1"
   
2. Host B: ARP-Antwort (Unicast)
   "192.168.1.10 ist bei AA:BB:CC:DD:EE:FF"
   
3. Host A: Speichert die Zuordnung im Cache, sendet Paket
```

## ARP-Paketformat

| Feld | Größe | Beschreibung |
|------|-------|--------------|
| Hardware Type | 2 Bytes | 1 = Ethernet |
| Protocol Type | 2 Bytes | 0x0800 = IPv4 |
| Hardware Length | 1 Byte | 6 für Ethernet |
| Protocol Length | 1 Byte | 4 für IPv4 |
| Operation | 2 Bytes | 1=Anfrage, 2=Antwort |
| Sender Hardware Address | 6 Bytes | Quell-MAC |
| Sender Protocol Address | 4 Bytes | Quell-IP |
| Target Hardware Address | 6 Bytes | Ziel-MAC |
| Target Protocol Address | 4 Bytes | Ziel-IP |

## ARP-Typen

| Typ | Beschreibung |
|-----|--------------|
| ARP Request | Anfrage nach MAC-Adresse |
| ARP Reply | Antwort mit MAC-Adresse |
| Gratuitous ARP | Unaufgeforderte Ankündigung |
| Proxy ARP | Router antwortet für andere Hosts |
| Reverse ARP (RARP) | MAC zu IP (veraltet, ersetzt durch DHCP) |

## Sicherheitsüberlegungen

| Angriff | Beschreibung | Gegenmaßnahme |
|---------|--------------|---------------|
| ARP Spoofing | Gefälschte ARP-Antworten | Statisches ARP, DAI |
| ARP Cache Poisoning | Korrumpiert ARP-Cache | 802.1X, Port-Security |
| MITM via ARP | Abfangen von Verkehr | Verschlüsselung, VLANs |
ARP arbeitet in allen Ethernet-Netzwerken:
- CARP/VRRP verwendet Gratuitous ARP für Failover

## Offizielles Dokument

**RFC 826**: [https://www.rfc-editor.org/rfc/rfc826](https://www.rfc-editor.org/rfc/rfc826)

## Verwandte RFCs

- [[RFC 791 IPv4]] - IP-Adressierung
- RFC 903 - Reverse ARP (RARP) - veraltet
- [[RFC 5227 ARP Conflict Detection]] - IPv4 Address Conflict Detection
- RFC 5494 - IANA Allocation Guidelines for ARP
