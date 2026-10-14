---
author: Andreas Hümmer
title: HTTP - Hypertext Transfer Protocol
tags:
  - content
  - rn
  - application-layer
  - http
  - https
  - web
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# HTTP - Hypertext Transfer Protocol

## Definition

Das **Hypertext Transfer Protocol (HTTP)** ist das Anwendungsprotokoll für die Übertragung von Webinhalten zwischen Clients (Browsern) und Servern im World Wide Web.

## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Zustandslos** | Jede Anfrage ist unabhängig (kein Session-State) |
| **Request-Response** | Client fragt an, Server antwortet |
| **Textbasiert** | Menschenlesbare Header (bis HTTP/2) |
| **Erweiterbar** | Neue Header und Methoden möglich |
| **Port** | TCP 80 (HTTP), TCP 443 (HTTPS) |

## HTTP-Versionen

```
┌────────────────────────────────────────────────────────────────┐
│                    HTTP-Entwicklung                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  HTTP/0.9 (1991)                                              │
│  └─ Nur GET, keine Header, nur HTML                           │
│                                                                │
│  HTTP/1.0 (1996)                                              │
│  └─ Header, Methoden, Statuscodes, MIME-Types                 │
│  └─ Eine Verbindung pro Request                               │
│                                                                │
│  HTTP/1.1 (1997)  ← Heute noch weit verbreitet                │
│  └─ Persistent Connections (Keep-Alive)                       │
│  └─ Pipelining, Chunked Transfer, Host-Header                 │
│                                                                │
│  HTTP/2 (2015)                                                │
│  └─ Binäres Protokoll, Multiplexing                           │
│  └─ Header-Kompression (HPACK)                                │
│  └─ Server Push                                               │
│                                                                │
│  HTTP/3 (2022)                                                │
│  └─ Basiert auf QUIC (UDP statt TCP)                         │
│  └─ Verbesserte Performance, 0-RTT                            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## HTTP-Kommunikation

### Request-Response-Zyklus

```
┌────────────────────────────────────────────────────────────────┐
│                  HTTP Request-Response                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Client (Browser)                        Server                │
│       │                                     │                  │
│       │  1. DNS-Auflösung                   │                  │
│       │     www.example.com → 93.184.216.34 │                  │
│       │                                     │                  │
│       │  2. TCP-Verbindung (3-Way-Handshake)│                  │
│       │ ◄──────────────────────────────────►│                  │
│       │                                     │                  │
│       │  3. HTTP Request                    │                  │
│       │  GET /index.html HTTP/1.1           │                  │
│       │  Host: www.example.com              │                  │
│       │ ────────────────────────────────────►│                  │
│       │                                     │                  │
│       │  4. HTTP Response                   │                  │
│       │  HTTP/1.1 200 OK                    │                  │
│       │  Content-Type: text/html            │                  │
│       │  <html>...</html>                   │                  │
│       │ ◄────────────────────────────────────│                  │
│       │                                     │                  │
│       │  5. Weitere Requests (CSS, JS, Bilder)                │
│       │ ◄────────────────────────────────────►                │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## HTTP-Request

### Aufbau

```
┌────────────────────────────────────────────────────────────────┐
│                    HTTP-Request-Format                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Request-Line:    METHODE /pfad/ressource HTTP/Version        │
│  ─────────────────────────────────────────────────────────    │
│  Header:          Header-Name: Header-Wert                     │
│                   Header-Name: Header-Wert                     │
│                   ...                                          │
│  ─────────────────────────────────────────────────────────    │
│  Leerzeile:       (trennt Header vom Body)                    │
│  ─────────────────────────────────────────────────────────    │
│  Body:            (optional, z.B. bei POST)                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Beispiel:

GET /search?q=test HTTP/1.1
Host: www.google.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Accept-Language: de-DE,de;q=0.9,en;q=0.8
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

```

### HTTP-Methoden

| Methode | Beschreibung | Body | Idempotent | Safe |
|---------|--------------|------|------------|------|
| **GET** | Ressource abrufen | Nein | Ja | Ja |
| **POST** | Daten senden/erstellen | Ja | Nein | Nein |
| **PUT** | Ressource ersetzen | Ja | Ja | Nein |
| **PATCH** | Ressource teilweise ändern | Ja | Nein | Nein |
| **DELETE** | Ressource löschen | Optional | Ja | Nein |
| **HEAD** | Nur Header (wie GET) | Nein | Ja | Ja |
| **OPTIONS** | Verfügbare Methoden | Optional | Ja | Ja |
| **CONNECT** | Tunnel aufbauen | Nein | Nein | Nein |
| **TRACE** | Echo der Anfrage | Nein | Ja | Ja |

