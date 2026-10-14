---
author: Andreas Hümmer
title: DNS - Domain Name System
tags:
  - content
  - rn
  - protokolle
  - dns
  - layer7
  - namensauflösung
  - netzwerkdienst
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# DNS – Domain Name System

## Definition

Das **Domain Name System (DNS)** ist ein hierarchisches, verteiltes System zur Namensauflösung. Es übersetzt menschenlesbare Domainnamen (z.B. `www.example.de`) in IP-Adressen (z.B. `93.184.216.34`) und umgekehrt.

> [!info] Schichtzuordnung
> DNS ist ein **Layer-7-Protokoll** (Anwendungsschicht), das primär **UDP Port 53** verwendet. Für Zonentransfers und große Antworten (>512 Bytes) wird **TCP Port 53** genutzt.

## Warum DNS?

```
┌─────────────────────────────────────────────────────────────────┐
│              Das Problem: Menschen vs. Computer                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Menschen merken sich:     Computer brauchen:                  │
│   ────────────────────      ──────────────────                  │
│   www.google.de             142.250.185.99                      │
│   mail.example.org          93.184.216.34                       │
│   ftp.firma.local           192.168.1.50                        │
│                                                                  │
│   DNS ist das "Telefonbuch" des Internets:                     │
│   Name → IP-Adresse (Forward Lookup)                           │
│   IP-Adresse → Name (Reverse Lookup)                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## DNS-Hierarchie

> [!info] RFC-Referenz
> - DNS Concepts: [[A-RFC-Index#RFC 1034|RFC 1034]]
> - DNS Implementation: [[A-RFC-Index#RFC 1035|RFC 1035]]

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNS-Hierarchie (Baumstruktur)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                            . (Root)                             │
│                    13 Root-Server weltweit                      │
│                    a.root-servers.net bis                       │
│                    m.root-servers.net                           │
│                               │                                  │
│         ┌─────────────────────┼─────────────────────┐           │
│         │                     │                     │           │
│        com                   de                    org          │
│    (Generic TLD)        (Country Code       (Generic TLD)       │
│                           TLD - ccTLD)                          │
│         │                     │                     │           │
│    ┌────┴────┐          ┌─────┴─────┐              │           │
│    │         │          │           │              │           │
│  google   amazon     example     bund         wikipedia         │
│ (SLD)    (SLD)       (SLD)      (SLD)          (SLD)           │
│    │                    │                                       │
│   www                 mail                                      │
│ (Host)              (Host)                                      │
│                                                                  │
│   FQDN: www.google.com.  (beachte den Punkt am Ende!)          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Hierarchie-Ebenen

| Ebene | Name | Beispiel | Beschreibung |
|-------|------|----------|--------------|
| **0** | Root | `.` | 13 Root-Server (a-m.root-servers.net) |
| **1** | TLD | `.de`, `.com`, `.org` | Top-Level-Domain |
| **2** | SLD | `example.de` | Second-Level-Domain |
| **3+** | Subdomain | `www.example.de` | Subdomains/Hosts |

> [!tip] FQDN
> Ein **Fully Qualified Domain Name (FQDN)** endet immer mit einem Punkt: `www.example.de.`
> Der Punkt repräsentiert die Root-Zone.

## DNS-Auflösung

### Rekursive vs. Iterative Auflösung

```
┌─────────────────────────────────────────────────────────────────┐
│              Rekursive Auflösung (Client-Sicht)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Client ───────────────────────────► Resolver                  │
│     │                                     │                     │
│     │  "Löse www.example.de auf"         │                     │
│     │ ─────────────────────────────────► │                     │
│     │                                     │ ← Resolver          │
│     │                                     │   erledigt alles    │
│     │  "Antwort: 93.184.216.34"          │                     │
│     │ ◄───────────────────────────────── │                     │
│     │                                     │                     │
│                                                                  │
│   → Client fragt einmal, Resolver liefert Endergebnis          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              Iterative Auflösung (Resolver-Sicht)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Resolver    Root-Server    TLD-Server    Auth-Server         │
│      │             │              │              │              │
│      │ "www.example.de?"         │              │              │
│      │────────────►│              │              │              │
│      │             │              │              │              │
│      │ "Frag .de-Server"         │              │              │
│      │◄────────────│              │              │              │
│      │                            │              │              │
│      │ "www.example.de?"         │              │              │
│      │───────────────────────────►│              │              │
│      │                            │              │              │
│      │ "Frag ns1.example.de"     │              │              │
│      │◄───────────────────────────│              │              │
│      │                                           │              │
│      │ "www.example.de?"                        │              │
│      │──────────────────────────────────────────►│              │
│      │                                           │              │
│      │ "93.184.216.34"                          │              │
│      │◄──────────────────────────────────────────│              │
│      │                                                          │
│                                                                  │
│   → Resolver erhält bei jedem Schritt nur einen Verweis        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Vollständiger DNS-Auflösungsprozess

```
┌─────────────────────────────────────────────────────────────────┐
│          Vollständige DNS-Auflösung für www.example.de         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. Client prüft lokalen Cache und /etc/hosts                 │
│      → Nicht gefunden                                          │
│                                                                  │
│   2. Client fragt konfigurierten DNS-Resolver (z.B. 8.8.8.8)   │
│      (rekursive Anfrage)                                       │
│                                                                  │
│   3. Resolver prüft seinen Cache                               │
│      → Nicht gefunden                                          │
│                                                                  │
│   4. Resolver fragt Root-Server (a.root-servers.net)           │
│      → Antwort: "Frag die .de-Server" (NS für .de)            │
│                                                                  │
│   5. Resolver fragt .de-TLD-Server                             │
│      → Antwort: "Frag ns1.example.de" (NS für example.de)     │
│                                                                  │
│   6. Resolver fragt ns1.example.de (autoritativer Server)      │
│      → Antwort: "www.example.de = 93.184.216.34" (A-Record)   │
│                                                                  │
│   7. Resolver speichert Antwort im Cache (TTL beachten!)       │
│                                                                  │
│   8. Resolver antwortet dem Client                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## DNS-Caching

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNS-Caching                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Caching-Ebenen:                                               │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ 1. Browser-Cache (Chrome, Firefox, etc.)                │  │
│   │ 2. Betriebssystem-Cache (nscd, systemd-resolved)        │  │
│   │ 3. Lokaler Resolver-Cache (Router, Pi-hole)             │  │
│   │ 4. ISP-Resolver-Cache                                   │  │
│   │ 5. Öffentliche Resolver (8.8.8.8, 1.1.1.1)             │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   TTL (Time To Live):                                          │
│   • Bestimmt, wie lange ein Eintrag gecacht werden darf       │
│   • Typische Werte: 300s (5 Min) bis 86400s (1 Tag)           │
│   • Nach Ablauf: Neue Anfrage erforderlich                    │
│                                                                  │
│   Negative Caching:                                            │
│   • Auch "NXDOMAIN" (Domain existiert nicht) wird gecacht     │
│   • Verhindert wiederholte Anfragen für nicht existente Namen │
│   • SOA MINIMUM-Feld bestimmt negative TTL                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## DNS-Paketformat

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│              ID               │QR| Opcode |AA|TC|RD|RA| Z |RCODE│
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│            QDCOUNT            │            ANCOUNT            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│            NSCOUNT            │            ARCOUNT            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                         Question Section                      │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                         Answer Section                        │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                        Authority Section                      │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                       Additional Section                      │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### Header-Felder

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **ID** | 16 | Transaktions-ID (zur Zuordnung Anfrage/Antwort) |
| **QR** | 1 | 0 = Query, 1 = Response |
| **Opcode** | 4 | 0 = Standard Query, 1 = Inverse Query, 2 = Status |
| **AA** | 1 | Authoritative Answer |
| **TC** | 1 | Truncated (Antwort zu groß für UDP) |
| **RD** | 1 | Recursion Desired (Client wünscht Rekursion) |
| **RA** | 1 | Recursion Available (Server unterstützt Rekursion) |
| **RCODE** | 4 | Response Code (0=OK, 3=NXDOMAIN) |
| **QDCOUNT** | 16 | Anzahl Fragen |
| **ANCOUNT** | 16 | Anzahl Antworten |
| **NSCOUNT** | 16 | Anzahl Authority Records |
| **ARCOUNT** | 16 | Anzahl Additional Records |

### Sektionen

| Sektion | Inhalt |
|---------|--------|
| **Question** | Angefragter Name, Typ und Klasse |
| **Answer** | Antwort-Records (A, AAAA, MX, etc.) |
| **Authority** | Nameserver-Records (NS) für die Zone |
| **Additional** | Zusätzliche hilfreiche Records (z.B. IP der NS) |

## DNS Record-Typen

| Typ | IPv4 | IPv6 | Beschreibung | Beispiel |
|-----|------|------|--------------|----------|
| **A** | ✓ | - | Name → IPv4-Adresse | `www IN A 192.168.1.2` |
| **AAAA** | - | ✓ | Name → IPv6-Adresse | `www IN AAAA 2001:db8::1` |
| **PTR** | ✓ | ✓ | IP → Name (Reverse) | `2.1.168.192.in-addr.arpa. IN PTR www.example.de.` |
| **CNAME** | ✓ | ✓ | Alias für Namen | `www IN CNAME webserver.example.de.` |
| **NS** | ✓ | ✓ | Nameserver für Zone | `example.de. IN NS ns1.example.de.` |
| **MX** | ✓ | ✓ | Mailserver (mit Priorität) | `example.de. IN MX 10 mail.example.de.` |
| **TXT** | ✓ | ✓ | Textinformation | SPF, DKIM, DMARC, Domain Verification |
| **SOA** | ✓ | ✓ | Start of Authority | Seriennummer, Refresh, Retry, Expire, Minimum |
| **SRV** | ✓ | ✓ | Service-Lokalisierung | `_ldap._tcp.example.de. IN SRV 0 100 389 dc.example.de.` |
| **CAA** | ✓ | ✓ | Certificate Authority Auth. | Wer darf Zertifikate ausstellen |

### Beispiel: Zonendatei

```dns
$TTL 86400
@       IN  SOA     ns1.example.de. admin.example.de. (
                    2024101301  ; Serial
                    3600        ; Refresh (1h)
                    1800        ; Retry (30min)
                    604800      ; Expire (1 Woche)
                    86400 )     ; Minimum TTL (1 Tag)

