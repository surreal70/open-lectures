---
author: Andreas Hümmer
created: '2026-10-09'
modified: '2026-10-24'
tags:
  - content
  - index
  - vs
  - kommunikation
bereich: VS
---

# Kommunikation in Verteilten Systemen

Dieses Kapitel behandelt die grundlegenden Kommunikationsmechanismen in verteilten Systemen – von synchronen Fernaufrufen über asynchrone Messaging-Systeme bis hin zu Architekturkonzepten.

## Inhaltsverzeichnis

| Nr. | Thema | Beschreibung |
|-----|-------|--------------|
| 01 | [[01-RPC]] | Remote Procedure Call – synchrone Fernaufrufe |
| 02 | [[02-Message-Queues]] | Asynchrone Nachrichtenwarteschlangen |
| 03 | [[03-REST]] | Representational State Transfer – HTTP-basierte APIs |
| 04 | [[04-SOAP]] | Simple Object Access Protocol – XML-basierter Nachrichtenaustausch |
| 05 | [[05-SOA]] | Service-orientierte Architektur |
| 06 | [[06-gRPC]] | Google Remote Procedure Call – hochperformantes RPC-Framework |
| 07 | [[07-GraphQL]] | Flexible Query Language für APIs |
| 08 | [[08-WebSockets]] | Bidirektionale Echtzeit-Kommunikation |

## Übersicht der Kommunikationsparadigmen

| Paradigma | Technologien | Charakteristik |
|-----------|--------------|----------------|
| **Synchron (Request-Response)** | RPC, REST, SOAP, gRPC, GraphQL | Client wartet auf Antwort |
| **Asynchron (Message-Based)** | Message Queues | Fire-and-Forget, entkoppelt |
| **Bidirektional (Full-Duplex)** | WebSockets | Echtzeit, persistente Verbindung |
| **Architekturkonzept** | SOA | Übergeordnetes Designprinzip |

### Technologie-Einordnung

| Technologie | Protokoll | Datenformat | Typische Anwendung |
|-------------|-----------|-------------|-------------------|
| RPC | Proprietär | Binär/Text | Lokale Netzwerke, Legacy |
| REST | HTTP/HTTPS | JSON, XML | Web-APIs, CRUD-Operationen |
| SOAP | HTTP, SMTP | XML | Enterprise, WS-*-Standards |
| gRPC | HTTP/2 | Protocol Buffers | Microservices, Low-Latency |
| GraphQL | HTTP/HTTPS | JSON | Flexible Frontend-APIs |
| WebSockets | WS/WSS | Beliebig | Chat, Gaming, Live-Daten |
| Message Queues | AMQP, MQTT | Beliebig | Event-Driven, Entkopplung |

## Lernpfad

1. **Grundlagen**: Beginne mit [[01-RPC]] um das fundamentale Konzept von Fernaufrufen zu verstehen
2. **Synchron vs. Asynchron**: Vergleiche [[01-RPC]] mit [[02-Message-Queues]]
3. **Web-APIs klassisch**: Vertiefe mit [[03-REST]] und [[04-SOAP]]
4. **Moderne Alternativen**: Erkunde [[06-gRPC]] und [[07-GraphQL]] als moderne API-Ansätze
5. **Echtzeit**: Lerne [[08-WebSockets]] für bidirektionale Kommunikation
6. **Architektur**: Schließe mit [[05-SOA]] als übergeordnetem Konzept ab
