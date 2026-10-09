---
author: Andreas Hümmer
title: Semaphore
tags:
  - content
  - bs
  - synchronisation
  - semaphore
  - mutex
  - producer-consumer
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Semaphore

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept von Semaphoren verstehen
> - Die Operationen P (wait) und V (signal) erklären können
> - Binäre und Counting Semaphore unterscheiden
> - Das Producer-Consumer Problem mit Semaphoren lösen können
> - Die Gefahren bei falscher Semaphor-Verwendung kennen

---

## Definition

> [!quote] **Formale Definition**
> Ein **Semaphor** ist eine Synchronisationsprimitive mit einem Integer-Zähler und zwei **atomaren** Operationen: **P** (wait/down) und **V** (signal/up).

---

## Operationen

```
┌─────────────────────────────────────────────────────────────┐
│              SEMAPHOR-OPERATIONEN                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   P (wait/down/proberen):          V (signal/up/verhogen): │
│   ┌───────────────────────┐        ┌───────────────────────┐│
│   │ if (S > 0) {          │        │ S = S + 1;            ││
│   │     S = S - 1;        │        │ // Wartende Prozesse  ││
│   │ } else {              │        │ // aufwecken          ││
│   │     // blockieren     │        └───────────────────────┘│
│   │     // und warten     │                                 │
│   │ }                     │        (atomar, nicht           │
│   └───────────────────────┘         unterbrechbar!)         │
│                                                             │
│   (atomar, nicht                                            │
│    unterbrechbar!)                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

> [!note] **Herkunft der Namen**
> - **P** = "proberen" (niederländisch: "versuchen")
> - **V** = "verhogen" (niederländisch: "erhöhen")
> - Erfunden von Edsger Dijkstra

---

## Typen von Semaphoren

### 1. Binärer Semaphor (Mutex)

Wert kann nur **0** oder **1** sein → gegenseitiger Ausschluss.

```
┌─────────────────────────────────────────────────────────────┐
│              BINÄRER SEMAPHOR (MUTEX)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Semaphore mutex = 1;      // Initialisiert mit 1         │
│                                                             │
│   Prozess A:                Prozess B:                      │
│   ┌──────────────────┐      ┌──────────────────┐           │
│   │ P(mutex)         │      │ P(mutex)         │           │
│   │   // krit. Abschn│      │   // wartet...   │           │
│   │ V(mutex)         │      │   // krit. Abschn│           │
│   └──────────────────┘      │ V(mutex)         │           │
│                             └──────────────────┘           │
│                                                             │
│   mutex = 1: frei (ein Prozess kann eintreten)             │
│   mutex = 0: belegt (andere müssen warten)                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. Counting Semaphor

Wert kann **beliebig nicht-negativ** sein → begrenzte Ressourcen verwalten.

```
┌─────────────────────────────────────────────────────────────┐
│              COUNTING SEMAPHOR                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Semaphore pool = 5;   // 5 verfügbare Ressourcen         │
│                                                             │
│   Prozess will Ressource:   Prozess gibt Ressource zurück: │
│   ┌──────────────────────┐  ┌──────────────────────┐       │
│   │ P(pool)              │  │ // Nutzung beendet   │       │
│   │ // Ressource nutzen  │  │ V(pool)              │       │
│   └──────────────────────┘  └──────────────────────┘       │
│                                                             │
│   pool = 5: alle 5 frei                                    │
│   pool = 3: 2 belegt, 3 frei                               │
│   pool = 0: alle belegt → neue Anfragen warten             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Producer-Consumer Problem

Klassisches Synchronisationsproblem: Produzenten erzeugen Daten, Konsumenten verarbeiten sie.

```
┌─────────────────────────────────────────────────────────────┐
│              PRODUCER-CONSUMER MIT SEMAPHOREN               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Semaphore mutex = 1;     // Zugriff auf Puffer           │
│   Semaphore empty = N;     // Anzahl freier Plätze         │
│   Semaphore full = 0;      // Anzahl belegter Plätze       │
│                                                             │
│   PRODUCER:                 CONSUMER:                       │
│   ┌─────────────────────┐   ┌─────────────────────┐        │
│   │ while (true) {      │   │ while (true) {      │        │
│   │   item = produce(); │   │   P(full);          │        │
│   │   P(empty);         │   │   P(mutex);         │        │
│   │   P(mutex);         │   │   item = remove();  │        │
│   │   insert(item);     │   │   V(mutex);         │        │
│   │   V(mutex);         │   │   V(empty);         │        │
│   │   V(full);          │   │   consume(item);    │        │
│   │ }                   │   │ }                   │        │
│   └─────────────────────┘   └─────────────────────┘        │
│                                                             │
│   Puffer:  [■][■][■][□][□]    (N=5, 3 belegt, 2 frei)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Übungsbeispiel: Waschraum-Problem

