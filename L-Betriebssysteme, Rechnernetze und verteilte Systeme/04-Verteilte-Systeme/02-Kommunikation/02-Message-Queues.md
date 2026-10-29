---
author: Andreas Hümmer
title: Message Queues
tags:
  - content
  - vs
  - kommunikation
  - messaging
  - asynchron
  - middleware
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# Message Queues

> [!info] Lernziele
> - Konzept der asynchronen Kommunikation verstehen
> - Liefergarantien unterscheiden können
> - Vor- und Nachteile gegenüber synchroner Kommunikation kennen
> - Anwendungsfälle für Message Queues identifizieren

## Einleitung

Message Queues sind asynchrone Kommunikationsmechanismen, bei denen Nachrichten in einer Warteschlange zwischengespeichert werden. Sie bilden das Gegenstück zu synchronen Verfahren wie RPC.

> [!important] Kernkonzept
> Message Queues **entkoppeln** Sender und Empfänger sowohl **zeitlich** (der Empfänger muss nicht sofort verfügbar sein) als auch **räumlich** (Sender kennt den Empfänger nicht direkt). Die Warteschlange fungiert als Puffer und garantiert die Nachrichtenzustellung.

> [!example] Analogie
> Message Queues funktionieren wie ein Briefkasten: Du wirfst einen Brief ein (Nachricht senden) und gehst weiter, ohne auf eine Antwort zu warten. Der Empfänger holt den Brief ab, wenn er Zeit hat. Auch wenn der Empfänger gerade im Urlaub ist, geht der Brief nicht verloren – er wartet im Briefkasten.

## Kommunikationsmodelle

### Synchron vs. Asynchron

![[mq-synchron.png]]
*<span class="fig-id">04-02-02-mq-synchron</span>: Synchrone Kommunikation – Client blockiert während der Verarbeitung*

![[mq-asynchron.png]]
*<span class="fig-id">04-02-02-mq-asynchron</span>: Asynchrone Kommunikation – Producer arbeitet sofort weiter*

### Messaging-Pattern

| Pattern | Beschreibung |
|---------|--------------|
| **Point-to-Point** | Eine Nachricht wird von genau einem Consumer verarbeitet |
| **Publish/Subscribe** | Nachrichten werden an alle Subscriber verteilt |
| **Request/Reply** | Asynchrone Anfrage mit Antwort über separate Queue |
| **Fan-out** | Eine Nachricht an viele Consumer verteilen |

## Liefergarantien

| Garantie | Beschreibung | Trade-off |
|----------|--------------|-----------|
| **At-most-once** | Nachricht wird höchstens einmal zugestellt | Kann verloren gehen |
| **At-least-once** | Nachricht wird mindestens einmal zugestellt | Kann dupliziert werden |
| **Exactly-once** | Nachricht wird genau einmal zugestellt | Aufwändig zu implementieren |

### Exactly-once Semantik

Die Exactly-once-Garantie erfordert:
- Idempotente Consumer (mehrfache Verarbeitung hat gleichen Effekt)
- Transaktionale Verarbeitung
- Deduplizierung auf Basis von Message-IDs

---

## Dead Letter Queues (DLQ)

### Wohin mit fehlerhaften Nachrichten?
Nicht jede Nachricht kann erfolgreich verarbeitet werden. **Dead Letter Queues** sind spezielle Queues für Nachrichten, die nach mehreren Versuchen nicht verarbeitet werden konnten.

#### Gründe für DLQ

| Grund                    | Beispiel                                    |
| ------------------------ | ------------------------------------------- |
| **Poison Message**       | Nachricht verursacht immer einen Fehler     |
| **Schema-Mismatch**      | Nachricht passt nicht zum erwarteten Format |
| **Abhängigkeit fehlt**   | Referenzierte Ressource existiert nicht     |
| **TTL abgelaufen**       | Nachricht ist zu alt                        |
| **Max Retries erreicht** | Verarbeitung scheitert wiederholt           |

#### DLQ-Workflow

![[dlq-workflow.png]]
*<span class="fig-id">04-02-02-dlq-workflow</span>: Dead Letter Queue Workflow – Fehlerhafte Nachrichten werden nach mehreren Retries in die DLQ verschoben*

**Best Practices:**
- DLQ-Nachrichten mit Metadaten anreichern (Fehlergrund, Retry-Count)
- Alerting bei DLQ-Einträgen
- Regelmäßige manuelle Review der DLQ
- Möglichkeit zum Replay nach Bugfix

---

## Ordering-Garantien

### Das Ordering-Problem

In verteilten Queues ist die Reihenfolge nicht trivial:

```
Producer sendet: A, B, C
Consumer 1 empfängt: A, C
Consumer 2 empfängt: B

Globale Reihenfolge? Nicht garantiert!
```

### Lösungsansätze

