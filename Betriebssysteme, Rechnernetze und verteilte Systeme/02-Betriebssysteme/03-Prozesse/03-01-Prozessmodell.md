---
author: Andreas Hümmer
title: Prozessmodell
tags:
  - content
- bs
- prozesse
- prozessmodell
- pcb
- interrupt
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Prozessmodell

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition eines Prozesses kennen und erklären können
> - Den Aufbau und Inhalt des Process Control Blocks (PCB) verstehen
> - Die drei Prozesszustände (Running, Ready, Blocked) unterscheiden können
> - Die Prozesshierarchie und Prozesstypen verstehen
> - Die Funktion von Interrupts im Prozessmanagement erklären können
> - Den Unterschied zwischen Systemprozessen und Benutzerprozessen kennen

---
author: Andreas Hümmer

## Definition

> [!quote] **Formale Definition**
> Ein **Prozess** ist ein Programm, das ausgeführt wird. Er besitzt einen eigenen Prozesskontext und unterliegt der Kontrolle des Betriebssystems.

---
author: Andreas Hümmer

## Prozesskontext und PCB

Der **Process Control Block (PCB)** speichert alle Informationen eines Prozesses:

```
┌─────────────────────────────────────────────────────────┐
│                  PROCESS CONTROL BLOCK                  │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────────────────┐   │
│  │   Prozess-ID    │  │        Prozesszustand       │   │
│  │     (PID)       │  │  (Running/Ready/Blocked)    │   │
│  └─────────────────┘  └─────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  SPEICHER                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                  │
│  │  Code   │  │  Daten  │  │  Stack  │                  │
│  └─────────┘  └─────────┘  └─────────┘                  │
├─────────────────────────────────────────────────────────┤
│  PROZESSORREGISTER                                      │
│  • Instruktionszeiger (IP/PC)                           │
│  • Stapelzeiger (SP)                                    │
│  • Mehrzweckregister                                    │
│  • Prozessorstatusregister (PSW)                        │
├─────────────────────────────────────────────────────────┤
│  WEITERE INFORMATIONEN                                  │
│  • Benutzer und Zugriffsrechte                          │
│  • Belegte Betriebsmittel (Dateien, Geräte)             │
│  • Elternprozess / Kindprozesse                         │
│  • CPU-Zeitverbrauch                                    │
└─────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

## Prozesszustände

Prozesse durchlaufen während ihrer Lebenszeit verschiedene Zustände:

```
                    ┌───────────────────┐
                    │                   │
        ┌───────────▶     RUNNING       ◀───────────┐
        │           │   (Ausführung)    │           │
        │           └─────────┬─────────┘           │
        │                     │                     │
        │    Scheduler        │    E/A-Anfrage      │
        │    wählt aus        │    oder Warten      │
        │                     │                     │
        │                     ▼                     │
┌───────┴───────┐       ┌─────────────────┐         │
│               │       │                 │         │
│     READY     │◀──────│    BLOCKED      │─────────┘
│  (Bereit)     │       │   (Wartend)     │  E/A fertig
│               │  E/A  │                 │
└───────────────┘ fertig└─────────────────┘
        ▲
        │
   Neuer Prozess
```

| Zustand | Beschreibung |
|---------|--------------|
| **Running** | Der Prozess wird gerade auf der CPU ausgeführt |
| **Ready** | Der Prozess ist rechenbereit und wartet auf CPU-Zuteilung |
| **Blocked** | Der Prozess wartet auf Beendigung einer E/A-Aktivität |

---
author: Andreas Hümmer

## Prozesstypen und Prioritäten

Prozesse werden nach ihrer Art und Priorität unterschieden:

```
                    PRIORITÄT
                        ▲
                        │
         höchste  ──────┼──────  Systemprozesse
                        │           (Kernel, Treiber)
                        │
                  ──────┼──────  Interaktive Prozesse
                        │           (Benutzereingaben)
                        │
                  ──────┼──────  Batchprozesse
                        │           (Hintergrundaufgaben)
                        │
         niedrigste ────┼──────  Benutzerprozesse
                        │           (normale Anwendungen)
                        ▼
