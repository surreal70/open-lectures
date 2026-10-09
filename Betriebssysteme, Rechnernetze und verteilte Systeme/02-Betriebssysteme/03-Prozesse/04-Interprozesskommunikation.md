---
author: Andreas Hümmer
title: Interprozesskommunikation
tags:
  - content
  - bs
  - prozesse
  - ipc
  - pipes
  - sockets
  - shared-memory
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Interprozesskommunikation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen IPC-Mechanismen kennen und unterscheiden können
> - Shared Memory vs. Message Passing erklären können
> - Unix IPC-Mechanismen (Pipes, Signals, Sockets) kennen
> - Die Vor- und Nachteile der verschiedenen Kommunikationsarten verstehen
> - Wissen, wann welcher IPC-Mechanismus sinnvoll ist

---

## Definition

> [!quote] **Formale Definition**
> **Interprozesskommunikation (IPC)** bezeichnet Mechanismen zur Zusammenarbeit mehrerer Prozesse – sowohl zur Kommunikation (Datenaustausch) als auch zur Koordination.

---

## Kommunikationsszenarien

```
┌─────────────────────────────────────────────────────────────┐
│              KOMMUNIKATIONSSZENARIEN                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Im System, auf einer CPU      Im System, auf mehreren CPUs │
│  ┌─────────────────────┐       ┌─────────────────────┐      │
│  │  ┌───┐     ┌───┐    │       │  CPU 1    CPU 2     │      │
│  │  │P1 │ ◀──▶│P2 │    │       │  ┌───┐    ┌───┐     │      │
│  │  └───┘     └───┘    │       │  │P1 │◀──▶│P2 │     │      │
│  │       CPU           │       │  └───┘    └───┘     │      │
│  └─────────────────────┘       └─────────────────────┘      │
│  (zeitversetzt)                (parallel möglich)           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│           Über Systemgrenzen hinweg                         │
│  ┌──────────────────┐       ┌──────────────────┐            │
│  │    System A      │       │    System B      │            │
│  │    ┌───┐         │       │         ┌───┐   │            │
│  │    │P1 │─────────┼───────┼────────▶│P2 │   │            │
│  │    └───┘         │  Netz │         └───┘   │            │
│  └──────────────────┘       └──────────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## IPC-Methoden im Überblick

### Zwei Grundansätze

```
┌─────────────────────────────────────────────────────────────┐
│                    IPC-GRUNDANSÄTZE                         │
├────────────────────────────┬────────────────────────────────┤
│      SHARED MEMORY         │       MESSAGE PASSING          │
├────────────────────────────┼────────────────────────────────┤
│                            │                                │
│   ┌───────────────────┐    │    ┌───┐  Nachricht  ┌───┐    │
│   │  Gemeinsamer      │    │    │P1 │────────────▶│P2 │    │
│   │  Speicherbereich  │    │    └───┘             └───┘    │
│   │  ┌───┐   ┌───┐    │    │                                │
│   │  │P1 │   │P2 │    │    │                                │
│   │  └───┘   └───┘    │    │                                │
│   └───────────────────┘    │                                │
│                            │                                │
│   • Schnell                │    • Sicherer                  │
│   • Erfordert Sync.        │    • Portabler                 │
│   • Lokal                  │    • Auch über Netzwerk        │
│                            │                                │
└────────────────────────────┴────────────────────────────────┘
```

| Methode | Vorteile | Nachteile |
|---------|----------|-----------|
| **Shared Memory** | Schnell, direkter Zugriff | Erfordert Synchronisation |
| **Message Passing** | Sicher, portabel | Langsamer, Kopieraufwand |

---

## Unix IPC-Mechanismen

### 1. Signals

Asynchrone Benachrichtigungen zwischen Prozessen.

```
Prozess A                    Prozess B
┌─────────┐    SIGTERM       ┌─────────┐
│         │ ────────────────▶│         │
│  kill() │                  │ Handler │
│         │                  │         │
└─────────┘                  └─────────┘
```

| Signal | Beschreibung |
|--------|--------------|
| `SIGTERM` | Terminierung anfragen |
| `SIGKILL` | Sofortige Terminierung (nicht abfangbar) |
| `SIGINT` | Interrupt (Ctrl+C) |
| `SIGUSR1/2` | Benutzerdefiniert |

Siehe: `man signal(2)`

---

### 2. Pipes

Unidirektionale Kommunikation zwischen verwandten Prozessen.

```
┌─────────────────────────────────────────────────────────────┐
│                    ANONYMOUS PIPE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Prozess A              Pipe              Prozess B        │
│   (Eltern)                                 (Kind)           │
│   ┌─────────┐     ┌──────────────┐     ┌─────────┐         │
│   │         │────▶│  Puffer      │────▶│         │         │
│   │ write() │     │  (FIFO)      │     │ read()  │         │
│   └─────────┘     └──────────────┘     └─────────┘         │
│                                                             │
│   Beispiel: ls | grep ".txt"                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Named Pipes (FIFOs)

