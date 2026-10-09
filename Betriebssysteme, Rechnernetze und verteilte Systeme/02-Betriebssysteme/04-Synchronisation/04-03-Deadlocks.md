---
author: Andreas Hümmer
title: Deadlocks
tags:
  - content
- bs
- synchronisation
- deadlock
- verklemmung
- banker-algorithmus
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Deadlocks (Verklemmungen)

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition eines Deadlocks kennen
> - Die vier notwendigen Bedingungen (Coffman-Bedingungen) verstehen
> - Die vier Strategien zur Behandlung von Deadlocks kennen
> - Den Banker's Algorithm erklären können
> - Deadlock-Situationen erkennen und lösen können

---
author: Andreas Hümmer

## Definition

> [!quote] **Formale Definition**
> Eine Menge von Prozessen befindet sich in einem **Deadlock-Zustand**, wenn jeder Prozess aus der Menge auf ein Ereignis wartet, das nur ein anderer Prozess aus der Menge auslösen kann.

---
author: Andreas Hümmer

## Visualisierung

```
┌─────────────────────────────────────────────────────────────┐
│              DEADLOCK – VISUALISIERUNG                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌───────────┐                     ┌───────────┐           │
│   │           │    wartet auf       │           │           │
│   │ Prozess A │ ──────────────────▶ │ Ressource │           │
│   │           │                     │     B     │           │
│   └─────┬─────┘                     └─────┬─────┘           │
│         │                                 │                 │
│         │ hält                            │ gehalten von    │
│         │                                 │                 │
│         ▼                                 ▼                 │
│   ┌───────────┐                     ┌───────────┐           │
│   │ Ressource │                     │           │           │
│   │     A     │ ◀────────────────── │ Prozess B │           │
│   │           │    wartet auf       │           │           │
│   └───────────┘                     └───────────┘           │
│                                                             │
│   → Zyklische Wartesituation = DEADLOCK!                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

## Die vier Coffman-Bedingungen

Ein Deadlock kann **nur** auftreten, wenn **alle vier** Bedingungen gleichzeitig erfüllt sind:

```
┌─────────────────────────────────────────────────────────────┐
│              COFFMAN-BEDINGUNGEN                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. MUTUAL EXCLUSION (Gegenseitiger Ausschluss)             │
│     Betriebsmittel sind nur unteilbar benutzbar             │
│     (nur ein Prozess kann sie gleichzeitig nutzen)          │
│                                                             │
│  2. HOLD AND WAIT (Halten und Warten)                       │
│     Betriebsmittel sind nur schrittweise belegbar           │
│     (Prozess hält Ressourcen und wartet auf weitere)        │
│                                                             │
│  3. NO PREEMPTION (Keine Entziehbarkeit)                    │
│     Betriebsmittel sind nicht entziehbar                    │
│     (können nur freiwillig freigegeben werden)              │
│                                                             │
│  4. CIRCULAR WAIT (Zyklisches Warten)                       │
│     Es existiert eine zyklische Kette von Prozessen,        │
│     die aufeinander warten                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

## Strategien zur Deadlock-Behandlung

### Übersicht

```
┌─────────────────────────────────────────────────────────────┐
│              DEADLOCK-STRATEGIEN                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  1. PREVENTION (Vorbeugung)                         │    │
│  │     Eine der vier Bedingungen unmöglich machen      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  2. AVOIDANCE (Vermeidung)                          │    │
│  │     Nur sichere Zustände zulassen (Banker's Alg.)   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  3. DETECTION (Erkennung)                           │    │
│  │     Deadlocks erkennen und dann reagieren           │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  4. IGNORANCE (Ignorieren)                          │    │
│  │     "Ostrich Algorithm" – hoffen, dass es nicht     │    │
│  │     passiert (z.B. bei seltenen Deadlocks)          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

### 1. Prevention (Vorbeugung)

Eine der vier Bedingungen verhindern:

| Bedingung | Maßnahme | Problem |
|-----------|----------|---------|
| **Mutual Exclusion** | Ressourcen teilbar machen | Meist nicht möglich |
| **Hold and Wait** | Alle Ressourcen auf einmal anfordern | Ineffizient, Starvation |
| **No Preemption** | Ressourcen entziehbar machen | Nicht immer möglich |
| **Circular Wait** | Nummerierung und Ordnung | Funktioniert gut! |

#### Beispiel: Ressourcen-Ordnung

```
Ressourcen: R1 < R2 < R3 < R4  (feste Ordnung)

Regel: Prozess darf nur Ressourcen in aufsteigender
       Reihenfolge anfordern!

Prozess A: R1 → R3 → R4   ✓ OK
Prozess B: R2 → R1        ✗ VERBOTEN (R1 < R2)

