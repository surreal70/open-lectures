---
author: Andreas Hümmer
title: REST (Representational State Transfer)
tags:
  - content
  - vs
  - kommunikation
  - rest
  - http
  - api
  - webservices
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# REST (Representational State Transfer)

> [!info] Lernziele
> - REST als Architekturstil verstehen
> - HTTP-Methoden und ihre Semantik kennen
> - Unterschiede zwischen REST und SOAP erklären können
> - REST-Prinzipien nach Fielding benennen

## Einleitung

REST ist ein Architekturstil für verteilte Hypermedia-Systeme, der 2000 von Roy Fielding in seiner Dissertation beschrieben wurde. Er nutzt das HTTP-Protokoll und dessen Methoden für die Kommunikation zwischen Client und Server.

> [!important] Kernkonzept
> REST basiert auf dem Konzept von **Ressourcen**, die über eindeutige URIs identifiziert werden. Der Zustand einer Ressource wird als **Repräsentation** (z.B. JSON, XML) übertragen. Jede Anfrage ist **zustandslos** und enthält alle notwendigen Informationen.

> [!example] Analogie
> REST funktioniert wie eine Bibliothek: Jedes Buch (Ressource) hat eine eindeutige Signatur (URI). Du kannst ein Buch ansehen (GET), ein neues hinzufügen (POST), eines ersetzen (PUT) oder entfernen (DELETE). Der Bibliothekar merkt sich nicht, was du vorher gemacht hast – jeder Besuch (Request) ist unabhängig.

## HTTP-Protokoll

### HTTP-Methoden (Primitiven)

| Methode | Beschreibung | Idempotent |
|---------|--------------|------------|
| **GET** | Liefert den Inhalt einer Ressource | ✓ |
| **HEAD** | Wie GET, aber nur Metadaten (Header) | ✓ |
| **POST** | Sendet Daten zur Verarbeitung an den Server | ✗ |
| **PUT** | Speichert/ersetzt eine Ressource unter der URI | ✓ |
| **DELETE** | Löscht die angegebene Ressource | ✓ |
| **PATCH** | Partielle Aktualisierung einer Ressource | ✗ |
| **OPTIONS** | Liefert unterstützte Methoden für eine URI | ✓ |
| **TRACE** | Gibt die empfangene Anfrage zurück (Debug) | ✓ |

### Request-Response-Zyklus

![[rest-request-response.png]]
*<span class="fig-id">04-02-03-rest-request-response</span>: REST Request-Response-Zyklus mit HTTP-Methoden*

### Statischer vs. Dynamischer Inhalt

GET-Requests können referenzieren auf:
- **Statische Webseiten**: Direkte Auslieferung von HTML/CSS/JS-Dateien
- **Dynamische Inhalte**: Ausführung eines Programms auf dem Server
  - Server Side Includes (SSI) für einfache Modifikationen
  - Query-Parameter (`?key=value`) für parametrisierte Aufrufe

## REST-Prinzipien (nach Fielding)

1. **Client-Server-Architektur**: Klare Trennung der Verantwortlichkeiten
2. **Zustandslosigkeit (Stateless)**: Jede Anfrage ist unabhängig
3. **Cachebarkeit**: Antworten können als cachebar markiert werden
4. **Einheitliche Schnittstelle (Uniform Interface)**: 
   - Ressourcen-Identifikation durch URIs
   - Manipulation durch Repräsentationen
   - Selbstbeschreibende Nachrichten
   - HATEOAS (Hypermedia as the Engine of Application State)
5. **Schichtensystem**: Zwischengeschaltete Schichten möglich (Proxies, Load Balancer)
6. **Code on Demand** (optional): Ausführbarer Code kann übertragen werden

### HATEOAS im Detail

> [!important] Oft vernachlässigt, aber zentral für REST
> **HATEOAS** bedeutet: Die API-Antwort enthält Links zu möglichen nächsten Aktionen. Der Client muss keine URLs hardcoden – er "entdeckt" die API.

HATEOAS ist das am häufigsten missverstandene und vernachlässigte REST-Prinzip. Viele sogenannte "REST-APIs" sind eigentlich nur HTTP-APIs, weil sie HATEOAS nicht implementieren. Roy Fielding selbst hat kritisiert, dass APIs ohne Hypermedia-Kontrollen nicht als REST bezeichnet werden sollten.

**Ohne HATEOAS:**
```json
{
  "order_id": 123,
  "status": "pending",
  "total": 99.99
}
```
Client muss wissen: "Um zu bezahlen, rufe ich `/orders/123/pay` auf."

