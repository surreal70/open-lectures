---
author: Andreas Hümmer
title: WebSockets und Echtzeit-Kommunikation
tags:
  - content
  - vs
  - kommunikation
  - websockets
  - echtzeit
  - bidirektional
created: '2026-10-29'
modified: '2026-10-24'
bereich: VS
---

# WebSockets und Echtzeit-Kommunikation

> [!info] Lernziele
> - WebSocket-Protokoll verstehen und von HTTP abgrenzen
> - Anwendungsfälle für Echtzeit-Kommunikation kennen
> - Fallback-Strategien (Long Polling, SSE) erklären können
> - Skalierungsherausforderungen bei WebSockets verstehen

---

## Einleitung

WebSockets ermöglichen **bidirektionale, persistente Verbindungen** zwischen Client und Server. Im Gegensatz zu HTTP, wo der Client immer die Kommunikation initiieren muss, können bei WebSockets beide Seiten jederzeit Nachrichten senden.

Das WebSocket-Protokoll wurde 2011 als RFC 6455 standardisiert und ist heute in allen modernen Browsern nativ verfügbar. Es entstand aus der Notwendigkeit, Echtzeit-Anwendungen im Web zu ermöglichen, ohne auf ineffiziente Workarounds wie Polling zurückgreifen zu müssen.

> [!important] Kernkonzept
> HTTP ist ein **Request/Response-Protokoll**: Der Client fragt, der Server antwortet. WebSockets sind ein **Full-Duplex-Protokoll**: Nach dem initialen Handshake können beide Seiten unabhängig voneinander Nachrichten senden – die Verbindung bleibt offen.

> [!example] Analogie
> HTTP ist wie SMS: Du schickst eine Nachricht und wartest auf Antwort. Jede Nachricht ist unabhängig. WebSockets sind wie ein Telefonat: Nach dem Verbindungsaufbau können beide Seiten jederzeit sprechen, ohne neu anrufen zu müssen.

### Historischer Kontext

| Jahr | Ereignis |
|------|----------|
| 2008 | Erste Diskussionen über ein bidirektionales Web-Protokoll |
| 2009 | Google Chrome implementiert experimentelle WebSocket-Unterstützung |
| 2011 | RFC 6455 standardisiert das WebSocket-Protokoll |
| 2013 | Alle großen Browser unterstützen WebSockets |
| Heute | Standard für Echtzeit-Web-Anwendungen |

---

## Das Problem mit HTTP

### Polling (klassisch)

```
Client: Gibt's was Neues? → Server: Nein
Client: Gibt's was Neues? → Server: Nein
Client: Gibt's was Neues? → Server: Nein
Client: Gibt's was Neues? → Server: Ja, hier!
```

**Problem:** Viele unnötige Requests, hohe Latenz, Server-Last.

### Long Polling

```
Client: Gibt's was Neues? → Server: (wartet...)
                          → Server: (wartet...)
                          → Server: Ja, hier!
Client: Gibt's was Neues? → Server: (wartet...)
```

**Besser:** Server hält die Verbindung offen, bis Daten vorliegen. Aber: Immer noch Request/Response-Overhead bei jedem Update.

### WebSockets

```
Client ←→ Server: Verbindung aufgebaut
Server → Client: Update 1
Server → Client: Update 2
Client → Server: Nachricht
Server → Client: Update 3
```

**Optimal:** Eine Verbindung, sofortige Updates in beide Richtungen.

---

## WebSocket-Handshake

WebSockets starten als HTTP-Request und werden dann "upgraded". Dieser Mechanismus wurde bewusst so gewählt, damit WebSockets durch bestehende HTTP-Infrastruktur (Proxies, Load Balancer) funktionieren.

### Ablauf des Handshakes

1. **Client sendet HTTP-Upgrade-Request** mit speziellen Headern
2. **Server prüft** die Anfrage und entscheidet, ob er WebSockets akzeptiert
3. **Server antwortet mit 101 Switching Protocols**
4. **Protokollwechsel**: Ab jetzt gilt das WebSocket-Protokoll (binär, Frame-basiert)

