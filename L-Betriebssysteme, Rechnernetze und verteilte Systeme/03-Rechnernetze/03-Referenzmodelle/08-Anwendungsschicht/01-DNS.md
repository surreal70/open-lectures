---
author: Andreas Hümmer
title: DNS - Domain Name System
tags:
  - content
  - rn
  - application-layer
  - dns
  - namensaufloesung
  - records
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# DNS - Domain Name System

## Definition

Das **Domain Name System (DNS)** ist ein hierarchisches, verteiltes System zur Auflösung von menschenlesbaren Domainnamen in IP-Adressen und umgekehrt.

## Grundlagen

### Warum DNS?

```
┌────────────────────────────────────────────────────────────────┐
│                   Problem und Lösung                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Menschen merken sich:        Computer brauchen:               │
│  www.google.com               142.250.185.206                  │
│  www.amazon.de                52.95.120.67                     │
│  mail.example.org             192.0.2.1                        │
│                                                                │
│                      ┌───────────┐                             │
│  Domainname ─────────►│   DNS    │─────────► IP-Adresse       │
│                      │  Server   │                             │
│                      └───────────┘                             │
│                                                                │
│  DNS ist das "Telefonbuch des Internets"                      │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Hierarchisch** | Baumstruktur mit Root → TLD → Domain → Subdomain |
| **Verteilt** | Keine zentrale Datenbank, weltweit verteilt |
| **Caching** | Zwischenspeicherung für Performance |
| **Redundant** | Mehrere Server pro Zone |
| **Port** | UDP 53 (Anfragen), TCP 53 (Zonentransfer, große Antworten) |

## DNS-Hierarchie

```
┌────────────────────────────────────────────────────────────────┐
│                      DNS-Hierarchie                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│                          . (Root)                              │
│                             │                                  │
│           ┌─────────────────┼─────────────────┐               │
│           │                 │                 │               │
│          com               de                org              │
│           │                 │                 │               │
│     ┌─────┴─────┐     ┌────┴────┐      ┌────┴────┐          │
│     │           │     │         │      │         │          │
│   google    amazon  example   tum   wikipedia  mozilla       │
│     │           │     │         │      │         │          │
│    www        www   mail      www     de        www          │
│                       │                │                      │
│                     smtp              en                      │
│                                                                │
│  FQDN-Beispiel: www.example.de.                               │
│                 ▲   ▲       ▲  ▲                              │
│                 │   │       │  └── Root (implizit)            │
│                 │   │       └───── TLD (Top-Level Domain)     │
│                 │   └───────────── SLD (Second-Level Domain)  │
│                 └───────────────── Subdomain/Hostname         │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Top-Level Domains (TLDs)

| Kategorie | Beispiele | Beschreibung |
|-----------|-----------|--------------|
| **gTLD** | .com, .org, .net | Generic TLDs |
| **ccTLD** | .de, .at, .ch | Country-Code TLDs |
| **sTLD** | .edu, .gov, .mil | Sponsored TLDs |
| **neue gTLD** | .berlin, .shop, .app | Seit 2012 eingeführt |

## DNS-Server-Typen

