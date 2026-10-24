---
author: Andreas Hümmer
title: TLS
tags:
  - content
  - rn
  - sicherheit
  - tls
  - ssl
  - verschluesselung
created: '2026-10-07'
modified: '2026-10-24'
bereich: RN
---

# TLS

> [!info] Lernziele
> - Verstehen der Grundprinzipien von TLS zur sicheren Kommunikation
> - Kennenlernen des TLS-Handshake-Ablaufs
> - Unterscheiden zwischen symmetrischer und asymmetrischer Verschlüsselung bei TLS
> - Verstehen der Rolle von Zertifikaten bei der Server-Authentifizierung
> - Kennen der Unterschiede zwischen TLS 1.2 und TLS 1.3

## Definition

> [!quote] Definition
> **TLS (Transport Layer Security)** ist ein kryptographisches Protokoll zur Absicherung der Kommunikation über Netzwerke. Es bietet Vertraulichkeit, Integrität und Authentizität auf der Transportschicht.

## Erklärung

TLS ist der Nachfolger von SSL (Secure Sockets Layer) und wird heute für nahezu alle sicherheitskritischen Internetkommunikationen verwendet. Das Protokoll arbeitet zwischen der Anwendungs- und Transportschicht und kann beliebige Anwendungsprotokolle absichern.

### Schutzziele

| Schutzziel | Mechanismus | Beschreibung |
|------------|-------------|--------------|
| **Vertraulichkeit** | Symmetrische Verschlüsselung | Daten können nicht mitgelesen werden |
| **Integrität** | MAC (Message Authentication Code) | Manipulation wird erkannt |
| **Authentizität** | Zertifikate (X.509) | Identität des Servers wird geprüft |
| **Forward Secrecy** | Ephemeral Keys (DHE/ECDHE) | Kompromittierter Langzeitschlüssel gefährdet alte Sessions nicht |

## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **OSI-Schicht** | Zwischen 4 (Transport) und 7 (Anwendung) |
| **Aktuelle Version** | TLS 1.3 (RFC 8446, 2018) |
| **Standardport HTTPS** | 443/tcp |
| **Zertifikatsformat** | X.509 |
| **Schlüsselaustausch** | ECDHE, DHE (TLS 1.3 nur ephemeral) |

## Versionshistorie

| Version | Jahr | Status |
|---------|------|--------|
| SSL 2.0 | 1995 | ⛔ Unsicher, deaktiviert |
| SSL 3.0 | 1996 | ⛔ Unsicher (POODLE), deaktiviert |
| TLS 1.0 | 1999 | ⛔ Deprecated (RFC 8996) |
| TLS 1.1 | 2006 | ⛔ Deprecated (RFC 8996) |
| TLS 1.2 | 2008 | ✓ Noch unterstützt |
| TLS 1.3 | 2018 | ✓ **Empfohlen** |

## TLS-Handshake

Der Handshake etabliert eine sichere Verbindung durch Schlüsselaustausch und optionale Authentifizierung.

### TLS 1.2 Handshake (2-RTT)

![[tls12-handshake.png]]
*<span class="fig-id">05-03-tls12-handshake</span>: TLS 1.2 Handshake mit 10 Nachrichten über zwei Round-Trips.*

### TLS 1.3 Handshake (1-RTT)

TLS 1.3 reduziert den Handshake auf einen Round-Trip durch Parallelisierung:

![[tls13-handshake.png]]
*<span class="fig-id">05-03-tls13-handshake</span>: TLS 1.3 Handshake mit nur einem Round-Trip – Key Share bereits im ClientHello.*

### TLS 1.3: 0-RTT (Early Data)

Bei Wiederaufnahme einer Session kann der Client bereits mit der ersten Nachricht verschlüsselte Daten senden:

- **Vorteil**: Minimale Latenz für wiederholte Verbindungen
- **Risiko**: Replay-Angriffe möglich (nur für idempotente Requests verwenden)

## TLS 1.2 vs. TLS 1.3 Vergleich

| Aspekt | TLS 1.2 | TLS 1.3 |
|--------|---------|---------|
| **Handshake RTT** | 2 | 1 (0 bei Resumption) |
| **Cipher Suites** | ~300 | 5 |
| **Key Exchange** | RSA, DHE, ECDHE | Nur ECDHE/DHE |
| **Symmetric Ciphers** | AES-CBC, RC4, 3DES | Nur AEAD (AES-GCM, ChaCha20) |
| **Hash Functions** | MD5, SHA-1, SHA-256 | Nur SHA-256+ |
| **Forward Secrecy** | Optional | **Obligatorisch** |
| **Renegotiation** | Möglich | Entfernt |
| **Compression** | Möglich | Entfernt (CRIME) |

### Entfernte unsichere Features in TLS 1.3

- RSA Key Exchange (kein Forward Secrecy)
- CBC-Mode Ciphers (Padding-Oracle-Angriffe)
- RC4, 3DES, MD5, SHA-1
- Renegotiation (Komplexität, Angriffsfläche)
- Compression (CRIME-Angriff)

## Cipher Suites

Eine Cipher Suite definiert die Algorithmen für Schlüsselaustausch, Authentifizierung, Verschlüsselung und Integrität.

### TLS 1.2 Cipher Suite Format

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
     │     │         │    │   │    │
     │     │         │    │   │    └── PRF Hash
     │     │         │    │   └────── Key Size
     │     │         │    └────────── Mode (GCM = AEAD)
     │     │         └─────────────── Symmetric Cipher
     │     └───────────────────────── Authentication
     └─────────────────────────────── Key Exchange
```

### TLS 1.3 Cipher Suites (nur 5)

| Cipher Suite | Beschreibung |
|--------------|--------------|
| `TLS_AES_256_GCM_SHA384` | AES-256 im GCM-Modus |
| `TLS_AES_128_GCM_SHA256` | AES-128 im GCM-Modus |
| `TLS_CHACHA20_POLY1305_SHA256` | ChaCha20 mit Poly1305 |
| `TLS_AES_128_CCM_SHA256` | AES-128 im CCM-Modus |
| `TLS_AES_128_CCM_8_SHA256` | AES-128 CCM mit 8-Byte Tag |

> [!info] Hinweis
> In TLS 1.3 ist der Key Exchange (immer ECDHE/DHE) nicht mehr Teil der Cipher Suite.

## Public Key Infrastructure (PKI)

### Zertifikatskette

![[certificate-chain.png]]
*<span class="fig-id">05-03-certificate-chain</span>: Chain of Trust – vom Root CA über Intermediate CA zum Server-Zertifikat.*

### X.509 Zertifikat Felder

| Feld | Beschreibung |
|------|--------------|
| **Subject** | Identität des Zertifikatsinhabers (CN, O, OU, C) |
| **Issuer** | Aussteller (CA) |
| **Serial Number** | Eindeutige Nummer innerhalb der CA |
| **Validity** | Gültigkeitszeitraum (Not Before, Not After) |
| **Public Key** | Öffentlicher Schlüssel des Subjects |
| **Signature** | Signatur der CA über das Zertifikat |
| **Extensions** | SAN, Key Usage, Basic Constraints |

### Subject Alternative Names (SAN)

Moderne Zertifikate verwenden SAN statt CN für Domainnamen:

```
X509v3 Subject Alternative Name:
    DNS:example.com
    DNS:www.example.com
    DNS:*.example.com
    IP Address:192.168.1.1
```

## Zertifikatsvalidierung

Der Client prüft bei jeder TLS-Verbindung:

1. **Kette**: Führt das Zertifikat zu einer vertrauenswürdigen Root CA?
2. **Gültigkeit**: Liegt das aktuelle Datum im Gültigkeitszeitraum?
3. **Hostname**: Stimmt der Hostname mit CN oder SAN überein?
4. **Revocation**: Wurde das Zertifikat widerrufen? (CRL/OCSP)
5. **Key Usage**: Ist das Zertifikat für TLS-Authentifizierung vorgesehen?

### Zertifikatswiderruf

| Methode | Beschreibung | Nachteile |
|---------|--------------|-----------|
| **CRL** | Certificate Revocation List | Große Listen, selten aktualisiert |
| **OCSP** | Online Certificate Status Protocol | Latenz, Privacy (CA sieht Anfragen) |
| **OCSP Stapling** | Server liefert OCSP-Antwort mit | Server-Konfiguration nötig |

## Anwendungsprotokolle mit TLS

| Protokoll | Port (unverschlüsselt) | Port (TLS) | Name |
|-----------|------------------------|------------|------|
| HTTP | 80 | 443 | HTTPS |
| SMTP | 25 | 465/587 | SMTPS |
| IMAP | 143 | 993 | IMAPS |
| POP3 | 110 | 995 | POP3S |
| FTP | 21 | 990 | FTPS |
| LDAP | 389 | 636 | LDAPS |

### STARTTLS vs. Implicit TLS

| Methode | Beschreibung |
|---------|--------------|
| **Implicit TLS** | Verbindung startet direkt verschlüsselt (eigener Port) |
| **STARTTLS** | Upgrade von unverschlüsselter Verbindung (gleicher Port) |

> [!warning] STARTTLS-Risiko
> STARTTLS ist anfällig für Downgrade-Angriffe, wenn der Client die STARTTLS-Antwort nicht erzwingt.

## Let's Encrypt und ACME

### Automatische Zertifikatsverwaltung

**Let's Encrypt** ist eine kostenlose CA, die Zertifikate über das ACME-Protokoll automatisiert ausstellt.

**Validierungsmethoden:**

| Challenge | Beschreibung | Anwendung |
|-----------|--------------|-----------|
| **HTTP-01** | Token unter `/.well-known/acme-challenge/` | Webserver |
| **DNS-01** | TXT-Record `_acme-challenge.domain` | Wildcard, DNS-API |
| **TLS-ALPN-01** | Spezielles TLS-Zertifikat auf Port 443 | Reverse Proxies |

```bash
# Beispiel mit Certbot
certbot certonly --webroot -w /var/www/html -d example.com -d www.example.com