```

| Prozesstyp | Beschreibung | Priorität |
|------------|--------------|-----------|
| **Systemprozesse** | Kernel-Aktivitäten, Treiber | Höchste |
| **Interaktive Prozesse** | Reagieren auf Benutzereingaben | Hoch |
| **Batchprozesse** | Hintergrundverarbeitung | Mittel |
| **Benutzerprozesse** | Normale Anwendungen | Normal |

---
author: Andreas Hümmer

## Interrupts

> [!quote] **Definition**
> Ein **Interrupt** ist ein Signal an den Prozessor, um die sequenzielle Abarbeitung der Befehlszyklen zu unterbrechen.

### Funktionsweise

```
┌─────────────────┐     Interrupt     ┌─────────────────┐
│   Programm A    │ ◀───────────────▶ │ Interrupt       │
│   (läuft)       │      Signal       │ Handler         │
└────────┬────────┘                   └────────┬────────┘
         │                                     │
         │  1. Zustand sichern                 │
         │  2. Handler ausführen               │
         │  3. Zustand wiederherstellen        │
         │                                     │
         ▼                                     ▼
┌─────────────────┐                   ┌─────────────────┐
│   Programm A    │                   │   Reaktion      │
│   (fortgesetzt) │                   │   ausgeführt    │
└─────────────────┘                   └─────────────────┘
```

### Eigenschaften von Interrupts

- Kann von Systemprogrammen (privilegierte Rechte) ausgelöst werden
- Ermöglicht Echtzeit-Systemantworten während anderer Programmausführung
- **Interrupt Handler**: Sichert Zustand, reagiert, stellt Zustand wieder her
- Beispiel: Tastatureingabe während Programmausführung

---
author: Andreas Hümmer

## Prozesshierarchie

Prozesse bilden eine **Prozesshierarchie** (Eltern-Kind-Beziehungen):

```
                    ┌─────────────┐
                    │    init     │  PID 1 (Linux)
                    │   (root)    │
                    └──────┬──────┘
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
      ┌──────────┐   ┌──────────┐   ┌──────────┐
      │  login   │   │  sshd    │   │  cron    │
      └────┬─────┘   └────┬─────┘   └──────────┘
           ▼              ▼
      ┌──────────┐   ┌──────────┐
      │  shell   │   │  shell   │
      └────┬─────┘   └──────────┘
           ▼
      ┌──────────┐
      │   vim    │
      └──────────┘
```

---
author: Andreas Hümmer

## Praktische Kommandos

### Linux/Unix

| Kommando | Beschreibung |
|----------|--------------|
| `ps -eax` | Alle Prozesse anzeigen |
| `pstree` | Prozesshierarchie als Baum |
| `top`, `htop` | Interaktive Prozessübersicht |
| `nice`, `renice` | Priorität ändern |
| `kill` | Prozess beenden |

### Windows

| Kommando | Beschreibung |
|----------|--------------|
| `TASKLIST` | Prozesse auflisten |
| `start /B /WAIT` | Priorität setzen |
| Taskmanager | GUI-Prozessverwaltung |
| Perfmon | Performance Monitor |

---
author: Andreas Hümmer

## Zusammenhänge

- [[03-02-Scheduling|Scheduling]] → CPU-Zuteilung für Prozesse
- [[03-03-Threads|Threads]] → Leichtgewichtige Prozesse
- [[03-04-Interprozesskommunikation|Interprozesskommunikation]] → Kommunikation zwischen Prozessen
- [[04-01-Kritische-Abschnitte|Kritische Abschnitte]] → Synchronisation bei Ressourcenzugriff

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition von Prozess vs. Programm
> - Aufbau und Inhalte des PCB
> - Die drei Prozesszustände und ihre Übergänge
> - Unterschied Systemprozesse vs. Benutzerprozesse
> - Funktion von Interrupts

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen einem Programm und einem Prozess?
> 2. Welche Informationen enthält der PCB?
> 3. Erklären Sie die drei Prozesszustände und ihre Übergänge!
> 4. Was ist ein Interrupt und wozu wird er benötigt?
> 5. Welche Prozesstypen gibt es und wie unterscheiden sie sich in der Priorität?

> [!tip] **Merkhilfen**
> - **PCB** = "Personalausweis" des Prozesses (alle wichtigen Daten)
> - **RRB**: Running → Ready → Blocked (Zustandskreislauf)
> - **Interrupt** = "Türklingel" für die CPU

---
author: Andreas Hümmer

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – A Program is not a Process
> - CoreDumped – Processes
> - AnimOS (Uni Osnabrück): https://ess.cs.uni-osnabrueck.de/software/AnimOS/

---
author: Andreas Hümmer

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
