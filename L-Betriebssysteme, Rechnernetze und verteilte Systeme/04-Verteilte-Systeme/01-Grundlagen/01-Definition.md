---
author: Andreas Hümmer
title: Definition verteilter Systeme
tags:
  - content
  - vs
  - grundlagen
  - definition
created: '2026-10-07'
modified: '2026-10-13'
bereich: VS
---

# Definition verteilter Systeme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die klassischen Definitionen verteilter Systeme kennen (Tanenbaum, Bal, Lamport)
> - Den Unterschied zwischen Distributed Computing, Parallel Computing und Multiprocessing verstehen
> - Die Begriffe Node, Nebenläufigkeit und Transparenz einordnen können
> - Die grundlegenden Merkmale verteilter Systeme benennen können

---

## Was ist ein verteiltes System?

> [!important] **Kernkonzept**
> Ein **verteiltes System** ist eine Sammlung von unabhängigen Computern, die sich gegenüber dem Anwender als ein kohärentes System darstellen. Die Verteilung ist für den Benutzer transparent – er nimmt das System als Einheit wahr.

### Klassische Definitionen

```
┌─────────────────────────────────────────────────────────────────┐
│              Definitionen verteilter Systeme                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Tanenbaum:                                                    │
│   "Verteilte Systeme sind eine Sammlung von unabhängigen       │
│    Computern, die sich gegenüber dem Anwender als ein          │
│    kohärentes System darstellen."                               │
│                                                                  │
│   Bal:                                                          │
│   "Ein verteiltes Computersystem besteht aus mehreren          │
│    autonomen Prozessoren, die sich keinen Hauptspeicher        │
│    teilen, aber mittels Austausch von Nachrichten über ein     │
│    Netzwerk miteinander kooperieren."                          │
│                                                                  │
│   Lamport:                                                      │
│   "Ein verteiltes System ist es, wenn ein Fehler eines         │
│    Computers, von dessen Existenz Du nichts wusstest,          │
│    deinen eigenen Rechner unbrauchbar macht."                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> [!example] **Analogie: Restaurant-Kette**
> - Viele **Filialen** (= Nodes) arbeiten unabhängig
> - Gemeinsames **Bestellsystem** (= verteilte Anwendung)
> - Kunde sieht nur "**eine Firma**" (= Transparenz)
> - Fällt eine Filiale aus, läuft der Rest weiter (= Fehlertoleranz)
> - Bei mehr Kunden: mehr Filialen öffnen (= Skalierbarkeit)

---

## Abgrenzung: Distributed vs. Parallel vs. Multi

```
┌─────────────────────────────────────────────────────────────────┐
│              Abgrenzung der Begriffe                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Multithreading          Multitasking          Multiprocessing │
│   ───────────────         ────────────          ─────────────── │
│   Quasi-gleichzeitiges    Quasi-gleichzeitiges  Echtes gleich-  │
│   Abarbeiten mehrerer     Abarbeiten mehrerer   zeitiges Abarb. │
│   Threads des selben      Prozesse              auf mehreren    │
│   Prozesses                                     Prozessoren     │
│                                                                  │
│         │                       │                     │         │
│         └───────────────────────┴─────────────────────┘         │
│                         │                                       │
│                    Nebenläufig                                  │
│                   (concurrent)                                  │
│                                                                  │
│   Zielsetzung: Optimale Ausnutzung der Ressourcen und          │
│                schnellerer Ablauf der Programme                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Distributed Computing vs. Parallel Computing