Für nicht-verwandte Prozesse, haben einen Namen im Dateisystem.

```bash
mkfifo /tmp/mypipe
echo "Hello" > /tmp/mypipe &    # Schreiber
cat /tmp/mypipe                  # Leser
```

---

### 3. Message Queues

Nachrichtenwarteschlangen für strukturierte Kommunikation.

```
┌─────────────────────────────────────────────────────────────┐
│                    MESSAGE QUEUE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Sender                Queue                  Empfänger     │
│  ┌───────┐    ┌─────────────────────┐       ┌───────┐      │
│  │ P1    │───▶│ [Msg3][Msg2][Msg1] │──────▶│ P2    │      │
│  └───────┘    └─────────────────────┘       └───────┘      │
│  ┌───────┐                                                  │
│  │ P3    │───▶        (FIFO)                               │
│  └───────┘                                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### 4. Shared Memory

Der schnellste IPC-Mechanismus für große Datenmengen.

```
┌─────────────────────────────────────────────────────────────┐
│                    SHARED MEMORY                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     Prozess A              Shared              Prozess B    │
│    ┌─────────┐            Memory              ┌─────────┐  │
│    │         │         ┌─────────┐            │         │  │
│    │  Addr   │────────▶│         │◀───────────│  Addr   │  │
│    │  Space  │         │  Daten  │            │  Space  │  │
│    │         │         │         │            │         │  │
│    └─────────┘         └─────────┘            └─────────┘  │
│                                                             │
│    ⚠️ Erfordert Synchronisation (Semaphore, Mutex)!        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

> [!danger] **Achtung**
> Bei Shared Memory muss der Zugriff synchronisiert werden, sonst entstehen Race Conditions! → Siehe [[01-Kritische-Abschnitte|Kritische Abschnitte]]

---

### 5. Sockets

Netzwerkfähige Kommunikation, auch lokal (Unix Domain Sockets).

```
┌─────────────────────────────────────────────────────────────┐
│                    SOCKETS                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────────┐           ┌──────────────────┐      │
│   │    Client        │           │    Server        │      │
│   │   ┌──────────┐   │           │   ┌──────────┐   │      │
│   │   │ socket() │   │           │   │ socket() │   │      │
│   │   │connect() │───┼───────────┼──▶│ bind()   │   │      │
│   │   │ send()   │   │  Netzwerk │   │ listen() │   │      │
│   │   │ recv()   │◀──┼───────────┼───│ accept() │   │      │
│   │   │ close()  │   │    oder   │   │ recv()   │   │      │
│   │   └──────────┘   │   lokal   │   │ send()   │   │      │
│   └──────────────────┘           │   │ close()  │   │      │
│                                  │   └──────────┘   │      │
│                                  └──────────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Socket-Typ | Beschreibung |
|------------|--------------|
| **TCP (Stream)** | Verbindungsorientiert, zuverlässig |
| **UDP (Datagram)** | Verbindungslos, schnell |
| **Unix Domain** | Nur lokal, schneller als IP |

---

## Synchron vs. Asynchron

| Modus | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Synchron** | Sender wartet auf Empfang/Bestätigung | Telefonat |
| **Asynchron** | Sender wartet nicht | E-Mail, Signals |

---

## Zusammenfassung der IPC-Mechanismen

| Mechanismus | Richtung | Verwandte Prozesse | Netzwerkfähig |
|-------------|----------|-------------------|---------------|
| Signals | Unidirektional | Nein | Nein |
| Pipes | Unidirektional | Ja | Nein |
| Named Pipes | Unidirektional | Nein | Nein |
| Message Queues | Bidirektional | Nein | Nein |
| Shared Memory | Bidirektional | Nein | Nein |
| Sockets | Bidirektional | Nein | Ja |

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Prozesse müssen kommunizieren
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Synchronisation bei Shared Memory
- [[03-Deadlocks|Deadlocks]] → Können bei IPC auftreten!
- [[02-Semaphore|Semaphore]] → Für Shared Memory Synchronisation

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Shared Memory vs. Message Passing
> - Unix IPC-Mechanismen (Pipes, Signals, Sockets, Shared Memory)
> - Vor- und Nachteile der verschiedenen Mechanismen
> - Wann braucht man Synchronisation?

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen und erklären Sie drei IPC-Mechanismen unter Unix!
> 2. Was ist der Unterschied zwischen Shared Memory und Message Passing?
> 3. Warum benötigt Shared Memory Synchronisation?
> 4. Was ist der Unterschied zwischen Pipes und Named Pipes?
> 5. Welche IPC-Methode würden Sie für Netzwerkkommunikation wählen und warum?

> [!tip] **Merkhilfen**
> - **Pipe** = "Rohrpost" (nur eine Richtung, nur verwandte)
> - **Shared Memory** = "Gemeinsame Kreidetafel" (schnell, aber alle müssen aufpassen)
> - **Socket** = "Telefon" (bidirektional, auch über Distanz)
> - **Signal** = "Klopfzeichen" (nur Benachrichtigung, keine Daten)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – Inter Process Communication

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
