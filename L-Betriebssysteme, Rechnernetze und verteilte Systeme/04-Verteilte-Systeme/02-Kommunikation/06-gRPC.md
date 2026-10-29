---
author: Andreas Hümmer
title: gRPC (Google Remote Procedure Call)
tags:
  - content
  - vs
  - kommunikation
  - grpc
  - protobuf
  - microservices
created: '2026-10-29'
modified: '2026-10-24'
bereich: VS
---

# gRPC (Google Remote Procedure Call)

> [!info] Lernziele
> - gRPC als modernes RPC-Framework verstehen
> - Protocol Buffers als Serialisierungsformat kennen
> - Streaming-Modi von gRPC erklären können
> - Unterschiede zu REST und klassischem RPC benennen

---

## Einleitung

gRPC ist ein von Google entwickeltes, quelloffenes RPC-Framework, das seit 2015 verfügbar ist. Es wurde für hochperformante Kommunikation zwischen Microservices entwickelt und ist heute in vielen Cloud-Native-Umgebungen Standard.

> [!important] Kernkonzept
> gRPC kombiniert **HTTP/2** als Transportprotokoll mit **Protocol Buffers** als Serialisierungsformat. Aus einer Schema-Definition (.proto-Datei) wird automatisch Client- und Server-Code in verschiedenen Programmiersprachen generiert – typsicher und effizient.

> [!example] Analogie
> gRPC ist wie ein Vertrag zwischen zwei Geschäftspartnern: Beide haben eine exakte Kopie des Vertrags (die .proto-Datei), die genau definiert, welche Anfragen möglich sind und wie die Antworten aussehen. Der Notar (protoc-Compiler) sorgt dafür, dass beide Seiten den Vertrag korrekt umsetzen.

---

## Protocol Buffers

### Was sind Protocol Buffers?

Protocol Buffers (Protobuf) sind ein sprachunabhängiges, plattformunabhängiges Serialisierungsformat. Sie sind **binär** (nicht menschenlesbar), dafür aber extrem kompakt und schnell zu verarbeiten.

### Beispiel einer .proto-Datei

```protobuf
syntax = "proto3";

package ecommerce;

// Service-Definition
service OrderService {
  rpc CreateOrder (OrderRequest) returns (OrderResponse);
  rpc GetOrder (OrderId) returns (Order);
  rpc ListOrders (ListRequest) returns (stream Order);
  rpc Chat (stream Message) returns (stream Message);
}

// Nachrichtentypen
message OrderRequest {
  string customer_id = 1;
  repeated Item items = 2;
}

message Item {
  string product_id = 1;
  int32 quantity = 2;
  double price = 3;
}

message OrderResponse {
  string order_id = 1;
  bool success = 2;
  string message = 3;
}
```

### Vorteile von Protocol Buffers

| Aspekt | Protocol Buffers | JSON |
|--------|------------------|------|
| **Größe** | 3-10x kleiner | Baseline |
| **Parsing** | 20-100x schneller | Baseline |
| **Schema** | Strikt definiert | Optional (JSON Schema) |
| **Typsicherheit** | Zur Compile-Zeit | Zur Laufzeit |
| **Lesbarkeit** | Binär (nicht lesbar) | Menschenlesbar |

Der Nachteil der fehlenden Lesbarkeit wird durch Tools wie `grpcurl` oder Debugging-Proxies ausgeglichen.

---

## HTTP/2-Vorteile

gRPC nutzt HTTP/2 und profitiert von dessen Features:

| Feature | Beschreibung | Vorteil für gRPC |
|---------|--------------|------------------|
| **Multiplexing** | Mehrere Streams über eine Verbindung | Weniger Verbindungsaufbau |
| **Header-Kompression** | HPACK-Algorithmus | Reduzierter Overhead |
| **Server Push** | Server kann proaktiv senden | Effizienteres Streaming |
| **Binäres Protokoll** | Nicht textbasiert | Schnelleres Parsing |
| **Stream Prioritization** | Wichtige Requests bevorzugen | Bessere Latenz |

---

## Streaming-Modi

gRPC unterstützt vier Kommunikationsmuster:

### 1. Unary RPC (Request/Response)

Klassisches Muster: Ein Request, eine Response.

```
Client ──Request──> Server
Client <──Response── Server
```

**Anwendung:** Einfache Abfragen, CRUD-Operationen

### 2. Server Streaming

Client sendet einen Request, Server antwortet mit einem Stream von Nachrichten.

```
Client ──Request──────────> Server
Client <──Response 1─────── Server
Client <──Response 2─────── Server
Client <──Response n─────── Server
```

**Anwendung:** Logs abrufen, Suchergebnisse streamen, Echtzeit-Updates