# Automatische Erneuerung (Cronjob)
0 0 * * * certbot renew --quiet
```

## Bekannte TLS-Angriffe

| Angriff | Betroffene Version | Beschreibung |
|---------|-------------------|--------------|
| **BEAST** | TLS 1.0 | CBC IV-Vorhersage |
| **CRIME** | TLS + Compression | Kompression leakt Plaintext |
| **POODLE** | SSL 3.0 | Padding-Oracle auf CBC |
| **Heartbleed** | OpenSSL (Implementation) | Buffer Over-Read |
| **DROWN** | SSLv2 | Cross-Protocol-Angriff |
| **ROBOT** | RSA Key Exchange | Bleichenbacher-Angriff |

> [!tip] Empfehlung
> TLS 1.3 eliminiert die meisten dieser Angriffsvektoren durch Entfernung unsicherer Features.

## Beispiele

### Typische TLS-Konfiguration (nginx)

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    # TLS 1.2 und 1.3
    ssl_protocols TLSv1.2 TLSv1.3;
    
    # Sichere Cipher Suites
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;
    
    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
    
    # HSTS
    add_header Strict-Transport-Security "max-age=31536000" always;
}
```

### TLS-Verbindung testen

```bash
# OpenSSL s_client
openssl s_client -connect example.com:443 -servername example.com

# Zertifikat anzeigen
openssl s_client -connect example.com:443 | openssl x509 -text -noout

# TLS-Version erzwingen
openssl s_client -connect example.com:443 -tls1_3

# Cipher Suites des Servers auflisten
nmap --script ssl-enum-ciphers -p 443 example.com
```

### HSTS (HTTP Strict Transport Security)

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

Erzwingt HTTPS für die Domain und optional alle Subdomains. Mit `preload` kann die Domain in Browser-Preload-Listen aufgenommen werden.

## Prüfungstipps

> [!warning] Häufige Klausurfehler
> - Verwechslung von SSL und TLS (SSL ist veraltet, TLS ist der Nachfolger)
> - Annahme, dass TLS auf Schicht 4 arbeitet – es liegt zwischen Schicht 4 und 7
> - Vergessen, dass TLS 1.3 **keinen** RSA Key Exchange mehr unterstützt
> - Verwechslung von symmetrischer (Daten) und asymmetrischer (Handshake) Verschlüsselung

> [!question] Typische Prüfungsfragen
> - Beschreiben Sie den TLS 1.2 Handshake in Grundzügen
> - Was ist Forward Secrecy und warum ist es wichtig?
> - Welche Verbesserungen bringt TLS 1.3 gegenüber TLS 1.2?
> - Wie funktioniert die Zertifikatsvalidierung?
> - Was ist der Unterschied zwischen STARTTLS und Implicit TLS?
> - Auf welchem Port läuft HTTPS?

> [!tip] Prüfungsvorbereitung
> - Verstehe die **zwei Phasen**: Handshake (asymmetrisch) → Datentransfer (symmetrisch)
> - Merke: TLS 1.3 = 1 RTT, TLS 1.2 = 2 RTT
> - Kenne die Zertifikatskette: Root CA → Intermediate CA → Server-Zertifikat
> - Wisse, welche Features TLS 1.3 **entfernt** hat (RSA Key Exchange, CBC, Compression)

---

## Weiterführende Ressourcen

- [RFC 8446 – TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) – Offizielle Spezifikation
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) – Sichere Konfigurationen
- [SSL Labs Server Test](https://www.ssllabs.com/ssltest/) – TLS-Konfiguration testen
- [Let's Encrypt Dokumentation](https://letsencrypt.org/docs/) – Kostenlose Zertifikate
- [Cloudflare Learning: TLS](https://www.cloudflare.com/learning/ssl/what-is-tls/) – Verständliche Einführung

---

## Zusammenhänge

- [[00-Sicherheit-Index]] – Sicherheit Übersicht
- [[01-Firewalls]] – Netzwerkfilterung, HTTPS-Inspection
- [[02-VPN/01-IPsec]] – Alternative auf Schicht 3
- [[02-VPN/03-OpenVPN]] – OpenVPN nutzt TLS für Control Channel
- [[../04-Basisprotokolle/02-HTTP]] – HTTP über TLS = HTTPS

---

## Quellen

- RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2
- RFC 8996: Deprecating TLS 1.0 and TLS 1.1
- Rescorla, E.: "SSL and TLS: Designing and Building Secure Systems"
- https://www.ssllabs.com/
- https://letsencrypt.org/