> [!example] **Aufgabe**
> Ein Waschraum fasst maximal 6 Personen. Im Waschraum befinden sich 4 Toiletten, jede für eine Person. Stellen Sie sicher, dass nie mehr als die angegebene Personenzahl im Waschraum bzw. in den Toiletten ist.

```
┌─────────────────────────────────────────────────────────────┐
│              WASCHRAUM-PROBLEM                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────────────────────────────────────────┐     │
│   │             WASCHRAUM (max 6)                    │     │
│   │   ┌────┐  ┌────┐  ┌────┐  ┌────┐                │     │
│   │   │ T1 │  │ T2 │  │ T3 │  │ T4 │                │     │
│   │   │    │  │    │  │    │  │    │   Toiletten    │     │
│   │   └────┘  └────┘  └────┘  └────┘   (max 4)      │     │
│   └──────────────────────────────────────────────────┘     │
│                                                             │
│   Semaphore SW = 6;    // Waschraum-Kapazität              │
│   Semaphore ST = 4;    // Toiletten-Kapazität              │
│                                                             │
│   Person betritt:                                           │
│   ┌──────────────────┐                                      │
│   │ P(SW)            │  // Waschraum betreten              │
│   │ P(ST)            │  // Toilette betreten               │
│   │ // ... benutzen  │                                      │
│   │ V(ST)            │  // Toilette verlassen              │
│   │ V(SW)            │  // Waschraum verlassen             │
│   └──────────────────┘                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Gefahren bei Semaphoren

> [!danger] **Achtung: Deadlock-Gefahr!**
> Bei falscher Reihenfolge der P-Operationen können Deadlocks entstehen!

```
┌─────────────────────────────────────────────────────────────┐
│              DEADLOCK DURCH FALSCHE REIHENFOLGE             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Semaphore A = 1, B = 1;                                  │
│                                                             │
│   Prozess 1:                Prozess 2:                      │
│   ┌──────────────────┐      ┌──────────────────┐           │
│   │ P(A)             │      │ P(B)             │           │
│   │ P(B)  ← wartet   │      │ P(A)  ← wartet   │           │
│   │ ...              │      │ ...              │           │
│   │ V(B)             │      │ V(A)             │           │
│   │ V(A)             │      │ V(B)             │           │
│   └──────────────────┘      └──────────────────┘           │
│                                                             │
│   → Prozess 1 hält A, wartet auf B                         │
│   → Prozess 2 hält B, wartet auf A                         │
│   → DEADLOCK!                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Regeln zur Vermeidung

1. **Immer gleiche Reihenfolge** bei mehreren Semaphoren
2. **P und V immer paarweise** verwenden
3. **Nicht im kritischen Abschnitt** blockieren

---

## Zusammenhänge

- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Semaphore lösen dieses Problem
- [[03-Deadlocks|Deadlocks]] → Können durch falsche Semaphor-Nutzung entstehen
- [[03-Threads|Threads]] → Nutzen Semaphore zur Synchronisation

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - P und V Operationen verstehen und anwenden
> - Binärer vs. Counting Semaphor
> - Producer-Consumer Problem lösen
> - Deadlock-Gefahren erkennen

> [!question] **Häufige Prüfungsfragen**
> 1. Was sind die Operationen P und V bei Semaphoren?
> 2. Was ist der Unterschied zwischen binären und Counting Semaphoren?
> 3. Lösen Sie das Producer-Consumer Problem mit Semaphoren!
> 4. Wie kann es bei Semaphoren zu einem Deadlock kommen?
> 5. Gegeben ein Szenario: Welche Semaphore mit welchen Initialwerten werden benötigt?

> [!tip] **Merkhilfen**
> - **P** = "Passieren wollen" (runter zählen, ggf. warten)
> - **V** = "Verlassen" (hoch zählen, andere wecken)
> - **Mutex** = "MUTual EXclusion" (gegenseitiger Ausschluss)
> - **Producer-Consumer**: "empty" + "full" + "mutex" = die drei Semaphore

---

## Weiterführende Ressourcen

> [!note] **Workshop**
> MOSS Deadlock Simulator:
> http://www.ontko.com/moss/deadlock/user_guide.html

> [!note] **Beispielcode**
> https://github.com/KR-Ravindra/Deadlock-Simulation

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- Dijkstra: "Cooperating Sequential Processes" (1965)
