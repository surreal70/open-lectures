---
title: "RFC 2131 - Dynamic Host Configuration Protocol (DHCP)"
rfc_number: 2131
version: "March 1997"
status: Draft Standard
author: "R. Droms"
obsoletes: "RFC 1541"
obsoleted_by: ""
updated_by: "RFC 3396, RFC 4361, RFC 5494, RFC 6842"
language: DE
tags:
  - rfc
  - networking
  - dhcp
  - ip-configuration
  - foundation
---

# RFC 2131 - Dynamic Host Configuration Protocol (DHCP)

## Überblick

RFC 2131 definiert das Dynamic Host Configuration Protocol (DHCP), das ein Framework für die automatische Konfiguration von IP-Adressen und anderen Netzwerkparametern bereitstellt. DHCP ist ein grundlegender Dienst für den Netzwerkbetrieb.

## Zusammenfassung

DHCP automatisiert die Netzwerkkonfiguration:

- **IP-Adresszuweisung**: Automatische IP-Zuordnung
- **Lease-Verwaltung**: Temporäre Adresszuweisungen
- **Konfigurationsoptionen**: DNS, Gateway, NTP, etc.
- **Client/Server-Modell**: DHCP-Server verwaltet Adresspool
- **Relay-Agents**: Weiterleitung von Anfragen über Subnetze

## DHCP-Ablauf (DORA)

```
┌────────┐                          ┌────────┐
│ Client │                          │ Server │
└───┬────┘                          └───┬────┘
    │                                   │
    │ ──── DHCPDISCOVER (Broadcast) ──► │
    │                                   │
    │ ◄──── DHCPOFFER ───────────────── │
    │                                   │
    │ ──── DHCPREQUEST (Broadcast) ──►  │
    │                                   │
    │ ◄──── DHCPACK ─────────────────── │
    │                                   │
```

**DORA-Prozess:**
1. **D**iscover - Client sendet Broadcast um Server zu finden
2. **O**ffer - Server bietet eine IP-Adresse an
3. **R**equest - Client fordert angebotene Adresse an
4. **A**ck - Server bestätigt die Lease

## DHCP-Nachrichtentypen

| Typ | Name | Beschreibung |
|-----|------|--------------|
| 1 | DHCPDISCOVER | Client sendet Broadcast um Server zu finden |
| 2 | DHCPOFFER | Server bietet Konfiguration an |
| 3 | DHCPREQUEST | Client fordert angebotene Parameter an |
| 4 | DHCPDECLINE | Client lehnt angebotene Adresse ab |
| 5 | DHCPACK | Server bestätigt Lease |
| 6 | DHCPNAK | Server lehnt Anfrage ab |
| 7 | DHCPRELEASE | Client gibt Adresse frei |
| 8 | DHCPINFORM | Client fordert nur lokale Konfiguration an |

## Häufige DHCP-Optionen

| Option | Name | Beschreibung |
|--------|------|--------------|
| 1 | Subnet Mask | Netzwerkmaske |
| 3 | Router | Standard-Gateway |
| 6 | DNS Servers | Nameserver |
| 15 | Domain Name | DNS-Domain |
| 42 | NTP Servers | Zeitserver |
| 51 | Lease Time | Dauer der Lease |
| 54 | Server Identifier | DHCP-Server-IP |
| 66 | TFTP Server | Boot-Server (PXE) |
| 67 | Bootfile Name | Boot-Image (PXE) |

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | UDP |
| Server-Port | 67 |
| Client-Port | 68 |
| Lease-Typen | Automatisch, Dynamisch, Manuell |
DHCP bietet automatische IP-Konfiguration:

- Server: OPNsense-Firewalls pro Standort
- Optionen: DNS (10.10.100.101), NTP, Gateway
- Lease-Tracking: Pro VLAN-Pools

## Offizielles Dokument

**RFC 2131**: [https://www.rfc-editor.org/rfc/rfc2131](https://www.rfc-editor.org/rfc/rfc2131)

## Verwandte RFCs

- [[RFC 2132 DHCP Options]] - DHCP Options and BOOTP Vendor Extensions
- [[RFC 4361 DHCPv4 Client Identifiers]] - Node-specific Identifiers for DHCPv4
- [[RFC 3927 Link-Local]] - Fallback wenn DHCP nicht verfügbar
- [[RFC 791 IPv4]] - IP-Adressierung
