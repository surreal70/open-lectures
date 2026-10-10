---
author: Andreas Hümmer
title: Message-Queues
tags:
  - content
  - vs
  - kommunikation
  - messaging
  - asynchron
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---

# Message-Queues

## Definition

Message Queues sind asynchrone Kommunikationsmechanismen, bei denen Nachrichten in einer Warteschlange zwischengespeichert werden.

## Erklärung

Message Queues entkoppeln Sender und Empfänger zeitlich und räumlich. Der Sender muss nicht warten, bis der Empfänger verfügbar ist. Dies ermöglicht lose Kopplung, bessere Skalierbarkeit und Fehlertoleranz in verteilten Systemen.

## Eigenschaften

- Asynchrone Nachrichtenübertragung
- Persistente Speicherung möglich
- Entkopplung von Producer und Consumer
- Verschiedene Liefergarantien (at-least-once, at-most-once, exactly-once)
- Unterstützung für Pub/Sub-Muster

## Beispiele

- Apache Kafka für Event-Streaming
- RabbitMQ für Message Brokering
- Amazon SQS als Cloud-Service

## Zusammenhänge

- [[RPC]]
- [[REST]]
- [[Konsistenzmodelle]]

## Prüfungstipps

- Liefergarantien kennen und unterscheiden
- Vor- und Nachteile gegenüber RPC
- Anwendungsfälle für Message Queues

## Quellen

- *Quelle 1*
