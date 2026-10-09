---
author: Andreas Hümmer
title: Threads
tags:
  - content
  - bs
  - prozesse
  - threads
  - multithreading
  - kernel-threads
  - user-threads
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Threads

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition von Threads (leichtgewichtige Prozesse) kennen
> - Den Unterschied zwischen User-Level und Kernel-Level Threads verstehen
> - Vorteile und Nachteile von Threads erklären können
> - Die Begriffe Multithreading, Multitasking und Multiprocessing unterscheiden
> - Verstehen, was Threads teilen und was sie nicht teilen

---

## Definition

> [!quote] **Formale Definition**
> Ein **Thread** ist eine leichtgewichtige Ausführungseinheit innerhalb eines Prozesses. Die direkte Beziehung zwischen Kontrollfluss und Adressraum wird aufgehoben – kooperierende Threads können sich einen Adressraum teilen (aber nicht den Stack).

---

## Prozesse und Threads im Kontext

```
┌─────────────────────────────────────────────────────────────┐
│                         PROZESS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │           Globale und statische Daten                 │  │
│  │                   (gemeinsam)                         │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐      ┌─────────┐    │
│  │ Stack 1 │  │ Stack 2 │  │ Stack 3 │ ···  │ Stack n │    │
│  │         │  │         │  │         │      │         │    │
│  └────┬────┘  └────┬────┘  └────┬────┘      └────┬────┘    │
│       │            │            │                │          │
│  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐      ┌────┴────┐    │
│  │Thread 1 │  │Thread 2 │  │Thread 3 │ ···  │Thread n │    │
│  └─────────┘  └─────────┘  └─────────┘      └─────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Was Threads teilen und was nicht

| Geteilt (pro Prozess) | Nicht geteilt (pro Thread) |
|----------------------|---------------------------|
| Adressraum | Stack |
| Globale Variablen | Programmzähler (PC) |
| Offene Dateien | Register |
| Signalhandler | Thread-ID |
| Code-Segment | Zustand (Running/Ready/Blocked) |

---

## User-Level vs. Kernel-Level Threads

```
┌─────────────────────────────────────────────────────────────┐
│              USER-LEVEL THREADS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────┐  User Space       │
│  │         Thread-Bibliothek           │                   │
│  │  ┌───────┐ ┌───────┐ ┌───────┐     │                   │
│  │  │  T1   │ │  T2   │ │  T3   │     │                   │
│  │  └───────┘ └───────┘ └───────┘     │                   │
│  └────────────────┬────────────────────┘                   │
│                   │                                         │
│  ─────────────────┼───────────────────────────────────────  │
│                   ▼                    Kernel Space        │
│           ┌───────────────┐                                │
│           │    Prozess    │  ← Kernel sieht nur            │
│           │   (1 Thread)  │    einen Thread                │
│           └───────────────┘                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              KERNEL-LEVEL THREADS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────┐  User Space       │
│  │           Anwendung                 │                   │
│  │  ┌───────┐ ┌───────┐ ┌───────┐     │                   │
│  │  │  T1   │ │  T2   │ │  T3   │     │                   │
│  │  └───┬───┘ └───┬───┘ └───┬───┘     │                   │
│  └──────┼─────────┼─────────┼──────────┘                   │
│         │         │         │                               │
│  ───────┼─────────┼─────────┼────────────────────────────  │
│         ▼         ▼         ▼          Kernel Space        │
│     ┌───────┐ ┌───────┐ ┌───────┐                         │
│     │ K-T1  │ │ K-T2  │ │ K-T3  │  ← Kernel kennt         │
│     └───────┘ └───────┘ └───────┘    alle Threads         │
└─────────────────────────────────────────────────────────────┘
```

### Vergleich

| Eigenschaft | Kernel-Threads | User-Threads |
|-------------|----------------|--------------|
| **Vorteile** | Ausnutzung mehrerer Prozessorkerne | Sehr schneller Kontextwechsel |
| | Ggf. mehr Rechenzeit | Keine Kernel-Beteiligung |
| | Threads können unabhängig blockieren | Portabel |
| **Nachteile** | Nur im Supervisor-Mode möglich | Blockierung eines Threads blockiert den ganzen Prozess |
| | Kontextwechsel teurer | Kein zusätzlicher Rechenzeitanteil |
| | | Keine echte Parallelität |

---

## Multithreading vs. Multitasking vs. Multiprocessing

```
┌─────────────────────────────────────────────────────────────┐
│                    VERGLEICH                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MULTITHREADING          MULTITASKING         MULTIPROCESSING
│  ┌─────────────┐        ┌─────────────┐      ┌─────────────┐
│  │   Prozess   │        │  Prozess A  │      │   CPU 1     │
│  │ ┌───┬───┬───┤        ├─────────────┤      │  Prozess A  │
│  │ │T1 │T2 │T3 │        │  Prozess B  │      ├─────────────┤
│  │ └───┴───┴───┘        ├─────────────┤      │   CPU 2     │
│  │             │        │  Prozess C  │      │  Prozess B  │
│  └─────────────┘        └─────────────┘      └─────────────┘
│                                                             │
│  Quasi-gleichzeitig     Quasi-gleichzeitig   Echt parallel │
│  mehrere Threads        mehrere Prozesse     mehrere CPUs  │
│  eines Prozesses        auf einer CPU        /Kerne        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Begriff | Beschreibung |
|---------|--------------|
| **Multithreading** | Quasi-gleichzeitiges Abarbeiten mehrerer Threads **desselben** Prozesses |
| **Multitasking** | Quasi-gleichzeitiges Abarbeiten mehrerer **Prozesse** |
| **Multiprocessing** | **Echtes** gleichzeitiges Abarbeiten auf mehreren Prozessoren/Kernen |

