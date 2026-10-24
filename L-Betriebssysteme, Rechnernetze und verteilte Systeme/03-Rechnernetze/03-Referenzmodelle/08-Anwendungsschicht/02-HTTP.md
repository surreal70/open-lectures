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
modified: '2026-10-24'
bereich: RN
---

# HTTP - Hypertext Transfer Protocol

## Definition

> [!quote] Definition
> Das **Hypertext Transfer Protocol (HTTP)** ist das Anwendungsprotokoll für die Übertragung von Webinhalten zwischen Clients (Browsern) und Servern im World Wide Web.
## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Zustandslos** | Jede Anfrage ist unabhängig (kein Session-State) |
| **Request-Response** | Client fragt an, Server antwortet |
| **Textbasiert** | Menschenlesbare Header (bis HTTP/2) |
| **Erweiterbar** | Neue Header und Methoden möglich |
| **Port** | TCP 80 (HTTP), TCP 443 (HTTPS) |

## HTTP-Versionen

![[http-timeline.png]]
*<span class="fig-id">03-08-02-http-timeline</span>: Entwicklung des HTTP-Protokolls von 1991 bis 2022*

### HTTP/0.9 (1991)
Die erste Version von Tim Berners-Lee war extrem einfach: Nur die GET-Methode, keine Header, nur HTML-Dokumente. Eine Anfrage bestand aus einer einzigen Zeile (`GET /page.html`), die Antwort war reiner HTML-Text.

### HTTP/1.0 (1996)
Mit der Standardisierung kamen Header, verschiedene Methoden (GET, POST, HEAD), Statuscodes und MIME-Types. **Problem:** Jede Anfrage erforderte eine neue TCP-Verbindung – bei Seiten mit vielen Bildern sehr ineffizient.

### HTTP/1.1 (1997)
Die bis heute am weitesten verbreitete Version löste das Verbindungsproblem:
- **Persistent Connections (Keep-Alive):** Eine TCP-Verbindung für mehrere Requests
- **Pipelining:** Mehrere Requests senden ohne auf Antwort zu warten
- **Host-Header:** Pflicht – ermöglicht Virtual Hosting (mehrere Domains auf einer IP)
- **Chunked Transfer:** Streaming von Daten unbekannter Größe

### HTTP/2 (2015)
Ein grundlegender Umbau zur Performanceverbesserung:
- **Binäres Protokoll:** Nicht mehr textbasiert, effizienter zu parsen
- **Multiplexing:** Mehrere Streams parallel über eine Verbindung (löst Head-of-Line-Blocking auf Anwendungsebene)
- **Header-Kompression (HPACK):** Reduziert redundante Header drastisch
- **Server Push:** Server kann Ressourcen proaktiv senden

> [!info] Warum binär?
> Textbasierte Protokolle sind menschenlesbar, aber ineffizient. HTTP/2 optimiert für Maschinen – Browser-DevTools zeigen die Daten trotzdem lesbar an.

### HTTP/3 (2022)
Der radikalste Wechsel: Statt TCP wird **QUIC über UDP** verwendet:
- **0-RTT Connection Setup:** Bei bekannten Servern kann sofort gesendet werden
- **Kein Head-of-Line-Blocking:** Paketverlust in einem Stream blockiert andere nicht
- **Verbindungsmigration:** Wechsel zwischen WLAN und Mobilfunk ohne Verbindungsabbruch

> [!warning] TCP vs. QUIC
> TCP hat Head-of-Line-Blocking auf Transportebene: Ein verlorenes Paket blockiert alle nachfolgenden. QUIC löst dies durch unabhängige Streams auf UDP-Basis.

## HTTP-Kommunikation

### Request-Response-Zyklus

![[http-request-response.png]]
*<span class="fig-id">03-08-02-http-request-response</span>: HTTP Request-Response-Zyklus von DNS bis zur Antwort*

## HTTP-Request

### Aufbau

Ein HTTP-Request besteht aus vier Teilen:

| Teil             | Beschreibung                        | Beispiel                   |
| ---------------- | ----------------------------------- | -------------------------- |
| **Request-Line** | Methode, Pfad, HTTP-Version         | `GET /index.html HTTP/1.1` |
| **Header**       | Key-Value-Paare mit Metadaten       | `Host: www.example.com`    |
| **Body**         | Nutzdaten (optional, z.B. bei POST) | `{"name": "Max"}`          |