```
┌────────────────────────────────────────────────────────────────┐
│                     DNS-Server-Typen                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. ROOT NAME SERVER (13 logische, ~1500 physische)           │
│     ┌─────────────────────────────────────────────────────┐   │
│     │ Kennen die autoritativen Server für alle TLDs       │   │
│     │ a.root-servers.net bis m.root-servers.net           │   │
│     └─────────────────────────────────────────────────────┘   │
│                                                                │
│  2. TLD NAME SERVER                                            │
│     ┌─────────────────────────────────────────────────────┐   │
│     │ Verwalten eine TLD (.com, .de, .org)                │   │
│     │ Kennen autoritative Server der Second-Level Domains │   │
│     └─────────────────────────────────────────────────────┘   │
│                                                                │
│  3. AUTHORITATIVE NAME SERVER                                  │
│     ┌─────────────────────────────────────────────────────┐   │
│     │ Verwalten eine spezifische Domain (z.B. example.de) │   │
│     │ Primary: Original-Daten, Secondary: Kopie           │   │
│     └─────────────────────────────────────────────────────┘   │
│                                                                │
│  4. RECURSIVE RESOLVER (Caching Name Server)                   │
│     ┌─────────────────────────────────────────────────────┐   │
│     │ Führt Auflösung im Auftrag des Clients durch        │   │
│     │ Typisch: ISP-DNS, 8.8.8.8 (Google), 1.1.1.1 (CF)   │   │
│     └─────────────────────────────────────────────────────┘   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## DNS-Auflösung

### Rekursive vs. Iterative Anfrage

```
┌────────────────────────────────────────────────────────────────┐
│                  DNS-Auflösungsprozess                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Client fragt: "Was ist die IP von www.example.de?"           │
│                                                                │
│  ┌────────┐                                                   │
│  │ Client │                                                   │
│  └───┬────┘                                                   │
│      │ 1. Anfrage (rekursiv)                                  │
│      ▼                                                        │
│  ┌────────────┐                                               │
│  │ Recursive  │  2. Cache-Check: nicht vorhanden             │
│  │  Resolver  │                                               │
│  └─────┬──────┘                                               │
│        │ 3. Iterative Anfrage an Root                         │
│        ▼                                                      │
│  ┌────────────┐                                               │
│  │   Root     │  4. Antwort: "Frag .de-Server"               │
│  │   Server   │     (Referral)                                │
│  └────────────┘                                               │
│        │                                                      │
│        ▼ 5. Iterative Anfrage an .de                         │
│  ┌────────────┐                                               │
│  │   .de      │  6. Antwort: "Frag ns.example.de"            │
│  │   TLD      │     (Referral)                                │
│  └────────────┘                                               │
│        │                                                      │
│        ▼ 7. Iterative Anfrage an example.de                  │
│  ┌────────────┐                                               │
│  │ example.de │  8. Antwort: "www.example.de = 93.184.216.34"│
│  │   Auth.    │     (Authoritative Answer)                    │
│  └────────────┘                                               │
│        │                                                      │
│        ▼ 9. Antwort an Client (+ Caching)                    │
│  ┌────────┐                                                   │
│  │ Client │  www.example.de = 93.184.216.34                  │
│  └────────┘                                                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Caching und TTL

> [!info] Time to Live (TTL)
> Jeder DNS-Record hat einen TTL-Wert (in Sekunden), der angibt, wie lange er gecacht werden darf.
> - **Kurze TTL (300s):** Schnelle Änderungen möglich, mehr DNS-Traffic
> - **Lange TTL (86400s):** Weniger Traffic, Änderungen dauern länger

```
Caching-Hierarchie:

┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Browser    │ → │   OS-Cache   │ → │   Resolver   │
│    Cache     │   │ (Stub Res.)  │   │    Cache     │
└──────────────┘   └──────────────┘   └──────────────┘

Cache-Check bei jeder Ebene vor weiterer Anfrage
```

## DNS-Record-Typen

### Wichtige Records

| Typ | Name | Beschreibung | Beispiel |
|-----|------|--------------|----------|
| **A** | Address | IPv4-Adresse | www IN A 93.184.216.34 |
| **AAAA** | IPv6 Address | IPv6-Adresse | www IN AAAA 2606:2800:220:1:... |
| **CNAME** | Canonical Name | Alias für anderen Namen | www IN CNAME server1.example.de. |
| **MX** | Mail Exchange | Mailserver (mit Priorität) | @ IN MX 10 mail.example.de. |
| **NS** | Name Server | Autoritativer NS | @ IN NS ns1.example.de. |
| **PTR** | Pointer | Reverse DNS (IP→Name) | 34.216.184.93.in-addr.arpa IN PTR www.example.de. |
| **TXT** | Text | Beliebiger Text | @ IN TXT "v=spf1 include:..." |
| **SOA** | Start of Authority | Zonen-Metadaten | (siehe unten) |
| **SRV** | Service | Dienst-Lokalisierung | _sip._tcp IN SRV 10 5 5060 sip.example.de. |

### SOA-Record (Start of Authority)

```
example.de.    IN    SOA    ns1.example.de. admin.example.de. (
                            2024010101  ; Serial (YYYYMMDDNN)
                            3600        ; Refresh (1 Stunde)
                            900         ; Retry (15 Minuten)
                            604800      ; Expire (1 Woche)
                            86400       ; Minimum TTL (1 Tag)
                            )
```

### Zonendatei-Beispiel

```
$TTL 86400
@       IN      SOA     ns1.example.de. admin.example.de. (
                        2024010101 3600 900 604800 86400 )

; Nameserver
@       IN      NS      ns1.example.de.
@       IN      NS      ns2.example.de.

; Mailserver
@       IN      MX      10 mail.example.de.
@       IN      MX      20 backup-mail.example.de.

; A-Records
@       IN      A       93.184.216.34
www     IN      A       93.184.216.34
mail    IN      A       93.184.216.35
ns1     IN      A       93.184.216.36
ns2     IN      A       93.184.216.37

; AAAA-Records
@       IN      AAAA    2606:2800:220:1:248:1893:25c8:1946
www     IN      AAAA    2606:2800:220:1:248:1893:25c8:1946

; Aliase
ftp     IN      CNAME   www.example.de.
shop    IN      CNAME   www.example.de.

; TXT-Records (SPF, DKIM, etc.)
@       IN      TXT     "v=spf1 mx a -all"
```

