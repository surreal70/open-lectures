---
title: "RFCs - Request for Comments"
version: 1.1.0
author: "Andreas Hümmer"
created: 2026-10-07
updated: 2026-10-07
language: DE
tags:
  - rfc
  - standards
  - ietf
  - index
---

# RFCs - Request for Comments

Dieser Abschnitt enthält Zusammenfassungen und Verweise auf RFC-Dokumente (Request for Comments), die für Betriebssysteme, Rechnernetze und verteilte Systeme relevant sind.

## Über RFCs

RFCs sind Veröffentlichungen der Internet Engineering Task Force (IETF) und anderer Standardisierungsgremien, die Protokolle, Verfahren und Konzepte für das Internet definieren. Sie sind wesentliche Referenzen zum Verständnis von Netzwerk-, Sicherheits- und Infrastrukturstandards.

## RFC-Index

### IPv4/IPv6 und Adressierung

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 791 IPv4]] | Internet Protocol (IPv4) | Kern-Netzwerkprotokoll |
| [[RFC 950 Subnetting]] | Subnetting Procedure | Netzwerk-Unterteilung |
| [[RFC 1918 Private Networks]] | Private Internets | Private IP-Bereiche |
| [[RFC 8200 IPv6]] | Internet Protocol Version 6 | IPv6-Spezifikation |
| [[RFC 4291 IPv6 Addressing]] | IPv6 Addressing Architecture | IPv6-Adressierung |
| [[RFC 4862 IPv6 SLAAC]] | Stateless Address Autoconfiguration | IPv6-Autokonfiguration |
| [[RFC 4193 Unique Local IPv6]] | Unique Local IPv6 Addresses | Private IPv6-Adressen |
| [[RFC 6890 Special-Purpose Addresses]] | Special-Purpose IP Addresses | Sonderzweck-Adressen |

### Layer 2 und Overlay

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 826 ARP]] | Address Resolution Protocol | MAC-Auflösung |
| [[RFC 5227 ARP Conflict Detection]] | IPv4 Address Conflict Detection | ARP-Konflikterkennung |
| [[RFC 3927 Link-Local]] | IPv4 Link-Local Addresses | APIPA/DHCP-Fallback |
| [[RFC 7348 VXLAN]] | Virtual eXtensible LAN | Overlay-Netzwerke |
| [[RFC 7432 BGP EVPN]] | BGP MPLS-Based Ethernet VPN | EVPN-Grundlagen |
| [[RFC 8365 EVPN Overlay]] | EVPN Network Virtualization | EVPN + VXLAN |

### Multicast

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 5771 Multicast]] | IPv4 Multicast Addresses | Multicast-Adressverwaltung |
| [[RFC 1112 IGMP]] | Host Extensions for IP Multicasting | IGMPv1 |
| [[RFC 3376 IGMPv3]] | IGMP Version 3 | IGMPv3 mit Source Filtering |
| [[RFC 4604 SSM]] | Source-Specific Multicast | SSM mit IGMPv3/MLDv2 |

### DNS

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 1034 DNS Concepts]] | DNS Concepts and Facilities | DNS-Konzepte |
| [[RFC 1035 DNS]] | Domain Name System | DNS-Implementierung |
| [[RFC 4033-4035 DNSSEC]] | DNS Security Extensions | DNSSEC-Signierung |
| [[RFC 5155 NSEC3]] | NSEC3 Hashed Denial | Zone Walking Schutz |
| [[RFC 6781 DNSSEC Practices]] | DNSSEC Operational Practices | DNSSEC-Betrieb |
| [[RFC 8484 DoH]] | DNS over HTTPS | Verschlüsseltes DNS (HTTPS) |
| [[RFC 7858 DoT]] | DNS over TLS | Verschlüsseltes DNS (TLS) |

### Konfiguration und Zeit

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 2131 DHCP]] | Dynamic Host Configuration Protocol | DHCP-Protokoll |
| [[RFC 2132 DHCP Options]] | DHCP Options | DHCP-Optionen |
| [[RFC 4361 DHCPv4 Client Identifiers]] | DHCPv4 Client Identifiers | Client-Identifikation |
| [[RFC 5905 NTP]] | Network Time Protocol v4 | Zeitdienste |

### E-Mail

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 5321 SMTP]] | Simple Mail Transfer Protocol | E-Mail-Transport |
| [[RFC 3207 SMTP STARTTLS]] | SMTP STARTTLS | SMTP-Verschlüsselung |
| [[RFC 7208 SPF]] | Sender Policy Framework | Absendervalidierung |
| [[RFC 6376 DKIM]] | DomainKeys Identified Mail | E-Mail-Signierung |
| [[RFC 8463 Ed25519 DKIM]] | Ed25519 for DKIM | Moderne DKIM-Signaturen |
| [[RFC 7489 DMARC]] | Domain-based Message Authentication | E-Mail-Richtlinie |

### TLS und Zertifikate

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 8446 TLS 1.3]] | Transport Layer Security 1.3 | TLS-Verschlüsselung |
| [[RFC 8447 TLS IANA Registry]] | TLS IANA Registry Updates | TLS-Registrierung |
| [[RFC 8449 TLS Record Size]] | TLS Record Size Limit | TLS für IoT |
| [[RFC 8555 ACME]] | Automatic Certificate Management | Let's Encrypt |
| [[RFC 8737 ACME ALPN Challenge]] | ACME TLS-ALPN-01 | ACME Port 443 Challenge |
| [[RFC 8738 ACME IP Validation]] | ACME IP Identifier | IP-Zertifikate |

### OAuth und Authentifizierung

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 6749 OAuth 2.0]] | OAuth 2.0 Framework | Autorisierung |
| [[RFC 6750 OAuth Bearer Token]] | OAuth 2.0 Bearer Token | Token-Verwendung |
| [[RFC 7636 PKCE]] | Proof Key for Code Exchange | Sicherheit für Public Clients |
| [[RFC 8252 OAuth Native Apps]] | OAuth for Native Apps | Mobile/Desktop OAuth |
| [[RFC 7519 JWT]] | JSON Web Token | Token-Format |
| [[RFC 4511 LDAP]] | Lightweight Directory Access Protocol | Verzeichnisdienste |

### HTTP

| RFC | Titel | Beschreibung |
|-----|-------|--------------|
| [[RFC 9110 HTTP Semantics]] | HTTP Semantics | HTTP-Grundlagen |
| [[RFC 9111 HTTP Caching]] | HTTP Caching | HTTP-Cache |
| [[RFC 9112 HTTP 1.1]] | HTTP/1.1 | HTTP/1.1 Syntax |
| [[RFC 9113 HTTP 2]] | HTTP/2 | Binäres HTTP |
| [[RFC 9114 HTTP 3]] | HTTP/3 | HTTP über QUIC |

## Statistik

| Kategorie | Anzahl |
|-----------|--------|
| IPv4/IPv6 & Adressierung | 8 |
| Layer 2 & Overlay | 6 |
| Multicast | 4 |
| DNS | 7 |
| Konfiguration & Zeit | 4 |
| E-Mail | 6 |
| TLS & Zertifikate | 6 |
| OAuth & Authentifizierung | 6 |
| HTTP | 5 |
| **Gesamt** | **52** |

## Externe Ressourcen

- [IETF RFC-Index](https://www.rfc-editor.org/rfc-index.html)
- [RFC-Suche](https://www.rfc-editor.org/search/rfc_search.php)
- [IETF Datatracker](https://datatracker.ietf.org/)
