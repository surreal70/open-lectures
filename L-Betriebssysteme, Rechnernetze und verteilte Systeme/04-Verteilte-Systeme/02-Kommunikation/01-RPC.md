---
author: Andreas Hümmer
title: Remote Procedure Call (RPC)
tags:
  - content
  - vs
  - kommunikation
  - rpc
  - middleware
  - client-server
created: '2026-10-07'
modified: '2026-10-24'
bereich: VS
---

# Remote Procedure Call (RPC)

> [!info] Lernziele
> - Funktionsprinzip von RPC verstehen
> - Ablauf eines RPC-Aufrufs erklären können
> - Unterschied zwischen blockierenden und nicht-blockierenden Aufrufen kennen
> - Praktische Implementierungen benennen können

## Einleitung

Remote Procedure Call (RPC) ist ein fundamentales Kommunikationsparadigma in verteilten Systemen. Es ermöglicht einem Programm, eine Prozedur auf einem entfernten Rechner so aufzurufen, als wäre es ein lokaler Funktionsaufruf.

> [!important] Kernkonzept
> RPC ist eine Generalisierung von Fernaufrufen. Ein Client schickt eine Nachricht (ggf. zusammen mit Parametern) an einen Server, woraufhin der Server ein Programm startet und die Ausgaben dieses Programms an den Client zurückliefert.

> [!example] Analogie
> RPC funktioniert wie ein Telefonanruf bei einem Dienstleister: Du rufst an (Request), nennst dein Anliegen und Parameter (z.B. "Ich möchte eine Pizza Margherita"), der Dienstleister führt die Arbeit aus (Prozedur) und teilt dir das Ergebnis mit (Response). Während du wartest, kannst du nichts anderes tun – der Anruf blockiert.

## Funktionsprinzip

### Grundlegender Ablauf

1. **Client-Aufruf**: Der Client ruft eine lokale Stub-Funktion auf
2. **Marshalling**: Parameter werden serialisiert (in Netzwerkformat umgewandelt)
3. **Übertragung**: Request wird über das Netzwerk zum Server gesendet
4. **Server-Stub**: Empfängt die Nachricht und deserialisiert die Parameter
5. **Ausführung**: Die eigentliche Prozedur wird auf dem Server ausgeführt
6. **Rückgabe**: Ergebnis wird serialisiert und an den Client zurückgesendet
7. **Client empfängt**: Der Client-Stub deserialisiert das Ergebnis

![[rpc-ablauf.png]]
*<span class="fig-id">04-02-01-rpc-ablauf</span>: Ablauf eines RPC-Aufrufs – Request (durchgezogen) und Response (gestrichelt)*

### Blockierendes Verhalten

> [!warning] Achtung
> RPC-Aufrufe sind typischerweise **blockierend**! Der Client wartet auf die Antwort des Servers und kann währenddessen keine anderen Operationen ausführen.

## Implementierungen

| Implementierung | Beschreibung | Protokoll |
|-----------------|--------------|-----------|
| **HTTP GET/POST** | Einfachste Form von RPC | HTTP |
| **Java RMI** | Remote Method Invocation für Java | JRMP/IIOP |
| **gRPC** | Modernes Framework von Google | HTTP/2 + Protocol Buffers |
| **XML-RPC** | XML-basierte Kodierung | HTTP |
| **JSON-RPC** | JSON-basierte Kodierung | HTTP |
| **SAP RFC** | Remote Function Call in SAP | Proprietär |

### Portmapper und Service Discovery

Ein zentrales Problem bei RPC: Wie findet der Client den Port, auf dem ein bestimmter Dienst läuft? RPC-Dienste verwenden oft dynamisch zugewiesene Ports, die sich bei jedem Neustart ändern können.

> [!info] Portmapper-Konzept
> Der **Portmapper** (auch *rpcbind* genannt) ist ein Verzeichnisdienst, der auf einem festen, bekannten Port läuft und die Zuordnung von RPC-Programmnummern zu dynamischen Ports verwaltet.

**Ablauf der Service-Registrierung und -Abfrage:**

| Schritt | Aktion | Beschreibung |
|---------|--------|--------------|
| 1 | Server startet | RPC-Server bindet sich an einen freien Port (z.B. 54321) |
| 2 | Registrierung | Server meldet sich beim Portmapper: "Programm 100003 (NFS) läuft auf Port 54321" |
| 3 | Client-Anfrage | Client fragt Portmapper: "Auf welchem Port läuft Programm 100003?" |
| 4 | Antwort | Portmapper antwortet: "Port 54321" |
| 5 | Direktverbindung | Client verbindet sich direkt zum RPC-Server auf Port 54321 |

> [!example] Analogie
> Der Portmapper funktioniert wie die Telefonzentrale eines Unternehmens: Du rufst die Hauptnummer an (Port 111) und fragst nach der Durchwahl für die Buchhaltung (Programmnummer). Die Zentrale nennt dir die Durchwahl (dynamischer Port), und ab dann rufst du direkt dort an.

**Bekannte Ports:**

