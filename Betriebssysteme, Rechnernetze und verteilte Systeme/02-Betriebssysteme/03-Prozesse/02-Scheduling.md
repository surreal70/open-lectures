---
author: Andreas Hümmer
title: Scheduling
tags:
  - content
  - bs
  - prozesse
  - scheduling
  - fcfs
  - round-robin
  - sjf
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Scheduling

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Basisziel des Schedulings erklären können
> - Verschiedene Scheduling-Algorithmen kennen und unterscheiden können
> - Preemptive vs. Non-Preemptive Scheduling verstehen
> - Die Ziele und Kriterien für Scheduling-Entscheidungen kennen
> - Konkrete Beispiele für Scheduling-Strategien durchrechnen können

---

## Definition

> [!quote] **Formale Definition**
> **Scheduling** ist der Prozess der geordneten CPU-Zuteilung an konkurrierende Prozesse durch einen Scheduler-Algorithmus.

---

## Grundlegendes

### Basisziel

Das Basisziel des Schedulings ist der **geordnete Ablauf konkurrierender Prozesse**.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Prozess A  │     │  Prozess B  │     │  Prozess C  │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                   ┌───────────────┐
                   │  Warteschlange│
                   │    (Ready)    │
                   └───────┬───────┘
                           │
                   ┌───────┴───────┐
                   │   SCHEDULER   │
                   │   (Auswahl)   │
                   └───────┬───────┘
                           │
                           ▼
                   ┌───────────────┐
                   │     CPU       │
                   └───────┬───────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
      ┌───────────────┐         ┌───────────────┐
      │    Fertig     │         │   Verdrängt   │
      │   (beendet)   │         │ (zurück in WS)│
      └───────────────┘         └───────────────┘
```

### Scheduling-Ziele

| Ziel | Beschreibung |
|------|--------------|
| **Kurze Antwortzeiten** | Schnelle Reaktion auf Benutzereingaben |
| **Optimale CPU-Auslastung** | CPU möglichst nicht im Leerlauf |
| **Hoher Durchsatz** | Viele Aufträge pro Zeiteinheit |
| **Fairness** | Alle Prozesse erhalten CPU-Zeit |
| **Echtzeitverhalten** | Garantierte Reaktionszeiten |

> [!note] **Wichtig**
> Es gibt kein "one fits all" – Zielsetzungen müssen für jedes System individuell festgelegt werden!

---

## Scheduling-Strategien

### Übersicht

| Kategorie | Algorithmen |
|-----------|-------------|
| **Einfach** | FCFS (First Come First Serve) |
| **Zeitscheibenbasiert** | RR (Round Robin), VRR (Virtual Round Robin) |
| **Vorhersagebasiert** | SPN/SJF, SRTF, HRRN |
| **Prioritätenbasiert** | FB, MLQ, MLFQ |

---

### 1. FCFS – First Come First Serve

**Non-Preemptive**: Prozesse werden in Ankunftsreihenfolge abgearbeitet.

```
Ankunft:    P1(0)   P2(1)   P3(2)
Burst:      24      3       3
            
Zeit:   0        24      27      30
        ├────────┼───────┼───────┤
        │   P1   │  P2   │  P3   │
        └────────┴───────┴───────┘

Wartezeiten: P1=0, P2=23, P3=25
Durchschnitt: (0+23+25)/3 = 16
```

| Vorteile | Nachteile |
|----------|-----------|
| Einfach zu implementieren | Convoy-Effekt (lange Prozesse blockieren) |
| Fair (Reihenfolge) | Schlechte Antwortzeiten |

---

### 2. Round Robin (RR)

**Preemptive**: Jeder Prozess erhält eine feste Zeitscheibe (Quantum).

```
Zeitscheibe: 4 Einheiten

Prozesse:   P1(Burst=24)  P2(Burst=3)  P3(Burst=3)

Zeit:   0    4    7    10   14   18   22   26   30
        ├────┼────┼────┼────┼────┼────┼────┼────┤
        │ P1 │ P2 │ P3 │ P1 │ P1 │ P1 │ P1 │ P1 │
        └────┴────┴────┴────┴────┴────┴────┴────┘
              ▲    ▲
              3    3  (fertig vor Quantum-Ende)
```

| Vorteile | Nachteile |
|----------|-----------|
| Faire CPU-Verteilung | Overhead durch Kontextwechsel |
| Gute Antwortzeiten | Quantum-Wahl kritisch |
| Keine Starvation | |

> [!tip] **Quantum-Wahl**
> - Zu klein: Viele Kontextwechsel (Overhead)
> - Zu groß: Nähert sich FCFS an

---

### 3. SJF/SPN – Shortest Job First

**Non-Preemptive**: Der kürzeste Job wird zuerst ausgeführt.

```
Prozesse:   P1(Burst=6)  P2(Burst=8)  P3(Burst=7)  P4(Burst=3)

Sortiert nach Burst:  P4(3) → P1(6) → P3(7) → P2(8)