; Nameserver
@       IN  NS      ns1.example.de.
@       IN  NS      ns2.example.de.

; Mailserver
@       IN  MX  10  mail.example.de.
@       IN  MX  20  backup-mail.example.de.

; A-Records
@       IN  A       93.184.216.34
www     IN  A       93.184.216.34
mail    IN  A       93.184.216.35
ns1     IN  A       93.184.216.10
ns2     IN  A       93.184.216.11

; AAAA-Records
www     IN  AAAA    2001:db8::1

; CNAME
ftp     IN  CNAME   www.example.de.

; TXT für SPF
@       IN  TXT     "v=spf1 mx -all"
```

## DNS-Zonen

### Zonentypen

| Zonentyp | Beschreibung |
|----------|--------------|
| **Primary (Master)** | Originale Zonendaten, Änderungen nur hier |
| **Secondary (Slave)** | Kopie vom Primary, für Redundanz und Lastverteilung |
| **Stub Zone** | Nur NS-Records, für Delegationen |
| **Forward Zone** | Leitet Anfragen an anderen Server weiter |
| **Hidden Primary** | Primary nicht öffentlich, nur Secondaries antworten |

### Zone Transfers

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNS Zone Transfer                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Primary                                      Secondary        │
│   (Master)                                     (Slave)          │
│      │                                            │             │
│      │  1. SOA-Anfrage (UDP)                     │             │
│      │◄───────────────────────────────────────────│             │
│      │                                            │             │
│      │  2. SOA-Antwort mit Seriennummer          │             │
│      │────────────────────────────────────────────►│             │
│      │                                            │             │
│      │     Seriennummer geändert?                │             │
│      │     Ja → Zone Transfer anfordern          │             │
│      │                                            │             │
│      │  3. AXFR/IXFR Request (TCP)               │             │
│      │◄───────────────────────────────────────────│             │
│      │                                            │             │
│      │  4. Zonendaten übertragen (TCP)           │             │
│      │────────────────────────────────────────────►│             │
│      │                                            │             │
│                                                                  │
│   AXFR = Full Transfer (komplette Zone)                        │
│   IXFR = Incremental Transfer (nur Änderungen)                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Sicherheit

### DNS-Spoofing / Cache Poisoning

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNS Cache Poisoning                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Client         Resolver         Angreifer      Auth-Server   │
│      │               │                │               │         │
│      │  Anfrage      │                │               │         │
│      │──────────────►│                │               │         │
│      │               │  Anfrage       │               │         │
│      │               │────────────────┼──────────────►│         │
│      │               │                │               │         │
│      │               │  Gefälschte    │  Echte       │         │
│      │               │  Antwort!      │  Antwort     │         │
│      │               │◄───────────────│               │         │
│      │               │◄───────────────┼───────────────│         │
│      │               │                │               │         │
│      │               │                │               │         │
│   Resolver akzeptiert die schnellere (gefälschte) Antwort!    │
│   Cache enthält jetzt falsche IP für die Domain.               │
│                                                                  │
│   Angreifer kann Nutzer auf Phishing-Seite umleiten.           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### DNSSEC (DNS Security Extensions)

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNSSEC-Funktionsweise                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   DNSSEC fügt kryptographische Signaturen zu DNS hinzu:        │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ Neue Record-Typen:                                       │  │
│   │ • RRSIG  - Signatur für einen Record-Set                │  │
│   │ • DNSKEY - Öffentlicher Schlüssel der Zone              │  │
│   │ • DS     - Delegation Signer (Vertrauenskette)          │  │
│   │ • NSEC/NSEC3 - Authenticated Denial of Existence        │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Vertrauenskette (Chain of Trust):                            │
│   Root (.) → .de → example.de                                  │
│                                                                  │
│   ✓ Authentizität: Record stammt wirklich vom Zoneninhaber    │
│   ✓ Integrität: Record wurde nicht verändert                   │
│   ✗ Keine Verschlüsselung! Nur Signierung.                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### DoH und DoT (Verschlüsseltes DNS)

| Protokoll | Name | Port | Beschreibung |
|-----------|------|------|--------------|
| **DoT** | DNS over TLS | 853 | DNS in TLS-Tunnel |
| **DoH** | DNS over HTTPS | 443 | DNS als HTTPS-Anfrage |
| **DoQ** | DNS over QUIC | 853 | DNS über QUIC-Protokoll |

```
┌─────────────────────────────────────────────────────────────────┐
│              Klassisches DNS vs. DoH/DoT                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Klassisches DNS:                                              │
│   • Port 53 (UDP/TCP)                                          │
│   • Unverschlüsselt → ISP kann mitlesen                        │
│   • Leicht zu blockieren/umzuleiten                            │
│                                                                  │
│   DoH (DNS over HTTPS):                                        │
│   • Port 443 (wie normaler HTTPS-Traffic)                      │
│   • Verschlüsselt → ISP sieht nur "HTTPS zu 1.1.1.1"          │
│   • Schwer zu blockieren (gleicher Port wie Web)               │
│                                                                  │
│   DoT (DNS over TLS):                                          │
│   • Port 853 (dedizierter Port)                                │
│   • Verschlüsselt → ISP sieht nur "TLS zu DNS-Server"         │
│   • Leichter zu blockieren als DoH                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Praxisbeispiele