### 3. Client Streaming

Client sendet einen Stream von Nachrichten, Server antwortet einmal.

```
Client ──Request 1──> Server
Client ──Request 2──> Server
Client ──Request n──> Server
Client <──Response─── Server
```

**Anwendung:** Datei-Upload, Batch-Verarbeitung, Sensor-Daten sammeln

### 4. Bidirectional Streaming

Beide Seiten senden unabhängig voneinander Streams.

```
Client ──Request 1──> Server
Client <──Response 1── Server
Client ──Request 2──> Server
Client <──Response 2── Server
       ...
```

**Anwendung:** Chat, Multiplayer-Games, Echtzeit-Kollaboration

---

## gRPC vs. REST vs. GraphQL

| Aspekt | gRPC | REST | GraphQL |
|--------|------|------|---------|
| **Protokoll** | HTTP/2 | HTTP/1.1 oder 2 | HTTP |
| **Format** | Protocol Buffers | JSON/XML | JSON |
| **Schema** | .proto (required) | OpenAPI (optional) | Schema (required) |
| **Streaming** | Nativ (4 Modi) | Nicht nativ | Subscriptions |
| **Browser-Support** | Eingeschränkt | Vollständig | Vollständig |
| **Code-Generierung** | Automatisch | Manuell/Tools | Manuell/Tools |
| **Performance** | Sehr hoch | Mittel | Mittel |
| **Debugging** | Schwieriger (binär) | Einfach (lesbar) | Einfach (lesbar) |

### Wann welches Protokoll?

- **gRPC**: Microservices, hohe Performance, interne Kommunikation
- **REST**: Öffentliche APIs, Browser-Clients, einfache CRUD
- **GraphQL**: Flexible Abfragen, Mobile Apps mit variablem Datenbedarf

---

## Fehlerbehandlung

gRPC definiert standardisierte Status-Codes:

| Code | Name | Beschreibung |
|------|------|--------------|
| 0 | OK | Erfolgreich |
| 1 | CANCELLED | Operation abgebrochen |
| 2 | UNKNOWN | Unbekannter Fehler |
| 3 | INVALID_ARGUMENT | Ungültige Parameter |
| 4 | DEADLINE_EXCEEDED | Timeout |
| 5 | NOT_FOUND | Ressource nicht gefunden |
| 13 | INTERNAL | Interner Serverfehler |
| 14 | UNAVAILABLE | Service nicht erreichbar |

Diese Codes sind sprachunabhängig und ermöglichen einheitliche Fehlerbehandlung über verschiedene Services hinweg.

---

## Praktische Implementierungen

| Sprache | Client-Library | Server-Library |
|---------|----------------|----------------|
| **Go** | google.golang.org/grpc | google.golang.org/grpc |
| **Java** | io.grpc:grpc-stub | io.grpc:grpc-netty |
| **Python** | grpcio | grpcio |
| **Node.js** | @grpc/grpc-js | @grpc/grpc-js |
| **C#/.NET** | Grpc.Net.Client | Grpc.AspNetCore |

### Tools

- **protoc**: Protocol Buffer Compiler
- **grpcurl**: curl für gRPC (Debugging)
- **BloomRPC**: GUI-Client für gRPC
- **Evans**: Interaktiver gRPC-Client

---

## Zusammenhänge

- [[01-RPC]] → gRPC ist die moderne Evolution von RPC
- [[03-REST]] → Alternative für öffentliche APIs
- [[07-GraphQL]] → Alternative für flexible Abfragen
- [[02-Message-Queues]] → Für asynchrone Kommunikation

---

## Prüfungstipps

> [!warning] Prüfungsrelevant
NA

> [!question] **Typische Prüfungsfragen**
> 1. Vergleichen Sie gRPC und REST hinsichtlich Performance und Einsatzgebiete.
> 2. Erklären Sie den Unterschied zwischen Server Streaming und Bidirectional Streaming.
> 3. Warum ist gRPC für Microservices besonders geeignet?

> [!tip] Merkhilfe
> **gRPC = Schnell, Strikt, Streaming**
> - **S**chnell: Binäres Format, HTTP/2
> - **S**trikt: Schema-Definition erforderlich
> - **S**treaming: 4 Modi für jede Situation

---

## Quellen

- gRPC Official Documentation: https://grpc.io/docs/
- Google (2015). gRPC: A High Performance, Open Source Universal RPC Framework.
- Protocol Buffers Documentation: https://protobuf.dev/
- RFC 7540 (2015). Hypertext Transfer Protocol Version 2 (HTTP/2). IETF.
- Protocol Buffers Language Guide: https://developers.google.com/protocol-buffers
- Google Cloud: gRPC vs. REST - https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest
