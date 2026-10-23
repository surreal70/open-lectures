---
author: Andreas Hümmer
title: E-Mail-Protokolle (SMTP, IMAP, POP3)
tags:
  - content
  - rn
  - application-layer
  - smtp
  - imap
  - pop3
  - email
created: '2026-10-07'
modified: '2026-10-23'
bereich: RN
---

# E-Mail-Protokolle

## Übersicht

E-Mail-Kommunikation verwendet verschiedene Protokolle für unterschiedliche Aufgaben:

| Protokoll | Funktion | Port (unverschl.) | Port (TLS) |
|-----------|----------|-------------------|------------|
| **SMTP** | Versand von E-Mails | 25, 587 | 465 |
| **IMAP** | Zugriff auf E-Mails (Server-basiert) | 143 | 993 |
| **POP3** | Abruf von E-Mails (Client-basiert) | 110 | 995 |

## E-Mail-Architektur

![[email-architecture.png]]
*<span class="fig-id">03-08-03-email-architecture</span>: E-Mail-Übertragung von Sender zu Empfänger über MTA-Kette*

## SMTP - Simple Mail Transfer Protocol

### Definition

**SMTP** ist das Protokoll zum Versenden und Weiterleiten von E-Mails zwischen Mailservern (MTA zu MTA) und vom E-Mail-Client zum Mailserver.

### SMTP-Kommunikation

![[smtp-dialog.png]]
*<span class="fig-id">03-08-03-smtp-dialog</span>: SMTP-Dialog zwischen Client und Server*

### SMTP-Befehle

| Befehl | Beschreibung |
|--------|--------------|
| **HELO/EHLO** | Begrüßung (EHLO für Extended SMTP) |
| **MAIL FROM:** | Absender-Adresse |
| **RCPT TO:** | Empfänger-Adresse |
| **DATA** | Beginn des Nachrichteninhalts |
| **QUIT** | Verbindung beenden |
| **AUTH** | Authentifizierung |
| **STARTTLS** | TLS-Verschlüsselung starten |
| **RSET** | Transaktion zurücksetzen |
| **VRFY** | Adresse verifizieren |

### SMTP-Statuscodes

| Code | Kategorie | Beispiel |
|------|-----------|----------|
| **2xx** | Erfolg | 250 OK |
| **3xx** | Daten erwartet | 354 Start mail input |
| **4xx** | Temporärer Fehler | 421 Service not available |
| **5xx** | Permanenter Fehler | 550 User unknown |

### SMTP-Ports

| Port | Verwendung |
|------|------------|
| **25** | Server-zu-Server (MTA-MTA) |
| **587** | Client-zu-Server (Submission, mit Auth) |
| **465** | SMTPS (SMTP über TLS, veraltet aber wieder aktuell) |

## IMAP - Internet Message Access Protocol

### Definition

**IMAP** ermöglicht den Zugriff auf E-Mails, die auf dem Server gespeichert bleiben. Ideal für Zugriff von mehreren Geräten.

### IMAP-Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Server-basiert** | E-Mails bleiben auf dem Server |
| **Multi-Device** | Synchronisation zwischen Geräten |
| **Ordnerstruktur** | Verwaltung von Ordnern auf dem Server |
| **Teilweiser Download** | Nur Header oder Teile laden |
| **Flags** | Lese-Status, Markierungen serverseitig |

### IMAP vs. POP3

![[imap-vs-pop3.png]]
*<span class="fig-id">03-08-03-imap-vs-pop3</span>: Vergleich der Speichermodelle von IMAP und POP3*

### IMAP-Befehle

| Befehl | Beschreibung |
|--------|--------------|
| **LOGIN** | Authentifizierung |
| **SELECT** | Ordner auswählen |
| **FETCH** | Nachrichten abrufen |
| **SEARCH** | Nachrichten suchen |
| **STORE** | Flags setzen/löschen |
| **COPY** | Nachrichten kopieren |
| **EXPUNGE** | Gelöschte Nachrichten entfernen |
| **LOGOUT** | Sitzung beenden |

## POP3 - Post Office Protocol

### Definition

**POP3** ist ein einfaches Protokoll zum Herunterladen von E-Mails vom Server auf den lokalen Client.

### POP3-Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Client-basiert** | E-Mails werden heruntergeladen |
| **Single-Device** | Typisch: Ein Hauptgerät |
| **Einfach** | Wenige Befehle |
| **Offline-Zugriff** | Nach Download serverunabhängig |
| **Speicherplatz** | Server wird entlastet |