> [!info] Idempotent vs. Safe
> - **Safe:** Ändert keine Serverdaten (GET, HEAD, OPTIONS)
> - **Idempotent:** Mehrfaches Ausführen hat gleichen Effekt wie einmaliges (GET, PUT, DELETE)

### Wichtige Request-Header

| Header | Beschreibung | Beispiel |
|--------|--------------|----------|
| **Host** | Ziel-Domain (Pflicht in HTTP/1.1) | Host: www.example.com |
| **User-Agent** | Client-Information | User-Agent: Mozilla/5.0... |
| **Accept** | Akzeptierte Medientypen | Accept: text/html |
| **Accept-Language** | Bevorzugte Sprachen | Accept-Language: de-DE |
| **Accept-Encoding** | Akzeptierte Kompression | Accept-Encoding: gzip |
| **Authorization** | Authentifizierung | Authorization: Bearer token |
| **Cookie** | Session-Cookies | Cookie: session=abc123 |
| **Content-Type** | Typ des Bodys | Content-Type: application/json |
| **Content-Length** | Größe des Bodys | Content-Length: 1234 |

## HTTP-Response

### Aufbau

```
HTTP/1.1 200 OK
Date: Mon, 13 Oct 2026 10:30:00 GMT
Server: Apache/2.4.52
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Cache-Control: max-age=3600
Connection: keep-alive

<!DOCTYPE html>
<html>
<head><title>Example</title></head>
<body>
  <h1>Hello World</h1>
</body>
</html>
```

### HTTP-Statuscodes

| Code | Kategorie | Beschreibung |
|------|-----------|--------------|
| **1xx** | Informational | Anfrage wird verarbeitet |
| **2xx** | Success | Anfrage erfolgreich |
| **3xx** | Redirection | Weiterleitung erforderlich |
| **4xx** | Client Error | Fehler auf Client-Seite |
| **5xx** | Server Error | Fehler auf Server-Seite |

### Wichtige Statuscodes

| Code | Name | Beschreibung |
|------|------|--------------|
| **200** | OK | Erfolgreich |
| **201** | Created | Ressource erstellt (POST) |
| **204** | No Content | Erfolgreich, kein Body |
| **301** | Moved Permanently | Permanente Weiterleitung |
| **302** | Found | Temporäre Weiterleitung |
| **304** | Not Modified | Cached Version nutzen |
| **400** | Bad Request | Ungültige Anfrage |
| **401** | Unauthorized | Authentifizierung erforderlich |
| **403** | Forbidden | Zugriff verweigert |
| **404** | Not Found | Ressource nicht gefunden |
| **405** | Method Not Allowed | Methode nicht erlaubt |
| **500** | Internal Server Error | Serverfehler |
| **502** | Bad Gateway | Upstream-Server-Fehler |
| **503** | Service Unavailable | Dienst nicht verfügbar |
| **504** | Gateway Timeout | Upstream-Timeout |

## HTTPS (HTTP Secure)

### TLS/SSL-Schicht

```
┌────────────────────────────────────────────────────────────────┐
│                    HTTPS = HTTP + TLS                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  HTTP (ohne TLS):                  HTTPS (mit TLS):           │
│                                                                │
│  ┌─────────────┐                   ┌─────────────┐            │
│  │    HTTP     │                   │    HTTP     │            │
│  ├─────────────┤                   ├─────────────┤            │
│  │    TCP      │                   │    TLS      │  ← NEU     │
│  ├─────────────┤                   ├─────────────┤            │
│  │    IP       │                   │    TCP      │            │
│  └─────────────┘                   ├─────────────┤            │
│                                    │    IP       │            │
│  Port 80                           └─────────────┘            │
│  Unverschlüsselt                   Port 443                   │
│                                    Verschlüsselt              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### TLS-Handshake (vereinfacht)

```
┌────────────────────────────────────────────────────────────────┐
│                      TLS-Handshake                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Client                                          Server        │
│     │                                               │          │
│     │  1. ClientHello                               │          │
│     │     (unterstützte Cipher Suites, Random)      │          │
│     │ ─────────────────────────────────────────────►│          │
│     │                                               │          │
│     │  2. ServerHello + Certificate                 │          │
│     │     (gewählte Cipher Suite, Server-Zertifikat)│          │
│     │ ◄─────────────────────────────────────────────│          │
│     │                                               │          │
│     │  3. Client verifiziert Zertifikat             │          │
│     │     (Zertifikatskette, CA-Vertrauen)          │          │
│     │                                               │          │
│     │  4. Key Exchange                              │          │
│     │     (Pre-Master Secret, verschlüsselt mit    │          │
│     │      Server Public Key)                       │          │
│     │ ─────────────────────────────────────────────►│          │
│     │                                               │          │
│     │  5. Beide Seiten berechnen Session Key        │          │
│     │                                               │          │
│     │  6. Finished (verschlüsselt)                  │          │
│     │ ◄────────────────────────────────────────────►│          │
│     │                                               │          │
│     │  ═══════ Verschlüsselte Kommunikation ═══════│          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Session-Management