→ Kein Zyklus möglich!
```

---
author: Andreas Hümmer

### 2. Avoidance (Vermeidung) – Banker's Algorithm

Das System prüft vor jeder Ressourcenzuteilung, ob ein **sicherer Zustand** erreichbar bleibt.

> [!quote] **Sicherer Zustand**
> Ein Zustand ist **sicher**, wenn es eine Reihenfolge gibt, in der alle Prozesse ihre Arbeit beenden können.

```
┌─────────────────────────────────────────────────────────────┐
│              BANKER'S ALGORITHM – BEISPIEL                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Verfügbare Ressourcen: 3                                  │
│                                                             │
│   Prozess │ Belegt │ Max │ Noch benötigt                    │
│   ────────┼────────┼─────┼──────────────                    │
│      P1   │   1    │  4  │      3                           │
│      P2   │   2    │  6  │      4                           │
│      P3   │   2    │  8  │      6                           │
│                                                             │
│   Verfügbar: 3                                              │
│                                                             │
│   Sichere Sequenz finden:                                   │
│   1. P1 kann fertig werden (braucht 3, haben 3)             │
│      Nach P1: Verfügbar = 3 + 1 = 4                         │
│   2. P2 kann fertig werden (braucht 4, haben 4)             │
│      Nach P2: Verfügbar = 4 + 2 = 6                         │
│   3. P3 kann fertig werden (braucht 6, haben 6) ✓           │
│                                                             │
│   → Sicherer Zustand! Sequenz: P1 → P2 → P3                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

### 3. Detection (Erkennung)

Deadlocks zulassen, aber erkennen und beheben.

#### Erkennung: Resource Allocation Graph

```
┌─────────────────────────────────────────────────────────────┐
│              RESOURCE ALLOCATION GRAPH                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ○ = Prozess                                               │
│   □ = Ressource                                             │
│   ──▶ = Anforderung (Prozess → Ressource)                   │
│   ◀── = Zuteilung (Ressource → Prozess)                     │
│                                                             │
│   ┌───┐          ┌───┐                                      │
│   │ P1│──────────│ R1│                                      │
│   └───┘     ┌───▶└───┘                                      │
│     ▲       │      │                                        │
│     │       │      ▼                                        │
│   ┌───┐     │    ┌───┐                                      │
│   │ R2│─────┘    │ P2│                                      │
│   └───┘          └───┘                                      │
│     ▲              │                                        │
│     └──────────────┘                                        │
│                                                             │
│   Zyklus erkannt: P1 → R1 → P2 → R2 → P1                    │
│   → DEADLOCK!                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Recovery (Behebung)

| Methode | Beschreibung |
|---------|--------------|
| **Prozess abbrechen** | Einen oder mehrere Prozesse terminieren |
| **Ressourcen entziehen** | Ressourcen von Prozessen wegnehmen |
| **Rollback** | Prozesse auf früheren Checkpoint zurücksetzen |

---
author: Andreas Hümmer

### 4. Ignorance (Ignorieren)

Der "Ostrich Algorithm": Kopf in den Sand stecken.

> [!note] **Praxis**
> Viele Betriebssysteme (auch Linux, Windows) ignorieren seltene Deadlocks, weil die Prävention zu teuer wäre.

---
author: Andreas Hümmer

## Klassische Deadlock-Probleme

### Dining Philosophers (Philosophenproblem)

```
┌─────────────────────────────────────────────────────────────┐
│              DINING PHILOSOPHERS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    Philosoph 1                              │
│                       ┌───┐                                 │
│                 Gabel │   │ Gabel                           │
│                   ◄───┤ 1 ├───►                             │
│                       └───┘                                 │
│           ┌───┐               ┌───┐                         │
│     Gabel │   │               │   │ Gabel                   │
│       ◄───┤ 5 │     TISCH     │ 2 ├───►                     │
│           └───┘               └───┘                         │
│                    Teller                                   │
│           ┌───┐               ┌───┐                         │
│     Gabel │   │               │   │ Gabel                   │
│       ◄───┤ 4 │               │ 3 ├───►                     │
│           └───┘               └───┘                         │
│                                                             │
│   Regel: Zum Essen braucht man ZWEI Gabeln                  │
│                                                             │
│   Deadlock: Alle nehmen ihre linke Gabel →                  │
│             Alle warten auf die rechte Gabel                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

## Zusammenhänge

- [[04-01-Kritische-Abschnitte|Kritische Abschnitte]] → Deadlocks bei Synchronisation
- [[04-02-Semaphore|Semaphore]] → Falsche Nutzung → Deadlocks
- [[03-01-Prozessmodell|Prozessmodell]] → Prozesse als Beteiligte an Deadlocks

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Die vier Coffman-Bedingungen (auswendig!)
> - Unterschied Prevention, Avoidance, Detection, Ignorance
> - Banker's Algorithm verstehen und anwenden
> - Resource Allocation Graph interpretieren

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen und erklären Sie die vier notwendigen Bedingungen für einen Deadlock!
> 2. Wie kann man Deadlocks durch Ressourcen-Ordnung verhindern?
> 3. Erklären Sie den Banker's Algorithm anhand eines Beispiels!
> 4. Gegeben ein Resource Allocation Graph: Liegt ein Deadlock vor?
> 5. Welche Strategien gibt es zur Behandlung von Deadlocks?

> [!tip] **Merkhilfen**
> - **4 Bedingungen**: "MuHNo-Cy" = Mutual exclusion, Hold&wait, No preemption, Circular wait
> - **Banker's Algorithm** = "Vorsichtiger Bankier gibt nur Kredit, wenn Rückzahlung sicher"
> - **Philosophen** = "Alle greifen gleichzeitig zur linken Gabel → keiner kann essen"

---
author: Andreas Hümmer

## Weiterführende Ressourcen

> [!note] **Workshop**
> MOSS Deadlock Simulator:
> http://www.ontko.com/moss/deadlock/user_guide.html

> [!note] **Beispielcode**
> https://github.com/KR-Ravindra/Deadlock-Simulation

---
author: Andreas Hümmer

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- Coffman et al.: "System Deadlocks" (1971)