Zeit:   0    3    9    16   24
        ├────┼────┼────┼────┤
        │ P4 │ P1 │ P3 │ P2 │
        └────┴────┴────┴────┘

Wartezeiten: P4=0, P1=3, P3=9, P2=16
Durchschnitt: (0+3+9+16)/4 = 7
```

| Vorteile | Nachteile |
|----------|-----------|
| Minimale durchschnittliche Wartezeit | Burst-Zeit muss bekannt/geschätzt sein |
| Optimal für Batch-Systeme | Starvation langer Prozesse möglich |

---

### 4. SRTF – Shortest Remaining Time First

**Preemptive** Version von SJF: Der Prozess mit der kürzesten **verbleibenden** Zeit wird ausgeführt.

```
Ankunft:    P1(0,8)  P2(1,4)  P3(2,9)  P4(3,5)
            (Zeit, Burst)

Zeit:   0  1  2  3  4  5 10 17 26
        ├──┼──┼──┼──┼──┼──┼──┼──┤
        │P1│   P2    │P4 │P1 │P3│
        └──┴─────────┴───┴───┴──┘
           ▲
           P2 verdrängt P1 (4 < 7)
```

---

### 5. HRRN – Highest Response Ratio Next

Berücksichtigt sowohl Wartezeit als auch Bedienzeit:

```
                   Wartezeit + Bedienzeit
Response Ratio = ─────────────────────────
                       Bedienzeit
```

→ Verhindert Starvation, da Wartezeit die Priorität erhöht.

---

### 6. Multi-Level Feedback Queue (MLFQ)

Mehrere Warteschlangen mit unterschiedlichen Prioritäten:

```
┌─────────────────────────────────────────────┐
│           MULTI-LEVEL FEEDBACK QUEUE        │
├─────────────────────────────────────────────┤
│                                             │
│  Priorität HOCH    ┌─────────────────────┐  │
│  Quantum: kurz     │ Queue 0: RR (q=8)   │──┼──▶ CPU
│                    └──────────┬──────────┘  │
│                               │ (Quantum    │
│                               │  verbraucht)│
│                               ▼             │
│  Priorität MITTEL  ┌─────────────────────┐  │
│  Quantum: mittel   │ Queue 1: RR (q=16)  │──┼──▶ CPU
│                    └──────────┬──────────┘  │
│                               │             │
│                               ▼             │
│  Priorität NIEDRIG ┌─────────────────────┐  │
│  Quantum: lang     │ Queue 2: FCFS       │──┼──▶ CPU
│                    └─────────────────────┘  │
└─────────────────────────────────────────────┘
```

| Regel | Beschreibung |
|-------|--------------|
| Neue Prozesse | Starten in höchster Queue |
| Quantum verbraucht | Abstieg in nächste Queue |
| E/A-Blockierung | Verbleibt in aktueller Queue |
| Lange Wartezeit | Kann wieder aufsteigen (Aging) |

---

## Preemptive vs. Non-Preemptive

| Eigenschaft | Non-Preemptive | Preemptive |
|-------------|----------------|------------|
| **Verdrängung** | Nein | Ja |
| **Kontextwechsel** | Nur bei Beendigung/Blockierung | Jederzeit möglich |
| **Antwortzeiten** | Schlechter | Besser |
| **Overhead** | Geringer | Höher |
| **Beispiele** | FCFS, SJF | RR, SRTF, MLFQ |

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Prozesszustände werden durch Scheduler verändert
- [[03-Threads|Threads]] → Können ebenfalls geschedult werden
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Scheduling kann Race Conditions beeinflussen

---

## Praktische Tools

> [!note] **AnimOS – Interaktives Tool**
> Die Universität Osnabrück bietet ein interaktives Scheduling-Tool:
> https://ess.cs.uni-osnabrueck.de/software/AnimOS/

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Preemptive vs. Non-Preemptive
> - FCFS, Round Robin, SJF/SPN verstehen und berechnen können
> - Multi-Level Feedback Queue Konzept
> - Vor- und Nachteile der Algorithmen

> [!question] **Häufige Prüfungsfragen**
> 1. Berechnen Sie die durchschnittliche Wartezeit für FCFS/RR/SJF bei gegebenen Prozessen!
> 2. Was ist der Convoy-Effekt bei FCFS?
> 3. Erklären Sie den Unterschied zwischen preemptive und non-preemptive Scheduling!
> 4. Wie funktioniert eine Multi-Level Feedback Queue?
> 5. Welche Probleme hat SJF und wie löst HRRN diese?

> [!tip] **Merkhilfen**
> - **FCFS** = "Warteschlange an der Kasse" (wer zuerst da ist)
> - **RR** = "Karussell" (jeder bekommt eine Runde)
> - **SJF** = "Expresskasse" (wenige Artikel zuerst)
> - **MLFQ** = "Aufzug" (neu oben, bei Verzögerung nach unten)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – Scheduling
> - AnimOS Demo Videos

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