### Cookies

```
┌────────────────────────────────────────────────────────────────┐
│                    HTTP Cookies                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. Server setzt Cookie:                                       │
│                                                                │
│     HTTP/1.1 200 OK                                           │
│     Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure  │
│     Set-Cookie: user=john; Expires=Wed, 13 Oct 2027 10:00:00 │
│                                                                │
│  2. Client sendet Cookie bei folgenden Requests:              │
│                                                                │
│     GET /dashboard HTTP/1.1                                   │
│     Cookie: session_id=abc123; user=john                      │
│                                                                │
│  Cookie-Attribute:                                             │
│  ┌────────────────┬────────────────────────────────────────┐  │
│  │ Expires/Max-Age│ Lebensdauer des Cookies                │  │
│  │ Path           │ Gültigkeitspfad                        │  │
│  │ Domain         │ Gültige Domain(s)                      │  │
│  │ Secure         │ Nur über HTTPS                         │  │
│  │ HttpOnly       │ Nicht per JavaScript zugreifbar        │  │
│  │ SameSite       │ CSRF-Schutz (Strict/Lax/None)          │  │
│  └────────────────┴────────────────────────────────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## REST (Representational State Transfer)

### REST-Prinzipien

REST ist ein Architekturstil für Web-APIs:

| Prinzip | Beschreibung |
|---------|--------------|
| **Client-Server** | Trennung von UI und Datenhaltung |
| **Zustandslos** | Jede Anfrage enthält alle nötigen Infos |
| **Cacheable** | Antworten können gecacht werden |
| **Einheitliche Schnittstelle** | Standardisierte Ressourcen-URLs |
| **Schichtenarchitektur** | Transparente Zwischenschichten möglich |

### REST-Beispiel

```
┌────────────────────────────────────────────────────────────────┐
│                    RESTful API Beispiel                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Ressource: Benutzer (/users)                                 │
│                                                                │
│  ┌────────────┬─────────────────┬──────────────────────────┐  │
│  │ Methode    │ URL             │ Aktion                   │  │
│  ├────────────┼─────────────────┼──────────────────────────┤  │
│  │ GET        │ /users          │ Alle Benutzer abrufen    │  │
│  │ GET        │ /users/42       │ Benutzer 42 abrufen      │  │
│  │ POST       │ /users          │ Neuen Benutzer erstellen │  │
│  │ PUT        │ /users/42       │ Benutzer 42 ersetzen     │  │
│  │ PATCH      │ /users/42       │ Benutzer 42 aktualisieren│  │
│  │ DELETE     │ /users/42       │ Benutzer 42 löschen      │  │
│  └────────────┴─────────────────┴──────────────────────────┘  │
│                                                                │
│  Beispiel POST:                                                │
│                                                                │
│  POST /users HTTP/1.1                                         │
│  Content-Type: application/json                               │
│                                                                │
│  {"name": "Max Mustermann", "email": "max@example.de"}        │
│                                                                │
│  Response:                                                     │
│  HTTP/1.1 201 Created                                         │
│  Location: /users/43                                          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
>
> **Häufige Prüfungsthemen:**
> 1. HTTP-Methoden (GET, POST, PUT, DELETE)
> 2. Wichtige Statuscodes (200, 301, 404, 500)
> 3. Request/Response-Aufbau
> 4. HTTP vs. HTTPS (TLS)
> 5. Cookies und Session-Management

### Merkregeln

> [!tip] Merkhilfe: Statuscodes
> - **2xx** = "Alles gut" (Success)
> - **3xx** = "Geh woanders hin" (Redirect)
> - **4xx** = "Du hast was falsch gemacht" (Client Error)
> - **5xx** = "Ich hab was verbockt" (Server Error)

## Zusammenhänge

- [[01-DNS]] - DNS-Auflösung vor HTTP-Verbindung
- [[07-Transportschicht/01-TCP|TCP]] - HTTP nutzt TCP
- [[07-Transportschicht/03-Ports|Ports]] - Port 80/443
- [[04-Sicherheit/00-Sicherheit-Index|Netzwerksicherheit]] - TLS/SSL, HTTPS

## Quellen

- [[A-RFC-Index|RFC 9110]] - HTTP Semantics
- [[A-RFC-Index|RFC 9111]] - HTTP Caching
- [[A-RFC-Index|RFC 9112]] - HTTP/1.1
- [[A-RFC-Index|RFC 9113]] - HTTP/2
- [[A-RFC-Index|RFC 9114]] - HTTP/3