> [!example] DNS-Abfragen
> 
> **nslookup (Windows/Linux):**
> ```bash
> $ nslookup www.example.de
> Server:     8.8.8.8
> Address:    8.8.8.8#53
> 
> Non-authoritative answer:
> Name:   www.example.de
> Address: 93.184.216.34
> ```
> 
> **dig (Linux):**
> ```bash
> $ dig www.example.de
> 
> ;; QUESTION SECTION:
> ;www.example.de.            IN      A
> 
> ;; ANSWER SECTION:
> www.example.de.     300     IN      A       93.184.216.34
> 
> ;; Query time: 23 msec
> ;; SERVER: 8.8.8.8#53(8.8.8.8)
> ```
> 
> **dig mit spezifischen Typen:**
> ```bash
> $ dig example.de MX         # Mailserver
> $ dig example.de NS         # Nameserver
> $ dig example.de ANY        # Alle Records
> $ dig @1.1.1.1 example.de   # Bestimmten Server fragen
> $ dig +trace example.de     # Vollständige Auflösung zeigen
> ```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. DNS-Hierarchie (Root, TLD, SLD, Subdomain)
> 2. Rekursive vs. iterative Auflösung
> 3. Wichtige Record-Typen (A, AAAA, MX, CNAME, NS, PTR)
> 4. TTL und Caching
> 5. Zone Transfers (AXFR, IXFR)
> 6. DNSSEC Grundprinzip (Signierung, keine Verschlüsselung)