**Mit HATEOAS:**
```json
{
  "order_id": 123,
  "status": "pending",
  "total": 99.99,
  "_links": {
    "self": { "href": "/orders/123" },
    "pay": { "href": "/orders/123/pay", "method": "POST" },
    "cancel": { "href": "/orders/123", "method": "DELETE" }
  }
}
```
Client folgt den Links – wie ein Browser, der Links auf einer Webseite folgt.

### Richardson Maturity Model

Leonard Richardson definierte ein Reifegradmodell für REST-APIs:

| Level | Name | Beschreibung | Beispiel |
|-------|------|--------------|----------|
| **0** | The Swamp of POX | Ein Endpunkt, alles über POST | SOAP-ähnlich |
| **1** | Resources | Individuelle URIs für Ressourcen | `/orders/123` |
| **2** | HTTP Verbs | Korrekte HTTP-Methoden | GET, POST, PUT, DELETE |
| **3** | Hypermedia Controls | HATEOAS – Links in Antworten | `_links`, `_embedded` |

> [!tip] Praxisrealität
> Die meisten "REST-APIs" erreichen Level 2. Level 3 (echtes REST) ist selten, weil der Implementierungsaufwand hoch ist und viele Clients die Hypermedia-Links nicht nutzen.

### Standardformate für Hypermedia

| Format | Beschreibung | Verwendung |
|--------|--------------|------------|
| **HAL** (Hypertext Application Language) | JSON mit `_links` und `_embedded` | Weit verbreitet |
| **JSON-LD** | Linked Data für JSON | Semantic Web |
| **Collection+JSON** | Spezialisiert auf Collections | CRUD-APIs |
| **Siren** | Entities mit Actions | Komplexe Workflows |

**HAL-Beispiel:**
```json
{
  "_links": {
    "self": { "href": "/orders/123" },
    "customer": { "href": "/customers/456" }
  },
  "_embedded": {
    "items": [
      { "product": "Widget", "quantity": 2 }
    ]
  },
  "total": 99.99
}
```

---

## Content Negotiation

REST erlaubt verschiedene Repräsentationen derselben Ressource. Der Client teilt über den `Accept`-Header mit, welches Format er bevorzugt:

```http
GET /users/123 HTTP/1.1
Accept: application/json
```

```http
GET /users/123 HTTP/1.1
Accept: application/xml
```

Der Server antwortet mit dem `Content-Type`-Header:

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```

| Header | Richtung | Zweck |
|--------|----------|-------|
| `Accept` | Request | Gewünschtes Format |
| `Content-Type` | Response/Request | Tatsächliches Format |
| `Accept-Language` | Request | Sprachpräferenz |
| `Accept-Encoding` | Request | Kompression (gzip, br) |

---

## Fehlerbehandlung

RESTful APIs sollten HTTP-Statuscodes konsistent verwenden:

### Erfolg (2xx)

| Code | Name | Verwendung |
|------|------|------------|
| 200 | OK | Erfolgreiche GET, PUT, PATCH |
| 201 | Created | Ressource erstellt (POST) |
| 204 | No Content | Erfolg ohne Body (DELETE) |

### Client-Fehler (4xx)

| Code | Name | Verwendung |
|------|------|------------|
| 400 | Bad Request | Ungültige Anfrage |
| 401 | Unauthorized | Authentifizierung erforderlich |
| 403 | Forbidden | Keine Berechtigung |
| 404 | Not Found | Ressource existiert nicht |
| 409 | Conflict | Konflikt (z.B. Duplikat) |
| 422 | Unprocessable Entity | Validierungsfehler |

### Server-Fehler (5xx)

| Code | Name | Verwendung |
|------|------|------------|
| 500 | Internal Server Error | Unerwarteter Fehler |
| 502 | Bad Gateway | Upstream-Server-Fehler |
| 503 | Service Unavailable | Überlastet/Wartung |

**Best Practice – Strukturierte Fehlerantworten:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email address is invalid",
    "details": [
      { "field": "email", "issue": "Invalid format" }
    ]
  }
}
```

---

## API-Versionierung

APIs entwickeln sich weiter, aber bestehende Clients dürfen nicht brechen. Strategien:

| Strategie | Beispiel | Vorteile | Nachteile |
|-----------|----------|----------|-----------|
| **URL-Path** | `/v1/users`, `/v2/users` | Explizit, einfach | URL-Pollution |
| **Query-Parameter** | `/users?version=2` | Flexibel | Leicht zu übersehen |
| **Header** | `Accept: application/vnd.api.v2+json` | Saubere URLs | Schwerer zu testen |
| **Content Negotiation** | `Accept: application/json;version=2` | Standard-konform | Komplex |