```
┌─────────────────────────────────────────────────────────────────┐
│        Distributed Computing vs. Parallel Computing            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Distributed Computing:                                        │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │      CPU              CPU              CPU               │  │
│   │   ┌───────┐        ┌───────┐        ┌───────┐           │  │
│   │   │Speicher│       │Speicher│       │Speicher│          │  │
│   │   └───────┘        └───────┘        └───────┘           │  │
│   │        │               │               │                 │  │
│   │        └───────────────┼───────────────┘                 │  │
│   │                    Netzwerk                              │  │
│   │                                                          │  │
│   │   → Eigenständige Systeme, kommunizieren über Netzwerk  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Parallel Computing:                                           │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │      CPU        CPU        CPU                           │  │
│   │        │          │          │                           │  │
│   │        └──────────┼──────────┘                           │  │
│   │              Speicher                                    │  │
│   │                                                          │  │
│   │   → Mehrere CPUs, gemeinsamer Speicher                  │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Multiprocessing mit Shared Storage:                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │    CPU         CPU         CPU                           │  │
│   │  ┌─────┐     ┌─────┐     ┌─────┐                        │  │
│   │  │Speicher│  │Speicher│  │Speicher│                     │  │
│   │  └───┬───┘   └───┬───┘   └───┬───┘                      │  │
│   │      └───────────┼───────────┘                           │  │
│   │            Shared Storage                                │  │
│   │                                                          │  │
│   │   → Eigener Speicher + gemeinsamer Speicher             │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Nodes

Ein **Node** ist ein Teilnehmer in einem verteilten System:

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Autonomie** | Jeder Node kann eigenständig agieren |
| **Synonym** | Computer, Prozess, Prozessor |
| **Vollständig** | Kann ein vollwertiges System mit eigenem OS sein |
| **Teil** | Kann Teil eines Mehrprozessorsystems sein |
| **Vernetzt** | Nodes sind miteinander über ein Netzwerk verbunden |

---

## Grundlegende Definitionen

```
┌─────────────────────────────────────────────────────────────────┐
│              Kernpunkte verteilter Systeme                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Teilnehmer werden als Nodes bezeichnet                     │
│   ✓ Die teilnehmenden Nodes sind miteinander vernetzt          │
│   ✓ Nodes kommunizieren auf unterschiedliche Weise             │
│                                                                  │
│   ✓ Prozessor, Speicher und Kommunikation müssen gemeinsam    │
│     betrachtet werden                                          │
│                                                                  │
│   ✓ Konflikte und kritische Abschnitte erfordern sorgfältige  │
│     Synchronisation                                            │
│                                                                  │
│   ✓ Transaktionsverwaltung muss Konsistenz garantieren        │
│   ✓ Persistenz der (flüchtigen) Daten muss sichergestellt sein│
│                                                                  │
│   ✓ Der Service verbirgt die Komplexität gegenüber dem        │
│     Benutzer                                                   │
│   ✓ Es erscheint als würde der Dienst von "einem" System      │
│     erbracht                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Zusammenhänge

```mermaid
graph LR
    A[Verteiltes System] --> B[Nodes]
    A --> C[Netzwerk]
    A --> D[Transparenz]
    A --> E[Synchronisation]
    B --> F[Autonomie]
    C --> G[Kommunikation]
    D --> H[Kohärenz]
    E --> I[ACID]
```

- [[02-Eigenschaften|Eigenschaften]] → Skalierbarkeit, Fehlertoleranz, Transparenz
- [[03-Fallacies|Fallacies]] → Die 8 Irrtümer verteilter Systeme
- [[../02-Kommunikation/00-Kommunikation-Index|Kommunikation]] → Nachrichtenaustausch, RPC, REST
- [[../03-Konsistenz/01-CAP-Theorem|CAP-Theorem]] → Consistency, Availability, Partition Tolerance

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition nach Tanenbaum, Bal und Lamport
> - Unterschied Distributed vs. Parallel Computing
> - Begriff "Node" und dessen Eigenschaften
> - Transparenz als zentrales Merkmal

> [!question] **Häufige Prüfungsfragen**
> 1. Definieren Sie ein verteiltes System nach Tanenbaum.
> 2. Was unterscheidet Distributed Computing von Parallel Computing?
> 3. Was bedeutet Transparenz im Kontext verteilter Systeme?
> 4. Was ist ein Node und welche Eigenschaften hat er?
> 5. Erklären Sie Lamports humorvolle Definition.

> [!tip] **Merkhilfen**
> - **Tanenbaum** = "kohärentes System" (Zusammenhalt)
> - **Bal** = "Nachrichten über Netzwerk" (kein gemeinsamer Speicher)
> - **Lamport** = "Fehler macht deinen Rechner kaputt" (Abhängigkeiten)
> - **Distributed** = Netzwerk, **Parallel** = gemeinsamer Speicher

---

## Weiterführende Ressourcen

> [!note] **Literatur**
> - Tanenbaum, van Steen: Verteilte Systeme – Das Standardwerk
> - Coulouris et al.: Distributed Systems – Concepts and Design

> [!tip] **Praktische Beispiele**
> - **AWS/Azure/GCP** – Cloud-Plattformen als verteilte Systeme
> - **Kubernetes** – Container-Orchestrierung
> - **Apache Kafka** – Verteiltes Message-System

---

## Quellen

- Tanenbaum, Andrew S.; van Steen, Maarten: Verteilte Systeme – Das Standardwerk für verteilte Systeme mit den klassischen Definitionen.
- Bal, Henri E.: Programming Distributed Systems – Grundlegende Konzepte der Verteilung.
- Lamport, Leslie: Diverse Publikationen – Fundamentale Arbeiten zu verteilten Algorithmen und Uhren.