## Reverse DNS (PTR)

Auflösung von IP-Adresse zu Hostname:

```
┌────────────────────────────────────────────────────────────────┐
│                      Reverse DNS                               │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Forward DNS:  www.example.de  →  93.184.216.34               │
│  Reverse DNS:  93.184.216.34   →  www.example.de               │
│                                                                │
│  Spezielle Domain: in-addr.arpa (IPv4)                        │
│                    ip6.arpa (IPv6)                             │
│                                                                │
│  IP: 93.184.216.34                                            │
│  PTR-Lookup: 34.216.184.93.in-addr.arpa                       │
│              └──────────────────────────┘                     │
│                   IP-Oktette umgekehrt!                       │
│                                                                │
│  Verwendung:                                                   │
│  • E-Mail-Server-Verifizierung (Anti-Spam)                    │
│  • Logging (IP → lesbarer Name)                               │
│  • Sicherheitsüberprüfungen                                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## DNS-Sicherheit

### Probleme

| Problem | Beschreibung |
|---------|--------------|
| **DNS Spoofing** | Gefälschte DNS-Antworten einschleusen |
| **Cache Poisoning** | Cache mit falschen Daten vergiften |
| **DNS Amplification** | DDoS-Angriff über offene Resolver |
| **Eavesdropping** | DNS-Anfragen sind unverschlüsselt |

### Lösungen

| Lösung | Beschreibung |
|--------|--------------|
| **DNSSEC** | Digitale Signaturen für DNS-Records |
| **DoH** | DNS over HTTPS (Port 443) |
| **DoT** | DNS over TLS (Port 853) |
| **Response Rate Limiting** | Schutz vor Amplification |

## DNS-Tools

```bash
# Einfache Abfrage
nslookup www.example.de

# Detaillierte Abfrage
dig www.example.de

# Spezifischer Record-Typ
dig www.example.de AAAA
dig example.de MX
dig example.de NS

# Reverse DNS
dig -x 93.184.216.34

# Trace (gesamter Auflösungspfad)
dig +trace www.example.de

# DNS-Server spezifizieren
dig @8.8.8.8 www.example.de
```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Sehr hoch
>
> **Häufige Prüfungsthemen:**
> 1. DNS-Hierarchie (Root, TLD, SLD)
> 2. Record-Typen (A, AAAA, CNAME, MX, NS, PTR)
> 3. Rekursive vs. iterative Auflösung
> 4. Caching und TTL
> 5. Reverse DNS

### Merkregeln

> [!tip] Merkhilfe: Record-Typen
> - **A** = Address (IPv4)
> - **AAAA** = Adresse hoch 4 (IPv6, 4× so lang)
> - **MX** = Mail eXchange
> - **NS** = Name Server
> - **PTR** = PoinTeR (Reverse)
> - **CNAME** = Canonical NAME (Alias)

### Beispielaufgabe

> [!example] DNS-Auflösung erklären
> **Frage:** Beschreiben Sie die Schritte bei der Auflösung von www.tum.de durch einen Client.
>
> **Antwort:**
> 1. Client fragt lokalen Resolver (z.B. Router/ISP)
> 2. Resolver prüft Cache → nicht vorhanden
> 3. Resolver fragt Root-Server → Verweis auf .de-TLD
> 4. Resolver fragt .de-TLD → Verweis auf tum.de NS
> 5. Resolver fragt autoritativen NS von tum.de
> 6. Autoritativer NS antwortet mit IP für www.tum.de
> 7. Resolver cached Antwort und sendet an Client

## Zusammenhänge

- [[02-HTTP]] - DNS-Auflösung vor HTTP-Verbindung
- [[03-SMTP]] - MX-Records für E-Mail-Routing
- [[07-Transportschicht/02-UDP|UDP]] - DNS nutzt primär UDP
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - DNSSEC, DoH, DoT

## Quellen

- [[A-RFC-Index|RFC 1034]] - Domain Names - Concepts and Facilities
- [[A-RFC-Index|RFC 1035]] - Domain Names - Implementation
- [[A-RFC-Index|RFC 4033-4035]] - DNSSEC
- [[A-RFC-Index|RFC 8484]] - DNS over HTTPS (DoH)