**Best Practice:** URL-Path für Major Versions (`/v1`, `/v2`), Breaking Changes vermeiden durch additive Änderungen.

---

## Pagination

Bei großen Datenmengen muss paginiert werden:

### Offset-basiert

```
GET /users?offset=20&limit=10
```

| Vorteil | Nachteil |
|---------|----------|
| Einfach zu verstehen | Performance bei großem Offset |
| Wahlfreier Zugriff | Inkonsistent bei Änderungen |

### Cursor-basiert

```
GET /users?cursor=eyJpZCI6MTIzfQ&limit=10
```

| Vorteil | Nachteil |
|---------|----------|
| Konsistent bei Änderungen | Kein wahlfreier Zugriff |
| Performant | Komplexere Implementierung |

Der Cursor ist typischerweise ein Base64-kodierter Wert (z.B. letzte ID).

---

## Rate Limiting

APIs müssen sich vor Überlastung schützen:

### HTTP-Status und Header

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1699520400
```

### Algorithmen

| Algorithmus | Beschreibung |
|-------------|--------------|
| **Fixed Window** | N Requests pro Minute |
| **Sliding Window** | N Requests in den letzten 60 Sekunden |
| **Token Bucket** | Tokens werden kontinuierlich aufgefüllt |
| **Leaky Bucket** | Requests werden mit konstanter Rate verarbeitet |

**Best Practice:** Rate Limits in Response-Headern kommunizieren, damit Clients sich anpassen können.

## REST vs. SOAP

| Aspekt | REST | SOAP |
|--------|------|------|
| **Typ** | Architekturstil | Protokoll |
| **Ressourcen** | Leichtgewichtig | Ressourcenintensiv |
| **Bandbreite** | Geringer Overhead | XML-Overhead |
| **Kopplung** | Lose Kopplung | Engere Bindung |
| **Caching** | Unterstützt | Nicht direkt |
| **Sicherheit** | HTTPS, OAuth | WS-Security (gilt als sicherer) |

> [!tip] Entscheidungshilfe
> - **REST**: Öffentliche APIs, Mobile Apps, Microservices
> - **SOAP**: Enterprise-Anwendungen mit hohen Sicherheitsanforderungen

## Zusammenhänge

| Beziehung | Konzept | Beschreibung |
|-----------|---------|--------------|
| Nutzt | HTTP-Protokoll | GET, POST, PUT, DELETE |
| Alternative zu | [[04-SOAP]] | Leichtgewichtiger Ansatz |
| Basiert auf | [[01-RPC]]-Konzept | Request-Response-Muster |
| Architektur für | Microservices | Lose gekoppelte APIs |
| Transportiert | JSON/XML | Repräsentationen |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - HTTP-Methoden und ihre Semantik (GET, POST, PUT, DELETE, PATCH)
> - REST-Prinzipien: Ressourcenorientierung, Zustandslosigkeit, einheitliche Schnittstelle
> - Vergleich REST vs. SOAP
> - Idempotenz bei HTTP-Methoden

> [!question] **Häufige Prüfungsfragen**
> 1. Erklären Sie die HTTP-Methoden und ihre Semantik.
> 2. Vergleichen Sie REST und SOAP.
> 3. Was bedeutet "zustandslos" und warum ist das wichtig?
> 4. Was ist der Unterschied zwischen PUT und POST?
> 5. Warum ist REST leichtgewichtiger als SOAP?

> [!tip] Merkhilfe
> **REST = Ressourcen über HTTP**: 
> - **R**essourcen haben **U**RIs
> - **E**inheitliche Schnittstelle (HTTP-Methoden)
> - **S**tateless (zustandslos)
> - **T**ransfer von Repräsentationen

---

## Weiterführende Ressourcen

- [[01-RPC]] – Grundlegendes RPC-Konzept
- [[02-Message-Queues]] – Asynchrone Alternative
- [[04-SOAP]] – XML-basiertes Protokoll

---

## Quellen

- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine.
- RFC 7230–7235 (2014). HTTP/1.1 Specification. IETF.
- RFC 9110 (2022). HTTP Semantics. IETF.
- Richardson, L., Amundsen, M., & Ruby, S. (2013). *RESTful Web APIs*. O'Reilly Media.
- Kelly, M. (2012). HAL - Hypertext Application Language Specification.