| System | Port | Dienst |
|--------|------|--------|
| Unix/Linux | 111/tcp, 111/udp | Portmapper (rpcbind) |
| Windows | 135/tcp | RPC Endpoint Mapper |

**Sicherheitshinweis:**

> [!warning] Portmapper als Angriffsvektor
> Der Portmapper verrät, welche RPC-Dienste auf einem System laufen – wertvolle Information für Angreifer. Deshalb:
> - Port 111 und 135 sollten durch Firewalls geschützt sein
> - Moderne Systeme beschränken Portmapper-Anfragen auf localhost oder vertrauenswürdige Netze
> - Tools wie `rpcinfo -p <host>` können zur Enumeration missbraucht werden

**Praktische Befehle (Linux):**

```bash
# Alle registrierten RPC-Dienste anzeigen
rpcinfo -p localhost

# Beispielausgabe:
#    program vers proto   port  service
#    100000    4   tcp    111  portmapper
#    100003    3   tcp   2049  nfs
#    100005    3   tcp  20048  mountd
```

---

## Fehlerbehandlung und Idempotenz

### Was kann schiefgehen?

Bei RPC-Aufrufen können verschiedene Fehler auftreten, die unterschiedlich behandelt werden müssen:

| Fehlertyp | Beschreibung | Problem |
|-----------|--------------|---------|
| **Request verloren** | Nachricht erreicht Server nie | Client wartet ewig |
| **Server-Absturz** | Server stürzt während Verarbeitung ab | Unklarer Zustand |
| **Response verloren** | Antwort erreicht Client nie | Client denkt, Request fehlgeschlagen |
| **Timeout** | Antwort kommt zu spät | War der Request erfolgreich? |

### Das Idempotenz-Problem

> [!warning] Kritisch bei Retries
> Wenn ein Client nach einem Timeout den Request wiederholt, kann es sein, dass der ursprüngliche Request doch verarbeitet wurde. Ohne **Idempotenz** führt das zu Problemen.

**Idempotent** bedeutet: Mehrfaches Ausführen hat denselben Effekt wie einmaliges Ausführen.

| Operation | Idempotent? | Beispiel |
|-----------|-------------|----------|
| Lesen | ✓ | `GET /user/123` |
| Absolutes Setzen | ✓ | `SET balance = 100` |
| Löschen | ✓ | `DELETE /user/123` |
| Inkrementieren | ✗ | `balance += 10` |
| Erstellen | ✗ | `POST /orders` |

**Lösung für nicht-idempotente Operationen:**
- **Request-IDs**: Server speichert verarbeitete Request-IDs und ignoriert Duplikate
- **Optimistic Locking**: Versionsnummer prüfen vor Änderung
- **Two-Phase Commit**: Erst reservieren, dann bestätigen

### Semantiken der Ausführung

| Semantik | Garantie | Implementierungsaufwand |
|----------|----------|-------------------------|
| **Maybe** | Request wird 0 oder 1 mal ausgeführt | Minimal |
| **At-least-once** | Request wird mindestens 1 mal ausgeführt | Mittel (Retries) |
| **At-most-once** | Request wird höchstens 1 mal ausgeführt | Mittel (Duplikat-Erkennung) |
| **Exactly-once** | Request wird genau 1 mal ausgeführt | Hoch (Transaktionen) |

## Zusammenhänge

| Beziehung | Konzept | Beschreibung |
|-----------|---------|--------------|
| Architekturstil | [[03-REST]] | REST baut auf RPC-Konzept auf |
| XML-basiert | [[04-SOAP]] | SOAP nutzt RPC über XML |
| Nutzt | HTTP | Transport über HTTP möglich |
| Alternative | [[02-Message-Queues]] | Asynchrone Alternative zu RPC |

---

## Prüfungstipps

> [!warning] Häufige Prüfungsfragen
> - Beschreiben Sie den Ablauf eines RPC-Aufrufs

> [!question] Verständnisfragen
> - Warum braucht man Marshalling/Unmarshalling?
> - Welche Probleme können bei RPC auftreten (Netzwerkfehler, Timeouts)?
> - Wie unterscheidet sich synchrones von asynchronem RPC?

> [!tip] Merkhilfe
> **RPC = Remote Procedure Call**: Der Client "ruft an", der Server "führt aus", das Ergebnis wird "zurückgerufen". Denke an einen Telefonanruf – während du wartest, ist die Leitung blockiert.

---

## Weiterführende Ressourcen

- [[REST]] – Vergleich mit ressourcenorientiertem Ansatz
- [[Message-Queues]] – Asynchrone Alternative
- [[02-Eigenschaften|Transparenz in verteilten Systemen]]

---

## Quellen

- Birrell, A. D., & Nelson, B. J. (1984). *Implementing Remote Procedure Calls*. ACM Transactions on Computer Systems.
- RFC 707 (1976). A High-Level Framework for Network-Based Resource Sharing. IETF.
- RFC 1057 (1988). RPC: Remote Procedure Call Protocol Specification Version 2. IETF.
- RFC 5531 (2009). RPC: Remote Procedure Call Protocol Specification Version 2. IETF.