### POP3-Befehle

| Befehl | Beschreibung |
|--------|--------------|
| **USER** | Benutzername |
| **PASS** | Passwort |
| **STAT** | Status (Anzahl, Größe) |
| **LIST** | Nachrichtenliste |
| **RETR** | Nachricht abrufen |
| **DELE** | Nachricht zum Löschen markieren |
| **QUIT** | Verbindung beenden (löscht markierte) |

### POP3-Dialog

![[pop3-dialog.png]]
*<span class="fig-id">03-08-03-pop3-dialog</span>: POP3-Dialog mit Authentifizierung und Nachrichtenabruf*

## Vergleichstabelle

| Aspekt | SMTP | IMAP | POP3 |
|--------|------|------|------|
| **Funktion** | Versand | Zugriff | Abruf |
| **Richtung** | Client→Server→Server | Client↔Server | Client←Server |
| **Port** | 25/587/465 | 143/993 | 110/995 |
| **E-Mail-Speicherort** | Transit | Server | Client |
| **Komplexität** | Mittel | Hoch | Niedrig |

## E-Mail-Format (RFC 5322)

Eine E-Mail besteht aus **Header** (Metadaten) und **Body** (Inhalt), getrennt durch eine Leerzeile.

### Header-Felder

| Feld | Beschreibung |
|------|--------------|
| **From** | Absender-Adresse |
| **To** | Empfänger-Adresse(n) |
| **Cc** | Kopie-Empfänger (sichtbar) |
| **Bcc** | Blindkopie (nicht sichtbar) |
| **Subject** | Betreff |
| **Date** | Sendedatum und -zeit |
| **Message-ID** | Eindeutige Nachrichten-ID |
| **MIME-Version** | MIME-Standard (meist 1.0) |
| **Content-Type** | Medientyp und Zeichensatz |

> [!example] E-Mail-Struktur
> ```
> From: Alice <alice@example.com>
> To: Bob <bob@mail.de>
> Cc: Carol <carol@example.org>
> Subject: Wichtige Nachricht
> Date: Mon, 13 Oct 2026 10:30:00 +0200
> Message-ID: <abc123@example.com>
> MIME-Version: 1.0
> Content-Type: text/plain; charset="UTF-8"
> 
> Hallo Bob,
> 
> dies ist eine wichtige Nachricht.
> 
> Viele Grüße
> Alice
> ```
> *Header und Body sind durch eine Leerzeile getrennt*

## E-Mail-Sicherheit

### Spam-Schutz

| Mechanismus | Beschreibung |
|-------------|--------------|
| **SPF** | Sender Policy Framework - Autorisierte Server |
| **DKIM** | DomainKeys - Digitale Signatur |
| **DMARC** | Domain-based Message Authentication |

### SPF-Record (DNS TXT)

```
example.com.  IN TXT "v=spf1 mx a ip4:192.0.2.0/24 -all"

v=spf1        → SPF Version 1
mx            → Erlaubt MX-Server der Domain
a             → Erlaubt A-Record der Domain
ip4:...       → Erlaubt IP-Bereich
-all          → Alle anderen ablehnen
```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Mittel bis Hoch
>
> **Häufige Prüfungsthemen:**
> 1. SMTP-Kommandos (EHLO, MAIL FROM, RCPT TO, DATA)
> 2. Unterschied IMAP vs. POP3
> 3. Portnummern für E-Mail-Protokolle
> 4. E-Mail-Übertragungsweg (MUA → MTA → MTA → MDA)
> 5. Grundlegendes Verständnis von SPF/DKIM

### Merkregeln

> [!tip] Merkhilfe: E-Mail-Ports
> **SMTP:** 25 (Server-Server), 587 (Client-Server), 465 (TLS)
> **IMAP:** 143, 993 (TLS)
> **POP3:** 110, 995 (TLS)
> 
> Merke: TLS-Ports sind oft "normal + 860" oder haben eine 9 vorne

## Zusammenhänge

- [[01-DNS]] - MX-Records für E-Mail-Routing
- [[07-Transportschicht/01-TCP|TCP]] - E-Mail-Protokolle nutzen TCP
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - TLS, SPF, DKIM

## Quellen

- [[A-RFC-Index|RFC 5321]] - SMTP
- [[A-RFC-Index|RFC 9051]] - IMAP
- [[A-RFC-Index|RFC 1939]] - POP3
- [[A-RFC-Index|RFC 5322]] - Internet Message Format
- [[A-RFC-Index|RFC 7208]] - SPF