### Typische Prüfungsfragen

> [!question] Übungsfragen
> 1. Beschreiben Sie den Ablauf einer DNS-Auflösung für www.example.de.
> 2. Was ist der Unterschied zwischen einem A- und einem CNAME-Record?
> 3. Warum ist DNS anfällig für Spoofing? Wie hilft DNSSEC?
> 4. Was bedeutet TTL und welche Auswirkungen hat ein niedriger Wert?
> 5. Erklären Sie Primary vs. Secondary DNS-Server.

### Merkhilfen

> [!tip] Merkregeln
> - **A** = Address (IPv4)
> - **AAAA** = Address (IPv6, 4x A = 128 Bit)
> - **MX** = Mail eXchange
> - **NS** = Name Server
> - **PTR** = PoinTeR (Reverse)
> - **CNAME** = Canonical NAME (Alias)

## Zusammenfassung

```
┌─────────────────────────────────────────────────────────────────┐
│                    DNS auf einen Blick                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zweck:      Namensauflösung (Name ↔ IP-Adresse)              │
│   Schicht:    Layer 7 (Anwendungsschicht)                      │
│   Port:       53 (UDP für Queries, TCP für Transfers)          │
│   Standard:   RFC 1034, RFC 1035                               │
│                                                                  │
│   Hierarchie: Root (.) → TLD (.de) → SLD (example) → Host (www)│
│                                                                  │
│   Auflösung:                                                    │
│   • Rekursiv: Client fragt einmal, Resolver erledigt alles    │
│   • Iterativ: Resolver fragt stufenweise (Root→TLD→Auth)      │
│                                                                  │
│   Wichtige Records: A, AAAA, MX, NS, CNAME, PTR, TXT, SOA     │
│                                                                  │
│   Caching:    TTL bestimmt Gültigkeitsdauer                    │
│   Sicherheit: DNSSEC (Signierung), DoH/DoT (Verschlüsselung)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Querverweise

- [[02-DHCP|DHCP]] – Liefert DNS-Server-Adressen
- [[04-NTP|NTP]] – Zeitsynchronisation für DNSSEC wichtig
- [[../05-Sicherheit/03-TLS|TLS]] – Zertifikate basieren auf DNS-Namen
- [[../03-Referenzmodelle/08-Anwendungsschicht/02-HTTP|HTTP]] – Nutzt DNS für Hostname-Auflösung

## Quellen

- [[A-RFC-Index#RFC 1034|RFC 1034]] - Domain Names - Concepts and Facilities
- [[A-RFC-Index#RFC 1035|RFC 1035]] - Domain Names - Implementation and Specification
- [[A-RFC-Index#RFC 4033|RFC 4033]] - DNS Security Introduction and Requirements (DNSSEC)
- [[A-RFC-Index#RFC 8484|RFC 8484]] - DNS Queries over HTTPS (DoH)
- [[A-RFC-Index#RFC 7858|RFC 7858]] - DNS over TLS (DoT)