> [!example] Beispiel: HTTP GET Request
> ```http
> GET /search?q=test HTTP/1.1
> Host: www.google.com
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
> Accept: text/html,application/xhtml+xml
> Accept-Language: de-DE,de;q=0.9,en;q=0.8
> Accept-Encoding: gzip, deflate, br
> Connection: keep-alive
> ```
> *kein Body bei GET*

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

![[https-stack-comparison.png]]
*<span class="fig-id">03-08-02-https-stack-comparison</span>: HTTPS fügt eine TLS-Verschlüsselungsschicht zwischen HTTP und TCP ein*

### TLS-Handshake (vereinfacht)

![[tls-handshake.png]]
*<span class="fig-id">03-08-02-tls-handshake</span>: TLS-Handshake – Schlüsselaustausch vor der verschlüsselten Kommunikation*

## Session-Management

### Cookies

HTTP ist zustandslos – Cookies ermöglichen Session-Management durch kleine Datenpakete, die der Server beim Client speichert.

#### Cookie-Ablauf

1. **Server setzt Cookie** (Response-Header):
   ```http
   Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure
   Set-Cookie: user=john; Expires=Wed, 13 Oct 2027 10:00:00 GMT
   ```

2. **Client sendet Cookie** (bei folgenden Requests):
   ```http
   GET /dashboard HTTP/1.1
   Cookie: session_id=abc123; user=john
   ```

#### Cookie-Attribute

| Attribut | Beschreibung |
|----------|--------------|
| **Expires / Max-Age** | Lebensdauer des Cookies (ohne: Session-Cookie) |
| **Path** | Gültigkeitspfad (z.B. `/admin`) |
| **Domain** | Gültige Domain(s) inkl. Subdomains |
| **Secure** | Nur über HTTPS übertragen |
| **HttpOnly** | Nicht per JavaScript zugreifbar (XSS-Schutz) |
| **SameSite** | CSRF-Schutz: `Strict`, `Lax`, oder `None` |

> [!warning] Sicherheitsattribute
> - **HttpOnly** verhindert, dass Angreifer per XSS (Cross-Site Scripting) Session-Cookies stehlen können
> - **Secure** stellt sicher, dass Cookies nicht über unverschlüsselte Verbindungen abgefangen werden
> - **SameSite=Strict** blockiert das Cookie bei Cross-Site-Requests (stärkster CSRF-Schutz)

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

### REST-Beispiel: Benutzer-API

Eine typische RESTful API für Benutzer (`/users`):

| Methode | URL | Aktion |
|---------|-----|--------|
| **GET** | `/users` | Alle Benutzer abrufen |
| **GET** | `/users/42` | Benutzer 42 abrufen |
| **POST** | `/users` | Neuen Benutzer erstellen |
| **PUT** | `/users/42` | Benutzer 42 komplett ersetzen |
| **PATCH** | `/users/42` | Benutzer 42 teilweise aktualisieren |
| **DELETE** | `/users/42` | Benutzer 42 löschen |

> [!example] POST-Request mit Response
> **Request:**
> ```http
> POST /users HTTP/1.1
> Host: api.example.com
> Content-Type: application/json
> 
> {"name": "Max Mustermann", "email": "max@example.de"}
> ```
> 
> **Response:**
> ```http
> HTTP/1.1 201 Created
> Location: /users/43
> Content-Type: application/json
> 
> {"id": 43, "name": "Max Mustermann", "email": "max@example.de"}
> ```

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - HTTP-Methoden (GET, POST, PUT, DELETE)
> - Wichtige Statuscodes (200, 301, 404, 500)
> - Request/Response-Aufbau
> - HTTP vs. HTTPS (TLS)
> - Cookies und Session-Management

> [!question] Typische Prüfungsfragen
> - Erklären Sie den Unterschied zwischen GET und POST.
> - Was bedeuten die HTTP-Statuscodes 200, 301, 404 und 500?
> - Wie ist eine HTTP-Anfrage aufgebaut?
> - Was ist der Unterschied zwischen HTTP und HTTPS?
> - Wie funktioniert Session-Management mit Cookies?

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