> [!note] **Zielsetzung**
> Alle drei Konzepte dienen der **optimalen Ausnutzung der Ressourcen** und dem **schnelleren Ablauf der Programme**.

---

## Vorteile und Nachteile von Threads

### Vorteile

- **Hyperthreading-Nutzung**: Programme können von mehreren Kontrollflüssen profitieren
- **Schneller Kontextwechsel**: Selber Adressraum → weniger zu sichern/laden
- **Ressourceneffizienz**: Threads teilen Speicher und Ressourcen
- **Kommunikation**: Gemeinsamer Adressraum vereinfacht Datenaustausch

### Nachteile

- **Komplexere Programmierung**: Thread-sichere Programmierung ist schwierig
- **Synchronisation nötig**: Zugriff auf gemeinsame Ressourcen muss koordiniert werden
- **Debugging schwieriger**: Race Conditions sind schwer zu finden
- **Risiko von Deadlocks**: Bei falscher Synchronisation

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Threads existieren innerhalb von Prozessen
- [[02-Scheduling|Scheduling]] → Threads können geschedult werden
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Threads erfordern Synchronisation
- [[02-Semaphore|Semaphore]] → Synchronisationsmechanismus für Threads

---

## Praktische Kommandos

### Linux/Unix

| Kommando | Beschreibung |
|----------|--------------|
| `ps -eLf` | Threads anzeigen |
| `top -H` | Threads in top anzeigen |
| `htop` | Threads interaktiv (F2 → Display → Show threads) |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition Thread vs. Prozess
> - User-Level vs. Kernel-Level Threads (Vor-/Nachteile)
> - Was teilen Threads, was nicht?
> - Unterschied Multithreading/Multitasking/Multiprocessing

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen einem Prozess und einem Thread?
> 2. Vergleichen Sie User-Level und Kernel-Level Threads!
> 3. Was passiert, wenn ein User-Level Thread blockiert?
> 4. Erklären Sie den Unterschied zwischen Multithreading und Multiprocessing!
> 5. Welche Vorteile bieten Threads gegenüber Prozessen?

> [!tip] **Merkhilfen**
> - **Thread** = "Faden" (mehrere Fäden in einem Stoff = Prozess)
> - **User-Thread blockiert** = "Eine verstopfte Leitung blockiert das ganze Haus"
> - **Kernel-Thread blockiert** = "Nur ein Zimmer ist betroffen"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – Threads on a single core Processor
> - CoreDumped – Threads on Multicore Systems
> - CoreDumped – Concurrency

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