### Client Request

```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```

| Header | Bedeutung |
|--------|-----------|
| `Upgrade: websocket` | Signalisiert den Protokollwechsel |
| `Connection: Upgrade` | Bestätigt die Upgrade-Anfrage |
| `Sec-WebSocket-Key` | Zufälliger Base64-kodierter Wert zur Handshake-Validierung |
| `Sec-WebSocket-Version` | Protokollversion (aktuell: 13) |

### Server Response

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

Der `Sec-WebSocket-Accept`-Wert wird berechnet aus: `SHA-1(Sec-WebSocket-Key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11")`. Dieser Mechanismus verhindert, dass ein einfacher HTTP-Server versehentlich als WebSocket-Server fungiert.

Nach dem Handshake wechselt das Protokoll von HTTP zu WebSocket (ws:// oder wss://).

---

## WebSocket-Frames

Nach dem Handshake werden Daten in **Frames** übertragen. Ein Frame ist die kleinste Übertragungseinheit im WebSocket-Protokoll.

### Frame-Typen

| Opcode | Typ | Beschreibung |
|--------|-----|--------------|
| 0x0 | Continuation | Fortsetzung einer fragmentierten Nachricht |
| 0x1 | Text | UTF-8-kodierte Textnachricht |
| 0x2 | Binary | Binärdaten |
| 0x8 | Close | Verbindung schließen |
| 0x9 | Ping | Heartbeat-Anfrage |
| 0xA | Pong | Heartbeat-Antwort |

### Masking

Alle Frames vom Client zum Server müssen **maskiert** werden. Dies verhindert Cache-Poisoning-Angriffe auf Proxy-Server. Server-zu-Client-Frames sind nicht maskiert.

```
Client → Server: Maskiert (XOR mit 32-Bit-Key)
Server → Client: Unmaskiert
```

---

## Vergleich der Kommunikationsmuster

| Methode | Richtung | Latenz | Server-Last | Komplexität |
|---------|----------|--------|-------------|-------------|
| **Polling** | Client → Server | Hoch | Hoch | Niedrig |
| **Long Polling** | Client → Server | Mittel | Mittel | Mittel |
| **SSE** | Server → Client | Niedrig | Niedrig | Niedrig |
| **WebSockets** | Bidirektional | Sehr niedrig | Niedrig | Hoch |

### Server-Sent Events (SSE)

SSE ist eine einfachere Alternative für **unidirektionale** Server-zu-Client-Kommunikation:

```javascript
// Client
const eventSource = new EventSource('/updates');
eventSource.onmessage = (event) => {
  console.log(event.data);
};

// Server sendet
data: Erste Nachricht

data: Zweite Nachricht
```

**Vorteile:** Einfacher als WebSockets, automatische Reconnection, funktioniert mit HTTP/1.1.
**Nachteile:** Nur Server → Client, begrenzte Browser-Connections.

---

## Anwendungsfälle

### Ideal für WebSockets

| Anwendung | Warum WebSockets? |
|-----------|-------------------|
| **Chat-Anwendungen** | Bidirektional, Echtzeit |
| **Multiplayer-Spiele** | Niedrige Latenz, viele Updates |
| **Collaborative Editing** | Google Docs, Figma |
| **Live-Dashboards** | Trading, Monitoring |
| **Notifications** | Push ohne Polling |
| **IoT-Steuerung** | Bidirektionale Befehle |

### Weniger geeignet

- **Einfache Benachrichtigungen** → SSE reicht
- **Seltene Updates** → Long Polling günstiger
- **Request/Response-APIs** → REST/gRPC besser
- **Stateless-Anforderungen** → WebSockets sind stateful

---

## Skalierung

WebSockets stellen besondere Herausforderungen an die Skalierung. Im Gegensatz zu REST-APIs, die stateless sind und beliebig auf Server verteilt werden können, sind WebSocket-Verbindungen **stateful** – sie binden einen Client dauerhaft an einen bestimmten Server.

### Problem: Sticky Sessions

Bei horizontaler Skalierung entsteht ein fundamentales Problem: Jeder Client hat eine persistente Verbindung zu genau einem Server. Wenn zwei Clients auf verschiedenen Servern landen, können sie nicht direkt miteinander kommunizieren.

![[ws-sticky-sessions.png]]
*<span class="fig-id">04-02-08-ws-sticky-sessions</span>: Das Sticky-Sessions-Problem bei WebSocket-Skalierung – Clients auf verschiedenen Servern können nicht direkt kommunizieren.*

### Lösung: Pub/Sub-Backend

Die Standardlösung ist ein **Message Broker** als zentraler Koordinationspunkt. Alle WebSocket-Server subscriben auf denselben Channel und können so Nachrichten zwischen Clients auf verschiedenen Servern vermitteln.

![[ws-pubsub.png]]
*<span class="fig-id">04-02-08-ws-pubsub</span>: Pub/Sub-Backend als Lösung – alle Server kommunizieren über einen zentralen Message Broker.*

Gängige Message Broker für WebSocket-Skalierung:

| Broker | Eigenschaften | Anwendung |
|--------|---------------|-----------|
| **Redis Pub/Sub** | Einfach, In-Memory, niedrige Latenz | Kleine bis mittlere Anwendungen |
| **Redis Streams** | Persistenz, Consumer Groups | Wenn Nachrichten nicht verloren gehen dürfen |
| **Apache Kafka** | Hoher Durchsatz, Persistenz, Replay | Enterprise, Event Sourcing |
| **RabbitMQ** | Feature-reich, Routing | Komplexe Routing-Anforderungen |
| **NATS** | Ultra-niedrige Latenz, Cloud-native | Microservices, IoT |

### Connection Limits

Die Anzahl gleichzeitiger WebSocket-Verbindungen ist durch mehrere Faktoren begrenzt:

| Faktor | Typischer Wert | Beschreibung |
|--------|----------------|--------------|
| **RAM** | 10-50 KB/Verbindung | Puffer, Session-Daten |
| **File Descriptors** | 1024 (default) - 1M+ | OS-Limit, konfigurierbar |
| **CPU** | variabel | Nachrichtenverarbeitung |
| **Bandbreite** | variabel | Abhängig von Nachrichtengröße |

Ein moderner Server kann typischerweise **10.000-100.000** gleichzeitige WebSocket-Verbindungen halten. Mit spezialisierten Setups (z.B. Elixir/Phoenix, Go) sind auch Millionen Verbindungen pro Server möglich.

> [!note] C10K und C10M Problem
> Das **C10K-Problem** (10.000 concurrent connections) war in den 2000ern eine Herausforderung. Heute ist das **C10M-Problem** (10 Millionen) das neue Ziel für hochskalierte Systeme.

---

## Heartbeats und Reconnection

WebSocket-Verbindungen können aus verschiedenen Gründen "still sterben" – ohne dass eine Seite davon erfährt. Ursachen sind NAT-Timeouts, Firewall-Regeln oder Netzwerkprobleme.

### Heartbeat (Ping/Pong)

```
Client ──Ping──> Server
Client <──Pong── Server
```

Das WebSocket-Protokoll definiert native Ping/Pong-Frames (Opcodes 0x9 und 0xA):

| Aspekt | Beschreibung |
|--------|--------------|
| **Zweck** | Erkennung toter Verbindungen |
| **Initiator** | Üblicherweise Server |
| **Intervall** | Typisch 30-60 Sekunden |
| **Timeout** | Keine Pong-Antwort → Verbindung schließen |
| **NAT-Keepalive** | Verhindert, dass NAT-Tabellen die Verbindung vergessen |

> [!note] Application-Level Heartbeats
> Zusätzlich zu den Protokoll-Heartbeats implementieren viele Anwendungen eigene Heartbeats auf Anwendungsebene, um auch die Anwendungslogik zu überwachen.

### Reconnection-Strategie

Verbindungsabbrüche sind bei WebSockets unvermeidlich. Eine robuste Reconnection-Strategie ist daher essentiell.

```javascript
let reconnectDelay = 1000;
const maxDelay = 30000;

function connect() {
  const ws = new WebSocket('wss://example.com');
  
  ws.onopen = () => {
    reconnectDelay = 1000; // Reset bei Erfolg
  };
  
  ws.onclose = () => {
    setTimeout(connect, reconnectDelay);
    reconnectDelay = Math.min(reconnectDelay * 2, maxDelay);
  };
}
```

### Exponential Backoff

Das **Exponential Backoff**-Pattern ist kritisch für die Systemstabilität:

| Versuch | Wartezeit | Kumuliert |
|---------|-----------|-----------|
| 1 | 1s | 1s |
| 2 | 2s | 3s |
| 3 | 4s | 7s |
| 4 | 8s | 15s |
| 5 | 16s | 31s |
| 6+ | 30s (max) | - |

**Warum wichtig?** Ohne Backoff würden bei einem Server-Neustart alle Clients gleichzeitig reconnecten – das **Thundering Herd Problem**. Der Server wäre sofort wieder überlastet.

> [!tip] Best Practice: Jitter
> Zusätzlich zum Exponential Backoff sollte ein zufälliger **Jitter** (±20%) hinzugefügt werden, um Reconnection-Wellen weiter zu entzerren.

---

## Sicherheit

### Authentifizierung

WebSockets unterstützen keine HTTP-Header nach dem Handshake. Lösungen:

1. **Token in URL**: `wss://example.com/ws?token=xyz` (nicht ideal, Token im Log)
2. **Cookie-basiert**: Funktioniert mit Same-Origin
3. **Erste Nachricht**: Token als erste WebSocket-Nachricht senden

### Schutzmaßnahmen

- **Origin-Check**: Nur erlaubte Origins akzeptieren
- **Rate Limiting**: Nachrichten pro Sekunde begrenzen
- **Message Validation**: Eingehende Daten validieren
- **TLS (wss://)**: Verschlüsselung obligatorisch

---

## Praktische Implementierungen

| Plattform | Library/Framework |
|-----------|-------------------|
| **Browser** | Native WebSocket API |
| **Node.js** | ws, Socket.IO, µWebSockets |
| **Python** | websockets, Socket.IO |
| **Java** | Spring WebSocket, Tyrus |
| **Go** | gorilla/websocket, nhooyr/websocket |

### Socket.IO

Socket.IO ist eine beliebte Abstraktion über WebSockets:

- Automatische Fallbacks (Long Polling, SSE)
- Reconnection-Handling
- Rooms und Namespaces
- Broadcasting

```javascript
// Server
io.on('connection', (socket) => {
  socket.join('room1');
  socket.to('room1').emit('message', 'Hallo Room!');
});

// Client
socket.emit('message', 'Hallo Server!');
```

---

## Zusammenhänge

- [[03-REST]] → REST für Request/Response, WebSockets für Echtzeit
- [[07-GraphQL]] → GraphQL Subscriptions nutzen WebSockets
- [[02-Message-Queues]] → Backend für WebSocket-Skalierung
- [[06-gRPC]] → gRPC Streaming als Alternative

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] **Typische Prüfungsfragen**
> 1. Erklären Sie den Unterschied zwischen HTTP und WebSockets.
> 2. Was ist das Thundering Herd Problem und wie löst man es?
> 3. Warum sind WebSockets schwieriger zu skalieren als REST-APIs?

> [!tip] Merkhilfe
> **WebSocket = Offene Telefonleitung**
> - **W**echselseitig: Beide können senden
> - **S**chnell: Keine Request-Overhead
> - **S**tateful: Verbindung bleibt offen
> - Handshake über HTTP, dann Protokollwechsel

---

## Quellen

- RFC 6455 (2011). The WebSocket Protocol. IETF. https://tools.ietf.org/html/rfc6455
- W3C (2021). WebSocket API. https://websockets.spec.whatwg.org/
- Fette, I., & Melnikov, A. (2011). The WebSocket Protocol. IETF.
- MDN Web Docs. WebSockets API: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- Socket.IO Documentation - https://socket.io/docs/