| Strategie | Ordering | Throughput | Beispiel |
|-----------|----------|------------|----------|
| **Single Partition** | Strikt (FIFO) | Begrenzt | Eine Queue |
| **Partition Key** | Pro Key | Hoch | Kafka mit Customer-ID |
| **Sequence Numbers** | Rekonstruierbar | Hoch | Client sortiert |
| **Kein Ordering** | Keine Garantie | Maximal | SQS Standard |

### Kafka-Beispiel: Partition Key

```
Topic: orders (3 Partitionen)

Order für Customer A → Partition 0 (Hash von "A")
Order für Customer B → Partition 1 (Hash von "B")
Order für Customer A → Partition 0 (gleicher Hash!)

→ Alle Orders eines Customers sind geordnet
```

---

## Backpressure

**Was tun, wenn Consumer zu langsam?**
Wenn Producer schneller Nachrichten senden als Consumer verarbeiten können, füllt sich die Queue. **Backpressure** sind Mechanismen, um mit diesem Ungleichgewicht umzugehen.

### Strategien

| Strategie | Beschreibung | Trade-off |
|-----------|--------------|-----------|
| **Unbounded Queue** | Queue wächst unbegrenzt | Speicher-Explosion |
| **Bounded Queue + Drop** | Neue Nachrichten verwerfen | Datenverlust |
| **Bounded Queue + Block** | Producer blockiert | Producer wird langsamer |
| **Rate Limiting** | Producer drosseln | Kontrollierter Durchsatz |
| **Sampling** | Nur Stichproben verarbeiten | Für Metriken ok |

### Reactive Streams

Moderne Frameworks (Project Reactor, RxJava, Akka Streams) implementieren Backpressure:

```
Subscriber: "Ich kann 100 Nachrichten verarbeiten"
Publisher: Sendet 100 Nachrichten
Subscriber: "Ich bin fertig, gib mir 50 mehr"
Publisher: Sendet 50 Nachrichten
```

Der Consumer **zieht** (pull) statt der Producer **drückt** (push).

## Implementierungen

| System | Typ | Besonderheit |
|--------|-----|--------------|
| **Apache Kafka** | Event-Streaming | Hoher Durchsatz, Log-basiert |
| **RabbitMQ** | Message Broker | AMQP, flexible Routing |
| **Amazon SQS** | Cloud-Service | Managed, skalierbar |
| **Apache ActiveMQ** | Message Broker | JMS-kompatibel |
| **Redis Pub/Sub** | In-Memory | Sehr schnell, keine Persistenz |

## Vor- und Nachteile

### Vorteile

- **Entkopplung**: Sender und Empfänger unabhängig
- **Skalierbarkeit**: Consumer können horizontal skaliert werden
- **Fehlertoleranz**: Nachrichten überleben Ausfälle
- **Load Leveling**: Lastspitzen werden gepuffert
- **Asynchronität**: Sender blockiert nicht

### Nachteile

- **Komplexität**: Zusätzliche Infrastruktur erforderlich
- **Latenz**: Nachrichten müssen gepuffert werden
- **Monitoring**: Schwieriger zu debuggen
- **Konsistenz**: Eventual Consistency statt Strong Consistency

## Zusammenhänge

| Beziehung | Konzept | Beschreibung |
|-----------|---------|--------------|
| Alternative zu | [[01-RPC]] | Asynchron statt synchron |
| Ermöglicht | Microservices | Lose Kopplung zwischen Services |
| Nutzt | Asynchrone Verarbeitung | Fire-and-Forget Pattern |
| Unterstützt | Horizontale Skalierung | Mehrere Consumer parallel |
| Erfordert | Eventual Consistency | Keine sofortige Konsistenz |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> N/A – Dieses Thema ist nicht prüfungsrelevant, dient aber dem Verständnis asynchroner Kommunikationsmuster.

> [!question] **Häufige Prüfungsfragen**
> 1. Warum ist Exactly-once so schwer zu implementieren?
> 2. Was passiert, wenn die Queue voll ist?
> 3. Wie erreicht man Ordering in verteilten Queues?
> 4. Vergleichen Sie Message Queues mit RPC.

> [!tip] Merkhilfe
> **Message Queue = Asynchroner Briefkasten**:
> - **A**synchron: Sender wartet nicht
> - **P**ersistent: Nachrichten überleben
> - **E**ntkoppelt: Sender kennt Empfänger nicht
> - **S**kalierbar: Mehrere Consumer möglich

---

## Weiterführende Ressourcen

- [[01-RPC]] – Synchrone Alternative
- [[03-REST]] – HTTP-basierte Kommunikation
- [[03-Konsistenz/01-CAP-Theorem]] – Verteilte Konsistenz

---

## Quellen

- Kreps, J. (2011). *The Log: What every software engineer should know about real-time data's unifying abstraction*. LinkedIn Engineering Blog.
- Apache Kafka Documentation: https://kafka.apache.org/documentation/
- RabbitMQ Documentation: https://www.rabbitmq.com/documentation.html
- Hohpe, G., & Woolf, B. (2003). *Enterprise Integration Patterns*. Addison-Wesley.
